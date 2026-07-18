#!/usr/bin/env python3
"""Review a real agent transcript against Complex behavior-case rules.

This tool is intentionally modest. It checks required/forbidden marker groups,
optionally requires normalized structured runtime events, and emits human-review
questions. It does not claim to be a full LLM judge or authenticate event origin.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "docs" / "behavior-regression-cases.json"
RULES = ROOT / "docs" / "behavior-transcript-review-rules.json"
MATURITY = ROOT / "docs" / "mechanism-maturity.json"
EVENT_PREFIX = "COMPLEX_EVENT "


def fail(message: str) -> None:
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def load_json(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(f"missing file: {path}")
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {path}: {exc}")
    if not isinstance(data, dict):
        fail(f"expected JSON object: {path}")
    return data


def known_case_ids() -> set[str]:
    pack = load_json(PACK)
    cases = pack.get("cases")
    if not isinstance(cases, list):
        fail("behavior pack cases must be a list")
    return {str(case.get("case_id")) for case in cases if isinstance(case, dict)}


def cases_by_id() -> dict[str, dict[str, Any]]:
    pack = load_json(PACK)
    cases = pack.get("cases")
    if not isinstance(cases, list):
        fail("behavior pack cases must be a list")
    return {str(case.get("case_id")): case for case in cases if isinstance(case, dict)}


def mechanisms_by_id() -> dict[str, dict[str, Any]]:
    maturity = load_json(MATURITY)
    mechanisms = maturity.get("mechanisms")
    if not isinstance(mechanisms, list):
        fail("mechanism maturity registry mechanisms must be a list")
    return {str(mechanism.get("id")): mechanism for mechanism in mechanisms if isinstance(mechanism, dict)}


def extract_text_from_json(data: Any) -> str:
    if isinstance(data, str):
        return data
    if isinstance(data, list):
        return "\n".join(extract_text_from_json(item) for item in data)
    if not isinstance(data, dict):
        return ""

    if isinstance(data.get("assistant_response"), str):
        return data["assistant_response"]
    if isinstance(data.get("transcript"), str):
        return data["transcript"]
    if isinstance(data.get("text"), str):
        return data["text"]

    messages = data.get("messages")
    if isinstance(messages, list):
        parts = []
        for message in messages:
            if not isinstance(message, dict):
                continue
            role = str(message.get("role", ""))
            content = message.get("content", "")
            if isinstance(content, str):
                parts.append(f"{role}: {content}")
        return "\n".join(parts)

    return "\n".join(extract_text_from_json(value) for value in data.values())


def load_transcript(args: argparse.Namespace) -> str:
    if args.text_file:
        return Path(args.text_file).read_text(encoding="utf-8")
    if args.json_file:
        return extract_text_from_json(load_json(Path(args.json_file)))
    if args.stdin:
        return sys.stdin.read()
    fail("provide --text-file, --json-file, or --stdin")


def marker_group_hit(text: str, group: dict[str, Any]) -> tuple[bool, list[str]]:
    markers = group.get("any")
    if not isinstance(markers, list) or not markers:
        fail(f"marker group missing non-empty any list: {group}")
    hits = [str(marker) for marker in markers if str(marker).lower() in text.lower()]
    return bool(hits), hits


def extract_structured_events(text: str) -> tuple[list[dict[str, Any]], list[str]]:
    events: list[dict[str, Any]] = []
    errors: list[str] = []
    for line_number, line in enumerate(text.splitlines(), start=1):
        stripped = line.strip()
        if not stripped.startswith(EVENT_PREFIX):
            continue
        payload = stripped.removeprefix(EVENT_PREFIX)
        try:
            event = json.loads(payload)
        except json.JSONDecodeError as exc:
            errors.append(f"line {line_number}: {exc.msg}")
            continue
        if not isinstance(event, dict):
            errors.append(f"line {line_number}: event must be an object")
            continue
        events.append(event)
    return events, errors


def event_matches(event: dict[str, Any], expected: dict[str, Any]) -> bool:
    for key, value in expected.items():
        if key.endswith("_required"):
            event_key = key.removesuffix("_required")
            if value and not event.get(event_key):
                return False
            continue
        actual = event.get(key)
        if isinstance(value, str):
            if str(actual).lower() != value.lower():
                return False
        elif actual != value:
            return False
    return True


def event_group_hit(events: list[dict[str, Any]], group: dict[str, Any]) -> tuple[bool, list[dict[str, Any]]]:
    alternatives = group.get("any")
    if not isinstance(alternatives, list) or not alternatives:
        fail(f"event group missing non-empty any list: {group}")
    hits = [
        event
        for event in events
        if any(isinstance(expected, dict) and event_matches(event, expected) for expected in alternatives)
    ]
    return bool(hits), hits


def review(case_id: str, transcript: str) -> dict[str, Any]:
    rules_doc = load_json(RULES)
    rules_by_case = rules_doc.get("case_rules")
    if not isinstance(rules_by_case, dict):
        fail("rules file must contain case_rules object")

    cases = cases_by_id()
    case_ids = set(cases)
    if case_id not in case_ids:
        fail(f"unknown case_id: {case_id}")
    if case_id not in rules_by_case:
        fail(f"missing transcript review rules for case_id: {case_id}")

    rules = rules_by_case[case_id]
    linked_mechanism_ids = [str(item) for item in cases[case_id].get("linked_mechanisms", [])]
    mechanism_lookup = mechanisms_by_id()
    linked_mechanisms = [
        {
            "id": mechanism_id,
            "status": mechanism_lookup.get(mechanism_id, {}).get("status", "unknown"),
            "name": mechanism_lookup.get(mechanism_id, {}).get("name", mechanism_id),
        }
        for mechanism_id in linked_mechanism_ids
    ]
    required_groups = rules.get("required_marker_groups", [])
    forbidden_groups = rules.get("forbidden_marker_groups", [])
    minimum_required = int(rules.get("minimum_required_groups", len(required_groups)))
    mandatory_required_labels = {
        str(label) for label in rules.get("mandatory_required_labels", [])
    }
    structured_events, event_parse_errors = extract_structured_events(transcript)
    required_event_groups = rules.get("required_event_groups", [])

    required_results = []
    for group in required_groups:
        hit, hits = marker_group_hit(transcript, group)
        required_results.append(
            {
                "label": group.get("label", ""),
                "passed": hit,
                "hits": hits,
            }
        )

    forbidden_results = []
    for group in forbidden_groups:
        hit, hits = marker_group_hit(transcript, group)
        forbidden_results.append(
            {
                "label": group.get("label", ""),
                "failed": hit,
                "hits": hits,
            }
        )

    required_event_results = []
    for group in required_event_groups:
        hit, hits = event_group_hit(structured_events, group)
        required_event_results.append(
            {
                "label": group.get("label", ""),
                "passed": hit,
                "hits": hits,
            }
        )

    required_passed = sum(1 for item in required_results if item["passed"])
    missing_mandatory_labels = sorted(
        item["label"]
        for item in required_results
        if item["label"] in mandatory_required_labels and not item["passed"]
    )
    forbidden_failed = [item for item in forbidden_results if item["failed"]]
    passed = (
        required_passed >= minimum_required
        and not missing_mandatory_labels
        and not forbidden_failed
        and all(item["passed"] for item in required_event_results)
        and not event_parse_errors
    )

    return {
        "case_id": case_id,
        "passed": passed,
        "required_passed": required_passed,
        "required_total": len(required_results),
        "minimum_required_groups": minimum_required,
        "mandatory_required_labels": sorted(mandatory_required_labels),
        "missing_mandatory_labels": missing_mandatory_labels,
        "required_results": required_results,
        "structured_event_count": len(structured_events),
        "event_parse_errors": event_parse_errors,
        "required_event_results": required_event_results,
        "forbidden_results": forbidden_results,
        "human_review_questions": rules.get("human_review_questions", []),
        "linked_mechanisms": linked_mechanisms,
        "outcome_review_template": {
            "human_passed": None,
            "outcome_passed": None,
            "outcome_evidence": "",
            "trajectory_diagnosis": "",
            "failure_layer": "prompt / context / harness / loop / model / none / uncertain",
            "auto_progressed": None,
            "forward_artifact_created": None,
            "user_correction_count": None,
            "main_failure_if_any": "",
            "mechanism_maturity_change": "none / candidate_to_tested / tested_to_validated / demote / retire",
        },
    }


def validate_rules() -> dict[str, Any]:
    rules_doc = load_json(RULES)
    rules_by_case = rules_doc.get("case_rules")
    if not isinstance(rules_by_case, dict):
        fail("rules file must contain case_rules object")

    case_ids = known_case_ids()
    rule_ids = set(rules_by_case)
    missing_rules = sorted(case_ids - rule_ids)
    extra_rules = sorted(rule_ids - case_ids)
    if missing_rules or extra_rules:
        fail(f"case/rule mismatch: missing={missing_rules}, extra={extra_rules}")

    for case_id, rules in rules_by_case.items():
        for key in ["required_marker_groups", "forbidden_marker_groups", "human_review_questions"]:
            value = rules.get(key)
            if not isinstance(value, list) or not value:
                fail(f"{case_id}.{key} must be a non-empty list")
        minimum_required = rules.get("minimum_required_groups")
        if not isinstance(minimum_required, int) or minimum_required < 1:
            fail(f"{case_id}.minimum_required_groups must be a positive integer")
        if minimum_required > len(rules["required_marker_groups"]):
            fail(f"{case_id}.minimum_required_groups exceeds required_marker_groups length")
        mandatory_required_labels = rules.get("mandatory_required_labels", [])
        if not isinstance(mandatory_required_labels, list):
            fail(f"{case_id}.mandatory_required_labels must be a list when present")
        available_labels = {
            str(group.get("label", "")) for group in rules["required_marker_groups"]
        }
        unknown_mandatory_labels = sorted(
            str(label) for label in mandatory_required_labels
            if str(label) not in available_labels
        )
        if unknown_mandatory_labels:
            fail(
                f"{case_id}.mandatory_required_labels contains unknown labels: "
                f"{unknown_mandatory_labels}"
            )
        required_event_groups = rules.get("required_event_groups", [])
        if not isinstance(required_event_groups, list):
            fail(f"{case_id}.required_event_groups must be a list when present")
        for group in required_event_groups:
            if not isinstance(group, dict) or not str(group.get("label", "")).strip():
                fail(f"{case_id}.required_event_groups entries need a label")
            alternatives = group.get("any")
            if not isinstance(alternatives, list) or not alternatives:
                fail(f"{case_id}.required_event_groups entries need a non-empty any list")
            if not all(isinstance(expected, dict) and expected for expected in alternatives):
                fail(f"{case_id}.required_event_groups alternatives must be non-empty objects")

    return {
        "passed": True,
        "case_count": len(case_ids),
        "rule_count": len(rule_ids),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--case-id")
    parser.add_argument("--text-file")
    parser.add_argument("--json-file")
    parser.add_argument("--stdin", action="store_true")
    parser.add_argument("--validate-rules", action="store_true")
    args = parser.parse_args()

    if args.validate_rules:
        print(json.dumps(validate_rules(), ensure_ascii=False, indent=2))
        return

    if not args.case_id:
        fail("--case-id is required unless --validate-rules is used")
    transcript = load_transcript(args)
    if not transcript.strip():
        fail("transcript is empty")

    result = review(args.case_id, transcript)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
