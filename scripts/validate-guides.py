#!/usr/bin/env python3
"""
Validate guide files, the hand-authored us-federal set, and index.json.

Checks (ERROR = exit 1, WARN = printed summary only):
  1. Every guide file's frontmatter block parses (a file that opens `---`
     must close it). Files without any frontmatter are treated as docs, not
     guides, and skipped (same rule scripts/build-index.py uses).
  2. `name` and `description` are present — ERROR if missing, except for the
     frozen LEGACY_MISSING_DESCRIPTION baseline below (grandfathered; the
     list must only ever shrink).
  3. `tier` and `last_updated` are required — ERROR if missing (the one-time
     sweep was scripts/backfill-metadata.py). `tier` must be 1 or 2;
     `last_updated` must be YYYY-MM-DD — ERROR otherwise.
  3a. `jurisdiction` is required — ERROR if missing, except inside the
     JURISDICTION_OPTIONAL_DIRS below (dirs whose deliberate convention is
     "no jurisdiction key": jurisdiction-agnostic templates/engines and the
     EU-wide shared base). There it stays a WARN summary count.
  3b. `tax_year`, when present, must be a bare integer 2015-2035 — ERROR
     otherwise (no grandfathering; scripts/normalize-tax-year.py did the
     one-time sweep, and calendar/range/qualifier text belongs in
     `tax_year_notes`).
  4. ERROR if any file under packages/us-federal/ was deleted relative to
     git history (hand-authored, no builder — a deletion is unrecoverable).
     Skipped when git / origin/main is unavailable.
  5. ERROR if index.json is stale: regenerated index (ignoring generated_at)
     must match the committed one. Fix with: python3 scripts/build-index.py

Stdlib only. Run: python3 scripts/validate-guides.py
"""

import importlib.util
import json
import os
import re
import subprocess
import sys
import tempfile

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD_INDEX = os.path.join(REPO_ROOT, "scripts", "build-index.py")

# Legacy guides that predate the description requirement. Grandfathered so CI
# can be strict for everything new. Never add to this list — remove entries as
# the files gain descriptions.
LEGACY_MISSING_DESCRIPTION = {
    "skills/cross-border/treaty-corridors/americas-corridors.md",
    "skills/cross-border/treaty-corridors/asia-pacific-corridors.md",
    "skills/cross-border/treaty-corridors/emerging-market-corridors.md",
    "skills/cross-border/treaty-corridors/eu-intra-rates.md",
    "skills/cross-border/treaty-corridors/uk-major-partners.md",
    "skills/cross-border/treaty-corridors/us-major-partners.md",
}

# Dirs whose deliberate convention is "no jurisdiction key" — the content is
# jurisdiction-agnostic (templates, intelligence engines, treaty corridor
# reference tables) or spans the whole EU (the shared eu-vat-base). Missing
# `jurisdiction` here is a WARN, not an ERROR. Everywhere else it is required
# (scripts/backfill-metadata.py did the one-time sweep).
JURISDICTION_OPTIONAL_DIRS = {
    "skills/cross-border/treaty-corridors",
    "skills/intelligence",
    "skills/templates",
    "skills/international/eu",
}


def load_build_index():
    spec = importlib.util.spec_from_file_location("build_index", BUILD_INDEX)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# `tax_year` must be a bare integer year, e.g. `tax_year: 2025`. Ranges,
# calendars, and qualifiers go in `tax_year_notes` (see
# scripts/normalize-tax-year.py, issue #49).
TAX_YEAR_RE = re.compile(r"^tax_year:[ \t]*(.*?)[ \t]*$", re.MULTILINE)
TAX_YEAR_MIN, TAX_YEAR_MAX = 2015, 2035


LAST_UPDATED_FMT = re.compile(r"\d{4}-\d{2}-\d{2}")


def check_guides(bi, errors, warnings):
    warn_counts = {"jurisdiction (jurisdiction-agnostic dirs)": 0}
    guides = skipped = 0
    for rel in bi.guide_files():
        with open(os.path.join(REPO_ROOT, rel), encoding="utf-8", errors="replace") as fh:
            text = fh.read()
        block = bi.extract_frontmatter(text)
        if block is None:
            if text.startswith("---"):
                errors.append(f"{rel}: frontmatter opens with --- but never closes")
            else:
                skipped += 1  # doc file, not a guide
            continue
        guides += 1
        fields = bi.parse_known_keys(block)
        if not fields["name"]:
            errors.append(f"{rel}: missing required frontmatter key `name`")
        has_description = re.search(r"^description:", block, re.MULTILINE)
        if not has_description and rel not in LEGACY_MISSING_DESCRIPTION:
            errors.append(f"{rel}: missing required frontmatter key `description`")
        tax_year = TAX_YEAR_RE.search(block)
        if tax_year:
            value = tax_year.group(1)
            if not re.fullmatch(r"\d{4}", value) or not (TAX_YEAR_MIN <= int(value) <= TAX_YEAR_MAX):
                errors.append(
                    f"{rel}: `tax_year` must be a bare integer "
                    f"{TAX_YEAR_MIN}-{TAX_YEAR_MAX} (got {value!r}) — put "
                    "ranges/calendars/qualifiers in `tax_year_notes`"
                )
        tier = fields["tier"]
        if not tier:
            errors.append(f"{rel}: missing required frontmatter key `tier`")
        elif tier not in ("1", "2"):
            errors.append(f"{rel}: `tier` must be 1 or 2 (got {tier!r})")
        last_updated = fields["last_updated"]
        if not last_updated:
            errors.append(f"{rel}: missing required frontmatter key `last_updated`")
        elif not LAST_UPDATED_FMT.fullmatch(last_updated):
            errors.append(
                f"{rel}: `last_updated` must be YYYY-MM-DD (got {last_updated!r})"
            )
        if not fields["jurisdiction"]:
            if os.path.dirname(rel) in JURISDICTION_OPTIONAL_DIRS:
                warn_counts["jurisdiction (jurisdiction-agnostic dirs)"] += 1
            else:
                errors.append(f"{rel}: missing required frontmatter key `jurisdiction`")
    for key, count in sorted(warn_counts.items()):
        if count:
            warnings.append(f"{count} guides missing `{key}`")
    print(f"checked {guides} guides ({skipped} non-guide .md files skipped)")


def check_us_federal_deletions(errors):
    """The hand-authored us-federal package has no builder; a deleted file is gone."""
    for label, args in (
        ("origin/main...HEAD", ["git", "diff", "--name-status", "origin/main...HEAD", "--", "packages/us-federal"]),
        ("working tree vs HEAD", ["git", "diff", "--name-status", "HEAD", "--", "packages/us-federal"]),
    ):
        try:
            out = subprocess.run(args, cwd=REPO_ROOT, capture_output=True, text=True, timeout=60)
        except (OSError, subprocess.TimeoutExpired):
            print(f"skipping us-federal deletion check ({label}): git unavailable")
            continue
        if out.returncode != 0:
            print(f"skipping us-federal deletion check ({label}): {out.stderr.strip().splitlines()[:1]}")
            continue
        for line in out.stdout.splitlines():
            status, _, path = line.partition("\t")
            if status.startswith("D"):
                errors.append(f"hand-authored file deleted ({label}): {path}")


def check_index_fresh(errors):
    index_path = os.path.join(REPO_ROOT, "index.json")
    if not os.path.isfile(index_path):
        errors.append("index.json missing — run: python3 scripts/build-index.py")
        return
    with tempfile.TemporaryDirectory() as tmp:
        fresh_path = os.path.join(tmp, "index.json")
        result = subprocess.run(
            [sys.executable, BUILD_INDEX, "--out", fresh_path],
            cwd=REPO_ROOT, capture_output=True, text=True,
        )
        if result.returncode != 0:
            errors.append(f"build-index.py failed while checking freshness: {result.stderr.strip()}")
            return
        with open(fresh_path, encoding="utf-8") as fh:
            fresh = json.load(fh)
    with open(index_path, encoding="utf-8") as fh:
        committed = json.load(fh)
    for section in ("counts", "guides"):
        if committed.get(section) != fresh.get(section):
            errors.append(
                f"index.json is stale (`{section}` differs) — regenerate with: "
                "python3 scripts/build-index.py"
            )
            return


def main():
    errors, warnings = [], []
    bi = load_build_index()
    check_guides(bi, errors, warnings)
    check_us_federal_deletions(errors)
    check_index_fresh(errors)

    for warning in warnings:
        print(f"WARN: {warning}")
    for error in errors:
        print(f"ERROR: {error}")
    if errors:
        print(f"\nvalidation FAILED: {len(errors)} error(s), {len(warnings)} warning group(s)")
        sys.exit(1)
    print(f"\nvalidation passed ({len(warnings)} warning group(s))")


if __name__ == "__main__":
    main()
