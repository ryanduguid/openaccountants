#!/usr/bin/env python3
"""
Build index.json — a machine-readable inventory of every Guide in the repo.

Walks skills/**/*.md (the source tree; packages/ is generated from it), skips
READMEs and files without frontmatter, and writes index.json at the repo root:

{
  "generated_at": "<UTC ISO>",
  "counts": { "guides": N, "jurisdictions": N, "accountant_reviewed": N },
  "guides": [ { "slug", "path", "name", "jurisdiction", "category", "tier",
                "verified_by", "reviewed_by", "tax_year", "last_updated" }, ... ]
}

Dependency-free (stdlib only). Guide discovery and the tolerant frontmatter
reader are the shared ones in scripts/oa_tools/ (guides.py, frontmatter.py);
malformed YAML is tolerated by regex-extracting the known keys, so a guide with
a broken block still lands in the inventory with whatever it does carry.

Usage:
    python3 scripts/build-index.py            # write index.json at repo root
    python3 scripts/build-index.py --out PATH # write elsewhere (used by CI)
"""

import json
import os
import re
import sys
from datetime import datetime, timezone

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:  # this file is loaded by path (importlib) as well as run
    sys.path.insert(0, _HERE)

from oa_tools import guides, paths, roster  # noqa: E402
# Both are used below and re-exported on purpose: the one-off metadata scripts
# (backfill-metadata.py, normalize-tax-year.py) load this module by path and
# reach the tolerant reader as `bi.extract_frontmatter` / `bi.parse_known_keys`.
from oa_tools.frontmatter import extract_frontmatter, parse_known_keys  # noqa: E402

REPO_ROOT = paths.REPO_ROOT

# Directories walked for guide files (scripts/oa_tools/paths.py).
GUIDE_TREES = list(paths.GUIDE_TREES)

# Jurisdiction values that look like codes get uppercased (MT, US, US-CA, CA-ON).
CODE_RE = re.compile(r"^[A-Za-z]{2,3}(-[A-Za-z0-9]{1,4})*$")


def guide_files():
    """Repo-relative paths of candidate guide files under REPO_ROOT, sorted.

    A wrapper rather than a re-export so that a test which points this
    module's REPO_ROOT at a temporary tree indexes that tree.
    """
    return guides.guide_files(REPO_ROOT, GUIDE_TREES)


def build_index():
    guides = []
    for rel_path in guide_files():
        with open(os.path.join(REPO_ROOT, rel_path), encoding="utf-8", errors="replace") as fh:
            text = fh.read()
        block = extract_frontmatter(text)
        if block is None:
            continue  # not a guide (no frontmatter)
        fields = parse_known_keys(block)

        jurisdiction = fields["jurisdiction"]
        if jurisdiction and CODE_RE.match(jurisdiction):
            jurisdiction = jurisdiction.upper()

        tier = fields["tier"]
        if isinstance(tier, str) and tier.isdigit():
            tier = int(tier)

        guides.append({
            "slug": fields["name"] or os.path.splitext(os.path.basename(rel_path))[0],
            "path": rel_path,
            "name": fields["name"],
            "jurisdiction": jurisdiction,
            "category": fields["category"],
            "tier": tier,
            "verified_by": fields["verified_by"],
            "reviewed_by": fields["reviewed_by"],
            "tax_year": fields["tax_year"],
            "last_updated": fields["last_updated"],
        })

    guides.sort(key=lambda g: g["path"])

    jurisdictions = {g["jurisdiction"] for g in guides if g["jurisdiction"]}

    # The one counting rule (scripts/oa_tools/roster.py), which the MCP
    # server's `_quality_tier` mirrors: only an explicit `tier: 1` plus a
    # named reviewer counts. A reviewer name alone never implies sign-off, or
    # this inventory reports guides as accountant-reviewed that the MCP server
    # serves as research-verified. PARTNERS.md and the headline gate use it too.
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "counts": {
            "guides": len(guides),
            "jurisdictions": len(jurisdictions),
            "accountant_reviewed": sum(1 for g in guides if roster.reviewer_of(g)),
        },
        "guides": guides,
    }


def main():
    out_path = os.path.join(REPO_ROOT, "index.json")
    if "--out" in sys.argv:
        flag = sys.argv.index("--out")
        if flag + 1 >= len(sys.argv) or sys.argv[flag + 1].startswith("--"):
            sys.exit("error: --out requires a file path")
        out_path = sys.argv[flag + 1]
    index = build_index()
    if not index["guides"]:
        # A wrong root or a broken checkout must not overwrite the inventory
        # with an empty one that every consumer would read as "no guides".
        sys.exit(
            f"error: no guides found under {REPO_ROOT} "
            f"(looked in {', '.join(GUIDE_TREES)}); not writing {out_path}"
        )
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(index, fh, indent=1, ensure_ascii=False)
        fh.write("\n")
    counts = index["counts"]
    print(f"index written to {out_path}")
    print(f"  guides: {counts['guides']}")
    print(f"  jurisdictions: {counts['jurisdictions']}")
    print(f"  accountant_reviewed: {counts['accountant_reviewed']}")


if __name__ == "__main__":
    main()
