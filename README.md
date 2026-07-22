# complex-project-continuous-governance

Complex is a Codex-native runtime for long-running complex projects.

It combines a stable seven-behavior execution spine with four coupled engineering layers:

| Layer | Contract |
| --- | --- |
| Prompt Contract | Goal, completion criteria, responsibility boundary, and output contract |
| Context Working Set | the smallest sufficient, current, attributable context for the next judgment |
| Runtime Harness | tools, environment, policies, observability, checkpoints, and recovery |
| Progress Loop | act, observe, evaluate, route, retry, rollback, or stop from outcomes |

The layers are not a linear sequence and not four new gates. Complex diagnoses which layer failed before changing prompts, context, tools, or continuation logic.

Long projects also define time convergence: a project-specific time appetite, the next stage result horizon, and a usable stage artifact. When the intended scope does not fit the observed pace, Complex preserves quality and converges scope or route rather than polishing indefinitely or pretending an expired timebox means completion.

Complex is organized as one small runtime kernel, two universal boundaries, supporting practices, and conditional extensions. Architecture role is separate from empirical evidence: `core` means a rule is universally normative, while `screened`, `tested`, and `validated` describe what outcome evidence exists. External projects are inspected as pinned reference implementations, not borrowed as slogans. Examples illustrate, checkers screen, fixed-version fixtures reproduce, locked runs compare, and repeated real Complex outcomes validate.

Current evidence baseline: three core mechanisms and four supporting practices are `tested`; four conditional extensions remain `screened`; none is `validated`. The current seven-mechanism writable suite completed 84/84 valid synthetic trials with no terminal error, but baseline and candidate both reached the environment scorer ceiling. This shows bounded contract executability, not superiority, trajectory quality, human preference, or real-project benefit.

## Install

```bash
mkdir -p ~/Documents
git clone https://github.com/chuanqi210-creator/complex-project-continuous-governance.git \
  ~/Documents/complex-project-front-governance
export COMPLEX_HOME="$HOME/Documents/complex-project-front-governance"
mkdir -p "$HOME/.codex/skills"
ln -sfn "$COMPLEX_HOME/.agents/skills/complex-runtime" \
  "$HOME/.codex/skills/complex-runtime"
cd "$COMPLEX_HOME"
python3 tools/verify_complex_integrity.py
test -f "$HOME/.codex/skills/complex-runtime/SKILL.md"
```

Start a new Codex task after installation so skill discovery reloads. If your Codex surface uses a different capability root, select this repository's `.agents/skills` directory through that surface instead of copying protocol files into each target project.

Update with:

```bash
cd "${COMPLEX_HOME:-$HOME/Documents/complex-project-front-governance}"
git pull --ff-only
python3 tools/verify_complex_integrity.py
```

Complex remains a standalone runtime. A target repository does not need its own `Complex` directory. The installed skill is the runtime entry; `protocol/current-state.md` is only for maintaining Complex itself and must not be used as target-project state.

## Start A Project

Copy-ready high-fit request:

```text
请先读取已安装的 Complex，并结合当前项目建立 Project Prompt Contract。请区分稳定目标与动态上下文，把项目性质作为长期先验，并按当前阶段、模块或工作单元重新判断实际路线；明确担责边界、完成标准、评价方法和交付对象。为长期工作定义时间胃口、下一次阶段成果时点、届时必须可用的最小成果及质量和证据底线；如果观察到的进展无法在时间胃口内收敛，就缩减范围、停放外围分支或调整路线，不要无限完善，也不要把时间到期当成完成。

项目开始或发生战略重构时，先做一次顶层框架质询（Framework Grilling）：只追问会实质改变目标函数、主要受益对象、总体架构、担责边界或评价方法的分叉。先自行读取仓库和外部依据；代码库能回答、可逆、可试验或属于 AI 内部决策的问题不要问我。每次只问一个问题，同时给出你的推荐答案、依据、主要备选及不同答案会改变什么；没有合格问题就直接继续。

随后按四层运行：每拍从稳定的 Prompt Contract 和最新状态生成 Beat Planning Packet；组装最小充分、可溯源的 Context Working Set；先定义当前工件契约，再按不确定性、程序稳定性、可并行性和评审独立性选择最小充分工作拓扑；确认 Runtime Harness 的工具、环境、检查点和降级路线；运行以真实结果为完成条件的 Progress Loop。能在担责边界内继续时自动进入下一拍，不等我说继续。

如果项目包含多个模块、仓库、线程、工作流或长期职责，并且它们分别维护状态，请让各边界保留自己的局部权威记录，由总控在恢复、阶段切换、跨边界交接、依赖变化、状态冲突或阶段交付时做跨边界状态对账，更新一份紧凑的全局控制视图。不要每拍复制所有局部账本，也不要按文件最新时间决定真相；局部冲突只阻塞依赖它的路线。

请先诊断问题属于 prompt、context、harness、loop 还是 model limitation，再修改对应层。不要把上下文遗漏、工具故障或停止逻辑问题都修成更长的提示词。重要评审使用清上下文；重要机制判断做外部校准；输出只要人看版。
```

If you want prompt design before execution:

```text
请先扫描 Complex 和当前项目，只设计 Project Prompt Contract、Context Working Set、Runtime Harness 与 Progress Loop 方案，不执行项目。给出可复制 prompt 和第一拍的 planning checkpoint；我确认项目目标后再执行。
```

## How Complex Runs

The seven stable behaviors are:

1. Restore true state and assemble the current working context.
2. Classify project nature as a durable prior, then classify the active phase, module, or work item closely enough to route the current beat.
3. Assign decision rights through a responsibility boundary.
4. Define the current artifact contract, then establish the minimum control, runtime harness, and work topology; add durable organization or portfolio control only when recurrence or multiple modules justify them.
5. Run a bounded target-function Progress Loop that changes an outcome, exposes a decision, or falsifies a route.
6. Deliver to the right audience and evaluate the outcome.
7. Leave `next_route`, accepted artifacts, recovery pointers, and layer diagnosis.

### Framework Grilling

Complex adapts the Grill Me pattern from the high-star [`mattpocock/skills`](https://github.com/mattpocock/skills) project for top-level framework alignment. It does not turn every startup into an interview. Before asking, the agent inspects available facts and removes questions it can answer or test itself. A surviving question must expose a user-owned fork that materially changes the Goal, target function, architecture, responsibility boundary, or evaluation. Questions are asked one at a time with a recommendation and consequence map; the result is a compact Framework Decision Contract. If no such fork exists, Complex records `no_grill_needed` and continues.

### Adaptive work topology

Complex does not impose one fixed multi-agent organization on a whole project. `project_nature` is a durable prior; the current phase, module, or work item determines the next route. Before allocating a thread, subagent, lane, tool, or workflow, Complex defines the local artifact contract: accepted input, operation or decision, expected artifact or route outcome, acceptance, failure recovery, and state write-back.

It then selects the smallest sufficient arrangement: manager-only work, a deterministic Harness, temporary parallel workers, a recurring standing lane, a clean evaluator, or an exact responsibility handoff. Stable repeated judgments may become templates, checkers, tool contracts, or state machines. Repeated mechanical failures caused by changed assumptions route back to discovery or strategic judgment. This keeps domain-specific organizations in their projects while preserving one reusable control logic.

When several durable boundaries maintain their own state, the controller also owns an event-triggered cross-boundary reconciliation checkpoint. Local records remain authoritative for local facts; a compact global control projection carries only the Goal/phase, observed source generations, module and lane status, accepted artifact pointers, dependencies, conflicts, stage horizon, and one global next route. It refreshes at recovery, transitions, handoffs, topology/dependency changes, conflicts, stage delivery, or a project-specific staleness limit, not through a full fan-in on every beat.

### Codex surface map

- Plan mode is a planning surface. Use it when the desired outcome, constraints, or strategic route is unclear; otherwise keep the durable outcome in Goal and use a lightweight plan-shaped beat checkpoint. Complex never claims an unavailable UI action occurred.
- Codex Goal carries a durable `thread_goal` or `phase_goal`; `beat_objective` belongs to the current Plan/Loop.
- When a task spans multiple turns or queued beats and has a verifiable stopping condition, Complex activates the available Codex Goal surface. A non-terminal `next_route` is queued work, not a request for the user to say “continue.”
- Subagents are bounded workers. Standing lanes are recurring responsibilities. Threads, worktrees, and automations are selected according to platform and task fit.
- Continuous cadence advances queued beats until objective completion or a real responsibility/tool boundary. When cross-turn continuation is selected and the current Codex surface exposes heartbeat/automation tooling, Complex activates it and records the resource instead of waiting for another user message. A completed beat does not complete the longer Codex Goal while useful queued work remains.

### Responsibility boundary

AI decides project-internal planning, reading, verification, reversible commands, topology fit, context compaction, and next-beat routing. The user is asked for Goal/public-voice changes, credentials, payment, publishing, external writes, irreversible shared-state changes, high-impact commitments, or undelegated value judgments.

### Completion

A forward-execution beat is accepted when it creates or updates a forward artifact, passes the relevant guard/evaluator, updates state or indexes, and selects the next route from observed results. A declared diagnostic beat may instead produce a route decision, falsified route, bounded blocker, or parking decision. A fixed beat count or agent self-report is not completion.

The target project's own completion predicate, artifact path, schema, field names, value types, and verifier are the executable interface. Complex governs how the route is chosen; it must not reshape project artifacts into Complex vocabulary, suppress requested evidence, or export internal contract labels as reader-facing headings.

## Diagnose Before Patching

| Failure class | Typical symptom | Repair target |
| --- | --- | --- |
| Prompt | Goal, constraint, output, or completion contract is ambiguous | prompt contract and eval case |
| Context | required facts are absent, stale, or polluted | context assembly, retrieval, compaction |
| Harness | tools, environment, policy, observability, or recovery fail | runtime interface and mechanical controls |
| Loop | retry, route, evaluation, continuation, or stop logic is wrong | completion predicate and progress controller |
| Model | the first four layers are adequate but performance remains weak | model choice, decomposition, or escalation |

## Runtime Kit

- Core protocol: `protocol/core.md`
- Quickstart: `docs/quickstart.md`
- Complex self-maintenance state: `protocol/current-state.md` (maintainer-only, never target-project context)
- Templates: `templates/`
- Filled examples: `docs/examples/`
- External method mapping: `docs/external-methods.md`
- Complex self-optimization: `docs/self-optimization.md`
- Pinned reference-implementation evidence: `docs/reference-implementation-evidence.json`
- Active architecture re-baseline: `docs/active-architecture-rebaseline.md` and `docs/active-architecture-rebaseline.json`
- Mechanism maturity: `docs/mechanism-maturity.md` and `docs/mechanism-maturity.json`
- Behavior cases and transcript rules: `docs/behavior-regression-cases.json`, `docs/behavior-transcript-review-rules.json`
- Experimental borrowing and repeated comparisons: `docs/evals/experiment-program.md`, `docs/evals/records/`
- Codex repo skill: `.agents/skills/complex-runtime/SKILL.md`

The four primary runtime templates are:

- `templates/prompt.md`
- `templates/context.md`
- `templates/harness.md`
- `templates/loop.md`

Templates are optional landing pads, not mandatory machine fields. Current examples are filled examples, not certified representative cases.

## Verification

```bash
python3 tools/check_behavior_regression_pack.py
python3 tools/review_behavior_transcript.py --validate-rules
python3 tools/check_mechanism_maturity.py
python3 tools/check_active_architecture_rebaseline.py
python3 tools/check_eval_records.py
python3 tools/check_mechanism_revalidation_results.py
python3 tools/check_reference_implementation_evidence.py
python3 tools/check_experiment_program.py
# Optional empirical suites; use Codex calls and write append-only eval records.
# The first is a diagnostic contract screen, not effectiveness evidence.
python3 tools/run_bounded_experiments.py
# The second runs writable synthetic projects and reports descriptive outcomes.
python3 tools/run_executable_mechanism_pilots.py
# Scorer-only repairs must re-score frozen outputs and write a separate result.
python3 tools/rescore_executable_mechanism_pilots.py docs/evals/results/<frozen-run>.json
python3 tools/test_run_executable_mechanism_pilots.py
python3 tools/test_inspect_recovery_anchor.py
python3 tools/test_verify_complex_integrity.py
python3 tools/verify_complex_integrity.py
pnpm -C docs/protocol_explainer_site build
```

Expected integrity result:

- behavior cases and transcript rules have the same IDs, and the required core inventory is covered;
- eleven active mechanisms after consolidation and fifteen pinned reference implementations;
- two bounded upstream reproductions recorded separately from Complex validation;
- seven externally calibrated primary experiments covering every core and conditional-extension mechanism;
- one current frozen full-suite result, one append-only scorer repair, and one clean-context independent model review;
- every case links to a known mechanism;
- integrity verifier reports `failure_count: 0`;
- the explainer site builds successfully.

Keep this repository current and small. Do not add history archives, migration logs, rendered output packages, or long machine-board records to the active tree.
