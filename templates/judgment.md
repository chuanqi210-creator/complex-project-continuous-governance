# Judgment Template

Use this file when the agent needs to decide route, depth, tools, collaboration, convergence pace, external calibration, or whether to ask the user. Keep it short; this is a recovery record, not a long essay.

## Judgment Context

- project_nature:
- convergence_status:
- current_basis:
- codex_surface_alignment:
- thread_goal:
- phase_goal:
- beat_objective:
- decision to make:
- uncertainty_level: low / medium / high
- reversibility: reversible / partly_reversible / irreversible
- side_effect_level: none / local_write / external_read / external_write / account_or_platform_boundary / real_world_action

## Adaptive Judgment

- judgment_mode: fast / diagnostic / exploratory / strategic / critical
- autonomy_level: strong_autonomy_inside_responsibility_boundary / ask_before_strategic_change
- decision_right: ai_decide / ask_user / manual_action_required / blocked_until_responsibility_boundary
- ask_user_needed: yes / no
- ask_user_necessity: necessary / unnecessary / manual_action_required
- unnecessary_user_intervention_reason:
- ai_can_continue_without_user: yes / no
- human_input_drift_risk: low / medium / high
- ai_decided_without_user_reason:
- user_boundary_respected:
- responsibility_boundary_decision:
- planning_checkpoint_decision:
- prompt_rehydration_decision:
- beat_router_decision:
- termination_condition:

## Operating Organization Judgment

- target_function:
- operating_organization_status:
- controller_lane_decision:
- human_interface_lane_decision:
- literature_data_acquisition_lane_decision:
- model_component_lane_decision:
- data_code_lane_decision:
- review_risk_lane_decision:
- writing_delivery_lane_decision:
- standing_lane_vs_subagent_boundary:
- temporary_worker_or_subagent_fit:
- heartbeat_or_automation_decision:
- review_context_reset_decision:

## Portfolio Judgment

- local_route_supports_target_function: yes / no / uncertain
- portfolio_before_greedy_route_rule: passed / route_back / not_needed
- global_bottleneck_claim: true_dependency / local_branch / uncertain
- minimum_viable_closure_status: not_needed / missing / partial / complete / route_back
- closure_gap: question / source_data / model_assumption / result_calculation / figure_table / claim / limitation / output_validation / none
- toil_wip_review_status: healthy / due / route_to_forward_artifact / branch_parking_needed / justified_true_dependency
- forward_artifact_needed_next: model_delta / data_delta / parameter_delta / writing_delta / branch_delta / calibration_delta / state_delta / topology_delta / none
- parallel_portfolio_routing_decision:
- branch_parking_decision:
- hot_warm_cold_state_decision:
- trace_appraisal_decision:

## External Calibration

- external_calibration_decision: not_needed / reuse_fresh / run_now / stale
- source:
- problem_matched:
- adopted:
- rejected:
- not_transferable:
- Complex_micro_contract:
- refresh_trigger:
- hallucination_sentinel_decision:
- unsupported_claim_downgrade:

## Attention Governance

- attention_budget_status: healthy / too_much_process / under_observed / needs_checkpoint
- minimum_sufficient_observability_decision: light_signal / heavier_audit / defer_audit
- progress_signal_needed: closure_segment / forward_artifact / uncertainty_reduction / next_beat / none
- heavy_reporting_trigger: none / phase_switch / public_delivery / claim_upgrade / contradiction / repeated_guardrail_only / missing_closure / external_calibration / hallucination_sentinel / reviewer_handoff / user_requested_audit
- process_to_avoid_this_beat:

## Route Choice

- selected_route:
- rejected_routes:
- why_selected:
- highest_misjudgment_risk:
- counterexample_or_hostile_case:
- rollback_or_recovery_route:

## Follow-Through

- state_update_needed:
- prompt_patch_needed:
- topology_or_capability_change:
- delivery_contract_change:
- next_route:
