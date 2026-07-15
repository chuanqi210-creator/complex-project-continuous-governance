#!/usr/bin/env python3
"""Smoke-test the Complex integrity verifier against this repository."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    result = subprocess.run(
        [sys.executable, str(ROOT / "tools" / "verify_complex_integrity.py")],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        print(result.stdout)
        print(result.stderr, file=sys.stderr)
        raise SystemExit(result.returncode)

    data = json.loads(result.stdout)
    if data.get("failure_count") != 0:
        print(result.stdout)
        raise SystemExit(1)

    check_names = {item.get("name") for item in data.get("checks", [])}
    required_four_layer_checks = {
        "four_layer_flagship_complete",
        "four_layer_entrypoint:README.md",
        "four_layer_entrypoint:protocol/core.md",
        "four_layer_entrypoint:docs/quickstart.md",
        "four_layer_entrypoint:.agents/skills/complex-runtime/SKILL.md",
        "four_layer_mechanism_maturity_boundary",
        "four_layer_behavior_coverage",
        "current_state_semantic_recovery_contract",
    }
    missing = sorted(required_four_layer_checks - check_names)
    if missing:
        print(json.dumps({"missing_four_layer_checks": missing}, indent=2))
        raise SystemExit(1)

    print("ok")


if __name__ == "__main__":
    main()
