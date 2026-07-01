# Complex Runtime Cadence Simulation 2026-07-01

用途：用小模拟验证本轮修复是否覆盖用户在其他项目使用 Complex 时遇到的四类摩擦：完整扫描不足、提示词设计未前置、连续节拍中拓扑/工具不复盘、Goal 漂移或完成后自动停止。

本记录不是新的长期机器看版，不改变当前恢复入口；它只作为本轮协议修复的小题证据。

## Scenario 0: 新用户只说“按 Complex 推进”

用户提示：

```text
这个项目按 Complex 推进。
```

旧风险：

- 模型把用户带进“普通项目/重大项目/Plan-only/Goal 模式”的模式菜单，让用户理解内部路由。
- 模型等用户自己说出“连续节拍、多线程、外部工具、人看版”等触发词，新用户不知道这些入口。
- 一次性任务没有 round_goal、Loop 或评分路由，后续交付和恢复容易漂移。

新期望：

- 先运行 `complex_setup_question_card`，确认或默认交付对象、能力权限、协作拓扑、推进节拍和人工边界。
- 展示 `user_visible_trigger_guide`，告诉用户可以用“先设计提示词/prompt”“连续节拍”“多线程/子代理”“外部工具/账号/API”“完整扫描 Complex”“只要人看版”改变推进方式。
- 不让用户选择普通/重大项目；若有高风险、高返工或高公共性，只在内部做工作力度/风险升级并兼容记录 `major_project_mode`。
- 无论是否连续，都建立 round_goal、Plan、Loop/小检查、评分路由、交付契约和恢复记录。

模拟结论：

- 新协议可检查到 `hidden_trigger_vocab_gap`、`major_project_user_mode_confusion_gap`、`optional_goal_plan_loop_gap` 和 `setup_question_missing_gap`。
- Runtime Kit 由 `templates/question.md` 承接启动提问卡，`templates/state.md` 记录用户选择，`templates/loop.md` 记录本轮目标和 Loop 路由。

## Scenario 0.5: 用户只想先设计项目 prompt

用户提示：

```text
请帮我扫描 Complex，并对我们的项目设计提示词。之后给出一个完美 prompt，再根据这个 prompt 结合 Complex 推进项目。
```

旧风险：

- 模型直接开始做项目，跳过提示词设计前置。
- 模型只给普通 prompt 模板，没有说明实际扫描了哪些 Complex 组件。
- prompt 没有写进能力边界、子代理/多线程、连续节拍、Goal/Loop、评分路由和交付契约，后续线程仍然会漂移。

新期望：

- 先触发 `complex_prompt_bootstrap_gate`，业务执行暂停。
- 输出 `protocol_scan_summary`、`startup_questions_or_defaults`、`project_prompt_design_rationale`、`copy_ready_prompt` 和 `execution_bridge`。
- `copy_ready_prompt` 必须包含项目目标、材料、交付对象、能力边界、协作拓扑、cadence、round_goal/active_goal、Loop、评分路由、证据/权限边界和恢复记录方式。
- 用户确认前不执行、发布或写外部系统；确认后仍以 Complex 主协议和用户最新指令为准。

模拟结论：

- 新协议可检查到 `prompt_bootstrap_missing_gap`。
- Runtime Kit 由 `templates/prompt.md` 承接可复制 prompt，`templates/question.md` 承接 Prompt Bootstrap Card，`templates/state.md` 记录 prompt_bootstrap_status。

## Scenario 0.6: 第二轮 Plan 忘记总 prompt

用户提示：

```text
根据上一轮设计好的 prompt，开启 Plan 模式继续推进下一轮。
```

旧风险：

- 第一轮 `copy_ready_prompt` 质量高，但第二轮 Plan 只关注当前任务，把总规划降级成一句“遵循前文”。
- 用户补充局部细节后，Plan 把细节放大成主线，长期目标、能力边界和交付契约逐渐淡化。
- 连续几轮后，`active_goal`、`next_route` 和项目实际版本仍在推进，但 master prompt 没有进入恢复链。

新期望：

- 先触发 `round_prompt_rehydration_gate`，从 master prompt / active goal、最新 state 和本轮最高杠杆问题生成 `round_execution_prompt`。
- 第二轮 Plan 必须写明：来自总规划的约束、来自上一轮状态的变化、本轮新增判断。
- 用户补充局部细节时默认作为 prompt patch 写入本轮 prompt；除非用户明确改目标，否则总 prompt 不重写。
- 到第 3 轮或主链变化时，同时触发 prompt rehydration、goal refresh、工具/线程复查。

模拟结论：

- 新协议可检查到 `round_plan_attention_drift_gap`、`master_prompt_decay_gap` 和 `round_prompt_missing_gap`。
- Runtime Kit 由 `templates/prompt.md` 的 Round Prompt Rehydration、`templates/loop.md` 的 `round_execution_prompt` 和 `templates/state.md` 的 master prompt 字段承接。

## Scenario 1: Plan Mode 完整扫描 Complex

用户提示：

```text
请在 Plan 模式下完整扫描 Complex，再规划本项目。
```

旧风险：

- 模型只读取快速入口或几个熟悉字段。
- 计划只写普通任务步骤，没有覆盖 Complex 的可借鉴组件。

新期望：

- 先按 `protocol_scan_sequence` 读取：项目状态、快速入口、启动提问卡、用户可见触发词、连续节拍、Stage 0-10、能力发现、子代理/线程、Loop/评分、Plan/Goal、交付拆分、Runtime Kit。
- 输出 `user_visible_trigger_guide`，说明“Plan 模式”和“完整扫描”触发的是计划前的协议理解，而不是立即执行；旧称 Plan-only 只是当前环境限制。
- 计划中必须写 `adopt_now`、`skip_now`、`backlog` 和最大误读风险。
- 计划仍必须包含 round_goal、Loop 验证、评分路由和交付契约。

模拟结论：

- 新协议可检查到 `protocol_scan_order_ambiguity_gap` 和 `plan_mode_full_scan_undercoverage_gap`。
- Runtime Kit 由 `templates/state.md` 和 `templates/loop.md` 承接扫描结果与下一轮目标。

## Scenario 2: 连续节拍中的长期分线程和外部工具失配

用户提示：

```text
按 Complex 连续节拍推进，使用多线程和外部工具。
```

旧风险：

- round 1 建过子代理或长期线程，但 round 4 以后主链变化，分线程仍按旧职责输出。
- round 1 选过工具，但后期任务变成渲染、检索、交付或代码验证后，工具组合没有更新。

新期望：

- round 1 建立 `round_index: 1`、`review_interval: 3`、topology_summary 和 capability_summary。
- round 3 或主链变化时触发 `continuous_cadence_refresh_gate`。
- 主线程必须给每个分线程一个结果：keep / adjust / pause / close / replace。
- 能力清单必须给每个工具一个结果：keep / adjust / replace / pause / manual_action / retire。

模拟结论：

- 新协议可检查到 `scheduled_topology_refresh_gap` 和 `scheduled_capability_refresh_gap`。
- `templates/state.md` 已有 topology/capability 复盘字段，`docs/runtime-skill-management.md` 已有每 3 轮刷新规则。

## Scenario 3: Goal 停在旧版本或一轮完成后停止

用户提示：

```text
连续节拍推进这个项目，当前已经从 v32 走到 v38。
```

旧风险：

- active goal 仍写 v32，实际工作已到 v38。
- round_goal 完成后，模型把整个长期目标标成 complete，导致 next_route 没有继续触发。

新期望：

- 每轮开始运行 `goal_refresh_gate`。
- 区分 active_goal、round_goal 和 next_route：active_goal 服务持续会话，round_goal 服务本轮 Loop。
- 若 active_goal 与 current_basis、版本号、next_route 或交付对象不一致，标记 `stale_goal`，迁移到新目标或写 `protocol_round_goal`。
- round_goal 完成只更新本轮，不自动结束 continuous route。

模拟结论：

- 新协议可检查到 `fake_goal_drift_gap`。
- `templates/state.md` 和 `templates/loop.md` 已增加 goal_refresh_status、stale_goal_check、round_goal 和 next refresh trigger。

## Overall Result

本轮修复把用户体验问题转成 11 个可触发机制：

1. `protocol_scan_sequence`
2. `complex_prompt_bootstrap_gate`
3. `round_prompt_rehydration_gate`
4. `continuous_cadence_refresh_gate`
5. `scheduled_topology_capability_review`
6. `goal_refresh_gate`
7. `plan_mode_full_scan_coverage`
8. `complex_setup_question_card`
9. `user_visible_trigger_guide`
10. `core_goal_plan_loop_required`
11. 内部工作力度/风险升级，替代用户侧普通/重大模式选择

这些机制默认不新增 verifier required 字段；它们先作为主协议行为规则、Runtime Kit 模板字段和发布包能力项存在。若后续真实项目继续暴露同类问题，再考虑把其中稳定可检查的字段纳入恢复链验证器。
