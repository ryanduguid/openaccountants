#!/usr/bin/env python3
"""Keep exactly one CTA block — the marker version — at the end of each guide.

CLAUDE.md says every published guide ends with the
``<!-- openaccountants-cta-block -->`` marker followed by one "Talk to a
verified accountant" section. The corpus drifted from that in two ways:

- 591 guides carried the older Calendly-linked "Talk to a verified accountant"
  section *and* the newer marker block, so the CTA appeared twice (17 of the
  old sections sat mid-file, with real content after them).
- 116 guides carried no marker at all: 115 had no CTA, one had the new text
  without the marker line.

This script repairs both, and nothing else:

1. Every "Talk to a verified accountant" section that is not introduced by the
   marker is removed. A section runs from its heading to the next heading, the
   marker, or the end of the file. Surrounding blank lines collapse to one. A
   section that mentions neither calendly.com nor openaccountants.com is not a
   shape this repo ever stamped, so it is left in place and reported.
2. A guide with no marker gets the canonical block appended (a trailing
   horizontal rule is folded into the block's own), unless it lives in one of
   the template directories listed in scripts/cta_block.py.
3. `last_updated` is set to --date (default: today, UTC) on every guide whose
   body changed, because scripts/check-sync-integrity.py --strict-metadata
   fails a body change that advances neither the date nor the version.

Only files with YAML frontmatter are touched; READMEs and docs are skipped.
Idempotent: a second run changes nothing. scripts/validate-guides.py enforces
the resulting invariant.

Usage:
    python3 scripts/normalize-cta-block.py            # dry run over skills/
    python3 scripts/normalize-cta-block.py --apply    # write the changes
    python3 scripts/normalize-cta-block.py --apply --date 2026-09-28 skills/international/malta
"""

from __future__ import annotations

import argparse
import datetime
import os
import re
import sys

from cta_block import (
    CANONICAL_BLOCK,
    MARKER,
    SECTION_LINK_RE,
    is_any_heading,
    is_cta_heading,
    is_optional,
)

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

_FM_CLOSE_RE = re.compile(r"^(---|\.\.\.)[ \t]*$", re.MULTILINE)
_LAST_UPDATED_RE = re.compile(r"^last_updated:[ \t]*.*$", re.MULTILINE)


def split_frontmatter(text: str) -> tuple[str | None, str]:
    """Return (frontmatter including both delimiters and the newline after the
    closing one, body), or (None, text) when the file has no frontmatter.
    Mirrors scripts/build-index.py's opener rule: `---` at byte 0."""
    if not text.startswith("---"):
        return None, text
    first_nl = text.find("\n")
    if first_nl == -1 or text[:first_nl].strip() != "---":
        return None, text
    close = _FM_CLOSE_RE.search(text, first_nl + 1)
    if close is None:
        return None, text
    end = close.end()
    if end < len(text) and text[end] == "\n":
        end += 1
    return text[:end], text[end:]


def _marker_owned_headings(lines: list[str]) -> set[int]:
    """Indices of CTA headings that the marker introduces: the first heading
    after a marker line, separated from it only by blank lines or a rule."""
    owned: set[int] = set()
    for index, line in enumerate(lines):
        if line.strip() != MARKER:
            continue
        cursor = index + 1
        while cursor < len(lines) and lines[cursor].strip() in ("", "---"):
            cursor += 1
        if cursor < len(lines) and is_cta_heading(lines[cursor]):
            owned.add(cursor)
    return owned


def _strip_trailing_blank(lines: list[str]) -> None:
    while lines and lines[-1].strip() == "":
        lines.pop()


def normalize(
    text: str,
    rel: str = "skills/guide.md",
    date: str | None = None,
    optional: bool | None = None,
) -> tuple[str, list[str], list[str]]:
    """Return (new_text, actions, skipped) for one guide.

    `actions` describes each edit made; `skipped` describes each CTA section
    left in place because its shape was unexpected. Both are empty for a file
    that is already normal or is not a guide.
    """
    frontmatter, body = split_frontmatter(text)
    if frontmatter is None:
        return text, [], []
    if optional is None:
        optional = is_optional(rel)

    actions: list[str] = []
    skipped: list[str] = []
    lines = body.split("\n")
    body_line_offset = frontmatter.count("\n")

    owned = _marker_owned_headings(lines)
    removable = [i for i, line in enumerate(lines) if is_cta_heading(line) and i not in owned]
    for start in reversed(removable):  # bottom-up keeps earlier indices valid
        end = start + 1
        while end < len(lines) and not (is_any_heading(lines[end]) or lines[end].strip() == MARKER):
            end += 1
        section = "\n".join(lines[start:end])
        human_line = body_line_offset + start + 1
        if not SECTION_LINK_RE.search(section):
            skipped.append(
                f"{rel}: line {human_line}: \"Talk to a verified accountant\" section "
                "has an unexpected shape (no calendly.com / openaccountants.com link); left in place"
            )
            continue
        before = lines[:start]
        after = lines[end:]
        _strip_trailing_blank(before)
        while after and after[0].strip() == "":
            after.pop(0)
        lines = before + ([""] + after if after else [""])
        actions.append(f"removed the duplicate CTA section at line {human_line}")

    has_marker = any(line.strip() == MARKER for line in lines)
    if not has_marker and not optional:
        _strip_trailing_blank(lines)
        if lines and lines[-1].strip() == "---":
            lines.pop()  # the canonical block opens with its own rule
            _strip_trailing_blank(lines)
        new_body = "\n".join(lines) + "\n\n" + CANONICAL_BLOCK
        actions.append("appended the marker CTA block")
    else:
        new_body = "\n".join(lines)

    if new_body == body:
        return text, [], skipped

    stamp = date or datetime.datetime.now(datetime.timezone.utc).date().isoformat()
    new_frontmatter, replaced = _LAST_UPDATED_RE.subn(f"last_updated: {stamp}", frontmatter, count=1)
    if replaced:
        actions.append(f"set last_updated: {stamp}")
    return new_frontmatter + new_body, actions, skipped


def guide_paths(targets: list[str]) -> list[str]:
    paths: list[str] = []
    for target in targets:
        if os.path.isfile(target):
            paths.append(target)
            continue
        for dirpath, dirnames, filenames in os.walk(target):
            dirnames.sort()
            for filename in sorted(filenames):
                if filename.endswith(".md") and not filename.lower().startswith("readme"):
                    paths.append(os.path.join(dirpath, filename))
    return sorted(set(paths))


def repo_relative(path: str) -> str:
    absolute = os.path.abspath(path)
    if absolute.startswith(REPO_ROOT + os.sep):
        return os.path.relpath(absolute, REPO_ROOT).replace(os.sep, "/")
    return path.replace(os.sep, "/")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("paths", nargs="*", default=[os.path.join(REPO_ROOT, "skills")],
                        help="files or directories to process (default: skills/)")
    parser.add_argument("--apply", action="store_true", help="write changes (default: dry run)")
    parser.add_argument("--date", default=None, metavar="YYYY-MM-DD",
                        help="last_updated stamp for changed guides (default: today, UTC)")
    parser.add_argument("--quiet", action="store_true", help="print the summary only")
    args = parser.parse_args(argv)

    if args.date and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", args.date):
        parser.error("--date must be YYYY-MM-DD")

    scanned = changed = removed = appended = 0
    skipped_all: list[str] = []
    for path in guide_paths(args.paths):
        rel = repo_relative(path)
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        new_text, actions, skipped = normalize(text, rel, args.date)
        skipped_all.extend(skipped)
        if not text.startswith("---"):
            continue
        scanned += 1
        if not actions:
            continue
        changed += 1
        removed += sum(1 for a in actions if a.startswith("removed"))
        appended += sum(1 for a in actions if a.startswith("appended"))
        if not args.quiet:
            print(f"{'CHANGED' if args.apply else 'WOULD CHANGE'} {rel}: {'; '.join(actions)}")
        if args.apply:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(new_text)

    for note in skipped_all:
        print(f"SKIPPED {note}")
    mode = "APPLIED" if args.apply else "DRY RUN"
    print(f"{mode} — {scanned} guides scanned, {changed} {'changed' if args.apply else 'would change'}: "
          f"{removed} duplicate CTA section(s) removed, {appended} marker block(s) appended, "
          f"{len(skipped_all)} section(s) skipped")
    return 0


if __name__ == "__main__":
    sys.exit(main())
