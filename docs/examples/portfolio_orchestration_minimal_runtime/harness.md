# Filled Runtime Harness

## Artifact Contract

- accepted input: records accepted by the evidence boundary and mapping version 3.
- operation: normalize fields into the project-native schema.
- expected artifact: normalized dataset plus verifier result.
- acceptance: schema and invariant checks pass; rejected records remain traceable.
- recovery: distinguish malformed input from invalid mapping assumption; retry only the first.
- state write-back: accepted artifact pointer, mapping version, rejected-record index, and next route.

## Selected Topology

- controller: owns accepted state, work-item routing, and final integration.
- current topology: deterministic Harness for B; no temporary worker or discussion group.
- mechanization level: schema plus checker plus transformation tool contract.
- temporary parallel workers: reserved for independent evidence branches in contested work item A.
- recurring clean evaluator: used for claim work item C because evaluation independence recurs.
- topology resource evidence: manager process, local checker, and clean-review packet paths.

## Legibility And Recovery

- inspectable state: `state.md`, work-item index, artifact contract, checker output, and accepted artifacts.
- mechanical checks: artifact existence, schema, invariants, state write-back, and residual scan.
- route-back trigger: repeated failures trace to changed assumptions or evaluation criteria rather than malformed input.
- checkpoint: after every accepted artifact.
- retry: bounded only for transient tool or malformed-input classes.
- idempotency: stable work-item, input, mapping, and artifact identifiers.
- rollback: restore the last accepted artifact and mapping version.

## State Control

- global projection writer: controller only.
- local writers: each work item updates only its local project-native record and artifact index.
- reconciliation input: one bounded state capsule per affected work item, with source generation/hash and accepted artifact pointer.
- projection update: compare observed generations, reconcile dependencies and acceptance, then write one new versioned portfolio projection.
- contradiction handling: do not use last-write-wins; isolate the dependent route and keep unrelated queued work active.
- projection renewal: checkpoint active state into a fresh epoch when history or version fragmentation makes recovery costly; preserve old history by pointer.
