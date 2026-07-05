# Judgment Example: External Calibration

## Judgment Context

- decision to make: Change Loop from "smallest local action" to "target-function Loop."
- project_nature: mixed.
- beat_objective: Decide whether the Loop rule should change.

## External Calibration

- source: CRISP-DM, NASA Systems Engineering Handbook, Google SRE toil.
- problem_matched: local action can be cheap yet strategically wrong.
- adopted:
  - CRISP-DM: iteration must serve the business/project objective, not only a data task.
  - NASA: gate reviews need entry/success criteria.
  - SRE: toil should not become the main work.
- rejected:
  - full stage bureaucracy for every beat.
  - heavyweight formal review boards.
- not_transferable:
  - enterprise staffing and compliance paperwork.
- Complex_micro_contract:
  - every Loop states target function, module, lane, forward artifact, guard, and why it is not local greedy optimization.
  - repeated guardrail-only work triggers toil/WIP review.
- refresh_trigger: after 5 accepted beats, phase switch, or repeated local-detail drift.

## Hallucination Sentinel

- current_basis: user reported local greedy drift in real practice.
- external_basis: listed sources above.
- inference: target-function Loop is more robust than "lightest useful action."
- unsupported_claim: it will solve every attention-drift failure.
- falsification_cue: future transcripts still show local detail loops without project-level movement.

## Route Choice

- selected_route: update protocol, templates, examples, and behavior cases.
- rejected_routes:
  - keep "lightest action" wording: too local.
  - add a new heavy gate: increases bloat.
- next_route: update behavior regression and examples.

