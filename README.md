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

Complex is organized as a stable core plus testable extensions. External precedent grounds new mechanisms; real transcripts and end-to-end outcomes are required before they are called validated.

## Install

```bash
mkdir -p ~/Documents
git clone https://github.com/chuanqi210-creator/complex-project-continuous-governance.git \
  ~/Documents/complex-project-front-governance
export COMPLEX_HOME="$HOME/Documents/complex-project-front-governance"
cd "$COMPLEX_HOME"
python3 tools/verify_complex_integrity.py
```

Update with:

```bash
cd "${COMPLEX_HOME:-$HOME/Documents/complex-project-front-governance}"
git pull --ff-only
python3 tools/verify_complex_integrity.py
```

Complex remains a standalone runtime. A target repository does not need its own `Complex` directory.

## Start A Project

Copy-ready high-fit request:

```text
请先读取已安装的 Complex，并结合当前项目建立 Project Prompt Contract。请区分稳定目标与动态上下文，判断项目性质，明确担责边界、完成标准、评价方法和交付对象。

随后按四层运行：每拍重水化 Prompt Contract；组装最小充分、可溯源的 Context Working Set；确认 Runtime Harness 的工具、环境、检查点和降级路线；运行以真实结果为完成条件的 Progress Loop。能在担责边界内继续时自动进入下一拍，不等我说继续。

请先诊断问题属于 prompt、context、harness、loop 还是 model limitation，再修改对应层。不要把上下文遗漏、工具故障或停止逻辑问题都修成更长的提示词。重要评审使用清上下文；重要机制判断做外部校准；输出只要人看版。
```

If you want prompt design before execution:

```text
请先扫描 Complex 和当前项目，只设计 Project Prompt Contract、Context Working Set、Runtime Harness 与 Progress Loop 方案，不执行项目。给出可复制 prompt 和第一拍的 planning checkpoint；我确认项目目标后再执行。
```

## How Complex Runs

The seven stable behaviors are:

1. Restore true state and assemble the current working context.
2. Classify project nature: `evidence_fill`, `model_discovery`, `mixed`, or `execution_delivery`.
3. Assign decision rights through a responsibility boundary.
4. Establish the control plane, operating organization, and runtime harness.
5. Run the smallest meaningful target-function Progress Loop.
6. Deliver to the right audience and evaluate the outcome.
7. Leave `next_route`, accepted artifacts, recovery pointers, and layer diagnosis.

### Codex surface map

- Plan mode is a planning surface. Complex uses it when available at key checkpoints and never claims an unavailable UI action occurred.
- Codex Goal carries a durable `thread_goal` or `phase_goal`; `beat_objective` belongs to the current Plan/Loop.
- Subagents are bounded workers. Standing lanes are recurring responsibilities. Threads, worktrees, and automations are selected according to platform and task fit.
- Continuous cadence advances queued beats until objective completion or a real responsibility/tool boundary. When cross-turn continuation is selected and the current Codex surface exposes heartbeat/automation tooling, Complex activates it and records the resource instead of waiting for another user message. A completed beat does not complete the longer Codex Goal while useful queued work remains.

### Responsibility boundary

AI decides project-internal planning, reading, verification, reversible commands, topology fit, context compaction, and next-beat routing. The user is asked for Goal/public-voice changes, credentials, payment, publishing, external writes, irreversible shared-state changes, high-impact commitments, or undelegated value judgments.

### Completion

A beat is accepted when it creates or updates a forward artifact, passes the relevant guard/evaluator, updates state or indexes, and selects the next route from observed results. A fixed beat count or agent self-report is not completion.

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
- Complex self-maintenance state: `protocol/current-state.md` (not target-project context)
- Quickstart: `docs/quickstart.md`
- Templates: `templates/`
- Filled examples: `docs/examples/`
- External production mapping: `docs/external-methods.md`
- Mechanism maturity: `docs/mechanism-maturity.md` and `docs/mechanism-maturity.json`
- Behavior cases and transcript rules: `docs/behavior-regression-cases.json`, `docs/behavior-transcript-review-rules.json`
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
python3 tools/test_inspect_recovery_anchor.py
python3 tools/test_verify_complex_integrity.py
python3 tools/verify_complex_integrity.py
pnpm -C docs/protocol_explainer_site build
```

Expected baseline:

- 42 behavior cases and 42 transcript rules;
- every case links to a known mechanism;
- integrity verifier reports `failure_count: 0`;
- the explainer site builds successfully.

Keep this repository current and small. Do not add history archives, migration logs, rendered output packages, or long machine-board records to the active tree.
