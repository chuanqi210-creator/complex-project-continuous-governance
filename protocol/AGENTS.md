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
- Keep portfolio orchestration in `core.md` as a unified control-plane rule: target function, module portfolio, standing lane portfolio, forward indexes, branch parking, and Hot/Warm/Cold state. Avoid adding one-off gates for each project failure.
- Keep trace appraisal and external calibration in `core.md` as control-plane rules. Do not solve context bloat by appending more long logs, and do not solve hallucination risk by naming external frameworks without transfer limits.
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
python3 tools/test_inspect_recovery_anchor.py
python3 tools/test_verify_complex_integrity.py
python3 tools/verify_complex_integrity.py
```
