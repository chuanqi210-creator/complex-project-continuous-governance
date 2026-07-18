#!/usr/bin/env python3
"""Check the active Complex architecture re-baseline."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REBASELINE = ROOT / "docs" / "active-architecture-rebaseline.json"
MATURITY = ROOT / "docs" / "mechanism-maturity.json"
REFERENCES = ROOT / "docs" / "reference-implementation-evidence.json"
EVAL_CHECKER = ROOT / "tools" / "check_eval_records.py"
EVAL_RECORDS = (ROOT / "docs" / "evals" / "records").resolve()

REQUIRED_OBJECTS = {
    "runtime_architecture",
    "public_language",
    "change_governance",
    "evaluation_system",
}
ALLOWED_DECISIONS = {"keep", "merge", "demote", "retire"}
CLAIM_VOCABULARY = {"illustrates", "screens", "reproduces", "compares", "validates"}
REQUIRED_OBJECT_FIELDS = {
    "id",
    "external_reference_ids",
    "inspected_artifacts",
    "provisional_micro_contracts",
    "rejected_patterns",
    "not_transferable",
    "repository_changes",
    "next_validation",
}
REQUIRED_MECHANISM_FIELDS = {
    "mechanism_id",
    "decision",
    "normative_role_before",
    "normative_role_after",
    "evidence_status_before",
    "evidence_status_after",
    "external_reference_ids",
    "rationale",
    "next_validation",
}


def fail(message: str) -> None:
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def load(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(f"missing file: {path}")
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {path}: {exc}")
    if not isinstance(value, dict):
        fail(f"expected object in {path}")
    return value


def text(value: Any, label: str) -> None:
    if not isinstance(value, str) or not value.strip():
        fail(f"{label} must be non-empty text")


def text_list(value: Any, label: str) -> None:
    if not isinstance(value, list) or not value:
        fail(f"{label} must be a non-empty list")
    if not all(isinstance(item, str) and item.strip() for item in value):
        fail(f"{label} must contain non-empty text")


def main() -> None:
    eval_check = subprocess.run(
        [sys.executable, str(EVAL_CHECKER)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if eval_check.returncode != 0:
        fail(f"eval records failed validation: {eval_check.stderr.strip() or eval_check.stdout.strip()}")

    rebaseline = load(REBASELINE)
    maturity = load(MATURITY)
    references = load(REFERENCES)

    if set(rebaseline.get("allowed_decisions", [])) != ALLOWED_DECISIONS:
        fail("allowed_decisions must match the canonical decision set")
    if set(rebaseline.get("evidence_claim_vocabulary", {})) != CLAIM_VOCABULARY:
        fail("evidence_claim_vocabulary must define the canonical five claims")

    reference_ids = {
        str(reference.get("id"))
        for reference in references.get("references", [])
        if isinstance(reference, dict)
    }
    active_mechanisms = {
        str(mechanism.get("id")): mechanism
        for mechanism in maturity.get("mechanisms", [])
        if isinstance(mechanism, dict) and mechanism.get("normative_role") != "retired"
    }

    objects = rebaseline.get("object_rebaselines")
    if not isinstance(objects, list):
        fail("object_rebaselines must be a list")
    object_ids: set[str] = set()
    for obj in objects:
        if not isinstance(obj, dict):
            fail("each object re-baseline must be an object")
        missing = REQUIRED_OBJECT_FIELDS - set(obj)
        if missing:
            fail(f"object {obj.get('id', '<unknown>')} missing fields: {sorted(missing)}")
        object_id = str(obj["id"])
        if object_id in object_ids:
            fail(f"duplicate object re-baseline: {object_id}")
        object_ids.add(object_id)
        for field in [
            "external_reference_ids",
            "inspected_artifacts",
            "provisional_micro_contracts",
            "rejected_patterns",
            "repository_changes",
        ]:
            text_list(obj[field], f"{object_id}.{field}")
        for field in ["not_transferable", "next_validation"]:
            text(obj[field], f"{object_id}.{field}")
        unknown_refs = set(obj["external_reference_ids"]) - reference_ids
        if unknown_refs:
            fail(f"{object_id} links unknown references: {sorted(unknown_refs)}")
    if object_ids != REQUIRED_OBJECTS:
        fail(f"object re-baseline must cover exactly {sorted(REQUIRED_OBJECTS)}")

    rows = rebaseline.get("mechanism_rebaselines")
    if not isinstance(rows, list):
        fail("mechanism_rebaselines must be a list")
    row_ids: set[str] = set()
    for row in rows:
        if not isinstance(row, dict):
            fail("each mechanism re-baseline must be an object")
        missing = REQUIRED_MECHANISM_FIELDS - set(row)
        if missing:
            fail(f"mechanism row {row.get('mechanism_id', '<unknown>')} missing fields: {sorted(missing)}")
        mechanism_id = str(row["mechanism_id"])
        if mechanism_id in row_ids:
            fail(f"duplicate mechanism re-baseline: {mechanism_id}")
        row_ids.add(mechanism_id)
        if row["decision"] not in ALLOWED_DECISIONS:
            fail(f"{mechanism_id}.decision is invalid")
        text_list(row["external_reference_ids"], f"{mechanism_id}.external_reference_ids")
        unknown_refs = set(row["external_reference_ids"]) - reference_ids
        if unknown_refs:
            fail(f"{mechanism_id} links unknown references: {sorted(unknown_refs)}")
        if mechanism_id not in active_mechanisms:
            fail(f"mechanism re-baseline links inactive or unknown mechanism: {mechanism_id}")
        if row["normative_role_after"] != active_mechanisms[mechanism_id].get("normative_role"):
            fail(f"{mechanism_id}.normative_role_after does not match maturity registry")
        if row["evidence_status_after"] != active_mechanisms[mechanism_id].get("evidence_status"):
            fail(f"{mechanism_id}.evidence_status_after does not match maturity registry")
        text(row["rationale"], f"{mechanism_id}.rationale")
        text(row["next_validation"], f"{mechanism_id}.next_validation")
    if row_ids != set(active_mechanisms):
        missing = sorted(set(active_mechanisms) - row_ids)
        extra = sorted(row_ids - set(active_mechanisms))
        fail(f"active mechanism coverage mismatch missing={missing} extra={extra}")

    consolidations = rebaseline.get("consolidations")
    if not isinstance(consolidations, list) or not consolidations:
        fail("consolidations must be a non-empty list")
    removed_ids: set[str] = set()
    for item in consolidations:
        if not isinstance(item, dict):
            fail("each consolidation must be an object")
        for field in ["removed_id", "merged_into", "reason"]:
            text(item.get(field), f"consolidation.{field}")
        removed_id = str(item["removed_id"])
        if removed_id in removed_ids:
            fail(f"duplicate consolidation: {removed_id}")
        removed_ids.add(removed_id)
        if removed_id in active_mechanisms:
            fail(f"consolidated mechanism is still active: {removed_id}")
        if item["merged_into"] not in active_mechanisms:
            fail(f"consolidation target is not active: {item['merged_into']}")

    for mechanism_id, mechanism in active_mechanisms.items():
        if mechanism.get("evidence_status") != "validated":
            continue
        eval_paths = {
            item.removeprefix("eval_record:")
            for item in mechanism.get("internal_evidence", [])
            if isinstance(item, str) and item.startswith("eval_record:")
        }
        if len(eval_paths) < 2:
            fail(f"{mechanism_id} needs at least two linked eval records before validated")
        distinct_real_samples: set[tuple[str, ...]] = set()
        for relative in eval_paths:
            record_path = (ROOT / relative).resolve()
            if record_path.parent != EVAL_RECORDS or record_path.suffix != ".json":
                fail(f"{mechanism_id} links eval evidence outside docs/evals/records: {relative}")
            record = load(record_path)
            if record.get("status") != "reviewed":
                fail(f"{mechanism_id} links non-reviewed validation record: {relative}")
            comparison = record.get("comparison")
            if not isinstance(comparison, dict) or comparison.get("decision") != "transfer_candidate":
                fail(f"{mechanism_id} validation record does not select the candidate: {relative}")
            if comparison.get("human_preference") != "candidate":
                fail(f"{mechanism_id} validation record lacks candidate human preference: {relative}")
            case = record.get("eval_case")
            if not isinstance(case, dict) or case.get("sample_origin") not in {"real_project", "redacted_real_project"}:
                fail(f"{mechanism_id} validation record is not a real-project sample: {relative}")
            if mechanism_id not in case.get("mechanism_ids", []):
                fail(f"{mechanism_id} validation record evaluates a different mechanism: {relative}")
            sample_ids = case.get("sample_ids")
            if not isinstance(sample_ids, list):
                fail(f"{mechanism_id} validation record has invalid sample IDs: {relative}")
            distinct_real_samples.add(tuple(sorted(map(str, sample_ids))))
        if len(distinct_real_samples) < 2:
            fail(f"{mechanism_id} validated status needs at least two distinct real-project sample sets")

    print(
        "ok "
        f"objects={len(object_ids)} "
        f"mechanisms={len(row_ids)} "
        f"consolidated={len(removed_ids)} "
        f"references={len(reference_ids)}"
    )


if __name__ == "__main__":
    main()
