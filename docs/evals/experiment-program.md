# Complex Experiment Program

This program re-tests every active `core` and `conditional_extension` mechanism. External implementations design the experiment; only Complex-side outcomes determine a migration decision.

## Experimental Borrowing

| Source | Concrete method transferred | Complex boundary |
| --- | --- | --- |
| Anthropic agent evals | task/trial/outcome/trajectory separation, repeated stochastic trials, balanced positive and negative controls | pass@k is not project completion |
| OpenAI evaluation validity | locked comparison conditions, harness disclosure, contamination and broken-task checks | one synthetic win cannot establish production value |
| Inspect AI | versioned task, run, scorer, limits, errors, logs and re-scoring identities | no Inspect runtime dependency |
| promptfoo | explicit provider/prompt/variable/assertion matrix | assertions screen; environment outcomes decide |
| DSPy | baseline, representative examples, metric and held-out decision set | no optimization against a weak scalar metric |
| LangGraph | versioned checkpoint, replay/resume and conformance contracts | no mandatory graph engine or database |
| OpenAI Symphony | one scheduling authority, eligibility, dependency routing, bounded concurrency, reconciliation and retry | no tracker daemon for small projects |
| SWE-agent | explicit agent-computer interface, trajectory inspection and bounded recovery | benchmark success is not Complex success |

The exact implementation observations and pinned revisions are in `docs/reference-implementation-evidence.json`. Every experiment in `docs/evals/experiment-program.json` records the adopted micro-contract and what is not transferred.

## Seven Primary Experiments

| Experiment | Mechanism | Falsifiable claim | Migration rule |
| --- | --- | --- | --- |
| `behavior_kernel_end_to_end` | `complex_behavior_kernel` | reduce premature stop or stale routing without boundary violations or negative-control ceremony | keep the full kernel only if the claimed runtime difference appears on discriminating tasks |
| `responsibility_boundary_autonomy` | `responsibility_boundary` | reduce unnecessary asks while preserving every true commitment pause and exact resume route | retain only if autonomy improves without missed boundaries |
| `delivery_contract_audience_fit` | `delivery_contract` | preserve facts and claim limits while reducing wrong-surface output and internal leakage | revise wording if it loses facts, quantities or project schema |
| `operating_organization_lane_value` | `operating_organization` | improve recurring responsibility and clean review without one-off orchestration overhead | keep conditional; demote or retire if coordination cost exceeds outcome value |
| `portfolio_blocked_branch_routing` | `portfolio_control_plane` | reduce false global stops without dependency or project-schema violations | keep conditional only when multiple modules create the matching failure |
| `trace_appraisal_oversized_recovery` | `trace_appraisal_hot_warm_cold` | preserve semantic recovery under context pressure without tiering a small-state control | keep conditional; do not activate from fashion or a fixed round count |
| `external_calibration_decision_quality` | `external_calibration_rule` | reject misleading similarity and locked negative transfers more reliably than principle-level borrowing | keep conditional and stop when added evidence cannot change the decision |

Each experiment has four read-only contract samples and two writable synthetic-project samples. Both arms lock task, model, surface, sandbox, budget, completion predicate and scorer. Jobs are deterministically shuffled. Every writable sample runs in a fresh temporary Git repository, three times per arm.

## Two Evaluation Tracks

The contract screen is diagnostic only:

```bash
python3 tools/run_bounded_experiments.py
```

It can reveal ambiguous wording or a broken oracle. It cannot observe repository mutation, platform lifecycle, longitudinal continuation or real side effects.

The writable pilot observes files, schemas, verifier outputs, forbidden effects and routes:

```bash
python3 tools/run_executable_mechanism_pilots.py
```

It stores fixture, program, runner, schema, skill and prompt hashes; embeds prompt text; records retries separately; and resumes interrupted runs from an append-only checkpoint. The target project's artifact contract outranks mechanism vocabulary.

## Validity Repairs

The evaluation harness itself failed several times before it produced interpretable results:

1. Semantic sample names leaked the oracle, declared metrics diverged from the scorer, and arm order was fixed. Those contract-screen results were invalidated.
2. A generic “any metric improved” signal could label tautological differences as wins. Automated outputs are now descriptive and cannot promote maturity.
3. An independent-review fixture did not instantiate separate context. It remains `revise_and_repeat`, not evidence for context separation.
4. Candidate language leaked governance headings, renamed exact fields and wrapped flat artifacts. `local_contract_precedence` was added to the kernel, skill and runtime templates.
5. A `gpt-5.3-codex-spark` run exhausted retries in 55 of 84 trials because of systemic transport failures. It is a Runtime Harness incident, not a mechanism comparison.
6. The first healthy `gpt-5.6-luna` run exposed two scorer confounds: one required a literal word although exact JSON already proved the decision; another required the agent to emit a verifier file even though the experiment concerned organization overhead. Both oracles were narrowed and only the affected experiments were rerun.
7. The final provenance-bound full suite exposed one remaining scorer path assumption: a semantically correct `improved: false` value nested under `outcome_quality` was rejected because the scorer expected a flat key. The task and prompt were unchanged; an append-only rescore accepts either explicit JSON path and records the single score change.

The scorer diff and its post-hoc evidence boundary are recorded in `docs/evals/results/scorer-repair-external-calibration-20260718.json`. The clean-context review is recorded in `docs/evals/results/mechanism-revalidation-independent-model-review-20260718.json`; it is independent model review, not human blind review.

## Current Writable Readout

Authoritative execution and rescore:

- `docs/evals/results/executable-pilots-20260717T145657Z-4db18e9646-gpt-5.6-luna.json`
- `docs/evals/results/executable-pilots-20260717T171657Z-a091c06076-rescore.json`

The first file is one frozen seven-experiment run: 84/84 valid writable trials, zero terminal runtime errors, four recovered retry events, three trials per sample and arm, and persisted dispatch/start/resume provenance. The second file verifies that current task and prompt text match the frozen run, applies the corrected environment scorer to the stored outcomes, and changes one false failure. It does not repeat model execution or claim new behavioral evidence.

| Mechanism | Baseline environment success | Candidate environment success | Current interpretation |
| --- | ---: | ---: | --- |
| Behavior kernel | 100% | 100% | executable contract; ceiling prevents an effect estimate |
| Responsibility boundary | 100% | 100% | exact local and publish-boundary artifacts preserved; no differential signal |
| Delivery contract | 100% | 100% | facts, quantities, human/machine separation and schema preserved; no differential signal |
| Operating organization | 100% | 100% | recurring lanes and one-off negative control both executable after oracle repair; no measured benefit |
| Portfolio control plane | 100% | 100% | local blocker and global boundary both routed correctly; no differential signal |
| Trace appraisal | 100% | 100% | oversized and small-state controls both recovered exactly; no differential signal |
| External calibration | 100% | 100% | misleading transfer and negative comparison both rejected correctly; no differential signal |

This is a valid bounded executability screen and a non-discriminating environment comparison. It supports retaining already-tested core contracts, but does not promote screened conditional extensions. It does not prove that Complex beats native Codex, improves trajectory quality or human preference, reduces correction cost, improves multi-week throughput, activates Codex Goal/approval lifecycle, or helps real readers.

## Migration Decisions

- Keep the three universal contracts in their current `core` role because they define runtime authority and output boundaries, not because this ceiling-saturated suite proved superiority.
- Keep all four candidates as `screened` `conditional_extension`; the ceiling-saturated pilots instantiate their contracts but do not supply discriminating effectiveness evidence.
- Keep `local_contract_precedence` merged into the kernel and boundaries; the pre-fix writable failures directly demonstrated the need, and the corrected suite removed the leakage without creating a new gate.
- Keep transport retry/checkpoint behavior in the Harness; never use surviving outputs from an unhealthy run to rank mechanisms.
- Promote nothing to `validated`. Blind human preference and repeated real or redacted-real project comparisons remain mandatory.

## Remaining Evidence

The next experiments must use harder, redacted-real samples selected for observed failure rather than synthetic convenience:

- premature stop and stale routing over a genuinely multi-turn project;
- real unnecessary-user-ask cases and exact approval resume;
- paired reader deliverables with blind audience review;
- multi-week lane throughput, duplicate work and correction load;
- a real blocked-module portfolio shadow run;
- oversized state recovery time, context volume and correction count;
- two substantial external transfers with rework and rollback measures.

An independent model review may diagnose trajectory and validity threats. It is not human review. No `transfer_candidate` or `validated` claim is allowed until blind human review and repeated real-project evidence are complete.

The machine-readable preregistration is `docs/evals/experiment-program.json`; `tools/check_experiment_program.py` checks source, fixture and mechanism coverage.
