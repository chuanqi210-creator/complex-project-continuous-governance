#!/usr/bin/env python3
"""Verify the active Complex Runtime Kit structure.

This replaces the old long-log recovery verifier. It checks the current
runtime kit, not historical machine-board chains.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "AGENTS.md",
    "protocol/AGENTS.md",
    "protocol/core.md",
    "protocol/current-state.md",
    "docs/quickstart.md",
    "docs/behavior-regression-cases.json",
    "docs/behavior-transcript-review-rules.json",
    "docs/behavior-review.md",
    "docs/mechanism-maturity.md",
    "docs/mechanism-maturity.json",
    "docs/active-architecture-rebaseline.md",
    "docs/active-architecture-rebaseline.json",
    "docs/reference-implementation-evidence.json",
    "docs/self-optimization.md",
    "docs/evals/README.md",
    "docs/evals/complex-eval-record.schema.json",
    "docs/evals/bounded-experiment-fixtures.json",
    "docs/evals/bounded-experiment-output.schema.json",
    "docs/evals/executable-mechanism-fixtures.json",
    "docs/evals/executable-pilot-output.schema.json",
    "docs/evals/experiment-program.json",
    "docs/evals/experiment-program.md",
    "docs/evals/results/executable-pilots-20260717T145657Z-4db18e9646-gpt-5.6-luna.json",
    "docs/evals/results/executable-pilots-20260717T171657Z-a091c06076-rescore.json",
    "docs/evals/results/scorer-repair-external-calibration-20260718.json",
    "docs/evals/results/mechanism-revalidation-independent-model-review-20260718.json",
    "docs/evals/records/active-architecture-rebaseline-comparison.json",
    "docs/evals/reference-langgraph-checkpoint.py",
    "docs/evals/reference-promptfoo-echo.yaml",
    "docs/examples/example-currentness.md",
    "docs/runtime-skill-management.md",
    "docs/external-methods.md",
    ".agents/skills/complex-runtime/SKILL.md",
    ".codex/shared-skills.json",
    ".codex/skills/README.md",
    "tools/check_behavior_regression_pack.py",
    "tools/review_behavior_transcript.py",
    "tools/check_mechanism_maturity.py",
    "tools/check_active_architecture_rebaseline.py",
    "tools/check_eval_records.py",
    "tools/check_experiment_program.py",
    "tools/check_mechanism_revalidation_results.py",
    "tools/check_reference_implementation_evidence.py",
    "tools/run_bounded_experiments.py",
    "tools/run_executable_mechanism_pilots.py",
    "tools/rescore_executable_mechanism_pilots.py",
    "tools/test_run_executable_mechanism_pilots.py",
    "tools/inspect_recovery_anchor.py",
    "tools/test_inspect_recovery_anchor.py",
    "tools/verify_complex_integrity.py",
    "tools/test_verify_complex_integrity.py",
]

REQUIRED_TEMPLATES = [
    "argument.md",
    "context.md",
    "decision.md",
    "delivery.md",
    "evidence.md",
    "framing.md",
    "harness.md",
    "judgment.md",
    "loop.md",
    "prompt.md",
    "question.md",
    "search.md",
    "state.md",
]

REQUIRED_EXAMPLE_DIRS = [
    "docs/examples/evidence_fill_minimal_runtime",
    "docs/examples/model_discovery_minimal_runtime",
    "docs/examples/independent_review_minimal_runtime",
    "docs/examples/portfolio_orchestration_minimal_runtime",
    "docs/examples/external_calibration_micro_contract_runtime",
    "docs/examples/operating_organization_multi_lane_runtime",
]

FORBIDDEN_PATHS = [
    "docs" + "/" + "history",
    "docs" + "/" + "migration",
    "outputs",
    "tools/append_eof_section.py",
    "tools/scan_docx_links.py",
    "tools/verify_governance_recovery.py",
    "tools/test_verify_governance_recovery.py",
]

ALLOWED_ROOT_MD = {"AGENTS.md", "README.md"}
ALLOWED_PROTOCOL_MD = {"AGENTS.md", "core.md", "current-state.md"}

FORBIDDEN_TEXT = [
    "ai " + "\u79d1\u7814",
    "AI " + "\u79d1\u7814",
    "\u5386\u53f2" + "\u6765\u6e90",
    "\u8fc1\u79fb" + "\u6e05\u5355",
    "docs" + "/" + "history",
    "docs" + "/" + "migration",
    "outputs" + "/" + "front_governance_protocol" + "_v" + "2",
    "## " + str(200 + 24) + ". " + "\u5f53\u524d" + "\u673a\u5668" + "\u770b\u7248",
    "Complex项目持续治理协议" + "_v3_核心版",
    "behavior_regression_cases" + "_20260702",
    "behavior_transcript_review_rules" + "_20260702",
    "complex_new_agent_5_minute_quickstart" + "_20260702",
]

REQUIRED_REFERENCES = [
    "protocol/core.md",
    "protocol/current-state.md",
    "docs/quickstart.md",
    "docs/behavior-regression-cases.json",
    "docs/behavior-transcript-review-rules.json",
    "docs/mechanism-maturity.json",
    "docs/mechanism-maturity.md",
    "docs/active-architecture-rebaseline.json",
    "docs/active-architecture-rebaseline.md",
    "docs/reference-implementation-evidence.json",
    "docs/self-optimization.md",
    ".agents/skills/complex-runtime/SKILL.md",
]

FOUR_LAYER_TERMS = {
    "prompt": "Prompt Contract",
    "context": "Context Working Set",
    "harness": "Runtime Harness",
    "loop": "Progress Loop",
}

FOUR_LAYER_ENTRYPOINTS = [
    "README.md",
    "protocol/core.md",
    "docs/quickstart.md",
    ".agents/skills/complex-runtime/SKILL.md",
]

FLAGSHIP_EXAMPLE_FILES = [
    "README.md",
    "prompt.md",
    "context.md",
    "harness.md",
    "loop.md",
    "state.md",
]

FOUR_LAYER_BEHAVIOR_CASES = {
    "prompt_change_is_eval_driven_and_versioned",
    "context_working_set_is_curated_and_recoverable",
    "harness_legibility_and_mechanical_guardrails",
    "durable_loop_uses_outcome_completion_and_recovery",
    "cross_layer_failure_is_diagnosed_before_prompt_patch",
}

SEMANTIC_RECOVERY_LABELS = {
    "thread_goal": "- thread_goal:",
    "goal_surface_status": "- goal_surface_status:",
    "goal_resource_evidence": "- goal_resource_evidence:",
    "goal_completion_predicate": "- goal_completion_predicate:",
    "current_basis": "- current_basis:",
    "active_module": "- active_module:",
    "open_risks": "- open_risks:",
    "next_route": "- next_route:",
}


def recovery_value(text: str, label: str) -> str:
    prefix = f"- {label}:"
    for line in text.splitlines():
        if line.startswith(prefix):
            return line.removeprefix(prefix).strip()
    return ""


def read_json(relative: str) -> dict:
    path = ROOT / relative
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise AssertionError(f"missing JSON file: {relative}")
    except json.JSONDecodeError as exc:
        raise AssertionError(f"invalid JSON in {relative}: {exc}")
    if not isinstance(data, dict):
        raise AssertionError(f"expected JSON object: {relative}")
    return data


def active_text_files() -> list[Path]:
    roots = [
        ROOT / "README.md",
        ROOT / "AGENTS.md",
        ROOT / "protocol",
        ROOT / "docs",
        ROOT / "templates",
        ROOT / "tools",
        ROOT / ".codex",
        ROOT / ".agents",
    ]
    paths: list[Path] = []
    for root in roots:
        if root.is_file():
            paths.append(root)
            continue
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if not path.is_file():
                continue
            parts = set(path.relative_to(ROOT).parts)
            if "node_modules" in parts or "dist" in parts:
                continue
            if path.suffix.lower() in {".md", ".py", ".json", ".jsx", ".js", ".mjs", ".html", ".css"}:
                paths.append(path)
    return paths


def check(result: list[dict[str, object]], name: str, ok: bool, detail: object = "") -> None:
    result.append({"name": name, "ok": bool(ok), "detail": detail})


def main() -> None:
    checks: list[dict[str, object]] = []

    experiment_validation = subprocess.run(
        [sys.executable, str(ROOT / "tools" / "check_experiment_program.py")],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    check(
        checks,
        "external_calibrated_experiment_program",
        experiment_validation.returncode == 0,
        (experiment_validation.stdout + experiment_validation.stderr).strip(),
    )

    reference_validation = subprocess.run(
        [sys.executable, str(ROOT / "tools" / "check_reference_implementation_evidence.py")],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    check(
        checks,
        "reference_implementation_evidence_schema",
        reference_validation.returncode == 0,
        (reference_validation.stdout + reference_validation.stderr).strip(),
    )

    rebaseline_validation = subprocess.run(
        [sys.executable, str(ROOT / "tools" / "check_active_architecture_rebaseline.py")],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    check(
        checks,
        "active_architecture_rebaseline_schema",
        rebaseline_validation.returncode == 0,
        (rebaseline_validation.stdout + rebaseline_validation.stderr).strip(),
    )

    eval_record_validation = subprocess.run(
        [sys.executable, str(ROOT / "tools" / "check_eval_records.py")],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    check(
        checks,
        "structured_eval_records",
        eval_record_validation.returncode == 0,
        (eval_record_validation.stdout + eval_record_validation.stderr).strip(),
    )

    revalidation_result_validation = subprocess.run(
        [sys.executable, str(ROOT / "tools" / "check_mechanism_revalidation_results.py")],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    check(
        checks,
        "mechanism_revalidation_result_chain",
        revalidation_result_validation.returncode == 0,
        (revalidation_result_validation.stdout + revalidation_result_validation.stderr).strip(),
    )

    for relative in REQUIRED_FILES:
        check(checks, f"required_file:{relative}", (ROOT / relative).is_file())

    for template in REQUIRED_TEMPLATES:
        check(checks, f"template:{template}", (ROOT / "templates" / template).is_file())

    for directory in REQUIRED_EXAMPLE_DIRS:
        path = ROOT / directory
        check(checks, f"example_dir:{directory}", path.is_dir() and any(path.glob("*.md")))

    flagship = ROOT / "docs/examples/portfolio_orchestration_minimal_runtime"
    missing_flagship_files = sorted(
        name for name in FLAGSHIP_EXAMPLE_FILES if not (flagship / name).is_file()
    )
    check(
        checks,
        "four_layer_flagship_complete",
        not missing_flagship_files,
        missing_flagship_files,
    )

    for relative in FOUR_LAYER_ENTRYPOINTS:
        path = ROOT / relative
        content = path.read_text(encoding="utf-8", errors="ignore") if path.is_file() else ""
        missing_terms = sorted(
            layer for layer, term in FOUR_LAYER_TERMS.items() if term not in content
        )
        check(
            checks,
            f"four_layer_entrypoint:{relative}",
            not missing_terms,
            missing_terms,
        )

    current_state_text = (ROOT / "protocol/current-state.md").read_text(
        encoding="utf-8", errors="ignore"
    )
    missing_recovery_labels = sorted(
        name for name, label in SEMANTIC_RECOVERY_LABELS.items()
        if label not in current_state_text
    )
    authoritative_next_route_count = current_state_text.count("- next_route:")
    check(
        checks,
        "current_state_semantic_recovery_contract",
        not missing_recovery_labels and authoritative_next_route_count == 1,
        {
            "missing_labels": missing_recovery_labels,
            "authoritative_next_route_count": authoritative_next_route_count,
        },
    )
    next_route = recovery_value(current_state_text, "next_route")
    goal_surface_status = recovery_value(current_state_text, "goal_surface_status")
    goal_resource_evidence = recovery_value(current_state_text, "goal_resource_evidence")
    goal_completion_predicate = recovery_value(current_state_text, "goal_completion_predicate")
    terminal_route = next_route == "STOP_COMPLETE" or next_route.startswith(
        ("INTERRUPT_FOR_INPUT", "REAL_BOUNDARY", "BLOCKED")
    )
    recoverable_goal_contract = (
        goal_surface_status == "active_in_origin_task; recheck_required_on_resume"
        and "observed_in_origin_task" in goal_resource_evidence
        and "resource=" in goal_resource_evidence
        and "status=active" in goal_resource_evidence
    )
    unavailable_with_fallback = goal_surface_status.startswith("unavailable:") and "same_run_fallback=" in goal_surface_status
    check(
        checks,
        "nonterminal_next_route_declares_goal_runtime_contract",
        bool(next_route)
        and (
            terminal_route
            or (
                bool(goal_completion_predicate)
                and (recoverable_goal_contract or unavailable_with_fallback)
            )
        ),
        {
            "next_route": next_route,
            "goal_surface_status": goal_surface_status,
            "goal_resource_evidence": goal_resource_evidence,
            "goal_completion_predicate": goal_completion_predicate,
        },
    )

    for relative in FORBIDDEN_PATHS:
        check(checks, f"forbidden_path_absent:{relative}", not (ROOT / relative).exists())

    extra_root_md = sorted(path.name for path in ROOT.glob("*.md") if path.name not in ALLOWED_ROOT_MD)
    extra_protocol_md = sorted(
        path.name
        for path in (ROOT / "protocol").glob("*.md")
        if path.name not in ALLOWED_PROTOCOL_MD
    )
    check(checks, "root_md_allowlist", not extra_root_md, extra_root_md)
    check(checks, "protocol_md_allowlist", not extra_protocol_md, extra_protocol_md)

    pack = read_json("docs/behavior-regression-cases.json")
    rules = read_json("docs/behavior-transcript-review-rules.json")
    maturity = read_json("docs/mechanism-maturity.json")
    reference_evidence = read_json("docs/reference-implementation-evidence.json")
    cases = pack.get("cases")
    case_ids = {case.get("case_id") for case in cases if isinstance(case, dict)} if isinstance(cases, list) else set()
    required_ids = set(pack.get("required_case_ids", []))
    rule_ids = set(rules.get("case_rules", {}))
    mechanisms = maturity.get("mechanisms")
    mechanism_ids = {mechanism.get("id") for mechanism in mechanisms if isinstance(mechanism, dict)} if isinstance(mechanisms, list) else set()
    check(checks, "behavior_case_inventory_nonempty", bool(case_ids), sorted(case_ids))
    check(checks, "required_case_inventory_nonempty", bool(required_ids), sorted(required_ids))
    check(checks, "transcript_rule_inventory_nonempty", bool(rule_ids), sorted(rule_ids))
    check(checks, "behavior_cases_match_rules", case_ids == rule_ids == required_ids)
    check(checks, "mechanism_maturity_present", len(mechanism_ids) >= 10, sorted(mechanism_ids))

    references = reference_evidence.get("references")
    reference_ids = {
        reference.get("id")
        for reference in references
        if isinstance(reference, dict)
    } if isinstance(references, list) else set()
    transfer_statuses = {
        reference.get("transfer_status")
        for reference in references
        if isinstance(reference, dict)
    } if isinstance(references, list) else set()
    reproduced_references = {
        reference.get("id")
        for reference in references
        if isinstance(reference, dict) and reference.get("transfer_status") == "reproduced"
    } if isinstance(references, list) else set()
    reference_layers = {
        layer
        for reference in references or []
        if isinstance(reference, dict)
        for layer in reference.get("engineering_layers", [])
    } if isinstance(references, list) else set()
    check(
        checks,
        "reference_implementation_transfer_evidence",
        len(reference_ids) >= 11
        and len(reproduced_references) >= 2
        and reference_layers == set(FOUR_LAYER_TERMS)
        and "implementation_inspected" in transfer_statuses,
        {
            "references": sorted(reference_ids),
            "reproduced": sorted(reproduced_references),
            "layers": sorted(reference_layers),
            "statuses": sorted(status for status in transfer_statuses if status),
        },
    )

    four_layer_mechanism = next(
        (
            mechanism
            for mechanism in mechanisms
            if isinstance(mechanism, dict)
            and mechanism.get("id") == "complex_behavior_kernel"
        ),
        None,
    ) if isinstance(mechanisms, list) else None
    expected_layers = set(FOUR_LAYER_TERMS)
    actual_layers = set(four_layer_mechanism.get("engineering_layers", [])) if four_layer_mechanism else set()
    actual_linked_cases = set(four_layer_mechanism.get("linked_behavior_cases", [])) if four_layer_mechanism else set()
    check(
        checks,
        "four_layer_mechanism_maturity_boundary",
        bool(four_layer_mechanism)
        and four_layer_mechanism.get("normative_role") == "core"
        and four_layer_mechanism.get("evidence_status") in {"tested", "validated"}
        and actual_layers == expected_layers,
        {
            "normative_role": four_layer_mechanism.get("normative_role") if four_layer_mechanism else None,
            "evidence_status": four_layer_mechanism.get("evidence_status") if four_layer_mechanism else None,
            "layers": sorted(actual_layers),
        },
    )
    check(
        checks,
        "four_layer_behavior_coverage",
        FOUR_LAYER_BEHAVIOR_CASES <= case_ids
        and FOUR_LAYER_BEHAVIOR_CASES <= rule_ids
        and FOUR_LAYER_BEHAVIOR_CASES <= actual_linked_cases,
        {
            "missing_cases": sorted(FOUR_LAYER_BEHAVIOR_CASES - case_ids),
            "missing_rules": sorted(FOUR_LAYER_BEHAVIOR_CASES - rule_ids),
            "missing_maturity_links": sorted(FOUR_LAYER_BEHAVIOR_CASES - actual_linked_cases),
        },
    )
    external_calibration_mechanism = next(
        (
            mechanism
            for mechanism in mechanisms
            if isinstance(mechanism, dict)
            and mechanism.get("id") == "external_calibration_rule"
        ),
        None,
    ) if isinstance(mechanisms, list) else None
    external_cases = set(external_calibration_mechanism.get("linked_behavior_cases", [])) if external_calibration_mechanism else set()
    check(
        checks,
        "reference_transfer_behavior_and_maturity_link",
        "reference_implementation_transfer_requires_reproduction" in case_ids
        and "reference_implementation_transfer_requires_reproduction" in rule_ids
        and "reference_implementation_transfer_requires_reproduction" in external_cases,
        sorted(external_cases),
    )
    missing_layer_maps = sorted(
        mechanism.get("id")
        for mechanism in mechanisms
        if isinstance(mechanism, dict) and not mechanism.get("engineering_layers")
    ) if isinstance(mechanisms, list) else ["<mechanisms-not-list>"]
    check(checks, "mechanisms_map_engineering_layers", not missing_layer_maps, missing_layer_maps)
    if isinstance(cases, list):
        cases_without_mechanisms = sorted(
            case.get("case_id")
            for case in cases
            if isinstance(case, dict) and not case.get("linked_mechanisms")
        )
        unknown_case_mechanisms = sorted(
            {
                mechanism
                for case in cases
                if isinstance(case, dict)
                for mechanism in case.get("linked_mechanisms", [])
                if mechanism not in mechanism_ids
            }
        )
    else:
        cases_without_mechanisms = ["<cases-not-list>"]
        unknown_case_mechanisms = []
    check(checks, "behavior_cases_link_mechanisms", not cases_without_mechanisms, cases_without_mechanisms)
    check(checks, "behavior_case_mechanisms_known", not unknown_case_mechanisms, unknown_case_mechanisms)

    active_text = "\n".join(path.read_text(encoding="utf-8", errors="ignore") for path in active_text_files())
    for forbidden in FORBIDDEN_TEXT:
        check(checks, f"forbidden_text_absent:{forbidden}", forbidden not in active_text)

    reference_surface = "\n".join(
        (ROOT / path).read_text(encoding="utf-8", errors="ignore")
        for path in ["README.md", "AGENTS.md", "protocol/AGENTS.md", "docs/protocol_explainer_site/src/App.jsx"]
        if (ROOT / path).exists()
    )
    for reference in REQUIRED_REFERENCES:
        check(checks, f"active_reference:{reference}", reference in reference_surface)

    failures = [item for item in checks if not item["ok"]]
    output = {
        "failure_count": len(failures),
        "failures": failures,
        "checks": checks,
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))
    raise SystemExit(1 if failures else 0)


if __name__ == "__main__":
    try:
        main()
    except AssertionError as exc:
        print(json.dumps({"failure_count": 1, "failures": [str(exc)]}, ensure_ascii=False, indent=2))
        raise SystemExit(1)
