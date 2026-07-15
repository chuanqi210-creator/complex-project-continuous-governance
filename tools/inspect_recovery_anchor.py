#!/usr/bin/env python3
"""Emit a bounded fact ledger for target-project recovery-anchor review.

This tool performs deterministic extraction only. It does not decide which
route is authoritative and never writes to the target repository.
"""

from __future__ import annotations

import argparse
import json
import re
import time
from pathlib import Path
from typing import Any


DEFAULT_PATTERN = r"authority|authoritative|current|phase|status|route|next|stage|handoff|recovery"
TERM_PATTERN = re.compile(DEFAULT_PATTERN, re.IGNORECASE)


def json_type(value: Any) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "boolean"
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return "number"
    if isinstance(value, str):
        return "string"
    if isinstance(value, list):
        return "array"
    if isinstance(value, dict):
        return "object"
    return type(value).__name__


def target_path(target: Path, relative: str) -> Path:
    candidate = (target / relative).resolve()
    try:
        candidate.relative_to(target)
    except ValueError as exc:
        raise ValueError(f"path escapes target repository: {relative}") from exc
    return candidate


def content_shape(text: str) -> dict[str, Any]:
    clean = text.rstrip("\r\n")
    stripped = clean.lstrip()
    if not stripped:
        kind = "blank"
    elif stripped.startswith("#"):
        kind = "heading"
    elif stripped.startswith(("- ", "* ", "+ ")):
        kind = "list_item"
    else:
        kind = "text"
    return {
        "kind": kind,
        "char_count": len(clean),
        "matched_terms": sorted({match.group(0).lower() for match in TERM_PATTERN.finditer(clean)}),
    }


def summarize_text(
    path: Path,
    *,
    display_path: str,
    preview_limit: int,
    match_limit: int,
    max_scan_bytes: int,
    deadline: float,
    pattern: re.Pattern[str] | None = None,
) -> dict[str, Any]:
    summary: dict[str, Any] = {
        "path": display_path,
        "exists": path.is_file(),
    }
    if not path.is_file():
        return summary

    summary["size_bytes"] = path.stat().st_size
    preview: list[dict[str, Any]] = []
    matches: list[dict[str, Any]] = []
    line_count = 0
    match_count = 0
    bytes_scanned = 0
    scan_budget_exceeded = False
    time_budget_exceeded = False

    with path.open("r", encoding="utf-8", errors="replace") as handle:
        for line_number, line in enumerate(handle, start=1):
            if time.monotonic() >= deadline:
                time_budget_exceeded = True
                break
            encoded_size = len(line.encode("utf-8", errors="replace"))
            if bytes_scanned + encoded_size > max_scan_bytes:
                scan_budget_exceeded = True
                break
            bytes_scanned += encoded_size
            line_count = line_number
            if len(preview) < preview_limit:
                preview.append({"line": line_number, **content_shape(line)})
            if pattern is not None and pattern.search(line):
                match_count += 1
                if len(matches) < match_limit:
                    matches.append({"line": line_number, **content_shape(line)})
                else:
                    break

    summary.update(
        {
            "line_count_scanned": line_count,
            "bytes_scanned": bytes_scanned,
            "scan_budget_exceeded": scan_budget_exceeded,
            "time_budget_exceeded": time_budget_exceeded,
            "raw_content_exposed": False,
        }
    )
    if pattern is None:
        summary["preview"] = preview
    else:
        summary.update(
            {
                "matches": matches,
                "match_count": match_count,
                "match_overflow": match_count > match_limit,
            }
        )
    return summary


def summarize_manifest(
    path: Path,
    *,
    display_path: str,
    pattern: re.Pattern[str],
    key_limit: int,
    max_json_bytes: int,
    deadline: float,
) -> dict[str, Any]:
    summary: dict[str, Any] = {
        "path": display_path,
        "exists": path.is_file(),
    }
    if not path.is_file():
        return summary

    size = path.stat().st_size
    summary["size_bytes"] = size
    if time.monotonic() >= deadline:
        summary.update(
            {
                "parse_skipped": True,
                "parse_skip_reason": "time_budget_exceeded",
                "matching_keys": [],
                "matching_key_overflow": False,
            }
        )
        return summary
    if size > max_json_bytes:
        summary.update(
            {
                "parse_skipped": True,
                "parse_skip_reason": "json_byte_budget_exceeded",
                "matching_keys": [],
                "matching_key_overflow": True,
            }
        )
        return summary

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        summary.update({"parse_error": type(exc).__name__, "matching_keys": []})
        return summary

    if time.monotonic() >= deadline:
        summary.update(
            {
                "parse_skipped": True,
                "parse_skip_reason": "time_budget_exceeded_after_parse",
                "matching_keys": [],
                "matching_key_overflow": False,
            }
        )
        return summary

    if not isinstance(data, dict):
        summary.update(
            {
                "top_level_type": json_type(data),
                "matching_keys": [],
                "matching_key_overflow": False,
            }
        )
        return summary

    matching_names = [name for name in data if pattern.search(str(name))]
    matching_keys = []
    for name in matching_names[:key_limit]:
        name_text = str(name)
        matching_keys.append(
            {
                "matched_terms": sorted(
                    {match.group(0).lower() for match in TERM_PATTERN.finditer(name_text)}
                ),
                "value_type": json_type(data[name]),
            }
        )
    summary.update(
        {
            "top_level_type": "object",
            "top_level_key_count": len(data),
            "matching_key_count": len(matching_names),
            "matching_key_overflow": len(matching_names) > key_limit,
            "matching_keys": matching_keys,
            "values_opened": [],
            "raw_key_names_exposed": False,
        }
    )
    return summary


def encoded_size(payload: dict[str, Any]) -> int:
    return len(json.dumps(payload, ensure_ascii=False, indent=2).encode("utf-8"))


def enforce_output_budget(payload: dict[str, Any], max_output_bytes: int) -> dict[str, Any]:
    removable = [
        payload["sources"].get("status", {}).get("matches"),
        payload["sources"].get("manifest", {}).get("matching_keys"),
        payload["sources"].get("context", {}).get("preview"),
        payload["sources"].get("instructions", {}).get("preview"),
    ]
    payload["output_truncated"] = False
    payload["output_bytes"] = 0
    while True:
        for _ in range(3):
            payload["output_bytes"] = encoded_size(payload)
        if payload["output_bytes"] <= max_output_bytes:
            return payload

        changed = False
        for items in removable:
            if isinstance(items, list) and items:
                items.pop()
                changed = True
                payload["output_truncated"] = True
                break
        if not changed:
            minimal = {
                "purpose": "bounded recovery-anchor fact ledger",
                "error": "output_budget_too_small_for_full_fact_ledger",
                "stop_signals": ["output_budget_exceeded"],
                "output_truncated": True,
                "max_output_bytes": max_output_bytes,
                "output_bytes": 0,
            }
            for _ in range(3):
                minimal["output_bytes"] = encoded_size(minimal)
            if minimal["output_bytes"] > max_output_bytes:
                raise ValueError("max_output_bytes is too small for the minimal error ledger")
            return minimal


def build_summary(args: argparse.Namespace) -> dict[str, Any]:
    started = time.monotonic()
    numeric_limits = {
        "max_preview_lines": args.max_preview_lines,
        "max_matched_lines": args.max_matched_lines,
        "max_json_keys": args.max_json_keys,
        "max_text_scan_bytes": args.max_text_scan_bytes,
        "max_json_bytes": args.max_json_bytes,
        "max_output_bytes": args.max_output_bytes,
        "max_seconds": args.max_seconds,
    }
    invalid = [name for name, value in numeric_limits.items() if value <= 0]
    if invalid:
        raise ValueError(f"inspection limits must be positive: {', '.join(invalid)}")

    target = Path(args.target).expanduser().resolve()
    if not target.is_dir():
        raise ValueError(f"target repository is not a directory: {target}")

    deadline = started + args.max_seconds
    pattern = re.compile(DEFAULT_PATTERN, re.IGNORECASE)
    sources = {
        "instructions": summarize_text(
            target_path(target, args.instructions),
            display_path=args.instructions,
            preview_limit=args.max_preview_lines,
            match_limit=0,
            max_scan_bytes=args.max_text_scan_bytes,
            deadline=deadline,
        ),
        "context": summarize_text(
            target_path(target, args.context),
            display_path=args.context,
            preview_limit=args.max_preview_lines,
            match_limit=0,
            max_scan_bytes=args.max_text_scan_bytes,
            deadline=deadline,
        ),
        "status": summarize_text(
            target_path(target, args.status),
            display_path=args.status,
            preview_limit=0,
            match_limit=args.max_matched_lines,
            max_scan_bytes=args.max_text_scan_bytes,
            deadline=deadline,
            pattern=pattern,
        ),
        "manifest": summarize_manifest(
            target_path(target, args.manifest),
            display_path=args.manifest,
            pattern=pattern,
            key_limit=args.max_json_keys,
            max_json_bytes=args.max_json_bytes,
            deadline=deadline,
        ),
    }

    stop_signals: list[str] = []
    status = sources["status"]
    manifest = sources["manifest"]
    if status.get("match_overflow"):
        stop_signals.append("match_overflow")
    if status.get("scan_budget_exceeded"):
        stop_signals.append("text_scan_budget_exceeded")
    if status.get("time_budget_exceeded"):
        stop_signals.append("time_budget_exceeded")
    if manifest.get("matching_key_overflow"):
        stop_signals.append("manifest_key_overflow")
    if manifest.get("parse_skip_reason"):
        stop_signals.append(str(manifest["parse_skip_reason"]))

    payload: dict[str, Any] = {
        "purpose": "bounded recovery-anchor fact ledger; no authority decision is made",
        "envelope": numeric_limits,
        "sources": sources,
        "stop_signals": stop_signals,
        "elapsed_seconds": round(time.monotonic() - started, 4),
    }
    return enforce_output_budget(payload, args.max_output_bytes)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target")
    parser.add_argument("--instructions", default="AGENTS.md")
    parser.add_argument("--context", default="CONTEXT.md")
    parser.add_argument("--status", default="notes/current_status.md")
    parser.add_argument("--manifest", default="deliverables/manifest.json")
    parser.add_argument("--max-preview-lines", type=int, default=20)
    parser.add_argument("--max-matched-lines", type=int, default=40)
    parser.add_argument("--max-json-keys", type=int, default=20)
    parser.add_argument("--max-text-scan-bytes", type=int, default=2_000_000)
    parser.add_argument("--max-json-bytes", type=int, default=2_000_000)
    parser.add_argument("--max-output-bytes", type=int, default=32_768)
    parser.add_argument("--max-seconds", type=float, default=30.0)
    return parser.parse_args()


def main() -> None:
    try:
        payload = build_summary(parse_args())
    except (OSError, ValueError, re.error) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False, indent=2))
        raise SystemExit(2)
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
