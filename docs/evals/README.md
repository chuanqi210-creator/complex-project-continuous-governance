# Complex Evals

Complex behavior review should move from "the rule exists" toward "the agent actually behaved better."

Do not commit raw private transcripts by default. Use a redacted summary, a short response excerpt, or a synthetic minimal reproduction unless the source is explicitly safe to publish.

## Review Record

Use this shape for real transcript or end-to-end project reviews:

```yaml
case_id:
mechanism_ids:
source_type: real_transcript / redacted_transcript / synthetic_reproduction / end_to_end_project
transcript_location:
target_project_type: evidence_fill / model_discovery / mixed / execution_delivery
agent_behavior_summary:
marker_passed:
human_passed:
auto_progressed:
forward_artifact_created:
user_correction_count:
main_failure_if_any:
mechanism_maturity_change: none / candidate_to_tested / tested_to_validated / demote / retire
notes:
```

## Human Review Questions

- Did the agent reduce user correction cost?
- Did it continue inside the responsibility boundary without asking for unnecessary permission?
- Did it produce or update a forward artifact?
- Did it preserve the thread or phase goal while choosing the beat objective?
- Did it keep external calibration and hallucination checks proportional?
- Did it avoid turning Complex into visible process burden?

## Evidence Thresholds

Marker pass is only a first screen. A mechanism should not be called `validated` unless real transcript or end-to-end project evidence shows a behavior improvement across more than one relevant run.

The preferred validation unit is a compact project sample:

1. startup or continuation prompt;
2. state recovery;
3. execution beats;
4. forward artifacts;
5. delivery;
6. user correction count;
7. final human judgment.
