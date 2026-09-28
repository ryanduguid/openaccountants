#!/usr/bin/env python3
"""
Validate guide files, the hand-authored us-federal set, and index.json.

Checks (ERROR = exit 1, WARN = printed summary only):
  1. Every guide file's frontmatter block is valid, unambiguous YAML (a file
     that opens `---` must close it). Files without any frontmatter are treated
     as docs, not guides, and skipped (same rule scripts/build-index.py uses).
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
  6. ERROR if a deprecated inventory file reappears (skills/manifest.json,
     packages/manifest.json). index.json is the single canonical inventory;
     the old manifests had no consumers and were removed so they can't drift.
  7. ERROR if llms-full.txt is stale: regenerated copy must match the
     committed one. Fix with: python3 scripts/build-llms-full.py
  8. ERROR if packages/** is stale: a fresh build into a temp dir (via
     build-packages.py --out) must match the committed tree file for file,
     the hand-authored packages/us-federal/ excepted.
     Fix with: python3 scripts/build-packages.py

Checks 5, 7 and 8 are the derived-tree freshness checks. The derived trees
have exactly one writer: whoever edits skills/ runs the three generators and
commits their output in the same change. Nothing else regenerates them.

Flags:
  --changed-only    per-guide checks (1-3b) only on files changed vs
                    origin/main (PR mode). The freshness checks still run:
                    they describe the whole tree, not the diff.
  --no-index-check  skip the freshness checks (CI's `validate` job; the
                    `guard-derived-trees` job runs them with --derived-only)
  --derived-only    run only the freshness checks (5, 6, 7, 8)

Install scripts/requirements-validation.txt, then run:
python3 scripts/validate-guides.py
"""

import importlib.util
import json
import os
import re
import subprocess
import sys
import tempfile

from frontmatter_yaml import FrontmatterError, load_frontmatter

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD_INDEX = os.path.join(REPO_ROOT, "scripts", "build-index.py")
BUILD_PACKAGES = os.path.join(REPO_ROOT, "scripts", "build-packages.py")
BUILD_LLMS_FULL = os.path.join(REPO_ROOT, "scripts", "build-llms-full.py")

#: How many differing paths a stale-packages error lists before "... and N more".
MAX_LISTED_DIFFS = 10

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


def load_build_packages():
    """The generator module, for HAND_AUTHORED_PACKAGES (its list, not a copy)."""
    spec = importlib.util.spec_from_file_location("build_packages", BUILD_PACKAGES)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# `tax_year` must be a bare integer year, e.g. `tax_year: 2025`. Ranges,
# calendars, and qualifiers go in `tax_year_notes` (see
# scripts/normalize-tax-year.py, issue #49).
TAX_YEAR_RE = re.compile(r"^tax_year:[ \t]*(.*?)[ \t]*$", re.MULTILINE)
TAX_YEAR_MIN, TAX_YEAR_MAX = 2015, 2035


LAST_UPDATED_FMT = re.compile(r"\d{4}-\d{2}-\d{2}")
NON_REVIEWER_MARKERS = {"pending", "pending_review", "none", "no", "false", "-", "n/a", "tbd"}


def real_reviewer(value):
    """Whether a frontmatter reviewer field makes a real named claim."""
    return bool(value and str(value).strip().lower() not in NON_REVIEWER_MARKERS)


def check_quality_metadata(rel, fields, errors):
    """Enforce the fail-closed quality-tier contract for canonical sources."""
    tier = fields["tier"]
    reviewed_by = real_reviewer(fields["reviewed_by"])
    verified_by = real_reviewer(fields["verified_by"])
    if not tier:
        errors.append(f"{rel}: missing required frontmatter key `tier`")
    elif tier not in ("1", "2"):
        errors.append(f"{rel}: `tier` must be 1 or 2 (got {tier!r})")
    elif tier == "1" and not (reviewed_by or verified_by):
        errors.append(f"{rel}: tier 1 requires a real `reviewed_by` or `verified_by` value")
    elif tier == "2" and verified_by:
        errors.append(f"{rel}: tier 2 must not claim accountant verification in `verified_by`")


def changed_files_vs_main():
    """Files changed vs origin/main (PR mode). Empty list = nothing relevant."""
    import subprocess
    try:
        out = subprocess.run(
            ["git", "diff", "--name-only", "origin/main...HEAD"],
            cwd=REPO_ROOT, capture_output=True, text=True, check=True,
        ).stdout
        return [l.strip() for l in out.splitlines() if l.strip()]
    except Exception as e:  # pragma: no cover
        print(f"WARN: could not compute changed files ({e}); validating everything")
        return None


#: Bytes that may precede a frontmatter opener without being part of it:
#: a UTF-8 byte-order mark, spaces, tabs, and line breaks.
LEADING_JUNK = "\ufeff \t\r\n"


def misplaced_frontmatter(bi, text):
    """Whether a file carries a frontmatter block that does not start at byte 0.

    ``extract_frontmatter`` requires ``---`` in the first bytes, so a UTF-8 BOM,
    a leading blank line, or a leading space returns None while
    ``text.startswith("---")`` is also false: the file was counted as a doc and
    silently skipped the strict check. Only flagged when removing the leading
    bytes turns the file into a parseable block, so a doc opening on a `---`
    horizontal rule is not caught by mistake.
    """
    stripped = text.lstrip(LEADING_JUNK)
    if stripped == text or not stripped.startswith("---"):
        return False
    return bi.extract_frontmatter(stripped) is not None


def packages_files():
    """Repo-relative paths of generated package guides, sorted.

    build-index.py's GUIDE_TREES covers skills/ and the hand-authored
    packages/us-federal only, so the rest of the generated tree was validated by
    nothing, while sync-mcp.yml mirrors it to the MCP repo on every push to
    main.
    """
    paths = []
    base = os.path.join(REPO_ROOT, "packages")
    for dirpath, dirnames, filenames in os.walk(base):
        dirnames.sort()
        for filename in sorted(filenames):
            if not filename.endswith(".md"):
                continue
            if filename.lower().startswith("readme"):
                continue
            full = os.path.join(dirpath, filename)
            paths.append(os.path.relpath(full, REPO_ROOT).replace(os.sep, "/"))
    return sorted(set(paths))


LEGACY_DEPENDS_ON = re.compile(r"^(depends_on):[ \t]+(- .+)$", re.MULTILINE)


def normalize_legacy_depends_on(block):
    """Fold the legacy single-line `depends_on: - x` into a real YAML list.

    663 generated files (and their skills/ sources) predate the strict sweep and
    carry the flat form, which strict YAML rejects ("sequence entries are not
    allowed here"). The strictness is right for everything NEW; failing the
    whole tree on a format that shipped for months is not. Normalizing exactly
    this one known shape keeps the sweep strict for every other error while a
    format migration cleans the corpus (tracked separately). Never widen this
    to other keys - each legacy exception must earn its own entry.
    """
    return LEGACY_DEPENDS_ON.sub(lambda m: f"{m.group(1)}:\n  {m.group(2)}", block)


def check_packages_frontmatter(bi, errors, only_files=None):
    """Strict-YAML sweep over the whole generated packages/** tree."""
    already_checked = set(bi.guide_files())
    checked = 0
    for rel in packages_files():
        if rel in already_checked:
            continue  # packages/us-federal gets the full guide contract instead
        if only_files is not None and rel not in only_files:
            continue
        with open(os.path.join(REPO_ROOT, rel), encoding="utf-8", errors="replace") as fh:
            text = fh.read()
        block = bi.extract_frontmatter(text)
        if block is None:
            if text.startswith("---"):
                errors.append(f"{rel}: frontmatter opens with --- but never closes")
            elif misplaced_frontmatter(bi, text):
                errors.append(
                    f"{rel}: frontmatter `---` must be the first bytes of the file"
                )
            continue
        checked += 1
        try:
            load_frontmatter(normalize_legacy_depends_on(block))
        except FrontmatterError as exc:
            errors.append(f"{rel}: invalid YAML frontmatter: {exc}")
    print(f"checked {checked} generated package frontmatter block(s)")


def check_guides(bi, errors, warnings, only_files=None):
    warn_counts = {"jurisdiction (jurisdiction-agnostic dirs)": 0}
    guides = skipped = 0
    for rel in bi.guide_files():
        if only_files is not None and rel not in only_files:
            continue
        with open(os.path.join(REPO_ROOT, rel), encoding="utf-8", errors="replace") as fh:
            text = fh.read()
        block = bi.extract_frontmatter(text)
        if block is None:
            if text.startswith("---"):
                errors.append(f"{rel}: frontmatter opens with --- but never closes")
            elif misplaced_frontmatter(bi, text):
                errors.append(
                    f"{rel}: frontmatter `---` must be the first bytes of the file "
                    "(a byte-order mark, blank line, or leading whitespace before "
                    "it makes the file count as a doc and skip validation entirely)"
                )
            else:
                skipped += 1  # doc file, not a guide
            continue
        guides += 1
        try:
            load_frontmatter(block)
        except FrontmatterError as exc:
            errors.append(f"{rel}: invalid YAML frontmatter: {exc}")
            continue
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
        check_quality_metadata(rel, fields, errors)
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


# Deprecated inventories, removed 2026-07 (they had drifted and nothing read
# them — the MCP server indexes packages/**/*.md frontmatter directly, and the
# website sync works from files + frontmatter). index.json is canonical.
DEPRECATED_INVENTORY_FILES = (
    "skills/manifest.json",
    "packages/manifest.json",
)


def check_no_deprecated_manifests(errors):
    for rel in DEPRECATED_INVENTORY_FILES:
        if os.path.isfile(os.path.join(REPO_ROOT, rel)):
            errors.append(
                f"{rel} is deprecated and must not be committed — index.json is "
                "the canonical inventory (python3 scripts/build-index.py). "
                "Delete the file; see docs/REPO-LAYOUT.md."
            )


def check_llms_full_fresh(errors):
    """llms-full.txt embeds llms.txt, the index inventory, START-HERE, and
    QUALITY-TIERS — it drifts silently when any of those change. Regenerate to
    a temp file and compare, mirroring the index.json staleness check."""
    import subprocess
    import tempfile

    committed = os.path.join(REPO_ROOT, "llms-full.txt")
    if not os.path.isfile(committed):
        errors.append("llms-full.txt is missing — run: python3 scripts/build-llms-full.py")
        return
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as tf:
        tmp = tf.name
    try:
        result = subprocess.run(
            [sys.executable, BUILD_LLMS_FULL, "--out", tmp],
            capture_output=True, text=True,
        )
        if result.returncode != 0:
            errors.append(f"build-llms-full.py failed during freshness check: {result.stderr.strip()}")
            return
        with open(committed, encoding="utf-8") as fh:
            a = fh.read()
        with open(tmp, encoding="utf-8") as fh:
            b = fh.read()
        if a != b:
            errors.append(
                "llms-full.txt is stale (its embedded docs or the guide inventory "
                "changed) — regenerate: python3 scripts/build-llms-full.py"
            )
    finally:
        os.unlink(tmp)


def package_tree_files(root, skip_dirs=()):
    """Relative posix paths of every file under a packages tree.

    Top-level entries named in skip_dirs (the hand-authored packages) are left
    out. A missing root is an empty tree.
    """
    files = set()
    if not os.path.isdir(root):
        return files
    for entry in sorted(os.listdir(root)):
        if entry in skip_dirs:
            continue
        full = os.path.join(root, entry)
        if os.path.isfile(full):
            files.add(entry)
            continue
        for dirpath, dirnames, filenames in os.walk(full):
            dirnames.sort()
            for filename in filenames:
                rel = os.path.relpath(os.path.join(dirpath, filename), root)
                files.add(rel.replace(os.sep, "/"))
    return files


def compare_package_trees(committed_root, fresh_root, skip_dirs=()):
    """Paths where the committed packages tree and a fresh build disagree.

    Each entry is `<relative path> (<why>)`: present on one side only, or
    present on both with different bytes. Empty means the committed tree is
    exactly what the generator produces today.
    """
    committed = package_tree_files(committed_root, skip_dirs)
    fresh = package_tree_files(fresh_root, skip_dirs)
    differing = []
    for rel in sorted(committed | fresh):
        if rel not in committed:
            differing.append(f"{rel} (a fresh build produces it; packages/ lacks it)")
        elif rel not in fresh:
            differing.append(f"{rel} (in packages/; a fresh build does not produce it)")
        else:
            with open(os.path.join(committed_root, rel), "rb") as a:
                a_bytes = a.read()
            with open(os.path.join(fresh_root, rel), "rb") as b:
                b_bytes = b.read()
            if a_bytes != b_bytes:
                differing.append(f"{rel} (content differs)")
    return differing


def check_packages_fresh(errors):
    """packages/** must equal a fresh build, hand-authored directories aside.

    build-packages.py rebuilds in place, so the comparison goes through its
    --out flag into a temp dir. The tree is the copy the MCP server and every
    downloader read; a stale copy serves rules and tiers the sources no longer
    carry (five guides demoted to tier 2 were still served as tier 1 when this
    check was added).
    """
    committed = os.path.join(REPO_ROOT, "packages")
    if not os.path.isdir(committed):
        errors.append("packages/ missing — run: python3 scripts/build-packages.py")
        return
    skip = load_build_packages().HAND_AUTHORED_PACKAGES
    with tempfile.TemporaryDirectory() as tmp:
        fresh = os.path.join(tmp, "packages")
        result = subprocess.run(
            [sys.executable, BUILD_PACKAGES, "--out", fresh],
            cwd=REPO_ROOT, capture_output=True, text=True,
        )
        if result.returncode != 0:
            tail = result.stderr.strip().splitlines()[-5:]
            errors.append(
                "build-packages.py failed while checking freshness: " + " | ".join(tail)
            )
            return
        differing = compare_package_trees(committed, fresh, skip_dirs=skip)
    if differing:
        listed = differing[:MAX_LISTED_DIFFS]
        more = len(differing) - len(listed)
        detail = "\n    ".join(listed) + (f"\n    ... and {more} more" if more else "")
        errors.append(
            f"packages/ is stale ({len(differing)} file(s) differ from a fresh build) "
            "— regenerate with: python3 scripts/build-packages.py\n    " + detail
        )


def main():
    # Modes:
    #   (no flags)        per-guide checks on every guide, the us-federal deletion
    #                     guard, and the derived-tree freshness checks
    #   --changed-only    per-guide checks only on files changed vs origin/main
    #                     (PR mode). The freshness checks still run: they describe
    #                     the whole tree, and a PR that changed no guide can still
    #                     have left index.json or llms-full.txt stale (both embed
    #                     docs/ and llms.txt).
    #   --no-index-check  skip the freshness checks. CI's `validate` job passes
    #                     this because its sibling `guard-derived-trees` job runs
    #                     them with --derived-only; skipping them anywhere else
    #                     hides the one class of staleness nothing else catches.
    #   --derived-only    only the freshness checks (and the deprecated-manifest
    #                     check, which is about the same trees)
    changed_only = "--changed-only" in sys.argv
    no_index_check = "--no-index-check" in sys.argv
    derived_only = "--derived-only" in sys.argv
    if derived_only and no_index_check:
        sys.exit("error: --derived-only and --no-index-check cancel each other out")

    errors, warnings = [], []
    bi = load_build_index()
    if not derived_only:
        only = None
        if changed_only:
            changed = changed_files_vs_main()
            if changed is not None:
                only = {f for f in changed if f.startswith(("skills/", "packages/"))}
                print(f"changed-only mode: validating {len(only)} changed guide file(s)")
        if only is not None and not only:
            print("no guide files changed — skipping the per-guide checks")
        else:
            check_guides(bi, errors, warnings, only_files=only)
            check_packages_frontmatter(bi, errors, only_files=only)
        check_us_federal_deletions(errors)
    check_no_deprecated_manifests(errors)
    if derived_only or not no_index_check:
        check_index_fresh(errors)
        check_llms_full_fresh(errors)
        check_packages_fresh(errors)

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
