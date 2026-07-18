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

- Plan mode is a planning surface. Use it when the desired outcome, constraints, or strategic route is unclear; otherwise keep the clear objective in Goal and use a lightweight plan-shaped checkpoint without claiming the UI changed.
- Codex Thread, Turn, Item, Goal, approval, skill, subagent, worktree, and automation are platform primitives. `thread_goal`, `phase_goal`, `beat_objective`, `goal_memory_summary`, and standing lane are Complex conventions layered on available primitives.
- Codex Goal carries the durable objective. If the work spans multiple turns or queued beats, has a verifiable stopping condition, and the Goal tool is callable, activate it before business execution; do not merely recommend `/goal` or leave the objective in state. Changing beat chores stay in `beat_objective` and recovery context.
- Continuous cadence advances queued beats in the same run until completion or a real responsibility/tool boundary. If cross-turn continuation was selected and a callable heartbeat/automation tool exists, activate it during harness setup and retain the resource evidence; do not merely recommend it. An accepted beat does not complete the Codex Goal while useful queued work remains.
- Treat a non-terminal `next_route` as queued work and continue executing it while tools and the responsibility boundary permit. Goal preserves continuation when the runtime yields or crosses turns; Goal activation alone does not execute the queue and is not a stopping condition. A human-readable progress report is not a stopping condition.
- Subagents are bounded workers. Standing lanes are durable manager-owned responsibilities.
- Threads, worktrees, and automations are platform resources selected according to task and tool fit.

## Runtime Spine

1. Restore true state and assemble the Context Working Set.
2. Classify `project_nature`: `evidence_fill`, `model_discovery`, `mixed`, or `execution_delivery`.
3. Assign decision rights through the responsibility boundary.
4. Establish the minimum control and Runtime Harness; add organization or portfolio control only when recurring lanes or multiple modules justify them.
5. Run a bounded target-function Progress Loop that changes an outcome, exposes a decision, or falsifies a route.
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

Treat an existing anchor as valid only if authority, freshness, bounded size, and one next route are clear. Oversized or conflicting anchors trigger a state-reconciliation beat, not deeper business execution: query route/status keys selectively, retain the contradiction, compact one active recovery anchor, and keep large manifests or ledgers by pointer.

Make bounded inspection measurable. Check scale first, classify names/types before values, and choose a project-specific match/output/time envelope. The bundled extractor's limits are safe fallback defaults, not universal protocol constants. If a query truncates, times out, or exceeds the envelope, stop: the source does not fit the current working set, although authority still requires separate judgment. Prefer `tools/inspect_recovery_anchor.py` or an equivalent deterministic extractor for repeated large-anchor audits, then pass only its content-minimized ledger to a clean evaluator. The manager enforces hard timeout with the available harness/watchdog.

### Harness

Make tools, environment, side effects, logs, validation, checkpoints, retries, idempotency, rollback, and degraded routes legible. Discover capabilities just in time. Prefer mechanical checks when a repeated textual rule can be enforced by tests, schemas, hooks, or verifiers.

Treat the target repository's explicit completion predicate, output path, field names, value types, and verifier as the executable interface. Complex terminology must not rename fields, add wrappers, suppress requested facts, or appear as reader-facing headings unless the target contract asks for it. Governance decides the route; the local contract decides the artifact shape.

Classify responsibility as `decision ownership x side-effect class`. Put approval on the exact external or irreversible operation and preserve its payload hash, scope/version, stable action ID, and resume route. Keep retry, checkpoint, idempotency, and compensation in the Harness rather than asking the user to own them.

### Loop

Use:

`restore -> select -> act -> observe -> evaluate -> route/retry/rollback/stop`

Define an outcome completion predicate. A forward-execution beat names its forward artifact; a diagnostic beat names its route decision, falsification, bounded blocker, or parking decision. For important work, separate executor and evaluator. A fixed beat count or agent self-report is not completion.

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

For recurring multi-lane work, establish only responsibilities that will be reused. A lane contract has accepted input/output, wake trigger, context policy, manager acceptance, retire condition, and owner/resource evidence. A lane is responsibility, not automatically a thread; a real platform resource requires its observed identifier and status. Independent review uses clean context, a fact ledger, or a separate reviewer; same-session review is diagnostic.

## External Calibration And Evidence

Before mechanism-level changes, use external projects as reference implementations, not names. Discover candidates, pin and inspect their goal/non-goals, state/control path, code/configuration, tests/evaluations, operating limits, and failure boundaries; reproduce a bounded mechanism when feasible; compare it with current Complex behavior on the same task; then transfer one reversible micro-contract. Record explicit status from discovery through `validated_in_complex`. A citation, README, star count, or upstream benchmark never proves a Complex transfer. For Complex maintenance, consult `docs/active-architecture-rebaseline.json` before creating a new mechanism; prefer merging into the kernel or a boundary.

For a same-task comparison, use `docs/evals/experiment-program.json` rather than an informal demonstration. Freeze and hash the task, fixtures, runner, schema, and prompts; hide semantic oracle labels; change one variable; repeat stochastic arms; score environment outcome, trajectory, and blind human preference separately; and screen broken tasks, contamination, reward hacking, harness mismatch, and grader disagreement. Prefer held-out projects when the transfer decision itself is being tested. If the harness does not instantiate the claimed condition, mark `revise_and_repeat`. Automated signals without completed human review remain `insufficient_evidence`.

At important transitions and claims, run a claim-basis check: current basis, external basis, inference, unsupported claim, and falsification cue.

## State And Output

When measured context growth or repeated handoff justifies state tiers, keep a versioned authoritative Hot State, a compact Warm Index, and raw traces in Cold Archive by pointer. Broken pointers route to reconciliation; never guess through them. Otherwise use one compact recovery anchor. Human delivery declares the reader task, surface, claim ceiling, sensitive-information boundary, and acceptance test; keep machine recovery and observability separate unless requested.

Use delivery terms to choose content, not as a mandatory outline. Human output leads with project facts, requested quantities, decision implications, and honest limits; machine output follows the project-native schema exactly.
