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

Dynamic facts belong in the Context Working Set. The generated project prompt references the installed Complex skill and protocol; it does not duplicate the whole protocol.

`prompt_rehydration` combines the stable prompt contract with the latest accepted state before each planning checkpoint or beat. A prompt patch requires an observed instruction-level failure, behavior case, transcript finding, or changed user goal. Context misses, unavailable tools, and bad stopping logic are not prompt failures by default.

### 3.2 Context Working Set

Context engineering assembles the smallest sufficient, current, attributable working set for the next judgment.

Standard assembly order:

`durable instructions -> current state -> active module -> just-in-time retrieval -> provenance/freshness check -> trim/compact -> excluded-context record`

At target-project entry, use the loaded Complex skill as the first-pass rule index and resolve target durable instructions plus one authoritative five-field recovery anchor before recursively scanning outputs or rereading the full Complex repository. Complex's own `protocol/current-state.md` is maintenance state, not reusable target context. If no project-native anchor exposes Goal, current basis, active module, open risks, and next route, classify `context_failure` and run a bounded bootstrap: inspect root instructions, repository status, the latest explicitly accepted artifact, and directly named pointers only. In writable execution, create the smallest project-native recovery anchor with unknowns left explicit; in read-only evaluation, return the missing fields and exact bootstrap route. Do not treat a dated plan, candidate output, thread return, or proposed controller update as accepted current state, and do not compensate with an unbounded repository scan.

A discovered recovery anchor is usable only when its authority is explicit, its freshness is assessable, its current state is bounded, and it exposes one authoritative next route. If state files are oversized or disagree, do not choose by recency alone and do not load a large manifest wholesale. Route first to a bounded state-reconciliation beat: compare only route/status keys and accepted pointers, preserve contradictions, compact one active recovery anchor, and keep large ledgers by pointer.

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

- target function and module served; add a standing lane only when recurring organization is active;
- `beat_objective` and Loop type;
- outcome completion predicate; expected forward artifact for execution, or route/falsification/blocker/parking outcome for diagnosis;
- relevant guard and independent evaluator when needed;
- failure class and recovery route;
- time, token, tool-call, and WIP budget;
- why the beat is not local greedy optimization.

Important Loop completion is based on environment state, tests, artifacts, or external outcomes, not a fixed beat count or the agent saying it is done. Outcome evaluation comes first; trajectory review explains why the outcome happened.

Retry only retryable failures. Use checkpoint, exponential backoff where appropriate, stable identifiers, and idempotent or compensating actions. Budgets limit waste and side effects; they do not create premature completion.

## 4. Seven-Behavior Execution Spine

`complex_behavior_kernel` is the normative execution spine, not a claim that every optional mechanism bundled around it has been empirically validated:

1. Restore true state and assemble the current Context Working Set.
2. Classify `project_nature`: `evidence_fill`, `model_discovery`, `mixed`, or `execution_delivery`.
3. Assign decision rights through the responsibility boundary.
4. Establish the minimum control and Runtime Harness needed for this project; add operating organization or portfolio control only when recurring lanes or multiple modules justify them.
5. Run a bounded target-function Progress Loop or execution beat that changes an outcome, exposes a decision, or falsifies a route.
6. Deliver to the right audience and evaluate the outcome.
7. Leave `next_route`, accepted artifacts, recovery pointers, and any layer-level diagnosis.

Named mechanisms are implementation guidance. If one conflicts with the spine, the spine wins. Candidate mechanisms apply only when their matching failure mode is present.

## 5. Project Nature And Convergence

- `evidence_fill`: model, metric, formula, or frame is stable. Fill evidence, validate claims, and deliver without paying unnecessary divergence overhead.
- `model_discovery`: the problem frame, model, metric, explanation, or story line is unsettled. Preserve 3-5 candidate frames, counterexamples, argument maps, and discriminating probes.
- `mixed`: protect discovery until convergence conditions are met, then switch to evidence discipline.
- `execution_delivery`: prioritize implementation, packaging, validation, delivery, and recovery.

Do not let an evidence lookup become the global target while the model is unsettled. Do not keep divergent research open after discriminating evidence and convergence criteria are satisfied.

## 6. Conditional Organization And Portfolio Control

Ordinary projects stay with the kernel. Activate this section only when work has recurring responsibilities, multiple modules, independent evaluation, or a demonstrated local-greedy routing problem.

The controller owns:

- direction: Goal, target function, project nature, completion and stop conditions;
- authority: responsibility boundary and external commitments;
- state: current basis, active modules, risks, accepted artifacts, and context health;
- topology: standing lanes, temporary workers, platform resources, and evaluator independence;
- routing: beat queue, branch parking, retry/recovery, and residual scan;
- calibration: external basis, hallucination sentinel, and mechanism maturity.

Each durable lane contract names responsibility, accepted input, accepted output, wake trigger, context policy, manager acceptance test, retirement condition, and current owner/resource evidence. A recorded lane is not a spawned platform resource. If a thread, subagent, worktree, or automation is created, retain the observed resource identifier and status; otherwise describe only the manager-owned responsibility.

Create only the standing lanes whose responsibilities recur:

- Controller: direction, portfolio, route, stop/park decisions.
- Human interface: responsibility-bearing asks, explanations, and delivery alignment.
- Literature/data acquisition: papers, official sources, databases, permission forecasts, and source escalation.
- Model/component: assumptions, variables, interfaces, and vertical slices.
- Data-code: schemas, scripts, hashes, reproducibility, and write boundaries.
- Review/risk: clean-context evaluation, overclaim, false precision, and public-risk review.
- Writing/delivery: claims, figures, methods, limitations, and reader-facing output.

Standing lanes are responsibilities, not mandatory threads. Use manager work, subagents, clean reviewers, worktrees, threads, or automations according to harness capability and task shape. Independent review requires a clean reviewer, separate context, fact-ledger packet, or read-only audit worker; same-session review is diagnostic only.

## 7. Responsibility Boundary

AI decides project-internal orchestration: planning, reading, verification depth, reversible local commands, Plan/Goal fit, topology fit, context compaction, temporary worker splits, convergence pacing, and next-beat routing. This is the default ownership class, not a low-risk exception.

Ask the user for responsibility-bearing boundaries:

- main-goal, public-voice, or delivery-contract changes;
- account credentials, paid services, publication, or external writes;
- irreversible shared-state changes;
- high-risk real-world actions or unsupported strong public claims;
- human value judgments not delegated by the project.

Before asking, prove the issue requires user authority or judgment. If state, files, links, or `next_route` already define an executable internal next step, continue. Read accessible directories and materials before asking the user to summarize them.

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

Important structural decisions use compact ADR form: Context, Decision, Consequences, Superseded by.

## 12. Planning, Cadence, And Stop Conditions

Use a planning checkpoint at project start, phase switch, strategic/model/method/evaluation change, significant user correction, repeated guardrail-only work, or public delivery.

Before each continuous beat:

1. rehydrate the Prompt Contract;
2. assemble and verify the Context Working Set;
3. confirm Harness capability and degraded routes;
4. choose `beat_objective` and completion predicate;
5. execute the Progress Loop;
6. evaluate outcome and route the next beat.

Continue queued beats inside the responsibility boundary. Do not stop because a fixed number of beats ran. `STOP_COMPLETE` requires objective completion, delivery-level validation, and a residual scan showing no useful internal beat remains.

An accepted beat is not completion of the Codex Goal. Keep the `thread_goal` or `phase_goal` active while the residual scan still finds useful queued work. Mark it complete only when the Goal-level outcome predicate, delivery validation, and residual scan all pass.

## 13. Delivery Contract

Before output, align the reader's task, delivery surface, audience, purpose, granularity, tone, evidence/claim ceiling, sensitive-information boundary, and acceptance test.

Human-facing output explains the project in ordinary language. Machine recovery state and runtime observability remain separate unless requested. If the user asks for human-readable output only, do not expose YAML, verifier internals, protocol fields, or private operational detail unless they affect the reader's decision.

Delivery-contract terms are an internal selection aid, not a required table of contents. Lead with the facts and decision the reader needs; preserve requested quantities and limitations; omit labels such as reader task, claim ceiling, gate, or acceptance condition unless those labels themselves help the reader act.

Routine progress uses minimum sufficient observability: what target-function segment moved, what artifact changed, what uncertainty changed, what cannot yet be claimed, and the next route. Heavy evidence packs are for phase switches, public delivery, claim upgrades, contradictions, evaluator handoff, or explicit audit.

## 14. Runtime Kit And Evaluation

Templates are optional landing pads, not mandatory fields. Use filled examples before blank templates.

Routine fixes use the normal edit-and-test path. A substantial change is one that adds a public term, schema, protocol default, Codex-surface contract, or maturity promotion. It records a compact decision packet: problem evidence, external implementation, alternatives, drawbacks, compatibility impact, evaluation plan, rollback, owner, and decision status.

Protocol maintenance sequence:

1. Capture the failure as an outcome and trajectory record.
2. Diagnose Prompt, Context, Harness, Loop, or model limitation.
3. Add or refine a behavior case and transcript rule.
4. Calibrate against external practice and state transfer boundaries.
5. Record a versioned evaluation case, run, and score when making a comparison claim.
6. Update a filled example and mechanism maturity evidence only when their teaching or status changes.
7. Change normative role to `core` only when the behavior is a repeated, high-impact universal boundary; change evidence status to `validated` only through the independent real-outcome standard. Never infer one axis from the other.

Examples illustrate. Markers and checkers screen. Fixed-version fixtures reproduce. Locked baseline/candidate runs compare. Repeated real Complex outcomes validate. Do not use a stronger verb than the evidence record supports.

Do not add history archives, long machine-board logs, dated release packages, or one-off recovery records to the active protocol.
