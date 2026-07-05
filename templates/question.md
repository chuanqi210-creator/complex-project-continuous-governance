# Question Template

Use this file to avoid asking the user low-value questions. Ask only when the answer changes direction, evidence threshold, delivery form, permissions, or high-cost execution.

## Complex Setup Question Card

Use `complex_setup_question_card` when a project starts with "use Complex", "按 Complex 推进", "读取 Complex", or a similar request and the important operating choices are not yet explicit.

Ask briefly, or state safe defaults if the task is low risk:

- Delivery: Who is the output for, and is it human-readable, machine-recovery, teacher/expert-facing, third-party-facing, or mixed?
- Capabilities: May the agent use web, browser, databases, accounts, APIs, skills, plugins, or external methods? Which create account, payment, external-write, publishing, irreversible, or high-risk responsibility boundaries?
- Collaboration: For continuous projects, the agent should choose the standing-lane topology and temporary-worker fit unless that choice creates a real platform side effect. If a preference matters, which standing lanes should exist first?
- Cadence: Should this be one beat with a clear next route, or continuous cadence until the user stops it?
- Portfolio: If this is a long project with multiple modules, sources, lanes, or deliverables, the agent should form the operating organization itself: target function, controller lane, human interface lane, literature/data lane, model/component lane, data-code lane, review/risk lane, writing/delivery lane, forward indexes, branch parking, and Hot/Warm/Cold state.
- Calibration: If the next decision changes strategy, model, method, evaluation, or protocol defaults, the agent should run an external calibration pass or reuse a fresh calibration note before execution.
- Project nature: Is the model, formula, research frame, or evidence table already fixed, or should the agent first protect divergent model discovery?
- Autonomy: Should the agent use "strong autonomy + guardrails" for reversible project details, or ask before each strategic adjustment?
- Boundaries: Are there privacy, payment, publishing, account, evidence, or real-world action limits?

Safe default if unanswered:

- Main thread first.
- One beat first, then leave `next_route`.
- Read-only local and public sources only.
- No external account, payment, publishing, or irreversible action.
- Strong autonomy inside the responsibility boundary: the agent may decide project-internal plan details, Plan/Goal fit, runtime topology, thread/worktree/automation fit, resource fit, state compaction, and next-beat routing, but must ask before goal changes, account/API credentials, payment, external writes, irreversible actions, delivery-public-voice changes, high-risk claims, or platform actions that create user-owned external commitments.
- Human-readable delivery that a third party can understand.

User-visible trigger guide:

> You can say these steering words to guide the agent: "开启 Plan 模式 / 先规划再执行", "模型发现型 / 先发散研究框架 / 不要早收敛", "证据填充型 / 模型和指标已定", "连续节拍 / 总规划别丢 / 每拍 prompt 重水化", "Codex Goal 是 thread_goal 或 phase_goal / beat_objective 属于每拍 Plan", "自动进入下一拍 / 不等我说继续", "模块组合 / 串并联系统 / 不要局部贪心", "forward artifact / 审计只是护栏 / Hot State", "外部优秀案例 / external calibration / micro-contract", "定期 hallucination sentinel", "standing lane 和 subagent 分开 / 每轮清上下文", "少问我 / 能推进就继续 / 我给目录你自己读", "运行资源 AI 自判 / 用户只担责授权", "独立评审 / 客观审查 / 避免上下文污染", "外部工具 / 账号 / API / skill", "目标仓库边界对账 / 真人工边界 / 剩余可自动小拍", "编排预检 / thread_goal / phase_goal / standing lane / automation / Beat Router / stop condition", and "只要人看版".
> You can also say "先设计提示词/prompt", "多线程/子代理", "完整扫描 Complex", or "先做问题-观点-论据图" when those operating choices matter.
> You can also say "强自治+护栏", "让 AI 自行判断细节", "动态推进", "只在高风险时问我", or "AI 自己调路线，但保留理由" when you want the agent to handle route, depth, tool, and collaboration details unless a real boundary is crossed.
> In continuous cadence, a clear queued `next_route` should auto-execute when it stays inside the responsibility boundary. The agent should not ask the user to say "continue" unless a real responsibility, account/API, payment, external-write, irreversible-action, publishing, high-risk, turn, or tool boundary exists. Continuous cadence also means per-beat `beat_objective`, prompt rehydration, and automatic start of the next queued beat when allowed.
> Independent review means context separation every review beat. If clean context, a read-only audit lane, or a fact-ledger-only packet is unavailable, label the result as same-session diagnostic review instead of independent review.
> In downstream repositories, steering words must be reconciled with local project boundaries. A true external-input/manual-action gate blocks only unsafe or impossible work; the agent should still run allowed residual beats before pausing.
> Plan mode is a planning surface. At complex or strategic beats, planning checkpoint is mandatory and is executed by the agent using its recommended route. The agent may use an available Plan surface, but if the current surface cannot be toggled by the agent, it must output a planning checkpoint without claiming automatic activation.
> Codex Goal is `thread_goal` or `phase_goal`: persistent objective and completion criteria for a longer task, thread, or bounded phase. AI decides whether the Goal surface should carry that contract; if unavailable, record the same contract in state, prompt, or handoff. Complex `beat_objective` is the per-beat target inside Plan/Loop.
> Plan mode must design an orchestration contract when continuous cadence, Goal mode, user-visible threads, standing lanes, subagents, automation, or independent review are requested. Continuous projects should refresh the control plane before local execution: direction, authority, state, topology, routing, external calibration, hallucination sentinel status, trace appraisal, and stop conditions. The topology includes manager thread, controller lane, human interface lane, literature/data lane, model/component lane, data-code lane, review/risk lane, writing/delivery lane, temporary worker pool, context reset policy, and wake triggers. Subagents are short-lived workers; user-visible Codex threads and automations are different resources with different platform boundaries. Choosing the topology is AI work; asking the user is for responsibility-bearing actions.
> Continuous projects with multiple modules or sources should maintain a portfolio operating model. A beat is not accepted merely because guards pass; it should create or update a forward artifact, update state/indexes, and choose the next route. Repeated guard-only beats trigger toil/WIP review: create an artifact, park the branch, route to another module, or justify why the guardrail is the true dependency.
> Long projects should keep traces recoverable but not hot forever: Hot State for the current map, Warm Index for compact ledgers, Cold Archive for raw trace and old branches. Strategic choices and every mechanism-level issue should check external mature practice, record adopted/rejected/not-transferable lessons, turn the lesson into a micro-contract, and run a hallucination sentinel before becoming durable rules.
> When scanning Complex from another project, use the installed Complex runtime (`COMPLEX_HOME` or a user-provided path) as the rule source, and use the target repository as the fact source.

## Complex Prompt Bootstrap Card

Use `complex_prompt_bootstrap_gate` when the user wants to scan Complex first, design a project prompt, and only then execute the project.

Ask briefly, or state safe defaults if the task is low risk:

- Project: What is the project goal, and what material should the prompt assume exists?
- Execution: Should the generated prompt be used in this thread after confirmation, or copied into a new project/thread?
- Plan mode: If the current interface supports Plan mode and the agent can use it, use that planning surface for protocol scan, prompt design, and plan generation before execution; if it is not enabled or not controllable from this surface, produce a plan-shaped plan instead of claiming automatic activation.
- Cadence: Should the prompt default to one beat with `next_route`, or continuous cadence with scheduled refresh?
- Project nature: Should the prompt treat this as evidence filling, model discovery, mixed discovery-to-evidence, or execution delivery?
- Steering words: Which of these should be preserved in the generated prompt: model discovery, evidence fill, continuous cadence, fewer questions, independent review, external tools, human-readable only?
- Capabilities: Which tools, browser paths, accounts, APIs, skills, plugins, or subagents may the prompt use, and which cross account, external-write, irreversible, publishing, or high-risk responsibility boundaries?
- Autonomy: Should the prompt default to strong autonomy with guardrails, and which decisions must still ask the user?
- Delivery: Who will read the result, and should the prompt enforce human-readable, machine-recovery, teacher/expert-facing, third-party-facing, or mixed delivery?

Safe default if unanswered:

- Design only first; do not execute until the user confirms.
- Main thread first, one beat first, then leave `next_route`.
- Read-only local and public sources only.
- No account, API write, payment, publishing, or irreversible action.
- Strong autonomy + guardrails for reversible project details and runtime topology; ask before goal, account/API, external-write, irreversible, delivery-public-voice, or high-risk-claim changes.
- Human-readable delivery that a third party can understand.

Required output before execution:

- `protocol_scan_summary`
- `startup_questions_or_defaults`
- `project_prompt_design_rationale`
- `copy_ready_prompt`
- `execution_bridge`

## Question Candidate

- Question:
- Why it matters:
- What happens if unanswered:
- Maximum rework risk:

## Type

- Goal or scope:
- Evidence standard:
- Tool or account permission:
- Collaboration structure:
- Delivery audience:
- Style or granularity:
- External action or irreversible cost:

## Recommended Default

- Default if user does not answer:
- Why this default is safe:
- What will be recorded as an assumption:

## Final Asked Question

Ask one concise question:

>

## Answer and Plan Patch

- User answer:
- Plan patch:
- Main goal changed: yes / no
