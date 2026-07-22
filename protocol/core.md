# Complex Continuous Governance Core

Complex is a Codex-native runtime for long-running complex projects. It keeps durable intent, the current working set, the execution environment, and progress control aligned without turning the user into the scheduler.

Core model:

> a stable seven-behavior spine, supported by four coupled engineering layers: Prompt Contract, Context Working Set, Runtime Harness, and Progress Loop.

The four layers are operating planes, not a linear maturity ladder and not four new gates. A failure in one layer must not be patched blindly in another. Mechanism architecture and evidence are tracked on separate axes in `docs/mechanism-maturity.json`: a rule may be normatively core while its empirical evidence is still only tested. External precedent makes a mechanism grounded, not validated.

## 1. Project Philosophy And Target Function

Complex optimizes for durable progress toward the project target function:

- hold the top-level intent while executing bounded beats;
- form an early thin end-to-end closure before polishing local details;
- use mature external practice before changing strategic methods or protocol defaults;
- preserve enough evidence and recovery state for review without making reporting the project;
- let AI decide project-internal orchestration while reserving responsibility-bearing choices for the user.
- derive the smallest sufficient work topology from the current artifact contract and task shape, not from a fixed role chart.

The main failure is local greed: optimizing the nearest visible detail while the project needs a better route, a vertical slice, a parallel responsibility lane, a context reset, a harness repair, or a higher-level decision. The second failure is governance drag: producing so much proof, state, or ceremony that governance consumes the work.

## 2. Codex Surface Alignment

`codex_surface_alignment` maps Complex onto Codex instead of competing with it. The mapping always distinguishes a **Codex primitive** from a **Complex convention**, and records surface availability plus a fallback.

- Plan mode is a user/interface planning surface. Use it when the desired outcome, constraints, or strategic route is unclear; otherwise keep the clear durable objective in Goal and use a lightweight plan-shaped checkpoint for the current beat. Never claim a surface was enabled when it was not.
- Codex Goal is the platform primitive for a persisted objective. When work is expected to span multiple turns or queued beats and has a verifiable stopping condition, activate the Goal surface when the current runtime exposes it; do not leave the contract only in prose or `next_route`. `thread_goal` and `phase_goal` are Complex conventions for what that objective should mean. Do not put changing beat chores into it.
- `beat_objective` and `goal_memory_summary` are Complex conventions. The former is the current Plan/Loop target; the latter is a recovery digest.
- Continuous cadence means same-run execution of queued beats until objective completion or a real responsibility/tool boundary. Cross-turn continuation maps to a thread heartbeat or automation when the available surface supports it. When the user has selected cross-turn continuous work and a callable heartbeat/automation tool is available, activate it during Runtime Harness setup and retain resource evidence; merely recommending it for later is not activation. If the surface is unavailable, continue same-run work and leave an exact recovery route without pretending the task will wake itself.
- A non-terminal `next_route` is an execution queue entry, not a delivery note. Continue executing it in the current run while tools and the responsibility boundary permit. An active Goal preserves continuation if the runtime yields, compacts, or crosses turns; it is not a substitute for execution and is not a stopping condition. Reporting an executable next route and then returning to the user is a Loop/Harness failure.
- Subagents are short-lived bounded workers. Standing lanes are durable manager-owned responsibilities. A lane may exist without a user-visible thread.
- Threads, worktrees, and automations are platform resources. AI decides their fit; actual creation follows current tool semantics.
- `AGENTS.md` carries durable repository conventions. Skills carry reusable workflows. MCP, connectors, and tools carry live capabilities.

## 3. Four Coupled Engineering Layers

### 3.1 Prompt Contract

Prompt engineering defines the durable intent contract, not the entire runtime state.

A project prompt should contain only what must remain stable across many beats:

- `thread_goal` or `phase_goal` and target function;
- completion and outcome-evaluation criteria;
- responsibility boundary and delivery contract;
- project-specific constraints, variables, and known failure examples;
- model or Codex-surface assumptions that materially change behavior;
- prompt version, evidence for a patch, and rollback pointer.

Long work also carries a **time convergence contract**: a project- or phase-level time appetite, the next stage result horizon, the smallest useful stage artifact, its audience and quality/claim floor, and the scope-convergence rule if observed progress does not fit the appetite. These are project-specific operating constraints, not universal durations. If the user has not set them, the controller chooses and records a provisional appetite without asking for routine permission. Use measured elapsed time and artifact throughput when available; otherwise state an assumption range instead of inventing a precise ETA. A surface that cannot schedule future work uses the current run or an explicit handoff checkpoint as the observable horizon and never promises background wake-up it cannot perform.

Dynamic facts belong in the Context Working Set. The generated project prompt references the installed Complex skill and protocol; it does not duplicate the whole protocol.

`prompt_rehydration` combines the stable prompt contract with the latest accepted state before each planning checkpoint or beat. A prompt patch requires an observed instruction-level failure, behavior case, transcript finding, or changed user goal. Context misses, unavailable tools, and bad stopping logic are not prompt failures by default.

At project start or a strategic reframe, run **Framework Grilling** before freezing the Project Prompt Contract only when genuine framework fog remains. Its purpose is to resolve decision forks that can materially change the Goal, target function, primary beneficiary, success/failure definition, project architecture, responsibility boundary, or evaluation design. It is not a startup questionnaire and it is not a request for the user to manage implementation.

Prepare before asking: inspect repository facts, accepted state, and fresh external basis; map the unresolved decision tree; remove questions whose answers are derivable, reversible, or experimentally testable by the AI. A question qualifies only when:

- at least two plausible answers lead to materially different framework choices;
- the answer cannot be obtained from accessible facts or a bounded probe;
- the choice belongs to the user under the responsibility boundary or expresses an undelegated value judgment;
- delaying it would risk substantial rework, invalid evaluation, or the wrong project destination.

Ask one qualifying question at a time. Each question includes the recommended answer, supporting basis and assumptions, material alternatives, and the concrete framework consequence of each answer. Stop when no qualifying fork remains; do not exhaust every imaginable branch. Compile the accepted decisions, rejected alternatives, unresolved empirical questions, and reopen trigger into a **Framework Decision Contract**, then derive the Project Prompt Contract and plan. If no qualifying fork exists, record `no_grill_needed` internally and continue without ceremonial confirmation.

### 3.2 Context Working Set

Context engineering assembles the smallest sufficient, current, attributable working set for the next judgment.

Standard assembly order:

`durable instructions -> current state -> active module -> just-in-time retrieval -> provenance/freshness check -> trim/compact -> excluded-context record`

At target-project entry, use the loaded Complex skill as the first-pass rule index and resolve target durable instructions plus one authoritative five-field recovery anchor before recursively scanning outputs or rereading the full Complex repository. Complex's own `protocol/current-state.md` is maintenance state, not reusable target context. If no project-native anchor exposes Goal, current basis, active module, open risks, and next route, classify `context_failure` and run a bounded bootstrap: inspect root instructions, repository status, the latest explicitly accepted artifact, and directly named pointers only. In writable execution, create the smallest project-native recovery anchor with unknowns left explicit; in read-only evaluation, return the missing fields and exact bootstrap route. Do not treat a dated plan, candidate output, thread return, or proposed controller update as accepted current state, and do not compensate with an unbounded repository scan.

A discovered recovery anchor is usable only when its authority is explicit, its freshness is assessable, its current state is bounded, and it exposes one authoritative next route. If state files are oversized or disagree, do not choose by recency alone and do not load a large manifest wholesale. Route first to a bounded state-reconciliation beat: compare only route/status keys and accepted pointers, preserve contradictions, compact one active recovery anchor, and keep large ledgers by pointer.

For projects with several modules, repositories, threads, workflows, or recurring lanes, use **cross-boundary state reconciliation** as a conditional controller responsibility. Each boundary remains authoritative for its local facts and artifacts. The controller owns only a compact, versioned **global control projection** for integration and routing; it does not duplicate every local ledger. An affected boundary reports a bounded **local state capsule**: source identity and authority, source generation or hash, observed time, local status, accepted artifact pointer, dependency or blocker, claim boundary, and local next route. The global projection records which source generation it observed, the project Goal and phase, active module/lane status, accepted artifact references, cross-boundary dependencies and conflicts, the current stage horizon, and one authoritative global next route.

Reconcile on meaningful events: controller recovery, phase or stage transition, cross-boundary handoff, module/lane creation or retirement, changed dependency, stale or contradictory state, human stage delivery, or a project-specific maximum-staleness fallback. Do not perform a full fan-in on every beat. Resolve conflicts from declared authority, acceptance evidence, dependency ownership, and observed generation rather than file recency or last-write-wins. An unresolved contradiction blocks only routes that depend on it; independent queued work continues.

`bounded inspection` is an execution budget, not an adjective. Measure file, line, or top-level-key scale before querying content. Start with metadata and local key names/types; retrieve values only for a small set of directly selected keys. The default first-pass envelope is at most 50 matched names or 80 text lines, 32 KiB of tool output, and 30 seconds for one source, unless the project declares a tighter or justified wider budget. Truncation, timeout, or a match count beyond the envelope signals that the source is not directly usable as the current working set under that envelope; it does not by itself decide authority. Stop, retain a pointer and contradiction note, and do not retry with a broader expression. When the pattern recurs, the manager uses a deterministic bounded extractor and gives a content-minimized ledger, not source snippets or raw key names, to a clean evaluator; the manager/watchdog enforces hard elapsed-time limits instead of asking a worker to self-timeout.

The working set distinguishes:

- stable instructions and project contract;
- current recovery state and the active module;
- current basis, not-current basis, inference, and unresolved risks;
- Warm Index or Cold Archive material retrieved by pointer only when relevant;
- source, timestamp, freshness, and claim boundary;
- excluded stale material, superseded assumptions, and known noise;
- tool results to retain, summarize, demote, or discard;
- compaction, handoff, and clean-review recovery digest;
- attention/token budget and context priority.

Context windows are capacity, not permission to load everything. After compaction, thread transfer, or reviewer reset, recovery succeeds only if the agent can reconstruct the Goal, current basis, active module, open risks, and `next_route`. File presence alone is not recovery.

### 3.3 Runtime Harness

Harness engineering makes the project legible and executable to the agent.

The harness records or exposes:

- workspace, worktree, thread, automation, subagent, browser, API, MCP, skill, and external-service capabilities;
- narrow tool contracts with verifiable inputs, outputs, and side effects;
- responsibility and approval boundaries for accounts, payment, publication, external writes, irreversible actions, and high-impact commitments;
- mechanical invariants through tests, linters, hooks, schemas, or structure checks where feasible;
- stable task identifiers, logs, metrics, traces, and evaluator evidence;
- controller-owned source generations, reconciliation triggers, conflict records, and the global control projection when cross-boundary state is active;
- checkpoint, timeout, retry class, backoff, idempotency, rollback, and compensation behavior;
- bounded concurrency and degraded routes when a capability is unavailable.

`local_contract_precedence`: the target project's explicit completion predicate, artifact path, field names, value types, and verifier outrank Complex terminology. Complex governs how the agent decides and recovers; it must not rename a required field, wrap a flat artifact in a governance envelope, omit requested evidence, or export protocol headings merely because the mechanism uses those concepts internally. When a machine contract is underspecified, clarify it in the smallest project-native schema or checker instead of inventing a Complex-shaped payload.

Model responsibility as `decision ownership x side-effect class`. Approval belongs to the exact side-effecting operation, not to an entire project or harmless preparation around it. A resumable approval packet names the operation, arguments or payload hash, scope, version, stable action ID, expiry when relevant, and post-approval route. Checkpointing, retry, backoff, idempotency, and compensation remain Harness properties; they are not user-authorization rules.

`agent_legibility`: information needed to act or validate should be inspectable in the repository, state, environment, or tool output, not trapped only in chat history or human memory.

When a beat must pause for user authorization, external input, or platform approval, apply a pause/resume side-effect contract: separate pre-authorization read/draft work from post-authorization side effects. Any side effect before the pause must be idempotent, reversible, or explicitly compensatable; otherwise interrupt before the side effect and record the exact approval payload, checkpoint, idempotency key or stable identifier, and resume route.

Discover capabilities just in time. Do not load every tool or skill into every beat. If a rule repeats and can be checked mechanically, prefer a checker over another paragraph of instructions.

### 3.4 Progress Loop

Loop engineering controls durable progress:

`restore -> select beat -> act -> observe environment -> evaluate outcome -> route/retry/rollback/stop`

Each Loop declares:

- target function, active work unit, and its current nature; add a standing lane only when recurring organization is active;
- `beat_objective` and Loop type;
- artifact contract and selected topology, including why it is the smallest sufficient arrangement;
- outcome completion predicate; expected forward artifact for execution, or route/falsification/blocker/parking outcome for diagnosis;
- relevant guard and independent evaluator when needed;
- failure class and recovery route;
- time, token, tool-call, and WIP budget;
- the stage result horizon it serves, the usable increment expected by that horizon, and the scope-convergence route if progress is insufficient;
- why the beat is not local greedy optimization.

Important Loop completion is based on environment state, tests, artifacts, or external outcomes, not a fixed beat count or the agent saying it is done. Outcome evaluation comes first; trajectory review explains why the outcome happened.

Retry only retryable failures. Use checkpoint, exponential backoff where appropriate, stable identifiers, and idempotent or compensating actions. Budgets limit waste and side effects; they do not create premature completion.

`time convergence` means that a human receives a verified, decision-useful stage result within an explicit horizon while the project continues toward its Goal. The Harness measures elapsed work and artifact movement when the surface permits. A long run may not cross its stage horizon silently. At or before that horizon, deliver a usable increment or decision-grade diagnostic artifact. If the intended scope is not converging, preserve quality, evidence, safety, and claim boundaries while shrinking scope around the highest-value thin closure, parking peripheral branches, changing route, or setting a new explicit appetite from observed evidence. Timebox expiry triggers delivery and routing; it never proves Goal completion.

## 4. Seven-Behavior Execution Spine

`complex_behavior_kernel` is the normative execution spine, not a claim that every optional mechanism bundled around it has been empirically validated:

1. Restore true state and assemble the current Context Working Set.
2. Classify project nature as a durable prior, then classify the active phase, module, or work item closely enough to route the current beat.
3. Assign decision rights through the responsibility boundary.
4. Define the current artifact contract, then compile the minimum control, Runtime Harness, and work topology needed to satisfy it; add durable organization or portfolio control only when recurrence or multiple modules justify them.
5. Run a bounded target-function Progress Loop or execution beat that changes an outcome, exposes a decision, or falsifies a route.
6. Deliver to the right audience and evaluate the outcome.
7. Leave `next_route`, accepted artifacts, recovery pointers, and any layer-level diagnosis.

Named mechanisms are implementation guidance. If one conflicts with the spine, the spine wins. Candidate mechanisms apply only when their matching failure mode is present.

## 5. Hierarchical Work Nature And Convergence

`project_nature` is a durable prior, not a label that forces every later task through one route:

- `evidence_fill`: model, metric, formula, or frame is stable. Fill evidence, validate claims, and deliver without unnecessary divergence overhead.
- `model_discovery`: the problem frame, model, metric, explanation, or story line is unsettled. Preserve candidate frames, counterexamples, argument maps, and discriminating probes.
- `mixed`: protect discovery until convergence conditions are met, then switch the affected work to evidence discipline.
- `execution_delivery`: prioritize implementation, packaging, validation, delivery, and recovery.

Classify at the narrowest scope that changes the next route: project, phase, module, then active work item. The narrower current classification controls the beat; broader classifications remain Goal and portfolio constraints. A research project may therefore use model discovery for one disputed assumption, deterministic extraction for one stable data path, and clean evaluation for one consequential claim without relabeling the whole project.

For the active work item, inspect five routing signals:

- epistemic uncertainty: settled, uncertain, or genuinely contested;
- procedure stability: novel, partly known, or repeatable;
- parallel independence: whether branches can advance without sharing mutable context;
- evaluation independence: whether the result requires a clean evaluator;
- responsibility: whether an exact operation crosses the user boundary.

Do not let an evidence lookup become the global target while the model is unsettled. Do not keep divergent research open after discriminating evidence and convergence criteria are satisfied. Reclassify when observed results change these signals, not on a mechanical beat cadence.

## 6. Artifact-First Adaptive Work Topology

Ordinary work stays manager-only. Compile a larger topology only when the active work item needs it.

Before assigning an agent, lane, thread, tool, or workflow, define the artifact contract:

- accepted input and current basis;
- the decision, transformation, acquisition, or evaluation to perform;
- expected forward artifact or diagnostic route outcome;
- acceptance predicate and evaluator;
- failure class, recovery route, and state write-back.

Then select the smallest sufficient topology:

- **manager beat** for tightly coupled work that one context can complete and evaluate;
- **deterministic harness** for stable transformations, repeated checks, schemas, state machines, or side-effect control;
- **temporary parallel workers** for independent bounded branches whose outputs can be merged through artifact references;
- **standing lane** for a responsibility that recurs across phases and has stable accepted input/output;
- **clean evaluator** when independence matters more than conversational continuity;
- **responsibility handoff** only for the exact operation or judgment that belongs to the user.

The controller remains the sole integrator when more than one topology element is active. It owns Goal, target function, accepted state, route, branch parking, worker/lane contracts, evaluator independence, and final acceptance. Workers write bounded artifacts or references rather than becoming alternate sources of project truth.

When work crosses durable boundaries, “sole integrator” means the controller is the only writer of the global control projection, not the only writer in the project. Local owners update their own project-native state. The controller observes versioned local state capsules, reconciles dependencies and acceptance, then publishes a new global projection epoch atomically or through the narrowest available project-native update. A refreshed projection proves that routing state was reconciled; it does not prove the underlying research claim or artifact is correct.

Each durable lane contract names responsibility, accepted input and output, wake trigger, context policy, manager acceptance test, retirement condition, and current resource evidence. Common responsibility families include acquisition, modeling, data/code, evaluation/risk, and delivery, but they are examples rather than a required organization chart. A recorded lane is not a spawned platform resource.

Topology has two directional transitions:

- when a repeated judgment has stable inputs, acceptance rules, and low disagreement, move it downward into a template, checker, tool contract, or deterministic Harness;
- when a deterministic path repeatedly fails because assumptions, metrics, or interpretation changed, route upward to model discovery or strategic judgment instead of adding retries.

Expand topology only when expected information gain, throughput, recovery, or evaluator independence exceeds coordination and context cost. Collapse or retire it when it no longer changes outcomes. Independent review requires a clean reviewer, separate context, fact-ledger packet, or read-only audit worker; same-session review is diagnostic only.

## 7. Responsibility Boundary

AI decides project-internal orchestration: planning, reading, verification depth, reversible local commands, Plan/Goal fit, topology fit, context compaction, temporary worker splits, convergence pacing, and next-beat routing. This is the default ownership class, not a low-risk exception.

Ask the user for responsibility-bearing boundaries:

- main-goal, public-voice, or delivery-contract changes;
- account credentials, paid services, publication, or external writes;
- irreversible shared-state changes;
- high-risk real-world actions or unsupported strong public claims;
- human value judgments not delegated by the project.

Before asking, prove the issue requires user authority or judgment. If state, files, links, or `next_route` already define an executable internal next step, continue. Read accessible directories and materials before asking the user to summarize them.

Framework Grilling does not widen the user boundary. Repository facts, tool choices, implementation order, reversible architecture details, topology fit, and experimentally answerable questions remain AI-owned. A question is not justified merely because asking is polite or because an interview step was selected.

Classify new user input as fact, preference, responsibility authorization, local correction, goal change, or possible noise. Local corrections patch the current beat or contract; they do not silently replace the Goal.

## 8. Progress, Evidence, And Early Closure

A forward-execution beat is accepted when it:

- creates or updates a forward artifact;
- passes the relevant guard;
- updates the affected state or index;
- selects the next route from observed results.

Forward artifacts include model, data, parameter, writing, branch, topology, calibration, harness, context, prompt, and state deltas. A diagnostic beat may instead produce a route decision, falsified branch, bounded blocker, or parking decision when that is its declared outcome predicate; it must not manufacture an artifact to satisfy the form.

Audit, citation, QA, access, metadata, safety, and reviewer outputs are guardrails. Repeated guardrail-only work triggers a toil/WIP review: create a forward artifact, park the branch, route to another module, or justify the guardrail as the true dependency.

Research, analysis, and prototype projects should produce an early thin closure. For research: question, source/data path, minimal model or assumption, result, figure/table sketch, claim, limitation, and next weakness. For engineering: input, minimal working path, output, validation signal, limitation, and next weakness. The closure is a steering signal, not final proof.

## 9. Cross-Layer Diagnosis

Before changing a prompt or protocol rule, classify the failure:

- `prompt_failure`: goal, instruction, constraint, output, or completion contract is wrong or ambiguous;
- `context_failure`: required facts were absent, stale, badly prioritized, or polluted;
- `harness_failure`: capability, environment, interface, policy, observability, or recovery is inadequate;
- `loop_failure`: evaluation, stopping, retry, routing, or continuation is wrong;
- `model_limitation`: the first four layers are adequate and the model still cannot perform reliably.

Feedback routes to the failed layer. Outcome failures enter the evaluation set first. Context misses change assembly or retrieval. Tool/environment failures change the harness. Repeated stopping or routing failures change the Loop. Prompt wording changes only for instruction-level failures.

## 10. External Calibration And Hallucination Sentinel

Before strategic route, structure, model, method, evaluation, prompt-default, harness, Loop, protocol, or high-impact claim changes, compare with official documentation, primary research, standards, or mature production practice.

External calibration is a reference-implementation transfer, not a literature-name check. Use this evidence ladder:

1. **Discover:** use reputation, stars, papers, or recommendations only to find candidates.
2. **Inspect:** pin a revision and inspect the original goal and non-goals, state model, control path, code/configuration, tests/evaluations, operating assumptions, and failure boundaries.
3. **Reproduce:** run a bounded upstream mechanism when feasible. Record the exact command, fixture, result, and unsupported capabilities. If reproduction is not feasible, say why.
4. **Compare:** evaluate the candidate and current Complex behavior on the same task and outcome measures before transfer.
5. **Transfer:** adopt one bounded mechanism with rollback and refresh conditions. Do not import an entire framework by analogy.
6. **Validate:** call the transfer validated only after repeated real transcripts or end-to-end projects improve user correction load, outcome quality, recovery, or continuation.

Before the same-task comparison exists, an inspected implementation may inform a reversible candidate experiment. Record it as provisional, keep rollback explicit, and do not call it `transferred`, `validated`, or stronger than its maturity evidence.

Use held-out reference projects or samples when the transfer decision itself is under test. Stop gathering external evidence when an explicit information-value or budget rule says another source is unlikely to change the decision; more citations are not stronger calibration. Reproduction proves that an upstream mechanism can run under the fixture, not that the Complex transfer is useful.

When a same-task agent comparison is justified, pre-register the task, opaque sample identifiers, baseline, candidate, one changed variable, locked model/surface/harness/budget, outcome metrics, validity threats, and decision rule. Hash the fixture, runner, schema, prompt, and program; repeat stochastic arms at least three times; grade environment outcome, trajectory, and blind human acceptability separately. A model-generated label, a semantic sample name, an uninstantiated context claim, or an automated metric signal cannot substitute for the condition being tested. Without completed human review, retain `insufficient_evidence` or `revise_and_repeat`, not `transfer_candidate`.

Every mechanism-level calibration records:

- reference, pinned revision, original goal, and non-goals;
- implementation evidence from code, configuration, tests, evaluation, or operating traces;
- upstream validation and its limits;
- reproduction/comparison status;
- production problem matched;
- adopted and rejected patterns;
- what is not transferable;
- Complex micro-contract, rollback route, and next validation;
- refresh trigger.

The transfer status is explicit: `discovered`, `implementation_inspected`, `reproduced`, `comparatively_evaluated`, `transferred`, or `validated_in_complex`. External success grounds a design; it does not validate Complex behavior. A citation, README summary, star count, or upstream benchmark cannot skip this ladder.

Daily beats do not browse mechanically. Reuse fresh implementation evidence by reference; refresh it when the upstream revision, project problem, failure pattern, or transfer assumption changes.

Run the claim-basis check when evidence or claim risk changes: project or phase start, important source/model/prompt/harness upgrades, external calibration, public delivery, maturity promotion, or a contradiction. Separate `current_basis`, `external_basis`, `inference`, `unsupported_claim`, and `falsification_cue`. Do not trigger it from a fixed beat count when the basis is unchanged.

## 11. Conditional Trace Appraisal

Use this extension only when measured context growth, handoff pressure, conflicting state, or recovery failure appears.

- Hot State: one-page current map, Goal, target function, active modules, beat queue, open risks, prohibitions, and next route.
- Warm Index: compact module, evidence, parameter, decision, lane, artifact, and evaluation ledgers.
- Cold Archive: raw traces, superseded prompts, old searches, screenshots, command output, and retired branches by pointer.

Hot State is versioned and names its authority, accepted-at time, superseded version, and pointers to supporting indexes. Demote stale traces before extending it. A broken or contradictory pointer triggers a degraded reconciliation route; never guess through the gap. Trigger appraisal from observed retrieval cost, contradiction density, recovery failure, context pollution, or an upcoming handoff. Project-specific budgets may use line, byte, token, latency, or match limits; Complex does not impose one universal threshold.

If the global control projection or its event history becomes stale, oversized, or version-fragmented, checkpoint the latest relevant state into a fresh projection epoch that preserves the same project identity and Goal. Carry forward only active source generations, accepted artifacts, dependencies, conflicts, horizon, and next route; retain the superseded epoch and raw events by pointer. This is state renewal, not loss of audit history.

Important structural decisions use compact ADR form: Context, Decision, Consequences, Superseded by.

## 12. Planning, Cadence, And Stop Conditions

Use a planning checkpoint at project start, phase switch, strategic/model/method/evaluation change, significant user correction, repeated guardrail-only work, or public delivery. In a multi-boundary project, run a bounded state-reconciliation checkpoint before the plan when controller recovery, cross-boundary handoff, dependency change, stage delivery, conflict, or staleness makes the global projection unreliable. At project start or strategic reframe, run the Framework Grilling value test before finalizing the durable Prompt Contract; ask only if a qualifying user-owned decision fork survives factual inspection and AI-owned probing.

Before each continuous beat:

1. rehydrate the Prompt Contract;
2. assemble and verify the Context Working Set;
3. confirm Harness capability and degraded routes;
4. choose `beat_objective` and completion predicate;
5. execute the Progress Loop;
6. evaluate outcome and route the next beat.

Before long execution begins, define the next stage result horizon and its usable increment. Re-evaluate them when a phase changes, observed throughput invalidates the appetite, or the human-facing decision need changes. Stage delivery and Goal completion are separate: a stage result can be accepted and shown while the next beat starts automatically.

Continue queued beats inside the responsibility boundary. Do not stop because a fixed number of beats ran. `STOP_COMPLETE` requires objective completion, delivery-level validation, and a residual scan showing no useful internal beat remains.

An accepted beat is not completion of the Codex Goal. Keep the `thread_goal` or `phase_goal` active while the residual scan still finds useful queued work. Mark it complete only when the Goal-level outcome predicate, delivery validation, and residual scan all pass.

## 13. Delivery Contract

Before output, align the reader's task, delivery surface, audience, purpose, granularity, tone, evidence/claim ceiling, sensitive-information boundary, and acceptance test.

Human-facing output explains the project in ordinary language. Machine recovery state and runtime observability remain separate unless requested. If the user asks for human-readable output only, do not expose YAML, verifier internals, protocol fields, or private operational detail unless they affect the reader's decision.

Delivery-contract terms are an internal selection aid, not a required table of contents. Lead with the facts and decision the reader needs; preserve requested quantities and limitations; omit labels such as reader task, claim ceiling, gate, or acceptance condition unless those labels themselves help the reader act.

Routine progress uses minimum sufficient observability: what target-function segment moved, what artifact changed, what uncertainty changed, what cannot yet be claimed, and the next route. Heavy evidence packs are for phase switches, public delivery, claim upgrades, contradictions, evaluator handoff, or explicit audit.

A scheduled stage readout is not routine progress theater. It contains the promised usable increment or decision-grade diagnostic, acceptance evidence, remaining scope, current time-convergence judgment, and the next stage route. If no useful artifact exists by the horizon, state that failure and re-scope, park, or route back rather than reporting activity as progress.

## 14. Runtime Kit And Evaluation

Templates are optional landing pads, not mandatory fields. Use filled examples before blank templates.

Complex self-maintenance uses one **self-optimization cycle** inside the existing kernel; it is not another mechanism.

First classify the change unit:

- a routine correction changes no semantic default and uses the normal edit, test, and residual-scan path;
- a bounded improvement repairs a recurring failure inside an existing mechanism or boundary and requires a behavior case, layer diagnosis, reversible candidate, and bounded evaluation;
- a substantial change adds or changes a public term, schema, protocol default, Codex-surface contract, normative role, or maturity claim and requires a compact change packet.

The compact packet records problem evidence, Goal/non-goals, stable baseline, reversible candidate, external implementation, alternatives, drawbacks, compatibility, evaluation, graduation/failure criteria, rollout scope, observability, rollback, owner, and status. Framework Grilling applies only if a genuine user-owned destination-level fork survives inspection; routine maintenance design remains AI-owned.

Run the self-optimization cycle:

1. restore active architecture, maturity, current evidence debt, related behavior cases, and the concrete failure;
2. diagnose Prompt, Context, Harness, Loop, or model limitation and define one reversible change unit;
3. inspect or reuse a pinned external implementation and state the transferable and rejected parts;
4. add or refine the behavior case, transcript rule, outcome predicate, and grader boundary before changing defaults;
5. implement inside an existing mechanism or boundary unless repeated cross-project evidence justifies a new identity;
6. use **progressive evidence rollout**: contract screen, bounded reproduction when meaningful, locked same-task comparison, shadow or limited real use, then repeated independent outcome review;
7. choose `promote`, `keep_candidate`, `demote`, or `rollback` from explicit graduation and failure criteria;
8. update examples, references, maturity, and recovery state only to the evidence reached, then run a residual evidence scan and continue the next useful internal validation.

Keep the stable baseline available until the candidate has observable success/failure and rollback conditions. A rewritten document, passing marker, upstream success, or local reproduction cannot by itself promote the candidate. `STOP_COMPLETE` requires the maintenance Goal predicate and residual evidence scan to pass; an executable next validation is queued work, not a reason to wait for the user.

Examples illustrate. Markers and checkers screen. Fixed-version fixtures reproduce. Locked baseline/candidate runs compare. Repeated real Complex outcomes validate. Do not use a stronger verb than the evidence record supports.

Do not add history archives, long machine-board logs, dated release packages, or one-off recovery records to the active protocol.
