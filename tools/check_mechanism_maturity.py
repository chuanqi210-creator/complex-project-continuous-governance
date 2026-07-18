#!/usr/bin/env python3
"""Check Complex mechanism maturity registry consistency."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "docs" / "mechanism-maturity.json"
CASES = ROOT / "docs" / "behavior-regression-cases.json"
RULES = ROOT / "docs" / "behavior-transcript-review-rules.json"
EXAMPLES = ROOT / "docs" / "examples"
REFERENCES = ROOT / "docs" / "reference-implementation-evidence.json"

ALLOWED_NORMATIVE_ROLES = {"core", "supporting_practice", "conditional_extension", "retired"}
ALLOWED_EVIDENCE_STATUSES = {"screened", "tested", "validated"}
ALLOWED_ENGINEERING_LAYERS = {"prompt", "context", "harness", "loop"}
REQUIRED_MECHANISM_FIELDS = {
    "id",
    "name",
    "normative_role",
    "evidence_status",
    "engineering_layers",
    "summary",
    "external_basis",
    "internal_evidence",
    "linked_behavior_cases",
    "linked_examples",
    "promotion_rule",
    "demotion_trigger",
    "refresh_trigger",
}


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
        fail(f"expected object in {path}")
    return data


def require_non_empty_list(value: Any, label: str) -> None:
    if not isinstance(value, list) or not value:
        fail(f"{label} must be a non-empty list")


def main() -> None:
    registry = load_json(REGISTRY)
    pack = load_json(CASES)
    rules = load_json(RULES)
    references = load_json(REFERENCES)

    mechanisms = registry.get("mechanisms")
    if not isinstance(mechanisms, list) or not mechanisms:
        fail("registry.mechanisms must be a non-empty list")

    cases = pack.get("cases")
    if not isinstance(cases, list) or not cases:
        fail("behavior pack cases must be a non-empty list")

    case_ids = {str(case.get("case_id")) for case in cases if isinstance(case, dict)}
    rule_ids = set(rules.get("case_rules", {}))
    example_ids = {path.name for path in EXAMPLES.iterdir() if path.is_dir()}
    reference_ids = {
        str(reference.get("id"))
        for reference in references.get("references", [])
        if isinstance(reference, dict)
    }

    mechanism_ids: set[str] = set()
    registry_case_links: dict[str, set[str]] = {}
    role_counts = {role: 0 for role in ALLOWED_NORMATIVE_ROLES}
    evidence_counts = {status: 0 for status in ALLOWED_EVIDENCE_STATUSES}
    for mechanism in mechanisms:
        if not isinstance(mechanism, dict):
            fail("each mechanism must be an object")
        missing = REQUIRED_MECHANISM_FIELDS - set(mechanism)
        if missing:
            fail(f"{mechanism.get('id', '<unknown>')} missing fields: {sorted(missing)}")

        mechanism_id = str(mechanism["id"])
        if mechanism_id in mechanism_ids:
            fail(f"duplicate mechanism id: {mechanism_id}")
        mechanism_ids.add(mechanism_id)

        normative_role = str(mechanism["normative_role"])
        evidence_status = str(mechanism["evidence_status"])
        if normative_role not in ALLOWED_NORMATIVE_ROLES:
            fail(f"{mechanism_id} has invalid normative_role: {normative_role}")
        if evidence_status not in ALLOWED_EVIDENCE_STATUSES:
            fail(f"{mechanism_id} has invalid evidence_status: {evidence_status}")
        role_counts[normative_role] += 1
        evidence_counts[evidence_status] += 1

        layers = mechanism["engineering_layers"]
        require_non_empty_list(layers, f"{mechanism_id}.engineering_layers")
        unknown_layers = sorted(set(map(str, layers)) - ALLOWED_ENGINEERING_LAYERS)
        if unknown_layers:
            fail(f"{mechanism_id} has invalid engineering layers: {unknown_layers}")
        if len(layers) != len(set(map(str, layers))):
            fail(f"{mechanism_id}.engineering_layers contains duplicates")

        for key in ["external_basis", "internal_evidence", "linked_behavior_cases", "linked_examples"]:
            require_non_empty_list(mechanism[key], f"{mechanism_id}.{key}")

        unknown_references = sorted(set(map(str, mechanism["external_basis"])) - reference_ids)
        if unknown_references:
            fail(f"{mechanism_id} links unknown external references: {unknown_references}")

        unknown_cases = sorted(set(map(str, mechanism["linked_behavior_cases"])) - case_ids)
        if unknown_cases:
            fail(f"{mechanism_id} links unknown behavior cases: {unknown_cases}")
        missing_rules = sorted(set(map(str, mechanism["linked_behavior_cases"])) - rule_ids)
        if missing_rules:
            fail(f"{mechanism_id} links cases without transcript rules: {missing_rules}")
        registry_case_links[mechanism_id] = set(map(str, mechanism["linked_behavior_cases"]))
        unknown_examples = sorted(set(map(str, mechanism["linked_examples"])) - example_ids)
        if unknown_examples:
            fail(f"{mechanism_id} links unknown examples: {unknown_examples}")

        for text_field in ["summary", "promotion_rule", "demotion_trigger", "refresh_trigger"]:
            if not str(mechanism[text_field]).strip():
                fail(f"{mechanism_id}.{text_field} must be non-empty")

    case_declared_links: dict[str, set[str]] = {mechanism_id: set() for mechanism_id in mechanism_ids}
    for case in cases:
        case_id = str(case.get("case_id"))
        linked = case.get("linked_mechanisms")
        require_non_empty_list(linked, f"{case_id}.linked_mechanisms")
        unknown = sorted(set(map(str, linked)) - mechanism_ids)
        if unknown:
            fail(f"{case_id} links unknown mechanisms: {unknown}")
        for mechanism_id in map(str, linked):
            case_declared_links[mechanism_id].add(case_id)

    for mechanism_id in sorted(mechanism_ids):
        if registry_case_links[mechanism_id] != case_declared_links[mechanism_id]:
            missing_from_registry = sorted(case_declared_links[mechanism_id] - registry_case_links[mechanism_id])
            missing_from_cases = sorted(registry_case_links[mechanism_id] - case_declared_links[mechanism_id])
            fail(
                f"{mechanism_id} behavior links are not bidirectional; "
                + f"missing_from_registry={missing_from_registry} "
                + f"missing_from_cases={missing_from_cases}"
            )

    if role_counts["conditional_extension"] == 0:
        fail("expected at least one conditional extension")
    if role_counts["core"] == 0:
        fail("expected at least one core mechanism")

    print(
        "ok "
        + f"mechanisms={len(mechanism_ids)} "
        + " ".join(f"role_{role}={role_counts[role]}" for role in sorted(role_counts))
        + " "
        + " ".join(f"evidence_{status}={evidence_counts[status]}" for status in sorted(evidence_counts))
    )


if __name__ == "__main__":
    main()
