# Complex Current State

current_version: 2026-07-03

## Recovery Anchor

Complex is in the behavior-compression and runtime-kit phase.

Current narrative:

> Complex = strong-autonomy continuous execution with control-plane orchestration, evidence boundaries, anti-human/context-drift safeguards, and an auditable recovery chain.

Current next route:

`use_real_project_transcripts_or_user_feedback_to_verify_public_onboarding_or_stop`

Default decision:

- Do not add new core gates for one-off failures.
- Prefer behavior cases, transcript review rules, and filled examples before expanding `protocol/core.md`.
- Treat continuous cadence as active runtime activation: per-beat narrow goal, Loop, route, and safe auto-start of the next queued beat.
- Treat continuous projects as control-plane-first: direction, authority, state, topology, routing, and stop conditions must be fresh enough before local execution.
- Distinguish durable lanes from temporary subagents. Standing lanes own recurring project responsibilities; subagents are bounded workers and are not long-running threads.
- For recurring review/evaluation, establish a standing review lane early and reset context with a fresh fact ledger or clean reviewer each review beat.
- Treat continuous orchestration as the default runtime after confirmation: maintain beat queue, per-beat Goal or protocol_round_goal, Beat Router execution, and clear stop conditions.
- Do not treat a fixed number of beats as completion. `STOP_COMPLETE` requires objective completion, delivery-level validation, and a residual-beat scan showing no useful low-risk internal beat remains.
- Continuous work must be visibly auditable in the human-facing final answer: per-beat goals, Goal/protocol_goal source, router decisions, resource evidence or `not_needed/degraded`, validation after the final write, and final residual scan.
- Reset independent review context every review beat; same-session review is diagnostic only.
- When Complex is copied into another repository, reconcile steering words with local rules and true manual-action boundaries before judging activation success or failure.
- Plan mode must design an orchestration contract before continuous execution: capability preflight, resource taxonomy, authorization status, manager/worker split, Beat Router, and stop conditions.
- When another project asks to scan Complex, use the installed Complex runtime as the rule source and the target project as the fact source.
- Keep the active repository free of historical logs and old output packages.

## Active Behavior Spine

1. Restore true state.
2. Classify project nature and convergence.
3. Assign decision rights and ask-user necessity.
4. Set the control plane, then choose the work target.
5. Run the lightest useful validation or execution.
6. Deliver to the right audience.
7. Leave `next_route`.

## Current Runtime Examples

- `docs/examples/evidence_fill_minimal_runtime/`
- `docs/examples/model_discovery_minimal_runtime/`
- `docs/examples/independent_review_minimal_runtime/`

## Current Checks

- `tools/check_behavior_regression_pack.py`
- `tools/review_behavior_transcript.py`
- `tools/verify_complex_integrity.py`

## Stop Rule

Continue improving Complex only when one of these appears:

- a real Complex project transcript
- a user correction event
- a verifier failure
- a public explanation/onboarding failure
- a high-value example gap

Otherwise, keep the current protocol stable and use it on projects.
