# Complex Usage Friction Fix 2026-07-01

本轮来源：用户在其他项目中使用 Complex 时反馈，模型仍会漏读协议、连续节拍中不复盘长期分工和外部工具、Plan 模式没有完整吸收 Complex、Goal 模式出现粗糙目标或旧版本目标漂移。

## 修复判断

这些问题不是“Complex 没有相关思想”，而是缺少更明确的运行触发和固定复盘节拍。尤其是连续节拍中，初始选择的子代理、长期线程、工具和 Goal 很容易随着项目阶段变化而过期。

## 写回内容

- 主协议新增 Complex 读取顺序与关键词触发表。
- 连续任务节拍新增 `continuous_cadence_refresh_gate`，默认每 3 轮复盘拓扑、能力和 Goal。
- `capability_discovery_cadence_gate` 增加连续节拍周期性能力复盘。
- `persistent_thread_orchestration_contract` 增加长期线程职责复核。
- `protocol_onboarding_comprehension_gate` 增加 Plan 模式完整扫描要求。
- 新增 `goal_refresh_gate`，区分 active_goal、round_goal 和 next_route。
- 失败模式库新增 protocol scan、scheduled topology/capability refresh、Plan full scan undercoverage 和 fake goal drift。
- Runtime Kit 状态与 Loop 模板增加 round_index、review_interval、topology/capability/goal refresh 字段。
- 发布包同步新增相关能力项。

## 本轮不做

- 不新增 verifier required 字段。
- 不新开长期机器看版。
- 不把每 3 轮复盘变成用户负担；它应由 AI 在机器状态或短说明里维护。

## 验证

模拟记录见 `docs/complex_runtime_cadence_simulation_20260701.md`。
