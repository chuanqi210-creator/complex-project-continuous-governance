# External Production Methods Mapped To Complex

Complex transfers production patterns, not brand names or dependencies. Every mechanism-level change records source, production problem, adopted pattern, rejected pattern, non-transferable boundary, Complex micro-contract, and refresh trigger.

The WeChat article "Prompt 到 Loop 进化" is a useful vocabulary and discovery source. It is not treated as proof that a production pattern works. The evidence anchors below are official documentation, primary research, standards, or mature engineering writeups.

## Prompt Contract

### Versioned, evaluation-driven prompts

- **Sources:** [OpenAI prompt management](https://help.openai.com/en/articles/9824968), [Anthropic prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview), [DSPy](https://dspy.ai/), [Vertex prompt optimizer](https://cloud.google.com/blog/products/ai-machine-learning/announcing-vertex-ai-prompt-optimizer).
- **Production problem:** teams patch prompt wording without a success criterion, evaluation set, version, or rollback path.
- **Adopted:** stable prompt identifiers/versions, explicit variables, linked evaluation cases, observed-failure-driven patches, rollback.
- **Rejected:** optimizing wording before defining success; treating every runtime failure as a prompt defect.
- **Not transferable:** Complex does not require a hosted prompt-management service or automated prompt optimizer.
- **Complex micro-contract:** every prompt patch names the observed instruction failure, linked evaluation, expected behavior change, and rollback condition.
- **Refresh trigger:** a Goal, model surface, output contract, or repeated instruction-level failure changes.

### Static contract, dynamic suffix

- **Sources:** [Anthropic prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching), [tool use with prompt caching](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching).
- **Production problem:** stable instructions are repeatedly mixed with changing state and large tool definitions.
- **Adopted:** stable project contract first, dynamic beat packet later, tools discovered on demand.
- **Rejected:** cache-oriented ordering as a correctness rule.
- **Not transferable:** cache behavior differs by model and platform.
- **Complex micro-contract:** Project Prompt Contract remains stable; changing facts enter Context Working Set and Beat Planning Packet.
- **Refresh trigger:** platform cache semantics or prompt/tool boundaries change.

## Context Working Set

### Minimal sufficient context and just-in-time retrieval

- **Sources:** [Anthropic context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), [OpenAI Codex Skills](https://developers.openai.com/codex/skills), [Lost in the Middle](https://arxiv.org/abs/2307.03172), [LangChain context engineering](https://docs.langchain.com/oss/python/langchain/context-engineering).
- **Production problem:** larger context windows invite context rot, weak prioritization, stale facts, and hidden contradictions.
- **Adopted:** skill-first progressive disclosure, minimal sufficient system instructions, just-in-time retrieval, structured notes, bounded source discovery, tool-result clearing, and explicit exclusions.
- **Rejected:** loading every potentially relevant artifact into each inference.
- **Not transferable:** a universal token threshold or one retrieval policy for all project types.
- **Complex micro-contract:** use the loaded skill as the rule index, resolve target durable instructions and an authoritative recovery anchor before deeper protocol or broad target scanning, exclude Complex maintenance state from target facts, then assemble Hot State, active module, JIT evidence, freshness/provenance, compaction, and exclusions. Bound source inspection mechanically: measure scale first, classify names/types before values, cap matches/output/time, and treat truncation or overflow as a working-set stop signal rather than an authority verdict or an invitation to broaden the search. Repeated large-anchor audits use a deterministic extractor to produce a small content-minimized ledger without source snippets or raw key names; clean-context evaluation consumes the ledger, and the manager enforces hard timeout.
- **Refresh trigger:** project nature, active module, source freshness, or context-window behavior changes.

### Compaction and semantic recovery

- **Sources:** [OpenAI Responses API computer environment](https://openai.com/index/equip-responses-api-computer-environment/), [Anthropic long-running agent harnesses](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents), [OpenHands SDK](https://docs.openhands.dev/sdk/index).
- **Production problem:** compaction saves tokens but may erase intent, open risks, or recovery-critical facts.
- **Adopted:** structured recovery digest, accepted-state pointers, clean handoff, semantic recovery test.
- **Rejected:** treating compaction or file existence as proof of recovery.
- **Not transferable:** a single compaction algorithm across models.
- **Complex micro-contract:** after compaction or handoff, recover Goal, current basis, active module, open risks, and next route before execution.
- **Refresh trigger:** context pollution, reviewer reset, phase handoff, or failed recovery.

## Runtime Harness

### Agent-legible repositories and mechanical invariants

- **Sources:** [OpenAI harness engineering](https://openai.com/index/harness-engineering/), [SWE-agent ACI](https://arxiv.org/abs/2405.15793), [OpenAI running Codex safely](https://openai.com/index/running-codex-safely/).
- **Production problem:** agents cannot inspect the same state, application behavior, logs, metrics, or architectural rules that humans use.
- **Adopted:** repository-legible state, direct observability, narrow tools, worktree isolation, structural tests, lints, and policy checks.
- **Rejected:** relying on long instruction prose when a mechanical check is possible.
- **Not transferable:** repository-specific lint architecture and internal OpenAI infrastructure.
- **Complex micro-contract:** execution and validation facts must be inspectable; repeated enforceable rules become checks before they become more prose.
- **Refresh trigger:** a repeated rule violation, hidden state, or new execution surface appears.

### Durable orchestration and reconciliation

- **Sources:** [OpenAI Symphony](https://openai.com/index/open-source-codex-orchestration-symphony/), [Microsoft Agent Framework Harness](https://learn.microsoft.com/en-us/agent-framework/agents/harness), [Temporal](https://temporal.io/).
- **Production problem:** long-running workers exit, tools fail transiently, state drifts, or duplicate side effects occur.
- **Adopted:** single authoritative orchestration state, isolated workspaces, bounded concurrency, checkpoints, stable identifiers, retry/backoff, idempotency, reconciliation, and observability.
- **Rejected:** assuming a worker exit means the task is complete; unlimited retry; concurrency without ownership.
- **Not transferable:** Complex does not require a daemon, Temporal server, or Microsoft runtime.
- **Complex micro-contract:** important harnesses declare checkpoint, retry class, backoff, idempotency/compensation, bounded concurrency, and degraded route.
- **Refresh trigger:** transient failures repeat, duplicate work occurs, or cross-turn continuation is added.

### Interrupt and resume side-effect safety

- **Sources:** [LangGraph interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts), [Temporal Activity Definition](https://docs.temporal.io/activity-definition).
- **Production problem:** human approval, external input, or retry can resume a workflow after partial work; if non-idempotent side effects happened before the pause, resume can duplicate records, overwrite state, or charge twice.
- **Adopted:** pause before non-idempotent external writes; keep pre-approval work read-only, local, draft, idempotent, reversible, or compensatable; record checkpoint, idempotency key or stable identifier, approval payload, and resume route.
- **Rejected:** importing LangGraph or Temporal as a required runtime; treating every user question as a durable interrupt; adding heavy transaction ceremony to read-only beats.
- **Not transferable:** Complex cannot guarantee platform-level exactly-once execution without a supporting runtime; it can only require agent-visible contracts and safe sequencing.
- **Complex micro-contract:** `interrupt_resume_safety` applies when a beat must pause for authorization or external input: non-idempotent side effects move after approval, or the beat records idempotency/rollback/compensation evidence before it can retry or resume.
- **Refresh trigger:** new approval surfaces, external-write tools, retryable background work, or duplicate side-effect failures.

### Explicit multi-agent organization

- **Sources:** [OpenAI Codex subagents](https://developers.openai.com/codex/subagents), [OpenAI Agents SDK handoffs](https://openai.github.io/openai-agents-python/handoffs/), [Microsoft orchestration patterns](https://learn.microsoft.com/en-us/agent-framework/workflows/orchestrations/), [Team Topologies](https://teamtopologies.com/key-concepts).
- **Production problem:** threads, workers, and durable responsibilities are conflated, creating unclear ownership and polluted review.
- **Adopted:** manager ownership, bounded worker contracts, durable responsibility lanes, clean-context evaluators, explicit handoff packets.
- **Rejected:** creating agents for every small task or calling a subagent a standing lane.
- **Not transferable:** organization design must fit project scale and available Codex surfaces.
- **Complex micro-contract:** controller owns integration; standing lanes own recurring responsibility; workers return bounded artifacts and summaries.
- **Refresh trigger:** recurring responsibility, reviewer contamination, or topology drift appears.

## Progress Loop

### Outcome-based completion and evaluator separation

- **Sources:** [Anthropic harness design for long-running apps](https://www.anthropic.com/engineering/harness-design-long-running-apps), [Anthropic agent evals](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents), [Microsoft Agent Framework LoopEvaluator](https://learn.microsoft.com/en-us/agent-framework/agents/harness).
- **Production problem:** agents stop because they produced text, completed a fixed number of turns, or self-reported success.
- **Adopted:** negotiate completion before execution, evaluate the actual environment or artifact, separate evaluator for important work, outcome-first grading.
- **Rejected:** exact trajectory matching as the primary definition of success.
- **Not transferable:** every small beat does not need an independent model evaluator.
- **Complex micro-contract:** every important Loop has an outcome predicate, evaluator, accepted artifact, and next route from observed results.
- **Refresh trigger:** false completion, evaluator disagreement, or path overfitting appears.

### Target-function iteration instead of local greed

- **Sources:** [CRISP-DM](https://www.ibm.com/docs/it/SS3RA7_18.3.0/pdf/ModelerCRISPDM.pdf), [NASA Systems Engineering Handbook](https://www.nasa.gov/wp-content/uploads/2018/09/nasa_systems_engineering_handbook_0.pdf), [Google SRE eliminating toil](https://sre.google/sre-book/eliminating-toil/).
- **Production problem:** repeated local checks, audits, or evidence collection consume work without closing the project chain.
- **Adopted:** target-function feedback, entry/success criteria, early end-to-end slice, toil/WIP review, branch parking.
- **Rejected:** heavyweight stage ceremonies for every small beat.
- **Not transferable:** fixed review cadence regardless of project events.
- **Complex micro-contract:** each Loop names target function, module, lane, forward artifact, completion predicate, and non-greedy rationale.
- **Refresh trigger:** guardrail-only repetition, missing early closure, or module bottleneck changes.

## Cross-Layer Diagnosis

The central transfer rule is diagnostic:

1. capture the failed outcome and relevant trajectory;
2. classify Prompt, Context, Harness, Loop, or model limitation;
3. repair the failed layer;
4. add an evaluation case;
5. update prompt defaults only for instruction-level failures.

This prevents context omissions, unavailable tools, poor recovery, and incorrect stopping logic from turning into an ever-longer prompt.

## Evidence Boundary

External production sources show that a pattern has precedent and clarify its transfer boundary. They do not prove the Complex implementation improves user outcomes. `docs/mechanism-maturity.json` records that distinction, and real transcript or end-to-end project evidence is required for promotion.
