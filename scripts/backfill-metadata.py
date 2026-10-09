#!/usr/bin/env python3
"""
Backfill missing frontmatter metadata (`tier`, `last_updated`, `jurisdiction`)
across every Guide so index.json is fully populated and validate-guides.py can
treat these as hard requirements.

STRICTLY METADATA-ONLY and MISSING-ONLY: a key that already exists (even with
an odd value) is never rewritten, and nothing outside the frontmatter block is
touched. Body text is preserved byte-for-byte.

What gets backfilled (missing keys only):

  last_updated  Date of the last commit that touched the file, from ONE
                `git log --name-only` pass over history (no per-file
                subprocesses). Inserted as `last_updated: YYYY-MM-DD`.

  tier          `tier: 2` (source-cited draft). A reviewer name alone records
                attribution; tier 1 requires explicit whole-guide sign-off
                under CONTRIBUTING.md. Existing tier keys are preserved.

  jurisdiction  Derived from the path only where unambiguous:
                - skills/us-states/<code>/*            -> US-<CODE>
                - skills/federal/*, packages/us-federal/* -> US
                - skills/international/<dir>/*         -> the jurisdiction
                  code sibling files in the SAME dir already use; a
                  country-name->ISO-3166 dict covers dirs with no sibling
                  convention; genuinely ambiguous dirs are left + reported
                  (skills/international/eu — a shared EU-wide base, not a
                  country).
                - skills/orchestrator/*                -> sibling filename
                  convention: <code>-… prefix (gb-* -> GB, us-ny-* -> US-NY),
                  so au-/ca-/de-/es-/in-/mt- -> AU/CA/DE/ES/IN/MT,
                  us-ca-* -> US-CA, us-federal-* -> US.
                - skills/patterns/*                    -> dir convention
                  (all jurisdiction-bearing siblings say GLOBAL).
                - skills/cross-border/*.md             -> nearest sibling
                  convention, per-file (EU-directive content -> EU-27 like
                  cbam/eu-directives; any-jurisdiction service/treaty guides
                  -> INTL like cross-border-vat-gst; *-matrix -> GLOBAL like
                  every other matrix sibling).
                - skills/foundation/us-tax-workflow-base.md -> US (the one
                  jurisdiction-specific file in an otherwise GLOBAL dir; the
                  us- filename prefix convention matches skills/federal).
                Dirs whose existing convention is "no jurisdiction key"
                (skills/cross-border/treaty-corridors, skills/intelligence,
                skills/templates) are LEFT ALONE and reported — we do not
                invent a convention.

Insertion point: after the last single-line tax_year / tax_year_notes /
jurisdiction value when present. A multiline anchor uses the closing delimiter
as the insertion point. New keys go in the order jurisdiction, tier, last_updated.

Stdlib only. Usage:
    python3 scripts/backfill-metadata.py             # dry run (default)
    python3 scripts/backfill-metadata.py --apply     # rewrite files
"""

import importlib.util
import os
import re
import subprocess
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

from oa_tools.cli import metadata_arguments
from oa_tools import roster
from oa_tools.frontmatter import FRONTMATTER_END_RE

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD_INDEX = os.path.join(REPO_ROOT, "scripts", "build-index.py")

# verified_by values that do NOT count as a real review (same set
# scripts/build-index.py uses for the accountant_reviewed count).
UNREVIEWED_MARKERS = roster.UNREVIEWED_MARKERS

# skills/international/<dir> -> ISO-3166 alpha-2, used ONLY when no sibling
# file in the dir already carries a jurisdiction value.
COUNTRY_CODES = {
    "andorra": "AD",
    "bahamas": "BS",
    "bahrain": "BH",
    "barbados": "BB",
    "brunei": "BN",
    "cambodia": "KH",
    "fiji": "FJ",
    "iran": "IR",
    "iraq": "IQ",
    "isle-of-man": "IM",
    "jamaica": "JM",
    "jordan": "JO",
    "kuwait": "KW",
    "laos": "LA",
    "lebanon": "LB",
    "liechtenstein": "LI",
    "maldives": "MV",
    "mauritius": "MU",
    "monaco": "MC",
    "mongolia": "MN",
    "myanmar": "MM",
    "nepal": "NP",
    "oman": "OM",
    "papua-new-guinea": "PG",
    "qatar": "QA",
    "sri-lanka": "LK",
    "tanzania": "TZ",
    "trinidad-and-tobago": "TT",
    "tunisia": "TN",
    "uganda": "UG",
    "zambia": "ZM",
    "zimbabwe": "ZW",
}

# Per-file assignments where the dir convention is mixed but the sibling
# match is clear (reasoning in the module docstring).
FILE_JURISDICTION = {
    "skills/cross-border/eu-oss-digital.md": "EU-27",
    "skills/cross-border/eu-reverse-charge.md": "EU-27",
    "skills/cross-border/non-eu-export-services.md": "INTL",
    "skills/cross-border/permanent-establishment-risk.md": "INTL",
    "skills/cross-border/withholding-tax-matrix.md": "GLOBAL",
    "skills/foundation/us-tax-workflow-base.md": "US",
}

# Dirs deliberately left without jurisdiction: their existing convention is
# "no jurisdiction key" (or, for international/eu, no single country applies).
LEAVE_DIRS = {
    "skills/cross-border/treaty-corridors",
    "skills/intelligence",
    "skills/templates",
    "skills/international/eu",
}

METADATA_KEYS = ("jurisdiction", "tier", "last_updated", "tax_year", "tax_year_notes")
EDITOR_KEY_RE = re.compile(r"^([A-Za-z_][\w-]*):(?:[ \t]+(.*)|$)")

# Only a complete scalar on one line is a safe immediate insertion anchor.
SINGLE_LINE_VALUE_RE = re.compile(
    r"""(?:(?:"(?:[^"\\]|\\.)*"|'(?:[^']|'')*')(?:\s+#.*)?|[^"'|>!&*\[{].*)"""
)


def load_build_index():
    """Reuse build-index.py's guide discovery + frontmatter parsing verbatim."""
    spec = importlib.util.spec_from_file_location("build_index", BUILD_INDEX)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def git_last_updated_map():
    """path -> YYYY-MM-DD of the newest commit touching it, in ONE git pass."""
    out = subprocess.run(
        [
            "git", "-c", "core.quotepath=false", "log",
            "--pretty=format:\x01%as", "--name-only",
            "--", "skills", "packages/us-federal",
        ],
        cwd=REPO_ROOT, capture_output=True, text=True, check=True,
    )
    dates = {}
    current = None
    for line in out.stdout.splitlines():
        if line.startswith("\x01"):
            current = line[1:].strip()
        elif line.strip() and current:
            dates.setdefault(line.strip(), current)  # newest-first: first wins
    return dates


def derive_jurisdiction(rel, sibling_values):
    """Return (value_or_None, reason). None value means: leave it, reason says why."""
    parts = rel.split("/")
    dirname = os.path.dirname(rel)
    basename = os.path.basename(rel)

    if dirname in LEAVE_DIRS:
        return None, "dir convention is no-jurisdiction (left deliberately)"
    if rel in FILE_JURISDICTION:
        return FILE_JURISDICTION[rel], "per-file sibling-convention assignment"

    if parts[0] == "packages" and parts[1] == "us-federal":
        return "US", "packages/us-federal -> US"
    if parts[0] != "skills":
        return None, "outside known trees"

    tree = parts[1]
    if tree == "federal":
        return "US", "skills/federal -> US"
    if tree == "us-states" and len(parts) >= 4:
        return "US-" + parts[2].upper(), "skills/us-states/<code> -> US-<CODE>"
    if tree == "international" and len(parts) >= 4:
        siblings = sibling_values.get(dirname, set())
        if len(siblings) == 1:
            return next(iter(siblings)), "sibling convention in same dir"
        if len(siblings) > 1:
            return None, "ambiguous: siblings disagree (%s)" % ", ".join(sorted(siblings))
        code = COUNTRY_CODES.get(parts[2])
        if code:
            return code, "country-name -> ISO code (no sibling convention)"
        return None, "no sibling convention and no country mapping"
    if tree == "orchestrator":
        if basename.startswith("us-federal-"):
            return "US", "orchestrator filename convention (us-federal-*)"
        m = re.match(r"^us-([a-z]{2})-", basename)
        if m:
            return "US-" + m.group(1).upper(), "orchestrator filename convention (us-<state>-*)"
        m = re.match(r"^([a-z]{2})-(?:freelance|return|business)", basename)
        if m:
            return m.group(1).upper(), "orchestrator filename convention (<code>-*)"
        return None, "orchestrator file without a recognizable code prefix"

    # Remaining category trees (patterns, foundation, verticals, ...): follow
    # the dir convention only when every jurisdiction-bearing sibling agrees.
    siblings = sibling_values.get(dirname, set())
    if len(siblings) == 1:
        return next(iter(siblings)), "dir convention (all siblings agree)"
    if len(siblings) > 1:
        return None, "ambiguous: siblings disagree (%s)" % ", ".join(sorted(siblings))
    return None, "dir convention is no-jurisdiction (left deliberately)"


def frontmatter_line_span(lines):
    """(start, end) line indexes of the frontmatter body, or None."""
    if not lines or lines[0].strip() != "---":
        return None
    for i in range(1, len(lines)):
        if FRONTMATTER_END_RE.match(lines[i]):
            return (1, i)
    return None


def is_reviewed(fields):
    """Whether fields record explicit tier-1 review; names alone are attribution."""
    return roster.reviewer_of(fields) is not None


def frontmatter_key_lines(lines, start, end):
    """Find column-zero keys, treating quoted scalar continuation lines as opaque.

    Tagged, anchored, flow and nested mapping values, and indented quoted nodes,
    are outside this editor's lexical contract. Refuse them before any insertion.
    """
    keys = []
    quote = None
    block_value = False
    plain_value = False
    for i in range(start, end):
        content = lines[i].rstrip("\r\n")
        if quote is None:
            if not content.strip() or content.lstrip().startswith("#"):
                continue
            match = EDITOR_KEY_RE.match(content)
            if match is None:
                if not content.startswith((" ", "\t")) or not keys:
                    raise ValueError(f"unsupported mapping syntax on line {i + 1}")
                if not block_value:
                    continuation = re.sub(r"^(?:-[ \t]+)+", "", content.lstrip())
                    if ((not plain_value and continuation[:1] in "\"'!&*[{?:") or
                            re.search(r":(?:[ \t]|$)", continuation)):
                        raise ValueError(f"unsupported indented value on line {i + 1}")
                continue
            keys.append((i, match.group(1)))
            content = (match.group(2) or "").strip()
            block_value = bool(re.fullmatch(r"[|>](?:[1-9][+-]?|[+-][1-9]?)?(?:[ \t]+#.*)?", content))
            plain_value = bool(content and not block_value and content[0] not in "#\"'!&*[{")
            if not content or content.startswith("#"):
                continue
            if content[0] in "!&*[{":
                raise ValueError(f"unsupported tagged, anchored or flow value on line {i + 1}")
            if content[0] not in "\"'":
                continue
            quote = content[0]
            cursor = 1
        else:
            cursor = 0
        while cursor < len(content):
            if quote == '"' and content[cursor] == "\\":
                cursor += 2
            elif content[cursor] == quote:
                if quote == "'" and content[cursor:cursor + 2] == "''":
                    cursor += 2
                    continue
                trailing = content[cursor + 1:].strip()
                if trailing and not trailing.startswith("#"):
                    raise ValueError(f"ambiguous quoted value on line {i + 1}")
                quote = None
                break
            else:
                cursor += 1
    if quote is not None:
        raise ValueError("unfinished quoted value")
    return keys


def process_file(rel, bi, git_dates, sibling_values, apply_changes, report):
    path = os.path.join(REPO_ROOT, rel)
    with open(path, encoding="utf-8", newline="") as fh:
        text = fh.read()
    block = bi.extract_frontmatter(text)
    if block is None:
        return  # doc file / broken frontmatter: not a guide, validator's job
    lines = text.splitlines(keepends=True)
    span = frontmatter_line_span(lines)
    if span is None:
        return
    start, end = span

    try:
        key_lines = frontmatter_key_lines(lines, start, end)
    except ValueError as exc:
        report["unsafe_frontmatter"].append((rel, str(exc)))
        return
    fields = bi.parse_known_keys("".join(lines[i] for i, _ in key_lines))
    # Presence protects empty and duplicate keys as well as populated ones.
    present = {key: False for key in METADATA_KEYS}
    anchor = None
    for i, key in key_lines:
        if key in present:
            present[key] = True
            if key in ("tax_year", "tax_year_notes", "jurisdiction"):
                anchor = i + 1
    for key in ("jurisdiction", "tier", "last_updated"):
        if present[key] and not fields[key]:
            report["empty_key"].append((rel, key))
    if anchor is None:
        anchor = end  # insert just before the closing delimiter
    else:
        value = lines[anchor - 1].split(":", 1)[1].strip()
        following = next((line for line in lines[anchor:end]
                          if line.strip() and not line.lstrip().startswith("#")), "")
        if not SINGLE_LINE_VALUE_RE.fullmatch(value) or following.startswith((" ", "\t")):
            # Preserve multiline quoted, block, flow and plain values intact.
            anchor = end

    additions = []  # (key, value) in insertion order

    if not present["jurisdiction"]:
        value, reason = derive_jurisdiction(rel, sibling_values)
        if value is None:
            report["jurisdiction_left"].setdefault(reason, []).append(rel)
        else:
            additions.append(("jurisdiction", value))
            report["jurisdiction"][reason] = report["jurisdiction"].get(reason, 0) + 1

    if not present["tier"]:
        additions.append(("tier", "2"))
        report["tier"] += 1

    if not present["last_updated"]:
        date = git_dates.get(rel)
        if date is None:
            report["no_git_date"].append(rel)
        else:
            additions.append(("last_updated", date))
            report["last_updated"] += 1

    if not additions:
        return

    nl = "\r\n" if lines[0].endswith("\r\n") else "\n"
    new_lines = list(lines)
    for offset, (key, value) in enumerate(additions):
        new_lines.insert(anchor + offset, f"{key}: {value}{nl}")
    if apply_changes:
        with open(path, "w", encoding="utf-8", newline="") as fh:
            fh.write("".join(new_lines))
    report["rows"].append((rel, ", ".join(f"{k}: {v}" for k, v in additions)))


def main(argv=None):
    args = metadata_arguments("Backfill missing guide metadata.", argv)
    if args.help:
        return
    apply_changes = args.apply
    bi = load_build_index()
    git_dates = git_last_updated_map()

    # Existing jurisdiction values per directory (the sibling conventions).
    sibling_values = {}
    guides = []
    for rel in bi.guide_files():
        with open(os.path.join(REPO_ROOT, rel), encoding="utf-8", errors="replace") as fh:
            text = fh.read()
        block = bi.extract_frontmatter(text)
        if block is None:
            continue
        guides.append(rel)
        value = bi.parse_known_keys(block)["jurisdiction"]
        if value:
            sibling_values.setdefault(os.path.dirname(rel), set()).add(value)

    report = {
        "rows": [], "tier": 0, "last_updated": 0, "tier1": [],
        "jurisdiction": {}, "jurisdiction_left": {}, "no_git_date": [],
        "empty_key": [], "unsafe_frontmatter": [],
    }
    for rel in guides:
        process_file(rel, bi, git_dates, sibling_values, apply_changes, report)

    mode = "APPLY" if apply_changes else "DRY RUN"
    print(f"[{mode}] {len(report['rows'])} of {len(guides)} guides need metadata backfill\n")
    for rel, change in report["rows"]:
        print(f"  {rel}\n      + {change}")

    print("\nsummary:")
    print(f"  tier added:         {report['tier']} (tier 1: {len(report['tier1'])})")
    print(f"  last_updated added: {report['last_updated']}")
    print(f"  jurisdiction added: {sum(report['jurisdiction'].values())}")
    for reason, count in sorted(report["jurisdiction"].items()):
        print(f"      {count:4}  {reason}")

    if report["tier1"]:
        print("\ntier: 1 (frontmatter records a real review):")
        for rel in report["tier1"]:
            print(f"  {rel}")

    left = report["jurisdiction_left"]
    if left:
        total = sum(len(v) for v in left.values())
        print(f"\njurisdiction left missing ({total} files):")
        for reason, rels in sorted(left.items()):
            print(f"  [{reason}]")
            for rel in rels:
                print(f"    {rel}")

    for label, key in (("no git date (file not in history?)", "no_git_date"),
                       ("key present but EMPTY (not touched)", "empty_key"),
                       ("unsupported frontmatter (not touched)", "unsafe_frontmatter")):
        if report[key]:
            print(f"\n{label}:")
            for item in report[key]:
                print(f"  {item}")

    if not apply_changes and report["rows"]:
        print("\ndry run — re-run with --apply to write these changes")


if __name__ == "__main__":
    main()
