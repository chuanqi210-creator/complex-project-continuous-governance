# complex-project-continuous-governance

这是从 `/Users/chuchenqidawang/Documents/ai 科研` 拆出并独立化后的 **Complex 项目持续治理协议** 项目。本仓库现在是当前权威工作区，旧 `ai 科研` 目录只作为历史来源。

本项目名称从 “front governance / 启动前置治理” 调整为 “continuous governance / 持续治理”，因为协议已经不只覆盖复杂项目启动前的目标和证据对齐，也覆盖持续推进中的动态路由、Loop 小闭环、评分迭代、协作拓扑、恢复链和交付边界。

## 当前版本状态

- 当前主协议：`protocol/Complex项目持续治理协议_v3_核心版.md`
- 当前低摩擦入口：`protocol/Complex项目持续治理_低摩擦用户入口_20260622.md`
- 当前恢复入口：`protocol/持续治理协议_二十个跨渠道项目逆向校验实验.md` 的 `## 220. 当前机器看版`
- 当前 next route：`continue_self_optimization_with_skill_adoption_expansion_or_stop`
- 最近一次整合：仓库独立化、历史回归迁移、恢复链第 215-220 轮、外部 skill 采用扩展、新能源汽车项目复盘后的人看版交付/注意力绑定规则、Runtime Kit 运行模板，以及 `complex_prompt_bootstrap_gate` 提示词设计前置流程。
- GitHub 同步策略：本仓库保留当前权威协议和 Runtime Kit；公开说明、可视化站点、模板和 reusable protocol package 均从该工作区同步。

## 项目目标

- 把复杂项目的目标对齐、证据分层、能力发现、动态路由、Loop 小闭环、评分迭代、协作拓扑、恢复链和交付边界放在一个小而清楚的项目里。
- 让 Codex 可以围绕该协议单独开工作树、持续迭代、测试和发布。
- 提供 Complex Runtime Kit / 持续治理运行时套件，让新项目能直接建立状态、证据、决策、检索、提问、提示词、Loop 和交付记录。
- 避免继续依赖或修改 `ai 科研` 大目录。

## 三层结构

1. `protocol/`：Complex 持续治理核心规则，决定项目如何恢复、路由、评分、协作和交付。
2. `templates/`：Runtime Kit 运行模板，帮助新项目快速建立 state、evidence、decision、search、question、prompt、loop 和 delivery 记录。
3. `.codex/`：项目级能力发现入口，记录推荐能力候选和项目本地 skill 放置规则；它不替代实际环境中的工具探测。

## 目录

- `.codex/shared-skills.json`：项目级能力候选清单，用于启动能力盘点，不声称所有能力当前可调用。
- `.codex/skills/`：项目本地 skill 放置区；当前仅保留说明，未来新增 skill 必须绑定真实项目缺口和小题验证。
- `protocol/`：协议核心文档、v3 主协议、低摩擦入口、发布包、自测记录、经验库索引。
- `protocol/Complex项目持续治理协议_v3_核心版.md`：当前权威主协议。
- `templates/`：Runtime Kit 轻量模板，供新项目复制或引用。
- `templates/prompt.md`：提示词设计前置模板，用于先扫描 Complex、设计项目专用执行 prompt、确认后再推进。
- `docs/runtime-skill-management.md`：运行时 skill / tool / plugin / API / 外部方法选择、拒绝、试用和写回规则。
- `docs/history/`：从旧目录同步来的历史回归记录、真实项目小题和治理样例。
- `docs/migration/`：独立化迁移清单和路径说明。
- `docs/Complex协议复盘与优化人看版_20260629.md`：新能源汽车项目作为例子的 Complex 协议人看版复盘。
- `docs/protocol_explainer_site/`：协议解释站点源码。
- `outputs/front_governance_protocol_v2/`：v2 版本 Markdown、DOCX、PDF 和渲染页。
- `tools/`：恢复链、链接扫描等辅助工具。
- `docs/`：后续新增说明和设计笔记。

## 使用说明

### 推荐最小入口

新项目最省心的用法，是先让 Complex 设计项目专用提示词，再确认执行：

```text
请帮我扫描 Complex，并对我们的项目设计提示词。之后给出一个可复制的 prompt；我确认后，再根据这个 prompt 结合 Complex 推进项目。
```

AI 应先触发 `complex_prompt_bootstrap_gate`，完成协议扫描、启动问题或安全默认、项目专用 `copy_ready_prompt` 和 `execution_bridge`。用户确认前不应进入业务执行、发布、提交外部系统或把 prompt 当成已授权操作。

### 直接推进入口

如果已经知道项目目标，也可以直接说：

```text
这个项目按 Complex 推进。
目标是：……
已有材料在：……
我希望结果达到：……
```

AI 应先用 `complex_setup_question_card` 确认或默认交付对象、外部能力权限、子代理/多线程、连续节拍和人工边界。用户不需要区分普通项目和重大项目；高风险、高返工或高公共性的工作只会触发内部工作力度/风险升级。

### 可选触发词

新用户不需要猜隐藏口令。可以直接说：

- `完整扫描 Complex`：先做协议理解，再给业务计划。
- `先设计提示词/prompt`：先生成项目专用执行 prompt，确认后再推进。
- `连续节拍`：每轮都有 `round_goal`、Loop、评分路由和 `next_route`；默认每 3 轮复查工具、子代理/线程职责和 goal 是否过期。
- `多线程/子代理`：先判断主线程、临时子代理或长期线程哪种拓扑合适，再执行。
- `外部工具/账号/API`：先建立能力候选清单，写清 selected / rejected / backlog / manual action。
- `只要人看版`：交付以第三方也能读懂的人看版为主，机器恢复记录另行保留或压缩。

### Runtime Kit 落地方式

需要让新项目可恢复时，复制或引用 `templates/` 中的轻量模板：

- `state.md`：当前状态、用户选择、goal、拓扑和能力刷新。
- `evidence.md`：证据层级、缺口和可声明边界。
- `decision.md`：关键取舍、拒绝路线和重评条件。
- `search.md`：资料检索、获取升级、账号/权限/用户协助边界。
- `question.md`：启动提问卡和高杠杆确认问题。
- `prompt.md`：先扫描 Complex、设计项目 prompt、确认后执行。
- `loop.md`：5-30 分钟小循环、评分和 route-back/execute 判断。
- `delivery.md`：人看版、机器恢复版、老师/专家/第三方版本的交付契约。

### 维护者工作流

1. 改协议前先看 `protocol/持续治理协议发布包_20260622.md`。
2. 涉及历史恢复链时看 `protocol/持续优化变更清单_20260622.md`。
3. 新项目要求读取 Complex 或 Auto Research 时，先理解低摩擦入口、启动提问卡、阶段流程、动态路由、能力发现、子代理/线程、Goal/Plan/Loop、评分和交付拆分规则，再开始业务执行。
4. 修改后运行工具或结构检查，记录结果。
5. 需要并行探索时，从本项目创建 worktree，而不是从原 `ai 科研` 大目录创建。

## 验证命令

协议或恢复链修改后，优先运行：

```bash
python3 tools/test_verify_governance_recovery.py
python3 tools/verify_governance_recovery.py --preset continuous-self-optimization --latest-heading '## 220. 当前机器看版' --expected-route continue_self_optimization_with_skill_adoption_expansion_or_stop
```

当前基线要求上述两条命令分别返回 `ok` 和 `failure_count: 0`。

## 来源

本项目源自 `/Users/chuchenqidawang/Documents/ai 科研`，相关历史记录已同步到 `docs/history/`。后续协议维护、验证和恢复默认只使用本仓库。
