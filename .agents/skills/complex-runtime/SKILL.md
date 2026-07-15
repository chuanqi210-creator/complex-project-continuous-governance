---
name: complex-runtime
description: Apply Complex to long-running Codex projects. Use when asked to scan or use Complex, design a project prompt, run continuous cadence, align Plan/Goal/thread/subagent/automation surfaces, diagnose prompt/context/harness/loop failures, or govern evidence/model-discovery/execution projects with strong autonomy inside responsibility boundaries.
---

# Complex Runtime

Complex is a Codex-native project runtime. Use its seven-behavior spine with four coupled engineering layers:

- **Prompt Contract**: durable Goal, completion criteria, responsibility boundary, and output contract.
- **Context Working Set**: current, attributable, minimal-sufficient facts for the next judgment.
- **Runtime Harness**: tools, environment, policies, observability, checkpoints, and recovery.
- **Progress Loop**: act, observe, evaluate, route, retry, rollback, or stop from outcomes.

The four layers are not stages or new gates. Use them together and diagnose the failed layer before changing the system.

Primary references when deeper detail is needed:

- `protocol/core.md`
- `docs/quickstart.md`
- `docs/mechanism-maturity.md`
- `docs/examples/`
- `templates/`

When applying Complex to a target project, this skill is the first-pass rule index. Inspect the target recovery anchor before opening deeper Complex references. Use `protocol/current-state.md` only when maintaining Complex itself; never mix Complex's maintenance state into a target project's facts.

## Codex Surface Map

- Plan mode is a planning surface. Use it when available at complex or strategic checkpoints; otherwise produce a plan-shaped checkpoint without claiming the UI changed.
- Codex Goal carries `thread_goal` or `phase_goal`, not changing beat chores.
- `beat_objective` is the current Plan/Loop target. `goal_memory_summary` is recovery context.
- Continuous cadence advances queued beats in the same run until completion or a real responsibility/tool boundary. If cross-turn continuation was selected and a callable heartbeat/automation tool exists, activate it during harness setup and retain the resource evidence; do not merely recommend it. An accepted beat does not complete the Codex Goal while useful queued work remains.
- Subagents are bounded workers. Standing lanes are durable manager-owned responsibilities.
- Threads, worktrees, and automations are platform resources selected according to task and tool fit.

## Runtime Spine

1. Restore true state and assemble the Context Working Set.
2. Classify `project_nature`: `evidence_fill`, `model_discovery`, `mixed`, or `execution_delivery`.
3. Assign decision rights through the responsibility boundary.
4. Establish the control plane, operating organization, and Runtime Harness.
5. Run the smallest meaningful target-function Progress Loop.
6. Deliver to the right audience and evaluate the outcome.
7. Leave `next_route`, accepted artifacts, recovery pointers, and layer diagnosis.

## Four-Layer Contract

### Prompt

Keep the project prompt stable and project-specific. Include Goal, target function, completion criteria, responsibility boundary, delivery contract, and evaluation. Put changing facts in context, not the master prompt. Patch a prompt only after an observed instruction-level failure or changed Goal.

### Context

Assemble in this order:

`durable instructions -> current state -> active module -> just-in-time retrieval -> provenance/freshness -> trim/compact -> exclusions`

After compaction or handoff, verify recovery of Goal, current basis, active module, open risks, and next route. Do not equate file presence with context recovery.

On a new target repository, find durable instructions and one authoritative five-field recovery anchor before broad scanning. If none exists, diagnose `context_failure`; inspect only bounded root facts and explicitly accepted pointers, then create the smallest project-native anchor when writable or return the missing fields and bootstrap route when read-only. Never promote a dated plan, candidate output, or thread return into current state merely because it is the newest visible file.

Treat an existing anchor as valid only if authority, freshness, bounded size, and one next route are clear. Oversized or conflicting anchors trigger a state-reconciliation beat, not deeper business execution: query route/status keys selectively, retain the contradiction, compact one Hot State, and keep large manifests or ledgers warm by pointer.

Make bounded inspection measurable. Check scale first; classify local key names/types before values; cap the first pass at 50 matched names or 80 text lines, 32 KiB of output, and 30 seconds per source unless a project-specific budget is justified. If a query truncates, times out, or exceeds the match budget, stop: the source does not fit the current working-set envelope, although authority still requires separate judgment. Do not broaden the query. Prefer `tools/inspect_recovery_anchor.py` or an equivalent deterministic extractor for repeated large-anchor audits, then pass only its content-minimized ledger to a clean evaluator. Do not cross the review boundary with source snippets, raw key names, absolute paths, or identifiers. The manager enforces hard worker timeout with the available harness/watchdog.

### Harness

Make tools, environment, side effects, logs, validation, checkpoints, retries, idempotency, rollback, and degraded routes legible. Discover capabilities just in time. Prefer mechanical checks when a repeated textual rule can be enforced by tests, schemas, hooks, or verifiers.

### Loop

Use:

`restore -> select -> act -> observe -> evaluate -> route/retry/rollback/stop`

Define an outcome completion predicate and forward artifact. For important work, separate executor and evaluator. A fixed beat count or agent self-report is not completion.

## Cross-Layer Diagnosis

Before adding prompt text, classify the failure:

- `prompt_failure`: instruction, constraint, output, or completion contract is wrong;
- `context_failure`: required facts are absent, stale, polluted, or badly prioritized;
- `harness_failure`: tool, environment, interface, policy, observability, or recovery failed;
- `loop_failure`: stopping, evaluation, retry, continuation, or routing failed;
- `model_limitation`: the first four layers are adequate and performance remains insufficient.

Repair the failed layer. Add the observed outcome to evaluation before changing defaults.

## Responsibility And Organization

AI decides project-internal planning, reading, verification, topology fit, context compaction, reversible local commands, and next-beat routing. Ask only for Goal/public-voice changes, credentials, payment, publishing, external writes, irreversible shared-state changes, high-impact external commitments, or undelegated human value judgments.

For recurring work, establish controller, human interface, literature/data, model/component, data-code, review/risk, and writing/delivery lanes. A lane is responsibility, not automatically a thread. Independent review uses clean context, a fact ledger, or a separate reviewer; same-session review is diagnostic.

## External Calibration And Evidence

Before mechanism-level changes, compare official docs, primary papers, standards, or mature production practice. Record source, problem matched, adopted, rejected, not transferable, micro-contract, and refresh trigger. External precedent grounds a design but does not validate Complex.

Use a hallucination sentinel for important transitions and claims: current basis, external basis, inference, unsupported claim, and falsification cue.

## State And Output

Keep Hot State short, Warm Index compact, and raw traces in Cold Archive by pointer. Routine human output shows only what moved, what artifact changed, what uncertainty changed, what cannot yet be claimed, and the next route.
