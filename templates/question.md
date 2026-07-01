# Question Template

Use this file to avoid asking the user low-value questions. Ask only when the answer changes direction, evidence threshold, delivery form, permissions, or high-cost execution.

## Complex Setup Question Card

Use `complex_setup_question_card` when a project starts with "use Complex", "按 Complex 推进", "读取 Complex", or a similar request and the important operating choices are not yet explicit.

Ask briefly, or state safe defaults if the task is low risk:

- Delivery: Who is the output for, and is it human-readable, machine-recovery, teacher/expert-facing, third-party-facing, or mixed?
- Capabilities: May the agent use web, browser, databases, accounts, APIs, skills, plugins, or external methods? Which require explicit authorization?
- Collaboration: Should the main thread handle this first, or should subagents, parallel checks, or long-running threads be considered?
- Cadence: Should this be one round with a clear next route, or continuous cadence until the user stops it?
- Boundaries: Are there privacy, payment, publishing, account, evidence, or real-world action limits?

Safe default if unanswered:

- Main thread first.
- One round first, then leave `next_route`.
- Read-only local and public sources only.
- No external account, payment, publishing, or irreversible action.
- Human-readable delivery that a third party can understand.

User-visible trigger guide:

> You can say "先设计提示词/prompt", "连续节拍", "多线程/子代理", "外部工具/账号/API", "完整扫描 Complex", or "只要人看版" to change how the project is run.

## Complex Prompt Bootstrap Card

Use `complex_prompt_bootstrap_gate` when the user wants to scan Complex first, design a project prompt, and only then execute the project.

Ask briefly, or state safe defaults if the task is low risk:

- Project: What is the project goal, and what material should the prompt assume exists?
- Execution: Should the generated prompt be used in this thread after confirmation, or copied into a new project/thread?
- Cadence: Should the prompt default to one round with `next_route`, or continuous cadence with scheduled refresh?
- Capabilities: Which tools, browser paths, accounts, APIs, skills, plugins, or subagents may the prompt authorize or only list as candidates?
- Delivery: Who will read the result, and should the prompt enforce human-readable, machine-recovery, teacher/expert-facing, third-party-facing, or mixed delivery?

Safe default if unanswered:

- Design only first; do not execute until the user confirms.
- Main thread first, one round first, then leave `next_route`.
- Read-only local and public sources only.
- No account, API write, payment, publishing, or irreversible action.
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
