# State Example: Operating Organization

## Goal Memory

- thread_goal: Run a long research/build project as an organized portfolio, not a single greedy task chain.
- phase_goal: Establish durable lane contracts and first beat queue.
- goal_memory_summary: The manager owns direction and integration; lanes own recurring responsibilities.
- beat_objective: Define lane contracts and choose the first lane to move.

## Lane Contracts

| Lane | Responsibility | Accepted input/output | Wake trigger | Context policy | Manager acceptance | Retire condition | Resource evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Controller | target function, route, stop/park | Hot State + indexes / route decision | every accepted beat or route event | keeps Hot State only | route advances target function | Goal complete | manager-owned record |
| Human interface | responsibility-bearing asks, summaries | controller notes / human-readable decision packet | true responsibility boundary or delivery | excludes raw trace | exact ask or accepted delivery | no open human boundary | manager-owned record |
| Literature/data acquisition | sources, databases, account forecasts | source question / source flow or exact auth ask | unresolved source dependency | source ledger only | provenance and claim boundary pass | source path closed or parked | manager-owned record |
| Model/component | assumptions, variables, vertical slices | model map / model_delta | model uncertainty or interface change | current model ledger | discriminating result or accepted slice | model branch accepted/parked | manager-owned record |
| Data-code | schemas, scripts, hashes | source/data assets / reproducible data_delta | executable data dependency | code/data ledger | test/hash/reproduction pass | data route complete | manager-owned record |
| Review/risk | claims, evidence, overclaim, safety | fact ledger / findings and route-back | claim-sensitive transition | clean context each beat | controller accepts finding disposition | no pending review trigger | clean reviewer resource ID when spawned |
| Writing/delivery | claims, figures, methods, limitations | accepted artifacts / writing_delta | reader-facing deliverable due | current claim scaffold | delivery contract passes | deliverable accepted | manager-owned record |

## External Calibration

- source: Team Topologies; OpenAI Codex Subagents; Codex Automations; Agents SDK handoffs.
- problem_matched: users ask for multi-threading but subagents, standing lanes, and platform threads have different semantics.
- adopted: durable responsibilities plus bounded workers and handoff packets.
- rejected: treating every lane as a visible thread.
- not_transferable: treating a short-lived worker as a durable lane, or claiming a platform thread/automation exists without an observed resource identifier.
- Complex_micro_contract: establish only recurring lane contracts; the manager may activate workers or platform resources when fit is demonstrated, and records their real identifiers/status when created.
- refresh_trigger: lane stale signal, phase switch, handoff, or review contamination.

## Next Route

- next_route: run_lane_fit_check_then_first_vertical_slice
