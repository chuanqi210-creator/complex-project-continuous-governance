# Progress Loop Template

Use this template for a meaningful cycle that changes project state. The Loop serves the target function; it is not merely the lightest nearby action.

## Loop Contract

- beat_index:
- thread_goal_or_phase_goal:
- goal_memory_summary:
- beat_objective:
- target_function:
- active_module:
- active_work_scope: project / phase / module / work_item
- active_work_nature: evidence_fill / model_discovery / mixed / execution_delivery
- standing_lane:
- project_nature_prior: evidence_fill / model_discovery / mixed / execution_delivery
- loop_type: strategy / discovery / extraction / vertical_slice / closure / review / writing / delivery
- why_not_local_greedy:
- artifact_contract_pointer_or_summary:
- selected_topology: manager_beat / deterministic_harness / temporary_parallel_workers / standing_lane / clean_evaluator / responsibility_handoff
- why_topology_is_smallest_sufficient:
- expected_forward_artifact:
- outcome_completion_predicate:
- relevant_guard:
- executor:
- evaluator:
- evaluator_independence: not_needed / clean_context / fact_ledger / separate_worker / degraded_diagnostic

## Four-Layer Preflight

- prompt_contract_version:
- prompt_rehydration_status:
- context_working_set_status:
- context_fidelity_status:
- runtime_harness_status:
- degraded_capability_route:
- failure_layer_before_execution: none / prompt / context / harness / loop / model / uncertain

## Budget And Durability

- time_budget:
- observed_elapsed_time_or_measurement_unavailable:
- stage_result_horizon_served:
- usable_increment_due_by_horizon:
- contribution_to_stage_increment:
- scope_convergence_route: close_thin_slice / park_peripheral / change_route / reset_appetite / not_needed
- token_or_attention_budget:
- tool_call_budget:
- wip_or_concurrency_limit:
- checkpoint:
- retryable_failure_classes:
- retry_limit_and_backoff:
- idempotency_or_stable_id:
- pause_resume_side_effect_contract:
- rollback_or_compensation:
- watchdog_or_stall_signal:

## Execute And Observe

- action:
- inputs:
- tool_or_method:
- observed_environment_result:
- evidence_or_output_path:
- forward_artifact_type: model_delta / data_delta / parameter_delta / writing_delta / branch_delta / topology_delta / calibration_delta / prompt_delta / context_delta / harness_delta / state_delta / none
- forward_artifact_path:
- guard_result:
- evaluator_result:
- completion_predicate_result: passed / failed / partial / indeterminate

## Diagnose

- outcome_gap:
- trajectory_note:
- failure_layer: prompt / context / harness / loop / model / none / uncertain
- diagnosis_evidence:
- prompt_patch_needed: yes / no
- context_reassembly_needed: yes / no
- harness_repair_or_degrade_needed: yes / no
- loop_route_or_stop_repair_needed: yes / no
- model_limitation_evidence:
- mechanize_stable_judgment: yes / no
- route_deterministic_failure_back_to_judgment: yes / no

## Learn And Route

- uncertainty_reduced_or_exposed:
- cannot_yet_claim:
- new_risk:
- state_or_index_update:
- selected_route: CONTINUE / RETRY / ROUTE_BACK / ROLLBACK / SPAWN_SUBAGENT / CREATE_THREAD / CREATE_AUTOMATION / INTERRUPT_FOR_RESPONSIBILITY / PARK_BRANCH / STOP_COMPLETE
- route_reason:
- next_beat_objective:
- next_route:
- residual_scan:
- minimum_progress_signal_for_human:
- cross_boundary_reconciliation: not_needed / event_triggered / reconciled / degraded
- affected_local_state_capsule_and_generation:
- global_projection_update_or_conflict_route:
- time_convergence_status: on_track / scope_convergence_due / stage_increment_ready / horizon_missed / not_applicable
- stage_delivery_or_replan_artifact:

## Transfer Evaluation

Use only when the beat evaluates an external reference implementation.

- reference_id:
- transfer_status_before_and_after:
- same_task_input_and_measures:
- baseline_result:
- candidate_result:
- comparison_artifacts:
- adopted_rejected_not_transferable:
- rollback_route:
- Complex_validation_records:
- real_complex_validation_still_needed:

## Acceptance

A beat is accepted only when its declared outcome exists: a forward artifact for execution, or a route decision, falsified route, bounded blocker, or parking decision for diagnosis. The relevant guard and evaluator must be satisfied, state/indexes updated, and the next route derived from observed results.

A stage horizon is a delivery and routing boundary, not a completion shortcut. By that horizon, provide a verified usable increment or decision-grade diagnostic. If the intended scope does not fit the remaining appetite, preserve the quality/evidence floor and converge scope instead of silently extending work or lowering acceptance.

- beat_acceptance: accepted / rejected / partial / parked
- acceptance_evidence:
