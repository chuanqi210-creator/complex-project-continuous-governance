# Complex Behavior Review

Purpose: check whether a real agent response followed the Complex behavior kernel, without turning the project back into a thick rule archive.

## Files

- `docs/behavior-regression-cases.json`: canonical behavior cases.
- `docs/behavior-transcript-review-rules.json`: marker groups and human-review questions.
- `docs/mechanism-maturity.json`: mechanism status and promotion/demotion evidence.
- `tools/check_behavior_regression_pack.py`: validates the case/rule structure.
- `tools/review_behavior_transcript.py`: checks one real response or exported transcript against one case.

## Use

Validate rules:

```bash
python3 tools/review_behavior_transcript.py --validate-rules
```

Review a plain-text response:

```bash
python3 tools/review_behavior_transcript.py \
  --case-id setup_card_default \
  --text-file path/to/agent_response.txt
```

Review an exported JSON transcript:

```bash
python3 tools/review_behavior_transcript.py \
  --case-id model_discovery_protect_divergence \
  --json-file path/to/transcript.json
```

Accepted JSON shapes:

- `{ "assistant_response": "..." }`
- `{ "transcript": "..." }`
- `{ "text": "..." }`
- `{ "messages": [{ "role": "user", "content": "..." }, { "role": "assistant", "content": "..." }] }`

## How To Read Results

The script returns:

- `passed`: marker-level pass/fail.
- `required_passed`: how many required marker groups were found.
- `forbidden_results`: forbidden marker hits.
- `human_review_questions`: questions a reviewer should still answer.

Passing means "no obvious marker-level regression." It does not mean the response was excellent.

Each case links to one or more mechanism ids. Use those links to decide whether a failure updates a rule, an example, a transcript marker, or the mechanism maturity status.

Human review still asks:

- Did the response reduce user correction cost?
- Did it choose the right depth for this project?
- Did it preserve the main goal while handling local details?
- Did it avoid asking the user to authorize project-internal work that is inside the responsibility boundary?
- Did it avoid turning Complex into visible process burden?
- Did the environment or artifact satisfy the outcome completion predicate?
- Was the trajectory merely unusual, or did it actually cause an outcome failure?
- Was the failure diagnosed as prompt, context, harness, loop, or model before repair?

## Result Record

Use this compact record for real replies:

```yaml
case_id:
mechanism_ids:
transcript_location:
source_type: real_transcript / redacted_transcript / synthetic_reproduction / end_to_end_project
marker_passed:
human_passed:
outcome_passed:
outcome_evidence:
trajectory_diagnosis:
failure_layer: prompt / context / harness / loop / model / none / uncertain
auto_progressed:
forward_artifact_created:
user_correction_count:
main_failure_if_any:
decision: no_change / update_rule / update_case / update_example / update_maturity / promote_candidate / demote_mechanism
notes:
```

Review outcomes first. Marker and trajectory checks are diagnostics: an unusual path may still be correct, while a marker-rich response may still fail the project outcome.

Do not record raw private transcripts by default. Prefer a redacted summary or a minimal reproduction unless the transcript is safe to publish. See `docs/evals/README.md`.

## Recent Real Feedback

```yaml
case_id: continuous_cadence_same_turn_vs_heartbeat / durable_loop_uses_outcome_completion_and_recovery
transcript_location: Complex self-optimization heartbeat lifecycle, redacted summary, 2026-07-15
source_type: end_to_end_project
marker_passed: yes
human_passed: yes
outcome_passed: yes
auto_progressed: yes, two cross-turn wakes without a user continue message
forward_artifact_created: yes, semantic recovery repair, cross-project fact-ledger harness, and validation evidence
user_correction_count: 0 after heartbeat activation
main_failure_if_any: initial run completed a narrow Goal while a useful next_route remained and had no heartbeat
failure_layer: loop_and_harness_repaired
decision: promote_continuous_cadence_and_four_layer_runtime_to_validated
notes: The repaired heartbeat remained ACTIVE through useful queued beats, resumed the recorded route twice, and was changed to PAUSED by the automation tool only after full checks, independent review, outcome completion, and residual scan found no high-value internal beat.
```

```yaml
case_id: complex_source_resolution_outside_target_repo / independent_review_context_separation
transcript_location: second low-cost anchor-quality rerun with deterministic fact ledger, redacted summary, 2026-07-15
source_type: end_to_end_project
marker_passed: yes
human_passed: yes
outcome_passed: yes
auto_progressed: yes, to bounded state reconciliation
forward_artifact_created: yes, 8,237-byte fact ledger plus clean-context route verdict
user_correction_count: 0
main_failure_if_any: none in the tested extraction-and-evaluation slice
failure_layer: none_observed_in_slice
decision: retain_tested_no_promotion
notes: The deterministic extractor summarized a 372,720-byte status file and 1,635-key manifest in 0.014 seconds, reported match and key overflow, opened no manifest values, and stayed below 10,000 output bytes. A clean evaluator used only that ledger, recovered none of the five fields as authoritative, and selected state reconciliation without recency inference. Independent review then found privacy, hard-output, execution-budget, and overclaim gaps; the extractor now emits a content-minimized ledger without snippets/raw key names/absolute paths/identifiers/fingerprints, stops after match overflow, closes the output-byte loop, and treats overflow as a working-set signal rather than an authority verdict. Follow-up review found no remaining P1/P2 issue in this feature. Cross-project breadth and project-local state compaction remain untested.
```

```yaml
case_id: complex_source_resolution_outside_target_repo
transcript_location: first low-cost anchor-quality rerun, redacted summary, 2026-07-15
source_type: end_to_end_project
marker_passed: partial
human_passed: partial
outcome_passed: partial
auto_progressed: yes, to bounded state reconciliation rather than business execution
forward_artifact_created: yes, four-part anchor verdict and contradiction-preserving route
user_correction_count: 0
main_failure_if_any: The reviewer correctly rejected the newest business route, but its broad status/route term filters emitted thousands of matches, were tool-truncated, and consumed about two minutes before interruption.
failure_layer: context_and_harness
decision: add_measurable_inspection_envelope
notes: Bounded inspection now probes scale first, lists names/types before values, caps first-pass matches/output/time, and treats truncation or overflow as evidence to stop rather than broaden.
```

```yaml
case_id: complex_source_resolution_outside_target_repo / trace_appraisal_hot_warm_cold_compaction
transcript_location: low-cost water-loop clean-context recovery audit, redacted summary, 2026-07-15
source_type: end_to_end_project
marker_passed: partial
human_passed: partial
outcome_passed: partial
auto_progressed: no, a real external field-input boundary was identified
forward_artifact_created: yes, recovery-anchor quality contract and exact non-mutating preflight
user_correction_count: 0
main_failure_if_any: The project had AGENTS, CONTEXT, status, code graph, and manifest entries, but the status was oversized, the manifest exposed more than 1,600 top-level fields, and next-route statements conflicted. The reviewer took over three minutes and selected the newer route without an explicit authority hierarchy.
failure_layer: context_and_harness
decision: update_anchor_acceptance_and_state_reconciliation
notes: Existing recovery files now pass authority, freshness, boundedness, and unique-route checks before use. Oversized or conflicting anchors route to selective status-key reconciliation and Hot State compaction rather than wholesale manifest loading or recency-based selection.
```

```yaml
case_id: complex_source_resolution_outside_target_repo
transcript_location: second NEV clean-context recovery audit, redacted summary, 2026-07-15
source_type: end_to_end_project
marker_passed: partial
human_passed: no
outcome_passed: no
auto_progressed: no
forward_artifact_created: yes, source-priority diagnosis
user_correction_count: 0
main_failure_if_any: The revised reviewer avoided broad target scanning but spent the bounded run rereading Complex references and reached no target file. It also cited Complex's self-maintenance current-state as prior evidence about the target, creating rule-source state pollution.
failure_layer: context
decision: update_progressive_disclosure_and_source_boundary
notes: The loaded complex-runtime skill is now the first-pass rule index. Target durable instructions and recovery anchor come next; deeper core/examples are on demand. Complex protocol/current-state.md is explicitly excluded from target current_basis.
```

```yaml
case_id: complex_source_resolution_outside_target_repo / context_working_set_is_curated_and_recoverable
transcript_location: NEV clean-context read-only recovery audit, redacted summary, 2026-07-15
source_type: end_to_end_project
marker_passed_before_change: partial
human_passed: no on the initial broad pass; yes after bounded rerouting
outcome_passed: partial
auto_progressed: no executable project beat could be proven because the target had no authoritative recovery anchor
forward_artifact_created: yes, cross-project failure diagnosis and bounded-bootstrap contract
user_correction_count: 0
main_failure_if_any: The target repository had no AGENTS, CONTEXT, current-state, controller, or handoff entry. A clean reviewer spent several minutes broad-scanning a large output tree before being interrupted; the only governance-looking plan explicitly disclaimed controller-state authority.
failure_layer: context_and_harness
decision: update_existing_source_resolution_behavior
notes: Complex now resolves a target recovery anchor before recursive scanning. If absent, it performs a bounded root/latest-accepted-artifact bootstrap and keeps proposals outside current_basis. This does not reconstruct the NEV project's missing controller state; it prevents false recovery and unbounded scan cost.
```

```yaml
case_id: context_working_set_is_curated_and_recoverable / independent_review_context_separation
transcript_location: second heartbeat plus clean-context read-only reviewer, redacted summary, 2026-07-15
source_type: real_transcript
marker_passed: yes
human_passed: yes for semantic recovery
outcome_passed: yes for this beat
auto_progressed: yes, second heartbeat wake required no user message
forward_artifact_created: yes, independent recovery audit and compacted single-route Hot State
user_correction_count: 0
main_failure_if_any: The reviewer recovered all five fields explicitly, but found three compatible route statements at different granularities without a declared hierarchy.
failure_layer: context
decision: update_state
notes: Removed the broad duplicate route and converted the previous beat route into a non-routing artifact summary. Current-state now has one authoritative next_route. This validates semantic recovery in this repository only; cross-project transfer and heartbeat self-disable remain open.
```

```yaml
case_id: context_working_set_is_curated_and_recoverable / continuous_cadence_same_turn_vs_heartbeat
transcript_location: first Complex self-optimization heartbeat, redacted summary, 2026-07-15
source_type: real_transcript
marker_passed: partial
human_passed: partial
outcome_passed: partial
auto_progressed: yes, the heartbeat resumed the active task without a user continue message
forward_artifact_created: yes, recovery audit and semantic-recovery verifier contract
user_correction_count: 0 for this wake
main_failure_if_any: Goal, current basis, and next_route were recoverable, but active_module and open_risks had to be inferred from prose rather than read as explicit Hot State fields.
failure_layer: context
decision: update_state_and_verifier
notes: Added explicit thread_goal/current_basis/active_module/open_risks/next_route fields to current-state and made the integrity harness check all five. The first wake is evidence of cross-turn activation, not yet evidence of sustained continuation or full semantic recovery across multiple wakes.
```

```yaml
case_id: continuous_cadence_same_turn_vs_heartbeat / durable_loop_uses_outcome_completion_and_recovery
transcript_location: Complex self-optimization task, redacted summary, 2026-07-15
source_type: real_transcript
marker_passed_before_change: protocol markers existed, but no cross-turn resource evidence was required
human_passed: no
outcome_passed: partial
auto_progressed: same-run no; cross-turn not configured
forward_artifact_created: yes, but the accepted artifact was followed by an unexecuted next_route
user_correction_count: 1
main_failure_if_any: A narrow self-optimization Goal was marked complete after one accepted beat. The response recorded a useful next_route but ended the task and required the user to request continuation. The available Codex heartbeat surface was not activated.
failure_layer: loop_and_harness
decision: update_rule_and_runtime_resource
notes: The existing continuous cadence mechanism was tightened without adding a new gate. Cross-turn cadence now requires actual heartbeat/automation activation plus resource evidence when the tool is callable; an accepted beat no longer completes a longer Goal while residual work remains. An ACTIVE 30-minute thread heartbeat was created; its first autonomous wake remains pending outcome validation.
```

```yaml
case_id: continuous_runtime_activation_after_plan
transcript_location: user-reported downstream run, 2026-07-03
marker_passed_before_change: true for a synthetic bad response that repeated continuous-cadence keywords
marker_passed_after_change: false for the same bad response; true for a minimal response with Beat Router, resource evidence, validation, and residual scan
human_passed: no
user_correction_count: 1
main_failure_if_any: Plan-mode prompt design said continuous cadence, per-beat goals, auto-start, subagents, and context-reset review were defaults, but execution still behaved like plan-only work: no visible per-beat Goal lifecycle, no next-beat auto-start evidence, no automatic low-side-effect topology activation, and no per-review context reset evidence.
decision: update_rule
notes: Tightened continuous_runtime_activation_after_plan to require execution evidence beyond steering-word recall: Beat Router execution, observable resource evidence or named not-needed/degraded boundary, next-beat outcome, validation/residual scan, and explicit rejection of promise-only future activation.
```

```yaml
case_id: orchestration_preflight_contract / continuous_orchestration_runtime_spine
transcript_location: user-reported downstream runs, 2026-07-03
marker_passed_before_change: likely partial; responses could mention threads/subagents while still optimizing a local beat first
marker_passed_after_change: pending real transcript review
human_passed: no
user_correction_count: 1
main_failure_if_any: The agent interpreted multi-threading as optional short-lived subagents. For long-running Complex projects, the first execution beat should form a durable manager/lane topology before local greedy execution: manager thread, standing review/evaluation lane, evidence/data lane, implementation lane, delivery lane, temporary worker pool, context reset policy, and stop conditions.
decision: update_rule
notes: Reframed continuous orchestration around standing lanes. A subagent is a temporary worker, not a long-running project lane. Recurring review/evaluation requires a standing lane or manager-owned lane record with a clean-context/fact-ledger reset policy.
```

```yaml
case_id: plan_mode_is_surface_not_runtime / codex_goal_thread_level_contract / continuous_cadence_same_turn_vs_heartbeat / subagent_explicit_trigger_boundary / standing_lane_record_not_user_thread
transcript_location: user-reported downstream Codex App runs, 2026-07-04
marker_passed_before_change: not applicable; behavior cases did not exist
marker_passed_after_change: pending real transcript review
human_passed: pending
user_correction_count: multiple
main_failure_if_any: Complex language was competing with Codex surfaces. Agents treated Plan mode as if it could be automatically toggled, treated Goal as both long-term continuity and per-beat state, blurred standing lanes with subagents or user-visible threads, and treated cross-turn continuation as possible without heartbeat/automation.
decision: update_case_and_skill
notes: Added codex_surface_alignment, a repo-scoped .agents skill, five behavior cases, and transcript rules. Complex now maps its concepts onto Codex surfaces: Plan mode is a planning surface, Codex Goal is thread_goal / phase_goal, beat_objective is the Complex Plan/Loop target, subagents are short-lived workers, standing lanes are manager-owned responsibilities, and cross-turn continuation uses heartbeat/automation only when available and allowed.
```

```yaml
case_id: portfolio_before_local_greedy_route / audit_guardrail_not_forward_artifact / hot_warm_cold_state_lightening
transcript_location: NEV downstream practice, 2026-07-05
marker_passed_before_change: not applicable; behavior cases did not exist
marker_passed_after_change: pending real transcript review
human_passed: pending
user_correction_count: multiple
main_failure_if_any: The project could run compliant continuous beats while remaining trapped in a local metadata/access/reviewer route. Guardrails passed, but the work did not reliably produce model/data/parameter/writing/branch/topology forward artifacts or maintain a light current operating map.
decision: update_case_and_core
notes: Added portfolio_operating_model, portfolio_before_greedy_route_rule, forward_artifact_acceptance_rule, audit_guardrail_not_engine_rule, parallel_portfolio_routing_rule, and hot_warm_cold_state_rule. Complex now treats long projects as module/lane portfolios rather than a single greedy chain of local beats.
```

```yaml
case_id: trace_appraisal_hot_warm_cold_compaction / external_calibration_before_strategic_decision
transcript_location: user design feedback, 2026-07-05
marker_passed_before_change: not applicable; behavior cases did not exist
marker_passed_after_change: pending real transcript review
human_passed: pending
user_correction_count: 1
main_failure_if_any: Complex had auditability and external-method mapping, but not a strong enough rule that active context must be appraised and compacted after many beats, and that strategic decisions should calibrate against mature external practice before becoming durable protocol behavior.
decision: update_case_and_core
notes: Added trace_appraisal_rule, external_calibration_rule, and hallucination_sentinel. Complex now separates recoverable trace from active context and requires strategic route/model/method/protocol changes to record outside reference basis, transfer limits, unsupported claims, and falsification cues.
```

```yaml
case_id: minimum_viable_closure_for_research / minimum_sufficient_observability_not_overreporting
transcript_location: user reflective practice text, 2026-07-08
marker_passed_before_change: not applicable; behavior cases did not exist
marker_passed_after_change: pending real transcript review
human_passed: pending
user_correction_count: 1
main_failure_if_any: Complex could make long projects auditable, but it did not yet make the attention economy explicit enough: research projects could spend too long on local audits, source gathering, and protocol-compliant work before showing a thin chain from question to evidence/model/result/claim, while heavier progress reporting risked consuming the same attention needed for project movement.
decision: update_case_skill_examples_core
notes: Added minimum_viable_closure_rule, attention_governance, and minimum_sufficient_observability_rule. Routine beats now expose a light progress signal; heavy audit is reserved for trigger points. Research/prototype projects route back if the startup window passes without an end-to-end closure chain.
```

```yaml
case_id: plan_checkpoint_for_key_beats / loop_not_local_greedy / standing_lane_operating_organization / external_calibration_required_for_each_issue / responsibility_boundary_not_low_risk_wording / human_interface_lane_for_long_projects / scheduled_structure_review_continues_project
transcript_location: user design feedback, 2026-07-05
marker_passed_before_change: not applicable; behavior cases did not exist
marker_passed_after_change: pending real transcript review
human_passed: pending
user_correction_count: multiple
main_failure_if_any: The protocol had many correct pieces, but new agents still over-prioritized local Plan output, treated user permission as the driver for next beats, blurred Codex Goal with beat-level work, under-built durable operating lanes, and did not require external mature practice for every mechanism-level fix.
decision: update_case_skill_examples_core
notes: Reframed Complex around thread_goal / phase_goal, beat_objective, planning checkpoints, target-function Loop, operating organization, external calibration for every mechanism-level issue, responsibility boundary wording, human-interface lane, hallucination sentinel, and trace appraisal.
```

Use this compact record for end-to-end project samples:

```yaml
project_type: evidence_fill / model_discovery / mixed / execution_delivery
runtime_records:
behavior_kernel_trace:
transcript_review_case_ids:
user_correction_count:
final_delivery_quality:
remaining_gap:
decision: no_change / update_rule / update_case / update_example / update_maturity / promote_candidate / demote_mechanism
```

## Promotion Rule

If a real transcript fails and the failure is repeated or high-impact:

1. Add or refine a marker group in `docs/behavior-transcript-review-rules.json`.
2. Update the matching behavior case only if expected behavior changed.
3. Add or adjust a filled example if agents need something concrete to imitate.
4. Use external calibration for each mechanism-level fix and write a project micro-contract.
5. Update `docs/mechanism-maturity.json` with the current status and evidence.
6. Promote to `protocol/core.md` only if cases, rules, examples, maturity records, and calibration notes are not enough.
