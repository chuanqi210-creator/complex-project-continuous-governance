# Complex Behavior Review

Purpose: check whether a real agent response followed the Complex behavior kernel, without turning the project back into a thick rule archive.

## Files

- `docs/behavior-regression-cases.json`: canonical behavior cases.
- `docs/behavior-transcript-review-rules.json`: marker groups and human-review questions.
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

Human review still asks:

- Did the response reduce user correction cost?
- Did it choose the right depth for this project?
- Did it preserve the main goal while handling local details?
- Did it avoid asking the user to authorize project-internal work that is inside the responsibility boundary?
- Did it avoid turning Complex into visible process burden?

## Result Record

Use this compact record for real replies:

```yaml
case_id:
transcript_location:
marker_passed:
human_passed:
user_correction_count:
main_failure_if_any:
decision: no_change / update_rule / update_case / update_example / promote_candidate
notes:
```

## Recent Real Feedback

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
decision: no_change / update_rule / update_case / update_example / promote_candidate
```

## Promotion Rule

If a real transcript fails and the failure is repeated or high-impact:

1. Add or refine a marker group in `docs/behavior-transcript-review-rules.json`.
2. Update the matching behavior case only if expected behavior changed.
3. Add or adjust a golden example if agents need something concrete to imitate.
4. Use external calibration for each mechanism-level fix and write a project micro-contract.
5. Promote to `protocol/core.md` only if cases, rules, examples, and calibration notes are not enough.
