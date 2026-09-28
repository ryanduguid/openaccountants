"""Relative links in the hand-written docs must point at files and headings
that exist.

START-HERE.md linked to two README headings for a month after the fork's own
README rewrite had removed them (`#try-it-in-60-seconds`,
`#are-you-an-accountant`), and nothing noticed: the file is the human
quick-start and the first thing an agent reads after llms.txt, which embeds
it. This test walks every relative link and `#anchor` in the root-level
markdown, `docs/`, and the two README files the quick-start points at, and
fails on a missing target. External URLs are not checked (no network).
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

CHECKED = sorted(
    {
        *REPO_ROOT.glob("*.md"),
        *(REPO_ROOT / "docs").glob("*.md"),
        REPO_ROOT / "mcp" / "README.md",
        REPO_ROOT / "workflows" / "README.md",
        REPO_ROOT / ".github" / "PULL_REQUEST_TEMPLATE.md",
    }
)

# `[label](target)` and `[label](target "title")`, but not images `![...]()`.
LINK_RE = re.compile(r'(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+"[^"]*")?\)')
FENCE_RE = re.compile(r"^(```|~~~).*?^\1[^\n]*$", re.MULTILINE | re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`]*`")  # a code span may wrap across lines
HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
HEADING_RE = re.compile(r"^#{1,6}\s+(.*?)\s*#*\s*$", re.MULTILINE)
EXPLICIT_ANCHOR_RE = re.compile(r'<a\s+(?:id|name)="([^"]+)"')
EXTERNAL_RE = re.compile(r"^[a-z][a-z0-9+.-]*:", re.IGNORECASE)


def prose(text: str) -> str:
    """The document with fenced blocks, inline code and HTML comments removed,
    so a `[x](y)` quoted as an example is not read as a link."""
    text = FENCE_RE.sub("", text)
    text = HTML_COMMENT_RE.sub("", text)
    return INLINE_CODE_RE.sub("", text)


def slugify(heading: str) -> str:
    """GitHub's heading-to-anchor rule: lowercase, drop everything but word
    characters, hyphens and spaces, then spaces to hyphens."""
    heading = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", heading)  # linked heading text
    heading = heading.replace("`", "").lower()
    heading = re.sub(r"[^\w\- ]", "", heading)
    return heading.replace(" ", "-")


def anchors(path: Path) -> set[str]:
    text = path.read_text(encoding="utf-8")
    found: set[str] = set(EXPLICIT_ANCHOR_RE.findall(text))
    seen: dict[str, int] = {}
    for heading in HEADING_RE.findall(FENCE_RE.sub("", text)):
        slug = slugify(heading)
        n = seen.get(slug, 0)
        found.add(slug if n == 0 else f"{slug}-{n}")
        seen[slug] = n + 1
    return found


def broken_links(path: Path) -> list[str]:
    problems = []
    text = path.read_text(encoding="utf-8")
    for match in LINK_RE.finditer(prose(text)):
        target = match.group(1)
        if EXTERNAL_RE.match(target):
            continue
        file_part, _, anchor = target.partition("#")
        target_path = path if not file_part else (path.parent / file_part).resolve()
        if not target_path.exists():
            problems.append(f"{target}: no such file")
            continue
        if anchor and target_path.is_file():
            if anchor.lower() not in anchors(target_path):
                problems.append(f"{target}: no heading with that anchor")
    return problems


class DocsLinkTests(unittest.TestCase):
    def test_every_relative_link_resolves(self) -> None:
        failures = []
        for path in CHECKED:
            rel = path.relative_to(REPO_ROOT)
            failures.extend(f"{rel} -> {problem}" for problem in broken_links(path))
        self.assertEqual(failures, [], "\n" + "\n".join(failures))

    def test_start_here_links_only_to_live_readme_headings(self) -> None:
        text = (REPO_ROOT / "START-HERE.md").read_text(encoding="utf-8")
        readme_anchors = anchors(REPO_ROOT / "README.md")
        for target in LINK_RE.findall(prose(text)):
            if target.startswith("README.md#"):
                self.assertIn(target.partition("#")[2], readme_anchors, target)

    def test_slugify_matches_github(self) -> None:
        self.assertEqual(slugify("Two states, greppable honesty"), "two-states-greppable-honesty")
        self.assertEqual(slugify("For developers"), "for-developers")
        self.assertEqual(slugify("Legal — Contributor License Agreement (CLA)"), "legal--contributor-license-agreement-cla")
        self.assertEqual(slugify("`index.json` is the only one"), "indexjson-is-the-only-one")


if __name__ == "__main__":
    unittest.main()
