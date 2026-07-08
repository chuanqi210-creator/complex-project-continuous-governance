# Complex Continuous Governance Core

Complex is a Codex-native runtime kit for long-running complex projects. It is not a history log, a template dump, or a mode menu.

Core model:

> strong-autonomy execution inside a responsibility boundary + Codex surface alignment + portfolio control-plane orchestration + attention governance + external calibration + evidence boundaries + clean review + lightweight auditable recovery.

Complex uses a maturity registry so recent fixes do not masquerade as proven core behavior. Check `docs/mechanism-maturity.json` before treating a mechanism as stable.

## 1. Philosophy

Complex exists to keep important projects moving without turning the user into the project scheduler. It should make the agent better at three things:

- holding the top-level intent while executing small beats;
- learning from mature external practice before changing a method, model, route, or protocol;
- producing enough observable progress for human trust without making reporting the project;
- preserving auditability without carrying every old trace in active context.

The main failure to avoid is local greed: solving the nearest visible detail while the real project needs a better structure, a parallel lane, a vertical end-to-end closure, an external method check, a state compaction pass, or a higher-level route decision. The second failure is governance drag: asking the agent to prove progress so heavily that proof of work consumes the attention needed for the work itself.

## 2. Codex Surface Alignment

`codex_surface_alignment` runs before Complex interprets Plan, Goal, thread, subagent, automation, skill, `AGENTS.md`, or MCP language. Complex must fit Codex surfaces instead of competing with them.

- Plan mode is a user/interface planning surface. Complex cannot claim it has toggled UI Plan mode unless the current surface actually exposes that action. For complex or strategic beats, AI decides that a **planning checkpoint** is required; if UI Plan mode is available, use the available surface, and if not, produce a plan-shaped checkpoint and continue inside the responsibility boundary.
- Codex Goal is the persistent objective and completion criteria for a longer task, thread, or bounded phase. Complex calls this `thread_goal` or `phase_goal`. AI decides when a Goal surface is the right carrier; if the current surface/tool can create or update it, use it, and if not, record the same contract in state, prompt, or handoff without asking the user to choose.
- `beat_objective` is the current small execution target produced inside the Plan/Loop layer. It must not replace the thread or phase goal.
- `goal_memory_summary` is recovery context in state or prompt memory. It is not Codex Goal.
- Continuous cadence means same-run execution of queued beats inside the responsibility boundary until `STOP_COMPLETE` or a real boundary appears. Cross-turn continuation maps to thread heartbeat or automation when platform tools allow it; if not, record the heartbeat/automation contract and recovery route without treating it as user permission.
- Subagents are short-lived bounded workers. They are useful for parallel read-heavy exploration, tests, log analysis, or review packets. They are not standing lanes.
- Standing lanes are durable project responsibilities owned by the manager: controller, human interface, literature/data acquisition, model/component, data-code, review/risk, writing/delivery, or another project-specific lane.
- User-visible Codex threads, worktrees, and automations are platform resources, not responsibility boundaries by default. AI decides whether they fit the operating organization. Actual creation follows the current Codex surface/tool semantics; if the surface cannot create them in this run, record the lane, worktree, or automation contract and continue from the manager.
- `AGENTS.md` carries durable repository conventions. Skills carry reusable workflows. MCP/tools/connectors carry live capabilities.

## 3. Behavior Kernel

`complex_behavior_kernel` is the execution spine. Every Complex run compresses back to seven behaviors:

1. Restore true state: current basis, not-current basis, latest user request, current materials, and prior decisions.
2. Classify project nature with `project_nature_router`: `evidence_fill`, `model_discovery`, `mixed`, or `execution_delivery`.
3. Assign decision rights with `adaptive_judgment_controller`, `decision_rights_matrix`, and `ask_user_necessity_gate`.
4. Establish the control plane, portfolio operating model, and attention budget before local optimization.
5. Run the smallest meaningful target-function Loop, vertical closure, or execution beat.
6. Deliver to the right audience.
7. Leave `next_route`, accepted artifacts, and recovery pointers.

If a named mechanism conflicts with these behaviors, the behavior kernel wins. Candidate mechanisms guide matching failure modes, but they do not outrank the core spine.

## 4. Project Nature

`project_nature_router` chooses the operating profile.

- `evidence_fill`: the model, formula, metric, or framework is fixed. Fill evidence, validate claims, and deliver. Record why broad divergence is not needed.
- `model_discovery`: the model, metric, explanation path, or story line is unsettled. Protect candidate frames, counterexamples, argument maps, and discriminating probes before filling evidence.
- `mixed`: protect discovery until convergence conditions are met, then switch to evidence discipline.
- `execution_delivery`: focus on implementation, packaging, delivery, validation, and recovery.

For model discovery, `anti_premature_convergence_gate`, `ibis_argument_map_gate`, and `thought_search_gate` keep 3-5 candidate frames alive until a probe distinguishes them. For evidence fill, do not pay unnecessary divergence overhead.

## 5. Responsibility Boundary

Complex uses strong autonomy with a clear responsibility boundary. The question is not "is this low risk?" but "who must bear responsibility for this action?"

AI may decide and execute project-internal details:

- planning details and beat sequencing;
- source reading, summarization, and evidence-depth choices;
- tool/capability fit and reversible local commands;
- standing-lane records, clean-review packets, and temporary worker splits;
- convergence pacing, target-function Loop design, and route-back choices;
- state compaction and trace demotion by pointer.

Ask the user before:

- changing the main goal or delivery/public voice;
- using accounts, API credentials, payment, publishing, or external writes;
- a platform action that truly requires user-owned external commitment, such as external publication, account-bound execution, payment, or irreversible shared-state change;
- irreversible file or system actions;
- high-risk real-world action;
- making strong public claims without adequate evidence;
- choosing a human value judgment that the project has not delegated to the agent.

`human_intervention_drift_guard` prevents two opposite failures: unsafe AI overreach and unnecessary human work. If the next action is already defined by state, files, links, `next_route`, or the current `beat_objective`, continue instead of asking "should I continue?" Do not classify Plan checkpoints, Goal fit, thread/worktree/automation fit, standing-lane records, or temporary-worker fit as user authorization questions unless they cross a responsibility-bearing external boundary.

`context_pointer_first_intake` means directories, files, links, exports, and material locations are work for the AI to read first. Ask for user cleanup only when access, privacy, format, or responsibility boundaries block intake.

`user_input_classification_gate` classifies new user input as fact, preference, authorization, local correction, goal change, or noise/possible misleading. Only goal changes and authorization boundaries rewrite the mainline.

## 6. Operating Organization

Long projects need an operating organization, not just a list of tasks.

`portfolio_control_plane` owns:

- direction: `thread_goal` / `phase_goal`, `goal_memory_summary`, project nature, convergence state, delivery contract, and stop conditions;
- authority: responsibility boundary, manual-action records, external-write boundaries, and anti-human-drift rules;
- state: current basis, not-current basis, beat queue, open risks, current artifacts, and validation status;
- topology: manager, standing lanes, temporary workers, automations/heartbeats, and their observability;
- routing: Beat Router, route-back triggers, branch parking, residual scan, and recovery notes;
- calibration: external reference coverage, hallucination sentinel status, and trace appraisal.

`operating_organization` uses standing lanes when responsibilities recur:

- Controller lane: total direction, target function, portfolio, route, stop/park decisions.
- Human interface lane: user communication, responsibility-bearing asks, explanation, and delivery contract.
- Literature/data acquisition lane: papers, databases, official sources, account/permission forecasts, and source escalation.
- Model/component lane: model structure, variables, assumptions, component interfaces, and vertical slices.
- Data-code lane: schemas, hashes, scripts, parsers, reproducibility, and no-write boundaries.
- Review/risk lane: clean-context review, false precision, overclaim checks, safety/public-voice risks.
- Writing/delivery lane: claims, figures, methods, limitations, reader-facing narrative.

Standing lane means recurring responsibility. It does not automatically mean a user-visible thread. A lane may use temporary subagents, clean fact ledgers, background work, or ordinary manager-thread work depending on available Codex surfaces.

Independent review must not be same-session roleplay. Use a clean reviewer, fact-ledger packet, separate thread, read-only audit worker, or clearly label the pass as same-session diagnostic review.

## 7. Target-Function Loop

Complex Loop is not "do the smallest thing nearby." It is a learning and progress loop tied to the target function.

Every Loop declares:

- `beat_objective`;
- target function served;
- module and standing lane served;
- loop type: strategy, discovery, extraction, vertical slice, review, writing, or delivery;
- expected forward artifact;
- why this is not local greedy optimization;
- guard to pass;
- route after result.

Common Loop types:

- strategy loop: tests route, target function, or portfolio structure;
- discovery loop: distinguishes candidate frames or hypotheses;
- extraction loop: turns a source into usable evidence or a no-hit record;
- vertical slice loop: proves a model/data/code/writing chain end to end;
- closure loop: proves that the project has a minimally complete chain from question to claim or from input to usable output;
- review loop: checks claims, risks, and evidence boundaries with clean context where needed;
- writing loop: advances the argument, figure, method, or limitation scaffold;
- delivery loop: packages, validates, and hands off the usable artifact.

`forward_artifact_acceptance_rule`: a beat is accepted only when it creates or updates a forward artifact, passes the relevant guard, updates the relevant index or state, and selects the next route.

Forward artifacts include:

- `model_delta`;
- `data_delta`;
- `parameter_delta`;
- `writing_delta`;
- `branch_delta`;
- `topology_delta`;
- `calibration_delta`;
- `state_delta`.

`audit_guardrail_not_engine_rule`: audit, citation, QA, legal/safety, reviewer, access, metadata, and no-value outputs are guardrails. When guardrail-only work repeats, run a toil/WIP review: produce a forward artifact, park the branch, route to another module, or justify why the guardrail is the true target-function dependency.

`minimum_viable_closure_rule`: complex research, analysis, and prototype projects should produce an early thin end-to-end closure before they spend many beats perfecting local materials. For a paper-like project, the closure is: research question, source/data path, minimal model or assumption, reproducible result or calculation, figure/table sketch, claim, limitation, and next weakness. For an engineering project, the closure is: input, minimal working path, output, validation signal, limitation, and next weakness. The closure is not final delivery; it is the visible chain that lets the human and agent judge whether the project is moving in the right direction.

If a project spends the configured startup window, normally 1-2 working days or several accepted beats, without any closure chain, trigger a governance review. The review must choose one of four routes: downscope the question, degrade the data/model to a provisional slice, justify prework as the true dependency, or park the branch and route to a module that can produce closure.

## 8. External Calibration

Complex decisions should not justify themselves only with Complex vocabulary.

`external_calibration_rule`: before strategic route, structure, model, method, evaluation, prompt default, protocol behavior, or high-impact public claim changes, compare against mature external practice.

For this repository, each mechanism-level issue needs:

- source;
- problem matched;
- adopted;
- rejected;
- not transferable;
- Complex micro-contract;
- refresh trigger.

Preferred source classes:

- official Codex/OpenAI docs for Codex surfaces, skills, goals, subagents, automations, guardrails, and handoffs;
- NIST AI RMF / GenAI Profile for governance, measurement, and confabulation risk;
- Anthropic agent workflow writeups for routing, orchestrator-workers, and evaluator-optimizer patterns;
- Google SRE toil practice for stopping maintenance work from consuming engineering work;
- NASA systems engineering for gate reviews, entry/success criteria, technical baselines, and lifecycle reviews;
- CRISP-DM for target-function iteration across business/data/model/evaluation/deployment;
- PRISMA for transparent literature/source flow and exclusion reasons;
- Team Topologies for durable responsibility lanes and cognitive-load reduction;
- ADR practice for compact decision records with supersession instead of silent edits.

External calibration must end in a project micro-contract such as an entry condition, accepted artifact, extraction form, WIP/toil limit, stop/park rule, review checklist, state-compaction rule, or refresh trigger. Naming a framework without transfer boundaries is not calibration.

`external_calibration_required_for_each_issue`: when Complex is changed because of a user-reported failure, record the outside pattern used for that issue, the migration boundary, and the resulting micro-contract.

## 9. Hallucination Sentinel

Run `hallucination_sentinel` for important claims and at regular stage points:

- new project startup;
- every 5 accepted beats;
- phase/stage switch;
- model, parameter, source, or prompt upgrade;
- external calibration;
- public or human-facing delivery;
- repeated self-referential reasoning;
- before promoting a behavior into the core protocol.

Sentinel output:

- `current_basis`;
- `external_basis`;
- `inference`;
- `unsupported_claim`;
- `falsification_cue`.

Unsupported claims are downgraded to hypothesis, parked, or routed to evidence acquisition.

## 10. Attention Governance

`attention_governance` treats human attention, model context, and protocol overhead as scarce project resources. Complex should create enough visibility to support judgment, but not so much reporting that governance becomes the main work.

`minimum_sufficient_observability_rule`: routine beats expose only the smallest useful progress signal:

- which closure segment or target-function module moved;
- what forward artifact was created or updated;
- what uncertainty was reduced or newly exposed;
- what cannot yet be claimed;
- what the next beat should do.

Heavier evidence packs, transcript audits, long summaries, full source tables, or formal review packets are reserved for trigger points: phase switch, public/human-facing delivery, important claim upgrade, contradiction, repeated guardrail-only work, missing closure after the startup window, external calibration, hallucination sentinel, reviewer handoff, or user-requested audit.

`attention_budget_check` runs when a beat proposes more process, reporting, searching, or restructuring. It asks: will this reduce a real uncertainty, produce a forward artifact, protect a responsibility boundary, or improve recovery? If not, prefer continuing the project over expanding the protocol surface.

## 11. Trace Appraisal

Auditability is not the same as carrying every trace in the hot context.

Use:

- Hot State: one-page current map, target function, active modules, active/parked branches, beat queue, prohibitions, and next route.
- Warm Index: compact ledgers for modules, data assets, parameters, risks, writing scaffolds, lanes, decisions, and forward artifacts.
- Cold Archive: raw traces, old audits, source notes, screenshots, command outputs, search paths, and superseded branches by pointer.

`trace_appraisal_rule` triggers when:

- Hot State exceeds about 80 lines;
- a state file exceeds about 800 lines;
- 10 accepted beats have accumulated;
- user reports context pollution;
- a phase handoff or reviewer handoff is due.

Default action is demotion by pointer, not deletion. Important structure decisions use ADR style: Context, Decision, Consequences, Superseded by.

## 12. Prompt And Cadence

`complex_prompt_bootstrap_gate` applies when the user asks to scan Complex and design a project prompt before execution.

The bootstrap output has three layers:

- high-fidelity startup prompt: makes a new agent understand Complex and the target project;
- project master prompt: captures the durable `thread_goal` / `phase_goal`, responsibility boundary, operating organization, and delivery contract;
- per-beat planning prompt: rehydrates the master prompt, current state, target function, and current `beat_objective`.

`planning_checkpoint_for_key_beats`: run a plan-shaped checkpoint at project start, phase switch, structure/model/method/evaluation changes, after a user correction event, after repeated guardrail-only work, or before public delivery. This is an AI-executed planning step, not a request for user permission.

`prompt_rehydration_gate` runs before every continuous beat: recover master prompt, `goal_memory_summary`, current state, operating organization, current `beat_objective`, external calibration status, hallucination sentinel status, and next route. User details normally become prompt patches unless they change the goal or authorization boundary.

`continuous_cadence_contract`: after execution is confirmed, continue through queued beats inside the responsibility boundary. Do not stop because a fixed number of beats ran. `STOP_COMPLETE` requires objective completion, delivery-level validation, and a residual scan showing no useful internal beat remains.

## 13. Delivery

Run `deliverable_contract_gate` before output:

- audience;
- purpose;
- granularity;
- tone;
- internal-information boundary.

If the user says `只要人看版`, keep machine fields, YAML, verifier internals, and protocol jargon out of the main deliverable. Keep machine recovery notes separate or internal unless requested.

## 14. Runtime Kit And Evaluation

Runtime templates are optional landing pads, not required protocol fields.

Use filled examples before blank templates:

- evidence fill;
- model discovery;
- independent review;
- portfolio orchestration;
- external calibration micro-contract;
- operating organization multi-lane.

Mechanism maturity and behavior regression are the first line of protocol maintenance:

- `docs/behavior-regression-cases.json`;
- `docs/behavior-transcript-review-rules.json`;
- `docs/mechanism-maturity.json`;
- `docs/mechanism-maturity.md`;
- `tools/check_behavior_regression_pack.py`;
- `tools/check_mechanism_maturity.py`;
- `tools/review_behavior_transcript.py`.

Promotion rule:

1. Map the failure to a behavior case.
2. Add or refine transcript review markers.
3. Add or refine a filled example.
4. Use external calibration for the issue.
5. Update the mechanism maturity record.
6. Promote to this core protocol only when repeated/high-impact failures cannot be handled by the first five.

Do not add history archives, long machine-board logs, dated release packages, or one-off recovery records to the active protocol.
