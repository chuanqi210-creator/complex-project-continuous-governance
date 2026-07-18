#!/usr/bin/env python3
"""Validate the externally calibrated Complex experiment program."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROGRAM = ROOT / "docs" / "evals" / "experiment-program.json"
MATURITY = ROOT / "docs" / "mechanism-maturity.json"
REFERENCES = ROOT / "docs" / "reference-implementation-evidence.json"
CONTRACT_FIXTURES = ROOT / "docs" / "evals" / "bounded-experiment-fixtures.json"
WRITABLE_FIXTURES = ROOT / "docs" / "evals" / "executable-mechanism-fixtures.json"

ALLOWED_LAYERS = {"prompt", "context", "harness", "loop"}
ALLOWED_STATUSES = {"planned", "screened", "completed"}
REQUIRED_GRADERS = {"environment", "trajectory", "human"}
REQUIRED_VALIDITY_CHECKS = {
    "broken_task",
    "reward_hacking",
    "contamination",
    "harness_parity",
    "grader_calibration",
}


def fail(message: str) -> None:
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def load(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(f"missing file: {path.relative_to(ROOT)}")
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")
    if not isinstance(value, dict):
        fail(f"expected JSON object: {path.relative_to(ROOT)}")
    return value


def text(value: object, label: str) -> None:
    if not isinstance(value, str) or not value.strip():
        fail(f"{label} must be non-empty text")


def text_list(value: object, label: str) -> None:
    if not isinstance(value, list) or not value or not all(isinstance(item, str) and item.strip() for item in value):
        fail(f"{label} must be a non-empty text list")


def main() -> None:
    program = load(PROGRAM)
    maturity = load(MATURITY)
    references = load(REFERENCES)
    contract_fixtures = load(CONTRACT_FIXTURES).get("experiments", {})
    writable_fixtures = load(WRITABLE_FIXTURES).get("experiments", {})
    if program.get("version") != "2.0":
        fail("version must be 2.0")

    mechanisms = {
        item.get("id"): item.get("normative_role")
        for item in maturity.get("mechanisms", [])
        if isinstance(item, dict)
    }
    target_roles = set(program.get("suite_scope_roles", []))
    if target_roles != {"core", "conditional_extension"}:
        fail("suite_scope_roles must select core and conditional_extension")
    target_mechanisms = {
        mechanism_id
        for mechanism_id, role in mechanisms.items()
        if role in {"core", "conditional_extension"}
    }
    reference_ids = {
        item.get("id")
        for item in references.get("references", [])
        if isinstance(item, dict)
    }

    method_sources = program.get("method_sources")
    if not isinstance(method_sources, list) or len(method_sources) < 5:
        fail("method_sources must contain at least five concrete sources")
    source_ids: set[str] = set()
    for source in method_sources:
        if not isinstance(source, dict):
            fail("each method source must be an object")
        for field in (
            "id",
            "url",
            "source_type",
            "observed_at",
            "version_pointer",
            "inspected_scope",
            "specific_method",
            "transfer_boundary",
            "refresh_trigger",
        ):
            text(source.get(field), f"method_sources.{field}")
        source_ids.add(source["id"])
    if len(source_ids) != len(method_sources):
        fail("method source ids must be unique")

    experiments = program.get("experiments")
    if not isinstance(experiments, list) or len(experiments) < 3:
        fail("experiments must contain at least three active comparisons")
    experiment_ids = {item.get("id") for item in experiments if isinstance(item, dict)}
    if len(experiment_ids) != len(experiments) or None in experiment_ids:
        fail("experiment ids must be present and unique")

    primary_mechanisms: set[str] = set()
    run_now = 0
    for experiment in experiments:
        if not isinstance(experiment, dict):
            fail("each experiment must be an object")
        experiment_id = experiment["id"]
        for field in (
            "question",
            "falsifiable_claim",
            "baseline",
            "candidate",
            "changed_variable",
            "completion_predicate",
            "decision_rule",
            "next_validation",
        ):
            text(experiment.get(field), f"{experiment_id}.{field}")
        if experiment.get("status") not in ALLOWED_STATUSES:
            fail(f"{experiment_id}.status is invalid")
        layers = experiment.get("engineering_layers")
        text_list(layers, f"{experiment_id}.engineering_layers")
        if set(layers) - ALLOWED_LAYERS:
            fail(f"{experiment_id} has invalid engineering layers")
        mechanism_ids = experiment.get("mechanism_ids")
        text_list(mechanism_ids, f"{experiment_id}.mechanism_ids")
        unknown_mechanisms = set(mechanism_ids) - set(mechanisms)
        if unknown_mechanisms:
            fail(f"{experiment_id} has unknown mechanisms: {sorted(unknown_mechanisms)}")
        primary_mechanism = experiment.get("primary_mechanism_id")
        text(primary_mechanism, f"{experiment_id}.primary_mechanism_id")
        if primary_mechanism not in mechanism_ids:
            fail(f"{experiment_id}.primary_mechanism_id must be listed in mechanism_ids")
        if primary_mechanism in primary_mechanisms:
            fail(f"mechanism has more than one primary experiment: {primary_mechanism}")
        primary_mechanisms.add(primary_mechanism)

        borrowing = experiment.get("external_borrowing")
        if not isinstance(borrowing, list) or not borrowing:
            fail(f"{experiment_id}.external_borrowing must be non-empty")
        for item in borrowing:
            if not isinstance(item, dict):
                fail(f"{experiment_id}.external_borrowing entries must be objects")
            for field in ("source_id", "implementation_detail", "complex_micro_contract", "not_transferred"):
                text(item.get(field), f"{experiment_id}.external_borrowing.{field}")
            if item["source_id"] not in source_ids and item["source_id"] not in reference_ids:
                fail(f"{experiment_id} has unknown external source: {item['source_id']}")

        samples = experiment.get("samples")
        text_list(samples, f"{experiment_id}.samples")
        if len(samples) < 2:
            fail(f"{experiment_id} needs at least two samples")
        writable_samples = experiment.get("writable_samples")
        text_list(writable_samples, f"{experiment_id}.writable_samples")
        if experiment_id not in contract_fixtures or experiment_id not in writable_fixtures:
            fail(f"{experiment_id} is missing a contract or writable fixture")
        contract_ids = [item.get("sample_id") for item in contract_fixtures[experiment_id].get("samples", [])]
        writable_ids = [item.get("sample_id") for item in writable_fixtures[experiment_id].get("samples", [])]
        if samples != contract_ids:
            fail(f"{experiment_id}.samples must equal its contract fixture sample IDs")
        if writable_samples != writable_ids:
            fail(f"{experiment_id}.writable_samples must equal its writable fixture sample IDs")
        if not isinstance(experiment.get("trials_per_arm"), int) or experiment["trials_per_arm"] < 3:
            fail(f"{experiment_id} needs at least three trials per arm")
        graders = experiment.get("graders")
        text_list(graders, f"{experiment_id}.graders")
        if set(graders) != REQUIRED_GRADERS:
            fail(f"{experiment_id} must use environment, trajectory, and human graders")
        validity = experiment.get("validity_checks")
        text_list(validity, f"{experiment_id}.validity_checks")
        if not REQUIRED_VALIDITY_CHECKS.issubset(validity):
            fail(f"{experiment_id} lacks canonical validity checks")
        text_list(experiment.get("outcome_metrics"), f"{experiment_id}.outcome_metrics")
        text_list(experiment.get("locked_variables"), f"{experiment_id}.locked_variables")
        if experiment.get("run_now") is True:
            run_now += 1

    if primary_mechanisms != target_mechanisms:
        fail(
            "primary experiment coverage mismatch: "
            + f"missing={sorted(target_mechanisms - primary_mechanisms)} "
            + f"extra={sorted(primary_mechanisms - target_mechanisms)}"
        )
    if run_now != len(experiments):
        fail("every core/conditional revalidation experiment must be selected for this suite")

    print(
        f"ok experiments={len(experiments)} method_sources={len(method_sources)} "
        f"primary_coverage={len(primary_mechanisms)}/{len(target_mechanisms)} run_now={run_now}"
    )


if __name__ == "__main__":
    main()
