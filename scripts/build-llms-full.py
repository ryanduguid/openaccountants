#!/usr/bin/env python3
"""
Build llms-full.txt at the repo root — the expanded companion to llms.txt.

Concatenates, in order:
  1. The current llms.txt (must exist; run after any llms.txt rewrite)
  2. A divider
  3. A compact one-line-per-guide inventory from index.json
     ("- <slug> | <jurisdiction> | tier <tier> | reviewed_by <reviewed_by or ->")
  4. A divider
  5. The full text of START-HERE.md, docs/QUALITY-TIERS.md and PARTNERS.md
     (the roster of accountants on record, itself generated from index.json)

Stdlib only. index.json and PARTNERS.md must be up to date first:
    python3 scripts/build-index.py && python3 scripts/build-partners.py && python3 scripts/build-llms-full.py
"""

import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from oa_tools.cli import generator_arguments  # noqa: E402

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


def build_text():
    parts = [
        read_text("llms.txt").rstrip("\n"),
        guide_inventory(),
        read_text("START-HERE.md").rstrip("\n"),
        read_text(os.path.join("docs", "QUALITY-TIERS.md")).rstrip("\n"),
        read_text("PARTNERS.md").rstrip("\n"),
    ]
    return DIVIDER.join(parts) + "\n"


def main():
    args = generator_arguments((__doc__ or "").split('\n\n')[0], output=OUT_PATH)
    if args.help:
        return
    out_path = args.out
    text = build_text()
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    print(f"{os.path.basename(out_path)} written ({os.path.getsize(out_path):,} bytes)")


if __name__ == "__main__":
    main()
