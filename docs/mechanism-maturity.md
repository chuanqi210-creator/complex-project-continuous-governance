# Mechanism Maturity

Complex separates stable behavior from mechanisms that are still being tested.

This matters because many Complex improvements come from real project friction. A useful fix should not automatically become a permanent core rule. It first needs a status, evidence, a promotion path, and a demotion trigger.

Machine-readable registry: `docs/mechanism-maturity.json`

Each mechanism also declares `engineering_layers`: `prompt`, `context`, `harness`, and/or `loop`. These tags locate the mechanism in the runtime; they are not maturity levels.

## Statuses

| Status | Meaning |
| --- | --- |
| `core` | Stable behavior spine or boundary every Complex run should respect. |
| `validated` | Repeated real transcripts or end-to-end project samples show that the mechanism improves behavior. |
| `tested` | Covered by behavior cases, transcript rules, examples, or repeated user feedback, but not yet broadly validated. |
| `candidate` | Promising mechanism from recent failures or external calibration; use when relevant, but do not present as proven. |
| `retired` | No longer active; kept only if needed to explain a replacement. |

## How To Use

New projects should execute the core behavior first:

1. Restore true state.
2. Classify project nature.
3. Assign decision rights.
4. Establish the control plane, operating organization, and runtime harness.
5. Run a target-function Progress Loop.
6. Deliver to the right audience and evaluate the outcome.
7. Leave recovery pointers and a layer-level diagnosis.

Then use tested and candidate mechanisms only when their failure mode appears. For example, use `operating_organization` when a long project risks local greedy work, and use `trace_appraisal_hot_warm_cold` when the hot context is becoming too large.

## Promotion Discipline

Candidate mechanisms do not move into the core protocol just because they sound right.

Promotion normally requires:

- a behavior case;
- transcript review rules;
- at least one filled example or template landing point;
- external calibration for mechanism-level changes;
- real transcript or end-to-end project evidence before claiming validation.

Demotion is just as important. A mechanism should be downgraded or retired if it adds visible process burden, causes local-greedy behavior, conflicts with Codex surfaces, or repeatedly passes marker checks while failing human review.

## Current Interpretation

The current Complex repository has:

- stable core behaviors and responsibility boundaries;
- validated continuous-cadence and four-layer runtime-alignment mechanisms backed by autonomous wakes, cross-project recovery tests, independent review, and outcome-based heartbeat shutdown;
- tested Codex-surface, prompt-continuity, source-resolution, and intervention-boundary rules;
- candidate operating-organization, portfolio, interrupt/resume side-effect safety, external-calibration, hallucination-sentinel, attention-governance, and example-currentness mechanisms that still need broader real transcript evidence.

The four-layer runtime distinguishes Prompt Contract, Context Working Set, Runtime Harness, and Progress Loop. Its validated status means repeated local transcripts and end-to-end target-project samples improved diagnosis, semantic recovery, continuation, and stopping. It does not prove every project class or public installation is covered; demotion remains available if later evidence shows ceremony without outcome improvement.

This is intentional. Complex should be honest about what is proven, what is promising, and what still needs pressure testing.
