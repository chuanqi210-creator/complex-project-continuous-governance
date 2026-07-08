# Complex Quickstart

Audience: a Codex agent asked to use Complex on a project.

Goal: start useful work in five minutes without reading history logs.

## Minute 0-1: Read Current Entrypoints

Read:

1. `README.md`
2. `protocol/current-state.md`
3. this file
4. `protocol/core.md`
5. `docs/mechanism-maturity.md`
6. the closest filled example in `docs/examples/`

Remember the model:

> Complex = Codex-native orchestration for strong-autonomy execution inside a responsibility boundary, portfolio control-plane organization, attention governance, external calibration, evidence boundaries, clean review, and lightweight auditable recovery.

When applying Complex to another repository, resolve the Complex runtime as the rule source and the target repository as the fact source. Do this quietly and proceed; do not turn source resolution into a user-facing apology.

## Minute 1-2: Align Codex Surfaces

Run `codex_surface_alignment`:

- Plan mode: user/interface surface. At complex or strategic beats, AI decides that a planning checkpoint is required. If UI Plan mode is not active or not controllable from the current surface, output a plan-shaped checkpoint and continue within the responsibility boundary.
- Codex Goal: persistent objective and completion criteria for a longer task, thread, or bounded phase. Use `thread_goal` / `phase_goal`; AI decides whether the Goal surface should carry the phase contract, and records the contract in state/prompt/handoff when the surface cannot be set.
- `beat_objective`: current small target inside Plan/Loop.
- `goal_memory_summary`: recovery summary, not Codex Goal.
- Continuous cadence: same-run queued beats continue until `STOP_COMPLETE` or a true boundary.
- Cross-turn continuation: use thread heartbeat or automation when available; if unavailable, record the heartbeat/automation contract and recovery route without treating it as user permission.
- Subagent: short-lived bounded worker.
- Standing lane: durable manager-owned responsibility.
- User-visible thread/worktree/automation: platform resource; AI decides whether it fits the operating organization, while actual creation follows current Codex surface/tool semantics.

## Minute 2-3: Use The Behavior Kernel

Compress the project into seven actions:

1. Restore true state.
2. Classify project nature and convergence.
3. Assign decision rights through the responsibility boundary.
4. Establish control plane and operating organization before local optimization.
5. Run the smallest meaningful target-function Loop or execution beat.
6. Deliver to the right audience.
7. Leave `next_route`, accepted artifacts, and recovery pointers.

If a mechanism name competes with these behaviors, the behavior kernel wins.

## Minute 2-3: Read Mechanism Maturity

Use `docs/mechanism-maturity.json` to decide how strongly a mechanism should steer the run:

- `core`: always respect it.
- `validated`: use it confidently for matching project shapes.
- `tested`: use it when its failure mode appears, but still watch for overhead.
- `candidate`: treat it as a promising route, not a proven answer.
- `retired`: do not use it for new work.

Do not promote a candidate just because it sounds elegant. Prefer behavior cases, transcript rules, examples, and external micro-contracts before expanding the core protocol.

## Minute 3: Form The Operating Organization

For a continuous project, do not jump from one local task to the next. First form the operating map:

- `thread_goal` or `phase_goal`: persistent objective and completion criteria.
- `target_function`: what the project is optimizing.
- `module_portfolio`: components that can move separately.
- `standing_lane_portfolio`: controller, human interface, literature/data acquisition, model/component, data-code, review/risk, writing/delivery, or project-specific lanes.
- `forward_indexes`: module status, data assets, parameter candidates, writing scaffolds, branch parking, decisions, and accepted artifacts.
- `state_lightening`: Hot State, Warm Index, Cold Archive.
- `external_calibration`: latest outside-pattern check or reason it is not needed for this beat.
- `hallucination_sentinel`: current basis, external basis, inference, unsupported claim, falsification cue.
- `attention_governance`: minimum viable closure, minimum sufficient observability, and process-overhead risk.

Use this acceptance rule:

```text
beat accepted = forward artifact exists or is updated
              + relevant guard passed
              + index/state updated
              + next route selected
```

Guardrail-only work is allowed, but repeated guardrail-only work triggers a toil/WIP review: create a forward artifact, park the branch, route to another module, or justify why the guardrail is the true target-function dependency.

For research, analysis, or prototype projects, do not spend many beats polishing local material before an end-to-end chain exists. Aim for a minimum viable closure: question/problem, source/data or input path, minimal model/assumption, result/output, figure/table or validation signal, claim/usable conclusion, limitation, and next weakness. If the startup window passes without this chain, run a governance review and choose: downscope, use a provisional slice, justify prework as the true dependency, or park and route elsewhere.

## Minute 3-4: Classify The Project

Choose one:

- `evidence_fill`: model, formula, metric, or framework is fixed; fill evidence and delivery boundary.
- `model_discovery`: framework, explanation path, metric, or research model is unsettled; protect candidate frames.
- `mixed`: start with model discovery, then switch to evidence fill when convergence conditions are met.
- `execution_delivery`: implementation, packaging, delivery, validation, and recovery.

If unsure, default to `mixed` and state the uncertainty.

Evidence-fill work should keep a clear claim boundary: what can be said, what cannot be said, and what source would upgrade the claim.

## Minute 4: External Calibration And Hallucination Sentinel

Do not change an important method, route, structure, prompt default, protocol behavior, model, or evaluation rule only from internal Complex vocabulary.

For each mechanism-level issue, record:

- source;
- problem matched;
- adopted;
- rejected;
- not transferable;
- Complex micro-contract;
- refresh trigger.

Use official docs, primary papers, standards, or mature production writeups. The micro-contract must be operational: entry condition, accepted artifact, extraction form, WIP/toil limit, stop/park rule, review checklist, state-compaction rule, or refresh trigger.

Run `hallucination_sentinel` at startup, every 5 accepted beats, phase switches, public delivery, model/source/prompt upgrades, external calibration, or before promoting a new protocol behavior.

## Minute 4-5: Pick Runtime Shape

Use filled examples before blank templates:

- `docs/examples/evidence_fill_minimal_runtime/`
- `docs/examples/model_discovery_minimal_runtime/`
- `docs/examples/independent_review_minimal_runtime/`
- `docs/examples/portfolio_orchestration_minimal_runtime/`
- `docs/examples/external_calibration_micro_contract_runtime/`
- `docs/examples/operating_organization_multi_lane_runtime/`

Check `docs/examples/example-currentness.md` before treating an example as authoritative. The current examples are filled examples unless real transcript or end-to-end reuse promotes them.

Minimum records for a resumable project:

- `state.md`: current basis, goal memory, `beat_objective`, decision rights, and next route.
- `loop.md`: target-function Loop, closure segment, observability decision, or explicit no-op.
- `delivery.md`: audience and output boundary.

For continuous work, also record:

- `beat_queue`;
- standing lane contracts;
- clean-review context reset policy;
- Beat Router decision;
- forward artifact acceptance;
- trace appraisal and external calibration status.

## Execution Defaults

Use recommended defaults instead of a mode menu:

- Manager thread owns direction and integration.
- Strong autonomy inside the responsibility boundary.
- Read accessible files, directories, and links yourself.
- Ask only for responsibility-bearing boundaries: main-goal change, account/API/payment/publishing/external write, irreversible action, public voice, high-risk claim, or a platform action that creates a user-owned external commitment.
- Human-readable delivery unless the user asks for machine recovery records.

If the next beat is clear and inside the responsibility boundary, execute it. Do not end with "say continue next time." If a true turn/tool boundary stops the run, write `next_route` as recovery, not as permission.

Routine beats should not become reporting ceremonies. Use minimum sufficient observability: closure segment moved, forward artifact changed, uncertainty reduced or exposed, cannot-yet-claim boundary, and next beat. Use heavier evidence packs only for trigger points such as phase switch, public delivery, claim upgrade, contradiction, repeated guardrail-only work, missing closure, external calibration, hallucination sentinel, reviewer handoff, or user-requested audit.

## Orchestration Contract

When the request mentions Plan mode, continuous cadence, Goal mode, threads, subagents, automation, standing review, or independent review, write the orchestration contract before business execution:

- `capability_preflight`: Codex Goal, thread/worktree, automation/heartbeat, subagent, browser/API/account tools, project scripts.
- `resource_taxonomy`: Plan surface, `thread_goal` / `phase_goal`, `beat_objective`, standing lane, subagent, automation.
- `control_plane`: direction, authority, state, topology, routing, stop conditions.
- `operating_organization`: controller, human interface, literature/data, model/component, data-code, review/risk, writing/delivery.
- `portfolio_operating_model`: target function, modules, lanes, forward indexes, branch parking, Hot/Warm/Cold state.
- `external_calibration`: source class used, transfer limits, micro-contract, hallucination sentinel, refresh trigger.
- `manager_worker_contract`: manager integrates; workers do bounded work and return summaries.
- `Beat Router`: `CONTINUE`, `SPAWN_SUBAGENT`, `CREATE_THREAD`, `CREATE_AUTOMATION`, `INTERRUPT_FOR_INPUT`, `STOP_COMPLETE`.

After execution starts, the orchestration contract is not itself completion. Each beat needs a `beat_objective`, action, route, validation, accepted artifact or branch decision, and next route.

## Independent Review

Same-session review is diagnostic. True independent review needs clean context, a separate reviewer/thread, read-only audit worker, or a fact-ledger packet. Reset the reviewer context every review beat.

Use `review_context_reset_each_beat` when review repeats: every independent review beat starts from a fresh fact ledger or clean reviewer context.

## When Something Feels Wrong

Do not immediately add a new core rule.

1. Map the failure to `docs/behavior-regression-cases.json`.
2. Compare the issue with external mature practice and write the micro-contract.
3. Run transcript review:

```bash
python3 tools/review_behavior_transcript.py --case-id <case_id> --text-file <response.txt>
```

4. Record the result in `docs/behavior-review.md`.
5. Check the linked mechanism status in `docs/mechanism-maturity.json`.
6. If the failure repeats, update a transcript rule, behavior case, filled example, or mechanism status before promoting a new core rule.

## Compact Default Prompt

```text
请按 Complex 推进当前项目。

先恢复状态，建立 thread_goal 或 phase_goal，并做 codex_surface_alignment：Plan mode 是界面规划 surface；关键节拍必须做 planning checkpoint，但不能伪称自动开启 UI Plan mode。Codex Goal 承载长期任务/线程/阶段的 persistent objective 和完成标准，由 AI 判断是否使用 Goal surface；不能设置时写入 state/prompt/handoff，不把 Goal 选择变成用户授权。beat_objective 是每拍 Plan/Loop 里的小目标；goal_memory_summary 只是恢复摘要。subagent 是短期 worker，standing lane 是长期责任通道；thread/worktree/automation fit 由 AI 判断，实际创建服从当前 Codex surface/tool 语义。

请判断 project_nature：evidence_fill / model_discovery / mixed / execution_delivery。采用强自治+担责边界：项目内部计划、读取、验证、Plan/Goal 适配、运行拓扑、standing lane 记录、thread/worktree/automation fit、临时 worker fit、状态压缩和下一拍推进由 AI 自行判断；只有主目标、账号/API、付款、外部写入、发布、不可逆动作、公开口径、高风险主张，或平台动作会造成我需要担责的外部承诺时再问我。

连续项目先建立 operating organization：controller、human interface、literature/data acquisition、model/component、data-code、review/risk、writing/delivery。每拍重水化 master prompt、current_basis、target_function 和 beat_objective；运行 target-function Loop 和 Beat Router；可继续时自动进入下一拍，直到 STOP_COMPLETE 或真实担责边界。每拍验收以 forward artifact 为核心；审计、citation、QA、reviewer、metadata/no-values 是护栏，不应长期成为唯一主产物。

重要路线、模型、方法、评估、prompt 默认值或协议判断前，做 external calibration：对照官方文档、原始论文、标准或成熟生产实践，说明 adopted / rejected / not transferable，并把 adopted lesson 翻译成项目 micro-contract。按阶段运行 hallucination sentinel，区分 current_basis、external_basis、inference、unsupported claim 和 falsification cue。长期项目用 Hot State / Warm Index / Cold Archive 轻量化。研究、分析或原型项目先追求最小可审计闭环：问题、数据/来源、最简模型或假设、结果、图表/验证信号、论断、局限和下一弱点。平时只输出最低充分可观测信号，不把汇报和审计变成项目主工作。

输出只要人看版。
```
