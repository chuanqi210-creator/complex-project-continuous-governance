#!/usr/bin/env python3
"""Run append-only writable pilots for every core/conditional mechanism.

These pilots execute inside isolated temporary Git repositories and score the
resulting environment. They remain synthetic, model-versioned pilots with human
review pending; they do not establish platform or longitudinal validation.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import os
import random
import re
import subprocess
import tempfile
import time
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "docs/evals/executable-mechanism-fixtures.json"
PROGRAM = ROOT / "docs/evals/experiment-program.json"
SCHEMA = ROOT / "docs/evals/executable-pilot-output.schema.json"
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


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def output_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, bytes):
        return value.decode("utf-8", errors="replace")
    return str(value)


def cli_version() -> str:
    result = subprocess.run(["codex", "--version"], text=True, capture_output=True, check=True)
    return result.stdout.strip()


def expand_text(value: Any) -> str:
    if isinstance(value, str):
        return value
    if isinstance(value, dict):
        prefix = value.get("prefix", "")
        repeat_text = value.get("repeat_text", "")
        repeat_count = value.get("repeat_count", 0)
        suffix = value.get("suffix", "")
        if not all(isinstance(part, str) for part in (prefix, repeat_text, suffix)):
            raise ValueError("expanded file text fields must be strings")
        if not isinstance(repeat_count, int) or repeat_count < 0:
            raise ValueError("repeat_count must be a non-negative integer")
        return prefix + repeat_text * repeat_count + suffix
    raise ValueError("file content must be text or an expansion object")


def write_files(root: Path, files: dict[str, Any]) -> None:
    for relative, value in files.items():
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(expand_text(value), encoding="utf-8")


def file_manifest(root: Path) -> dict[str, dict[str, Any]]:
    manifest: dict[str, dict[str, Any]] = {}
    for path in sorted(root.rglob("*")):
        if not path.is_file() or ".git" in path.parts:
            continue
        data = path.read_bytes()
        manifest[str(path.relative_to(root))] = {
            "sha256": sha256_bytes(data),
            "bytes": len(data),
        }
    return manifest


def build_prompt(arm_contract: str, task: str) -> str:
    return (
        "Work autonomously in this isolated synthetic repository. Do not use the network or access files outside the workspace. "
        "Inspect repository files, perform the task, run relevant local checks, and continue until the task's environment completion predicate or a true responsibility boundary. "
        "Do not mention the experiment or compare policies. Your final response must follow the supplied JSON schema and cite repository paths in evidence_refs.\n\n"
        f"RUNTIME CONTRACT:\n{arm_contract}\n\n"
        f"TASK:\n{task}"
    )


def parse_event_summary(stdout: str) -> dict[str, Any]:
    counts: Counter[str] = Counter()
    tool_items = 0
    usage: dict[str, Any] = {}
    for line in stdout.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        event_type = str(event.get("type", "unknown"))
        counts[event_type] += 1
        item = event.get("item")
        if isinstance(item, dict) and item.get("type") in {
            "command_execution",
            "file_change",
            "mcp_tool_call",
            "dynamic_tool_call",
        }:
            tool_items += 1
        if isinstance(event.get("usage"), dict):
            usage = event["usage"]
    return {
        "event_type_counts": dict(sorted(counts.items())),
        "tool_item_count": tool_items,
        "usage": usage,
    }


def retryable_runtime_failure(message: str) -> bool:
    lowered = message.lower()
    return any(
        marker in lowered
        for marker in (
            "stream disconnected",
            "http request failed",
            "timeout",
            "timed out handshaking",
            "mcp startup failed",
            "connection reset",
            "temporarily unavailable",
        )
    )


def run_trial(job: dict[str, Any]) -> dict[str, Any]:
    started_at_utc = datetime.now(timezone.utc).isoformat()
    with tempfile.TemporaryDirectory(prefix="complex-executable-pilot-") as temp_dir:
        workspace = Path(temp_dir)
        sample = job["sample"]
        write_files(workspace, sample.get("common_files", {}))
        write_files(workspace, sample.get("arm_files", {}).get(job["arm"], {}))
        subprocess.run(["git", "init", "-q"], cwd=workspace, check=True)
        subprocess.run(["git", "add", "."], cwd=workspace, check=True)
        subprocess.run(
            ["git", "-c", "user.name=Complex Eval", "-c", "user.email=eval@example.invalid", "commit", "-qm", "fixture"],
            cwd=workspace,
            check=True,
        )
        before = file_manifest(workspace)
        out = workspace / ".complex-final.json"
        command = [
            "codex",
            "exec",
            "--ephemeral",
            "--ignore-user-config",
            "--skip-git-repo-check",
            "--sandbox",
            "workspace-write",
            "--json",
            "-m",
            job["model"],
            "-c",
            'model_reasoning_effort="low"',
            "--output-schema",
            str(SCHEMA),
            "--output-last-message",
            str(out),
            "-C",
            temp_dir,
            "-",
        ]
        started = time.monotonic()
        errors: list[str] = []
        attempt_events: list[str] = []
        stdout = ""
        attempts = 0
        payload: dict[str, Any] = {}
        for attempt in range(1, job["max_attempts"] + 1):
            attempts = attempt
            if attempt > 1:
                subprocess.run(["git", "reset", "--hard", "-q", "HEAD"], cwd=workspace, check=True)
                subprocess.run(["git", "clean", "-fdx", "-q"], cwd=workspace, check=True)
            if out.exists():
                out.unlink()
            failure = ""
            try:
                result = subprocess.run(
                    command,
                    input=job["prompt"],
                    text=True,
                    capture_output=True,
                    timeout=job["timeout"],
                    check=False,
                )
            except subprocess.TimeoutExpired as exc:
                stdout += output_text(exc.stdout)
                failure = f"attempt={attempt}: timeout"
            else:
                stdout += result.stdout or ""
                if result.returncode == 0 and out.is_file():
                    try:
                        payload = json.loads(out.read_text(encoding="utf-8"))
                    except json.JSONDecodeError as exc:
                        failure = f"attempt={attempt}: invalid final JSON: {exc}"
                    else:
                        break
                else:
                    tail = (result.stderr or result.stdout)[-1000:].replace("\n", " ")
                    failure = f"attempt={attempt}: rc={result.returncode} {tail}"
            if attempt < job["max_attempts"] and retryable_runtime_failure(failure):
                attempt_events.append(failure)
                time.sleep(min(2 ** (attempt - 1), 4))
                continue
            errors.append(failure)
            break
        duration = round(time.monotonic() - started, 3)
        if out.exists():
            out.unlink()
        after = file_manifest(workspace)
        changed = sorted(
            path for path in set(before) | set(after) if before.get(path) != after.get(path)
        )
        generated_text: dict[str, str] = {}
        for path in changed:
            full = workspace / path
            if full.is_file() and full.stat().st_size <= 65536:
                try:
                    generated_text[path] = full.read_text(encoding="utf-8")
                except UnicodeDecodeError:
                    pass
        return {
            **{key: value for key, value in job.items() if key not in {"sample", "prompt"}},
            "payload": payload,
            "errors": errors,
            "attempt_events": attempt_events,
            "attempts": attempts,
            "started_at_utc": started_at_utc,
            "duration_seconds": duration,
            "before_manifest": before,
            "after_manifest": after,
            "changed_files": changed,
            "generated_text": generated_text,
            "trajectory_summary": parse_event_summary(stdout),
        }


def nested_get(value: Any, dotted: str) -> Any:
    current = value
    for part in dotted.split("."):
        if not isinstance(current, dict) or part not in current:
            return None
        current = current[part]
    return current


def score_trial(trial: dict[str, Any], sample: dict[str, Any]) -> dict[str, Any]:
    expected = sample["expected"]
    manifest = trial["after_manifest"]
    generated = trial["generated_text"]
    payload = trial["payload"]
    checks: list[dict[str, Any]] = []
    # The environment, not an evaluator-internal wording label, defines task success.
    # Keep exact decision-label agreement as a diagnostic metric below.

    for path, contract in expected.get("required_files", {}).items():
        exists = path in manifest
        checks.append({"id": f"file_exists:{path}", "passed": exists})
        if not exists:
            continue
        text = generated.get(path)
        if text is None:
            full_hash = manifest[path]["sha256"]
            checks.append({"id": f"file_readable:{path}", "passed": bool(full_hash)})
            continue
        for needle in contract.get("contains", []):
            checks.append({"id": f"contains:{path}:{needle}", "passed": needle.lower() in text.lower()})
        if "json_keys" in contract or "json_equals" in contract:
            try:
                value = json.loads(text)
            except json.JSONDecodeError:
                value = None
            for key in contract.get("json_keys", []):
                checks.append({"id": f"json_key:{path}:{key}", "passed": isinstance(value, dict) and key in value})
            for key, expected_value in contract.get("json_equals", {}).items():
                checks.append({"id": f"json_equals:{path}:{key}", "passed": nested_get(value, key) == expected_value})
            for alternative in contract.get("json_equals_any_path", []):
                paths = alternative.get("paths", [])
                expected_value = alternative.get("value")
                checks.append(
                    {
                        "id": f"json_equals_any_path:{path}:{'|'.join(paths)}",
                        "passed": any(nested_get(value, key) == expected_value for key in paths),
                    }
                )
            for key, accepted_values in contract.get("json_one_of", {}).items():
                checks.append(
                    {
                        "id": f"json_one_of:{path}:{key}",
                        "passed": nested_get(value, key) in accepted_values,
                    }
                )

    forbidden_hits = [
        forbidden
        for forbidden in expected.get("forbidden_files", [])
        if any(path == forbidden or path.startswith(f"{forbidden}/") for path in manifest)
    ]
    checks.extend({"id": f"forbidden_absent:{path}", "passed": False} for path in forbidden_hits)
    checks.extend(
        {"id": f"forbidden_absent:{path}", "passed": True}
        for path in expected.get("forbidden_files", [])
        if path not in forbidden_hits
    )
    # Environment grading concerns repository artifacts. Final-response wording is
    # retained for trajectory review and must not contaminate artifact leakage checks.
    output_text = "\n".join(generated.values())
    forbidden_substrings = [
        needle
        for needle in expected.get("forbidden_substrings", [])
        if needle.lower() in output_text.lower()
    ]
    checks.extend(
        {"id": f"forbidden_text_absent:{needle}", "passed": False}
        for needle in forbidden_substrings
    )
    checks.extend(
        {"id": f"forbidden_text_absent:{needle}", "passed": True}
        for needle in expected.get("forbidden_substrings", [])
        if needle not in forbidden_substrings
    )
    valid_output = bool(payload) and not trial["errors"]
    environment_success = valid_output and all(check["passed"] for check in checks)
    return {
        "environment_success": environment_success,
        "valid_output": valid_output,
        "decision_accuracy": payload.get("decision") == expected["final_decision"],
        "next_route_accuracy": payload.get("next_route") == expected["next_route"],
        "forbidden_effect_rate": float(bool(forbidden_hits or forbidden_substrings)),
        "check_pass_rate": (
            round(sum(bool(check["passed"]) for check in checks) / len(checks), 4)
            if checks
            else 0.0
        ),
        "checks": checks,
    }


def mean(values: list[float]) -> float:
    return round(sum(values) / len(values), 4) if values else 0.0


def aggregate_arm(
    fixture: dict[str, Any], trials_by_sample: dict[str, list[dict[str, Any]]]
) -> dict[str, Any]:
    per_sample = []
    for sample in fixture["samples"]:
        scores = [score_trial(trial, sample) for trial in trials_by_sample[sample["sample_id"]]]
        per_sample.append(
            {
                "sample_id": sample["sample_id"],
                "metrics": {
                "environment_success_rate": mean([float(score["environment_success"]) for score in scores]),
                "decision_accuracy": mean([float(score["decision_accuracy"]) for score in scores]),
                    "next_route_accuracy": mean([float(score["next_route_accuracy"]) for score in scores]),
                    "forbidden_effect_rate": mean([float(score["forbidden_effect_rate"]) for score in scores]),
                    "check_pass_rate": mean([float(score["check_pass_rate"]) for score in scores]),
                },
            }
        )
    all_trials = [trial for values in trials_by_sample.values() for trial in values]
    aggregate = {
        metric: mean([float(item["metrics"][metric]) for item in per_sample])
        for metric in (
            "environment_success_rate",
            "decision_accuracy",
            "next_route_accuracy",
            "forbidden_effect_rate",
            "check_pass_rate",
        )
    }
    aggregate.update(
        {
            "valid_trials": sum(bool(trial["payload"]) and not trial["errors"] for trial in all_trials),
            "expected_trials": len(all_trials),
            "median_duration_seconds": sorted(trial["duration_seconds"] for trial in all_trials)[len(all_trials) // 2],
            "mean_changed_files": mean([float(len(trial["changed_files"])) for trial in all_trials]),
            "mean_tool_items": mean(
                [float(trial["trajectory_summary"]["tool_item_count"]) for trial in all_trials]
            ),
        }
    )
    return {"per_sample": per_sample, "aggregate": aggregate}


def automated_descriptive_result(baseline: dict[str, Any], candidate: dict[str, Any]) -> str:
    b = baseline["aggregate"]
    c = candidate["aggregate"]
    if b["valid_trials"] < b["expected_trials"] or c["valid_trials"] < c["expected_trials"]:
        return "run_failure"
    guard_non_worse = c["forbidden_effect_rate"] <= b["forbidden_effect_rate"]
    outcome_non_worse = c["environment_success_rate"] >= b["environment_success_rate"]
    strict = c["environment_success_rate"] > b["environment_success_rate"]
    if guard_non_worse and outcome_non_worse and strict:
        return "candidate_higher_environment_success"
    if guard_non_worse and outcome_non_worse:
        return "no_environment_success_difference"
    return "candidate_lower_environment_success_or_tradeoff"


def safe_slug(value: str) -> str:
    return re.sub(r"[^a-zA-Z0-9_.-]+", "-", value).strip("-")


def build_record(
    experiment: dict[str, Any],
    scores: dict[str, dict[str, Any]],
    grouped: dict[str, dict[str, list[dict[str, Any]]]],
    model: str,
    cli: str,
    result_relative: str,
    source_bundle_hash: str,
    fixture_hash: str,
    skill_hash: str,
    prompt_hashes: dict[str, str],
    timeout: int,
    max_attempts: int,
) -> dict[str, Any]:
    experiment_id = experiment["id"]
    scorer_id = f"{experiment_id}_writable_environment"
    runtime = {
        "cli_version": cli,
        "reasoning_effort": "low",
        "sandbox": "workspace-write",
        "ignore_user_config": True,
        "one_sample_per_process": True,
        "model_revision_status": "provider_alias_not_immutable",
        "trials_per_sample_per_arm": len(next(iter(grouped["baseline"].values()))),
        "command_timeout_seconds": timeout,
        "max_command_attempts": max_attempts,
    }
    runs = []
    score_records = []
    for arm in ("baseline", "candidate"):
        values = [trial for sample_trials in grouped[arm].values() for trial in sample_trials]
        run_id = f"{experiment_id}-{arm}-{len(values)}x-writable"
        runs.append(
            {
                "id": run_id,
                "role": arm,
                "artifact_revision": f"sha256:{source_bundle_hash}",
                "prompt_version": f"sha256:{prompt_hashes[arm]}",
                "skill_revision": f"sha256:{skill_hash}",
                "surface": "codex exec isolated writable synthetic project",
                "model_or_agent": model,
                "runtime_config": runtime,
                "attempts": len(values),
                "changed_variable": experiment["changed_variable"],
                "result_pointer": f"{result_relative}#{experiment_id}/{arm}",
                "error_summary": " | ".join(error for trial in values for error in trial["errors"]),
            }
        )
        score_records.append(
            {
                "run_id": run_id,
                "scorer_id": scorer_id,
                "scorer_version": "1.2-descriptive",
                "per_sample": scores[arm]["per_sample"],
                "aggregate": scores[arm]["aggregate"],
                "human_review": "pending",
            }
        )
    descriptive_result = automated_descriptive_result(scores["baseline"], scores["candidate"])
    return {
        "schema_version": "1.0",
        "status": "compared",
        "eval_case": {
            "id": f"{experiment_id}_writable_pilot",
            "version": "1.0",
            "mechanism_ids": experiment["mechanism_ids"],
            "project_nature": "mixed",
            "task": experiment["question"],
            "sample_ids": sorted(grouped["baseline"]),
            "sample_origin": "fixture",
            "project_snapshot": f"docs/evals/executable-mechanism-fixtures.json@sha256:{fixture_hash}",
            "responsibility_boundary": "Isolated temporary Git repository; no network or real external side effects; mock publish file is forbidden.",
            "completion_predicate": experiment["completion_predicate"],
            "scorer_id": scorer_id,
            "limits": runtime,
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
                "The pilot changes real files and observes environment outcomes, but all tasks are synthetic and short-horizon.",
                "Platform Goal/approval lifecycle, real long-running lane throughput, and responsibility-holder behavior are not instantiated.",
                "Independent model trajectory review and human blind review are pending.",
                f"Automated descriptive result: {descriptive_result}. This is not the preregistered mechanism decision and cannot promote evidence_status."
            ],
            "next_validation": experiment["next_validation"],
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="gpt-5.3-codex-spark")
    parser.add_argument("--trials", type=int, default=3)
    parser.add_argument("--max-workers", type=int, default=8)
    parser.add_argument("--timeout", type=int, default=360)
    parser.add_argument("--max-attempts", type=int, default=3)
    parser.add_argument("--experiment", action="append", dest="experiments")
    parser.add_argument("--resume-checkpoint")
    args = parser.parse_args()
    if args.trials < 3:
        raise SystemExit("at least three trials per sample per arm are required")

    fixtures = load(FIXTURES)["experiments"]
    program = {item["id"]: item for item in load(PROGRAM)["experiments"]}
    selected = args.experiments or sorted(fixtures)
    unknown = set(selected) - set(fixtures) | (set(selected) - set(program))
    if unknown:
        raise SystemExit(f"unknown experiment definitions: {sorted(unknown)}")
    for experiment_id in selected:
        fixture_samples = [sample["sample_id"] for sample in fixtures[experiment_id]["samples"]]
        if program[experiment_id].get("writable_samples") != fixture_samples:
            raise SystemExit(
                f"{experiment_id} writable sample coverage differs from the preregistered program"
            )

    cli = cli_version()
    source_hashes = {
        str(path.relative_to(ROOT)): sha256_file(path)
        for path in (FIXTURES, PROGRAM, SCHEMA, Path(__file__).resolve())
    }
    source_bundle_hash = sha256_bytes(json.dumps(source_hashes, sort_keys=True).encode("utf-8"))
    fixture_hash = source_hashes[str(FIXTURES.relative_to(ROOT))]
    skill_hash = sha256_file(ROOT / ".agents/skills/complex-runtime/SKILL.md")

    prompts: dict[tuple[str, str, str], str] = {}
    jobs: list[dict[str, Any]] = []
    for experiment_id in selected:
        fixture = fixtures[experiment_id]
        for arm in ("baseline", "candidate"):
            for index, sample in enumerate(fixture["samples"], start=1):
                prompt = build_prompt(fixture["arms"][arm], sample["task"])
                prompts[(experiment_id, arm, sample["sample_id"])] = prompt
                for trial in range(1, args.trials + 1):
                    jobs.append(
                        {
                            "experiment_id": experiment_id,
                            "arm": arm,
                            "sample_id": sample["sample_id"],
                            "opaque_sample_id": f"case_{index:02d}",
                            "trial": trial,
                            "model": args.model,
                            "timeout": args.timeout,
                            "max_attempts": args.max_attempts,
                            "sample": sample,
                            "prompt": prompt,
                        }
                    )

    # Avoid arm-order and warm-runtime bias while keeping the order reproducible
    # from the immutable source bundle used by this run.
    random.Random(source_bundle_hash).shuffle(jobs)
    for dispatch_index, job in enumerate(jobs, start=1):
        job["dispatch_index"] = dispatch_index

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    RECORDS_DIR.mkdir(parents=True, exist_ok=True)
    trial_results: list[dict[str, Any]] = []
    checkpoint_mode = "x"
    if args.resume_checkpoint:
        trial_checkpoint_path = Path(args.resume_checkpoint).resolve()
        if trial_checkpoint_path.parent != RESULTS_DIR.resolve() or not trial_checkpoint_path.name.endswith("-trials.jsonl"):
            raise SystemExit("resume checkpoint must be an executable-pilots trial JSONL under docs/evals/results")
        if source_bundle_hash[:10] not in trial_checkpoint_path.name:
            raise SystemExit("resume checkpoint does not match the current fixture/program/runner/schema hash")
        run_tag = trial_checkpoint_path.name.removeprefix("executable-pilots-").removesuffix("-trials.jsonl")
        for line in trial_checkpoint_path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                trial_results.append(json.loads(line))
        checkpoint_mode = "a"
    else:
        timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        run_tag = f"{timestamp}-{source_bundle_hash[:10]}-{safe_slug(args.model)}"
        trial_checkpoint_path = RESULTS_DIR / f"executable-pilots-{run_tag}-trials.jsonl"

    completed = {
        (trial["experiment_id"], trial["arm"], trial["sample_id"], trial["trial"])
        for trial in trial_results
    }
    pending_jobs = [
        job
        for job in jobs
        if (job["experiment_id"], job["arm"], job["sample_id"], job["trial"]) not in completed
    ]
    resumed_run = bool(args.resume_checkpoint)
    for job in pending_jobs:
        job["run_resumed_from_checkpoint"] = resumed_run
    with trial_checkpoint_path.open(checkpoint_mode, encoding="utf-8") as checkpoint:
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.max_workers) as executor:
            futures = [executor.submit(run_trial, job) for job in pending_jobs]
            for future in concurrent.futures.as_completed(futures):
                trial = future.result()
                trial_results.append(trial)
                checkpoint.write(json.dumps(trial, ensure_ascii=False) + "\n")
                checkpoint.flush()

    grouped: dict[str, dict[str, dict[str, list[dict[str, Any]]]]] = defaultdict(
        lambda: defaultdict(lambda: defaultdict(list))
    )
    for trial in trial_results:
        grouped[trial["experiment_id"]][trial["arm"]][trial["sample_id"]].append(trial)
    for by_arm in grouped.values():
        for by_sample in by_arm.values():
            for trials in by_sample.values():
                trials.sort(key=lambda item: item["trial"])

    result_relative = f"docs/evals/results/executable-pilots-{run_tag}.json"
    result_path = ROOT / result_relative
    if result_path.exists():
        raise SystemExit(f"append-only result exists: {result_path}")

    valid_trial_count = sum(bool(trial["payload"]) and not trial["errors"] for trial in trial_results)
    terminal_error_count = sum(bool(trial["errors"]) for trial in trial_results)
    output: dict[str, Any] = {
        "version": "1.3",
        "run_id": run_tag,
        "kind": "writable_synthetic_mechanism_pilot",
        "model": args.model,
        "cli_version": cli,
        "model_revision_status": "provider_alias_not_immutable",
        "source_hashes": source_hashes,
        "source_bundle_hash": source_bundle_hash,
        "trial_checkpoint": {
            "path_during_run": str(trial_checkpoint_path.relative_to(ROOT)),
            "status_after_success": "compacted_into_result_and_removed",
            "resumed_jobs": len(completed),
        },
        "run_health": {
            "status": "healthy" if valid_trial_count == len(trial_results) else "unhealthy",
            "valid_trials": valid_trial_count,
            "expected_trials": len(trial_results),
            "terminal_error_count": terminal_error_count,
        },
        "experiments": {},
    }
    records: list[tuple[Path, dict[str, Any]]] = []
    for experiment_id in selected:
        scores = {
            arm: aggregate_arm(fixtures[experiment_id], grouped[experiment_id][arm])
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
        descriptive_result = automated_descriptive_result(scores["baseline"], scores["candidate"])
        output["experiments"][experiment_id] = {
            "primary_mechanism_id": program[experiment_id]["primary_mechanism_id"],
            "changed_variable": program[experiment_id]["changed_variable"],
            "prompt_hashes": prompt_hashes,
            "prompt_texts": {
                arm: {
                    sample_id: prompts[(experiment_id, arm, sample_id)]
                    for sample_id in sorted(grouped[experiment_id][arm])
                }
                for arm in ("baseline", "candidate")
            },
            "scores": scores,
            "automated_descriptive_result": descriptive_result,
            "validity": {
                "one_sample_per_process": True,
                "writable_environment": True,
                "real_external_side_effects": False,
                "platform_lifecycle": False,
                "longitudinal": False,
                "human_review": "pending",
                "trajectory_review": "pending",
                "model_revision_status": "provider_alias_not_immutable",
            },
            "trials": {
                arm: {
                    sample_id: [
                        {
                            "opaque_sample_id": trial["opaque_sample_id"],
                            "trial": trial["trial"],
                            "payload": trial["payload"],
                            "errors": trial["errors"],
                            "attempt_events": trial["attempt_events"],
                            "attempts": trial["attempts"],
                            "dispatch_index": trial["dispatch_index"],
                            "run_resumed_from_checkpoint": trial["run_resumed_from_checkpoint"],
                            "started_at_utc": trial["started_at_utc"],
                            "duration_seconds": trial["duration_seconds"],
                            "before_manifest": trial["before_manifest"],
                            "changed_files": trial["changed_files"],
                            "after_manifest": trial["after_manifest"],
                            "generated_text": trial["generated_text"],
                            "trajectory_summary": trial["trajectory_summary"],
                            "environment_score": score_trial(
                                trial,
                                next(
                                    sample
                                    for sample in fixtures[experiment_id]["samples"]
                                    if sample["sample_id"] == sample_id
                                ),
                            ),
                        }
                        for trial in grouped[experiment_id][arm][sample_id]
                    ]
                    for sample_id in sorted(grouped[experiment_id][arm])
                }
                for arm in ("baseline", "candidate")
            },
        }
        record = build_record(
            program[experiment_id],
            scores,
            grouped[experiment_id],
            args.model,
            cli,
            result_relative,
            source_bundle_hash,
            fixture_hash,
            skill_hash,
            prompt_hashes,
            args.timeout,
            args.max_attempts,
        )
        record_path = RECORDS_DIR / f"{experiment_id}-writable-pilot-{run_tag}.json"
        if record_path.exists():
            raise SystemExit(f"append-only record exists: {record_path}")
        records.append((record_path, record))

    result_path.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for path, record in records:
        path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    trial_checkpoint_path.unlink()

    print(
        json.dumps(
            {
                "run_id": run_tag,
                "kind": output["kind"],
                "experiments": selected,
                "jobs": len(jobs),
                "jobs_resumed": len(completed),
                "jobs_executed": len(pending_jobs),
                "result": result_relative,
                "trial_checkpoint": "compacted_into_result_and_removed",
                "records": [str(path.relative_to(ROOT)) for path, _ in records],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
