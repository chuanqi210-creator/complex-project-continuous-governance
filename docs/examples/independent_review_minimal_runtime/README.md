# Independent Review Minimal Runtime

Use this example when a project needs review quality beyond same-session self-critique.

This is not a new mandatory Runtime Kit template. It is a filled example for the `independent_review_context_separation` behavior case.

## What It Shows

- A fact ledger that gives a reviewer evidence, claims, decisions, and open questions without the full persuasion-heavy chat history.
- A clean-context review route for true independent review.
- A same-session diagnostic route when independence is not required or no separate reviewer is available.
- The boundary between "useful self-check" and "independent audit."
- How a recurring review/evaluation responsibility becomes a standing lane instead of a one-off subagent.
- A context-reset policy for each review beat.

## Files

- `state.md`: current review state and behavior-kernel trace.
- `fact-ledger.md`: reviewer input packet.
- `judgment.md`: decision rights and review independence judgment.
- `decision.md`: selected route, rejected routes, and downgrade rules.
- `delivery.md`: how to present same-session diagnostic vs independent review outputs.

## Four-Layer Boundary

- Prompt Contract: review criteria and decision audience remain stable.
- Context Working Set: the reviewer receives a fact ledger, not the persuasion-heavy manager transcript.
- Runtime Harness: clean reviewer context, read-only access, and observable evidence are required for a true independent label.
- Progress Loop: review completes from criterion-level findings and evidence, not from the reviewer saying the artifact looks good.

This example does not prove that a same-session diagnostic is independent or that every review needs another model.
