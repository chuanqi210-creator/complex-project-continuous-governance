# State Example: Evidence Fill

## Current State

- thread_goal: Complete a source-backed evidence table for a fixed evaluation rubric.
- project_nature: evidence_fill
- convergence_status: converged_model
- current_basis:
  - The metric list is fixed by the user.
  - The output should support a human-readable summary.
  - Only local files and public sources are allowed in this beat.
- not_current_basis:
  - Draft claims without source anchors.
  - Old candidate metrics not in the fixed rubric.

## Behavior Kernel

- restore true state: fixed rubric and current source set recovered.
- classify nature: evidence_fill; no model-discovery expansion.
- decision rights: AI may choose source order and verification depth; ask before external account/API/write actions.
- highest target-function question: which fixed metric has the weakest source support?
- target-function Loop: verify one representative metric before filling the rest.
- delivery contract: third-party human-readable summary plus concise evidence boundary.
- next-route recovery: continue evidence checks if sample metric passes; route back if source authority is weak.

## Adaptive Judgment

- judgment_mode: fast
- autonomy_level: strong_autonomy_with_guardrails
- decision_right: ai_decide
- ask_user_needed: no
- ai_decided_without_user_reason: Source ordering and evidence-depth choices are reversible and inside the fixed rubric.
- rollback_or_recovery_route: If source authority is insufficient, route back to search/access escalation.

## Goal State

- goal_memory_summary: Finish the fixed evidence table and delivery summary.
- beat_objective: Validate one weak metric and decide whether the evidence path is adequate.
- next_route: evidence_check_then_fill_remaining_metrics

## Attention Governance And Closure

- minimum_viable_closure_status: partial
- closure_chain: fixed question, fixed metric rubric, source path, evidence-row result, human-readable claim boundary, limitation, next weakest metric.
- minimum_sufficient_observability_status: light_signal_enough
- last_progress_signal: Metric C source path is the closure segment; this beat updates one evidence row and cannot yet prove real-world impact.
- heavy_audit_trigger: public delivery or source contradiction.

## External Calibration

- source: PRISMA source-flow discipline; NIST AI RMF evidence/risk framing.
- problem_matched: fixed evidence work needs transparent source inclusion/exclusion without reopening the model.
- adopted: record source authority, no-hit/exclusion reason, and claim boundary.
- rejected: full systematic-review ceremony.
- not_transferable: PRISMA publication checklist for every small evidence row.
- Complex_micro_contract: each evidence row states can-say, cannot-say, source role, and gap action.
- refresh_trigger: evidence standard changes, public delivery, or source path changes.

## Hallucination Sentinel

- current_basis: metric list is fixed and evidence row C is weak.
- external_basis: source-flow and risk-governance practices.
- inference: one representative source check can validate the evidence path.
- unsupported_claim: Metric C is fully externally validated.
- falsification_cue: primary or independent source rejects the metric role.
