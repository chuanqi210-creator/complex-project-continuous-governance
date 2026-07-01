# Complex Runtime Cadence Simulation 2026-07-01

用途：用小模拟验证本轮修复是否覆盖用户在其他项目使用 Complex 时遇到的三类摩擦：完整扫描不足、连续节拍中拓扑/工具不复盘、Goal 漂移或完成后自动停止。

本记录不是新的长期机器看版，不改变当前恢复入口；它只作为本轮协议修复的小题证据。

## Scenario 1: Plan Mode 完整扫描 Complex

用户提示：

```text
请在 Plan 模式下完整扫描 Complex，再规划本项目。
```

旧风险：

- 模型只读取快速入口或几个熟悉字段。
- 计划只写普通任务步骤，没有覆盖 Complex 的可借鉴组件。

新期望：

- 先按 `protocol_scan_sequence` 读取：项目状态、快速入口、连续节拍、Stage 0-10、能力发现、子代理/线程、Loop/评分、Plan/Goal、交付拆分、Runtime Kit。
- 输出 `keyword_trigger_map`，说明“Plan 模式”和“完整扫描”触发的是计划前的协议理解，而不是立即执行。
- 计划中必须写 `adopt_now`、`skip_now`、`backlog` 和最大误读风险。

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

本轮修复把用户体验问题转成 5 个可触发机制：

1. `protocol_scan_sequence`
2. `continuous_cadence_refresh_gate`
3. `scheduled_topology_capability_review`
4. `goal_refresh_gate`
5. `plan_mode_full_scan_coverage`

这些机制默认不新增 verifier required 字段；它们先作为主协议行为规则、Runtime Kit 模板字段和发布包能力项存在。若后续真实项目继续暴露同类问题，再考虑把其中稳定可检查的字段纳入恢复链验证器。
