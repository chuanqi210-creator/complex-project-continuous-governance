# Filled Runtime Harness

## Surfaces

- manager: owns portfolio state and integration.
- standing lanes: model/component, literature/data, review/risk, writing/delivery.
- temporary workers: available only for bounded read, extraction, or review packets.
- evaluator: project checks plus clean-context review for important delivery claims.

## Legibility And Guardrails

- inspectable state: `state.md`, module index, branch parking ledger, accepted artifacts.
- mechanical checks: artifact existence, guard result, state/index update, residual scan.
- unavailable capability route: keep the lane contract in manager state and execute the next useful manager beat.

## Recovery

- checkpoint: after every accepted module artifact.
- retry: bounded only for transient tool failure.
- idempotency: stable beat and artifact identifiers.
- rollback: restore last accepted portfolio checkpoint.
