# Prompt Contract Template

Use this template to separate durable project intent from changing beat context. Do not copy the complete Complex protocol into a project prompt.

## High-Fit User Request

```text
请先读取已安装的 Complex，并结合当前项目设计 Project Prompt Contract。请区分稳定目标与动态上下文，说明项目性质、担责边界、完成标准、评价方法和交付对象。随后按 Context Working Set、Runtime Harness 和 Progress Loop 组织连续推进；能在担责边界内继续时自动进入下一拍。
```

## Project Prompt Contract

When a material framework fork exists, derive this contract from an accepted Framework Decision Contract. Do not make the user repeat resolved decisions.

- prompt_id:
- prompt_version:
- previous_version_or_rollback_pointer:
- thread_goal:
- phase_goal:
- target_function:
- completion_criteria:
- outcome_evaluation:
- time_appetite:
- next_stage_result_horizon:
- smallest_useful_stage_artifact:
- stage_artifact_audience_and_acceptance:
- quality_evidence_and_claim_floor:
- scope_convergence_rule:
- project_nature_prior: evidence_fill / model_discovery / mixed / execution_delivery
- responsibility_boundary:
- delivery_contract:
- stable_project_constraints:
- variables:
- model_or_codex_surface_assumptions:
- known_failure_examples:
- Complex_skill_or_protocol_reference:

## Framework Decision Contract Reference

- framework_grilling_status: complete / no_grill_needed / waiting_on_user_owned_decision
- decision_contract_pointer_or_digest:
- accepted_goal_architecture_and_evaluation_decisions:
- rejected_alternatives:
- unresolved_empirical_questions:
- reopen_trigger:

The contract should remain stable across beats. Current files, temporary tool results, and changing module details belong in `context.md` or state.

## Prompt Design Evidence

- observed_instruction_failure_or_changed_goal:
- linked_behavior_case_or_transcript:
- failure_layer: prompt / context / harness / loop / model
- why_prompt_change_is_the_right_layer:
- alternatives_rejected:
- expected_behavior_change:
- evaluation_case:
- rollback_condition:

Do not patch the prompt when the actual failure is missing context, an unavailable tool, poor observability, stale state, or incorrect Loop completion.

## Beat Planning Packet

Assemble this before a planning checkpoint or continuous beat:

- beat_index:
- inherited_prompt_version:
- goal_memory_summary:
- current_context_packet:
- harness_status_and_degraded_routes:
- beat_objective:
- target_function_and_module_served:
- active_work_scope_and_nature:
- artifact_contract:
- selected_topology_and_fit_reason:
- standing_lane_served:
- candidate_routes:
- selected_route_and_reason:
- outcome_completion_predicate:
- evaluator_or_guard:
- forward_artifact:
- retry_or_recovery_route:
- beat_timebox_or_execution_budget:
- stage_result_horizon_served:
- contribution_to_usable_stage_increment:
- scope_convergence_if_over_budget:
- next_route_if_accepted:

## Prompt Rehydration

Before each beat:

1. Load the confirmed Project Prompt Contract.
2. Restore accepted state and `goal_memory_summary`.
3. Assemble the current Context Working Set by pointer.
4. Confirm Runtime Harness capability and responsibility boundaries.
5. Add only the current `beat_objective`, completion predicate, and route.
6. Preserve the master Goal unless the user explicitly changes it.

User details normally patch the current beat or delivery contract. They rewrite the Project Prompt Contract only when they change the Goal, responsibility boundary, stable constraint, or completion criteria.

## Compact Continuation Prompt

```text
继续按 Complex 推进。恢复 Project Prompt Contract 和已接受状态，组装当前 Context Working Set，确认 Runtime Harness 与降级路线，然后建立本拍 beat_objective 和 outcome completion predicate。运行 Progress Loop，以环境结果和 forward artifact 验收；可继续时自动进入下一拍，只在真实担责边界或不可恢复阻塞处暂停。输出只要人看版。
```
