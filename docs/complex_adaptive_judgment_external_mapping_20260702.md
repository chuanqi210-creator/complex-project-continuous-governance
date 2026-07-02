# Complex Adaptive Judgment External Mapping 2026-07-02

Purpose: record which external agent-governance ideas were borrowed for Complex's Adaptive Judgment Layer, what was not borrowed, and how the ideas map into the current protocol. This is a method note, not a new dependency list.

## Core Judgment

Complex already had dynamic routing, project-nature routing, capability discovery, Loop, scoring, and recovery records. The remaining weakness was not lack of rules, but insufficient deep judgment about when to apply them lightly, when to deepen, and when to ask the user.

The new layer therefore adds `adaptive_judgment_controller` above the existing dual profile:

- Evidence-fill work stays efficient and evidence-led.
- Model-discovery work protects divergence and delayed convergence.
- Mixed work can switch weights as the project matures.
- Routine reversible details are handled by the agent.
- Goal, authorization, irreversible action, delivery-public-voice, and high-risk claim changes still return to the user.

## External Method Mapping

| Source | Borrowed idea | Complex mapping | Boundary |
| --- | --- | --- | --- |
| Anthropic Building Effective Agents | Routing, orchestrator-workers, evaluator-optimizer, simplicity, transparency, tool-interface clarity | `adaptive_judgment_controller` chooses route/depth; strategic cases can use worker/reviewer patterns; `route_evaluator_reflection_gate` records route choice and risk | Do not add agent framework dependencies or complex orchestration when a single-thread Loop is enough |
| LangGraph | Durable state, interrupt, human-in-the-loop, resumable control flow | State/recovery records carry continuity; `decision_rights_matrix` decides when to interrupt for user input | Complex remains document/protocol driven; no LangGraph runtime is required |
| OpenAI Agents SDK | Guardrails, handoffs, tracing | Guardrails become ask-user/manual-action boundaries; handoff maps to subagent/thread contracts; tracing maps to route/evidence/recovery records | Do not expose hidden reasoning; record decision summaries, not private chain-of-thought |
| DSPy | Treat prompts and pipelines as optimizable artifacts, not one-off wording | `complex_prompt_bootstrap_gate` and `round_prompt_rehydration_gate` keep prompts refreshable and evaluable across rounds | Do not install DSPy or create optimization jobs unless a future project explicitly needs it |
| Reflexion | Verbal feedback and episodic memory can improve later trials without model fine-tuning | Failures become named gaps, route notes, recovery records, and reusable protocol patterns | Do not store vague self-critique; only durable, testable lessons should be written back |
| Agent evals | Evaluate not only final output, but tool use, transcript/trajectory, state, and regressions | Simulation cases and verification scripts check protocol behavior, route choices, tool boundaries, and recovery quality | Do not make every route decision a heavy eval; use strategic/critical checks and representative simulations |

## Protocol Additions

### `adaptive_judgment_controller`

Inputs:

- `project_nature`
- `convergence_status`
- `current_basis`
- uncertainty and confidence
- reversibility and side effects
- user boundary
- evidence status
- capability status
- collaboration topology
- delivery contract

Outputs:

- `judgment_mode`
- `autonomy_level`
- `decision_right`
- `route_event`
- `confidence_state`
- `ask_user_needed`
- `rollback_or_recovery_route`

Default behavior: the agent may decide reversible, low-side-effect project details by itself. It should not ask the user to adjudicate ordinary tool choice, Loop probe design, evidence depth, temporary subagent split, lightweight keep, or local route-back.

### `decision_rights_matrix`

AI may decide:

- Plan details and sequencing.
- Loop probes and discriminating tests.
- Evidence depth within the already agreed goal.
- Candidate tool/skill selection, rejection, backlog, or local smoke test.
- Temporary subagent or read-only review splits.
- Long-running thread duty micro-adjustments when the main goal and boundaries stay the same.
- Divergence/convergence pacing in model-discovery work.
- Whether a scheduled refresh can be a `lightweight_keep`.

AI must ask or require manual action:

- Main goal or scope change.
- Delivery audience, public voice, or publishable claim change.
- Account, API, paid resource, publishing, submission, external write, or private browser-session action.
- Irreversible file/project operation.
- High-risk real-world action.
- Strong external claim when evidence is below the required level.

### `judgment_depth_ladder`

- `fast`: routine execution, short note if needed.
- `diagnostic`: failures, conflicts, repeated blocks, or stale state.
- `exploratory`: model-discovery or open framing before convergence.
- `strategic`: main-chain, project-nature, topology, tool, or delivery direction changes.
- `critical`: high-risk, external side effects, or formal delivery claims.

### `route_evaluator_reflection_gate`

Use only for strategic or critical judgments. Record:

- selected route
- rejected route
- why selected
- highest misjudgment risk
- counterexample or hostile case
- rollback or recovery route

Routine judgments should stay lightweight. The point is better judgment, not a larger paperwork surface.

## What This Fixes

- Avoids over-asking the user about reversible details.
- Avoids unsafe autonomy around authorization and external side effects.
- Reduces mechanical three-round tool/topology reviews when no event changed.
- Allows model-discovery work to stay exploratory without losing recovery.
- Gives strategic route changes a small self-check without turning every Loop into a form.

## Sources

- Anthropic, "Building effective agents": https://www.anthropic.com/engineering/building-effective-agents
- LangGraph overview: https://docs.langchain.com/oss/python/langgraph/overview
- LangGraph interrupts: https://docs.langchain.com/oss/python/langgraph/interrupts
- OpenAI Agents SDK guardrails: https://openai.github.io/openai-agents-python/guardrails/
- OpenAI Agents SDK handoffs: https://openai.github.io/openai-agents-python/handoffs/
- OpenAI Agents SDK tracing: https://openai.github.io/openai-agents-python/tracing/
- DSPy documentation: https://dspy.ai/
- Reflexion paper: https://arxiv.org/abs/2303.11366
- Anthropic, "Demystifying evals for AI agents": https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
