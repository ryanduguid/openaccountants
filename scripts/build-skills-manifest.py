#!/usr/bin/env python3
"""
DEPRECATED — skills/manifest.json is gone.

This script used to build skills/manifest.json. That file was superseded by
the canonical, CI-enforced inventory at the repo root:

    index.json  — built by scripts/build-index.py, freshness enforced by
                  scripts/validate-guides.py (and .github/workflows/validate.yml)

Nothing reads skills/manifest.json (the MCP server indexes packages/**/*.md
frontmatter directly, and the website sync works from files + frontmatter),
so the file was removed rather than left to drift.

Need the inventory? Use index.json, or regenerate it:

    python3 scripts/build-index.py
"""

import sys


def main() -> int:
    print(
        "DEPRECATED: skills/manifest.json is no longer generated or checked in.\n"
        "The canonical machine-readable inventory is index.json at the repo root.\n"
        "Regenerate it with: python3 scripts/build-index.py",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
