# External Methods Mapped To Complex

Complex borrows method shapes, not dependencies. External methods are useful only when they become project micro-contracts.

## Calibration Rule

For every mechanism-level issue, record:

- source;
- problem matched;
- adopted;
- rejected;
- not transferable;
- Complex micro-contract;
- refresh trigger.

Do not name-drop a framework. A reference is useful only when it changes how the project starts, routes, validates, reviews, compacts, or stops.

## Full Benchmark Matrix

| Issue | External source | Transfer boundary | Complex micro-contract |
| --- | --- | --- | --- |
| Key problems should first look outside | NIST AI RMF govern/map/measure/manage; Anthropic Building Effective Agents; OpenAI Agents SDK guardrails/handoffs | External frameworks do not replace local project facts or Codex surface rules. | Before strategic route, method, model, evaluation, prompt-default, or protocol changes, create `external_calibration`: source, problem matched, adopted, rejected, not transferable, micro-contract, refresh trigger. |
| Periodic hallucination control | NIST AI RMF GenAI Profile / AI 600-1 confabulation risk; NIST Measure/Manage | NIST gives risk structure, not project truth. | Run `hallucination_sentinel` at startup, every 5 accepted beats, phase switch, public delivery, model/source/prompt upgrade, external calibration, or before promoting a rule. |
| Golden examples must remain current | OpenAI Skills progressive disclosure; Codex AGENTS.md practical guidance; Anthropic agent evals | Examples should teach shape, not become required forms. | Each golden example needs currentness review: current terminology, Goal/Plan/Loop relation, operating organization, external calibration, hallucination sentinel, trace appraisal, forward artifact. |
| Loop can become local greedy work | CRISP-DM business/data/model/evaluation iteration; NASA lifecycle/gate reviews; Google SRE toil control | Do not import heavy stage gates for small beats. | Replace "lightest action" with target-function Loop: every Loop names target function, module, lane, forward artifact, and why it is not local greedy optimization. |
| Plan mode cannot be auto-enabled but planning is mandatory at key beats | OpenAI Codex manual: Plan mode gathers context and builds stronger plans before implementation | Complex cannot toggle UI Plan mode. | `planning_checkpoint_for_key_beats`: at project start, phase switch, strategic/method changes, user correction, repeated guardrail-only work, or public delivery, output a plan-shaped checkpoint and continue inside the responsibility boundary. |
| Goal semantics drift | OpenAI Codex Goal mode: persistent objective and completion criteria across longer tasks | Codex Goal should not carry concrete next-step chores across many beats. | Use `thread_goal` / `phase_goal` for durable objective and completion criteria; use `beat_objective` for per-beat Plan/Loop. |
| Historical aliases pollute active docs | Codex AGENTS.md guidance: concise, practical, based on repeated mistakes; OpenAI Skills trigger clarity | Migration compatibility is handled by Git history, not active public docs. | Active docs use only current terms: `thread_goal`, `phase_goal`, `beat_objective`, `goal_memory_summary`. |
| User authorization boundary is overbroad | OpenAI Agents SDK guardrails/human review; Codex approval/security model | "Low risk" is too vague for project governance, and platform-resource fit is an orchestration decision before it is an authorization question. | Ask only for responsibility-bearing boundaries: main-goal/public-voice change, accounts/API/payment, external write, publishing, irreversible action, high-risk claim/action, or platform actions that create user-owned external commitments. |
| Skill should be a reusable experience template | OpenAI Agent Skills progressive disclosure and concise descriptions | Skill should not duplicate all protocol details. | `.agents/skills/complex-runtime/SKILL.md` carries the project view, Codex surface map, operating organization, target-function Loop, external calibration, hallucination sentinel, trace appraisal, and output defaults. |
| Guardrail-only beats can become mechanical | Google SRE toil; NASA entry/success criteria | Do not force a single next action mechanically. | Repeated guardrail-only work triggers toil/WIP review: create a forward artifact, park the branch, route to another module, or justify true dependency. |
| Long-term thread design needs organization | Team Topologies; OpenAI Subagents; Codex Automations; Agents SDK handoffs | Subagents are bounded workers; platform threads/automations are user-visible resources. | Build `operating_organization`: controller, human interface, literature/data, model/component, data-code, review/risk, writing/delivery. Lanes are responsibilities; workers are optional execution resources. |
| Prose and structure must remain unified | Codex AGENTS.md short guidance; ADR lightweight decisions; Skills progressive disclosure | Do not hide complexity by deleting necessary recovery surfaces. | Core protocol keeps philosophy/surface/organization/flow/evaluation; details live in templates/examples; important structural changes use ADR-style Context/Decision/Consequences/Superseded by. |
| Reading flow must be precise | Codex AGENTS discovery; Skills progressive disclosure; NIST governance lifecycle | Do not read every artifact for every beat. | Runtime read order: resolve rule source, read active entrypoints, recover Hot State, read target facts, form operating organization, run planning checkpoint, execute current beat; use Warm/Cold only by pointer when needed. |
| Default prompt must carry real architecture | Codex prompting and Plan mode guidance; Skills default prompts; AGENTS durable guidance | A prompt is not a replacement for protocol or current facts. | Provide high-fidelity startup prompt, project master prompt, per-beat planning prompt, and compact continuation prompt. |
| Scheduled retrospectives should continue the project | NIST Measure/Manage; Google SRE toil review; ADR superseding decision | Review should not become a pause ritual. | Every 5 accepted beats or phase switch: structure review + hallucination sentinel + trace appraisal; then either adjust, supersede, park, or continue through Beat Router. |
| Literature/source acquisition should be planned early | PRISMA transparent source flow and exclusion records; research data-management practice | PRISMA is too heavy for every source lookup. | Literature/data lane forecasts database/account needs early, records source flow, exclusion/no-hit reasons, and exact user responsibility asks when access is required. |

## Reference Anchors

- OpenAI Codex Goals: https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex
- OpenAI Codex Subagents: https://developers.openai.com/codex/subagents
- OpenAI Codex Skills: https://developers.openai.com/codex/skills
- OpenAI AGENTS.md: https://developers.openai.com/codex/guides/agents-md
- OpenAI Codex Automations: https://developers.openai.com/codex/app/automations
- OpenAI Agents SDK Guardrails: https://openai.github.io/openai-agents-python/guardrails/
- OpenAI Agents SDK Handoffs: https://openai.github.io/openai-agents-python/handoffs/
- Anthropic Building Effective Agents: https://www.anthropic.com/research/building-effective-agents
- Anthropic agent evals: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- NIST AI RMF Core: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/
- NIST GenAI Profile: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- Google SRE Eliminating Toil: https://sre.google/sre-book/eliminating-toil/
- NASA Systems Engineering Handbook: https://www.nasa.gov/wp-content/uploads/2018/09/nasa_systems_engineering_handbook_0.pdf
- IBM CRISP-DM Guide: https://www.ibm.com/docs/it/SS3RA7_18.3.0/pdf/ModelerCRISPDM.pdf
- PRISMA Statement: https://www.prisma-statement.org/
- Team Topologies key concepts: https://teamtopologies.com/key-concepts
- Architecture Decision Records: https://adr.github.io/

## How To Use This Document

Use this document when:

- a strategic or structural Complex rule is being changed;
- a user reports a repeated project-execution failure;
- a prompt default or behavior case is being promoted;
- a project route could become local greedy optimization;
- a long project needs state compaction, review independence, or operating-organization design.

Routine beats can reuse a fresh calibration note. Refresh when project nature changes, the method is novel, the prior map is stale, or the decision will guide many future beats.
