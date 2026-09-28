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

1. Every "Talk to a verified accountant" section that the marker does not
   introduce is removed. A section runs from its heading to the next heading,
   the marker, or the end of the file. Surrounding blank lines collapse to
   one. A section that mentions neither calendly.com nor openaccountants.com
   is not a shape this repo ever stamped, so it is left in place and reported.
2. A guide that carries the marker more than once keeps the last block the
   marker introduces and loses the others; a stray marker (one that introduces
   no CTA section) is dropped.
3. A guide left with no marker gets the canonical block appended (a trailing
   horizontal rule is folded into the block's own), unless it lives in one of
   the exempt directories listed in scripts/cta_block.py (the template
   directories and skills/integrations/).
4. `last_updated` is set to --date (default: today, UTC) on every guide whose
   body changed, because scripts/check-sync-integrity.py --strict-metadata
   fails a body change that advances neither the date nor the version.

The block is not moved: a marker block that other content follows (the
retired packages/us-federal/ guides carried a further marker-introduced
section after it) stays where it is. Only files with YAML frontmatter are
touched; READMEs and docs are skipped. Idempotent: a second run changes
nothing. scripts/validate-guides.py enforces the resulting invariant with the
same reading of the marker (cta_block.find_markers).

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

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:  # the tests load this file by path
    sys.path.insert(0, _HERE)

from cta_block import (  # noqa: E402
    CANONICAL_BLOCK,
    MARKER,
    find_markers,
    has_cta_link,
    is_cta_heading,
    is_optional,
    section_end,
)
from oa_tools import paths  # noqa: E402
from oa_tools.frontmatter import split_frontmatter  # noqa: E402

REPO_ROOT = paths.REPO_ROOT

_LAST_UPDATED_RE = re.compile(r"^last_updated:[ \t]*.*$", re.MULTILINE)


def _strip_trailing_blank(lines: list[str]) -> None:
    while lines and lines[-1].strip() == "":
        lines.pop()


def _delete(lines: list[str], start: int, end: int) -> list[str]:
    """Drop lines[start:end] and leave exactly one blank line at the seam."""
    before = lines[:start]
    after = lines[end:]
    _strip_trailing_blank(before)
    while after and after[0].strip() == "":
        after.pop(0)
    return before + ([""] + after if after else [""])


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
    offset = frontmatter.count("\n")

    def unexpected(index: int) -> None:
        skipped.append(
            f"{rel}: line {offset + index + 1}: \"Talk to a verified accountant\" section "
            "has an unexpected shape (no calendly.com / openaccountants.com link); left in place"
        )

    markers = find_markers(lines)
    proper = [entry for entry in markers if entry[1] is not None]
    keep = proper[-1] if proper else None
    owned = {heading for _, heading, _ in proper}

    removals: list[tuple[int, int, str]] = []
    for marker_index, heading, end in markers:
        if heading is None:
            removals.append((marker_index, marker_index + 1,
                             f"removed a stray CTA marker at line {offset + marker_index + 1}"))
        elif (marker_index, heading, end) != keep:
            if not has_cta_link("\n".join(lines[heading:end])):
                unexpected(heading)
                continue
            removals.append((marker_index, end,
                             f"removed a duplicate marker CTA block at line {offset + marker_index + 1}"))
    for index, line in enumerate(lines):
        if not is_cta_heading(line) or index in owned:
            continue
        end = section_end(lines, index)
        if not has_cta_link("\n".join(lines[index:end])):
            unexpected(index)
            continue
        removals.append((index, end, f"removed the duplicate CTA section at line {offset + index + 1}"))

    for start, end, note in sorted(removals, reverse=True):  # bottom-up keeps indices valid
        lines = _delete(lines, start, end)
        actions.append(note)
    actions.reverse()

    if keep is None and not optional:
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
          f"{removed} duplicate CTA section(s)/marker(s) removed, {appended} marker block(s) appended, "
          f"{len(skipped_all)} section(s) skipped")
    return 0


if __name__ == "__main__":
    sys.exit(main())
