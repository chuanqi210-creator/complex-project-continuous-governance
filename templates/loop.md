# Progress Loop Template

Use this template for a meaningful cycle that changes project state. The Loop serves the target function; it is not merely the lightest nearby action.

## Loop Contract

- beat_index:
- thread_goal_or_phase_goal:
- goal_memory_summary:
- beat_objective:
- target_function:
- active_module:
- standing_lane:
- project_nature: evidence_fill / model_discovery / mixed / execution_delivery
- loop_type: strategy / discovery / extraction / vertical_slice / closure / review / writing / delivery
- why_not_local_greedy:
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
- token_or_attention_budget:
- tool_call_budget:
- wip_or_concurrency_limit:
- checkpoint:
- retryable_failure_classes:
- retry_limit_and_backoff:
- idempotency_or_stable_id:
- interrupt_resume_safety:
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

## Acceptance

A beat is accepted only when the forward artifact or explicit branch decision exists, the guard and evaluator are satisfied at the required level, state/indexes are updated, and the next route follows from observed results.

- beat_acceptance: accepted / rejected / partial / parked
- acceptance_evidence:
