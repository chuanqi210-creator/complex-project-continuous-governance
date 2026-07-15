# Runtime Harness Template

Use this template when environment, tools, recovery, or observability materially affect execution. Keep routine beats lighter.

## Runtime Surface

- workspace_or_repository:
- worktree_or_isolation:
- thread_or_task_surface:
- automation_or_heartbeat:
- cross_turn_continuation_requested: yes / no
- cross_turn_resource_status: not_needed / heartbeat_created / automation_created / unavailable / responsibility_blocked
- cross_turn_resource_evidence:
- heartbeat_stop_or_disable_condition:
- temporary_worker_or_subagent_capability:
- browser_api_mcp_skills:
- evaluator_surface:

## Capability Contracts

| Capability | Use when | Input | Verifiable output | Side effect | Degraded route |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

- just_in_time_capability_discovery:
- tools_or_skills_intentionally_not_loaded:
- capability_freshness_check:

## Responsibility And Side Effects

- ai_internal_decisions:
- user_responsibility_required_for:
- account_or_payment_boundary:
- publishing_or_external_write_boundary:
- irreversible_or_high-impact_boundary:

## Agent Legibility

- repository_visible_instructions:
- inspectable_state_and_indexes:
- machine-readable_validation:
- logs_metrics_traces:
- stable_task_or_artifact_ids:
- information_still_trapped_in_chat_or_human_memory:
- legibility_repair:

## Mechanical Guardrails

- tests_or_verifiers:
- schemas_or_type_checks:
- lints_hooks_or_structure_checks:
- policy_or_approval_checks:
- evaluator_or_independent_review:
- textual_rule_that_should_become_mechanical:

## Durability And Recovery

- checkpoint_location:
- retryable_failure_classes:
- non_retryable_failure_classes:
- timeout:
- timeout_enforced_by: manager_watchdog / tool_runtime / platform
- worker_self_timeout_is_not_enforcement:
- retry_limit_and_backoff:
- idempotency_key_or_stable_identifier:
- interrupt_resume_safety:
- rollback_or_compensation:
- bounded_concurrency:
- watchdog_or_stall_detection:
- resume_entrypoint:

## Harness Diagnosis

- observed_failure:
- failure_is_harness_related: yes / no / uncertain
- missing_capability_or_interface:
- degraded_route:
- evidence_that_prompt_or_context_is_not_the_primary_failure:
