#!/usr/bin/env python3
"""Validate lightweight Complex eval records without an external dependency."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "docs" / "evals" / "complex-eval-record.schema.json"
RECORDS = ROOT / "docs" / "evals" / "records"
MATURITY = ROOT / "docs" / "mechanism-maturity.json"
STATUSES = {"planned", "screened", "compared", "reviewed"}
DECISIONS = {"pending", "keep_baseline", "transfer_candidate", "revise_and_repeat", "insufficient_evidence"}
RUN_ROLES = {"baseline", "candidate"}
PROJECT_NATURES = {"evidence_fill", "model_discovery", "mixed", "execution_delivery"}
PRIVACY_LEVELS = {"public", "redacted", "private_pointer"}
SAMPLE_ORIGINS = {"real_project", "redacted_real_project", "synthetic", "fixture"}
HUMAN_REVIEW_VALUES = {"pending", "pass", "fail", "mixed"}
HUMAN_PREFERENCES = {"pending", "baseline", "candidate", "tie", "insufficient"}
REQUIRED_LOCKED_VARIABLES = {
    "task",
    "sample_ids",
    "project_snapshot",
    "surface",
    "model_or_agent",
    "runtime_config",
    "responsibility_boundary",
    "limits",
    "completion_predicate",
    "scorer_id",
    "scorer_version",
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


def require_fields(value: dict[str, Any], fields: set[str], label: str) -> None:
    missing = fields - set(value)
    if missing:
        fail(f"{label} missing fields: {sorted(missing)}")


def require_nonempty_string(value: Any, label: str) -> None:
    if not isinstance(value, str) or not value.strip():
        fail(f"{label} must be a non-empty string")


def main() -> None:
    schema = load(SCHEMA)
    maturity = load(MATURITY)
    if schema.get("title") != "Complex Evaluation Record":
        fail("unexpected eval record schema")
    known_mechanism_ids = {
        str(mechanism.get("id"))
        for mechanism in maturity.get("mechanisms", [])
        if isinstance(mechanism, dict)
    }

    paths = sorted(RECORDS.glob("*.json"))
    if not paths:
        fail("no eval records found")

    for path in paths:
        record = load(path)
        require_fields(record, {"schema_version", "status", "eval_case", "runs", "scores", "comparison"}, path.name)
        if record["schema_version"] != "1.0" or record["status"] not in STATUSES:
            fail(f"{path.name} has invalid schema_version or status")

        case = record["eval_case"]
        if not isinstance(case, dict):
            fail(f"{path.name}.eval_case must be an object")
        require_fields(case, {"id", "version", "mechanism_ids", "project_nature", "task", "sample_ids", "sample_origin", "project_snapshot", "responsibility_boundary", "completion_predicate", "scorer_id", "limits", "privacy"}, f"{path.name}.eval_case")
        for field in ("id", "version", "task", "project_snapshot", "responsibility_boundary", "completion_predicate", "scorer_id"):
            require_nonempty_string(case[field], f"{path.name}.eval_case.{field}")
        if not isinstance(case["sample_ids"], list) or not case["sample_ids"]:
            fail(f"{path.name}.eval_case.sample_ids must be non-empty")
        if any(not isinstance(sample_id, str) or not sample_id.strip() for sample_id in case["sample_ids"]):
            fail(f"{path.name}.eval_case.sample_ids must contain non-empty strings")
        if len(set(case["sample_ids"])) != len(case["sample_ids"]):
            fail(f"{path.name}.eval_case.sample_ids must be unique")
        if not isinstance(case["mechanism_ids"], list) or not case["mechanism_ids"]:
            fail(f"{path.name}.eval_case.mechanism_ids must be non-empty")
        if any(not isinstance(mechanism_id, str) or not mechanism_id.strip() for mechanism_id in case["mechanism_ids"]):
            fail(f"{path.name}.eval_case.mechanism_ids must contain non-empty strings")
        if len(set(case["mechanism_ids"])) != len(case["mechanism_ids"]):
            fail(f"{path.name}.eval_case.mechanism_ids must be unique")
        unknown_mechanisms = sorted(set(case["mechanism_ids"]) - known_mechanism_ids)
        if unknown_mechanisms:
            fail(f"{path.name}.eval_case links unknown mechanisms: {unknown_mechanisms}")
        if not isinstance(case["limits"], dict) or not case["limits"]:
            fail(f"{path.name}.eval_case.limits must be a non-empty object")
        if case["project_nature"] not in PROJECT_NATURES or case["privacy"] not in PRIVACY_LEVELS or case["sample_origin"] not in SAMPLE_ORIGINS:
            fail(f"{path.name}.eval_case has invalid project_nature, privacy, or sample_origin")

        runs = record["runs"]
        scores = record["scores"]
        if not isinstance(runs, list) or not isinstance(scores, list):
            fail(f"{path.name} runs and scores must be lists")
        run_ids: set[str] = set()
        run_roles: dict[str, str] = {}
        roles: set[str] = set()
        for run in runs:
            if not isinstance(run, dict):
                fail(f"{path.name} run must be an object")
            require_fields(run, {"id", "role", "artifact_revision", "prompt_version", "skill_revision", "surface", "model_or_agent", "runtime_config", "attempts", "changed_variable", "result_pointer", "error_summary"}, f"{path.name}.run")
            if run["id"] in run_ids or run["role"] not in RUN_ROLES:
                fail(f"{path.name} has duplicate run id or invalid role")
            for field in ("id", "artifact_revision", "prompt_version", "skill_revision", "surface", "model_or_agent", "changed_variable", "result_pointer"):
                require_nonempty_string(run[field], f"{path.name}.run.{field}")
            if not isinstance(run["runtime_config"], dict) or not isinstance(run["attempts"], int) or run["attempts"] < 1:
                fail(f"{path.name} run has invalid runtime_config or attempts")
            run_ids.add(run["id"])
            run_roles[run["id"]] = run["role"]
            roles.add(run["role"])

        scored_run_ids: set[str] = set()
        for score in scores:
            if not isinstance(score, dict):
                fail(f"{path.name} score must be an object")
            require_fields(score, {"run_id", "scorer_id", "scorer_version", "per_sample", "aggregate", "human_review"}, f"{path.name}.score")
            if score["run_id"] not in run_ids:
                fail(f"{path.name} score links unknown run: {score['run_id']}")
            if score["run_id"] in scored_run_ids:
                fail(f"{path.name} has duplicate score for run: {score['run_id']}")
            if score["scorer_id"] != case["scorer_id"]:
                fail(f"{path.name} score uses a scorer_id different from eval_case")
            require_nonempty_string(score["scorer_version"], f"{path.name}.score.scorer_version")
            if not isinstance(score["per_sample"], list) or not isinstance(score["aggregate"], dict):
                fail(f"{path.name} score has invalid per_sample or aggregate")
            sample_score_ids: list[str] = []
            for sample_score in score["per_sample"]:
                if not isinstance(sample_score, dict):
                    fail(f"{path.name} per_sample score must be an object")
                require_fields(sample_score, {"sample_id", "metrics"}, f"{path.name}.score.per_sample")
                require_nonempty_string(sample_score["sample_id"], f"{path.name}.score.per_sample.sample_id")
                if not isinstance(sample_score["metrics"], dict) or not sample_score["metrics"]:
                    fail(f"{path.name} per_sample metrics must be a non-empty object")
                sample_score_ids.append(sample_score["sample_id"])
            if sample_score_ids and set(sample_score_ids) != set(case["sample_ids"]):
                fail(f"{path.name} per_sample IDs must match eval_case.sample_ids")
            if score["human_review"] not in HUMAN_REVIEW_VALUES:
                fail(f"{path.name} score has invalid human_review")
            scored_run_ids.add(score["run_id"])

        comparison = record["comparison"]
        if not isinstance(comparison, dict):
            fail(f"{path.name}.comparison must be an object")
        require_fields(comparison, {"baseline_run_id", "candidate_run_id", "changed_variable", "locked_variables", "decision", "human_preference", "limitations", "next_validation"}, f"{path.name}.comparison")
        if comparison["decision"] not in DECISIONS:
            fail(f"{path.name}.comparison.decision is invalid")
        if comparison["human_preference"] not in HUMAN_PREFERENCES:
            fail(f"{path.name}.comparison.human_preference is invalid")
        require_nonempty_string(comparison["changed_variable"], f"{path.name}.comparison.changed_variable")
        require_nonempty_string(comparison["next_validation"], f"{path.name}.comparison.next_validation")
        if not isinstance(comparison["locked_variables"], list) or set(comparison["locked_variables"]) != REQUIRED_LOCKED_VARIABLES:
            fail(f"{path.name}.comparison.locked_variables must equal the canonical locked set")
        if not isinstance(comparison["limitations"], list) or not comparison["limitations"]:
            fail(f"{path.name}.comparison.limitations must be a non-empty list")

        if record["status"] in {"compared", "reviewed"}:
            if roles != RUN_ROLES:
                fail(f"{path.name} compared/reviewed record needs baseline and candidate runs")
            if comparison["baseline_run_id"] not in run_ids or comparison["candidate_run_id"] not in run_ids:
                fail(f"{path.name} comparison links unknown runs")
            if run_roles[comparison["baseline_run_id"]] != "baseline" or run_roles[comparison["candidate_run_id"]] != "candidate":
                fail(f"{path.name} comparison run IDs must point to baseline and candidate roles")
            if comparison["baseline_run_id"] == comparison["candidate_run_id"]:
                fail(f"{path.name} comparison must use two distinct runs")
            baseline_run = next(run for run in runs if run["id"] == comparison["baseline_run_id"])
            candidate_run = next(run for run in runs if run["id"] == comparison["candidate_run_id"])
            if baseline_run["changed_variable"] != comparison["changed_variable"] or candidate_run["changed_variable"] != comparison["changed_variable"]:
                fail(f"{path.name} both runs must match comparison.changed_variable")
            for locked_run_field in ("surface", "model_or_agent", "runtime_config"):
                if baseline_run[locked_run_field] != candidate_run[locked_run_field]:
                    fail(f"{path.name} changed locked run field: {locked_run_field}")
            if scored_run_ids != run_ids:
                fail(f"{path.name} compared/reviewed record needs one score for each run")
            scorer_versions = {score["scorer_version"] for score in scores}
            if len(scorer_versions) != 1:
                fail(f"{path.name} compared/reviewed scores must use one scorer_version")
            for score in scores:
                if len(score["per_sample"]) != len(case["sample_ids"]):
                    fail(f"{path.name} compared/reviewed scores need one per_sample result for each sample")
                if not score["aggregate"]:
                    fail(f"{path.name} compared/reviewed scores need aggregate metrics")
            if comparison["decision"] == "pending":
                fail(f"{path.name} compared/reviewed record cannot retain a pending decision")
            score_by_run = {score["run_id"]: score for score in scores}
            if comparison["decision"] == "transfer_candidate":
                if comparison["human_preference"] != "candidate":
                    fail(f"{path.name} transfer_candidate needs human preference for candidate")
                if score_by_run[comparison["candidate_run_id"]]["human_review"] in {"pending", "fail"}:
                    fail(f"{path.name} transfer_candidate needs a completed non-failing candidate human review")
            if comparison["decision"] == "keep_baseline":
                if comparison["human_preference"] != "baseline":
                    fail(f"{path.name} keep_baseline needs human preference for baseline")
                if score_by_run[comparison["baseline_run_id"]]["human_review"] in {"pending", "fail"}:
                    fail(f"{path.name} keep_baseline needs a completed non-failing baseline human review")
            if record["status"] == "reviewed":
                if any(score["human_review"] == "pending" for score in scores):
                    fail(f"{path.name} reviewed record cannot retain pending human review")
                if comparison["human_preference"] == "pending":
                    fail(f"{path.name} reviewed record needs a human preference")
        elif comparison["decision"] != "pending":
            fail(f"{path.name} non-comparison record must keep decision pending")
        elif comparison["human_preference"] != "pending":
            fail(f"{path.name} non-comparison record must keep human_preference pending")

    print(f"ok eval_records={len(paths)}")


if __name__ == "__main__":
    main()
