#!/usr/bin/env python3
"""Re-score a frozen writable-pilot run without repeating model execution.

The source result remains immutable. This tool verifies that current task and
prompt text match the frozen run, applies the current environment scorer to the
stored repository outcomes, and writes a compact append-only rescore record.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
RUNNER_PATH = ROOT / "tools/run_executable_mechanism_pilots.py"
RESULTS_DIR = ROOT / "docs/evals/results"
SPEC = importlib.util.spec_from_file_location("complex_writable_pilots", RUNNER_PATH)
assert SPEC and SPEC.loader
runner = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(runner)


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sha256_json(value: Any) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True).encode("utf-8")).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    args = parser.parse_args()

    source_path = Path(args.input).resolve()
    if source_path.parent != RESULTS_DIR.resolve() or not source_path.name.endswith(".json"):
        raise SystemExit("input must be a JSON result under docs/evals/results")
    source = runner.load(source_path)
    if source.get("kind") != "writable_synthetic_mechanism_pilot":
        raise SystemExit("input is not a writable synthetic mechanism pilot")

    fixtures = runner.load(runner.FIXTURES)["experiments"]
    program = {item["id"]: item for item in runner.load(runner.PROGRAM)["experiments"]}
    experiment_ids = sorted(source.get("experiments", {}))
    if experiment_ids != sorted(fixtures) or experiment_ids != sorted(program):
        raise SystemExit("source result does not cover the current seven-experiment suite")

    scoring_source_hashes = {
        str(path.relative_to(ROOT)): sha256_file(path)
        for path in (
            runner.FIXTURES,
            runner.PROGRAM,
            runner.SCHEMA,
            RUNNER_PATH,
            Path(__file__).resolve(),
        )
    }
    scoring_bundle_hash = sha256_json(scoring_source_hashes)
    output: dict[str, Any] = {
        "version": "1.0",
        "kind": "writable_synthetic_mechanism_rescore",
        "source_result": str(source_path.relative_to(ROOT)),
        "source_result_sha256": sha256_file(source_path),
        "source_run_id": source["run_id"],
        "source_run_health": source["run_health"],
        "model": source["model"],
        "model_revision_status": source.get("model_revision_status", "unknown"),
        "scoring_source_hashes": scoring_source_hashes,
        "scoring_bundle_hash": scoring_bundle_hash,
        "task_and_prompt_match": True,
        "human_review": "pending",
        "trajectory_review": "pending",
        "experiments": {},
    }

    for experiment_id in experiment_ids:
        fixture = fixtures[experiment_id]
        source_experiment = source["experiments"][experiment_id]
        grouped: dict[str, dict[str, list[dict[str, Any]]]] = {
            arm: {sample["sample_id"]: [] for sample in fixture["samples"]}
            for arm in ("baseline", "candidate")
        }
        prompt_hashes: dict[str, str] = {}
        for arm in ("baseline", "candidate"):
            current_prompts: dict[str, str] = {}
            for sample in fixture["samples"]:
                sample_id = sample["sample_id"]
                prompt = runner.build_prompt(fixture["arms"][arm], sample["task"])
                current_prompts[sample_id] = prompt
                frozen_prompt = source_experiment["prompt_texts"][arm][sample_id]
                if prompt != frozen_prompt:
                    raise SystemExit(f"task/prompt drift: {experiment_id}/{arm}/{sample_id}")
                grouped[arm][sample_id] = source_experiment["trials"][arm][sample_id]
            prompt_hashes[arm] = sha256_json(current_prompts)
            if prompt_hashes[arm] != source_experiment["prompt_hashes"][arm]:
                raise SystemExit(f"prompt hash mismatch: {experiment_id}/{arm}")

        scores = {
            arm: runner.aggregate_arm(fixture, grouped[arm])
            for arm in ("baseline", "candidate")
        }
        changed_scores: list[dict[str, Any]] = []
        for arm in ("baseline", "candidate"):
            sample_map = {sample["sample_id"]: sample for sample in fixture["samples"]}
            for sample_id, trials in grouped[arm].items():
                for trial in trials:
                    before = bool(trial["environment_score"]["environment_success"])
                    after = bool(runner.score_trial(trial, sample_map[sample_id])["environment_success"])
                    if before != after:
                        changed_scores.append(
                            {
                                "arm": arm,
                                "sample_id": sample_id,
                                "trial": trial["trial"],
                                "before": before,
                                "after": after,
                            }
                        )
        output["experiments"][experiment_id] = {
            "primary_mechanism_id": program[experiment_id]["primary_mechanism_id"],
            "prompt_hashes": prompt_hashes,
            "scores": scores,
            "automated_descriptive_result": runner.automated_descriptive_result(
                scores["baseline"], scores["candidate"]
            ),
            "changed_trial_scores": changed_scores,
            "interpretation_boundary": (
                "Environment re-scoring only. It can repair a scorer mismatch; "
                "it cannot establish trajectory quality, human preference, or real-project benefit."
            ),
        }

    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    output["run_id"] = f"{timestamp}-{scoring_bundle_hash[:10]}-rescore"
    output_path = RESULTS_DIR / f"executable-pilots-{output['run_id']}.json"
    if output_path.exists():
        raise SystemExit(f"append-only result exists: {output_path}")
    output_path.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "run_id": output["run_id"],
                "source_run_id": source["run_id"],
                "experiments": len(output["experiments"]),
                "changed_trial_scores": sum(
                    len(item["changed_trial_scores"])
                    for item in output["experiments"].values()
                ),
                "result": str(output_path.relative_to(ROOT)),
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
