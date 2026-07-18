# Context Working Set Template

Use this template to assemble the smallest sufficient context for the next judgment. It is a working set, not a project archive.

## Stable Base

- durable_instruction_sources:
- project_prompt_contract:
- thread_goal_or_phase_goal:
- target_function:
- responsibility_boundary:
- delivery_contract:

## Active Working Set

- target_recovery_anchor_status: authoritative / partial / absent
- target_recovery_anchor_path:
- target_recovery_anchor_authority:
- target_recovery_anchor_freshness:
- target_recovery_anchor_size_and_budget:
- inspection_envelope: matched_names_or_lines / output_bytes / seconds
- inspection_scale_probe:
- inspection_stop_reason: completed_within_budget / match_overflow / output_truncated / timeout
- fact_ledger_content_minimization_and_review_boundary:
- values_opened_after_name_selection:
- authoritative_next_route_count:
- recovery_anchor_contradictions:
- bounded_bootstrap_sources:
- proposal_or_candidate_material_excluded_from_current_state:
- bootstrap_write_mode: create_project_native_anchor / report_missing_fields_read_only
- beat_objective:
- active_module:
- current_basis:
- not_current_basis:
- open_risks:
- unresolved_questions:
- latest_accepted_artifacts:
- current_state_pointer:

## Just-In-Time Retrieval

- warm_index_queries:
- cold_archive_pointers_used:
- retrieved_sources:
- source_timestamp_and_freshness:
- claim_boundary:
- retrieval_reason:

## Reference Implementation Packet

Use only for a mechanism-level external calibration.

- reference_id_and_pinned_revision:
- original_goal_and_non_goals:
- state_and_control_path:
- inspected_code_configuration_tests_evaluations:
- upstream_validation_and_limit:
- operating_constraints_and_failure_boundaries:
- excluded_readme_or_popularity_claims:

## Exclusions

- stale_or_superseded_material:
- noisy_or_low-priority_context:
- rejected_assumptions:
- excluded_tool_results:
- exclusion_reason:

## Tool-Result Lifecycle

- retain_verbatim:
- summarize:
- demote_to_warm_index:
- archive_by_pointer:
- discard_after_validation:

## Context Budget

- highest_attention_items:
- supporting_items:
- optional_items:
- token_or_attention_budget:
- compaction_trigger:
- cache_or_static_prefix_note:

## Recovery Digest

- goal_memory_summary:
- active_module_and_route:
- current_basis_digest:
- open_risks_digest:
- next_route:
- reviewer_context_reset_packet:

## Fidelity Check

After compaction, handoff, or context reset, verify that the next agent can recover:

- Goal and target function;
- current basis and exclusions;
- active module and accepted artifacts;
- open risks and responsibility boundaries;
- next route and completion predicate.

- fidelity_check_result: pass / fail / route_back
- missing_recovery_element:
- repair_route:
