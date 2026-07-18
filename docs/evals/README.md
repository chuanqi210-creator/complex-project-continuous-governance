# Complex Evals

Complex evaluation separates three jobs:

1. an `eval_case` names the mechanism under test and fixes the task, sample IDs and origin, project snapshot, responsibility/completion boundary, scorer, limits, project nature, and privacy boundary;
2. an `eval_run` records one baseline or candidate execution, model/agent, surface, runtime configuration, attempt count, and result pointer;
3. a `score_record` applies a versioned scorer and human outcome judgment to a run.

Schema: `docs/evals/complex-eval-record.schema.json`

Records: `docs/evals/records/`

Externally calibrated experiment inventory: `docs/evals/experiment-program.json`

Human-readable borrowing map and current readout: `docs/evals/experiment-program.md`

Validate them with:

```bash
python3 tools/check_eval_records.py
python3 tools/check_experiment_program.py
```

## Comparison Rule

A baseline/candidate comparison locks:

- task and sample version;
- target project snapshot;
- Codex surface and model;
- responsibility boundary;
- limits and completion predicate;
- scorer and scorer version.

The comparison declares the one intended changed variable, and both runs must name it. The canonical locked set is task, sample IDs, project snapshot, Codex surface, model/agent, runtime configuration, responsibility boundary, limits, completion predicate, scorer ID, and scorer version. If one of these changes, the result is diagnostic, not comparative evidence.

Check run health before interpreting an arm difference. If either arm lacks the preregistered number of valid trials, a transport or tool failure is systematic, or retry exhaustion is uneven across arms, classify the record as an infrastructure failure. Preserve the incident for Harness diagnosis, but do not rank mechanisms from the surviving outputs.

Compared or reviewed records require exactly one score per run, one metric-bearing result for every sample, the correct baseline/candidate role mapping, one scorer version, and a non-pending comparison decision. Reviewed records also require a non-pending human preference. A `transfer_candidate` decision requires human preference for a non-failing candidate; `keep_baseline` requires the corresponding baseline judgment.

Keep raw private transcripts outside the active repository. Store a redacted summary or private pointer in `result_pointer`.

## Evidence Claims

- A filled example **illustrates** intended structure.
- A marker or checker **screens** for a bounded failure.
- A pinned local fixture **reproduces** upstream behavior.
- Locked baseline and candidate runs **compare**.
- Repeated real Complex outcomes **validate** within a stated scope.

Marker pass is never a quality score. Human review asks whether the run reduced correction cost, continued appropriately, produced a useful outcome, preserved the Goal, respected responsibility boundaries, and avoided visible process burden.

## Trajectory Evidence

Runtime claims must be scored from the surface that can actually expose them. Final prose can screen wording, but it cannot prove that a Goal, automation, thread, subagent, approval, retry, or routed beat was activated.

For continuation and Goal evaluations, prefer a trace or event ledger that records:

- the Goal create/resume/complete event and stable resource identifier;
- the first domain action after Goal activation;
- every accepted non-terminal route and the next beat actually started from it;
- the terminal outcome predicate or exact responsibility/tool boundary;
- retry, rollback, checkpoint, and user-intervention events when present.

If the selected surface does not expose those events, record the result as a same-run outcome test or wording screen. Do not infer Goal activation from `goal_surface_status: active`, a final answer, or a state file written by the same agent. A useful fixture can prove that queued work completed without asking the user, while still being unable to prove cross-turn Goal behavior.

## Reference Implementation Reproductions

These optional fixtures reproduce bounded upstream mechanisms only:

```bash
npx -y promptfoo@0.121.19 eval -c docs/evals/reference-promptfoo-echo.yaml --no-cache
uv run --with langgraph==1.2.9 --with langgraph-checkpoint==4.1.1 \
  --with langgraph-checkpoint-conformance==0.0.2 \
  python docs/evals/reference-langgraph-checkpoint.py
```

The promptfoo fixture screens a zero-cost logged-output assertion path. It is not a baseline/candidate matrix. The LangGraph fixture reproduces five required checkpoint capabilities. Neither validates Complex.

## Mechanism Re-evaluation Tracks

Every core or conditional mechanism has one primary experiment. The two local tracks answer different questions.

The contract-legibility screen runs opaque, read-only decision samples:

```bash
python3 tools/run_bounded_experiments.py
```

It asks whether the baseline and mechanism contracts can be interpreted consistently. It does not expose tools, repository mutation, platform lifecycle, or longitudinal behavior. Its arm order is deterministically shuffled and its outputs are descriptive only. A difference here may reveal clear wording, an ambiguous contract, or a bad oracle; it cannot support effectiveness or maturity promotion.

The writable synthetic-project pilot runs each sample in a fresh temporary Git repository and scores observed files, checks, routes, and forbidden side effects:

```bash
python3 tools/run_executable_mechanism_pilots.py
```

It instantiates local execution and environment outcomes, but not real publication/account responsibility, Codex App Goal lifecycle, multi-week lane throughput, or human blind preference. Baseline and candidate use the same model, task, fixture, sandbox, budget, scorer, and three independent trials per sample and arm. Jobs are deterministically shuffled; fixture, program, runner, schema, skill, and prompt hashes are retained; prompt text is embedded for reconstruction; transient transport failures are retried from a clean Git checkpoint and recorded separately from mechanism outcomes. An interrupted suite resumes from its append-only trial checkpoint.

The target fixture is the artifact authority. Candidate governance text may choose a route, but it may not rename fixture fields, wrap a flat schema, omit required quantities, or export internal governance labels. Such failures are scored as mechanism-contract failures rather than polished away in the final response.

Results and comparison records are append-only under `docs/evals/results/` and `docs/evals/records/`. A scorer repair never rewrites the frozen run: `tools/rescore_executable_mechanism_pilots.py` verifies unchanged task and prompt text, re-scores stored outcomes, and writes a compact derived result. Record the old rule, new semantic alternatives, affected trials, reason, and maturity boundary. Keep only the current authoritative run and compact method-failure evidence in the active tree; summarize superseded exploratory runs before removal instead of accumulating machine traces indefinitely.

Neither track can by itself produce `validated`. Promotion still requires distinct real or redacted-real projects, outcome and trajectory review, completed blind human review, and a repeated improvement within the claimed scope. A broken task or prompt is repaired and rerun. A scorer-only defect may be repaired by append-only re-scoring of frozen outputs, with the original result and explicit scorer-change record retained.
