#!/usr/bin/env python3
"""Run append-only Complex contract-legibility screens.

This runner deliberately does not call these screens agent outcome validation. Each
opaque sample is a separate isolated Codex invocation, but the task remains a
read-only decision fixture. Executable, platform, longitudinal, and human-review
evidence is tracked separately.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import random
import re
import subprocess
import tempfile
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "docs/evals/bounded-experiment-fixtures.json"
OUTPUT_SCHEMA = ROOT / "docs/evals/bounded-experiment-output.schema.json"
PROGRAM = ROOT / "docs/evals/experiment-program.json"
RESULTS_DIR = ROOT / "docs/evals/results"
RECORDS_DIR = ROOT / "docs/evals/records"
LOCKED_VARIABLES = [
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
]


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected object: {path}")
    return value


def cli_version() -> str:
    result = subprocess.run(["codex", "--version"], text=True, capture_output=True, check=True)
    return result.stdout.strip()


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def expand_packet(value: Any) -> str:
    if isinstance(value, str):
        return value
    if isinstance(value, dict):
        prefix = value.get("prefix", "")
        repeat_text = value.get("repeat_text", "")
        repeat_count = value.get("repeat_count", 0)
        suffix = value.get("suffix", "")
        if not isinstance(prefix, str) or not isinstance(repeat_text, str) or not isinstance(suffix, str):
            raise ValueError("packet expansion text fields must be strings")
        if not isinstance(repeat_count, int) or repeat_count < 0:
            raise ValueError("packet repeat_count must be a non-negative integer")
        return prefix + repeat_text * repeat_count + suffix
    raise ValueError("packet must be text or an expansion object")


def packet_for(experiment_id: str, arm: str, sample: dict[str, Any]) -> str:
    arm_key = f"{arm}_packet"
    if arm_key in sample:
        return expand_packet(sample[arm_key])
    return expand_packet(sample["packet"])


def sample_aliases(fixture: dict[str, Any]) -> dict[str, str]:
    return {
        sample["sample_id"]: f"case_{index:02d}"
        for index, sample in enumerate(fixture["samples"], start=1)
    }


def build_prompt(
    experiment_id: str,
    arm: str,
    fixture: dict[str, Any],
    sample: dict[str, Any],
) -> str:
    alias = sample_aliases(fixture)[sample["sample_id"]]
    packet = packet_for(experiment_id, arm, sample)
    allowed_issues = fixture.get("allowed_issue_ids", [])
    return (
        "You are one isolated trial in a contract-legibility screen. "
        "Use only the supplied arm contract and packet; do not read files, invoke tools, or use outside facts. "
        "Return exactly one result for the one opaque sample. "
        f"primary_decision must be one of {fixture['allowed_decisions']}. "
        f"detected_issues may contain only {allowed_issues}; use an empty list when no issue vocabulary is supplied. "
        "evidence_refs should name short labels from the packet. Do not infer the semantic fixture name.\n\n"
        f"ARM CONTRACT:\n{fixture['arms'][arm]}\n\n"
        f"SAMPLE:\n{json.dumps({'sample_id': alias, 'packet': packet}, ensure_ascii=False, indent=2)}"
    )


def run_trial(job: dict[str, Any]) -> dict[str, Any]:
    with tempfile.TemporaryDirectory(prefix="complex-contract-screen-") as temp_dir:
        out = Path(temp_dir) / "out.json"
        command = [
            "codex",
            "exec",
            "--ephemeral",
            "--ignore-user-config",
            "--skip-git-repo-check",
            "--sandbox",
            "read-only",
            "-m",
            job["model"],
            "-c",
            'model_reasoning_effort="low"',
            "--output-schema",
            str(OUTPUT_SCHEMA),
            "--output-last-message",
            str(out),
            "-C",
            temp_dir,
            "-",
        ]
        errors: list[str] = []
        for command_attempt in range(1, 3):
            try:
                result = subprocess.run(
                    command,
                    input=job["prompt"],
                    text=True,
                    capture_output=True,
                    timeout=240,
                    check=False,
                )
            except subprocess.TimeoutExpired:
                errors.append(f"command_attempt={command_attempt}: timeout")
                continue
            if result.returncode == 0 and out.is_file():
                try:
                    payload = json.loads(out.read_text(encoding="utf-8"))
                except json.JSONDecodeError as exc:
                    errors.append(f"command_attempt={command_attempt}: invalid JSON: {exc}")
                    continue
                return {**job, "payload": payload, "error": "", "command_attempts": command_attempt}
            tail = (result.stderr or result.stdout)[-1000:].replace("\n", " ")
            errors.append(f"command_attempt={command_attempt}: rc={result.returncode} {tail}")
        return {**job, "payload": {"results": []}, "error": " | ".join(errors), "command_attempts": 2}


def normalized_result(trial: dict[str, Any], expected_alias: str) -> dict[str, Any] | None:
    values = trial.get("payload", {}).get("results", [])
    if not isinstance(values, list) or len(values) != 1 or not isinstance(values[0], dict):
        return None
    result = values[0]
    return result if result.get("sample_id") == expected_alias else None


def mean(values: list[float]) -> float:
    return round(sum(values) / len(values), 4) if values else 0.0


def score_arm(
    experiment_id: str,
    arm: str,
    fixture: dict[str, Any],
    trials_by_sample: dict[str, list[dict[str, Any]]],
) -> dict[str, Any]:
    aliases = sample_aliases(fixture)
    per_sample: list[dict[str, Any]] = []
    total_valid = 0
    total_expected = 0
    for sample in fixture["samples"]:
        sample_id = sample["sample_id"]
        trials = trials_by_sample[sample_id]
        outputs = [
            result
            for trial in trials
            if (result := normalized_result(trial, aliases[sample_id])) is not None
        ]
        total_valid += len(outputs)
        total_expected += len(trials)
        metrics: dict[str, float | int] = {
            "valid_trials": len(outputs),
            "decision_accuracy": mean(
                [float(item.get("primary_decision") == sample["expected_decision"]) for item in outputs]
            ),
        }
        allowed_decisions = set(fixture["allowed_decisions"])
        allowed_issues = set(fixture.get("allowed_issue_ids", []))
        metrics["output_contract_violation_rate"] = mean(
            [
                float(
                    item.get("primary_decision") not in allowed_decisions
                    or bool(set(item.get("detected_issues", [])) - allowed_issues)
                )
                for item in outputs
            ]
        )
        all_error_tags = sorted(
            {
                tag
                for tags in sample.get("decision_error_tags", {}).values()
                for tag in tags
            }
        )
        for tag in all_error_tags:
            metrics[tag] = mean(
                [
                    float(
                        tag
                        in sample.get("decision_error_tags", {}).get(
                            item.get("primary_decision"), []
                        )
                    )
                    for item in outputs
                ]
            )
        per_sample.append({"sample_id": sample_id, "metrics": metrics})

    aggregate: dict[str, float | int] = {
        "valid_trials": total_valid,
        "expected_trials": total_expected,
        "decision_accuracy": mean(
            [float(item["metrics"]["decision_accuracy"]) for item in per_sample]
        ),
        "working_set_chars": sum(
            len(packet_for(experiment_id, arm, sample)) for sample in fixture["samples"]
        ),
    }
    metric_names = sorted(
        {
            metric
            for item in per_sample
            for metric in item["metrics"]
            if metric not in {"valid_trials", "decision_accuracy"}
        }
    )
    for metric in metric_names:
        aggregate[metric] = mean(
            [float(item["metrics"].get(metric, 0.0)) for item in per_sample]
        )
    return {"per_sample": per_sample, "aggregate": aggregate}


def automated_signal(
    fixture: dict[str, Any], baseline: dict[str, Any], candidate: dict[str, Any]
) -> str:
    b = baseline["aggregate"]
    c = candidate["aggregate"]
    if b["valid_trials"] < b["expected_trials"] or c["valid_trials"] < c["expected_trials"]:
        return "run_failure"
    directions = fixture["metric_directions"]
    higher = directions.get("higher", [])
    lower = directions.get("lower", [])
    non_worse = all(float(c.get(metric, 0.0)) >= float(b.get(metric, 0.0)) for metric in higher)
    non_worse = non_worse and all(
        float(c.get(metric, 0.0)) <= float(b.get(metric, 0.0)) for metric in lower
    )
    strict = any(float(c.get(metric, 0.0)) > float(b.get(metric, 0.0)) for metric in higher)
    strict = strict or any(
        float(c.get(metric, 0.0)) < float(b.get(metric, 0.0)) for metric in lower
    )
    if non_worse and strict:
        return "descriptive_nonworse_difference"
    if non_worse:
        return "descriptive_no_difference"
    return "descriptive_tradeoff_or_oracle_conflict"


def build_record(
    experiment: dict[str, Any],
    fixture: dict[str, Any],
    scores: dict[str, dict[str, Any]],
    grouped: dict[str, dict[str, list[dict[str, Any]]]],
    model: str,
    version: str,
    result_file: str,
    source_bundle_hash: str,
    fixture_hash: str,
    skill_hash: str,
    prompt_hashes: dict[str, str],
) -> dict[str, Any]:
    experiment_id = experiment["id"]
    scorer = f"{experiment_id}_contract_screen"
    runtime = {
        "cli_version": version,
        "reasoning_effort": "low",
        "sandbox": "read-only",
        "ignore_user_config": True,
        "trials_per_sample_per_arm": experiment["trials_per_arm"],
        "sample_invocation": "one opaque sample per isolated process",
        "structured_output_schema": str(OUTPUT_SCHEMA.relative_to(ROOT)),
    }
    signal = automated_signal(fixture, scores["baseline"], scores["candidate"])
    runs = []
    score_records = []
    for arm in ("baseline", "candidate"):
        values = [
            trial
            for sample_trials in grouped[arm].values()
            for trial in sample_trials
        ]
        run_id = f"{experiment_id}-{arm}-{len(values)}x"
        runs.append(
            {
                "id": run_id,
                "role": arm,
                "artifact_revision": f"sha256:{source_bundle_hash}",
                "prompt_version": f"sha256:{prompt_hashes[arm]}",
                "skill_revision": f"sha256:{skill_hash}",
                "surface": "codex exec isolated contract screen",
                "model_or_agent": model,
                "runtime_config": runtime,
                "attempts": len(values),
                "changed_variable": experiment["changed_variable"],
                "result_pointer": f"{result_file}#{experiment_id}/{arm}",
                "error_summary": " | ".join(trial["error"] for trial in values if trial["error"]),
            }
        )
        score_records.append(
            {
                "run_id": run_id,
                "scorer_id": scorer,
                "scorer_version": "2.1-diagnostic-only",
                "per_sample": scores[arm]["per_sample"],
                "aggregate": scores[arm]["aggregate"],
                "human_review": "pending",
            }
        )
    return {
        "schema_version": "1.0",
        "status": "compared",
        "eval_case": {
            "id": experiment_id,
            "version": "2.0",
            "mechanism_ids": experiment["mechanism_ids"],
            "project_nature": "mixed",
            "task": experiment["question"],
            "sample_ids": [sample["sample_id"] for sample in fixture["samples"]],
            "sample_origin": "fixture",
            "project_snapshot": f"docs/evals/bounded-experiment-fixtures.json@sha256:{fixture_hash}",
            "responsibility_boundary": "Read-only contract screen; no project state or external side effect is available.",
            "completion_predicate": experiment["completion_predicate"],
            "scorer_id": scorer,
            "limits": {
                "trials_per_sample_per_arm": experiment["trials_per_arm"],
                "command_timeout_seconds": 240,
                "max_command_attempts": 2,
            },
            "privacy": "public",
        },
        "runs": runs,
        "scores": score_records,
        "comparison": {
            "baseline_run_id": runs[0]["id"],
            "candidate_run_id": runs[1]["id"],
            "changed_variable": experiment["changed_variable"],
            "locked_variables": LOCKED_VARIABLES,
            "decision": "insufficient_evidence",
            "human_preference": "pending",
            "limitations": [
                "This is a contract-legibility screen, not an executable agent outcome evaluation.",
                "The mechanism contract is the treatment; the native baseline is neutral, but fixture oracles still score a bounded decision task.",
                "No tools, environment state change, platform lifecycle, longitudinal outcome, or human blind review is instantiated.",
                f"Automated descriptive result: {signal}. It is not an effect estimate and cannot promote evidence_status; inspect oracle ambiguity and the experiment-specific decision rule before interpreting it.",
            ],
            "next_validation": experiment["next_validation"],
        },
    }


def safe_slug(value: str) -> str:
    return re.sub(r"[^a-zA-Z0-9_.-]+", "-", value).strip("-")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="gpt-5.3-codex-spark")
    parser.add_argument("--trials", type=int, default=3)
    parser.add_argument("--max-workers", type=int, default=12)
    parser.add_argument("--experiment", action="append", dest="experiments")
    args = parser.parse_args()
    if args.trials < 3:
        raise SystemExit("at least three trials per sample per arm are required")

    fixtures = load(FIXTURES)["experiments"]
    program = load(PROGRAM)
    program_items = {item["id"]: item for item in program["experiments"]}
    selected = args.experiments or [
        item["id"] for item in program["experiments"] if item.get("run_now") is True
    ]
    unknown = set(selected) - set(fixtures) | (set(selected) - set(program_items))
    if unknown:
        raise SystemExit(f"experiment definition missing for: {sorted(unknown)}")
    for experiment_id in selected:
        fixture_samples = [sample["sample_id"] for sample in fixtures[experiment_id]["samples"]]
        if program_items[experiment_id].get("samples") != fixture_samples:
            raise SystemExit(
                f"{experiment_id} contract sample coverage differs from the preregistered program"
            )
        if args.trials != program_items[experiment_id]["trials_per_arm"]:
            raise SystemExit(
                f"{experiment_id} preregisters {program_items[experiment_id]['trials_per_arm']} trials, got {args.trials}"
            )

    version = cli_version()
    source_hashes = {
        str(path.relative_to(ROOT)): sha256_file(path)
        for path in (FIXTURES, OUTPUT_SCHEMA, PROGRAM, Path(__file__).resolve())
    }
    source_bundle_hash = sha256_bytes(json.dumps(source_hashes, sort_keys=True).encode("utf-8"))
    fixture_hash = source_hashes[str(FIXTURES.relative_to(ROOT))]
    skill_hash = sha256_file(ROOT / ".agents/skills/complex-runtime/SKILL.md")

    prompts: dict[tuple[str, str, str], str] = {}
    jobs: list[dict[str, Any]] = []
    for experiment_id in selected:
        fixture = fixtures[experiment_id]
        aliases = sample_aliases(fixture)
        for arm in ("baseline", "candidate"):
            for sample in fixture["samples"]:
                sample_id = sample["sample_id"]
                prompt = build_prompt(experiment_id, arm, fixture, sample)
                if sample_id in prompt:
                    raise SystemExit(f"semantic sample id leaked into prompt: {experiment_id}/{sample_id}")
                prompts[(experiment_id, arm, sample_id)] = prompt
                for trial in range(1, args.trials + 1):
                    jobs.append(
                        {
                            "experiment_id": experiment_id,
                            "arm": arm,
                            "sample_id": sample_id,
                            "sample_alias": aliases[sample_id],
                            "trial": trial,
                            "model": args.model,
                            "prompt": prompt,
                        }
                    )

    # Keep arm and sample order from becoming a hidden runtime variable.
    random.Random(source_bundle_hash).shuffle(jobs)

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.max_workers) as executor:
        trial_results = list(executor.map(run_trial, jobs))

    grouped: dict[str, dict[str, dict[str, list[dict[str, Any]]]]] = defaultdict(
        lambda: defaultdict(lambda: defaultdict(list))
    )
    for result in trial_results:
        grouped[result["experiment_id"]][result["arm"]][result["sample_id"]].append(result)
    for by_arm in grouped.values():
        for by_sample in by_arm.values():
            for values in by_sample.values():
                values.sort(key=lambda item: item["trial"])

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    RECORDS_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_tag = f"{timestamp}-{source_bundle_hash[:10]}-{safe_slug(args.model)}"
    result_relative = f"docs/evals/results/contract-screen-{run_tag}.json"
    result_path = ROOT / result_relative
    if result_path.exists():
        raise SystemExit(f"append-only result already exists: {result_path}")

    compact_results: dict[str, Any] = {
        "version": "2.0",
        "run_id": run_tag,
        "kind": "contract_legibility_screen",
        "model": args.model,
        "cli_version": version,
        "source_hashes": source_hashes,
        "source_bundle_hash": source_bundle_hash,
        "experiments": {},
    }
    records: list[tuple[Path, dict[str, Any]]] = []
    for experiment_id in selected:
        fixture = fixtures[experiment_id]
        arm_scores = {
            arm: score_arm(experiment_id, arm, fixture, grouped[experiment_id][arm])
            for arm in ("baseline", "candidate")
        }
        prompt_hashes = {
            arm: sha256_bytes(
                json.dumps(
                    {
                        sample_id: prompts[(experiment_id, arm, sample_id)]
                        for sample_id in sorted(grouped[experiment_id][arm])
                    },
                    sort_keys=True,
                ).encode("utf-8")
            )
            for arm in ("baseline", "candidate")
        }
        record = build_record(
            program_items[experiment_id],
            fixture,
            arm_scores,
            grouped[experiment_id],
            args.model,
            version,
            result_relative,
            source_bundle_hash,
            fixture_hash,
            skill_hash,
            prompt_hashes,
        )
        signal = automated_signal(fixture, arm_scores["baseline"], arm_scores["candidate"])
        compact_results["experiments"][experiment_id] = {
            "primary_mechanism_id": program_items[experiment_id]["primary_mechanism_id"],
            "external_borrowing": program_items[experiment_id]["external_borrowing"],
            "changed_variable": program_items[experiment_id]["changed_variable"],
            "prompt_hashes": prompt_hashes,
            "sample_count": len(fixture["samples"]),
            "trials_per_sample_per_arm": args.trials,
            "scores": arm_scores,
            "automated_screen_signal": signal,
            "validity": {
                "semantic_sample_ids_hidden": True,
                "one_sample_per_process": True,
                "fixture_oracle_visible_to_subject": False,
                "executable_environment": False,
                "human_review": "pending",
            },
            "trials": {
                arm: {
                    sample_id: [
                        {
                            "trial": trial["trial"],
                            "payload": trial["payload"],
                            "error": trial["error"],
                            "command_attempts": trial["command_attempts"],
                        }
                        for trial in grouped[experiment_id][arm][sample_id]
                    ]
                    for sample_id in sorted(grouped[experiment_id][arm])
                }
                for arm in ("baseline", "candidate")
            },
        }
        record_path = RECORDS_DIR / f"{experiment_id}-contract-screen-{run_tag}.json"
        if record_path.exists():
            raise SystemExit(f"append-only record already exists: {record_path}")
        records.append((record_path, record))

    result_path.write_text(json.dumps(compact_results, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for path, record in records:
        path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(
        json.dumps(
            {
                "run_id": run_tag,
                "kind": "contract_legibility_screen",
                "experiments": selected,
                "jobs": len(jobs),
                "result": result_relative,
                "records": [str(path.relative_to(ROOT)) for path, _ in records],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
