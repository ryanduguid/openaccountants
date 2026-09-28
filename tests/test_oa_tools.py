"""Tests for scripts/oa_tools/, the helpers every script shares.

The package replaced three copies of the frontmatter block scanner
(build-index.py, build-packages.py, normalize-cta-block.py), two ad-hoc
splitters in the review aids, the strict loader module they all imported, and
the importlib shims that loaded build-index.py by path to reach its parser.
Copies drift: the scanner in build-packages.py had already grown its own
regex. These tests pin the reader's rules and that the scripts bind the shared
functions rather than a copy.
"""

from __future__ import annotations

import datetime
import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = REPO_ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from oa_tools import frontmatter, guides, paths  # noqa: E402


def _load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / filename)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


build_index = _load("build_index_for_oa_tools_tests", "build-index.py")
build_packages = _load("build_packages_for_oa_tools_tests", "build-packages.py")
validate_guides = _load("validate_guides_for_oa_tools_tests", "validate-guides.py")
normalize_cta = _load("normalize_cta_for_oa_tools_tests", "normalize-cta-block.py")
detect_contradictions = _load("detect_contradictions_for_oa_tools_tests", "detect-contradictions.py")

GUIDE = (
    "---\n"
    "name: synthetic\n"
    "jurisdiction: MT\n"
    "tier: 2\n"
    "last_updated: 2026-01-02\n"
    "---\n"
    "\n"
    "# Body\n"
)
BLOCK = "name: synthetic\njurisdiction: MT\ntier: 2\nlast_updated: 2026-01-02\n"


def _tree(case: unittest.TestCase, files: dict[str, str]) -> Path:
    tmp = tempfile.TemporaryDirectory()
    case.addCleanup(tmp.cleanup)
    root = Path(tmp.name)
    for rel, text in files.items():
        path = root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    return root


class ExtractFrontmatterTests(unittest.TestCase):
    def test_block_is_the_lines_between_the_delimiters(self) -> None:
        self.assertEqual(frontmatter.extract_frontmatter(GUIDE), BLOCK)

    def test_docs_horizontal_rules_and_unclosed_blocks_are_not_frontmatter(self) -> None:
        for text in (
            "",
            "# Notes\n\n---\n\nprose\n",        # a rule, not an opener
            "--- not a delimiter\nname: x\n---\n",
            "---\nname: x\n",                   # never closed
            " ---\nname: x\n---\n",             # not at byte 0
        ):
            self.assertIsNone(frontmatter.extract_frontmatter(text), repr(text))

    def test_document_end_marker_closes_the_block(self) -> None:
        self.assertEqual(frontmatter.extract_frontmatter("---\nname: x\n...\nbody\n"), "name: x\n")

    def test_trailing_whitespace_or_a_stray_cr_on_the_closer_still_closes(self) -> None:
        self.assertEqual(frontmatter.extract_frontmatter("---\nname: x\n--- \nbody\n"), "name: x\n")
        self.assertEqual(frontmatter.extract_frontmatter("---\nname: x\n---\r\nbody\n"), "name: x\n")

    def test_closer_with_other_text_on_the_line_does_not_close(self) -> None:
        self.assertIsNone(frontmatter.extract_frontmatter("---\nname: x\n---- \nbody\n"))


class SplitFrontmatterTests(unittest.TestCase):
    def test_delimiters_stay_with_the_frontmatter_and_the_parts_reassemble(self) -> None:
        fm, body = frontmatter.split_frontmatter(GUIDE)
        self.assertEqual(fm, "---\n" + BLOCK + "---\n")
        self.assertEqual(body, "\n# Body\n")
        self.assertEqual(fm + body, GUIDE)

    def test_no_frontmatter_means_everything_is_body(self) -> None:
        self.assertEqual(frontmatter.split_frontmatter("# Notes\n"), (None, "# Notes\n"))
        self.assertEqual(frontmatter.split_frontmatter("---\nnever closed\n"), (None, "---\nnever closed\n"))

    def test_blank_lines_after_the_closer_belong_to_the_body(self) -> None:
        fm, body = frontmatter.split_frontmatter("---\nname: x\n---\n\n\nbody\n")
        self.assertEqual(fm, "---\nname: x\n---\n")
        self.assertEqual(body, "\n\nbody\n")

    def test_closer_at_end_of_file_without_a_newline(self) -> None:
        self.assertEqual(frontmatter.split_frontmatter("---\nname: x\n---"), ("---\nname: x\n---", ""))


class TolerantReaderTests(unittest.TestCase):
    def test_every_known_key_is_present_and_defaults_to_none(self) -> None:
        fields = frontmatter.parse_known_keys("name: x\n")
        self.assertEqual(list(fields), frontmatter.KNOWN_KEYS)
        self.assertEqual(fields["name"], "x")
        self.assertIsNone(fields["tier"])

    def test_quotes_comments_null_and_block_scalars(self) -> None:
        block = (
            'name: "quoted"  \n'
            "jurisdiction: MT # trailing comment\n"
            "description: >\n"
            "  folded text\n"
            "tier: 2\n"
            "reviewed_by: ~\n"
            "verified_by: null\n"
        )
        fields = frontmatter.parse_known_keys(block)
        self.assertEqual(fields["name"], "quoted")
        self.assertEqual(fields["jurisdiction"], "MT")
        self.assertEqual(fields["tier"], "2")
        self.assertIsNone(fields["reviewed_by"])
        self.assertIsNone(fields["verified_by"])

    def test_first_occurrence_wins_and_malformed_lines_are_skipped(self) -> None:
        fields = frontmatter.parse_known_keys(
            "tier: 1\nqualifier: bad: colon soup\ntier: 2\n  jurisdiction: indented\n"
        )
        self.assertEqual(fields["tier"], "1")
        self.assertIsNone(fields["jurisdiction"])

    def test_custom_key_list(self) -> None:
        self.assertEqual(
            frontmatter.parse_known_keys("version: 1.2\nname: x\n", keys=["version"]),
            {"version": "1.2"},
        )


class ReadFrontmatterTests(unittest.TestCase):
    """The one entry point: tolerant by default, strict on request."""

    def test_no_frontmatter_is_none_either_way(self) -> None:
        self.assertIsNone(frontmatter.read_frontmatter("# doc\n"))
        self.assertIsNone(frontmatter.read_frontmatter("# doc\n", strict=True))

    def test_tolerant_returns_the_known_keys(self) -> None:
        fields = frontmatter.read_frontmatter(GUIDE)
        self.assertEqual(fields["name"], "synthetic")
        self.assertEqual(fields["tier"], "2")

    def test_strict_returns_the_typed_mapping(self) -> None:
        metadata = frontmatter.read_frontmatter(GUIDE, strict=True)
        self.assertEqual(metadata["name"], "synthetic")
        self.assertEqual(metadata["tier"], 2)
        self.assertEqual(metadata["last_updated"], datetime.date(2026, 1, 2))

    def test_strict_rejects_what_tolerant_shrugs_at(self) -> None:
        duplicated = "---\nname: x\nname: y\n---\n"
        self.assertEqual(frontmatter.read_frontmatter(duplicated)["name"], "x")
        with self.assertRaisesRegex(frontmatter.FrontmatterError, "duplicate key"):
            frontmatter.read_frontmatter(duplicated, strict=True)

    def test_tolerant_path_never_imports_pyyaml(self) -> None:
        """build-index.py is documented as stdlib-only; the strict loader is
        what needs PyYAML, and only when it runs."""
        code = (
            "import sys; sys.path.insert(0, 'scripts')\n"
            "from oa_tools import frontmatter, guides\n"
            "frontmatter.read_frontmatter('---\\nname: x\\n---\\n')\n"
            "assert 'yaml' not in sys.modules, 'tolerant reader imported PyYAML'\n"
        )
        result = subprocess.run(
            [sys.executable, "-c", code], cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        self.assertEqual(result.returncode, 0, result.stderr)


class GuideDiscoveryTests(unittest.TestCase):
    def test_walks_only_the_guide_trees_skips_readmes_and_sorts(self) -> None:
        root = _tree(self, {
            "skills/a/README.md": "# readme",
            "skills/a/readme.md": "# readme",
            "skills/a/z-guide.md": GUIDE,
            "skills/a/a-guide.md": GUIDE,
            "skills/a/notes.txt": "not markdown",
            "packages/us-federal/rates.2026.json": "{}",   # hand-authored data, not a guide tree
            "packages/malta/mt-vat.md": GUIDE,   # generated: not a guide tree
            "packages/_shared/base.md": GUIDE,   # generated: not a guide tree
            "docs/page.md": GUIDE,
        })
        self.assertEqual(
            guides.guide_files(str(root)),
            ["skills/a/a-guide.md", "skills/a/z-guide.md"],
        )

    def test_a_missing_tree_is_skipped(self) -> None:
        root = _tree(self, {"skills/a/guide.md": GUIDE})
        self.assertEqual(guides.guide_files(str(root)), ["skills/a/guide.md"])
        self.assertEqual(guides.guide_files(str(root), trees=("nowhere",)), [])

    def test_paths_are_posix_and_root_relative(self) -> None:
        root = _tree(self, {"skills/deep/er/guide.md": GUIDE})
        self.assertEqual(guides.guide_files(str(root)), ["skills/deep/er/guide.md"])

    def test_read_text_replaces_undecodable_bytes(self) -> None:
        root = _tree(self, {})
        (root / "guide.md").write_bytes(b"---\nname: x\n---\n\xff\n")
        self.assertEqual(guides.read_text("guide.md", str(root)), "---\nname: x\n---\n�\n")

    def test_defaults_point_at_this_repository(self) -> None:
        self.assertEqual(paths.REPO_ROOT, str(REPO_ROOT))
        self.assertEqual(paths.repo_root(), str(REPO_ROOT))
        self.assertEqual(paths.GUIDE_TREES, ("skills",))
        self.assertEqual(paths.SKILLS_DIR, str(REPO_ROOT / "skills"))
        self.assertEqual(paths.PACKAGES_DIR, str(REPO_ROOT / "packages"))
        self.assertEqual(paths.HAND_AUTHORED_PACKAGES, frozenset({"us-federal"}))
        self.assertEqual(paths.rel(str(REPO_ROOT / "skills" / "x.md")), "skills/x.md")


class ScriptsShareTheHelpersTests(unittest.TestCase):
    """Copies were the bug: each one drifted. The scripts must bind the shared
    objects, and no script may keep a private block scanner."""

    def test_build_index_re_exports_the_reader_and_walks_its_own_root(self) -> None:
        self.assertIs(build_index.extract_frontmatter, frontmatter.extract_frontmatter)
        self.assertIs(build_index.parse_known_keys, frontmatter.parse_known_keys)
        self.assertEqual(build_index.GUIDE_TREES, list(paths.GUIDE_TREES))
        root = _tree(self, {"skills/a/guide.md": GUIDE, "skills/a/README.md": "# r"})
        with mock.patch.object(build_index, "REPO_ROOT", str(root)):
            self.assertEqual(build_index.guide_files(), ["skills/a/guide.md"])
            self.assertEqual(build_index.build_index()["counts"]["guides"], 1)

    def test_build_packages_uses_the_shared_reader_and_hand_authored_list(self) -> None:
        self.assertIs(build_packages.extract_frontmatter, frontmatter.extract_frontmatter)
        self.assertIs(build_packages.load_frontmatter, frontmatter.load_frontmatter)
        self.assertIs(build_packages.HAND_AUTHORED_PACKAGES, paths.HAND_AUTHORED_PACKAGES)
        self.assertFalse(hasattr(build_packages, "_frontmatter_block"))

    def test_validator_reads_guides_through_the_package(self) -> None:
        bi = validate_guides.GuideTrees()
        self.assertIs(bi.extract_frontmatter, frontmatter.extract_frontmatter)
        self.assertIs(bi.parse_known_keys, frontmatter.parse_known_keys)
        root = _tree(self, {"skills/a/guide.md": GUIDE, "packages/malta/mt.md": GUIDE})
        with mock.patch.object(validate_guides, "REPO_ROOT", str(root)):
            self.assertEqual(bi.guide_files(), ["skills/a/guide.md"])
        for shim in ("load_build_index", "load_build_packages"):
            self.assertFalse(hasattr(validate_guides, shim), shim)

    def test_normalizer_and_contradiction_scanner_bind_the_shared_functions(self) -> None:
        self.assertIs(normalize_cta.split_frontmatter, frontmatter.split_frontmatter)
        self.assertIs(detect_contradictions.extract_frontmatter, frontmatter.extract_frontmatter)
        self.assertIs(detect_contradictions.parse_known_keys, frontmatter.parse_known_keys)

    def test_no_script_keeps_a_private_block_scanner_or_the_old_module(self) -> None:
        old_module = "frontmatter" + "_yaml"   # split so this file does not match itself
        offenders = []
        for path in sorted([*SCRIPTS.glob("*.py"), *(REPO_ROOT / "tests").glob("*.py")]):
            text = path.read_text(encoding="utf-8")
            if old_module in text:
                offenders.append(f"{path.name}: imports the removed {old_module} module")
            if path.parent == SCRIPTS and "first_nl" in text:
                offenders.append(f"{path.name}: carries a copy of the block scanner")
        self.assertEqual(offenders, [])

    def test_a_test_module_imports_on_its_own(self) -> None:
        """Regression: run alone, tests.test_validate_quality_metadata failed
        with ModuleNotFoundError because validate-guides.py relied on a sibling
        test having put scripts/ on sys.path first. Every script that imports
        oa_tools now puts its own directory there."""
        result = subprocess.run(
            [sys.executable, "-m", "unittest", "tests.test_validate_quality_metadata"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=120,
        )
        self.assertEqual(result.returncode, 0, result.stderr)


class BuildIndexCliTests(unittest.TestCase):
    def test_out_without_a_path_is_an_error_not_a_traceback(self) -> None:
        for argv in (["--out"], ["--out", "--other"]):
            result = subprocess.run(
                [sys.executable, str(SCRIPTS / "build-index.py"), *argv],
                cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
            )
            self.assertNotEqual(result.returncode, 0, argv)
            self.assertIn("--out requires a file path", result.stderr, argv)
            self.assertNotIn("Traceback", result.stderr, argv)

    def test_refuses_to_write_an_empty_index(self) -> None:
        root = _tree(self, {"skills/a/README.md": "# only docs"})
        out = root / "index.json"
        with mock.patch.object(build_index, "REPO_ROOT", str(root)), \
                mock.patch.object(sys, "argv", ["build-index.py", "--out", str(out)]):
            with self.assertRaises(SystemExit) as caught:
                build_index.main()
        self.assertIn("no guides found", str(caught.exception))
        self.assertFalse(out.exists())


if __name__ == "__main__":
    unittest.main()
