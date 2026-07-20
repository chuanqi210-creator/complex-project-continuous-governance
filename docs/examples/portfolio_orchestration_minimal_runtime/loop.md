# Filled Progress Loop: Adaptive Work Topology

## Contract

- beat_objective: Transform one bounded batch for work item B and classify any failure without changing the project-level prior.
- project_nature_prior: mixed.
- active_work_scope: work_item.
- active_work_nature: execution_delivery.
- active_module: B, stable record transformation.
- selected_topology: deterministic Harness.
- why_topology_is_smallest_sufficient: the input, mapping, output schema, and verifier are stable; parallel discussion would add coordination without information gain.
- expected_forward_artifact: normalized batch, rejected-record index, verifier result, and accepted-state update.
- outcome_completion_predicate: the batch is transformed, every record is accepted or explicitly rejected, the verifier passes, and the next route is derived from the observed failure class.
- evaluator: project-native verifier; clean reviewer is not needed for this mechanical beat.
- why_not_local_greedy: B advances the thin end-to-end closure and is not blocked by unresolved work item A.

## Observe, Diagnose, And Route

- if passed: accept the artifact, update state, and route to the next portfolio item.
- if malformed input: isolate the record, apply bounded retry or rejection, and preserve the mapping.
- if changed assumption: stop mechanical retry and route the affected rule to work item A for model discovery.
- mechanize_stable_judgment: allowed only after repeated stable acceptance and low disagreement.
- completion_predicate_result: pending execution in a real project.
- next_route: run_work_item_B_and_route_result.
