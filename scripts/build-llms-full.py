#!/usr/bin/env python3
"""
Build llms-full.txt at the repo root — the expanded companion to llms.txt.

Concatenates, in order:
  1. The current llms.txt (must exist; run after any llms.txt rewrite)
  2. A divider
  3. A compact one-line-per-guide inventory from index.json
     ("- <slug> | <jurisdiction> | tier <tier> | reviewed_by <reviewed_by or ->")
  4. A divider
  5. The full text of START-HERE.md and docs/QUALITY-TIERS.md

Stdlib only. index.json must be up to date first:
    python3 scripts/build-index.py && python3 scripts/build-llms-full.py
"""

import json
import os
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_PATH = os.path.join(REPO_ROOT, "llms-full.txt")
DIVIDER = "\n\n" + "=" * 72 + "\n\n"


def read_text(rel_path):
    path = os.path.join(REPO_ROOT, rel_path)
    if not os.path.isfile(path):
        sys.exit(f"error: required file missing: {rel_path}")
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def guide_inventory():
    index = json.loads(read_text("index.json"))
    lines = ["## Guide inventory "
             f"({index['counts']['guides']} guides, "
             f"{index['counts']['jurisdictions']} jurisdictions, "
             f"{index['counts']['accountant_reviewed']} accountant-reviewed)", ""]
    for guide in index["guides"]:
        jurisdiction = guide.get("jurisdiction") or "-"
        tier = guide.get("tier")
        tier = "-" if tier is None else tier
        reviewed_by = guide.get("reviewed_by") or "-"
        lines.append(
            f"- {guide['slug']} | {jurisdiction} | tier {tier} | reviewed_by {reviewed_by}"
        )
    return "\n".join(lines)


def main():
    parts = [
        read_text("llms.txt").rstrip("\n"),
        guide_inventory(),
        read_text("START-HERE.md").rstrip("\n"),
        read_text(os.path.join("docs", "QUALITY-TIERS.md")).rstrip("\n"),
    ]
    with open(OUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(DIVIDER.join(parts))
        fh.write("\n")
    print(f"llms-full.txt written ({os.path.getsize(OUT_PATH):,} bytes)")


if __name__ == "__main__":
    main()
