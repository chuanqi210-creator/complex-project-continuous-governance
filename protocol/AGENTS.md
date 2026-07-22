# AGENTS.md

## Purpose

`protocol/` contains the current Complex protocol and current recovery state. Keep this directory concise.

## Active Files

- `core.md`: behavior rules for Complex.
- `current-state.md`: current recovery anchor and next route.

## Editing Rules

- Put durable core behavior changes in `core.md`; put mechanism evidence and status in `docs/mechanism-maturity.json`.
- Keep Prompt Contract, Context Working Set, Runtime Harness, and Progress Loop as coupled operating planes under the seven-behavior spine. Diagnose the failed plane before adding wording; do not append four new gate families.
- Keep Codex surface semantics in `core.md` under `codex_surface_alignment`; do not scatter Plan/Goal/thread/subagent/automation reinterpretations across dated notes.
- Keep adaptive work topology in `core.md` as one unified rule: project nature is a prior, active work units route locally, artifact contracts precede resources, and one controller integrates manager work, deterministic Harness, temporary workers, recurring lanes, clean evaluation, and branch parking. Avoid fixed domain role charts and one-off gates.
- Treat Framework Grilling as part of Prompt Contract formation, not a new mechanism family. Preserve the responsibility boundary: factual, reversible, tool, topology, and implementation questions remain AI-owned.
- Treat self-optimization as a maintenance mode inside the behavior kernel, external calibration, evaluation, and maturity system. Routine corrections stay light; substantial changes keep a stable baseline, a reversible candidate, explicit graduation/failure criteria, progressive evidence rollout, and a residual evidence scan.
- Keep time convergence inside Prompt, Harness, Loop, and Delivery rather than creating a standalone gate. Long work defines a stage result horizon and usable increment; time pressure changes scope or route, never the quality/evidence floor or completion truth.
- Keep cross-boundary state reconciliation inside Context, Harness, portfolio control, and trace appraisal rather than creating a second state-manager mechanism. Local sources retain bounded authority; the controller owns a compact global control projection and refreshes it on meaningful events or measured staleness, not on every beat.
- Keep external transfer discipline in `core.md`. Keep operating organization, portfolio control, and trace appraisal conditional; do not turn candidates into universal startup ceremony. Do not solve context bloat by appending long logs or solve claim risk by naming external frameworks without implementation evidence and transfer limits.
- Put detailed runtime shapes in `templates/prompt.md`, `templates/context.md`, `templates/harness.md`, and `templates/loop.md` instead of expanding the core with fields.
- Put only the latest recoverable state in `current-state.md`; do not append long historical logs.
- If a change is better taught by a filled example, put it in `docs/examples/` and link it from mechanism maturity instead of expanding the core protocol.
- Do not add historical archives, migration notes, release packages, or dated machine-board chains to this directory.

## Verification

After protocol edits, run:

```bash
python3 tools/check_behavior_regression_pack.py
python3 tools/review_behavior_transcript.py --validate-rules
python3 tools/check_mechanism_maturity.py
python3 tools/check_active_architecture_rebaseline.py
python3 tools/check_eval_records.py
python3 tools/check_mechanism_revalidation_results.py
python3 tools/check_reference_implementation_evidence.py
python3 tools/test_inspect_recovery_anchor.py
python3 tools/test_verify_complex_integrity.py
python3 tools/verify_complex_integrity.py
```
