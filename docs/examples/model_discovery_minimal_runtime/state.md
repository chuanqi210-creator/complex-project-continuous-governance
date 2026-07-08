# State Example: Model Discovery

## Current State

- thread_goal: Discover a strong explanation framework before evidence filling.
- project_nature: model_discovery
- convergence_status: pre_convergence
- current_basis:
  - User wants framework discovery before evidence table work.
  - Several plausible explanation paths exist.
  - No single model has been selected.
- not_current_basis:
  - Any first-pass framework treated as final.
  - Evidence rows that assume a model not yet chosen.

## Behavior Kernel

- restore true state: framework unsettled; evidence table not yet primary.
- classify nature: model_discovery.
- decision rights: AI may generate, merge, and reject candidate frameworks; ask before changing the project goal or delivery audience.
- highest target-function question: which candidate framework best explains the project's core tension?
- target-function Loop: run a discriminating probe across candidate frameworks.
- delivery contract: interim human-readable explanation of options, not final proof.
- next-route recovery: converge only when conditions are met; otherwise keep candidate pool.

## Adaptive Judgment

- judgment_mode: exploratory
- autonomy_level: strong_autonomy_with_guardrails
- decision_right: ai_decide
- ask_user_needed: no
- ai_decided_without_user_reason: Candidate generation and probe design are reversible and directly serve the unsettled frame.
- rollback_or_recovery_route: If a chosen framework fails the probe, return to candidate pool and argument map.

## Goal State

- goal_memory_summary: Find a project framing that can later be supported by evidence.
- beat_objective: Produce 3-5 candidate frameworks and one discriminating probe.
- next_route: run_probe_then_decide_converge_or_continue_discovery

## Attention Governance And Closure

- minimum_viable_closure_status: missing
- closure_chain: candidate question exists, but source/data path, minimal model, result, claim, and limitation are not yet connected.
- minimum_sufficient_observability_status: light_signal_enough
- last_progress_signal: This beat should move the framing segment by producing a probe that can later connect to evidence.
- heavy_audit_trigger: convergence decision, public-facing framework claim, or missing closure after startup window.

## External Calibration

- source: Double Diamond; Tree/Graph of Thoughts; IBIS.
- problem_matched: an unsettled frame can collapse too early into one evidence path.
- adopted: keep candidate frameworks, issue-position-argument map, and discriminating probes visible.
- rejected: large workshop or diagram ceremony.
- not_transferable: assuming design-process stages map exactly to every research task.
- Complex_micro_contract: before convergence, keep 3-5 candidates, one pro/con map, and one probe that can reject or downgrade a frame.
- refresh_trigger: candidate pool narrows, audience changes, or evidence path becomes clear.

## Hallucination Sentinel

- current_basis: several plausible frames exist.
- external_basis: divergence/convergence and thought-search methods.
- inference: preserving candidates lowers premature convergence risk.
- unsupported_claim: one candidate is already the correct final frame.
- falsification_cue: the chosen frame lacks a feasible evidence path.
