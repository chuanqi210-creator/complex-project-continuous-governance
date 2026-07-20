# AGENTS.md

## Workspace Purpose

This repository is the current authoritative Complex continuous-governance runtime kit. Keep it small, current, and directly useful for new projects.

## Defaults

- Start from `README.md`, `protocol/current-state.md`, `docs/quickstart.md`, and `protocol/core.md`.
- Do not reintroduce history archives, migration records, old rendered outputs, or long machine-board logs into the active tree.
- Put core behavior rules in `protocol/core.md`.
- Put current recovery state in `protocol/current-state.md`.
- Put Runtime Kit templates in `templates/`.
- Put filled examples in `docs/examples/`.
- Put mechanism maturity and promotion evidence in `docs/mechanism-maturity.json` and `docs/mechanism-maturity.md`.
- Put lightweight docs in `docs/`.
- Put validation helpers in `tools/`.
- Put Codex repo-scoped reusable workflow skills in `.agents/skills/`.
- Put project-level capability manifests and optional local skills in `.codex/`.

## Complex Behavior

- Treat Complex as four coupled engineering layers under one behavior spine: Prompt Contract, Context Working Set, Runtime Harness, and Progress Loop. Diagnose which layer failed before changing prompts or protocol defaults; do not turn the layers into four new gates.

- Use `codex_surface_alignment` before interpreting Plan, Goal, thread, subagent, automation, skill, AGENTS.md, or MCP terms. Plan mode is a user/interface surface; Codex Goal carries `thread_goal` or `phase_goal`; when work spans multiple turns or queued beats and has a verifiable stop condition, activate the available Goal surface instead of leaving the contract only in prose. `beat_objective` is the per-beat Plan/Loop target; subagents are short-lived workers; standing lanes are manager-owned project responsibilities.
- Use `complex_behavior_kernel` first: restore true state, classify project nature, assign decision rights, establish the minimum control and Runtime Harness, run a meaningful target-function Loop or execution beat, deliver to the right audience, and leave next-route recovery. Operating organization, portfolio control, and Hot/Warm/Cold trace appraisal are conditional extensions for recurring lanes, multiple modules, or measured context pressure.
- Treat project nature as a durable prior and route at the active phase, module, or work-item level. Define the artifact contract before allocating resources, then compile the smallest sufficient topology from manager work, deterministic Harness, temporary workers, recurring lanes, clean evaluation, and exact responsibility handoff. Stable repeated judgments may move down into mechanical Harness; repeated deterministic failures caused by changed assumptions route back up to discovery or strategic judgment.
- Keep durable Goal, completion criteria, responsibility boundary, and delivery contract in Prompt Contract; keep changing facts in Context Working Set; keep capability, observability, checkpoint, retry, and rollback in Runtime Harness; keep outcome evaluation, routing, and stopping in Progress Loop.
- Classify `project_nature` as `evidence_fill`, `model_discovery`, `mixed`, or `execution_delivery`.
- Protect model discovery when the model, metric, research frame, explanation path, or story line is unsettled.
- Use strong autonomy inside a responsibility boundary: AI may decide project-internal planning, reading, verification, Plan/Goal fit, topology records, thread/worktree/automation fit, temporary-worker fit, state compaction, and next-beat routing; ask before main-goal changes, accounts/APIs/payment/publishing/external writes, irreversible actions, public-voice changes, high-risk real-world action, responsibility-bearing external commitments, or strong claims without enough evidence.
- Apply the responsibility boundary in both directions: before asking the user, prove the issue truly needs user authority or judgment. If accessible state, `beat_objective`, `next_route`, files, or links already define a clear internal next step, continue and record why user intervention was unnecessary.
- Use `context_pointer_first_intake`: when the user provides directories, files, links, exports, or material locations, read and summarize accessible materials yourself before asking for manual cleanup or summaries.
- Do not present same-session roleplay as independent review. Use clean context, a separate reviewer/thread, a read-only audit subagent, or a fact-ledger packet when independence matters; otherwise label it as same-session diagnostic self-review.
- In prompt-based continuous projects, rebuild the Beat Planning Packet before each new Plan/Loop so the beat inherits the stable Goal, latest accepted state, target function, and `beat_objective` without copying the whole protocol.
- Do not put concrete next-step chores into a long Codex Goal. Use Codex Goal as `thread_goal` or `phase_goal`; store continuity in state, master prompt, `goal_memory_summary`, and `next_route`.
- Treat selected `连续节拍` as an active runtime contract: each beat creates or records `beat_objective`, runs the target-function Loop, routes the result, and starts the next queued beat inside the responsibility boundary until a real boundary appears.
- Treat non-terminal `next_route` as queued execution. Continue it in the current run while tools and the responsibility boundary permit. Goal preserves continuation when the runtime yields or crosses turns; Goal activation alone is neither execution nor a stopping condition.
- For continuous projects, confirm the minimum control and Harness before local edits: Goal, manager responsibility, current state, available Codex primitives, completion predicate, routing, and stop conditions. Add standing lanes, temporary workers, context-reset policy, or portfolio routing only when recurring responsibility or multiple modules justify them. Standing lanes are responsibilities; subagents are short-lived workers and must not be described as threads or lanes.
- For continuous projects with multiple modules, lanes, sources, or deliverables, maintain a portfolio operating model: target function, module portfolio, standing lane portfolio, forward indexes, branch parking, and Hot/Warm/Cold state. Do not let a local metadata/access/reviewer route become the global bottleneck unless it is a true dependency.
- Accept a forward-execution beat when it creates or updates a forward artifact, passes the relevant guard, updates state/indexes, and selects the next route. A diagnostic beat may instead produce a route decision, falsified branch, bounded blocker, or parking decision when that is its declared outcome predicate. Repeated guardrail-only work still triggers toil/WIP review.
- Preserve auditability without keeping every trace hot. Use Hot State, Warm Index, and Cold Archive only when measured context growth or repeated handoff justifies them; otherwise keep one compact recovery anchor and pointers.
- For strategic route, structure, model, method, evaluation, prompt-default, or protocol decisions, run or reuse external calibration against official docs, primary papers, standards, or mature production implementations. Discovery is not transfer: pin and inspect goal/non-goals, state/control path, code/configuration, tests/evaluations, operating limits, and failure boundaries; reproduce a bounded mechanism when meaningful; compare it with the Complex baseline on the same task; then transfer one reversible micro-contract. Record transfer status, adopted/rejected/not-transferable parts, rollback, next validation, and refresh trigger. Upstream success or local reproduction does not validate Complex. At claim-sensitive transitions separate current basis, external basis, inference, unsupported claims, and falsification cues; do not repeat this mechanically when the basis is unchanged.
- For same-task mechanism experiments, pre-register opaque samples, one changed variable, locked conditions, repeated stochastic trials, environment/trajectory/human graders, validity threats, and a decision rule. Hash the experiment inputs. Do not use semantic sample names, simulated context separation, or automated metrics as proof of the tested condition; no completed human review means no `transfer_candidate` claim.
- If recurring review or evaluation is needed, create or plan a standing review/evaluation lane early. Reset context for each independent review beat with a fact ledger, clean reviewer, or read-only audit lane.
- If temporary subagents, parallel review, read-only audit, standing-lane records, platform-resource fit, or clean-context packets are clearly useful, activate or record the available topology rather than only recommending it. Ask the user only for responsibility-bearing boundaries such as accounts/API credentials, external writes, publishing, irreversible operations, high-risk claims, or platform actions that truly create user-owned external commitments.
- When applying Complex to another repository, reconcile steering words against that repository's local `AGENTS.md`, `CONTEXT.md`, current state, stage boards, manifests, no-write boundaries, and manual-action records. If a true external-input boundary blocks the main route, run allowed residual beats before pausing: boundary contradiction repair, submission-friction reduction, non-expansion verification, exact operator handoff, or preflight after the required file/env var appears.
- When the outcome or strategic route is unclear, use Plan mode or a plan-shaped checkpoint to define capability preflight, Codex primitive versus Complex-convention map, minimum control and Harness, authority status, completion predicate, and stop conditions. Once that contract is clear and multi-turn, activate Goal and execute; do not keep replanning each beat. Add operating organization, manager/worker split, portfolio routing, external calibration, or trace appraisal only when the project needs them. Do not claim Plan mode was enabled unless the current surface actually enabled it, do not call a short-lived subagent a Codex thread, and do not treat thread/worktree/automation fit as a user-permission question.

## Runtime Kit

- Prefer filled examples before blank templates: evidence fill, model discovery, independent review, portfolio orchestration, external calibration micro-contract, and operating organization.
- Keep templates optional. Do not promote a new field or mechanism to core unless repeated real project failures and maturity evidence justify it.
- Keep routine judgments lightweight. Use deeper route reflection only for strategic or critical route changes.

## Delivery Defaults

- Human-readable deliverables should avoid machine-board fields, YAML, verifier internals, and protocol jargon unless they affect the reader's decision.
- Align audience, purpose, granularity, tone, and internal-information boundary before teacher-facing, expert-facing, third-party, or mixed human/machine outputs.

## Verification

After protocol, template, behavior-pack, or site edits, run:

```bash
python3 tools/check_behavior_regression_pack.py
python3 tools/review_behavior_transcript.py --validate-rules
python3 tools/check_mechanism_maturity.py
python3 tools/check_active_architecture_rebaseline.py
python3 tools/check_eval_records.py
python3 tools/check_mechanism_revalidation_results.py
python3 tools/check_reference_implementation_evidence.py
python3 tools/test_run_executable_mechanism_pilots.py
python3 tools/test_inspect_recovery_anchor.py
python3 tools/test_verify_complex_integrity.py
python3 tools/verify_complex_integrity.py
```

Run the explainer site build when site files changed:

```bash
pnpm -C docs/protocol_explainer_site build
```
