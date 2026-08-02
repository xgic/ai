#!/usr/bin/env python3
"""Public-safe draft scanner for XGIC public GitHub artifacts.

Scans files or stdin for **generic** high-risk patterns that often indicate
private leakage (internal-looking hosts, private IPv4 literals, credential
shapes). Does **not** embed any organization-private hostnames or project
paths (those must never live in public trees).

Usage:
  python scripts/public-safe-scan.py path/to/draft.md
  python scripts/public-safe-scan.py --stdin < draft.md

Exit codes:
  0 — no findings
  1 — one or more findings (or usage error)
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# Generic patterns only — no private org hostnames or project paths.
PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    (
        "private_ipv4",
        re.compile(
            r"\b(?:10\.\d{1,3}\.\d{1,3}\.\d{1,3}"
            r"|192\.168\.\d{1,3}\.\d{1,3}"
            r"|172\.(?:1[6-9]|2\d|3[0-1])\.\d{1,3}\.\d{1,3})\b"
        ),
    ),
    (
        "internal_tld_host",
        re.compile(
            r"\b[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?"
            r"(?:\.[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?)*"
            r"\.(?:internal|local|lan|corp|intranet)\b",
            re.IGNORECASE,
        ),
    ),
    (
        "windows_drive_path",
        re.compile(r"\b[A-Za-z]:\\(?:Users|Dev|Data|Apps|Backup)\\[^\s`\"']+", re.IGNORECASE),
    ),
    (
        "unix_home_path",
        re.compile(r"/(?:home|Users)/[A-Za-z0-9._-]+/(?:Dev|source|projects)/[^\s`\"']+"),
    ),
    (
        "bearer_or_pat_shape",
        re.compile(r"\b(?:glpat-|ghp_|gho_|github_pat_)[A-Za-z0-9_]{8,}\b"),
    ),
    (
        "markdown_private_tracker_style",
        # Self-hosted GitLab-style work item URLs without naming any real host:
        # matches .../-/work_items/N or .../-/issues/N on non-github.com hosts.
        re.compile(
            r"https?://(?!github\.com)[a-z0-9.-]+/"
            r"[^\s)]+/-/(?:work_items|issues|merge_requests)/\d+",
            re.IGNORECASE,
        ),
    ),
]


def scan_text(text: str, source: str) -> list[str]:
    findings: list[str] = []
    for name, pattern in PATTERNS:
        for match in pattern.finditer(text):
            line = text.count("\n", 0, match.start()) + 1
            snippet = match.group(0)
            if len(snippet) > 80:
                snippet = snippet[:77] + "..."
            findings.append(f"{source}:{line}: [{name}] {snippet}")
    return findings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "paths",
        nargs="*",
        type=Path,
        help="Draft files to scan (Markdown, text, etc.)",
    )
    parser.add_argument(
        "--stdin",
        action="store_true",
        help="Read draft text from stdin",
    )
    args = parser.parse_args(argv)

    if not args.paths and not args.stdin:
        parser.error("provide one or more paths, or --stdin")

    all_findings: list[str] = []

    if args.stdin:
        all_findings.extend(scan_text(sys.stdin.read(), "<stdin>"))

    for path in args.paths:
        if not path.is_file():
            print(f"error: not a file: {path}", file=sys.stderr)
            return 1
        all_findings.extend(scan_text(path.read_text(encoding="utf-8", errors="replace"), str(path)))

    if all_findings:
        print("public-safe-scan: FINDINGS (review before public gh/GitHub write)")
        for item in all_findings:
            print(f"  {item}")
        print(
            "\nIf intentional public content, rewrite with fictional placeholders "
            "(gitlab.example.com, group/project). See BASE-STANDARDS hard security."
        )
        return 1

    print("public-safe-scan: OK (no generic high-risk patterns matched)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
