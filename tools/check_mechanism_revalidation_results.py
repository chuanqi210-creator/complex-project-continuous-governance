#!/usr/bin/env python3
"""Check the current seven-mechanism execution, rescore, and review chain."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs/evals/results/executable-pilots-20260717T145657Z-4db18e9646-gpt-5.6-luna.json"
RESCORE = ROOT / "docs/evals/results/executable-pilots-20260717T171657Z-a091c06076-rescore.json"
REPAIR = ROOT / "docs/evals/results/scorer-repair-external-calibration-20260718.json"
REVIEW = ROOT / "docs/evals/results/mechanism-revalidation-independent-model-review-20260718.json"
MATURITY = ROOT / "docs/mechanism-maturity.json"
PROGRAM = ROOT / "docs/evals/experiment-program.json"


def fail(message: str) -> None:
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def load(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError) as exc:
        fail(f"cannot load {path.relative_to(ROOT)}: {exc}")
    if not isinstance(value, dict):
        fail(f"expected object: {path.relative_to(ROOT)}")
    return value


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    source = load(SOURCE)
    rescore = load(RESCORE)
    repair = load(REPAIR)
    review = load(REVIEW)
    maturity = load(MATURITY)
    program = load(PROGRAM)

    experiment_ids = {item["id"] for item in program.get("experiments", [])}
    if len(experiment_ids) != 7:
        fail(f"expected seven program experiments, got {len(experiment_ids)}")
    if set(source.get("experiments", {})) != experiment_ids:
        fail("source result does not cover the current program")
    health = source.get("run_health", {})
    if health != {
        "status": "healthy",
        "valid_trials": 84,
        "expected_trials": 84,
        "terminal_error_count": 0,
    }:
        fail(f"unexpected source run health: {health}")

    if rescore.get("source_result_sha256") != sha256(SOURCE):
        fail("rescore does not pin the current source result")
    if rescore.get("task_and_prompt_match") is not True:
        fail("rescore did not verify frozen task and prompt text")
    if set(rescore.get("experiments", {})) != experiment_ids:
        fail("rescore does not cover all seven experiments")
    score_changes = []
    for experiment_id, item in rescore["experiments"].items():
        for arm in ("baseline", "candidate"):
            aggregate = item["scores"][arm]["aggregate"]
            if aggregate["valid_trials"] != aggregate["expected_trials"] or aggregate["environment_success_rate"] != 1.0:
                fail(f"non-ceiling current environment score: {experiment_id}/{arm}")
        if item.get("automated_descriptive_result") != "no_environment_success_difference":
            fail(f"unexpected descriptive result: {experiment_id}")
        score_changes.extend(item.get("changed_trial_scores", []))
    if score_changes != [
        {
            "arm": "baseline",
            "sample_id": "calibration_negative_comparison",
            "trial": 1,
            "before": False,
            "after": True,
        }
    ]:
        fail(f"unexpected rescore changes: {score_changes}")

    if repair.get("source_result_sha256") != sha256(SOURCE) or repair.get("rescore_result_sha256") != sha256(RESCORE):
        fail("scorer repair hashes do not match retained results")
    if repair.get("status") != "accepted_as_oracle_repair_not_mechanism_evidence":
        fail("scorer repair maturity boundary is missing")
    if repair.get("scorer_change", {}).get("score_changes") != 1:
        fail("scorer repair must declare exactly one changed trial")

    registry = {item["id"]: item for item in maturity.get("mechanisms", [])}
    review_decisions = {item["id"]: item for item in review.get("mechanism_decisions", [])}
    primary_mechanisms = {item["primary_mechanism_id"] for item in program["experiments"]}
    if set(review_decisions) != primary_mechanisms:
        fail("independent review does not cover every primary mechanism")
    for mechanism_id, decision in review_decisions.items():
        mechanism = registry.get(mechanism_id)
        if not mechanism:
            fail(f"review links unknown mechanism: {mechanism_id}")
        for field in ("normative_role", "evidence_status"):
            if decision.get(field) != mechanism.get(field):
                fail(f"review and maturity disagree: {mechanism_id}.{field}")
    if review.get("human_review") is not False or review.get("blind_human_review") != "pending":
        fail("independent model review is misclassified as human evidence")

    print(
        "ok "
        + f"experiments={len(experiment_ids)} trials={health['valid_trials']}/{health['expected_trials']} "
        + f"score_repairs={len(score_changes)} reviewed_mechanisms={len(review_decisions)} "
        + "human_review=pending validated=0"
    )


if __name__ == "__main__":
    main()
