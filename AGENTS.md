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

- Use `codex_surface_alignment` before interpreting Plan, Goal, thread, subagent, automation, skill, AGENTS.md, or MCP terms. Plan mode is a user/interface surface; Codex Goal is `thread_goal` or `phase_goal` and AI decides whether the Goal surface should carry that contract; `beat_objective` is the per-beat Plan/Loop target; subagents are short-lived workers; standing lanes are manager-owned project responsibilities.
- Use `complex_behavior_kernel` first: restore true state, classify project nature, assign decision rights, establish the control plane and operating organization, run the smallest meaningful target-function Loop or execution beat, deliver to the right audience, and leave next-route recovery. For continuous projects, the control plane covers direction, authority, state, topology, portfolio operating model, routing, external calibration, hallucination sentinel status, trace appraisal, and stop conditions before local optimization.
- Keep durable Goal, completion criteria, responsibility boundary, and delivery contract in Prompt Contract; keep changing facts in Context Working Set; keep capability, observability, checkpoint, retry, and rollback in Runtime Harness; keep outcome evaluation, routing, and stopping in Progress Loop.
- Classify `project_nature` as `evidence_fill`, `model_discovery`, `mixed`, or `execution_delivery`.
- Protect model discovery when the model, metric, research frame, explanation path, or story line is unsettled.
- Use strong autonomy inside a responsibility boundary: AI may decide project-internal planning, reading, verification, Plan/Goal fit, topology records, thread/worktree/automation fit, temporary-worker fit, state compaction, and next-beat routing; ask before main-goal changes, accounts/APIs/payment/publishing/external writes, irreversible actions, public-voice changes, high-risk real-world action, responsibility-bearing external commitments, or strong claims without enough evidence.
- Apply `human_intervention_drift_guard`: before asking the user, prove the issue truly needs user authority or judgment. If accessible state, `beat_objective`, `next_route`, files, or links already define a clear next step inside the responsibility boundary, continue and record why user intervention was unnecessary.
- Use `context_pointer_first_intake`: when the user provides directories, files, links, exports, or material locations, read and summarize accessible materials yourself before asking for manual cleanup or summaries.
- Do not present same-session roleplay as independent review. Use clean context, a separate reviewer/thread, a read-only audit subagent, or a fact-ledger packet when independence matters; otherwise label it as same-session diagnostic self-review.
- In prompt-based continuous projects, use `prompt_rehydration_gate` before each new Plan/Loop so each beat inherits the master prompt, current state, target function, and `beat_objective`.
- Do not put concrete next-step chores into a long Codex Goal. Use Codex Goal as `thread_goal` or `phase_goal`; store continuity in state, master prompt, `goal_memory_summary`, and `next_route`.
- Treat selected `连续节拍` as an active runtime contract: each beat creates or records `beat_objective`, runs the target-function Loop, routes the result, and starts the next queued beat inside the responsibility boundary until a real boundary appears.
- For continuous projects, confirm the control plane before choosing local edits: manager responsibility, standing lanes, temporary worker pool, context-reset policy, Beat Router, and stop conditions. Standing lanes are project responsibilities that persist across beats; subagents are short-lived workers and must not be described as threads or lanes.
- For continuous projects with multiple modules, lanes, sources, or deliverables, maintain a portfolio operating model: target function, module portfolio, standing lane portfolio, forward indexes, branch parking, and Hot/Warm/Cold state. Do not let a local metadata/access/reviewer route become the global bottleneck unless it is a true dependency.
- Treat each beat as accepted only when it creates or updates a forward artifact, passes the relevant guard, updates state/indexes, and selects the next route. QA, citation, reviewer, metadata/no-values, and still-closed notes are guardrails; repeated guardrail-only work triggers toil/WIP review: produce a model/data/parameter/writing/branch/calibration/state/topology delta, park the branch, route to another module, or justify why the guardrail is the true dependency.
- Preserve auditability without keeping every trace hot: demote stale material from Hot State to Warm Index or Cold Archive by pointer before adding another long log.
- For strategic route, structure, model, method, evaluation, prompt-default, or protocol decisions, run or reuse external calibration against official docs, primary papers, standards, or mature production writeups. Every mechanism-level issue needs source, problem matched, adopted, rejected, not transferable, Complex micro-contract, and refresh trigger. Then run a hallucination sentinel separating current basis, external basis, inference, unsupported claims, and falsification cues.
- If recurring review or evaluation is needed, create or plan a standing review/evaluation lane early. Reset context for each independent review beat with a fact ledger, clean reviewer, or read-only audit lane.
- If temporary subagents, parallel review, read-only audit, standing-lane records, platform-resource fit, or clean-context packets are clearly useful, activate or record the available topology rather than only recommending it. Ask the user only for responsibility-bearing boundaries such as accounts/API credentials, external writes, publishing, irreversible operations, high-risk claims, or platform actions that truly create user-owned external commitments.
- When applying Complex to another repository, reconcile steering words against that repository's local `AGENTS.md`, `CONTEXT.md`, current state, stage boards, manifests, no-write boundaries, and manual-action records. If a true external-input boundary blocks the main route, run allowed residual beats before pausing: boundary contradiction repair, submission-friction reduction, non-expansion verification, exact operator handoff, or preflight after the required file/env var appears.
- When Plan mode is asked to design continuous execution, produce a planning checkpoint and orchestration contract before business execution: capability preflight, Codex surface/resource taxonomy, control plane, operating organization, authority/platform-boundary status, manager/worker split, Beat Router, external calibration status, hallucination sentinel status, trace appraisal, and stop conditions. Do not claim Plan mode was automatically enabled unless the current surface actually enabled it, do not call a short-lived subagent a Codex thread, and do not treat thread/worktree/automation fit as a user-permission question; actual platform creation still follows current tool semantics.

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
python3 tools/test_inspect_recovery_anchor.py
python3 tools/test_verify_complex_integrity.py
python3 tools/verify_complex_integrity.py
```

Run the explainer site build when site files changed:

```bash
pnpm -C docs/protocol_explainer_site build
```
