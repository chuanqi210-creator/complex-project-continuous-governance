# Question Template

Complex uses questions to cross a responsibility boundary or resolve a high-leverage ambiguity. It does not ask the user to choose internal planning, topology, tools, state compaction, or the next executable route.

## Framework Grilling

Use this at project start or a strategic reframe only when the top-level design still contains a material user-owned decision fork. It adapts the high-star `mattpocock/skills` Grill Me pattern without importing its assumption that every design decision belongs to the human.

Before asking:

1. inspect repository facts, accepted state, and relevant external basis;
2. map the candidate decision forks;
3. remove derivable facts, reversible internal choices, and questions answerable by a bounded probe;
4. run the question value test below.

A question passes the **question value test** only when all are true. A derivable fact or an **AI-owned decision** does not qualify:

- two plausible answers materially change the Goal, target function, architecture, responsibility boundary, or evaluation;
- the answer is not available from the repository, files, links, tools, or a bounded experiment;
- the choice belongs to the user or is an undelegated value judgment;
- deciding late would cause substantial rework or invalidate the route.

Ask one question at a time. Include:

- the decision fork;
- the recommended answer and confidence;
- evidence and assumptions;
- the strongest alternative;
- what changes under each answer.

Stop when the remaining uncertainty is derivable, reversible, or testable. Produce a **Framework Decision Contract** containing accepted decisions, rejected alternatives, unresolved empirical questions, and the trigger for reopening the framework. If no question passes, record `no_grill_needed` and continue.

## Startup Defaults

When the user asks to use Complex, infer what is already clear and state the few consequential defaults:

- finish the current request or continue the selected cadence without asking for a generic "continue";
- classify the project as evidence fill, model discovery, mixed, or execution delivery;
- use strong autonomy for project-internal decisions;
- discover tools and Codex resources just in time;
- use a clean reviewer when independence matters;
- add standing lanes or portfolio control only for recurring responsibility or multiple modules;
- deliver a third-party-readable human version unless another audience is specified.

Ask only when the answer cannot be inferred and changes one of these:

- main Goal or public voice;
- credentials, accounts, payment, publishing, or external writes;
- irreversible shared-state change or high-impact external commitment;
- an undelegated human value judgment;
- evidence or material the agent cannot access by any allowed route.

## User-Visible Steering Words

Useful choices include:

- `先规划再执行`
- `先做顶层框架质询 / grill me 大框架`
- `模型发现型 / 不要早收敛`
- `证据填充型 / 模型和指标已定`
- `连续节拍 / 自动进入下一拍`
- `总规划别丢 / 每拍重水化`
- `多模块组合 / 不要局部贪心`
- `独立评审 / 清上下文`
- `外部优秀案例 / 可逆 micro-contract`
- `少问我 / 能推进就继续`
- `外部工具 / 账号 / API / skill`
- `只要人看版`

These steer runtime choices; they do not redefine Codex platform APIs.

## Planning And Continuation

- Plan mode is a Codex surface. At a complex or strategic checkpoint, use it when the surface allows; otherwise produce the same planning checkpoint without claiming the UI changed.
- Codex Goal carries a durable thread or phase objective. The current beat stays in `beat_objective`.
- A clear queued `next_route` continues inside the responsibility boundary. A new user message is not an execution prerequisite.
- Platform threads, worktrees, automations, and subagents are chosen from actual tool support and task shape. Their fit is an AI decision; credentials or external commitments remain human responsibility.

## Prompt Design Request

When the user explicitly asks to scan Complex and design a project prompt first, return:

- protocol and project facts actually inspected;
- project nature and responsibility boundary;
- stable Project Prompt Contract;
- current Beat Planning Packet;
- copy-ready project prompt;
- execution bridge and first completion predicate.

Do not copy the full Complex protocol into the prompt. Reference the installed skill and include only project-specific contracts.

## Question Record

- question:
- responsibility_or_ambiguity_it_resolves:
- why_the_agent_cannot_safely_infer_it:
- exact_user_action_or_answer_needed:
- work_that_continues_without_the_answer:
- default_if_unanswered:
- state_or_plan_patch_after_answer:

## Framework Decision Contract

- framework_goal_and_primary_beneficiary:
- target_function:
- success_and_failure_definition:
- accepted_framework_decisions:
- rejected_alternatives_and_reason:
- unresolved_empirical_questions:
- delegated_ai_decisions:
- responsibility_boundary:
- evaluation_frame:
- reopen_trigger:
- derived_project_prompt_contract:
