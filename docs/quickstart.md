# Complex Quickstart

Audience: a new agent asked to use Complex on a project.

Goal: start useful work in five minutes without reading a historical log.

## Minute 0-1: Read The Current Entrypoints

Read, in order:

1. `README.md`
2. `protocol/current-state.md`
3. this file
4. the first part of `protocol/core.md`

Remember the one-sentence model:

> Complex = strong-autonomy continuous execution with control-plane orchestration, evidence boundaries, anti-human/context-drift safeguards, and an auditable recovery chain.

If you are inside a downstream target project, resolve two sources before planning: the installed Complex runtime (`COMPLEX_HOME` or a user-provided path) and the target project materials. Complex provides operating rules; the target project provides facts, constraints, and local boundaries.

## Minute 1-2: Use The Behavior Kernel

Before planning, compress the project into seven actions:

1. Restore true state.
2. Classify project nature and convergence.
3. Assign decision rights and ask-user necessity.
4. Set the control plane, then choose the work target.
5. Run the lightest useful validation or execution on that target.
6. Deliver to the right audience.
7. Leave `next_route`.

If a mechanism name competes with these behaviors, the behavior kernel wins.

## Minute 2-3: Classify The Project

Choose one:

- `evidence_fill`: model, formula, metric, or framework is fixed; fill evidence and delivery boundary.
- `model_discovery`: framework, explanation path, metric, or research model is unsettled; protect candidate frames.
- `mixed`: start with model discovery, then switch to evidence fill when convergence conditions are met.
- `execution_delivery`: the main job is implementation, packaging, or delivery.

If unsure, default to `mixed` and make the uncertainty explicit.

## Minute 3-4: Pick A Runtime Shape

Use filled examples before blank templates:

- `docs/examples/evidence_fill_minimal_runtime/`
- `docs/examples/model_discovery_minimal_runtime/`
- `docs/examples/independent_review_minimal_runtime/`

Minimum records for a new project:

- `state.md`: current basis, goal, decision rights, and next route.
- `loop.md`: one small validation or explicit no-op.
- `delivery.md`: audience and output boundary.

Add only what the task needs:

- Evidence fill: `evidence.md`, `decision.md`, `search.md`.
- Model discovery: `framing.md`, `argument.md`, `judgment.md`.
- Independent review: `fact-ledger.md`, `judgment.md`, `decision.md`.
- Prompt-based continuity: `prompt.md`.

## Minute 4-5: Start Low-Friction Execution

If the user only says "按 Complex 推进", give short defaults instead of a mode menu:

- delivery audience:
- capability permission:
- topology:
- cadence:
- autonomy boundary:
- manual-action boundary:

Then make a narrow `round_goal` and execute the lightest useful next action. For continuous projects, first confirm the control plane: direction, authority, state, topology, routing, and stop conditions. If it is already valid, move directly into the work-plane beat.

Decision rights are two-sided:

- Prevent unsafe AI overreach.
- Prevent unnecessary human intervention.

If the next step is clear, low-risk, reversible, and inside the project's responsibility boundary, continue and record why the user was not asked. Do not write "next time you say continue" when `next_route` is already queued; either execute the next route now or, if a real turn/tool boundary stops the run, record the recovery route without making user continuation a permission condition. If `连续节拍` is selected, start each beat from a narrow `round_goal`, run the Loop, close or migrate the beat, then automatically enter the next queued low-risk beat until a real boundary appears. Do not stop because a fixed number of beats has run; before `STOP_COMPLETE`, scan for residual low-risk beats across the objective, current diff/state, validation gaps, consistency gaps, stale resources, and delivery contract. If the user gives paths, files, links, or material locations, read accessible materials yourself before asking for manual cleanup or summaries.

When Complex is applied to another repository, reconcile the user's steering words with that repository's local rules before executing. Read local `AGENTS.md`, `CONTEXT.md`, current state, stage boards, manifests, no-write boundaries, and manual-action records. Mark each major steering word as active, boundary-blocked, safety-overridden, or not needed with reason. If the main route is blocked by a true external-input boundary, continue only with allowed residual beats: boundary contradiction repair, submission-friction reduction, non-expansion verification, exact operator handoff, or preflight after the required file/env var appears.

When the request mentions Plan mode plus continuous cadence, Goal mode, threads, subagents, automation, or independent review, write an orchestration contract before the project plan:

- Which runtime resources are available: Goal/tool goal, user-visible Codex thread, worktree/background thread, automation/heartbeat, subagent, browser/API/account tools.
- Which resource is being used now and why.
- Which resource is unavailable, degraded, or crosses a real responsibility/platform side-effect boundary.
- Control plane: direction, authority, state, topology, routing, and stop conditions.
- Standing lane topology: manager thread, recurring review/evaluation lane, evidence/data lane, implementation lane, delivery/editorial lane, or other durable lanes that fit the project.
- Lane contract: each durable lane has a lane goal, input fact ledger, output contract, context reset rule, wake trigger, stale/retire condition, and observable evidence.
- Resource boundary: long-running lanes are project responsibilities; temporary subagents are short-lived workers. A subagent can help a lane, but it is not a lane.
- Authority boundary: choosing standing lanes, temporary workers, clean-context packets, or manager-owned lane records is AI runtime judgment. Ask the user only for accounts/API credentials, external writes, publishing, irreversible actions, high-risk claims, or platform-visible persistent resources that truly become user-owned side effects.
- Manager/worker split: main thread manages, workers do bounded work.
- Beat Router: `CONTINUE`, `SPAWN_SUBAGENT`, `CREATE_THREAD`, `CREATE_AUTOMATION`, `INTERRUPT_FOR_INPUT`, or `STOP_COMPLETE`.
- Stop conditions.

After the user confirms continuous execution, switch from planning to the continuous orchestration spine:

- Confirm the control plane before local execution unless current state already proves it is fresh.
- Keep a small `beat_queue`.
- Give every beat a narrow `round_goal`.
- Use a per-beat tool Goal when available; otherwise record `protocol_round_goal`.
- Execute the Beat Router decision before ending the beat.
- Continue through queued low-risk reversible beats until a real stop condition appears.
- Treat a fixed number of beats as a smoke-test floor, not a completion reason; stop only after the objective, validation, and residual-beat scan support `STOP_COMPLETE`.
- After the final write, run validation and residual-beat scan again before claiming `STOP_COMPLETE`.
- In the human-readable final answer, include a compact runtime audit: beat goals, Goal/protocol_goal use, Beat Router routes, auto-start decisions, resource evidence or degraded notes, final validation, and residual scan.
- Assess threads, subagents, review lanes, and automations as resources that may mature over the first few beats; do not block Goal/Plan/Loop because those resources are not ready yet. If a durable lane is needed but cannot yet be created as a visible thread or automation, keep a manager-owned lane record and continue. Do not phrase ordinary topology selection as "waiting for user authorization."
- Watch for unobservable resources: if a clean thread, worker, review lane, or automation produces no contract, action, or result in the first beat window, mark it degraded and route to another safe path instead of waiting indefinitely.

If the user asks for independent review inside the same session, do not claim roleplay is independent. Use clean context, a separate reviewer/thread, read-only audit subagent, or a fact-ledger packet when independence matters. Reset review context every independent review beat; if you stay in the same session, label it as diagnostic self-review.

During prompt design, choose safe recommended defaults yourself when the user asked for strong-autonomy Complex execution. Ask only for authority, irreversible choices, public-facing direction changes, or high-risk judgment. Do not phrase an AI-selected default as something the user selected.

Keep bootstrap in the manager thread. Source resolution, project-nature judgment, the first orchestration contract, and the first beat queue should not depend on a background thread or subagent returning. Auxiliary resources can help after a usable route exists; if they are silent, degrade them and continue.

## When Something Feels Wrong

Do not immediately add a new core rule.

1. Map the failure to a case in `docs/behavior-regression-cases.json`.
2. Run transcript review:

```bash
python3 tools/review_behavior_transcript.py --case-id <case_id> --text-file <response.txt>
```

3. Record the result in `docs/behavior-review.md`.
4. If the failure repeats, update a transcript rule, behavior case, or golden example before promoting a new core rule.

## Best Default Prompt

```text
请先按 Complex 恢复当前状态，并用 7 步行为内核压缩本轮行动。
Complex 来源使用 `COMPLEX_HOME` 或我提供的路径；目标项目来源使用当前仓库或我提供的材料路径。Complex 提供运行规则，目标项目提供事实材料和本地边界。
如果当前界面支持 Plan 模式，请先提醒我开启 Plan 模式完成扫描、判断和计划，再进入执行。
请先显式判断这些 steering words 是否适用，并把适用项写入本轮 prompt/plan：开启 Plan 模式 / 先规划再执行；模型发现型 / 先发散研究框架 / 不要早收敛；证据填充型 / 模型和指标已定；连续节拍 / 总规划别丢 / 每轮 prompt 重水化；每拍窄 Goal / 自动进入下一拍 / 不等我说继续；控制层优先 / 主控线程 / 长期审核评议通道；少问我 / 能推进就继续 / 我给目录你自己读；长期线程和临时子代理分开 / 每轮清上下文；运行资源 AI 自判 / 用户只担责授权；独立评审 / 客观审查 / 避免上下文污染；外部工具 / 账号 / API / skill；目标仓库边界对账 / 真人工边界 / 剩余可自动小拍；编排预检 / Goal mode / 长期线程 / automation / Beat Router / stop condition；只要人看版。
先判断本项目是 evidence_fill、model_discovery、mixed 还是 execution_delivery。
如果缺少我的确认，请优先采用安全推荐默认项并标注为 assumed_default；不要把内部路线选择抛给我。只有主目标、账号/API、外部写入、不可逆动作、公开口径或高风险判断变化才问我。不要把 AI 自己选的默认项写成“用户选择了”。
如果下一步已由 next_route / round_goal / 可访问材料说明清楚，请直接推进并说明为什么不需要回问；如果我给了目录、文件或链接，请优先自行读取。
不要用“下次你说继续时再推进”作为默认收尾。若下一拍已 queued 且低风险可逆，默认自动进入下一拍；若受回合或工具边界限制必须暂停，只记录 next_route，不把用户说“继续”当成许可门。不要因为已经跑了若干拍就停；停止前必须做 residual-beat scan，确认目标、验证、交付契约和可自动小拍都已经收口。若 residual scan 触发了新的写入，必须在最后一次写入之后重新验证并再次扫描，才能 STOP_COMPLETE。
如果启用连续节拍，每一拍都要建立/记录窄 round_goal，工具 Goal 可用则只承载本拍，不可用则记录 protocol_round_goal；执行 Loop 和 Beat Router 后自动进入下一拍。线程、代理、automation 可以先判断成熟度、可用性和责任/平台边界，不成熟不强开，但不能因此跳过 Goal/Plan/Loop。若需要独立评审，每一轮审核用清上下文、事实账本或只读审核线程，不把同 session 自评说成独立评审。
如果目标仓库本地规则把某个 steering word 缩窄或阻断，请明确做边界对账：哪些 active_now，哪些 active_but_boundary_blocked，哪些 overridden_by_project_safety，哪些 not_needed_with_reason。遇到真实外部输入门时，先做剩余可自动小拍；只有确实没有低风险内部小拍时，才暂停并给出具体文件、字段、env var 和命令。
如果请求涉及连续节拍、Goal、长期线程、子代理或 automation，先输出 Orchestration Contract：能力预检、资源术语消歧、控制层、长期通道拓扑、责任/平台边界、总控/worker 分工、Beat Router 和 stop condition。连续项目先确认控制层：方向、责任边界、状态、拓扑、路由和停止条件；其中拓扑包括主控线程、长期审核评议通道、资料/证据通道、执行通道、交付通道或其他适配项目的 durable lanes。不要把子代理说成左侧栏长期线程；子代理只是短期 worker。长期通道是否需要、何时成熟、先用 manager-owned lane record 还是可观察线程，由 AI 自行判断；只有账号/API、外部写入、发布、不可逆动作、高风险主张或平台可见持久资源创建真正需要用户担责时才回问。
连续项目先确认控制层；单轮任务再只抓一个最高杠杆问题。用最轻有效动作推进，最后给出适合交付对象的人看版，并留下 next_route。
```
