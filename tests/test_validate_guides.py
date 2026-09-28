from __future__ import annotations

import contextlib
import importlib.util
import io
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

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


validate_guides = _load("validate_guides", "validate-guides.py")
build_index = _load("build_index_for_validator_tests", "build-index.py")

from cta_block import CANONICAL_BLOCK, MARKER as CTA_MARKER  # noqa: E402  (needs SCRIPTS on sys.path)


#: A guide with everything but the closing CTA block — the shape 116 guides had.
GOOD_WITHOUT_CTA = """---
name: synthetic-guide
description: Synthetic guide used by the validator tests.
jurisdiction: MT
category: international
tier: 2
tax_year: 2025
last_updated: 2026-01-02
---

# Synthetic guide

Body.
"""

GOOD = GOOD_WITHOUT_CTA + "\n" + CANONICAL_BLOCK

#: The older Calendly-linked section that 591 guides carried beside the marker block.
OLD_CTA_SECTION = """## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**
"""

#: `depends_on: - x` is the shape the tolerant regex reader accepts and PyYAML
#: rejects, and the one 681 generated files carried.
# The flat `depends_on: - x` is now a GRANDFATHERED legacy form (663 files carry
# it; normalize_legacy_depends_on folds it into a real list before the strict
# parse). Malformed-for-testing therefore uses a shape with no legacy excuse:
# an unquoted colon inside a scalar.
MALFORMED = GOOD.replace("tier: 2\n", 'tier: 2\nqualifier: bad: colon soup\n')
LEGACY_FLAT_DEPENDS = GOOD.replace("tier: 2\n", "tier: 2\ndepends_on: - workflow-base\n")

#: A doc that opens on a horizontal rule, not frontmatter.
PLAIN_DOC = "# Notes\n\n---\n\nSome prose.\n"


class _Trees:
    """A `bi` stand-in: the real parsers, but a guide list the test controls."""

    def __init__(self, guides) -> None:
        self._guides = sorted(guides)
        self.extract_frontmatter = build_index.extract_frontmatter
        self.parse_known_keys = build_index.parse_known_keys

    def guide_files(self):
        return list(self._guides)


class _ValidatorCase(unittest.TestCase):
    def _tree(self, files) -> Path:
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        for rel, text in files.items():
            path = root / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
        return root

    def _check_guides(self, files, only_files=None):
        root = self._tree(files)
        errors, warnings = [], []
        with mock.patch.object(validate_guides, "REPO_ROOT", str(root)):
            with contextlib.redirect_stdout(io.StringIO()):
                validate_guides.check_guides(
                    _Trees(files), errors, warnings, only_files=only_files
                )
        return errors

    def _check_packages(self, files, guide_files=()):
        root = self._tree(files)
        errors = []
        with mock.patch.object(validate_guides, "REPO_ROOT", str(root)):
            with contextlib.redirect_stdout(io.StringIO()):
                validate_guides.check_packages_frontmatter(_Trees(guide_files), errors)
        return errors


class BuildIndexSlugTests(_ValidatorCase):
    def test_index_uses_canonical_names_for_same_named_country_files(self):
        root = self._tree({
            "skills/international/australia/references.md": GOOD.replace(
                "synthetic-guide", "australia-references"
            ).replace("jurisdiction: MT", "jurisdiction: AU"),
            "skills/international/malta/references.md": GOOD.replace(
                "synthetic-guide", "malta-references"
            ),
        })
        with mock.patch.object(build_index, "REPO_ROOT", str(root)):
            guides = build_index.build_index()["guides"]
        self.assertEqual(
            {(guide["slug"], guide["jurisdiction"]) for guide in guides},
            {("australia-references", "AU"), ("malta-references", "MT")},
        )

    def test_index_keeps_filename_fallback_for_unnamed_legacy_guides(self):
        root = self._tree({"skills/legacy.md": GOOD.replace("name: synthetic-guide\n", "")})
        with mock.patch.object(build_index, "REPO_ROOT", str(root)):
            guide = build_index.build_index()["guides"][0]
        self.assertEqual(guide["slug"], "legacy")


class StrictFrontmatterTests(_ValidatorCase):
    """The strict loader in check_guides had no test at all, so deleting it
    left `unittest discover` green while the primary validator reverted to the
    tolerant regex reader."""

    def test_valid_guide_passes(self) -> None:
        self.assertEqual(self._check_guides({"skills/good.md": GOOD}), [])

    def test_malformed_yaml_is_an_error(self) -> None:
        errors = self._check_guides({"skills/bad.md": MALFORMED})

        self.assertEqual(len(errors), 1, errors)
        self.assertIn("invalid YAML frontmatter", errors[0])

    def test_duplicate_keys_are_an_error(self) -> None:
        doubled = GOOD.replace("tier: 2\n", "tier: 2\ntier: 1\n")

        errors = self._check_guides({"skills/doubled.md": doubled})

        self.assertEqual(len(errors), 1, errors)
        self.assertIn("invalid YAML frontmatter", errors[0])


class MisplacedFrontmatterTests(_ValidatorCase):
    """`---` must be at byte 0. Otherwise extract_frontmatter returns None and
    text.startswith("---") is false, so the file counted as a doc and bypassed
    the strict check entirely: exit 0 with skipped += 1."""

    def test_byte_order_mark_before_frontmatter_is_rejected(self) -> None:
        errors = self._check_guides({"skills/bom.md": "\ufeff" + MALFORMED})

        self.assertEqual(len(errors), 1, errors)
        self.assertIn("first bytes", errors[0])

    def test_leading_blank_line_before_frontmatter_is_rejected(self) -> None:
        errors = self._check_guides({"skills/blank.md": "\n" + MALFORMED})

        self.assertEqual(len(errors), 1, errors)
        self.assertIn("first bytes", errors[0])

    def test_leading_space_before_frontmatter_is_rejected(self) -> None:
        errors = self._check_guides({"skills/space.md": " " + MALFORMED})

        self.assertEqual(len(errors), 1, errors)
        self.assertIn("first bytes", errors[0])

    def test_a_doc_opening_on_a_horizontal_rule_is_still_skipped(self) -> None:
        self.assertEqual(self._check_guides({"skills/notes.md": PLAIN_DOC}), [])


class GeneratedPackagesTreeTests(_ValidatorCase):
    """packages/** was validated by nothing: build-index.py's GUIDE_TREES stops
    at skills/ plus the hand-authored packages/us-federal, and sync-mcp.yml
    mirrors the rest to the MCP repo on every push to main."""

    def test_malformed_generated_frontmatter_is_an_error(self) -> None:
        errors = self._check_packages({"packages/albania/albania-income-tax.md": MALFORMED})

        self.assertEqual(len(errors), 1, errors)
        self.assertIn("invalid YAML frontmatter", errors[0])

    def test_legacy_flat_depends_on_is_grandfathered(self) -> None:
        # 663 existing files predate the strict sweep with this exact shape;
        # failing the whole tree on shipped history helps nobody. Only this one
        # key is folded — see normalize_legacy_depends_on.
        self.assertEqual(
            self._check_packages({"packages/albania/albania-income-tax.md": LEGACY_FLAT_DEPENDS}), []
        )

    def test_valid_generated_frontmatter_passes(self) -> None:
        self.assertEqual(
            self._check_packages({"packages/albania/albania-income-tax.md": GOOD}), []
        )

    def test_readmes_and_us_federal_are_not_double_reported(self) -> None:
        errors = self._check_packages(
            {
                "packages/us-federal/hand-authored.md": MALFORMED,
                "packages/albania/README.md": MALFORMED,
            },
            guide_files=["packages/us-federal/hand-authored.md"],
        )

        self.assertEqual(errors, [])


def _with_depends_on(text, *slugs):
    return text.replace(
        "tier: 2\n", "tier: 2\ndepends_on:\n" + "".join(f"  - {slug}\n" for slug in slugs)
    )


class DependsOnTests(_ValidatorCase):
    """`depends_on` is a promise that a guide exists. 238 entries broke it: no
    guide carried `income-tax-workflow-base`, `social-contributions-workflow-
    base` or `foundation`, and nothing noticed."""

    def test_dangling_depends_on_is_an_error(self) -> None:
        errors = self._check_guides(
            {"skills/dependent.md": _with_depends_on(GOOD, "no-such-base")}
        )

        self.assertEqual(len(errors), 1, errors)
        self.assertIn("`depends_on` names `no-such-base`", errors[0])

    def test_depends_on_resolves_against_both_guide_trees(self) -> None:
        files = {
            "skills/dependent.md": _with_depends_on(GOOD, "workflow-base", "us-form-1040"),
            "skills/foundation/workflow-base.md": GOOD.replace("synthetic-guide", "workflow-base"),
            "packages/us-federal/us-form-1040.md": GOOD.replace("synthetic-guide", "us-form-1040"),
        }

        self.assertEqual(self._check_guides(files), [])

    def test_names_come_from_the_whole_tree_in_changed_only_mode(self) -> None:
        # PR mode validates only the files in the diff; the base the dependent
        # names is not in the diff and must still count.
        files = {
            "skills/dependent.md": _with_depends_on(GOOD, "workflow-base"),
            "skills/foundation/workflow-base.md": GOOD.replace("synthetic-guide", "workflow-base"),
        }

        self.assertEqual(self._check_guides(files, only_files={"skills/dependent.md"}), [])

    def test_a_dependent_cannot_satisfy_itself_with_a_filename(self) -> None:
        # The slug must match a `name`, not a path stem.
        files = {"skills/foundation/other-base.md": _with_depends_on(GOOD, "other-base")}

        errors = self._check_guides(files)

        self.assertEqual(len(errors), 1, errors)
        self.assertIn("other-base", errors[0])


class CtaBlockTests(_ValidatorCase):
    """Every published guide ends with the marker followed by exactly one
    "Talk to a verified accountant" section. 591 guides had two sections and
    116 had no marker before scripts/normalize-cta-block.py swept them."""

    def test_the_canonical_block_passes(self) -> None:
        self.assertEqual(self._check_guides({"skills/good.md": GOOD}), [])

    def test_a_second_cta_section_is_an_error(self) -> None:
        doubled = GOOD_WITHOUT_CTA + "\n" + OLD_CTA_SECTION + "\n" + CANONICAL_BLOCK

        errors = self._check_guides({"skills/doubled.md": doubled})

        self.assertEqual(len(errors), 1, errors)
        self.assertIn('2 "Talk to a verified accountant" sections', errors[0])

    def test_a_missing_marker_is_an_error(self) -> None:
        errors = self._check_guides({"skills/bare.md": GOOD_WITHOUT_CTA})

        self.assertEqual(len(errors), 1, errors)
        self.assertIn(f"missing the `{CTA_MARKER}` CTA block", errors[0])

    def test_an_old_section_without_the_marker_is_still_a_missing_marker(self) -> None:
        errors = self._check_guides(
            {"skills/old.md": GOOD_WITHOUT_CTA + "\n" + OLD_CTA_SECTION}
        )

        self.assertEqual(len(errors), 1, errors)
        self.assertIn("missing the", errors[0])

    def test_template_directories_may_omit_the_block(self) -> None:
        files = {
            "skills/templates/crypto-template.md": GOOD_WITHOUT_CTA,
            "skills/cross-border/treaty-corridors/_templates/dtt-template.md": GOOD_WITHOUT_CTA,
        }

        self.assertEqual(self._check_guides(files), [])

    def test_template_directories_still_cannot_carry_two_sections(self) -> None:
        doubled = GOOD_WITHOUT_CTA + "\n" + OLD_CTA_SECTION + "\n" + CANONICAL_BLOCK

        errors = self._check_guides({"skills/templates/crypto-template.md": doubled})

        self.assertEqual(len(errors), 1, errors)
        self.assertIn("2 \"Talk to a verified accountant\" sections", errors[0])

    def test_the_marker_must_introduce_the_section(self) -> None:
        # Marker present, but the only section sits above it — the marker no
        # longer marks anything.
        inverted = GOOD_WITHOUT_CTA + "\n" + OLD_CTA_SECTION + "\n" + CTA_MARKER + "\n"

        errors = self._check_guides({"skills/inverted.md": inverted})

        self.assertEqual(len(errors), 1, errors)
        self.assertIn("must be followed by", errors[0])

    def test_two_markers_are_an_error(self) -> None:
        errors = self._check_guides({"skills/twice.md": GOOD + "\n" + CTA_MARKER + "\n"})

        self.assertEqual(len(errors), 1, errors)
        self.assertIn("2 `<!-- openaccountants-cta-block -->` markers", errors[0])

    def test_a_prose_mention_is_not_a_section(self) -> None:
        mentioned = GOOD.replace("Body.\n", "Body. See the Talk to a verified accountant section below.\n")

        self.assertEqual(self._check_guides({"skills/prose.md": mentioned}), [])


if __name__ == "__main__":
    unittest.main()
