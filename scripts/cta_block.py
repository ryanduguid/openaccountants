#!/usr/bin/env python3
"""The "Talk to a verified accountant" CTA block that ends every published guide.

Shared by scripts/validate-guides.py (which enforces the rule) and
scripts/normalize-cta-block.py (which repairs guides to it), so the checker and
the fixer can never disagree about what the block looks like.

The rule, as CLAUDE.md states it: every published guide ends with the
``<!-- openaccountants-cta-block -->`` marker followed by exactly one
"Talk to a verified accountant" section. The marker is what makes a bulk
re-stamp idempotent — a stamp skips any file that already carries it. Before
the 2026-09 sweep, 591 guides carried an older Calendly-linked section *and*
the marker block, and 116 carried no marker at all.
"""

from __future__ import annotations

import re

#: The idempotency marker. A guide carries it exactly once, immediately before
#: its CTA section.
MARKER = "<!-- openaccountants-cta-block -->"

#: The heading every CTA section (old or new) opens with.
HEADING_TEXT = "Talk to a verified accountant"

#: A CTA section heading, at any ATX level, on its own line.
HEADING_RE = re.compile(r"^#{1,6}[ \t]+Talk to a verified accountant[ \t]*$", re.MULTILINE)

#: Any ATX heading line — the boundary a CTA section runs up to. An empty
#: heading (``## `` with nothing after it) counts, so a stray one directly after
#: an old block cannot let the block swallow the content that follows it.
ANY_HEADING_RE = re.compile(r"^#{1,6}(?:[ \t]|$)", re.MULTILINE)

#: What a removable CTA section must mention. Every legacy block links either the
#: Calendly booking page or openaccountants.com; a "Talk to a verified
#: accountant" section without either is not a shape this repo has ever
#: stamped, so the normalizer leaves it alone and reports it.
SECTION_LINK_RE = re.compile(r"calendly\.com|openaccountants\.com", re.IGNORECASE)

#: The block itself, exactly as 1,806 guides already carry it.
CANONICAL_BLOCK = """<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
"""

#: Directories whose guides may omit the block. (They must still not carry
#: two.) The template directories hold scaffolding for new guides, not
#: published guides; skills/integrations/ holds platform guides (export
#: formats, column mappings, reconciliation) that are not tax guides and carry
#: no accountant CTA, by the maintainer's decision after #40 stamped them. Any
#: other guide under skills/ must carry the marker.
OPTIONAL_DIRS = (
    "skills/templates",
    "skills/cross-border/treaty-corridors/_templates",
    "skills/integrations",
)


def is_optional(rel: str) -> bool:
    """Whether a repo-relative POSIX path may omit the CTA block."""
    rel = rel.replace("\\", "/")
    return any(rel == d or rel.startswith(d + "/") for d in OPTIONAL_DIRS)


def is_cta_heading(line: str) -> bool:
    return HEADING_RE.fullmatch(line.rstrip("\r")) is not None


def is_any_heading(line: str) -> bool:
    return ANY_HEADING_RE.match(line) is not None


def has_cta_link(section: str) -> bool:
    """Whether a CTA section is one this repo stamped (it links the network or Calendly)."""
    return SECTION_LINK_RE.search(section) is not None


def section_end(lines: list[str], start: int) -> int:
    """Index of the first line after `start` that opens something else: the next
    ATX heading, the marker, or the end of the file."""
    end = start + 1
    while end < len(lines) and not (is_any_heading(lines[end]) or lines[end].strip() == MARKER):
        end += 1
    return end


def find_markers(lines: list[str]) -> list[tuple[int, int | None, int | None]]:
    """Every marker in a guide body, as (marker_index, heading_index, end_index).

    `heading_index` is the CTA heading the marker introduces: the first line
    after the marker once blank lines and `---` rules are skipped, if that line
    is a "Talk to a verified accountant" heading. `end_index` is where that
    section stops (see section_end). Both are None for a stray marker — one
    that introduces anything else. The validator and the normalizer share this
    reading so a marker means the same thing to both.
    """
    found: list[tuple[int, int | None, int | None]] = []
    for index, line in enumerate(lines):
        if line.strip() != MARKER:
            continue
        cursor = index + 1
        while cursor < len(lines) and lines[cursor].strip() in ("", "---"):
            cursor += 1
        if cursor < len(lines) and is_cta_heading(lines[cursor]):
            found.append((index, cursor, section_end(lines, cursor)))
        else:
            found.append((index, None, None))
    return found
