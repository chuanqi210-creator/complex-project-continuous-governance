#!/usr/bin/env python3
"""Behavior test for the bounded recovery-anchor fact-ledger extractor."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOOL = ROOT / "tools" / "inspect_recovery_anchor.py"


def main() -> None:
    with tempfile.TemporaryDirectory() as raw_tmp:
        target = Path(raw_tmp)
        (target / "notes").mkdir()
        (target / "deliverables").mkdir()
        (target / "AGENTS.md").write_text(
            "# Instructions\nAPI_KEY=supersecret\nowner=author@example.com\n",
            encoding="utf-8",
        )
        (target / "CONTEXT.md").write_text(
            "# Context\nsource=/Users/Alice/private-project\nnext_route: reconcile_state\n",
            encoding="utf-8",
        )
        status_lines = ["status password=hunter2 route candidate 0\n"]
        status_lines.extend(f"status route candidate {index}\n" for index in range(1, 120))
        (target / "notes" / "current_status.md").write_text("".join(status_lines), encoding="utf-8")
        manifest = {f"status_route_{index}": {"large": "x" * 100} for index in range(1600)}
        (target / "deliverables" / "manifest.json").write_text(
            json.dumps(manifest), encoding="utf-8"
        )

        result = subprocess.run(
            [sys.executable, str(TOOL), str(target)],
            text=True,
            capture_output=True,
            check=False,
        )
        tight_result = subprocess.run(
            [
                sys.executable,
                str(TOOL),
                str(target),
                "--max-output-bytes",
                "4096",
            ],
            text=True,
            capture_output=True,
            check=False,
        )
        tiny_result = subprocess.run(
            [
                sys.executable,
                str(TOOL),
                str(target),
                "--max-output-bytes",
                "512",
            ],
            text=True,
            capture_output=True,
            check=False,
        )

    if result.returncode != 0:
        print(result.stdout)
        print(result.stderr, file=sys.stderr)
        raise SystemExit(result.returncode)

    payload = json.loads(result.stdout)
    status = payload["sources"]["status"]
    manifest_summary = payload["sources"]["manifest"]

    assert status["match_overflow"] is True
    assert len(status["matches"]) == payload["envelope"]["max_matched_lines"]
    assert manifest_summary["matching_key_overflow"] is True
    assert len(manifest_summary["matching_keys"]) == payload["envelope"]["max_json_keys"]
    assert all(
        set(item) == {"matched_terms", "value_type"}
        for item in manifest_summary["matching_keys"]
    )
    assert payload["output_bytes"] <= payload["envelope"]["max_output_bytes"]
    assert "match_overflow" in payload["stop_signals"]
    assert "manifest_key_overflow" in payload["stop_signals"]
    assert "supersecret" not in result.stdout
    assert "author@example.com" not in result.stdout
    assert "/Users/Alice" not in result.stdout
    assert "hunter2" not in result.stdout
    assert payload["sources"]["instructions"]["raw_content_exposed"] is False
    assert payload["sources"]["manifest"]["raw_key_names_exposed"] is False
    assert "target_id" not in payload
    assert "content_fingerprint" not in result.stdout

    if tight_result.returncode != 0:
        print(tight_result.stdout)
        print(tight_result.stderr, file=sys.stderr)
        raise SystemExit(tight_result.returncode)
    tight_payload = json.loads(tight_result.stdout)
    assert tight_payload["output_truncated"] is True
    assert tight_payload["output_bytes"] <= 4096

    if tiny_result.returncode != 0:
        print(tiny_result.stdout)
        print(tiny_result.stderr, file=sys.stderr)
        raise SystemExit(tiny_result.returncode)
    tiny_payload = json.loads(tiny_result.stdout)
    assert tiny_payload["output_bytes"] <= 512
    assert tiny_payload["error"] == "output_budget_too_small_for_full_fact_ledger"

    print("ok")


if __name__ == "__main__":
    main()
