# Behavior Review

Complex behavior review answers one question: did the runtime produce a better project outcome with less user correction?

The behavior pack and transcript rules are structural screens. They catch missing triggers and forbidden patterns, but they do not validate a mechanism.

## Review Flow

1. Name the mechanism under test, select a behavior case, and freeze its version.
2. Record a baseline run and candidate run on the same project snapshot when comparison is intended.
3. For Goal, thread, subagent, automation, approval, retry, or routing claims, capture the structured runtime event ledger before reading the final prose.
4. Verify run health and project-contract parity before comparing arms; systemic transport/tool failure is Harness evidence, not a mechanism loss.
5. Apply marker screening to the human-visible transcript; never use a marker as a substitute for a tool event.
6. Score project outcome, exact artifact/schema compliance, correction cost, continuation, recovery, responsibility boundary, and process burden.
7. Use a clean independent model reviewer for trajectory diagnosis and a blind human reviewer for promotion decisions; do not merge those roles.
8. Keep, revise, demote, retire, or schedule another run.

The lightweight reviewer accepts normalized event-ledger lines in this form:

```text
COMPLEX_EVENT {"event_type":"tool_result","tool":"create_goal","status":"active","resource_id":"redacted-id"}
```

This proves only that the supplied review packet contains a structured event. Preserve the original surface trace or a private immutable pointer when provenance matters.

The machine-readable record is defined in `docs/evals/complex-eval-record.schema.json`. Do not create a second ad hoc review schema in prose.

## Human Outcome Questions

- Did the agent move the target function rather than merely pass a guard?
- Did it continue when the next internal step was clear?
- Did it stop at a real responsibility or tool boundary?
- Did it preserve the durable Goal while changing the beat objective?
- Did it recover current basis, active module, risks, and next route?
- Did it create a useful outcome, route decision, falsified branch, or other declared completion result?
- Did external calibration change a decision, or merely add citations?
- Did the user need fewer corrections?
- Did Complex remain mostly invisible to the human reader?

## Maturity Decisions

Use evidence verbs precisely:

- examples **illustrate**;
- transcript markers **screen**;
- local fixtures **reproduce**;
- locked runs **compare**;
- repeated real outcomes **validate**.

`screened -> tested` requires a behavior case, transcript rule, landing point, external implementation basis, and a valid bounded outcome run that instantiates the claimed mechanism.

`tested -> validated` requires locked baseline/candidate comparison, independent candidate-preferring human review, and repeated evidence from at least two distinct real or redacted-real project samples. A checker pass, an upstream benchmark, or one successful self-run is insufficient.

Demote or retire a mechanism when it duplicates the kernel, increases visible ceremony, conflicts with Codex, or passes markers while failing human review.

## Privacy And Storage

- Do not commit raw private transcripts by default.
- Store redacted summaries or private Cold Archive pointers.
- Keep eval cases, run metadata, scores, and maturity decisions compact and immutable.
- Re-score an existing run by adding a score record; do not rewrite the original run.

## Repository Change Rule

Routine fixes use the normal edit-and-test path. New public terms, schemas, protocol defaults, Codex-surface contracts, or maturity promotions require a compact substantial-change packet containing problem evidence, external implementation evidence, alternatives, drawbacks, compatibility, evaluation, rollback, owner, and decision status.

The first full packet is `docs/active-architecture-rebaseline.json`.
