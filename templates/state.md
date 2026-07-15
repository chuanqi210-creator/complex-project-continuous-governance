# Runtime State Template

Use this file to make a Complex project resumable. Keep Hot State short enough that a later agent can recover without rereading every artifact.

## Project Snapshot

- Project:
- Current stage:
- Current route:
- beat_index:
- current project version or milestone:
- Last updated:
- Owner or manager thread:

## Goal Memory

- thread_goal:
- phase_goal:
- goal_memory_summary:
- current_beat_objective:
- next_route:
- completion_criteria:
- stop_conditions:

## Four-Layer Runtime Snapshot

- prompt_contract_version:
- prompt_contract_location:
- context_working_set_location:
- context_fidelity_status: pass / fail / route_back / not_checked
- context_exclusions:
- runtime_harness_location:
- harness_status: ready / degraded / blocked / not_needed
- progress_loop_location:
- current_failure_layer: prompt / context / harness / loop / model / none / uncertain
- four_layer_runtime_alignment_status: pending / active / reviewed / route_back

## Project Nature

- project_nature: evidence_fill / model_discovery / mixed / execution_delivery
- convergence_status: divergent / candidate_pool_ready / provisionally_converged / evidence_fill_ready / execution_ready
- project_nature_router_status: pending / complete / route_back
- anti_premature_convergence_status: not_needed / active / passed / route_back
- candidate_frameworks:
- divergence_budget:
- discriminating_probe:
- convergence_switch_conditions:
- current scoring profile:

## Operating Organization

- operating_organization_status: not_needed / pending / active / stale / route_back
- target_function:
- controller_lane:
- human_interface_lane:
- literature_data_acquisition_lane:
- model_component_lane:
- data_code_lane:
- review_risk_lane:
- writing_delivery_lane:
- lane_context_reset_policy:
- lane_observability_evidence:
- lane_stale_or_retire_trigger:
- temporary_worker_pool:
- user_visible_resource_status:

## Portfolio Operating Model

- portfolio_operating_model_status: not_needed / pending / active / stale / route_back
- module_portfolio:
- module_status_index:
- standing_lane_portfolio:
- forward_artifact_index:
- branch_parking_ledger:
- data_asset_or_evidence_index:
- parameter_candidate_ledger:
- writing_scaffold_index:
- current_forward_artifact_types: model_delta / data_delta / parameter_delta / writing_delta / branch_delta / calibration_delta / state_delta / topology_delta / none
- guardrail_only_streak:
- toil_wip_review_status: healthy / due / route_to_artifact / branch_parking_needed / justified_true_dependency
- parallel_portfolio_routing_status: not_needed / active / route_to_parallel_module / blocked
- current_global_bottleneck_candidate:
- bottleneck_is_true_global_dependency: yes / no / uncertain

## Attention Governance And Closure

- attention_governance_status: healthy / under_observed / over_governed / review_due
- minimum_viable_closure_status: not_needed / missing / partial / complete / stale
- closure_chain:
  - question_or_problem:
  - source_data_or_input_path:
  - minimal_model_or_assumption:
  - result_or_output:
  - figure_table_or_validation_signal:
  - claim_or_usable_conclusion:
  - limitation:
  - next_weakness:
- startup_window_status: within_window / closure_due / overdue / justified_prework
- minimum_sufficient_observability_status: light_signal_enough / heavier_audit_due / too_much_reporting
- last_progress_signal:
- heavy_audit_trigger:
- process_overhead_risk: low / medium / high

## State Lightening

- hot_state_location:
- warm_index_locations:
- cold_archive_policy:
- trace_appraisal_status: not_needed / due / complete / stale
- trace_retention_classes:
- demoted_to_cold_archive:
- active_context_size_risk: low / medium / high

## External Calibration

- external_calibration_status: not_needed / fresh / due / stale / complete
- source:
- problem_matched:
- adopted:
- rejected:
- not_transferable:
- Complex_micro_contract:
- refresh_trigger:
- external_calibration_required_for_each_issue_status:

## Hallucination Sentinel

- hallucination_sentinel_status: not_needed / due / complete / route_back
- current_basis:
- external_basis:
- inference:
- unsupported_claim:
- falsification_cue:

## Adaptive Judgment

- judgment_mode: fast / diagnostic / exploratory / strategic / critical
- autonomy_level: strong_autonomy_inside_responsibility_boundary / ask_before_strategic_change
- decision_right: ai_decide / ask_user / manual_action_required / blocked_until_responsibility_boundary
- ask_user_needed: yes / no
- ask_user_necessity: necessary / unnecessary / manual_action_required
- ai_can_continue_without_user: yes / no
- human_input_drift_risk: low / medium / high
- ai_decided_without_user_reason:
- rollback_or_recovery_route:
- route_evaluator_reflection_status: not_needed / pending / complete

## Responsibility Boundary

- ai_auto_continue_allowed:
- known_next_step_auto_execute_rule: applicable / not_applicable / blocked_by_responsibility_boundary
- unnecessary_user_intervention_reason:
- must_ask_user_for:
- manual_action_required_for:
- context_pointers_user_provided:
- materials_ai_should_read_itself:
- user_input_classification: fact / preference / responsibility_boundary / local_correction / goal_change / noise_or_possible_misleading
- independent_review_context_separation: not_needed / required / degraded_to_same_session_diagnostic
- downstream_activation_reconciliation: not_needed / pending / complete
- local_boundary_effect_on_steering_words:
- residual_auto_beat_available: yes / no
- residual_auto_beat_type: boundary_contradiction_repair / submission_friction_reduction / non_expansion_verification / exact_operator_handoff / preflight_after_env_var / none

## Codex Surface And Cadence

- codex_surface_alignment_status: pending / complete / route_back
- plan_mode_surface_status: user_enabled / remind_user / planning_checkpoint / not_needed
- codex_goal_surface_status: thread_goal_fit / phase_goal_fit / not_needed / unavailable / stale
- thread_heartbeat_or_automation_status: not_needed / planned / available / unavailable / blocked_by_responsibility_boundary
- continuous_cadence_status: inactive / active / paused_by_boundary / stop_complete
- beat_queue:
- current_beat_objective_source: codex_goal / protocol_record / planning_checkpoint
- planning_checkpoint_status: not_needed / due / complete
- prompt_rehydration_status: not_needed / needs_rehydration / rehydrated / route_back_to_state_recovery
- last_prompt_refresh_beat:
- Beat Router decision: CONTINUE / SPAWN_SUBAGENT / CREATE_THREAD / CREATE_AUTOMATION / INTERRUPT_FOR_INPUT / STOP_COMPLETE
- termination_condition:

## Capability State

- selected now:
- rejected now:
- backlog:
- manual action:
- event_triggered_capability_refresh: due / lightweight_keep / completed / blocked
- refresh trigger:
- next capability review or fallback cap:

## Current Basis

Accepted as current basis:

-

Not current basis:

-

Unknown or stale:

-

## Open Questions

-

## Current Decisions

-

## Next Route

- next_route:
- route_reason:
- topology_refresh_due:
- capability_refresh_due:
- manual_action_required:
- next review trigger:

## Recovery Notes

- Files or links to read first:
- Files or links to ignore unless doing history comparison:
- Recent validation or QA evidence:
