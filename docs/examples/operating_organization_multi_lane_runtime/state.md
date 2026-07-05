# State Example: Operating Organization

## Goal Memory

- thread_goal: Run a long research/build project as an organized portfolio, not a single greedy task chain.
- phase_goal: Establish durable lane contracts and first beat queue.
- goal_memory_summary: The manager owns direction and integration; lanes own recurring responsibilities.
- beat_objective: Define lane contracts and choose the first lane to move.

## Lane Contracts

| Lane | Responsibility | Input | Output | Context Reset |
| --- | --- | --- | --- | --- |
| Controller | target function, route, stop/park | Hot State, indexes | Beat Router decision | keeps Hot State only |
| Human interface | responsibility-bearing asks, summaries | controller notes | concise human-readable output | excludes raw trace |
| Literature/data acquisition | sources, databases, account forecasts | source questions | source flow, no-hit, exact auth asks | source ledger only |
| Model/component | model assumptions, variables, vertical slices | current model map | model_delta | current model ledger |
| Data-code | schemas, scripts, hashes | source/data assets | data_delta, reproducibility note | code/data ledger |
| Review/risk | claims, evidence, overclaim, safety | fact ledger | findings and route-back | clean context each beat |
| Writing/delivery | claims, figures, methods, limitations | accepted artifacts | writing_delta | current claim scaffold |

## External Calibration

- source: Team Topologies; OpenAI Codex Subagents; Codex Automations; Agents SDK handoffs.
- problem_matched: users ask for multi-threading but subagents, standing lanes, and platform threads have different semantics.
- adopted: durable responsibilities plus bounded workers and handoff packets.
- rejected: treating every lane as a visible thread.
- not_transferable: assuming subagents spawn without explicit/clear prompt authorization.
- Complex_micro_contract: first continuous beat establishes lane contracts; later beats may activate workers or platform resources only when useful and authorized.
- refresh_trigger: lane stale signal, phase switch, handoff, or review contamination.

## Next Route

- next_route: run_lane_fit_check_then_first_vertical_slice

