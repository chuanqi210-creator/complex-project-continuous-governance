# External Production Methods Mapped To Complex

Complex transfers bounded reference implementations, not brand names or dependencies. Every mechanism-level change moves through discovery, pinned implementation inspection, bounded reproduction, same-task comparison, reversible transfer, and Complex-side validation. It records the original goal/non-goals, code/configuration/tests/evaluation evidence, upstream limits, production problem, adopted pattern, rejected pattern, non-transferable boundary, Complex micro-contract, rollback, next validation, and refresh trigger.

The WeChat article "Prompt 到 Loop 进化" is a useful vocabulary and discovery source. It is not treated as proof that a production pattern works. The evidence anchors below are official documentation, primary research, standards, or mature engineering writeups.

## Reference Implementation Transfer Standard

Popularity is a candidate-discovery signal only. A source becomes implementation evidence only after a fixed revision and concrete operating path have been inspected. Before same-task comparison, it may inform only a reversible provisional experiment with explicit rollback; it is not yet a transferred mechanism. A transfer becomes Complex evidence only after bounded reproduction or a justified unreproduced record, same-task comparison, and Complex-side testing.

| Status | Evidence required | What may be claimed |
| --- | --- | --- |
| `discovered` | relevant project or paper found | candidate exists |
| `implementation_inspected` | pinned revision plus code/config/tests/evals/control/state inspection | mechanism and limits are understood |
| `reproduced` | local fixture, command, and result | bounded upstream behavior ran locally |
| `comparatively_evaluated` | candidate and Complex baseline on the same input and measures | relative behavior on that task |
| `transferred` | bounded Complex change, rollback, and evaluation evidence | mechanism is implemented in Complex |
| `validated_in_complex` | repeated real transcripts or end-to-end project improvement | transfer improves Complex within the observed scope |

The machine-readable evidence is in `docs/reference-implementation-evidence.json`; its fixtures live in `docs/evals/`. Daily project beats reuse fresh records and do not repeat this research mechanically.

## Pinned Implementation Portfolio

| Layer | Reference implementation | Concrete mechanism inspected | Transfer boundary |
| --- | --- | --- | --- |
| Prompt/Loop | DSPy | development set, metric, baseline, optimizer compile/search | no optimizer without task data, metric, and model-call budget |
| Prompt/Harness/Loop | promptfoo | declarative provider/test/assertion matrix and logged-output evaluation | marker assertions do not prove project quality |
| Context/Harness | Mem0 | pinned OSS add path is additive with exact-hash dedup; update/delete are explicit APIs | memory lifecycle does not resolve project evidence authority, contradiction, or supersession |
| Context/Harness/Loop | LangGraph | typed state transitions and executable checkpoint conformance | no mandatory workflow-engine dependency |
| Harness/Loop | OpenAI Symphony | one controller state, reconcile-before-dispatch, continuation check, bounded backoff, snapshots | tracker-centric coding workflow is not a universal project model |
| Context/Loop | Ralph | fresh process per iteration with durable file/Git state | self-reported completion and fixed-iteration stop are rejected |
| Harness/Loop | SWE-agent | explicit tool/history/environment/trajectory/retry/reviewer contracts | benchmark-specific tools and patch assumptions do not generalize |
| Prompt/Harness/Loop | OpenAI Codex | thread/turn/item, persisted Goal, approvals, skills, sandbox and runtime capabilities | experimental RPCs and Complex conventions are not universal Codex primitives |
| Harness | OpenAI Agents SDK HITL | approval is attached to the exact tool call, serialized in run state, then resumed | framework approval objects do not create authority or exactly-once semantics outside that runtime |
| Prompt/Context | Kubernetes website | reader-oriented content types, canonical source, style/build/review discipline | Hugo, localization and SIG governance are not imported |
| Prompt/Harness/Loop | Rust RFCs | substantial-change threshold, alternatives, drawbacks, compatibility and disposition | no RFC ceremony for routine edits and no active-tree archive |
| Context/Harness/Loop | Inspect AI | task, run, scorer, limits, logs, retries and re-scoring as separate contracts | no framework dependency and no automated-score supremacy |
| Prompt/Context/Harness/Loop | Kubernetes KEPs | enhancement threshold, goals/non-goals, production-readiness, testing, graduation, rollback and implementation history | no KEP ceremony, SIG governance or release train for ordinary edits |
| Harness/Loop | Argo Rollouts | stable/candidate state, bounded exposure, metric analysis, promotion, abort and rollback | no Kubernetes dependency or fixed rollout percentages for protocol maintenance |
| Prompt/Context | Matt Pocock Grilling | inspect facts, ask one consequential question with a recommendation, preserve a decision artifact | no exhaustive interview or transfer of reversible AI-owned choices to the user |

Two bounded mechanisms are currently reproduced locally: promptfoo's zero-cost logged-output provider/assertion smoke and LangGraph's five required checkpoint capabilities. The promptfoo smoke is not a same-input baseline-versus-candidate matrix. Neither reproduction validates a Complex outcome. The other thirteen references remain `implementation_inspected` until their next validation is economically and semantically justified.

## Repository-wide Re-baseline

The 2026-07-17 re-baseline applies these implementations to four objects rather than adding four more runtime gates:

- runtime architecture: Codex, Symphony, LangGraph, Ralph and SWE-agent;
- public language: Kubernetes documentation and Codex skills;
- change governance: Rust RFCs and Kubernetes KEPs;
- evaluation and candidate rollout: Inspect AI, promptfoo and Argo Rollouts.

The resulting keep/merge/demote decisions and next validations are machine-readable in `docs/active-architecture-rebaseline.json`.

## Prompt Contract

### High-leverage framework grilling

- **Source:** [`mattpocock/skills` Grill Me and Grilling, v1.1.0](https://github.com/mattpocock/skills/releases/tag/v1.1.0), commit `d574778f94cf620fcc8ce741584093bc650a61d3`.
- **Implementation observation:** the user-invoked `grill-me` wrapper delegates to one reusable `grilling` primitive. That primitive walks a decision tree one question at a time, gives a recommended answer, looks up facts in the codebase, and waits for shared understanding before enactment. The v1.1.0 release explicitly separated discoverable facts from human decisions.
- **Production problem:** an agent begins implementation while the project destination is still ambiguous, or compensates by asking a long list of low-value questions whose answers are already available or safely delegable.
- **Adopted:** one-question-at-a-time decision-tree traversal, fact lookup before asking, recommended answers, explicit consequences, and a durable decision artifact before the Project Prompt Contract.
- **Rejected:** relentless coverage of every imaginable branch, treating all design decisions as human-owned, and requiring confirmation when no material fork remains.
- **Not transferable:** repository popularity and upstream user adoption do not establish that the Complex adaptation improves project outcomes; the source is a compact interaction skill, not a long-project governance system.
- **Complex micro-contract:** at project start or strategic reframe, ask only when two plausible user-owned answers materially alter Goal, target function, architecture, responsibility, or evaluation and cannot be resolved from facts or a bounded probe. Otherwise record `no_grill_needed` and continue.
- **Refresh trigger:** framework misalignment causes substantial rework, users report ceremonial or foolish questions, or the upstream Grilling contract changes.

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
- **Adopted:** versioned authoritative recovery digest, accepted-state and supersession pointers, clean handoff, semantic recovery test, and an explicit degraded route for broken pointers.
- **Rejected:** treating compaction or file existence as proof of recovery.
- **Not transferable:** a single compaction algorithm across models.
- **Complex micro-contract:** after compaction or handoff, recover Goal, current basis, active module, open risks, and next route before execution; if an accepted pointer is broken or contradictory, route to reconciliation instead of guessing.
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

- **Sources:** [OpenAI Symphony](https://openai.com/index/open-source-codex-orchestration-symphony/), [Kubernetes controller pattern](https://kubernetes.io/docs/concepts/architecture/controller/), [Magentic-One](https://www.microsoft.com/en-us/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks/), [Temporal Event History](https://docs.temporal.io/workflow-execution/event), and [Temporal Continue-As-New](https://docs.temporal.io/workflow-execution/continue-as-new).
- **Transfer status:** the pinned Symphony and LangGraph records in `docs/reference-implementation-evidence.json` remain the machine-readable implementation basis for the active portfolio and recovery mechanisms. Kubernetes, Magentic-One, and Temporal are fresh official design contrasts in this change; they do not add a pinned transfer or Complex validation claim.
- **Implementation observations:** Symphony makes the tracker the work control plane and gives one orchestrator authority over dispatch, retry, stop, and reconciliation state. Kubernetes separates desired state from observed status, lets bounded controllers own different resource aspects, and records which generation was observed rather than assuming the newest write is accepted truth. Magentic-One separates the outer Task Ledger from the per-step Progress Ledger and updates the outer plan after detected stalls. Temporal uses an append-only event history for recovery but explicitly checkpoints relevant state into a fresh execution when history or code generation becomes unwieldy.
- **Production problem:** long projects accumulate several locally useful state recorders across modules, lanes, repositories, threads, and workflows. Without a controller-level reconciliation view, global dependencies and the authoritative next route drift; copying all local state into one continuously growing master ledger creates the opposite failure.
- **Adopted:** one controller-owned global control projection; bounded local state capsules with authority and observed generation/hash; event-triggered reconciliation plus a project-specific staleness fallback; dependency-scoped conflict isolation; checkpoint into a fresh projection epoch when history becomes unwieldy; isolated workspaces, bounded concurrency, stable identifiers, retry/backoff, idempotency, and observability.
- **Rejected:** assuming a worker exit means the task is complete; unlimited retry; concurrency without ownership; last-write-wins; full fan-in on every beat; one monolithic ledger containing every local detail.
- **Not transferable:** Complex does not require Kubernetes, a daemon, issue tracker, Temporal server, or Microsoft runtime. It cannot provide atomic multi-system consistency unless the target Harness supports it; the portable contract is authority, source generation, bounded capsule, one global writer, conflict route, and recovery pointer.
- **Complex micro-contract:** local boundaries remain authoritative for local facts and artifacts. On recovery, phase/stage transition, handoff, topology/dependency change, conflict/staleness, stage delivery, or the project staleness limit, the controller gathers affected local capsules, reconciles desired Goal/portfolio state against observed generations and accepted artifacts, publishes one compact global projection, and continues independent routes. When the projection history becomes costly, carry the latest relevant state into a fresh epoch and retain old detail by pointer.
- **Refresh trigger:** duplicate work, stale global routing, inconsistent local recorders, cross-boundary handoff failure, history growth, transient failures, or new cross-turn continuation.

### Decision ownership, exact approval, and resume safety

- **Sources:** [OpenAI Agents SDK human-in-the-loop](https://openai.github.io/openai-agents-python/human_in_the_loop/), [LangGraph interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts), [Temporal Activity Definition](https://docs.temporal.io/activity-definition).
- **Production problem:** human approval, external input, or retry can resume a workflow after partial work; if non-idempotent side effects happened before the pause, resume can duplicate records, overwrite state, or charge twice.
- **Adopted:** classify decision ownership separately from side-effect class; approve the exact tool call or operation rather than the whole project; keep pre-approval work read-only, local, draft, idempotent, reversible, or compensatable; record scope/version, action ID, payload hash, checkpoint, and resume route.
- **Rejected:** importing LangGraph or Temporal as a required runtime; treating every user question as a durable interrupt; adding heavy transaction ceremony to read-only beats.
- **Not transferable:** Complex cannot guarantee platform-level exactly-once execution without a supporting runtime; it can only require agent-visible contracts and safe sequencing.
- **Complex micro-contract:** AI owns internal orchestration. When a specific external or irreversible operation needs authority, approval binds to that operation's payload and stable action ID; retry, idempotency, rollback, and compensation remain Harness responsibilities.
- **Refresh trigger:** new approval surfaces, external-write tools, retryable background work, or duplicate side-effect failures.

### Explicit multi-agent organization

- **Sources:** [OpenAI Codex subagents](https://developers.openai.com/codex/subagents), [OpenAI Agents SDK handoffs](https://openai.github.io/openai-agents-python/handoffs/), [Microsoft orchestration patterns](https://learn.microsoft.com/en-us/agent-framework/workflows/orchestrations/), [Team Topologies](https://teamtopologies.com/key-concepts).
- **Production problem:** threads, workers, and durable responsibilities are conflated, creating unclear ownership and polluted review.
- **Adopted:** manager ownership, bounded worker contracts, durable responsibility lanes with wake/retire conditions, clean-context evaluators, explicit handoff packets, and observed resource IDs/status when platform resources are actually created.
- **Rejected:** creating agents for every small task or calling a subagent a standing lane.
- **Not transferable:** organization design must fit project scale and available Codex surfaces.
- **Complex micro-contract:** controller owns integration and acceptance; each standing lane declares accepted input/output, wake trigger, context policy, manager acceptance, retirement condition, and resource evidence; workers return bounded artifacts and summaries.
- **Refresh trigger:** recurring responsibility, reviewer contamination, or topology drift appears.

### Artifact-first adaptive work topology

- **Sources:** [Magentic-One](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/magentic-one.html), [Anthropic multi-agent research](https://www.anthropic.com/engineering/multi-agent-research-system), [Virtual Lab](https://github.com/zou-group/virtual-lab), and [Agent Laboratory](https://github.com/SamuelSchmidgall/AgentLaboratory).
- **Transfer status:** these four sources are architecture contrast and documentation inspection, not new pinned transfer records. The machine-readable implementation basis for the active mechanisms remains the pinned Symphony, LangGraph, Codex, and SWE-agent records in `docs/reference-implementation-evidence.json`; this clarification does not promote evidence status.
- **Production problem:** one long project contains different kinds of work. A fixed phase pipeline is efficient for stable repeated transformations, while open-ended research benefits from an orchestrator that revises plans, parallelizes independent branches, and preserves clean contexts. Applying either topology to the entire project creates unnecessary coordination or premature convergence.
- **Implementation observations:** Agent Laboratory exposes a fixed literature-review, experimentation, and report-writing pipeline with phase checkpoints; Virtual Lab uses team and individual meetings around a human agenda and reports a real experimentally validated application; Magentic-One separates an outer Task Ledger from an inner Progress Ledger and replans after stalled progress; Anthropic's research system uses a lead agent, parallel bounded subagents, persistent plans, clean contexts, and artifact references while explicitly warning about token cost and tightly coupled tasks.
- **Adopted:** classify at project, phase, module, and active-work-item scope; define the artifact contract before assigning resources; retain one controller as integrator; use deterministic Harness for stable procedures, temporary workers for independent branches, standing lanes for recurring responsibility, and clean evaluation for independence-sensitive claims; pass artifacts or references rather than long agent conversations.
- **Rejected:** one permanent role chart for every project, a discussion cell for every decision, multi-agent work without a mergeable artifact, and fixed pipelines that cannot route back when assumptions change.
- **Not transferable:** biomedical laboratory roles, patent-workflow states, benchmark agent rosters, provider-specific memory, and reported upstream performance do not define a general Complex organization or validate this transfer.
- **Complex micro-contract:** for each active work item, record accepted input, operation or judgment, expected artifact or diagnostic outcome, acceptance, recovery, and write-back; inspect uncertainty, procedure stability, parallel independence, evaluation independence, and responsibility; compile the smallest sufficient topology; mechanize stable repeated judgment and route repeated assumption-driven mechanical failure back to discovery.
- **Evidence boundary:** these sources calibrate the design and contrast fixed versus adaptive implementations. Complex has not yet run a locked real-project comparison of the compiled topology, so the related operating-organization and portfolio mechanisms remain conditional and `screened`.
- **Refresh trigger:** a real project shows topology overhead, missed parallelism, reviewer contamination, unstable handoff, or failure to move between judgment and deterministic execution.

## Progress Loop

### Time appetite, usable increments, and stage reviews

- **Sources:** [Basecamp Shape Up: Set Boundaries](https://basecamp.com/shapeup/1.2-chapter-03), [Shape Up: Circuit Breaker](https://basecamp.com/shapeup/2.2-chapter-08), [official Scrum Guide](https://scrumguides.org/scrum-guide.html), and the [NASA Systems Engineering Handbook](https://www.nasa.gov/wp-content/uploads/2018/09/nasa_systems_engineering_handbook_0.pdf).
- **Implementation observation:** Shape Up fixes an investment appetite and varies scope rather than silently extending work; its circuit breaker forces reframing when the shaped solution does not fit. Scrum uses a fixed-length heartbeat whose accountable output is a usable, verified Increment, not an activity report. NASA technical reviews bind phase timing to explicit entrance/success criteria, reviewed products, and corrective action when cost, schedule, or technical trends indicate an unfavorable outcome.
- **Production problem:** long projects can remain scientifically or technically active while providing no decision-useful result to the human for an indefinite period. A raw timebox alone creates the opposite failure if expiry is mistaken for completion or quality is sacrificed to meet the date.
- **Adopted:** project-specific time appetite; explicit stage result horizon; smallest useful stage artifact; measured elapsed time and artifact movement; usable increment or decision-grade diagnostic by the horizon; fixed quality/evidence floor; scope convergence, parking, route change, or explicit re-appetite when progress does not fit.
- **Rejected:** universal sprint length, fixed six-week cycles, activity-only progress reports, silent deadline extension, and treating timebox expiry as Goal completion.
- **Not transferable:** product-team calendars, Scrum roles/events, Basecamp betting authority, and NASA review boards are not required Complex runtime structures.
- **Complex micro-contract:** Prompt owns the appetite, horizon, stage artifact, and quality floor; Harness observes elapsed work and checkpoints; Loop converges scope and routes at the horizon; Delivery exposes the usable increment and acceptance evidence while continuous cadence proceeds to the next stage.
- **Refresh trigger:** users wait too long for usable results, a stage produces only a status narrative, time pressure lowers evidence quality, or repeated horizon misses show the appetite is not grounded in observed throughput.

### Outcome-based completion and evaluator separation

- **Sources:** [Anthropic harness design for long-running apps](https://www.anthropic.com/engineering/harness-design-long-running-apps), [Anthropic agent evals](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents), [Microsoft Agent Framework LoopEvaluator](https://learn.microsoft.com/en-us/agent-framework/agents/harness).
- **Production problem:** agents stop because they produced text, completed a fixed number of turns, or self-reported success.
- **Adopted:** negotiate completion before execution, evaluate the actual environment or artifact, separate evaluator for important work, outcome-first grading.
- **Rejected:** exact trajectory matching as the primary definition of success.
- **Not transferable:** every small beat does not need an independent model evaluator.
- **Complex micro-contract:** every important Loop has an outcome predicate, evaluator, declared outcome (execution artifact or diagnostic decision), and next route from observed results.
- **Refresh trigger:** false completion, evaluator disagreement, or path overfitting appears.

### Target-function iteration instead of local greed

- **Sources:** [CRISP-DM](https://www.ibm.com/docs/it/SS3RA7_18.3.0/pdf/ModelerCRISPDM.pdf), [NASA Systems Engineering Handbook](https://www.nasa.gov/wp-content/uploads/2018/09/nasa_systems_engineering_handbook_0.pdf), [Google SRE eliminating toil](https://sre.google/sre-book/eliminating-toil/).
- **Production problem:** repeated local checks, audits, or evidence collection consume work without closing the project chain.
- **Adopted:** target-function feedback, entry/success criteria, early end-to-end slice, toil/WIP review, branch parking.
- **Rejected:** heavyweight stage ceremonies for every small beat.
- **Not transferable:** fixed review cadence regardless of project events.
- **Complex micro-contract:** each Loop names target function, module, completion predicate, and non-greedy rationale; add a lane only when recurring organization is active, use a forward artifact for execution, and use a route/falsification/blocker/parking result for diagnosis.

### Agent-facing governance, project-native artifacts

- **Sources:** OpenAI Harness Engineering, SWE-agent's agent-computer interface, and schema-checked agent evaluation harnesses.
- **Production problem:** a richer agent instruction can accidentally leak its own vocabulary into files, rename machine fields, add wrappers, or replace requested evidence with process explanation.
- **Adopted:** keep the agent interface narrow and mechanically checkable; treat repository paths, schemas, types, and verifiers as the executable contract; keep governance language in the decision layer.
- **Rejected:** requiring every target project to emit Complex-shaped YAML/JSON or expose protocol headings to human readers.
- **Not transferable:** no single artifact schema is universal across projects.
- **Complex micro-contract:** local completion and artifact contracts outrank mechanism vocabulary. Complex may select and justify the route, but it may not change the required artifact shape or suppress requested facts without an explicit project-level change.
- **Refresh trigger:** a candidate mechanism passes its semantic test but fails a local verifier, renames a field, wraps a flat state, or creates governance-heavy reader output.
- **Refresh trigger:** guardrail-only repetition, missing early closure, or module bottleneck changes.

## Cross-Layer Diagnosis

The central transfer rule is diagnostic:

1. capture the failed outcome and relevant trajectory;
2. classify Prompt, Context, Harness, Loop, or model limitation;
3. repair the failed layer;
4. add an evaluation case;
5. update prompt defaults only for instruction-level failures.

This prevents context omissions, unavailable tools, poor recovery, and incorrect stopping logic from turning into an ever-longer prompt.

## Complex Self-Optimization

### Substantial-change packet and progressive evidence rollout

- **Sources:** [Kubernetes Enhancement Proposals](https://github.com/kubernetes/enhancements/blob/master/keps/README.md), [KEP template](https://github.com/kubernetes/enhancements/blob/master/keps/NNNN-kep-template/README.md), [Argo Rollouts](https://github.com/argoproj/argo-rollouts/blob/master/docs/index.md), [Argo analysis controller](https://github.com/argoproj/argo-rollouts/blob/7b85ecc5c69047300da8eca1f85a21a9d66a4f11/rollout/analysis.go), Rust RFCs, Inspect AI, and promptfoo.
- **Implementation observation:** KEPs separate routine contribution from enhancement-level change and bind substantial proposals to goals/non-goals, testing, production-readiness, staged graduation, rollback, observability, and implementation history. Argo keeps a stable revision while a bounded candidate is observed and explicitly promoted, paused, aborted, or rolled back. Inspect and promptfoo preserve versioned task/run/score and baseline/candidate comparison boundaries.
- **Production problem:** Complex can turn a real failure into protocol prose, pass structure checks, and stop before proving that the new default improves project outcomes. The inverse failure is making every small correction carry a large evidence ceremony.
- **Adopted:** three change classes; one reversible change unit; stable baseline; explicit graduation/failure criteria; contract screening, bounded reproduction, same-task comparison, shadow or limited real use, repeated outcome review; promote/keep/demote/rollback; residual evidence continuation.
- **Rejected:** a proposal for every edit, Kubernetes release governance, fixed traffic percentages, automatic promotion from marker pass, and replacing the stable baseline before rollback is possible.
- **Not transferable:** cluster reconciliation, SIG authority, release trains, metric providers, and deployment percentages do not map to a small Codex runtime kit. They ground the state transition and evidence discipline only.
- **Complex micro-contract:** routine corrections use edit/test/residual scan; bounded and substantial changes define one falsifiable candidate, keep the stable baseline, advance only as far as observed evidence permits, update maturity claims precisely, and automatically execute remaining internal evidence work.
- **Refresh trigger:** a protocol change is declared complete at documentation, a candidate is promoted without comparable outcomes, a rollback cannot be executed, or maintenance procedure costs more than the decision value it creates.

## Evidence Boundary

External production sources show that a pattern has precedent and clarify its transfer boundary. They do not prove the Complex implementation improves user outcomes. `docs/mechanism-maturity.json` records that distinction, and real transcript or end-to-end project evidence is required for promotion.
