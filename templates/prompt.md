# Prompt Bootstrap Template

Use this file when a user wants the agent to scan Complex, design a project-specific prompt, and execute only after confirmation.

## High-Fit User Request

```text
请帮我扫描 Complex，并对我们的项目设计提示词。之后给出一个可复制的 prompt；我确认后，再根据这个 prompt 结合 Complex 推进项目。

请显式采用这些 steering words，并按项目实际情况取舍：
开启 Plan 模式 / 先规划再执行；模型发现型 / 先发散研究框架 / 不要早收敛；证据填充型 / 模型和指标已定；最小可审计闭环 / 先串起问题-数据-模型-结果-论断；注意力治理 / 最低充分可观测性 / 不要过度汇报；连续节拍 / 总规划别丢 / 每拍 prompt 重水化；Codex Goal 是 thread_goal 或 phase_goal / beat_objective 属于每拍 Plan；自动进入下一拍 / 不等我说继续；模块组合 / 串并联系统 / 不要局部贪心；forward artifact / 审计只是护栏 / Hot State；外部优秀案例 / external calibration / micro-contract；定期 hallucination sentinel；少问我 / 能推进就继续 / 我给目录你自己读；运行资源 AI 自判 / 用户只担责授权；standing lane 和 subagent 分开 / 每轮清上下文；独立评审 / 客观审查 / 避免上下文污染；外部工具 / 账号 / API / skill；只要人看版。
```

## Protocol Scan Summary

- complex_source_resolution:
- protocol_scan_sequence:
- complex_source files read:
- target_project_source files read:
- components adopted now:
- components skipped now:
- components backlogged:
- manual actions or permissions needed:
- biggest misread risk:

## Project Intake

- Project goal:
- Existing materials:
- User steering words:
- Codex surface alignment:
- Plan mode / planning checkpoint status:
- Codex Goal fit:
- Current basis:
- Known constraints:
- Project nature: evidence_fill / model_discovery / mixed / execution_delivery
- Convergence status:
- Candidate frameworks or fixed evidence model:

## Startup Defaults

- Delivery audience and format:
- Capability permission:
- Responsibility boundary:
- Cadence:
- Operating organization:
- Standing lane topology:
- Temporary worker fit:
- Review context reset policy:
- Portfolio operating model needed:
- Target function:
- Module portfolio:
- Forward indexes:
- State lightening:
- Minimum viable closure needed:
- Minimum sufficient observability:
- Attention budget:
- External calibration needed:
- Hallucination sentinel needed:

## Prompt Design Rationale

- Why this project needs Complex:
- Why this project nature fits:
- What the agent may decide without asking:
- What must trigger user confirmation:
- Why selected capabilities fit:
- Why rejected capabilities are deferred:
- What the first target-function Loop should learn or advance:
- What the first minimum viable closure should show:
- What prevents premature convergence or unnecessary divergence:
- What prevents local greedy optimization:
- What prevents governance/reporting from consuming attention:
- What would trigger route-back:

## High-Fidelity Startup Prompt

```text
请按 Complex 项目持续治理协议推进以下项目。

项目目标：

已有材料：

交付对象：

第一步请恢复状态，并建立：
1. thread_goal 或 phase_goal：长期任务/线程/阶段的顶层目标、完成标准和验收方式。
2. goal_memory_summary：便于后续恢复的摘要，不等于 Codex Goal。
3. beat_objective：本拍 Plan/Loop 要解决的小目标。

Codex surface map：
- Plan mode：如果当前界面支持并可由你实际使用，请使用可用的规划 surface；如果当前界面不能由你切换，也直接输出 planning checkpoint。不要伪称已经自动开启。
- Codex Goal：作为 thread_goal 或 phase_goal，承载 persistent objective 和完成标准；AI 判断是否使用 Goal surface。不能设置时写入 state/prompt/handoff，不把 Goal 选择变成用户授权；不要把下一步小动作塞进长期 Goal。
- beat_objective：每拍小目标，属于 Plan/Loop。
- continuous cadence：同一运行中自动推进 queued beats；跨回合续跑只在 heartbeat/automation 可用且担责边界允许时使用。
- subagent：短期 bounded worker，不是 standing lane。
- standing lane：长期责任通道，可先用 manager-owned lane record 表达。
- user-visible thread / worktree / automation：平台资源，不默认属于担责边界；AI 判断是否适合，实际创建服从当前 Codex surface/tool 语义。若不能创建，就记录 contract 并继续总控推进。

项目性质：
- project_nature：
- convergence_status：

强自治+担责边界：
- AI 可自行判断：项目内部计划细节、读取、验证、能力取舍、Plan/Goal 适配、standing lane 记录、thread/worktree/automation fit、临时 worker fit、证据深度、发散/收敛节奏、状态压缩和下一拍推进。
- 必须回问：主目标改变、账号/API/付款/发布/外部写入、不可逆动作、公开口径变化、高风险主张，或平台动作会造成我需要担责的外部承诺。

连续节拍：
- 每拍先重水化 master prompt、current_basis、target_function 和 beat_objective。
- 关键节拍固定做 planning checkpoint；这不是向我索要授权，而是 AI 自己按推荐方案规划。
- 运行 target-function Loop 和 Beat Router。
- 可继续时自动进入下一拍，不等我说继续。
- 如果真实边界阻断，只记录 next_route、具体边界和可恢复路径。
- STOP_COMPLETE 前必须做 residual scan；固定拍数不是停止条件。

操作组织：
- 先建立 operating organization：controller、human interface、literature/data acquisition、model/component、data-code、review/risk、writing/delivery。
- standing lane 是长期责任；subagent 是短期 worker。
- 文献/数据 lane 启动时要预判学术账号、数据库、API、机构权限和用户担责事项。
- 独立评审必须使用清上下文、事实账本、独立 reviewer/thread 或只读 audit worker；同 session 只能叫 diagnostic self-review。

项目组合编排：
- 连续项目先形成 portfolio operating model：target_function、module_portfolio、standing_lane_portfolio、forward_indexes、branch_parking 和 Hot/Warm/Cold state。
- 每拍验收以 forward artifact 为核心：model_delta、data_delta、parameter_delta、writing_delta、branch_delta、calibration_delta、state_delta 或 topology_delta。
- 审计、citation、QA、reviewer、metadata/no-values 是护栏，不应长期成为唯一主产物。
- 重复 guardrail-only work 触发 toil/WIP review：推进 forward artifact，停放分支，转向其他模块，或说明该 guardrail 为什么是真依赖。
- 串行只发生在同一证据链内部；不同模块、来源、写作 scaffold、审查 lane 可以并行推进时，不要让一个局部路径成为全局瓶颈。

注意力治理与最小闭环：
- 研究、分析或原型项目优先跑出最小可审计闭环：问题/目标、数据/来源或输入路径、最简模型/假设、结果/输出、图表/验证信号、论断/可用结论、局限和下一弱点。
- 最小闭环不是最终交付，而是判断项目是否真的向前的可见主链。
- 平时只给最低充分可观测信号：本拍推进了哪个闭环环节、更新了哪个 forward artifact、减少或暴露了哪个不确定性、现在还不能证明什么、下一拍是什么。
- 厚重证据包、完整审查报告和长总结只在阶段切换、公开交付、重要论断升级、矛盾、重复 guardrail-only、最小闭环缺失、外部校准、hallucination sentinel、评审交接或用户要求时触发。

外部校准与防幻觉：
- 重要战略、结构、模型、方法、评估、prompt 默认值或协议判断前做 external calibration。
- 每个机制级问题都要有：source、problem matched、adopted、rejected、not transferable、Complex micro-contract、refresh trigger。
- 优先对照官方文档、原始论文、标准或成熟生产实践。
- 定期运行 hallucination sentinel：区分 current_basis、external_basis、inference、unsupported claim 和 falsification cue。

轻量恢复：
- Hot State 保留当前地图。
- Warm Index 保留紧凑索引和 accepted artifacts。
- Cold Archive 保留原始 trace、旧 gate、旧搜索和旧审计指针。
- 不把全部历史塞入每拍上下文。

第一拍：
- beat_objective：
- target-function Loop：
- forward artifact：
- 验收条件：
- 不可证明什么：
- next_route：

输出只要人看版。若必须暂停，请只说明具体文件、字段、env var、命令或担责边界，不要泛泛问我要不要继续。
```

## Project Master Prompt

- thread_goal:
- phase_goal:
- completion_criteria:
- goal_memory_summary:
- responsibility_boundary:
- operating_organization:
- portfolio_operating_model:
- external_calibration_policy:
- hallucination_sentinel_policy:
- trace_appraisal_policy:
- minimum_viable_closure_policy:
- minimum_sufficient_observability_policy:
- delivery_contract:

## Per-Beat Planning Prompt

Use at the start of each continuous beat, Plan-mode continuation, or `next_route` handoff.

- beat_index:
- master_prompt_location:
- goal_memory_summary:
- thread_goal / phase_goal:
- beat_objective:
- latest state/current_basis:
- project_nature:
- convergence_status:
- inherited master constraints:
- previous-beat status:
- new beat judgment:
- prompt patch from user details:
- target_function:
- module served:
- standing lane served:
- closure segment served:
- observability signal:
- external_calibration_status:
- hallucination_sentinel_status:
- Hot/Warm/Cold state status:
- Beat Router decision:
- termination_condition:

Rules:

- Compress and inherit the confirmed master prompt; do not rewrite it unless the user explicitly changes the main goal.
- Treat user detail changes as prompt patches by default.
- Generate Plan and Loop from `beat_objective`, target function, and operating organization, not from the local task alone.
- If the beat prompt cannot be reconstructed, route back to state recovery before execution.

## Compact Continuation Prompt

```text
继续按 Complex 推进。先恢复 goal_memory_summary、current_basis、target_function、operating organization、external calibration status、hallucination sentinel status 和 next_route。建立本拍 beat_objective，做 planning checkpoint，运行 target-function Loop，验收 forward artifact，更新 Hot/Warm/Cold 状态，然后自动进入下一拍或说明真实担责边界。输出只要人看版。
```
