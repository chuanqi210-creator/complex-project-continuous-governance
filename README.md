# complex-project-continuous-governance

Complex is a Codex-native orchestration skill and runtime kit for long-running complex projects.

It helps an agent keep a project moving through:

**strong-autonomy execution inside a responsibility boundary + Codex surface alignment + portfolio control-plane orchestration + external calibration + evidence boundaries + clean review + lightweight auditable recovery.**

Install Complex once, then use it from any target project through `COMPLEX_HOME` or an explicit path.

## 30-Second Install

```bash
mkdir -p ~/Documents
git clone https://github.com/chuanqi210-creator/complex-project-continuous-governance.git \
  ~/Documents/complex-project-front-governance
cd ~/Documents/complex-project-front-governance
python3 tools/check_behavior_regression_pack.py
python3 tools/review_behavior_transcript.py --validate-rules
python3 tools/test_verify_complex_integrity.py
python3 tools/verify_complex_integrity.py
```

Optional shell setup:

```bash
export COMPLEX_HOME="$HOME/Documents/complex-project-front-governance"
```

Update:

```bash
cd "${COMPLEX_HOME:-$HOME/Documents/complex-project-front-governance}"
git pull --ff-only
python3 tools/verify_complex_integrity.py
```

## Start A Project

Use this when you want the agent to design a project prompt before execution:

```text
请帮我扫描 Complex，并对我们的项目设计提示词。之后给出一个可复制的 prompt；我确认后，再根据这个 prompt 结合 Complex 推进项目。

请显式采用这些 steering words，并按项目实际情况取舍：
开启 Plan 模式 / 先规划再执行；模型发现型 / 先发散研究框架 / 不要早收敛；证据填充型 / 模型和指标已定；连续节拍 / 总规划别丢 / 每拍 prompt 重水化；Codex Goal 是 thread_goal 或 phase_goal / beat_objective 属于每拍 Plan；自动进入下一拍 / 不等我说继续；模块组合 / 串并联系统 / 不要局部贪心；forward artifact / 审计只是护栏 / Hot State；外部优秀案例 / external calibration / micro-contract；定期 hallucination sentinel；少问我 / 能推进就继续 / 我给目录你自己读；运行资源 AI 自判 / 用户只担责授权；standing lane 和 subagent 分开 / 每轮清上下文；独立评审 / 客观审查 / 避免上下文污染；外部工具 / 账号 / API / skill；只要人看版。

如果当前界面支持 Plan 模式，请使用可用的规划 surface；如果当前界面不能由你实际切换，也请直接输出 planning checkpoint，不要伪称已经自动开启。关键节拍由 AI 自行做 plan-shaped planning，不把规划本身变成向我索要授权。
```

Use this when you want execution to begin after the plan is clear:

```text
这个项目按 Complex 推进。
目标是：……
已有材料在：……
交付对象是：……

采用强自治+担责边界：项目内部的计划细节、读取、验证、运行拓扑、Plan/Goal 适配、standing lane 记录、thread/worktree/automation fit、临时 worker fit、状态压缩和下一拍推进由 AI 自行判断；只有主目标、账号/API、付款、外部写入、发布、不可逆动作、公开口径、高风险主张，或平台动作会造成我需要担责的外部承诺时再问我。

先建立 thread_goal 或 phase_goal，再用每拍 beat_objective 执行。连续节拍启动后，每拍做 prompt 重水化、planning checkpoint、target-function Loop、Beat Router、forward artifact 验收和 next_route；可继续时自动进入下一拍，直到 STOP_COMPLETE 或真实担责边界。
```

## Codex Surface Map

Complex deliberately maps its rules onto Codex surfaces:

- **Plan mode** is a user/interface planning surface. Complex cannot claim it automatically enabled Plan mode unless the current surface actually exposes that action. For complex or strategic beats, AI decides that a **planning checkpoint** is required and continues within the responsibility boundary.
- **Codex Goal** is a persistent objective and completion criteria for a longer task, thread, or bounded phase. Complex names this `thread_goal` or `phase_goal`. AI decides whether the Goal surface should carry the phase contract; if it cannot be set from the current surface, record the same contract in state, prompt, or handoff and continue.
- **`beat_objective`** is the current small execution target inside the Plan/Loop layer.
- **`goal_memory_summary`** is recovery context, not Codex Goal.
- **Continuous cadence** means same-run execution of queued beats inside the responsibility boundary until `STOP_COMPLETE` or a true boundary.
- **Subagents** are short-lived workers for bounded parallel work. They are not standing lanes.
- **Standing lanes** are durable manager-owned responsibilities: controller, human interface, literature/data acquisition, model/component, data-code, review/risk, writing/delivery.
- **User-visible threads, worktrees, and automations** are platform resources, not responsibility boundaries by default. AI decides whether they fit the operating organization; actual creation follows the current Codex surface/tool semantics. If the surface cannot create them in this run, record the contract and continue.
- **AGENTS.md** carries durable repo conventions. **Skills** carry reusable workflows. **MCP/tools/connectors** carry live capabilities.

## How Complex Works

Complex starts from seven stable behaviors:

1. Restore the true current state.
2. Classify project nature: `evidence_fill`, `model_discovery`, `mixed`, or `execution_delivery`.
3. Assign decision rights through a responsibility boundary.
4. Establish the control plane and operating organization before local optimization.
5. Run the smallest meaningful target-function Loop or execution beat.
6. Deliver to the right audience.
7. Leave `next_route`, accepted artifacts, and recovery pointers.

For continuous projects, the control plane comes before local edits:

- direction: `thread_goal` / `phase_goal`, `goal_memory_summary`, project nature, convergence, delivery contract, stop condition;
- authority: responsibility boundary, manual-action records, external-write boundaries;
- state: current basis, not-current basis, beat queue, risks, validation status;
- topology: manager, standing lanes, temporary workers, heartbeat/automation fit;
- routing: Beat Router, residual scan, branch parking, recovery route;
- calibration: external reference coverage, hallucination sentinel, trace appraisal.

The operating organization keeps recurring work from collapsing into a single local path:

- Controller lane: project direction and route.
- Human interface lane: responsibility-bearing asks and explanations.
- Literature/data acquisition lane: papers, official sources, databases, account forecasts.
- Model/component lane: model structure, variables, component interfaces.
- Data-code lane: schema, scripts, hashes, reproducibility.
- Review/risk lane: clean-context review and overclaim control.
- Writing/delivery lane: claims, figures, methods, reader-facing output.

A beat is accepted when it creates or updates a forward artifact, passes the relevant guard, updates an index or state, and chooses the next route. Audit, citation, QA, access checks, and "still closed" notes are guardrails; repeated guardrail-only work triggers a toil/WIP review instead of becoming the project engine.

Important route, structure, model, method, evaluation, prompt-default, or protocol changes require external calibration. The agent compares the choice with official docs, primary papers, standards, or mature production writeups; records adopted / rejected / not transferable lessons; then turns the adopted lesson into a project micro-contract.

Complex keeps traceability lightweight:

- **Hot State**: one-page current map.
- **Warm Index**: compact ledgers and accepted artifacts.
- **Cold Archive**: raw evidence, old gates, source notes, command output, screenshots, and superseded branches by pointer.

`STOP_COMPLETE` requires objective completion, delivery-level validation, and a residual scan showing no useful internal beat remains. A fixed number of beats is never enough by itself.

## Runtime Kit

Current entrypoints:

- Core protocol: `protocol/core.md`
- Current state: `protocol/current-state.md`
- Quickstart: `docs/quickstart.md`
- Runtime templates: `templates/`
- Filled examples: `docs/examples/`
- Behavior cases: `docs/behavior-regression-cases.json`
- Transcript rules: `docs/behavior-transcript-review-rules.json`
- Behavior review: `docs/behavior-review.md`
- Capability guide: `docs/runtime-skill-management.md`
- External method mapping: `docs/external-methods.md`
- Codex repo skill: `.agents/skills/complex-runtime/SKILL.md`

Use filled examples before blank templates:

- `docs/examples/evidence_fill_minimal_runtime/`
- `docs/examples/model_discovery_minimal_runtime/`
- `docs/examples/independent_review_minimal_runtime/`
- `docs/examples/portfolio_orchestration_minimal_runtime/`
- `docs/examples/external_calibration_micro_contract_runtime/`
- `docs/examples/operating_organization_multi_lane_runtime/`

Templates are optional landing pads, not mandatory machine fields.

## Verification

Run these after protocol, template, behavior-pack, skill, or site changes:

```bash
python3 tools/check_behavior_regression_pack.py
python3 tools/review_behavior_transcript.py --validate-rules
python3 tools/test_verify_complex_integrity.py
python3 tools/verify_complex_integrity.py
pnpm -C docs/protocol_explainer_site build
```

Expected baseline:

- behavior pack: 34 cases and 34 transcript rules
- integrity verifier: `failure_count: 0`
- site build: Vite build succeeds

## Repository Shape

- `protocol/`: current protocol and state only.
- `docs/`: quickstart, examples, behavior review, external method mapping, and explainer site source.
- `templates/`: optional runtime records for downstream projects.
- `.agents/skills/`: Codex repo-scoped skills.
- `.codex/`: capability candidates and Complex repository metadata.
- `tools/`: lightweight structural and behavior-review checks.

Do not add history archives, migration records, rendered outputs, or long machine-board logs back into the active tree. If old context is needed, use Git history.
