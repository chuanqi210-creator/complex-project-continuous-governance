---
name: complex-runtime
description: Apply Complex to long-running Codex projects. Use when asked to scan or use Complex, design a project prompt, run continuous cadence, align Plan/Goal/thread/subagent/automation surfaces, set a portfolio control plane, use external calibration, prevent hallucination/context drift, or govern evidence/model-discovery/execution projects with strong autonomy inside responsibility boundaries.
---

# Complex Runtime

Use Complex as a Codex-native orchestration workflow, not as a competing mode system. First map the project to Codex surfaces, then establish the control plane and operating organization before local execution.

Primary entrypoints when deeper detail is needed:

- `README.md`
- `protocol/current-state.md`
- `docs/quickstart.md`
- `protocol/core.md`
- `docs/mechanism-maturity.md`
- `docs/examples/`
- `templates/`

## Project View

Complex optimizes for durable project progress:

> strong-autonomy execution inside a responsibility boundary + Codex surface alignment + portfolio control-plane orchestration + attention governance + external calibration + evidence boundaries + clean review + lightweight auditable recovery.

Avoid local greed. The next nearby edit is not automatically the right next beat. For continuous work, maintain target function, modules, standing lanes, forward indexes, minimum viable closure, and state lightening before choosing local work.

## Codex Surface Map

- Plan mode is a user/interface planning surface. Do not claim it was toggled automatically unless the current surface actually enabled it. At complex or strategic beats, AI decides that a planning checkpoint is required; use the available surface if possible, otherwise produce a plan-shaped checkpoint and continue inside the responsibility boundary.
- Codex Goal is the persistent objective and completion criteria for a longer task, thread, or bounded phase. Call it `thread_goal` or `phase_goal`. AI decides whether the Goal surface should carry the phase contract; if it cannot be set from the current surface, record the same contract in state, prompt, or handoff and continue.
- `beat_objective` is the current small target inside the Plan/Loop layer.
- `goal_memory_summary` is recovery context, not Codex Goal.
- Continuous cadence means same-run execution of queued beats until `STOP_COMPLETE` or a real boundary.
- Subagents are short-lived bounded workers. They are not standing lanes.
- Standing lanes are durable project responsibilities owned by the manager.
- User-visible threads, worktrees, and automations are platform resources, not responsibility boundaries by default. AI decides whether they fit the operating organization. Actual creation follows current Codex surface/tool semantics; if unavailable, record lane, worktree, or automation contracts and keep working.

## Runtime Spine

1. Restore true state: current basis, not-current basis, current materials, latest user request, and decisions.
2. Classify project nature: `evidence_fill`, `model_discovery`, `mixed`, or `execution_delivery`.
3. Assign decision rights through the responsibility boundary.
4. Establish control plane and operating organization.
5. Run the smallest meaningful target-function Loop or execution beat.
6. Deliver to the requested audience.
7. Leave `next_route`, accepted artifacts, and recovery pointers.

Use mechanism maturity to choose depth. Core behaviors always apply. Tested and candidate mechanisms apply when their failure mode is present; do not present candidate mechanisms as proven outcomes.

## Responsibility Boundary

AI decides project-internal details: planning sequence, reading, verification depth, reversible local commands, standing-lane records, clean-review packets, temporary worker fit, convergence pacing, route-back, state compaction, and next beat.

Ask the user only for responsibility-bearing boundaries: main-goal change, account/API credentials, payment, external write, publishing, irreversible action, public voice change, high-risk real-world action, strong public claim without evidence, or a platform action that creates a user-owned external commitment.

If the next beat is already defined and inside the responsibility boundary, continue. Do not ask "should I continue?" as a default.

## Operating Organization

For long projects, form lane contracts early:

- Controller: target function, portfolio, routing, stop/park decisions.
- Human interface: responsibility-bearing asks, concise explanations, delivery contract.
- Literature/data acquisition: papers, databases, official sources, account/permission forecasts, source escalation.
- Model/component: model structure, variables, assumptions, component interfaces, vertical slices.
- Data-code: schema, scripts, hashes, reproducibility, no-write boundaries.
- Review/risk: clean-context review, overclaim control, false precision, safety/public-voice risks.
- Writing/delivery: claims, figures, methods, limitations, reader-facing output.

A lane is a responsibility. It may use manager-thread work, temporary subagents, clean fact ledgers, or real platform threads/automations depending on tools and authorization.

Independent review requires clean context, a fact-ledger packet, separate reviewer/thread, or read-only audit worker. Same-session review is diagnostic only.

## Target-Function Loop

A Loop is not the lightest nearby action. It is the smallest meaningful cycle that serves the target function and, when relevant, advances the minimum viable closure.

Each Loop states:

- `beat_objective`
- target function served
- module and standing lane served
- loop type: strategy, discovery, extraction, vertical slice, review, writing, or delivery
- expected forward artifact
- why this is not local greedy optimization
- closure segment moved or reason closure is not needed
- minimum sufficient observability signal
- guard and route

Accept a beat only when it creates or updates a forward artifact, passes the guard, updates state/indexes, and selects the next route. Guardrail-only repetition triggers toil/WIP review: create an artifact, park the branch, route elsewhere, or justify why the guardrail is the true dependency.

For research, analysis, or prototype work, seek an early thin chain from question to source/data, minimal model or assumption, result/output, figure/table or validation signal, claim/conclusion, limitation, and next weakness. If many beats pass without that chain, downscope, use a provisional slice, justify prework as the true dependency, or route elsewhere.

Routine beats should expose only the minimum useful progress signal: closure segment, forward artifact, uncertainty changed, cannot-yet-claim boundary, and next route. Heavy audit packs are for phase switches, public delivery, claim upgrades, contradictions, repeated guardrail-only work, missing closure, external calibration, hallucination sentinel, reviewer handoff, or user-requested audit.

## External Calibration And Hallucination Sentinel

Before strategic route, structure, model, method, evaluation, prompt default, protocol behavior, or high-impact public claim changes, compare against mature external practice. Prefer official docs, primary papers, standards, and production writeups.

Record:

- source
- problem matched
- adopted
- rejected
- not transferable
- Complex micro-contract
- refresh trigger

Run a hallucination sentinel at startup, every 5 accepted beats, phase switches, model/source/prompt upgrades, external calibration, public delivery, or before promoting a behavior into core rules:

- current basis
- external basis
- inference
- unsupported claim
- falsification cue

## State Lightening

Keep Hot State short. Use Warm Index for compact ledgers and Cold Archive for raw trace by pointer. Demote stale traces before adding another long log. Use ADR-style decision records for important structure changes: Context, Decision, Consequences, Superseded by.

## Output

For human-readable output, avoid machine-board fields, YAML, verifier internals, and protocol jargon unless they affect the reader's decision.

When continuous cadence is active, expose a compact runtime audit: `thread_goal` / `phase_goal`, current `beat_objective`, router decision, forward artifact, guard result, next route, resource evidence or degraded note, and residual scan.
