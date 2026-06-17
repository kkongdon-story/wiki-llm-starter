#!/usr/bin/env python3
"""Lightweight structural lint for the LLM Wiki starter template."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


REQUIRED_DIRS = [
    "raw",
    "wiki",
    "wiki/sources",
    "wiki/concepts",
    "wiki/entities",
    "wiki/workflows",
    "wiki/questions",
    "schema",
    "ontology",
]

REQUIRED_FILES = [
    "CLAUDE.md",
    "log.md",
    "wiki/index.md",
    "schema/wiki-rules.md",
    "schema/page-template.md",
    "ontology/tbox.json",
    "ontology/abox.json",
    "ontology/inference-rules.json",
]


def wiki_links(text: str) -> list[str]:
    return re.findall(r"\[\[([^\]]+)\]\]", text)


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a starter LLM Wiki folder.")
    parser.add_argument("--root", default=".", help="Wiki root to lint")
    args = parser.parse_args()

    root = Path(args.root)
    errors: list[str] = []
    warnings: list[str] = []

    for rel in REQUIRED_DIRS:
        if not (root / rel).is_dir():
            errors.append(f"missing directory: {rel}")

    for rel in REQUIRED_FILES:
        if not (root / rel).is_file():
            errors.append(f"missing file: {rel}")

    wiki_files = [path for path in (root / "wiki").rglob("*.md") if path.is_file()] if (root / "wiki").exists() else []
    if not wiki_files:
        warnings.append("wiki has no Markdown pages yet")

    link_count = 0
    sourced_pages = 0
    for path in wiki_files:
        text = path.read_text(encoding="utf-8")
        link_count += len(wiki_links(text))
        if "source:" in text or "[[sources/" in text or "출처" in text:
            sourced_pages += 1

    if wiki_files and link_count == 0:
        warnings.append("wiki pages contain no [[wikilinks]] yet")
    if wiki_files and sourced_pages == 0:
        warnings.append("wiki pages do not appear to cite sources yet")

    print("LLM Wiki lint report")
    print(f"- root: {root}")
    print(f"- wiki pages: {len(wiki_files)}")
    print(f"- wikilinks: {link_count}")
    print(f"- pages with source signals: {sourced_pages}")

    if warnings:
        print("\nWarnings")
        for warning in warnings:
            print(f"- {warning}")

    if errors:
        print("\nErrors")
        for error in errors:
            print(f"- {error}")
        return 1

    print("\nOK: folder contract is present.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
