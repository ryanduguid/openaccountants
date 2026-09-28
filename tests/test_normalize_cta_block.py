from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = REPO_ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))


def _load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / filename)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


normalize_cta = _load("normalize_cta_block", "normalize-cta-block.py")

from cta_block import CANONICAL_BLOCK, MARKER  # noqa: E402  (needs SCRIPTS on sys.path)

DATE = "2026-09-28"

FRONTMATTER = """---
name: synthetic-guide
description: Synthetic guide used by the CTA normalizer tests.
jurisdiction: MT
tier: 2
last_updated: 2026-01-02
---
"""

BUMPED = FRONTMATTER.replace("last_updated: 2026-01-02", f"last_updated: {DATE}")

BODY = """
# Synthetic guide

## Section 1 — Scope

Body.

## Section 9 — Disclaimer

The most up-to-date version is maintained at [openaccountants.com](https://openaccountants.com).
"""

#: The older Calendly section, in the wrapped shape most of the 591 guides had.
OLD_SECTION = """## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).
"""

NORMAL = FRONTMATTER + BODY + "\n" + CANONICAL_BLOCK
NORMAL_BUMPED = BUMPED + BODY + "\n" + CANONICAL_BLOCK


def run(text: str, rel: str = "skills/international/malta/synthetic-guide.md", optional=None):
    return normalize_cta.normalize(text, rel, DATE, optional=optional)


class RemovalTests(unittest.TestCase):
    def test_removes_the_older_section_that_sits_before_the_marker(self) -> None:
        doubled = FRONTMATTER + BODY + "\n" + OLD_SECTION + "\n" + CANONICAL_BLOCK

        new_text, actions, skipped = run(doubled)

        self.assertEqual(new_text, NORMAL_BUMPED)
        self.assertEqual(skipped, [])
        self.assertTrue(any(a.startswith("removed the duplicate CTA section") for a in actions), actions)

    def test_removes_a_mid_file_section_and_keeps_the_content_after_it(self) -> None:
        # 17 guides had the old section in the middle, followed by real sections.
        mid = (
            FRONTMATTER
            + "\n# Synthetic guide\n\nIntro.\n\n"
            + OLD_SECTION
            + "\n## Section 2 — Workflow\n\n0. **Step 1** — Do the thing.\n\n"
            + CANONICAL_BLOCK
        )

        new_text, actions, _ = run(mid)

        self.assertEqual(
            new_text,
            BUMPED
            + "\n# Synthetic guide\n\nIntro.\n\n## Section 2 — Workflow\n\n0. **Step 1** — Do the thing.\n\n"
            + CANONICAL_BLOCK,
        )

    def test_an_empty_heading_after_the_section_bounds_it(self) -> None:
        # A stray `## ` line directly after the old block must stop the removal,
        # or the list under it would be swallowed.
        text = (
            FRONTMATTER
            + "\n# Synthetic guide\n\n"
            + OLD_SECTION
            + "\n## \n\n- **Limit** — 1\n\n"
            + CANONICAL_BLOCK
        )

        new_text, _, _ = run(text)

        self.assertIn("## \n\n- **Limit** — 1\n", new_text)
        self.assertEqual(new_text.count("Talk to a verified accountant"), 1)

    def test_single_line_variant_is_also_removed(self) -> None:
        flat = (
            "## Talk to a verified accountant\n\n"
            "This skill is a tool, not an engagement. → [Book a call](https://calendly.com/openaccountants-info/30min)\n"
        )

        new_text, _, _ = run(FRONTMATTER + BODY + "\n" + flat + "\n" + CANONICAL_BLOCK)

        self.assertEqual(new_text, NORMAL_BUMPED)

    def test_a_section_with_an_unexpected_shape_is_left_in_place(self) -> None:
        odd = "## Talk to a verified accountant\n\nCall your uncle.\n"
        text = FRONTMATTER + BODY + "\n" + odd + "\n" + CANONICAL_BLOCK

        new_text, actions, skipped = run(text)

        self.assertEqual(new_text, text)
        self.assertEqual(actions, [])
        self.assertEqual(len(skipped), 1)
        self.assertIn("unexpected shape", skipped[0])


class AppendTests(unittest.TestCase):
    def test_appends_the_block_when_the_guide_has_none(self) -> None:
        new_text, actions, _ = run(FRONTMATTER + BODY)

        self.assertEqual(new_text, NORMAL_BUMPED)
        self.assertIn("appended the marker CTA block", actions)

    def test_a_trailing_rule_is_folded_into_the_block(self) -> None:
        new_text, _, _ = run(FRONTMATTER + BODY + "\n---\n")

        self.assertEqual(new_text, NORMAL_BUMPED)

    def test_the_new_text_without_the_marker_gains_only_the_marker(self) -> None:
        # One guide carried the marker block's text but not the marker line.
        marker_less = CANONICAL_BLOCK.replace(MARKER + "\n\n", "")

        new_text, _, _ = run(FRONTMATTER + BODY + "\n" + marker_less)

        self.assertEqual(new_text, NORMAL_BUMPED)

    def test_template_guides_are_left_without_a_block(self) -> None:
        text = FRONTMATTER + BODY

        for rel in ("skills/templates/x.md", "skills/cross-border/treaty-corridors/_templates/dtt-template.md"):
            with self.subTest(rel=rel):
                new_text, actions, _ = run(text, rel=rel)
                self.assertEqual(new_text, text)
                self.assertEqual(actions, [])

    def test_template_guides_still_lose_a_duplicate(self) -> None:
        doubled = FRONTMATTER + BODY + "\n" + OLD_SECTION + "\n" + CANONICAL_BLOCK

        new_text, _, _ = run(doubled, rel="skills/templates/x.md")

        self.assertEqual(new_text, NORMAL_BUMPED)


class MarkerRepairTests(unittest.TestCase):
    """A marker means one thing: it introduces the guide's single CTA section.
    Two marker blocks, or a marker that introduces something else, are
    repaired rather than trusted."""

    def test_two_marker_blocks_keep_only_the_last(self) -> None:
        doubled = FRONTMATTER + BODY + "\n" + CANONICAL_BLOCK + "\n## Section 10 — Late addition\n\nMore.\n\n" + CANONICAL_BLOCK

        new_text, actions, skipped = run(doubled)

        self.assertEqual(
            new_text,
            BUMPED + BODY + "\n## Section 10 — Late addition\n\nMore.\n\n" + CANONICAL_BLOCK,
        )
        self.assertEqual(skipped, [])
        self.assertTrue(any(a.startswith("removed a duplicate marker CTA block") for a in actions), actions)

    def test_a_stray_marker_is_dropped_and_the_block_appended(self) -> None:
        # The marker sits above unrelated content and introduces no section.
        stray = FRONTMATTER + "\n# Synthetic guide\n\n" + MARKER + "\n\n## Section 1 — Scope\n\nBody.\n"

        new_text, actions, _ = run(stray)

        self.assertEqual(
            new_text,
            BUMPED + "\n# Synthetic guide\n\n## Section 1 — Scope\n\nBody.\n\n" + CANONICAL_BLOCK,
        )
        self.assertTrue(any(a.startswith("removed a stray CTA marker") for a in actions), actions)

    def test_a_marker_block_followed_by_content_is_not_moved(self) -> None:
        # The hand-authored packages/us-federal/ guides carry a further
        # marker-introduced section after the CTA block; the validator accepts
        # that, so the normalizer leaves such a block where it is.
        trailing = FRONTMATTER + BODY + "\n" + CANONICAL_BLOCK + "\n<!-- openaccountants-mcp-cta -->\n\n## The verified version lives in the connector\n\nText.\n"

        self.assertEqual(run(trailing), (trailing, [], []))


class InvariantTests(unittest.TestCase):
    def test_a_normal_guide_is_untouched_and_keeps_its_date(self) -> None:
        new_text, actions, skipped = run(NORMAL)

        self.assertEqual(new_text, NORMAL)
        self.assertEqual((actions, skipped), ([], []))

    def test_is_idempotent(self) -> None:
        once, _, _ = run(FRONTMATTER + BODY + "\n" + OLD_SECTION + "\n" + CANONICAL_BLOCK)
        twice, actions, _ = run(once)

        self.assertEqual(twice, once)
        self.assertEqual(actions, [])

    def test_docs_without_frontmatter_are_ignored(self) -> None:
        doc = "# Notes\n\n---\n\nSome prose.\n"

        self.assertEqual(run(doc), (doc, [], []))

    def test_last_updated_is_bumped_only_when_the_body_changes(self) -> None:
        untouched, _, _ = run(NORMAL)
        changed, actions, _ = run(FRONTMATTER + BODY)

        self.assertIn("last_updated: 2026-01-02", untouched)
        self.assertIn(f"last_updated: {DATE}", changed)
        self.assertIn(f"set last_updated: {DATE}", actions)


if __name__ == "__main__":
    unittest.main()
