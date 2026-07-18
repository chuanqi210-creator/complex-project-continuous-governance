#!/usr/bin/env python3
"""Validate implementation-level external reference evidence."""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "docs" / "reference-implementation-evidence.json"
ALLOWED_LAYERS = {"prompt", "context", "harness", "loop"}
CANONICAL_TRANSFER_STATUSES = [
    "discovered",
    "implementation_inspected",
    "reproduced",
    "comparatively_evaluated",
    "transferred",
    "validated_in_complex",
]
PLACEHOLDER_PREFIXES = ("not run", "none", "pending", "tbd", "unknown", "not yet")
REQUIRED_FIELDS = {
    "id",
    "repository",
    "url",
    "pinned_commit",
    "observed_at",
    "stars_snapshot",
    "engineering_layers",
    "original_goal",
    "original_non_goals",
    "state_or_data_path",
    "control_path",
    "inspected_artifacts",
    "operating_constraints",
    "failure_boundaries",
    "artifact_revision_provenance",
    "implementation_evidence",
    "upstream_validation",
    "candidate_transfer",
    "rejected",
    "not_transferable",
    "transfer_status",
    "reproduction_command",
    "reproduction_result",
    "local_fixture",
    "same_task_comparison",
    "comparison_metrics",
    "comparison_artifacts",
    "transfer_artifact",
    "complex_validation_evidence",
    "complex_validation_records",
    "rollback_route",
    "refresh_trigger",
    "next_validation",
}


def fail(message: str) -> None:
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def load() -> dict[str, Any]:
    try:
        data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(f"missing file: {REGISTRY}")
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {REGISTRY}: {exc}")
    if not isinstance(data, dict):
        fail("reference evidence registry must be an object")
    return data


def require_text(value: Any, label: str) -> None:
    if not isinstance(value, str) or not value.strip():
        fail(f"{label} must be non-empty text")


def require_text_list(value: Any, label: str) -> None:
    if not isinstance(value, list) or not value or not all(isinstance(item, str) and item.strip() for item in value):
        fail(f"{label} must be a non-empty text list")


def is_placeholder(value: Any) -> bool:
    return str(value).strip().lower().startswith(PLACEHOLDER_PREFIXES)


def main() -> None:
    data = load()
    allowed = data.get("allowed_transfer_statuses")
    if allowed != CANONICAL_TRANSFER_STATUSES:
        fail("allowed_transfer_statuses must match the canonical ordered transfer ladder")
    allowed_statuses = set(CANONICAL_TRANSFER_STATUSES)
    status_meanings = data.get("status_meanings")
    if not isinstance(status_meanings, dict) or set(status_meanings) != allowed_statuses:
        fail("status_meanings must define every allowed transfer status exactly once")

    references = data.get("references")
    if not isinstance(references, list) or not references:
        fail("references must be a non-empty list")

    ids: set[str] = set()
    status_counts: Counter[str] = Counter()
    covered_layers: set[str] = set()
    for reference in references:
        if not isinstance(reference, dict):
            fail("each reference must be an object")
        missing = REQUIRED_FIELDS - set(reference)
        if missing:
            fail(f"{reference.get('id', '<unknown>')} missing fields: {sorted(missing)}")

        reference_id = str(reference["id"])
        if reference_id in ids:
            fail(f"duplicate reference id: {reference_id}")
        ids.add(reference_id)

        repository = str(reference["repository"])
        if not re.fullmatch(r"[^/\s]+/[^/\s]+", repository):
            fail(f"{reference_id}.repository must be owner/name")
        if reference["url"] != f"https://github.com/{repository}":
            fail(f"{reference_id}.url does not match repository")
        if not re.fullmatch(r"[0-9a-f]{40}", str(reference["pinned_commit"])):
            fail(f"{reference_id}.pinned_commit must be a full Git SHA")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(reference["observed_at"])):
            fail(f"{reference_id}.observed_at must use YYYY-MM-DD")
        if not isinstance(reference["stars_snapshot"], int) or reference["stars_snapshot"] < 0:
            fail(f"{reference_id}.stars_snapshot must be a non-negative integer")

        layers = reference["engineering_layers"]
        require_text_list(layers, f"{reference_id}.engineering_layers")
        unknown_layers = set(layers) - ALLOWED_LAYERS
        if unknown_layers:
            fail(f"{reference_id} has invalid engineering layers: {sorted(unknown_layers)}")
        covered_layers.update(layers)

        for field in ["inspected_artifacts", "implementation_evidence", "upstream_validation"]:
            require_text_list(reference[field], f"{reference_id}.{field}")
        if len(reference["inspected_artifacts"]) < 2:
            fail(f"{reference_id}.inspected_artifacts must name at least two concrete artifacts")
        if not all("/" in str(item) or "." in str(item) for item in reference["inspected_artifacts"]):
            fail(f"{reference_id}.inspected_artifacts must use concrete repository paths")
        for field in [
            "original_goal",
            "original_non_goals",
            "state_or_data_path",
            "control_path",
            "operating_constraints",
            "failure_boundaries",
            "artifact_revision_provenance",
            "candidate_transfer",
            "rejected",
            "not_transferable",
            "reproduction_result",
            "same_task_comparison",
            "transfer_artifact",
            "complex_validation_evidence",
            "rollback_route",
            "refresh_trigger",
            "next_validation",
        ]:
            require_text(reference[field], f"{reference_id}.{field}")
        if str(reference["pinned_commit"]) not in str(reference["artifact_revision_provenance"]):
            fail(f"{reference_id}.artifact_revision_provenance must cite pinned_commit")
        for field in ["comparison_metrics", "comparison_artifacts", "complex_validation_records"]:
            if not isinstance(reference[field], list):
                fail(f"{reference_id}.{field} must be a list")
            if not all(isinstance(item, str) and item.strip() for item in reference[field]):
                fail(f"{reference_id}.{field} entries must be non-empty text")

        status = str(reference["transfer_status"])
        if status not in allowed_statuses:
            fail(f"{reference_id} has invalid transfer status: {status}")
        status_counts[status] += 1

        fixture = str(reference["local_fixture"])
        command = str(reference["reproduction_command"])
        if status in {"reproduced", "comparatively_evaluated", "transferred", "validated_in_complex"}:
            require_text(command, f"{reference_id}.reproduction_command")
            require_text(fixture, f"{reference_id}.local_fixture")
            if "@latest" in command or re.search(r"--with\s+[A-Za-z0-9_.-]+(?:\s|$)", command):
                fail(f"{reference_id}.reproduction_command must pin package versions")
            if not (ROOT / fixture).is_file():
                fail(f"{reference_id}.local_fixture does not exist: {fixture}")
            if is_placeholder(reference["reproduction_result"]):
                fail(f"{reference_id} cannot be {status} without a concrete reproduction result")
        if status in {"comparatively_evaluated", "transferred", "validated_in_complex"}:
            if is_placeholder(reference["same_task_comparison"]):
                fail(f"{reference_id} cannot be {status} without same-task comparison evidence")
            if not reference["comparison_metrics"] or not reference["comparison_artifacts"]:
                fail(f"{reference_id} cannot be {status} without comparison metrics and artifacts")
        if status in {"transferred", "validated_in_complex"}:
            if is_placeholder(reference["transfer_artifact"]):
                fail(f"{reference_id} cannot be {status} without a transfer artifact")
        if status == "validated_in_complex":
            if is_placeholder(reference["complex_validation_evidence"]):
                fail(f"{reference_id} cannot be validated_in_complex without real Complex evidence")
            if len(reference["complex_validation_records"]) < 2:
                fail(f"{reference_id} needs at least two Complex validation records")

    if covered_layers != ALLOWED_LAYERS:
        fail(f"reference portfolio must cover all four layers, got {sorted(covered_layers)}")
    if status_counts["implementation_inspected"] == 0:
        fail("expected at least one implementation_inspected reference")
    if status_counts["reproduced"] == 0:
        fail("expected at least one reproduced reference")

    print(
        "ok "
        + f"references={len(ids)} "
        + " ".join(f"{status}={status_counts[status]}" for status in sorted(status_counts))
        + f" layers={','.join(sorted(covered_layers))}"
    )


if __name__ == "__main__":
    main()
