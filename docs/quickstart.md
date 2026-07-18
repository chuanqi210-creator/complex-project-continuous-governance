# Complex Quickstart

Audience: a Codex agent applying Complex to a target project.

Goal: begin useful work quickly while preserving durable intent, a clean working context, executable infrastructure, and outcome-based continuation.

## 1. Read By Progressive Disclosure

When applying Complex to another project:

1. Use the loaded `complex-runtime` skill as the first-pass rule index.
2. Read the target repository's durable instructions.
3. Resolve the target project's authoritative recovery anchor.
4. Read target facts by pointer for the active beat.
5. Open `protocol/core.md`, a filled example, or mechanism maturity only when a real rule ambiguity or matching failure mode requires deeper detail.

If the skill is not visible from the target-project task, verify the user-level installation at `$CODEX_HOME/skills/complex-runtime/SKILL.md` (normally `~/.codex/skills/complex-runtime/SKILL.md`) or select this repository's `.agents/skills` root through the current Codex surface. Do not compensate by copying the whole protocol into the target repository.

Do not read Complex's `protocol/current-state.md` into a target project's Context Working Set. It describes Complex's own maintenance state, not the target project.

When maintaining Complex itself, read `README.md`, `protocol/current-state.md`, this quickstart, and `protocol/core.md` before changing the runtime.

Treat the installed Complex runtime as the rule source and the target repository as the fact source. Read Warm/Cold material only by pointer when the active beat needs it.

Before recursive target-project scanning, locate project-native durable instructions and one authoritative recovery anchor for Goal, current basis, active module, open risks, and next route. If the anchor is absent, do a bounded root/latest-accepted-artifact bootstrap and record unknowns explicitly. Do not search hundreds of outputs to manufacture certainty, and do not treat a proposal as accepted controller state.

An existing anchor must still pass four checks: explicit authority, assessable freshness, bounded current state, and exactly one authoritative next route. If it is oversized or contradictory, select a state-reconciliation beat before project work. Inspect only route/status keys and accepted pointers; do not read a giant manifest in full or resolve disagreement by choosing the newest file.

Bound the inspection itself: measure scale first, list names/types before values, and choose a project-specific match, output, and time envelope. The bundled extractor defaults to 50 matched names or 80 text lines, 32 KiB of output, and 30 seconds per source; these are fallback limits, not protocol constants. Truncation or over-budget matches show that the source does not fit the current working-set envelope; they do not decide authority. Keep it by pointer instead of retrying with a broader search.

For the common `AGENTS.md` / `CONTEXT.md` / `notes/current_status.md` / `deliverables/manifest.json` layout, create a bounded fact ledger mechanically before clean-context evaluation:

```bash
python3 "$COMPLEX_HOME/tools/inspect_recovery_anchor.py" /absolute/path/to/target-project
```

The extractor does not choose authority. Its default ledger emits relative source paths, scale, line numbers, structural line types, matched term categories, and value types; it does not emit source snippets, raw JSON key names, absolute paths, project identifiers, or content fingerprints. It caps previews, matches, scan bytes, elapsed work, and output bytes, and stops matching after overflow. The evaluator decides whether state reconciliation is required. The extractor's internal deadline is a soft cooperative bound; the manager/watchdog owns the hard process or worker timeout.

## 2. Align Codex Surfaces

- Plan mode is a planning surface. Use it when the outcome, constraints, or strategic route is unclear; otherwise keep the clear durable objective in Goal and use a lightweight plan-shaped checkpoint for the current beat.
- Codex Thread, Turn, Item, Goal, approval, skill, subagent, worktree, and automation are platform primitives whose availability depends on the current surface.
- `thread_goal`, `phase_goal`, `beat_objective`, standing lane, and portfolio control are Complex conventions. They describe how Complex uses available primitives; they are not Codex API names.
- Codex Goal carries the durable objective. When a multi-turn route has a verifiable stop condition and Goal is available, activate it; `beat_objective` remains the current Plan/Loop target.
- Subagents are bounded workers; standing lanes are recurring responsibilities.
- Thread, worktree, and automation fit are orchestration decisions executed through available tools.
- Continuous cadence continues queued work until objective completion or a real responsibility/tool boundary. Goal preserves continuation when the runtime yields or crosses turns, but does not replace same-run execution. If scheduled or recurring continuation is selected and heartbeat/automation tooling is callable, create it during harness setup and record its status.

## 3. Establish The Four-Layer Runtime

### Prompt Contract

Record the stable project contract:

- Goal and target function;
- completion and outcome-evaluation criteria;
- responsibility boundary;
- delivery contract;
- stable project constraints and prompt version.

Do not paste current files, temporary tool results, or the complete Complex protocol into the prompt.

### Context Working Set

Assemble:

`durable instructions -> current recovery state -> active module -> just-in-time retrieval -> provenance/freshness -> trim/compact -> exclusions`

The working set must identify current basis, stale material, open risks, retrieved pointers, and next route. After compaction or handoff, verify semantic recovery rather than file presence.

### Runtime Harness

Check the capabilities that affect this project:

- workspace and isolation;
- tools, skills, browser, MCP, API, and temporary workers;
- side effects and responsibility boundaries;
- tests, schemas, hooks, logs, metrics, and evaluator;
- checkpoint, retry, timeout, idempotency, rollback, and degraded routes.

Treat the target project's completion predicate, artifact paths, schema, field names, value types, and verifier as the executable interface. Complex may improve routing and evaluation, but it must not rename project fields, wrap a flat payload, omit requested evidence or quantities, or turn internal governance terms into visible headings.

If a beat must pause for approval or external input, apply a pause/resume side-effect contract: do read-only or local draft work before the pause, put non-idempotent external writes after authorization, and record the checkpoint, idempotency key or stable identifier, compensation path, and resume route.

Discover capabilities just in time. Do not load everything into every beat.

### Progress Loop

Use:

`restore -> select -> act -> observe -> evaluate -> route/retry/rollback/stop`

Define an outcome completion predicate before execution. A forward-execution beat names its forward artifact; a diagnostic beat names the route decision, falsification, bounded blocker, or parking decision it must produce. For important work, separate executor and evaluator. Do not stop from a fixed beat count or agent self-report.

## 4. Run The Behavior Spine

1. Restore state and context.
2. Classify `evidence_fill`, `model_discovery`, `mixed`, or `execution_delivery`.
3. Assign responsibility and decision rights.
4. Form the minimum control and harness; add operating organization or portfolio control only when recurring lanes or multiple modules justify them.
5. Run a target-function Loop.
6. Deliver and evaluate.
7. Record accepted artifacts, layer diagnosis, and `next_route`.

If a mechanism name competes with this spine, the spine wins.

## 5. Diagnose Before Repair

Classify unexpected behavior:

- `prompt_failure`: the instruction or completion contract is wrong;
- `context_failure`: the necessary facts are missing, stale, or polluted;
- `harness_failure`: the tool, environment, policy, observability, or recovery failed;
- `loop_failure`: route, retry, evaluation, continuation, or stop logic failed;
- `model_limitation`: the first four layers are adequate and the model still fails.

Repair the failed layer. Add the observed outcome to evaluation before changing defaults. Do not use a longer prompt as a universal fix.

## 6. Add Organization Only When Needed

For recurring multi-lane work, assign only the manager-owned lanes that will be reused:

- controller;
- human interface;
- literature/data acquisition;
- model/component;
- data-code;
- review/risk;
- writing/delivery.

A lane need not become a thread. Use manager work, subagents, clean reviewers, worktrees, threads, or automations according to harness capability. Independent review starts from clean context or a fact ledger.

## 7. Accept Progress From Outcomes

```text
beat accepted = forward artifact or declared diagnostic outcome
              + relevant guard/evaluator passed
              + state/index updated
              + next route derived from observed result
```

Guardrail-only work is allowed when it protects a true dependency. Repetition triggers toil/WIP review: produce a forward artifact, park the branch, route elsewhere, or justify the dependency.

Research, analysis, and prototypes should form an early thin closure from question/input to data/source, minimal model/assumption, result/output, validation signal, claim/conclusion, limitation, and next weakness.

## 8. Use The Responsibility Boundary

AI decides project-internal planning, reading, verification, reversible commands, topology fit, context compaction, and next-beat routing.

Ask the user for:

- Goal or public-voice changes;
- credentials, payment, publishing, or external writes;
- irreversible shared-state changes;
- high-impact external commitments or unsupported strong claims;
- undelegated human value judgments.

If the next internal beat is clear, continue. Do not ask the user to summarize readable files or authorize routine orchestration.

## 9. Calibrate And Keep State Light

For mechanism-level changes, do not stop at framework names or README principles. Select a candidate by problem fit, pin a revision, inspect its goal/non-goals, state/control path, code/configuration, tests/evaluations, operating constraints, and failure boundaries. Reproduce a bounded mechanism when feasible, then compare it and the current Complex behavior on the same task before transfer.

Record `transfer_status`, implementation evidence, upstream validation limits, reproduction/comparison result, adopted/rejected/not-transferable parts, rollback, next validation, and refresh trigger. External precedent is design evidence; only repeated Complex transcripts or end-to-end outcomes support `validated_in_complex`. Reuse fresh records from `docs/reference-implementation-evidence.json` rather than browsing mechanically every beat.

When a mechanism claim needs empirical testing, use `docs/evals/experiment-program.json`. Its experiments expose the external method being borrowed, the one changed variable, repeated baseline/candidate trials, environment/trajectory/human graders, validity threats, and the decision rule. Do not invent an informal success demonstration when a frozen same-task comparison is feasible.

Read `normative_role` and `evidence_status` separately. `core` means a universal runtime boundary; it does not mean the mechanism beat a baseline. `screened`, `tested`, and `validated` describe evidence strength. Run `tools/run_bounded_experiments.py` only as a contract-legibility screen and `tools/run_executable_mechanism_pilots.py` for isolated writable environment outcomes. Neither replaces distinct real-project replication and blind human review.

Use Hot State, Warm Index, and Cold Archive only when measured context growth or handoff pressure justifies the split. At claim-sensitive transitions, separate current basis, external basis, inference, unsupported claims, and falsification cues.

For substantial Complex changes, record a compact decision packet covering problem evidence, external implementation, alternatives, drawbacks, compatibility, evaluation, rollback, owner, and status. Routine fixes do not need this path.

Use evidence verbs precisely: examples illustrate, markers screen, fixtures reproduce, locked runs compare, and repeated real outcomes validate. The active decisions and evidence debt are in `docs/active-architecture-rebaseline.json`.

## 10. Choose Runtime Records

Use filled examples before blank templates. Minimum useful records are:

- `state.md` for recovery;
- `prompt.md` for stable intent;
- `context.md` when context selection matters;
- `harness.md` when tools, recovery, or observability matter;
- `loop.md` for outcome-based progress;
- `delivery.md` for audience alignment.

Templates remain optional. Use only the fields that influence judgment or recovery.

## Compact Start Prompt

```text
请按 Complex 推进当前项目。建立稳定的 Project Prompt Contract；每拍组装最小充分、可溯源的 Context Working Set；确认 Runtime Harness 的工具、边界、检查点和降级路线；运行以真实结果为完成条件的 Progress Loop：执行拍交付 forward artifact，诊断拍交付明确路线、反证、阻塞或停放决定。

先诊断问题属于 prompt、context、harness、loop 还是 model limitation，再修对应层。采用强自治与担责边界：项目内部编排由 AI 自判，只有 Goal/公开口径变化、账号付款、发布外写、不可逆或高影响外部承诺时问我。可继续时自动进入下一拍。输出只要人看版。
```
For multi-turn or multi-beat work with a verifiable stopping condition, activate Codex Goal when the surface exposes it. Keep the durable outcome and completion predicate in Goal, keep changing work in `beat_objective`, and treat a non-terminal `next_route` as queued execution rather than a progress-note ending.
