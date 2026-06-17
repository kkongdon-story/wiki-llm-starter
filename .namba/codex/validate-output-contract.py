#!/usr/bin/env python3
"""Validate the NambaAI output contract from stdin or a file."""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

SPEC = {
  "header": "NAMBA-AI Work Report",
  "header_aliases": [
    "NAMBA-AI Work Report",
    "NAMBA-AI Engineering Report",
    "NAMBA-AI Task Report"
  ],
  "sections": [
    {
      "emoji": "🧭",
      "primary": "Scope",
      "aliases": [
        "Scope",
        "Framing",
        "Problem Framing",
        "Definition"
      ]
    },
    {
      "emoji": "🧠",
      "primary": "Decision",
      "aliases": [
        "Decision",
        "Judgment",
        "Judgement",
        "Assessment"
      ]
    },
    {
      "emoji": "🛠",
      "primary": "Work Completed",
      "aliases": [
        "Work Completed",
        "Work Done",
        "Actions Taken",
        "Completed Work"
      ]
    },
    {
      "emoji": "🚧",
      "primary": "Current Issues",
      "aliases": [
        "Current Issues",
        "Open Issues",
        "Current Gaps",
        "Current Problems"
      ]
    },
    {
      "emoji": "⚠",
      "primary": "Potential Risks",
      "aliases": [
        "Potential Risks",
        "Risks",
        "Potential Problems",
        "Risk Boundaries"
      ]
    },
    {
      "emoji": "➡",
      "primary": "Next Steps",
      "aliases": [
        "Next Steps",
        "Recommended Next Steps",
        "Recommendations",
        "Next Move"
      ]
    }
  ]
}


def build_pattern(aliases: list[str]) -> re.Pattern[str]:
    escaped = "|".join(re.escape(alias) for alias in aliases)
    return re.compile(r"^\s*(?:#{1,6}\s*|[-*]\s+)?(?:\*\*)?[\W_]*(?P<label>(" + escaped + r"))(?:\*\*)?\s*(?:[:：-].*)?$")


def read_text(args: argparse.Namespace) -> str:
    if args.file:
        return pathlib.Path(args.file).read_text(encoding="utf-8")
    return sys.stdin.read().lstrip('\ufeff')


def find_first_match(lines: list[str], aliases: list[str], start: int = 0) -> int:
    pattern = build_pattern(aliases)
    for index, line in enumerate(lines[start:], start=start):
        if pattern.match(line.strip()):
            return index
    return -1


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the NambaAI output contract.")
    parser.add_argument("--file", help="Path to a saved response file.")
    args = parser.parse_args()

    text = read_text(args)
    if not text.strip():
        print("output-contract: empty input", file=sys.stderr)
        return 1

    lines = [line.lstrip('\ufeff') for line in text.lstrip('\ufeff').splitlines()]
    header_index = find_first_match(lines, SPEC['header_aliases'])
    if header_index < 0:
        print(f"output-contract: missing header '{SPEC['header']}'", file=sys.stderr)
        return 1

    previous = header_index
    for section in SPEC['sections']:
        found = find_first_match(lines, section['aliases'], start=previous + 1)
        if found < 0:
            print(f"output-contract: missing section '{section['primary']}'", file=sys.stderr)
            return 1
        if found <= previous:
            print(f"output-contract: section '{section['primary']}' is out of order", file=sys.stderr)
            return 1
        previous = found

    print("output-contract: ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
