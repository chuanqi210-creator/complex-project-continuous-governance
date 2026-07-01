# Prompt Bootstrap Template

Use this file when a user wants the agent to scan Complex, design a project-specific prompt, and execute only after confirmation.

This prompt is an execution contract for one project. It does not replace the Complex protocol, the user's latest instruction, or authorization boundaries.

## Minimal User Request

```text
请帮我扫描 Complex，并对我们的项目设计提示词。之后给出一个可复制的 prompt；我确认后，再根据这个 prompt 结合 Complex 推进项目。
```

## Protocol Scan Summary

- Complex files or sections read:
- Components adopted now:
- Components skipped now:
- Components backlogged:
- Manual actions or permissions needed:
- Biggest misread risk:

## Project Intake

- Project goal:
- Existing materials:
- Current basis:
- Known constraints:
- High-risk or high-rework signals:

## Startup Questions or Defaults

- Delivery audience and format:
- Capability permission:
- Collaboration topology:
- Cadence:
- Evidence, privacy, account, publishing, or manual-action boundary:

## Prompt Design Rationale

- Why this goal needs Complex:
- Why these capabilities are selected or rejected:
- Why this collaboration topology fits:
- Why this cadence fits:
- What the first Loop should test:
- What would trigger route-back:

## Copy-Ready Prompt

```text
请按 Complex 项目持续治理协议推进以下项目。

项目目标：

已有材料：

当前交付对象和交付形式：

能力边界：
- 可用：
- 暂不使用：
- 需要用户授权或人工操作：

协作拓扑：

推进节拍：

目标与计划：
- active_goal（如连续项目需要）：
- round_goal：
- 本轮计划：

Loop 小循环：
- 最大不确定性：
- 5-30 分钟验证动作：
- 通过标准：
- 失败后的 route-back：

评分与动态路由：
- 证据充分性：
- 风险/返工：
- 能力匹配：
- 用户确认需求：
- 下一步路由：

交付契约：
- 人看版：
- 机器恢复记录：
- 不应暴露的内部信息：

请先恢复或建立 state/current_basis，再执行本轮 round_goal。每轮结束时留下 next_route；如果启用连续节拍，每 3 轮复查工具、子代理/线程职责和 goal 是否过期。
```

## Execution Bridge

- User confirmation status:
- First round_goal after confirmation:
- First Loop:
- First verification:
- First next_route:

## Round Prompt Rehydration

Use this section at the start of each continuous round, Plan-mode continuation, or `next_route` handoff.

- round_index:
- master_prompt_location:
- active_goal_summary:
- latest state/current_basis:
- inherited master constraints:
- previous-round status:
- new round judgment:
- prompt patch from user details:
- round_execution_prompt:
- plan_alignment_to_master_prompt:
- next_route this prompt should preserve:

Rules:

- Compress and inherit the confirmed master prompt; do not rewrite it unless the user explicitly changes the main goal.
- Treat user detail changes as prompt patches by default.
- Generate the Plan and Loop from `round_execution_prompt`, not from the local task alone.
- If the round prompt cannot be reconstructed, route back to state recovery before execution.
