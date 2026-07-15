# Complex Continuous Governance Core

Complex is a Codex-native runtime for long-running complex projects. It keeps durable intent, the current working set, the execution environment, and progress control aligned without turning the user into the scheduler.

Core model:

> a stable seven-behavior spine, supported by four coupled engineering layers: Prompt Contract, Context Working Set, Runtime Harness, and Progress Loop.

The four layers are operating planes, not a linear maturity ladder and not four new gates. A failure in one layer must not be patched blindly in another. Mechanism maturity is tracked in `docs/mechanism-maturity.json`; external precedent makes a mechanism grounded, not validated.

## 1. Project Philosophy And Target Function

Complex optimizes for durable progress toward the project target function:

- hold the top-level intent while executing bounded beats;
- form an early thin end-to-end closure before polishing local details;
- use mature external practice before changing strategic methods or protocol defaults;
- preserve enough evidence and recovery state for review without making reporting the project;
- let AI decide project-internal orchestration while reserving responsibility-bearing choices for the user.

The main failure is local greed: optimizing the nearest visible detail while the project needs a better route, a vertical slice, a parallel responsibility lane, a context reset, a harness repair, or a higher-level decision. The second failure is governance drag: producing so much proof, state, or ceremony that governance consumes the work.

## 2. Codex Surface Alignment

`codex_surface_alignment` maps Complex onto Codex instead of competing with it.

- Plan mode is a user/interface planning surface. At project start and strategic beats, run a planning checkpoint. Use UI Plan mode when the current surface exposes it; otherwise produce a plan-shaped checkpoint and continue. Never claim a surface was enabled when it was not.
- Codex Goal carries a persistent objective and completion criteria for a longer task, thread, or bounded phase. Complex calls the contract `thread_goal` or `phase_goal`. Do not put changing beat chores into it.
- `beat_objective` is the current Plan/Loop target. `goal_memory_summary` is a recovery digest, not Codex Goal.
- Continuous cadence means same-run execution of queued beats until objective completion or a real responsibility/tool boundary. Cross-turn continuation maps to a thread heartbeat or automation when the available surface supports it. When the user has selected cross-turn continuous work and a callable heartbeat/automation tool is available, activate it during Runtime Harness setup and retain resource evidence; merely recommending it for later is not activation. If the surface is unavailable, continue same-run work and leave an exact recovery route without pretending the task will wake itself.
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

A discovered recovery anchor is usable only when its authority is explicit, its freshness is assessable, its Hot State is bounded, and it exposes one authoritative next route. If state files are oversized or disagree, do not choose by recency alone and do not load a large manifest wholesale. Route first to a bounded state-reconciliation beat: compare only route/status keys and accepted pointers, preserve contradictions, compact one Hot State, and demote large ledgers to Warm Index.

`bounded inspection` is an execution budget, not an adjective. Measure file, line, or top-level-key scale before querying content. Start with metadata and local key names/types; retrieve values only for a small set of directly selected keys. The default first-pass envelope is at most 50 matched names or 80 text lines, 32 KiB of tool output, and 30 seconds for one source, unless the project declares a tighter or justified wider budget. Truncation, timeout, or a match count beyond the envelope signals that the source is not directly usable as the current working set under that envelope; it does not by itself decide authority. Stop, retain a pointer and contradiction note, and do not retry with a broader expression. When the pattern recurs, the manager uses a deterministic bounded extractor and gives a content-minimized ledger, not source snippets or raw key names, to a clean evaluator; the manager/watchdog enforces hard elapsed-time limits instead of asking a worker to self-timeout.

The working set distinguishes:

- stable instructions and project contract;
- Hot State and the active module;
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

`agent_legibility`: information needed to act or validate should be inspectable in the repository, state, environment, or tool output, not trapped only in chat history or human memory.

`interrupt_resume_safety`: when a beat must pause for user authorization, external input, or platform approval, separate pre-authorization read/draft work from post-authorization side effects. Any side effect before the pause must be idempotent, reversible, or explicitly compensatable; otherwise interrupt before the side effect and record the exact approval payload, checkpoint, idempotency key or stable identifier, and resume route.

Discover capabilities just in time. Do not load every tool or skill into every beat. If a rule repeats and can be checked mechanically, prefer a checker over another paragraph of instructions.

### 3.4 Progress Loop

Loop engineering controls durable progress:

`restore -> select beat -> act -> observe environment -> evaluate outcome -> route/retry/rollback/stop`

Each Loop declares:

- target function, module, and standing lane served;
- `beat_objective` and Loop type;
- expected forward artifact and outcome completion predicate;
- relevant guard and independent evaluator when needed;
- failure class and recovery route;
- time, token, tool-call, and WIP budget;
- why the beat is not local greedy optimization.

Important Loop completion is based on environment state, tests, artifacts, or external outcomes, not a fixed beat count or the agent saying it is done. Outcome evaluation comes first; trajectory review explains why the outcome happened.

Retry only retryable failures. Use checkpoint, exponential backoff where appropriate, stable identifiers, and idempotent or compensating actions. Budgets limit waste and side effects; they do not create premature completion.

## 4. Seven-Behavior Execution Spine

`complex_behavior_kernel` remains the execution spine:

1. Restore true state and assemble the current Context Working Set.
2. Classify `project_nature`: `evidence_fill`, `model_discovery`, `mixed`, or `execution_delivery`.
3. Assign decision rights through the responsibility boundary.
4. Establish the control plane, operating organization, and Runtime Harness before local optimization.
5. Run the smallest meaningful target-function Progress Loop or execution beat.
6. Deliver to the right audience and evaluate the outcome.
7. Leave `next_route`, accepted artifacts, recovery pointers, and any layer-level diagnosis.

Named mechanisms are implementation guidance. If one conflicts with the spine, the spine wins. Candidate mechanisms apply only when their matching failure mode is present.

## 5. Project Nature And Convergence

- `evidence_fill`: model, metric, formula, or frame is stable. Fill evidence, validate claims, and deliver without paying unnecessary divergence overhead.
- `model_discovery`: the problem frame, model, metric, explanation, or story line is unsettled. Preserve 3-5 candidate frames, counterexamples, argument maps, and discriminating probes.
- `mixed`: protect discovery until convergence conditions are met, then switch to evidence discipline.
- `execution_delivery`: prioritize implementation, packaging, validation, delivery, and recovery.

Do not let an evidence lookup become the global target while the model is unsettled. Do not keep divergent research open after discriminating evidence and convergence criteria are satisfied.

## 6. Control Plane And Operating Organization

The controller owns:

- direction: Goal, target function, project nature, completion and stop conditions;
- authority: responsibility boundary and external commitments;
- state: current basis, active modules, risks, accepted artifacts, and context health;
- topology: standing lanes, temporary workers, platform resources, and evaluator independence;
- routing: beat queue, branch parking, retry/recovery, and residual scan;
- calibration: external basis, hallucination sentinel, and mechanism maturity.

Create standing lanes when responsibilities recur:

- Controller: direction, portfolio, route, stop/park decisions.
- Human interface: responsibility-bearing asks, explanations, and delivery alignment.
- Literature/data acquisition: papers, official sources, databases, permission forecasts, and source escalation.
- Model/component: assumptions, variables, interfaces, and vertical slices.
- Data-code: schemas, scripts, hashes, reproducibility, and write boundaries.
- Review/risk: clean-context evaluation, overclaim, false precision, and public-risk review.
- Writing/delivery: claims, figures, methods, limitations, and reader-facing output.

Standing lanes are responsibilities, not mandatory threads. Use manager work, subagents, clean reviewers, worktrees, threads, or automations according to harness capability and task shape. Independent review requires a clean reviewer, separate context, fact-ledger packet, or read-only audit worker; same-session review is diagnostic only.

## 7. Responsibility Boundary

AI decides project-internal orchestration: planning, reading, verification depth, reversible local commands, Plan/Goal fit, topology fit, context compaction, temporary worker splits, convergence pacing, and next-beat routing.

Ask the user for responsibility-bearing boundaries:

- main-goal, public-voice, or delivery-contract changes;
- account credentials, paid services, publication, or external writes;
- irreversible shared-state changes;
- high-risk real-world actions or unsupported strong public claims;
- human value judgments not delegated by the project.

Before asking, prove the issue requires user authority or judgment. If state, files, links, or `next_route` already define an executable internal next step, continue. Read accessible directories and materials before asking the user to summarize them.

Classify new user input as fact, preference, responsibility authorization, local correction, goal change, or possible noise. Local corrections patch the current beat or contract; they do not silently replace the Goal.

## 8. Progress, Evidence, And Early Closure

A beat is accepted only when it:

- creates or updates a forward artifact;
- passes the relevant guard;
- updates the affected state or index;
- selects the next route from observed results.

Forward artifacts include model, data, parameter, writing, branch, topology, calibration, harness, context, prompt, and state deltas.

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

Every mechanism-level calibration records:

- source and production problem matched;
- adopted and rejected patterns;
- what is not transferable;
- Complex micro-contract;
- refresh trigger.

External evidence grounds a design; it does not validate Complex behavior. Validation requires real transcripts or end-to-end project outcomes.

Run the hallucination sentinel at project startup, phase switches, important source/model/prompt/harness upgrades, external calibration, public delivery, before core promotion, and normally every 5 accepted beats. Separate `current_basis`, `external_basis`, `inference`, `unsupported_claim`, and `falsification_cue`.

## 11. State, Context Health, And Trace Appraisal

- Hot State: one-page current map, Goal, target function, active modules, beat queue, open risks, prohibitions, and next route.
- Warm Index: compact module, evidence, parameter, decision, lane, artifact, and evaluation ledgers.
- Cold Archive: raw traces, superseded prompts, old searches, screenshots, command output, and retired branches by pointer.

Demote stale traces before extending Hot State. Run trace appraisal when Hot State exceeds about 80 lines, a state file exceeds about 800 lines, 10 accepted beats accumulate, context pollution appears, or a phase/reviewer handoff is due.

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

Before output, align audience, purpose, granularity, tone, and internal-information boundary.

Human-facing output explains the project in ordinary language. Machine recovery state remains separate unless requested. If the user asks for human-readable output only, do not expose YAML, verifier internals, or protocol fields unless they affect the reader's decision.

Routine progress uses minimum sufficient observability: what target-function segment moved, what artifact changed, what uncertainty changed, what cannot yet be claimed, and the next route. Heavy evidence packs are for phase switches, public delivery, claim upgrades, contradictions, evaluator handoff, or explicit audit.

## 14. Runtime Kit And Evaluation

Templates are optional landing pads, not mandatory fields. Use filled examples before blank templates.

Protocol maintenance sequence:

1. Capture the failure as an outcome and trajectory record.
2. Diagnose Prompt, Context, Harness, Loop, or model limitation.
3. Add or refine a behavior case and transcript rule.
4. Calibrate against external practice and state transfer boundaries.
5. Update a filled example and mechanism maturity evidence.
6. Promote to core only after repeated, high-impact evidence.

Do not add history archives, long machine-board logs, dated release packages, or one-off recovery records to the active protocol.
