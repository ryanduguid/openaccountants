#!/usr/bin/env python3
"""
Validate guide files, the generated trees, and index.json.

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
     git history (hand-authored, no builder — a deletion is unrecoverable),
     unless it is a guide retired in favour of a skills/federal/ source of
     the same filename. Skipped when git / origin/main is unavailable.
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
  9. Every `depends_on` entry must be the `name` of a guide under skills/ —
     ERROR otherwise. Like the freshness checks, this
     describes the whole tree, so it runs over every guide in every mode but
     --derived-only: a pull request that deletes or renames a base breaks the
     unchanged guides that name it. (238 entries once named
     `income-tax-workflow-base`, `social-contributions-workflow-base` and
     `foundation` while no guide carried those names.)
  10. The closing CTA block (scripts/cta_block.py): at most one "Talk to a
     verified accountant" section per guide, and the
     `<!-- openaccountants-cta-block -->` marker must be present and introduce
     that section — ERROR otherwise, except that the directories in
     cta_block.OPTIONAL_DIRS (templates, integrations) may omit the block.
     Repair with:
     python3 scripts/normalize-cta-block.py --apply

Checks 5, 7 and 8 are the derived-tree freshness checks. The derived trees
have exactly one writer: whoever edits skills/ runs the generators (`make
build`) and commits their output in the same change. Nothing else regenerates
them. PARTNERS.md, the fourth generated file, is checked by
scripts/check-coverage-claims.py rather than here.

Flags:
  --changed-only    per-guide checks (1-3b) only on files changed vs
                    origin/main (PR mode). The freshness checks and check 9
                    still run: they describe the whole tree, not the diff.
  --no-index-check  skip the freshness checks (CI's `validate` job; the
                    `guard-derived-trees` job runs them with --derived-only)
  --derived-only    run only the freshness checks (5, 6, 7, 8)

Install scripts/requirements-validation.txt, then run:
python3 scripts/validate-guides.py
"""

import filecmp
import importlib.util
import json
import os
import re
import subprocess
import sys
import tempfile

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:  # the tests load this file by path
    sys.path.insert(0, _HERE)

from cta_block import MARKER as CTA_MARKER  # noqa: E402
from cta_block import find_markers as cta_markers  # noqa: E402
from cta_block import has_cta_link, is_cta_heading  # noqa: E402
from cta_block import is_optional as cta_optional  # noqa: E402
from oa_tools import guides, paths  # noqa: E402
from oa_tools.frontmatter import (  # noqa: E402
    FrontmatterError,
    extract_frontmatter,
    load_frontmatter,
    parse_known_keys,
)

REPO_ROOT = paths.REPO_ROOT
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

#: The `category` vocabulary (docs/skill-template.md): the topic first
#: (payroll, crypto, formation, bookkeeping, invoicing, tax-optimization,
#: transfer-pricing, financial-statements, orchestrator), otherwise the tree's
#: residual value (international, federal, state-tax, cross-border, foundation,
#: vertical, integration, pattern, intelligence, template). Every guide carries
#: one since 2026-09-29; before that 1,127 had none and 41 carried a legacy
#: synonym, so a join on the key silently dropped most of the corpus.
CATEGORY_VOCABULARY = frozenset({
    "international", "federal", "state-tax", "cross-border", "foundation",
    "orchestrator", "payroll", "tax-optimization", "transfer-pricing", "formation",
    "financial-statements", "bookkeeping", "invoicing", "crypto", "vertical",
    "integration", "pattern", "intelligence", "template",
})

#: A guide whose jurisdiction is US or US-<state> loads the scope-neutral
#: Circular 230 disclosure, so its `depends_on` must name it. The disclosure
#: is its own file because the sole-proprietor workflow base
#: (`us-tax-workflow-base`) carries a refusal catalogue that excludes payroll,
#: corporate and foreign taxpayers, so it cannot be required of every US
#: guide. Exempt: the foundation files (the disclosure and that base), the US
#: GAAP guides under skills/financial-reporting/ (accounting standards, not
#: tax practice) and the file templates.
US_DISCLOSURE = "us-circular-230-disclosure"
US_DISCLOSURE_EXEMPT_DIRS = ("skills/financial-reporting/", "skills/foundation/", "skills/templates/")


class GuideTrees:
    """What the check functions receive as `bi`: guide discovery plus the
    tolerant reader, rooted at this module's REPO_ROOT (the tests patch that,
    and pass stand-ins carrying the same three attributes). These are the
    functions build-index.py runs, so the validator and the inventory agree on
    which files are guides and what their frontmatter says."""

    extract_frontmatter = staticmethod(extract_frontmatter)
    parse_known_keys = staticmethod(parse_known_keys)

    def guide_files(self):
        return guides.guide_files(REPO_ROOT)


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


#: The values `review_status` may take (docs/skill-template.md): review
#: freshness, not assurance. `current` says the recorded sign-off covers the
#: text; `pending_review` that the guide awaits one, as a draft or because a
#: substantive edit superseded the reviewed text.
REVIEW_STATUSES = ("current", "pending_review")


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

    review_status = fields.get("review_status")
    if review_status is None:
        return
    if review_status not in REVIEW_STATUSES:
        errors.append(
            f"{rel}: `review_status` must be current or pending_review (got {review_status!r})"
        )
    elif review_status == "current" and tier == "2":
        # A tier-2 guide has no sign-off for `current` to be current with; the
        # combination read as "reviewed" on every other surface until 2026-09-29.
        errors.append(
            f"{rel}: `review_status: current` on a tier 2 guide claims a sign-off no review gave; "
            "use pending_review"
        )


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

    build-index.py's GUIDE_TREES covers skills/ only, so the generated tree
    was validated by nothing, even while upstream's mirror job shipped it to
    the MCP repo on every push to main.
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
            continue  # a listed guide already gets the full guide contract
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


def collect_guide_names(bi):
    """The `name` of every guide in every tree, validated or not.

    `depends_on` is a cross-file invariant: a slug is valid only if some guide
    carries it, so the lookup set comes from the whole tree even in
    --changed-only mode, where only the dependents in the diff are checked.
    Uses the tolerant key reader so one malformed block elsewhere cannot hide a
    name; the strict parse of that block reports its own error.
    """
    names = set()
    for rel in bi.guide_files():
        with open(os.path.join(REPO_ROOT, rel), encoding="utf-8", errors="replace") as fh:
            block = bi.extract_frontmatter(fh.read())
        if block is None:
            continue
        name = bi.parse_known_keys(block)["name"]
        if name:
            names.add(name)
    return names


def check_unique_names(bi, errors):
    """Every guide `name` is unique: it is the index slug and the MCP slug.

    A duplicate slipped through as two index rows and an MCP catalogue that
    silently dropped the slug. Eight did until 2026-09-28: four state guides
    that reused a country code (`de-income-tax` was Delaware and Germany) and
    four same-slug pairs inside one state folder. A whole-tree check, like
    check_depends_on: the two files that share a name are rarely both in the
    diff.
    """
    owners = {}
    for rel in bi.guide_files():
        with open(os.path.join(REPO_ROOT, rel), encoding="utf-8", errors="replace") as fh:
            block = bi.extract_frontmatter(fh.read())
        if block is None:
            continue
        name = bi.parse_known_keys(block)["name"]
        if name:
            owners.setdefault(name, []).append(rel)
    for name, files in sorted(owners.items()):
        if len(files) > 1:
            errors.append(
                f"`name: {name}` is carried by {len(files)} guides ({', '.join(files)}); "
                "a slug must be unique across the repository"
            )
    print(f"checked {len(owners)} guide names for uniqueness")


def check_depends_on(bi, errors, known_names=None):
    """Every `depends_on` slug must be the `name` of a guide that exists.

    A whole-tree check, run in every mode but --derived-only: the slug lives
    in one file and the name in another, so a pull request that deletes or
    renames a base breaks guides it never touched, and a diff-scoped check
    would pass them. Blocks the strict parser rejects are skipped here;
    check_guides reports those on their own. Before this check, 238 entries
    named `income-tax-workflow-base`, `social-contributions-workflow-base`
    and `foundation` while no guide carried those names, so an agent
    following the dependency found nothing.

    The same pass checks that every US-jurisdiction tax guide names
    US_DISCLOSURE, the scope-neutral Circular 230 disclosure: until
    2026-09-29 only 11 of 239 named even the sole-proprietor base, and that
    base is the wrong file to require, so a reader following the
    dependencies was never sent to a disclosure.
    """
    if known_names is None:
        known_names = collect_guide_names(bi)
    entries = 0
    for rel in bi.guide_files():
        with open(os.path.join(REPO_ROOT, rel), encoding="utf-8", errors="replace") as fh:
            block = bi.extract_frontmatter(fh.read())
        if block is None:
            continue
        try:
            metadata = load_frontmatter(block)
        except FrontmatterError:
            continue
        slugs = [str(slug).strip() for slug in metadata.get("depends_on") or []]
        for slug in slugs:
            entries += 1
            if slug not in known_names:
                errors.append(
                    f"{rel}: `depends_on` names `{slug}`, but no guide under skills/ "
                    "carries that `name` — fix the slug or add the missing base"
                )
        jurisdiction = str(metadata.get("jurisdiction") or "")
        if (
            (jurisdiction == "US" or jurisdiction.startswith("US-"))
            and not rel.startswith(US_DISCLOSURE_EXEMPT_DIRS)
            and US_DISCLOSURE not in slugs
        ):
            errors.append(
                f"{rel}: a `{jurisdiction}` guide must name `{US_DISCLOSURE}` (the Circular 230 "
                "disclosure) in `depends_on`"
            )
    print(f"checked {entries} depends_on entries against {len(known_names)} guide names")


def check_cta_block(rel, text, errors):
    """One CTA section, and the marker directly introduces it (scripts/cta_block.py).

    "Directly" is cta_block.find_markers' reading, shared with the normalizer:
    after the marker, only blank lines or a `---` rule may precede the "Talk
    to a verified accountant" heading, and the section under it must carry
    the network or Calendly link the repo stamps. Placement is not checked:
    a guide may carry a further marker-introduced section after the block,
    as the retired packages/us-federal/ guides did. Before this check, 591 guides
    carried the older Calendly section *and* the marker block, and 116
    carried no marker at all.
    """
    repair = "run: python3 scripts/normalize-cta-block.py --apply"
    lines = text.split("\n")
    markers = cta_markers(lines)
    headings = [index for index, line in enumerate(lines) if is_cta_heading(line)]
    if len(markers) > 1:
        errors.append(f"{rel}: {len(markers)} `{CTA_MARKER}` markers — keep one ({repair})")
    if len(headings) > 1:
        errors.append(
            f"{rel}: {len(headings)} \"Talk to a verified accountant\" sections — "
            f"keep only the marker block ({repair})"
        )
    if len(markers) != 1:
        if not markers and not cta_optional(rel):
            errors.append(
                f"{rel}: missing the `{CTA_MARKER}` CTA block that ends every "
                f"published guide ({repair})"
            )
        return  # several markers are reported above; the normalizer keeps the last block
    _, heading, end = markers[0]
    if heading is None:
        errors.append(
            f"{rel}: `{CTA_MARKER}` must directly introduce the \"Talk to a verified "
            f"accountant\" section — only blank lines or a `---` rule may sit between "
            f"them ({repair})"
        )
    elif not has_cta_link("\n".join(lines[heading:end])):
        errors.append(
            f"{rel}: the \"Talk to a verified accountant\" section under `{CTA_MARKER}` "
            f"has no openaccountants.com or calendly.com link — not the stamped block ({repair})"
        )


US_STATE_GUIDE = re.compile(r"^skills/us-states/([a-z]{2})/[^/]+\.md$")


def check_state_naming(rel, name, errors):
    """A US-state guide is `us-<state>-<topic>` and its file is `<name>.md`.

    Twenty-one state codes are also ISO country codes in use here (DE is
    Delaware and Germany, CA California and Canada), so a bare `de-income-tax`
    collided with Germany's and dropped out of the MCP catalogue. Since
    2026-09-28 every state guide carries the `us-<code>-` namespace, the one
    the packages (`us-de/`), the jurisdiction codes (`US-DE`) and the state
    orchestrators (`us-ca-freelance-intake`) already use.
    """
    match = US_STATE_GUIDE.match(rel)
    if not match or not name:
        return
    prefix = f"us-{match.group(1)}-"
    stem = os.path.splitext(os.path.basename(rel))[0]
    if not name.startswith(prefix) or stem != name:
        errors.append(
            f"{rel}: a US-state guide's `name` starts `{prefix}` and its file is named "
            f"`<name>.md` (got `name: {name}` in `{stem}.md`; see docs/skill-template.md)"
        )


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
        check_state_naming(rel, fields["name"], errors)
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
        category = fields["category"]
        if not category:
            errors.append(
                f"{rel}: missing required frontmatter key `category` "
                "(the vocabulary is in docs/skill-template.md)"
            )
        elif category not in CATEGORY_VOCABULARY:
            errors.append(
                f"{rel}: `category` must be one of the vocabulary in docs/skill-template.md "
                f"(got {category!r})"
            )
        check_cta_block(rel, text, errors)
    for key, count in sorted(warn_counts.items()):
        if count:
            warnings.append(f"{count} guides missing `{key}`")
    print(f"checked {guides} guides ({skipped} non-guide .md files skipped)")


def check_us_federal_deletions(errors):
    """The hand-authored us-federal package has no builder; a deleted file is gone.

    One deletion is allowed: a guide whose source now lives in skills/federal/
    under the same filename. That is how the 28 federal twins were retired on
    2026-09-28, and how any future twin would be, without losing content.
    The rates JSONs and the runbook have no source elsewhere and stay guarded.
    """
    federal_source = os.path.join(REPO_ROOT, "skills", "federal")
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
            if not status.startswith("D"):
                continue
            if path.endswith(".md") and os.path.isfile(os.path.join(federal_source, os.path.basename(path))):
                continue  # retired in favour of its skills/federal source
            errors.append(f"hand-authored file deleted ({label}): {path}")


def check_index_fresh(errors):
    index_path = os.path.join(REPO_ROOT, "index.json")
    if not os.path.isfile(index_path):
        errors.append("index.json missing — run: python3 scripts/build-index.py")
        return
    try:
        spec = importlib.util.spec_from_file_location("build_index_module", BUILD_INDEX)
        if spec is None or spec.loader is None:
            raise ImportError("Could not load build-index.py")
        builder = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(builder)
        fresh = builder.build_index()
    except Exception as exc:
        errors.append(f"build-index.py failed while checking freshness: {exc}")
        return
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
    """llms-full.txt embeds llms.txt, the index inventory, START-HERE,
    QUALITY-TIERS and PARTNERS.md — it drifts silently when any of those
    change. Regenerate to a temp file and compare, mirroring the index.json
    staleness check."""
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
    """Entries under a packages tree, keyed by relative posix path.

    The value is True for a regular file and False for anything else: a
    symlink (to a file or a directory), a device, a socket. Top-level entries
    named in skip_dirs (the hand-authored packages) are left out. A missing
    root is an empty tree. Nothing is opened here and symlinks are never
    followed, so a link pointing outside the tree costs nothing to list.
    """
    entries = {}
    if not os.path.isdir(root):
        return entries

    def record(path):
        rel = os.path.relpath(path, root).replace(os.sep, "/")
        entries[rel] = not os.path.islink(path) and os.path.isfile(path)

    for entry in sorted(os.listdir(root)):
        if entry in skip_dirs:
            continue
        full = os.path.join(root, entry)
        if os.path.islink(full) or not os.path.isdir(full):
            record(full)
            continue
        for dirpath, dirnames, filenames in os.walk(full):  # never follows links
            dirnames.sort()
            for name in dirnames:
                sub = os.path.join(dirpath, name)
                if os.path.islink(sub):
                    record(sub)  # listed as an entry, never entered
            for name in filenames:
                record(os.path.join(dirpath, name))
    return entries


def compare_package_trees(committed_root, fresh_root, skip_dirs=()):
    """Paths where the committed packages tree and a fresh build disagree.

    Each entry is `<relative path> (<why>)`: present on one side only, not a
    regular file (the generator only ever writes regular files, and a symlink
    in the checkout is reported without following it), or present on both
    with different bytes. Contents are compared in bounded chunks, never read
    whole into memory. Empty means the committed tree is exactly what the
    generator produces today.
    """
    committed = package_tree_files(committed_root, skip_dirs)
    fresh = package_tree_files(fresh_root, skip_dirs)
    differing = []
    for rel in sorted(set(committed) | set(fresh)):
        in_committed, in_fresh = committed.get(rel), fresh.get(rel)
        if in_committed is False or in_fresh is False:
            differing.append(f"{rel} (not a regular file; a fresh build only writes regular files)")
        elif in_committed is None:
            differing.append(f"{rel} (a fresh build produces it; packages/ lacks it)")
        elif in_fresh is None:
            differing.append(f"{rel} (in packages/; a fresh build does not produce it)")
        elif not filecmp.cmp(
            os.path.join(committed_root, rel), os.path.join(fresh_root, rel), shallow=False
        ):
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
    skip = paths.HAND_AUTHORED_PACKAGES
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
    bi = GuideTrees()
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
        check_depends_on(bi, errors)
        check_unique_names(bi, errors)
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
