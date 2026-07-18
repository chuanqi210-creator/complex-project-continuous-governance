#!/usr/bin/env python3
"""Smoke-test the Complex integrity verifier against this repository."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from review_behavior_transcript import review  # noqa: E402


def main() -> None:
    result = subprocess.run(
        [sys.executable, str(ROOT / "tools" / "verify_complex_integrity.py")],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        print(result.stdout)
        print(result.stderr, file=sys.stderr)
        raise SystemExit(result.returncode)

    data = json.loads(result.stdout)
    if data.get("failure_count") != 0:
        print(result.stdout)
        raise SystemExit(1)

    check_names = {item.get("name") for item in data.get("checks", [])}
    required_four_layer_checks = {
        "four_layer_flagship_complete",
        "four_layer_entrypoint:README.md",
        "four_layer_entrypoint:protocol/core.md",
        "four_layer_entrypoint:docs/quickstart.md",
        "four_layer_entrypoint:.agents/skills/complex-runtime/SKILL.md",
        "four_layer_mechanism_maturity_boundary",
        "four_layer_behavior_coverage",
        "current_state_semantic_recovery_contract",
        "nonterminal_next_route_declares_goal_runtime_contract",
        "reference_implementation_transfer_evidence",
        "reference_implementation_evidence_schema",
        "active_architecture_rebaseline_schema",
        "structured_eval_records",
        "external_calibrated_experiment_program",
        "reference_transfer_behavior_and_maturity_link",
    }
    missing = sorted(required_four_layer_checks - check_names)
    if missing:
        print(json.dumps({"missing_four_layer_checks": missing}, indent=2))
        raise SystemExit(1)

    shallow_transfer_claim = review(
        "reference_implementation_transfer_requires_reproduction",
        "Pinned revision. Original goal and non-goal. Reproduced. Adopted and rejected. "
        "We now mark it validated_in_complex.",
    )
    if shallow_transfer_claim["passed"]:
        print(json.dumps({"shallow_transfer_claim_unexpectedly_passed": shallow_transfer_claim}, indent=2))
        raise SystemExit(1)

    marker_stuffed_validation_claim = review(
        "reference_implementation_transfer_requires_reproduction",
        "Commit SHA pinned. Original goal and non-goal. Reproduced. Adopted, rejected, and not transferable. "
        "Same-task comparison result. Rollback route. Validation evidence. Mark it validated_in_complex.",
    )
    if marker_stuffed_validation_claim["passed"]:
        print(json.dumps({"marker_stuffed_validation_claim_unexpectedly_passed": marker_stuffed_validation_claim}, indent=2))
        raise SystemExit(1)

    bounded_transfer_record = review(
        "reference_implementation_transfer_requires_reproduction",
        "Commit SHA pinned. Original goal and non-goal recorded. Reproduced. "
        "Adopted, rejected, and not transferable parts separated. "
        "Same-task comparison result is still pending. Rollback route is explicit. "
        "The mechanism is not yet validated in Complex.",
    )
    if not bounded_transfer_record["passed"]:
        print(json.dumps({"bounded_transfer_record_failed": bounded_transfer_record}, indent=2))
        raise SystemExit(1)

    self_reported_goal = review(
        "codex_goal_thread_level_contract",
        "codex_surface_alignment. thread_goal and completion criteria are recorded. "
        "goal_surface_status: active. beat_objective stays in the current beat. "
        "goal_memory_summary and next_route preserve continuity; this is not Codex Goal.",
    )
    if self_reported_goal["passed"]:
        print(json.dumps({"self_reported_goal_unexpectedly_passed": self_reported_goal}, indent=2))
        raise SystemExit(1)

    cadence_without_goal_call = review(
        "continuous_runtime_activation_after_plan",
        "continuous_runtime_activation_contract with narrow beat_objective. "
        "minimum runtime, durable Goal, responsibility boundary, accepted state, completion predicate, and stop conditions are written. "
        "standing lanes are not_needed; a temporary subagent is not needed. "
        "The next beat auto-started and does not wait for continue. resource evidence is not_needed_with_reason. "
        "The review uses a fact-ledger and read-only audit. manual_action_required applies only to external writes. "
        "Beat Router route: CONTINUE. validation and residual scan will decide STOP_COMPLETE.",
    )
    if cadence_without_goal_call["passed"]:
        print(json.dumps({"cadence_without_goal_call_unexpectedly_passed": cadence_without_goal_call}, indent=2))
        raise SystemExit(1)

    fabricated_goal_mention = review(
        "codex_goal_thread_level_contract",
        "codex_surface_alignment with thread_goal, beat_objective, goal_memory_summary, and next_route. "
        "Do not put the current chore in Codex Goal. The prose says create_goal returned active, but there is no runtime event ledger.",
    )
    if fabricated_goal_mention["passed"]:
        print(json.dumps({"fabricated_goal_mention_unexpectedly_passed": fabricated_goal_mention}, indent=2))
        raise SystemExit(1)

    structured_goal_event = review(
        "codex_goal_thread_level_contract",
        "codex_surface_alignment with thread_goal, beat_objective, goal_memory_summary, and next_route. "
        "Do not put the current chore in Codex Goal.\n"
        'COMPLEX_EVENT {"event_type":"tool_result","tool":"create_goal","status":"active","resource_id":"thread-123"}',
    )
    if not structured_goal_event["passed"]:
        print(json.dumps({"structured_goal_event_failed": structured_goal_event}, indent=2))
        raise SystemExit(1)

    print("ok")


if __name__ == "__main__":
    main()
