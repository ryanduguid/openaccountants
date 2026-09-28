from __future__ import annotations

import contextlib
import importlib.util
import io
import os
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

    def _check_depends_on(self, files):
        root = self._tree(files)
        errors = []
        with mock.patch.object(validate_guides, "REPO_ROOT", str(root)):
            with contextlib.redirect_stdout(io.StringIO()):
                validate_guides.check_depends_on(_Trees(files), errors)
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


class PackagesFreshnessTests(_ValidatorCase):
    """Nothing compared packages/ to skills/: build-packages.py rebuilds in
    place, so a stale copy of a corrected guide sat in packages/ (and was served
    by the MCP server) until someone happened to rebuild."""

    def _trees(self, committed, fresh):
        root = self._tree(
            {f"committed/{rel}": text for rel, text in committed.items()}
            | {f"fresh/{rel}": text for rel, text in fresh.items()}
        )
        return str(root / "committed"), str(root / "fresh")

    def test_identical_trees_have_no_differences(self) -> None:
        committed, fresh = self._trees({"albania/a.md": GOOD}, {"albania/a.md": GOOD})

        self.assertEqual(validate_guides.compare_package_trees(committed, fresh), [])

    def test_changed_missing_and_extra_files_are_all_reported(self) -> None:
        committed, fresh = self._trees(
            {"albania/a.md": GOOD, "albania/old.md": GOOD},
            {"albania/a.md": GOOD.replace("Body.", "Changed."), "bulgaria/new.md": GOOD},
        )

        differing = validate_guides.compare_package_trees(committed, fresh)

        self.assertEqual(
            [entry.split(" ", 1)[0] for entry in differing],
            ["albania/a.md", "albania/old.md", "bulgaria/new.md"],
        )

    def test_hand_authored_directories_are_not_compared(self) -> None:
        # packages/us-federal has no builder, so a fresh build never contains it.
        committed, fresh = self._trees({"us-federal/form.md": GOOD}, {})

        self.assertEqual(
            validate_guides.compare_package_trees(committed, fresh, skip_dirs={"us-federal"}),
            [],
        )

    def _symlink(self, target, link):
        try:
            os.symlink(target, link)
        except (OSError, NotImplementedError):  # pragma: no cover - platform limit
            self.skipTest("symlinks are not available here")

    def test_a_symlinked_file_is_reported_without_being_followed(self) -> None:
        # The check runs against a pull request's checkout, so a committed link
        # to something large outside the tree must be reported, not read. The
        # link here points at a byte-identical regular file: following it would
        # compare equal and report nothing.
        committed, fresh = self._trees(
            {"albania/a.md": GOOD}, {"albania/a.md": GOOD, "albania/b.md": GOOD}
        )
        self._symlink(os.path.join(fresh, "albania", "b.md"), os.path.join(committed, "albania", "b.md"))

        differing = validate_guides.compare_package_trees(committed, fresh)

        self.assertEqual(len(differing), 1, differing)
        self.assertTrue(differing[0].startswith("albania/b.md (not a regular file"), differing)

    def test_a_symlinked_directory_is_reported_without_being_entered(self) -> None:
        committed, fresh = self._trees({"albania/a.md": GOOD}, {"albania/a.md": GOOD})
        self._symlink(os.path.join(fresh, "albania"), os.path.join(committed, "bulgaria"))

        differing = validate_guides.compare_package_trees(committed, fresh)

        self.assertEqual(len(differing), 1, differing)
        self.assertTrue(differing[0].startswith("bulgaria (not a regular file"), differing)


class ValidatorModeTests(unittest.TestCase):
    """The freshness checks describe the whole tree, so PR mode must not skip
    them when the PR changed no guide file (the old early return did), and
    --derived-only must run nothing else."""

    CHECKS = (
        "check_guides",
        "check_packages_frontmatter",
        "check_us_federal_deletions",
        "check_depends_on",
        "check_no_deprecated_manifests",
        "check_index_fresh",
        "check_llms_full_fresh",
        "check_packages_fresh",
    )
    FRESHNESS = ("check_index_fresh", "check_llms_full_fresh", "check_packages_fresh")

    def _run(self, argv, changed):
        calls: list[str] = []
        with contextlib.ExitStack() as stack:
            for name in self.CHECKS:
                stack.enter_context(mock.patch.object(
                    validate_guides, name,
                    side_effect=lambda *a, _name=name, **k: calls.append(_name),
                ))
            stack.enter_context(mock.patch.object(
                validate_guides, "changed_files_vs_main", return_value=changed,
            ))
            stack.enter_context(mock.patch.object(sys, "argv", ["validate-guides.py", *argv]))
            stack.enter_context(contextlib.redirect_stdout(io.StringIO()))
            validate_guides.main()
        return calls

    def test_changed_only_with_no_guide_changes_still_checks_freshness(self) -> None:
        calls = self._run(["--changed-only"], changed=["docs/QUALITY-TIERS.md"])

        self.assertNotIn("check_guides", calls)
        self.assertIn("check_depends_on", calls)  # whole-tree, like freshness
        for name in self.FRESHNESS:
            self.assertIn(name, calls)

    def test_derived_only_runs_only_the_freshness_checks(self) -> None:
        calls = self._run(["--derived-only"], changed=None)

        self.assertEqual(set(calls), {"check_no_deprecated_manifests", *self.FRESHNESS})

    def test_no_index_check_runs_everything_but_freshness(self) -> None:
        calls = self._run(["--no-index-check"], changed=None)

        self.assertIn("check_guides", calls)
        self.assertIn("check_us_federal_deletions", calls)
        for name in self.FRESHNESS:
            self.assertNotIn(name, calls)


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
    base` or `foundation`, and nothing noticed. The check reads the whole
    tree, never the diff: the slug and the name live in different files."""

    def test_dangling_depends_on_is_an_error(self) -> None:
        errors = self._check_depends_on(
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

        self.assertEqual(self._check_depends_on(files), [])

    def test_a_deleted_base_is_caught_without_touching_its_dependents(self) -> None:
        # PR mode runs the per-guide checks on the diff only. A pull request
        # that deletes a base changes nothing in the guides that name it, so
        # those guides are outside the diff — and the dangling slug must still
        # be reported. The per-guide loop therefore does not own this check.
        files = {"skills/dependent.md": _with_depends_on(GOOD, "workflow-base")}

        self.assertEqual(self._check_guides(files, only_files=set()), [])
        errors = self._check_depends_on(files)

        self.assertEqual(len(errors), 1, errors)
        self.assertIn("workflow-base", errors[0])

    def test_a_dependent_cannot_satisfy_itself_with_a_filename(self) -> None:
        # The slug must match a `name`, not a path stem.
        files = {"skills/foundation/other-base.md": _with_depends_on(GOOD, "other-base")}

        errors = self._check_depends_on(files)

        self.assertEqual(len(errors), 1, errors)
        self.assertIn("other-base", errors[0])

    def test_a_malformed_block_is_left_to_the_per_guide_checks(self) -> None:
        # check_guides reports the YAML error; this check must not double up
        # or crash on the block it cannot read.
        files = {
            "skills/bad.md": MALFORMED,
            "skills/dependent.md": _with_depends_on(GOOD, "synthetic-guide"),
        }

        self.assertEqual(self._check_depends_on(files), [])


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
        self.assertIn("must directly introduce", errors[0])

    def test_content_between_the_marker_and_the_section_is_an_error(self) -> None:
        # A marker above unrelated content, with the section further down, is
        # not a marked block: only blank lines or a rule may separate them.
        drifted = (
            GOOD_WITHOUT_CTA + "\n" + CTA_MARKER + "\n\n## Section 9 — Appendix\n\nText.\n\n"
            + CANONICAL_BLOCK.replace(CTA_MARKER + "\n\n", "")
        )

        errors = self._check_guides({"skills/drifted.md": drifted})

        self.assertEqual(len(errors), 1, errors)
        self.assertIn("must directly introduce", errors[0])

    def test_an_empty_section_under_the_marker_is_an_error(self) -> None:
        empty = GOOD_WITHOUT_CTA + "\n" + CTA_MARKER + "\n\n## Talk to a verified accountant\n"

        errors = self._check_guides({"skills/empty.md": empty})

        self.assertEqual(len(errors), 1, errors)
        self.assertIn("no openaccountants.com or calendly.com link", errors[0])

    def test_the_hand_authored_federal_shape_passes(self) -> None:
        # packages/us-federal/ guides carry the marker, a blank line, the
        # Calendly text, and then a further marker-introduced section after
        # the block. Placement is theirs to decide; the block is still one.
        federal = (
            GOOD_WITHOUT_CTA + "\n" + CTA_MARKER + "\n\n" + OLD_CTA_SECTION
            + "\n<!-- openaccountants-mcp-cta -->\n\n## The accountant-verified version lives in the connector\n\nText.\n"
        )

        self.assertEqual(self._check_guides({"packages/us-federal/us-form-1040.md": federal}), [])

    def test_two_markers_are_an_error(self) -> None:
        errors = self._check_guides({"skills/twice.md": GOOD + "\n" + CTA_MARKER + "\n"})

        self.assertEqual(len(errors), 1, errors)
        self.assertIn("2 `<!-- openaccountants-cta-block -->` markers", errors[0])

    def test_a_prose_mention_is_not_a_section(self) -> None:
        mentioned = GOOD.replace("Body.\n", "Body. See the Talk to a verified accountant section below.\n")

        self.assertEqual(self._check_guides({"skills/prose.md": mentioned}), [])


if __name__ == "__main__":
    unittest.main()
