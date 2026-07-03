# Complex Continuous Governance Core

Complex is a runtime protocol for complex projects. It is not a history log, a template dump, or a mode menu.

Core model:

> strong-autonomy continuous execution + control-plane orchestration + evidence boundaries + anti-human/context-drift safeguards + auditable recovery.

## 1. Behavior Kernel

`complex_behavior_kernel` is the first execution spine. Every Complex round must do seven things:

1. Restore true state: identify `current_basis`, `not_current_basis`, latest user request, current materials, and prior decisions.
2. Classify project nature: run `project_nature_router` and choose `evidence_fill`, `model_discovery`, `mixed`, or `execution_delivery`.
3. Assign decision rights: run `adaptive_judgment_controller`, `decision_rights_matrix`, and `ask_user_necessity_gate`.
4. Set the control plane, then choose the work-plane target: continuous projects refresh the operating topology before local optimization; single-round work can go straight to the highest-leverage question.
5. Run the lightest useful work-plane validation or execution.
6. Deliver to the right audience.
7. Leave `next_route` and recovery notes.

If a mechanism name conflicts with these behaviors, the behavior kernel wins.

## 2. Project Nature

`project_nature_router` decides the operating profile:

- `evidence_fill`: the model, formula, metric, or framework is fixed. Use `evidence_matrix`, `claim_readiness_ladder`, and `delivery_contract`; record `divergence_noop_reason` when no model discovery is needed.
- `model_discovery`: the frame is unsettled. Use `anti_premature_convergence_gate`, `ibis_argument_map_gate`, `thought_search_gate`, and `judgment_mode: exploratory`.
- `mixed`: protect discovery until convergence conditions are met, then switch to evidence fill.
- `execution_delivery`: focus on implementation, packaging, delivery, and recovery.

Model discovery must keep candidate frameworks, issue / position / pro / con maps, counterexamples, convergence conditions, and discriminating probes visible. It must not let a local evidence gap become the main goal too early.

Evidence fill must not pay unnecessary divergence overhead. If the model is fixed, fill evidence, validate claims, and deliver.

## 3. Decision Rights

Complex defaults to strong autonomy with guardrails.

AI may decide:

- plan details
- Loop probes
- evidence depth
- tool/capability fit
- temporary subagent splits
- minor long-thread responsibility adjustments
- divergence/convergence pacing
- `lightweight_keep` when no refresh event exists

AI must ask before:

- changing the main goal
- using accounts, APIs, payment, publishing, or external writes
- irreversible file or system actions
- changing delivery/public voice
- taking high-risk real-world action
- making strong public claims without enough evidence

`manual_action_required` is for true access, permission, privacy, account, external-write, payment, publication, or real-world responsibility boundaries.

## 4. Anti-Human And Context Drift

`human_intervention_drift_guard` has two duties:

- prevent unsafe AI overreach
- prevent AI from offloading low-risk work back to the user

`known_next_step_auto_execute_rule`: if `next_route`, `round_goal`, state, or accessible materials already define a clear, low-risk, reversible next step, execute or validate it instead of asking "should I continue?"

Do not end a continuous-cadence response with "next time you say continue" or equivalent phrasing when the next route is already clear. If the environment or turn boundary truly prevents further work, record `next_route` as a recovery fact, not as a user-permission gate. The default is `auto_continue_until_boundary`, not `wait_for_user_continue`.

`context_pointer_first_intake`: if the user provides directories, files, links, exports, or material locations, read and summarize accessible materials before asking for manual cleanup, copy-paste, or summaries. Record `resource_boundary` only when access or authorization blocks intake.

`user_input_classification_gate`: classify new user input as fact, preference, authorization, local correction, goal change, or noise/possible misleading. Only goal changes and authorization boundaries rewrite the mainline.

## 5. Prompt And Continuous Cadence

`complex_prompt_bootstrap_gate` applies when the user asks to scan Complex and design a project prompt before execution.

`complex_source_resolution` runs before protocol scanning. Treat Complex and the target project as two sources:

1. `complex_source`: explicit user path, `COMPLEX_HOME`, or a standard local install.
2. `target_project_source`: the repository or material set being governed.
3. target-repository adapters/manifests: downstream evidence that may show Complex was adopted, not the Complex rule source.
4. if `complex_source` cannot be resolved, ask for the installed Complex path instead of reconstructing rules from memory.

Keep two contexts separate:

- `complex_source`: the authoritative Complex Runtime Kit, normally the installed repository at `COMPLEX_HOME` or a user-provided path.
- `target_project_source`: the repository being governed, such as its `AGENTS.md`, `CONTEXT.md`, status files, manifests, stage boards, code, and outputs.

Output:

- `protocol_scan_sequence`
- startup questions or safe defaults; if a safe recommended default exists, choose it and label it `assumed_default` instead of asking the user to pick an internal route
- project prompt rationale
- `copy_ready_prompt`
- `execution_bridge`

Do not execute business work before confirmation unless the user explicitly authorizes it.
Do not say the user selected a route unless the user actually selected it. Plan mode may ask for authority, irreversible choices, or public-facing direction changes; it should self-select routine project framing, initial cadence, and first-beat defaults when the request already asks for strong-autonomy Complex execution.

`orchestration_contract`: when the user asks for Plan mode, continuous cadence, Goal mode, long-running threads, subagents, automation, or clean-context review, the Plan must design the runtime orchestration before business execution. This contract is not optional wording; it decides which runtime resources should be used, which are unavailable, and what the fallback is.

`manager_owned_bootstrap`: prompt bootstrap, source resolution, project-nature judgment, first orchestration contract, and first beat queue are manager-thread responsibilities. Do not delegate these startup decisions to a background thread, subagent, or clean-context reviewer as the only route. Auxiliary resources may inspect bounded materials after the manager has a usable default route; if they stay silent, the manager continues from its own state.

`control_plane_orchestration`: before a continuous project enters local execution, the agent must confirm the project control plane. This is the durable operating layer that keeps the project from collapsing into a greedy sequence of local edits.

The control plane contains:

- direction: `active_goal_summary`, project nature, convergence state, delivery contract, and stop conditions.
- authority: decision rights, authorization boundaries, manual-action records, and anti-human-drift rules.
- state: `current_basis`, `not_current_basis`, open risks, beat queue, recovery route, and validation status.
- topology: manager responsibility, standing lanes, temporary workers, automations, and their observability.
- routing: Beat Router, route-back triggers, residual-beat scan, and recovery notes.

`continuous_lane_topology` is the topology part of the control plane. For continuous projects, the first active beat confirms or refreshes this topology unless current state already proves it is fresh. This is a compact control-plane beat, not a new ceremony.

The topology part must define or refresh:

- the manager thread: owns `active_goal_summary`, `current_basis`, `not_current_basis`, `beat_queue`, route decisions, stop conditions, and integration.
- standing lanes: durable responsibility channels for recurring work such as review/evaluation, evidence/data, implementation, external activation, delivery/editorial, or method discovery.
- temporary workers: bounded subagents or parallel checks that serve one beat or one lane and then return a summary.
- lane contracts: each standing lane needs `lane_goal`, scope, input fact ledger, output contract, context-reset rule, wake/event triggers, stale/retire conditions, and observability evidence.
- authorization status: user-visible long-running Codex threads and automations need explicit authorization/tool availability; if they are unavailable, keep a manager-owned lane record and continue rather than pretending the lane exists.

Standing lanes and temporary subagents are different resources inside the same control plane. A subagent can help a lane, but it is not a long-running lane. If recurring review or evaluation will be needed across many beats, create or plan a standing review lane early and require clean context or a fresh fact ledger for each review beat.

The contract must include:

- `capability_preflight`: check or state availability for Codex Goal/tool goals, user-visible Codex threads, worktree/background threads, automations/heartbeats, subagents, browser/API/account tools, and project-local scripts.
- `resource_taxonomy`: distinguish user-visible long-running Codex threads from short-lived subagents/workers, automations/heartbeats, and per-round tool Goals. Do not call a subagent a long-running thread.
- `control_plane`: direction, authority, state, topology, routing, and stop conditions.
- `standing_lane_topology`: manager thread, durable lanes, temporary worker pool, lane context-reset policy, lane observability evidence, and stale/retire triggers.
- `authorization_status`: user-owned long threads, automations, account/API actions, external writes, publishing, and irreversible operations need explicit authorization. Short-lived read-only subagents may be used when the user requested subagents/review and the task is low-side-effect.
- `manager_worker_contract`: main thread is the manager; workers/subagents perform bounded work and return summaries. Workers do not complete the global goal or upgrade evidence.
- `beat_router`: every beat ends by selecting and executing or recording one route: `CONTINUE`, `SPAWN_SUBAGENT`, `CREATE_THREAD`, `CREATE_AUTOMATION`, `INTERRUPT_FOR_INPUT`, or `STOP_COMPLETE`.
- `termination_conditions`: goal complete with residual-beat scan clear, true external input missing, permission/account/API missing, no-write/evidence boundary, budget/time/safety limit, or user-only judgment.

`continuous_orchestration_spine`: once the user confirms execution or says to proceed under continuous cadence / orchestration protocol, the prompt-bootstrap waiting boundary is consumed for low-risk reversible work. The runtime must then maintain:

- a short `beat_queue` with the current beat and at least the next plausible low-risk beat
- a fresh `control_plane`, including a valid `standing_lane_topology` when continuous responsibilities recur
- one current `round_goal`
- a per-beat tool Goal when available, otherwise a recorded `protocol_round_goal`
- a `Beat Router` decision that is executed, not merely described
- an observable start signal for the active beat: a compact contract, first action, file touch, command, or explicit degraded-resource note
- `STOP_COMPLETE` only when the objective is complete, validation is clean enough for the delivery contract, and a residual-beat scan finds no useful low-risk internal beat remaining; `INTERRUPT_FOR_INPUT` only when the next required action crosses a real boundary and no lower-risk internal beat remains

Long-running threads, automations, and durable review lanes may mature over the first few beats. The agent must assess their fit and authorization as part of the orchestration spine; it should not treat their absence in beat one as a reason to drop Goal/Plan/Loop, beat routing, or automatic low-risk continuation. If a standing lane is clearly needed but cannot yet be created as a user-visible thread, record `lane_planned_pending_authorization_or_tooling` and continue through the manager-owned lane contract.

`orchestration_watchdog`: resources used for clean-context execution, background work, subagents, review lanes, automations, or user-visible threads must become observable. Activation means a real tool call, thread id, handoff packet, fact-ledger packet, returned summary, file touch, or explicit unavailable/degraded note. If a resource remains active but produces no readable contract, tool action, file change, or result within a reasonable first-beat window, mark it `degraded_or_unobservable`, record the reason, and continue through another available route such as main-thread execution, same-session diagnostic review, a smaller local beat, or `INTERRUPT_FOR_INPUT` only when no safe route remains. Do not describe a planned or silent resource as completed independent review.

`round_prompt_rehydration_gate` applies before each new Plan/Loop in a prompt-based or continuous project. Recover the master prompt or `active_goal_summary`, current state, and `round_goal` into `round_execution_prompt`.

Each round plan must say what comes from:

- master prompt
- prior state
- new judgment
- AI autonomous decision

`continuous_runtime_activation_contract`: when the user prompt or confirmed project prompt selects `连续节拍`, `continuous_until_stopped`, or equivalent wording, continuous cadence is an active execution contract, not a decorative steering word. Each beat must: rehydrate the round prompt, create or record a narrow `round_goal`, run the Loop, score/route, close or migrate the beat, and immediately enter the next low-risk reversible queued beat until a real boundary appears.

`continuous_until_no_issue_stop_rule`: a beat count is never a completion condition. Running 3 beats can be a smoke-test floor, not a stop reason. Before `STOP_COMPLETE`, run a residual-beat scan across the objective, current diff/state, validation gaps, obvious consistency gaps, stale resources, and delivery contract. If any useful low-risk reversible beat remains, route `CONTINUE`; if only optional low-value polish remains, state why it is below the delivery threshold before stopping.

`visible_continuous_runtime_audit`: when continuous cadence is active, the final human-readable answer must expose a compact runtime audit, not hidden machine-board fields. Include each beat's `round_goal` or `protocol_round_goal`, whether a tool Goal was used or why it was not, the executed Beat Router route, whether the next beat auto-started, resource evidence for any subagent/review/thread/automation, validation after the final write, and the final residual-beat scan. If a residual scan triggers another write, re-run validation and residual scan after that write before claiming `STOP_COMPLETE`.

`downstream_activation_reconciliation`: when Complex is applied inside another repository, local `AGENTS.md`, `CONTEXT.md`, current state, stage boards, manifests, no-write boundaries, and manual-action records can narrow how steering words execute. Before concluding that cadence, subagents, review, or tools are active, reconcile each requested steering word with local project boundaries and mark it as `active_now`, `active_but_boundary_blocked`, `overridden_by_project_safety`, or `not_needed_with_reason`.

If the local project declares a true external-input or manual-action boundary, continuous cadence does not mean inventing evidence or bypassing the boundary. It means: execute any allowed residual beat first, such as hard-boundary contradiction repair, submission-friction reduction, non-expansion verification, exact operator handoff, or preflight once the required env var/file exists. Only after those are exhausted may the agent pause, and the pause must name the exact boundary, required file/env var, command, and why no further low-risk internal beat remains.

`per_round_goal_lifecycle_gate`: do not use one long tool Goal for many rounds. Use a narrow per-round goal. If an old tool Goal is stale or blocked while the project can continue, record `stale_or_blocked_tool_goal`, `goal_refresh_gate`, and `protocol_round_goal`; do not declare the whole project blocked.

If a Codex tool Goal is available and the user has requested continuous Complex execution, use it only for the current beat's narrow objective. When that beat completes and the next route is clear, create or record the next `protocol_round_goal` and continue. Do not wait for a new user message merely to start the next beat.

`continuous_cadence_refresh_gate`: refresh tools, topology, goals, and prompt by event trigger first. Three rounds is only a fallback cap.

## 6. Capability And Topology

`capability_discovery_cadence_gate` runs lightly at entry and when events justify it. Consider tools, skills, plugins, connectors, APIs, browsers, accounts, databases, and external methods.

Record capability choices as:

- selected
- rejected
- backlog
- `manual_action_required`

Use `capability_type_and_side_effect_gate` and `external_state_write_guard` for anything that can change external state.

Use `agent_topology_selection_trace` when work may need main-thread execution, temporary subagents, long-running threads, or review lanes. Use `read_only_audit_subagent_contract` for evidence or conformance review.

`long_running_lane_vs_subagent_boundary`: long-running lanes are project responsibilities that persist across beats. Temporary subagents are short-lived workers. Do not satisfy a request for multi-threaded project construction by only mentioning a one-off subagent. For continuous projects, decide the durable lane topology first, then decide whether any lane needs a temporary worker in the current beat.

`topology_auto_activation_policy`: if the confirmed prompt authorizes strong-autonomy Complex execution and the work clearly benefits from temporary subagents, parallel review, or read-only audit, activate the available low-side-effect topology instead of merely recommending it. Ask the user only for user-owned long-thread creation, unavailable tools, account/API access, external writes, or other real authorization boundaries.

`independent_review_context_separation`: same-session roleplay is diagnostic only. True independent review requires clean context, a separate reviewer/thread, read-only audit subagent, different reviewer/model where available, or a fact-ledger-only packet. Track `human_input_drift_risk` when prior conversation may bias judgment.

`review_context_reset_each_round`: every independent review beat must start from a fresh fact-ledger packet or clean reviewer context. Reusing the full prior conversation is allowed only as same-session diagnostic review and must be labeled as such.

## 7. Delivery Contract

Run `deliverable_contract_gate` before output:

- audience
- purpose
- granularity
- tone
- internal-information boundary

Run `reader_translation_gate` for human-facing work. If the user says `只要人看版`, keep machine fields, YAML, verifier internals, and protocol jargon out of the main deliverable.

Keep human-readable delivery and machine recovery notes separate.

## 8. Setup Card And User-Visible Triggers

`complex_setup_question_card` applies when the user only says "use Complex" or "按 Complex 推进".

Ask or default only route-changing choices:

- delivery audience
- project nature
- capability permission
- collaboration topology
- cadence
- autonomy boundary
- manual-action boundary

`user_visible_trigger_guide` means steering words are visible to users, not hidden commands:

- `开启 Plan 模式 / 先规划再执行`
- `先设计提示词/prompt`
- `模型发现型 / 先发散研究框架 / 不要早收敛`
- `证据填充型 / 模型和指标已定`
- `连续节拍 / 总规划别丢 / 每轮 prompt 重水化`
- `多线程/子代理`
- `外部工具 / 账号 / API / skill`
- `少问我 / 能推进就继续 / 我给目录你自己读`
- `独立评审 / 客观审查 / 避免上下文污染`
- `只要人看版`

## 9. Runtime Kit And Evaluation

Runtime templates are optional landing pads, not required protocol fields.

Use filled examples before blank templates:

- evidence fill
- model discovery
- independent review

Behavior regression is the first line of protocol maintenance:

- `docs/behavior-regression-cases.json`
- `docs/behavior-transcript-review-rules.json`
- `tools/check_behavior_regression_pack.py`
- `tools/review_behavior_transcript.py`

Promotion rule:

1. Add or refine a behavior case.
2. Add or refine transcript review rules.
3. Add or refine a golden example.
4. Promote to this core protocol only when repeated/high-impact failures cannot be handled by the first three.

Do not add history archives, long machine-board logs, dated release packages, or one-off recovery records to the active protocol.
