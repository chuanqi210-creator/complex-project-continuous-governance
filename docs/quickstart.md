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

Do not read Complex's `protocol/current-state.md` into a target project's Context Working Set. It describes Complex's own maintenance state, not the target project.

When maintaining Complex itself, read `README.md`, `protocol/current-state.md`, this quickstart, and `protocol/core.md` before changing the runtime.

Treat the installed Complex runtime as the rule source and the target repository as the fact source. Read Warm/Cold material only by pointer when the active beat needs it.

Before recursive target-project scanning, locate project-native durable instructions and one authoritative recovery anchor for Goal, current basis, active module, open risks, and next route. If the anchor is absent, do a bounded root/latest-accepted-artifact bootstrap and record unknowns explicitly. Do not search hundreds of outputs to manufacture certainty, and do not treat a proposal as accepted controller state.

An existing anchor must still pass four checks: explicit authority, assessable freshness, bounded Hot State, and exactly one authoritative next route. If it is oversized or contradictory, select a state-reconciliation beat before project work. Inspect only route/status keys and accepted pointers; do not read a giant manifest in full or resolve disagreement by choosing the newest file.

Bound the inspection itself: measure scale first, list names/types before values, and stop the first pass after 50 matched names or 80 text lines, 32 KiB of output, or 30 seconds per source unless the project records a justified alternative. Truncation or over-budget matches show that the source does not fit the current working-set envelope; they do not decide authority. Keep it Warm by pointer instead of retrying with a broader search.

For the common `AGENTS.md` / `CONTEXT.md` / `notes/current_status.md` / `deliverables/manifest.json` layout, create a bounded fact ledger mechanically before clean-context evaluation:

```bash
python3 "$COMPLEX_HOME/tools/inspect_recovery_anchor.py" /absolute/path/to/target-project
```

The extractor does not choose authority. Its default ledger emits relative source paths, scale, line numbers, structural line types, matched term categories, and value types; it does not emit source snippets, raw JSON key names, absolute paths, project identifiers, or content fingerprints. It caps previews, matches, scan bytes, elapsed work, and output bytes, and stops matching after overflow. The evaluator decides whether state reconciliation is required. The extractor's internal deadline is a soft cooperative bound; the manager/watchdog owns the hard process or worker timeout.

## 2. Align Codex Surfaces

- Plan mode is a planning surface. Use it at project start and strategic checkpoints when available; otherwise create a plan-shaped checkpoint.
- Codex Goal carries `thread_goal` or `phase_goal`, not changing beat chores.
- `beat_objective` is the current Plan/Loop target.
- Subagents are bounded workers; standing lanes are recurring responsibilities.
- Thread, worktree, and automation fit are orchestration decisions executed through available tools.
- Continuous cadence continues queued work until objective completion or a real responsibility/tool boundary. If cross-turn continuation is selected and heartbeat/automation tooling is callable, create it during harness setup and record its status. Do not treat a saved `next_route` or a recommendation to create automation later as cross-turn activation.

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

`durable instructions -> Hot State -> active module -> just-in-time retrieval -> provenance/freshness -> trim/compact -> exclusions`

The working set must identify current basis, stale material, open risks, retrieved pointers, and next route. After compaction or handoff, verify semantic recovery rather than file presence.

### Runtime Harness

Check the capabilities that affect this project:

- workspace and isolation;
- tools, skills, browser, MCP, API, and temporary workers;
- side effects and responsibility boundaries;
- tests, schemas, hooks, logs, metrics, and evaluator;
- checkpoint, retry, timeout, idempotency, rollback, and degraded routes.

If a beat must pause for approval or external input, apply `interrupt_resume_safety`: do read-only or local draft work before the pause, put non-idempotent external writes after authorization, and record the checkpoint, idempotency key or stable identifier, compensation path, and resume route.

Discover capabilities just in time. Do not load everything into every beat.

### Progress Loop

Use:

`restore -> select -> act -> observe -> evaluate -> route/retry/rollback/stop`

Define a forward artifact and outcome completion predicate before execution. For important work, separate executor and evaluator. Do not stop from a fixed beat count or agent self-report.

## 4. Run The Behavior Spine

1. Restore state and context.
2. Classify `evidence_fill`, `model_discovery`, `mixed`, or `execution_delivery`.
3. Assign responsibility and decision rights.
4. Form the control plane, operating organization, and harness.
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

## 6. Form The Operating Organization

For recurring work, assign manager-owned lanes:

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
beat accepted = forward artifact or explicit branch decision
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

For mechanism-level changes, record external source, problem matched, adopted, rejected, not transferable, micro-contract, and refresh trigger. External precedent is design evidence, not proof of Complex effectiveness.

Use Hot State for the current map, Warm Index for compact ledgers, and Cold Archive for raw traces by pointer. Run a hallucination sentinel at important transitions and before public delivery.

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
请按 Complex 推进当前项目。建立稳定的 Project Prompt Contract；每拍组装最小充分、可溯源的 Context Working Set；确认 Runtime Harness 的工具、边界、检查点和降级路线；运行以真实结果和 forward artifact 为完成条件的 Progress Loop。

先诊断问题属于 prompt、context、harness、loop 还是 model limitation，再修对应层。采用强自治与担责边界：项目内部编排由 AI 自判，只有 Goal/公开口径变化、账号付款、发布外写、不可逆或高影响外部承诺时问我。可继续时自动进入下一拍。输出只要人看版。
```
