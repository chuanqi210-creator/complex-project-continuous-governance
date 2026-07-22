# Mechanism Maturity

Complex keeps one small active mechanism registry. It does not give every observed failure its own gate.

Machine-readable source: `docs/mechanism-maturity.json`

## Two Independent Axes

Architecture role and empirical maturity are different questions. Calling a boundary `core` means every run must respect it; it does not mean a baseline/candidate experiment has proved an outcome improvement.

| Normative role | Meaning |
| --- | --- |
| `core` | Universal execution spine or responsibility/output boundary. |
| `supporting_practice` | Reusable practice that supports the core but is not a universal boundary. |
| `conditional_extension` | Activate only when its scale condition or failure mode appears. |
| `retired` | Inactive; retained only when compatibility evidence requires it. |

| Evidence status | Meaning |
| --- | --- |
| `screened` | Contract and external basis were reviewed; no valid outcome comparison supports effectiveness. |
| `tested` | Behavior screens, filled examples, bounded pilots, or project observations exist; real comparative validation is incomplete. |
| `validated` | Repeated, versioned real-project comparisons improve outcomes in a stated scope and pass independent human review. |

The evidence verbs are also fixed:

- examples **illustrate**;
- markers and checkers **screen**;
- fixed-version fixtures **reproduce**;
- locked baseline/candidate runs **compare**;
- repeated real outcomes **validate**.

## Current Active Set

### Core Role, Tested Evidence

- `complex_behavior_kernel`: seven behaviors plus the Prompt, Context, Harness, and Loop diagnostic axes. Prompt rehydration, continuous cadence, source resolution, target-function execution, forward-artifact acceptance, and bounded recovery live here rather than as separate gate families.
- `responsibility_boundary`: AI-owned project decisions, user-owned commitments, approval pauses, idempotency, rollback, and unnecessary-intervention prevention share one boundary.
- `delivery_contract`: audience, purpose, claim strength, granularity, internal-information boundary, and minimum sufficient observability.

Framework Grilling is not a twelfth mechanism. It is a Prompt Contract technique inside the behavior kernel and responsibility boundary: inspect facts first, ask one high-leverage framework question only when a user-owned fork can change the destination, then compile the answer into a Framework Decision Contract. The upstream implementation is pinned and inspected; the Complex transfer is behavior-screened but has no same-task outcome comparison yet.

Complex self-optimization is also not a new mechanism. It is the maintenance use of the behavior kernel, external calibration, transcript/evaluation records, and maturity registry. Routine corrections remain light; bounded and substantial changes keep a stable baseline and one reversible candidate, then advance through contract screening, reproduction, same-task comparison, limited real use, and repeated outcome review only as justified. Kubernetes KEP and Argo Rollouts are pinned implementation evidence for this shape; the Complex integration is behavior-screened and has not yet completed a real maintenance-path comparison.

Time convergence is not a new mechanism either. It is a cross-layer operating contract inside the kernel, delivery boundary, and conditional portfolio control. Long work must define when the human next receives a usable increment and what that increment is; if observed progress does not fit, Complex changes scope or route while preserving the quality/evidence floor. Shape Up, Scrum, and NASA provide external design precedent, but the contract currently has behavior coverage only and no locked time-to-stage-value comparison.

Cross-boundary state reconciliation is likewise not a twelfth mechanism. It is a controller responsibility within the kernel plus the conditional portfolio and trace extensions. Local modules, lanes, repositories, threads, or workflows keep authority over bounded local facts; the controller refreshes one compact global control projection from versioned local state capsules only at recovery, transitions, handoffs, dependency/conflict changes, stage delivery, or measured staleness. Current evidence is documentation, a filled example, and behavior screening; no locked real-project comparison yet measures stale-route reduction, duplicate-work reduction, or reconciliation cost.

### Supporting Practices, Tested Evidence

- `codex_surface_alignment`
- `project_nature_router`
- `independent_review_context_separation`
- `behavior_transcript_review`

These have behavior coverage and project evidence, but none is currently labeled `validated` under the stricter comparison standard.

`project_nature_router` now treats the project label as a prior and permits a narrower phase, module, or work-item classification to control the current beat. This is a clarification of routing scope, not a new mechanism or evidence promotion.

### Conditional Extensions, Screened Evidence

- `operating_organization`
- `portfolio_control_plane`
- `trace_appraisal_hot_warm_cold`
- `external_calibration_rule`

Conditional extensions are not startup ceremony. They activate only when recurring lanes, multiple modules, measured context pressure, or mechanism-level change makes them relevant. Their synthetic pilots show that the written contracts can execute, but the tasks disclose much of the desired answer and reach the baseline ceiling; under the strict promotion rule this remains `screened`.

`operating_organization` and `portfolio_control_plane` now use artifact-first topology compilation: define accepted input, expected artifact or route outcome, acceptance, recovery, and write-back before selecting manager work, deterministic Harness, temporary workers, standing lanes, clean evaluation, or responsibility handoff. Domain-specific role charts remain in domain projects and examples. This consolidation still needs a locked real-project comparison.

## Current Mechanism Readout

The 2026-07-17 revalidation gives each of the three core mechanisms and four conditional candidates a falsifiable claim, implementation-level external basis, frozen baseline/candidate contract, two writable samples, three trials per sample and arm, environment/trajectory/human grader boundary, and migration decision.

The final `gpt-5.6-luna` suite contains one provenance-bound run with 84/84 valid writable trials, zero terminal runtime errors, and four recovered retry events. An append-only rescore verifies unchanged task and prompt hashes and corrects one false failure caused by an overly narrow JSON path. After re-scoring, baseline and candidate reach 100% environment success for all seven mechanisms. That ceiling shows contract executability and exposes no candidate advantage. Core mechanisms remain `tested` from their wider behavior and project evidence; all four conditional mechanisms remain `screened`. Nothing moves to `validated`, and no conditional mechanism becomes core.

An earlier `gpt-5.3-codex-spark` run exhausted retries in 55 of 84 trials. It is evidence that run health must be checked before mechanism ranking, not evidence against any mechanism. Earlier scorer requirements were narrowed only when they measured wording, evaluator-generated files, or an arbitrary JSON path rather than the task outcome.

The method, result pointers, external borrowing, invalidated comparisons, and residual human/real-project boundary are in `docs/evals/experiment-program.md`.

## Re-baseline Result

The 2026-07-17 active architecture re-baseline reduced 22 mechanisms to 11. Eleven duplicate identities were merged into the kernel, responsibility boundary, delivery/evaluation, or external calibration. The previous standalone `validated` labels were removed because their evidence was useful but not stored as locked, reproducible baseline/candidate comparisons.

See `docs/active-architecture-rebaseline.md` and `docs/active-architecture-rebaseline.json` for every keep, merge, demote, and next-validation decision.

## Promotion Discipline

A conditional extension normally needs before its evidence status can move beyond `screened`:

1. a behavior case and transcript rule;
2. an implementation-grounded external basis;
3. a filled example or template landing point;
4. a valid bounded, versioned outcome pilot that actually instantiates the claimed mechanism.

`tested` becomes `validated` only after the case version, samples, project snapshot, surface/model/runtime, responsibility boundary, completion predicate, scorer, limits, and changed variable are locked; baseline and candidate run on the same task; independent human review prefers the candidate; and repeated real Complex outcomes improve. At least two reviewed records from distinct real or redacted-real sample sets, each with a `transfer_candidate` decision, must be linked from `internal_evidence` as `eval_record:docs/evals/records/<file>.json`. External success or a local upstream reproduction cannot skip this step. Normative role does not automatically change when evidence status changes.

Demotion is expected when a mechanism duplicates a stronger abstraction, creates visible process burden, conflicts with Codex, or passes marker screens while failing human outcome review.
