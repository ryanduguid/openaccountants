"""Executable cases must assert results and fail on malformed arithmetic."""

import importlib.util
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
from decimal import Decimal


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "check-examples.py"
SPEC = importlib.util.spec_from_file_location("check_examples", SCRIPT)
checker = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(checker)

CASE = """name: Croft Manor tile count
inputs:
  count: 12
steps:
  - tiles: count * 2
expected:
  tiles: 24
"""


def fenced(body=CASE):
    return "```oa-check\n" + body + "```\n"


class ExampleArithmeticTests(unittest.TestCase):
    def test_decimal_arithmetic_and_supported_functions(self):
        cases = {
            "0.1 + 0.2": "0.3",
            "100000000000000.01 - 100000000000000": "0.01",
            "-(3 + 2) * 4 / 2": "-10",
            "min(3, 2) + max(4, 5)": "7",
            "round(1.005, 2)": "1.01",
            "abs(-2) + floor(2.9) + ceil(1.1)": "6",
            "pct(200, 15)": "30",
            "clamp(12, 0, 10)": "10",
        }
        for expression, expected in cases.items():
            with self.subTest(expression=expression):
                self.assertEqual(checker.evaluate(expression, {}), Decimal(expected))

    def test_rejects_non_arithmetic_nodes_and_invalid_operations(self):
        for expression in ("__import__('os')", "value.real", "[1, 2]", "2 ** 4",
                           "True", "missing + 1", "1 / 0", "round(1, 1.5)",
                           "round(1, places=2)", "min()"):
            with self.subTest(expression=expression):
                with self.assertRaises(checker.CheckError):
                    checker.evaluate(expression, {})

    def test_steps_recompute_and_wrong_expected_values_fail(self):
        block = checker.parse_block(CASE)
        self.assertEqual(checker.run_block(block), [])
        block["expected"]["tiles"] = Decimal(25)
        self.assertEqual(len(checker.run_block(block)), 1)

    def test_expected_name_must_exist(self):
        with self.assertRaises(checker.CheckError):
            checker.run_block(checker.parse_block(CASE.replace("  tiles: 24", "  missing: 24")))
        with self.assertRaises(checker.CheckError):
            checker.run_block(checker.parse_block(CASE.replace("  tiles: 24", "  count: 12")))

    def test_tolerance_boundary(self):
        block = checker.parse_block(CASE.replace("  tiles: 24", "  tiles: 24.01"))
        self.assertEqual(checker.run_block(block), [])
        block["expected"]["tiles"] = Decimal("24.0101")
        self.assertEqual(len(checker.run_block(block)), 1)


class ExampleParsingTests(unittest.TestCase):
    def test_steps_without_expected_values_are_not_a_check(self):
        with self.assertRaises(checker.CheckError):
            checker.parse_block(CASE.split("expected:")[0])

    def test_requires_name_and_steps(self):
        for text in (CASE.replace("name: Croft Manor tile count\n", ""),
                     CASE.replace("steps:\n  - tiles: count * 2\n", "")):
            with self.subTest(text=text):
                with self.assertRaises(checker.CheckError):
                    checker.parse_block(text)

    def test_nonfinite_numbers_and_negative_tolerance_are_rejected(self):
        for value in ("Infinity", "-Infinity", "NaN", "sNaN"):
            for text in (CASE.replace("count: 12", "count: " + value),
                         CASE.replace("tiles: 24", "tiles: " + value),
                         CASE + "tolerance: " + value + "\n"):
                with self.subTest(value=value, text=text):
                    with self.assertRaises(checker.CheckError):
                        checker.parse_block(text)
        with self.assertRaises(checker.CheckError):
            checker.parse_block(CASE + "tolerance: -1\n")

    def test_duplicate_and_malformed_fields_are_rejected(self):
        invalid = (
            CASE.replace("  count: 12", "  count: 11\n  count: 12"),
            CASE.replace("  - tiles: count * 2", "  - count: 12\n  - tiles: count * 2"),
            CASE.replace("  tiles: 24", "  tiles: 25\n  tiles: 24"),
            CASE + "expected:\n  tiles: 24\n",
            CASE + "unknown: 0\n",
            CASE.replace("inputs:", "inputs: ignored"),
            CASE.replace("  count: 12", "  invalid-name: 12"),
            CASE.replace("  count: 12", "  count 12"),
            CASE.replace("  count: 12", "  count: 1,2"),
        )
        for text in invalid:
            with self.subTest(text=text):
                with self.assertRaises(checker.CheckError):
                    checker.parse_block(text)

    def test_correctly_grouped_numbers_are_supported(self):
        block = checker.parse_block(CASE.replace("count: 12", "count: 1,200")
                                    .replace("tiles: 24", "tiles: 2,400"))
        self.assertEqual(checker.run_block(block), [])

    def test_malformed_fences_cannot_silently_remove_a_case(self):
        for text in ("```oa-check\n" + CASE, "```oa-check extra\n" + CASE + "```\n",
                     " ```oa-check\n" + CASE + "```\n", fenced() + "```oa-check\n" + CASE):
            with self.subTest(text=text), tempfile.TemporaryDirectory() as directory:
                path = Path(directory) / "skills" / "case.md"
                path.parent.mkdir()
                path.write_text(text, encoding="utf-8")
                with patch.object(checker, "REPO_ROOT", directory):
                    self.assertTrue(checker.check_file(path)[1])


class ExampleCliTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.directory = Path(temporary.name)
        self.root = self.directory / "checkout"
        scripts = self.root / "scripts"
        shutil.copytree(ROOT / "scripts" / "oa_tools", scripts / "oa_tools",
                        ignore=shutil.ignore_patterns("__pycache__"))
        self.script = scripts / SCRIPT.name
        shutil.copyfile(SCRIPT, self.script)
        self.guide = self.root / "skills" / "international" / "australia" / "au-case.md"
        self.guide.parent.mkdir(parents=True)

    def invoke(self, *args, cwd=None):
        return subprocess.run([sys.executable, str(self.script), *map(str, args)],
                              cwd=cwd or self.root, capture_output=True, text=True,
                              encoding="utf-8", timeout=10)

    def run_checker(self, text, *args):
        self.guide.write_text(text, encoding="utf-8")
        return self.invoke(*args, self.guide)

    def assert_rejected(self, result):
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("FAIL", result.stdout)
        self.assertIn("0 oa-check blocks", result.stdout)
        self.assertNotIn("OUTSIDE_CONTENT", result.stdout + result.stderr)
        self.assertNotIn("Traceback", result.stderr)

    def symlink(self, link, target, *, directory=False):
        try:
            link.symlink_to(target, target_is_directory=directory)
        except (NotImplementedError, OSError) as exc:
            self.skipTest(f"symlinks unavailable: {exc}")

    def test_accepts_absolute_relative_and_contained_traversal_paths(self):
        self.guide.write_text(fenced() * 2, encoding="utf-8")
        for path, cwd in ((self.guide, self.root),
                          (self.guide.relative_to(self.root), self.root),
                          ("../australia/au-case.md", self.guide.parent)):
            with self.subTest(path=path):
                result = self.invoke("--require", path, cwd=cwd)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                self.assertIn("2 oa-check blocks", result.stdout)

    def test_rejects_external_absolute_relative_and_prefix_collision_paths(self):
        outside = self.directory / "outside.md"
        sibling = self.directory / "checkout-other" / "skills" / "outside.md"
        sibling.parent.mkdir(parents=True)
        for path in (outside, sibling):
            path.write_text(fenced(CASE + "OUTSIDE_CONTENT: 73\n"), encoding="utf-8")
        for path in (outside, "../outside.md", sibling):
            with self.subTest(path=path):
                self.assert_rejected(self.invoke(path))
                self.assert_rejected(self.invoke("--require", path))

    def test_rejects_non_guides_missing_files_and_directories(self):
        for name in ("README.md", "readme-draft.md", "case.txt"):
            path = self.guide.parent / name
            path.write_text(fenced() * 2, encoding="utf-8")
            with self.subTest(path=path):
                self.assert_rejected(self.invoke(path))
        directory = self.guide.parent / "directory.md"
        directory.mkdir()
        for path in (directory, self.guide, self.root / "skills"):
            with self.subTest(path=path):
                self.assert_rejected(self.invoke(path))

    def test_explicit_and_discovered_file_symlinks_cannot_escape(self):
        outside = self.directory / "outside.md"
        outside.write_text(fenced(CASE + "OUTSIDE_CONTENT: 73\n"), encoding="utf-8")
        self.symlink(self.guide, outside)
        self.assert_rejected(self.invoke(self.guide))
        self.assert_rejected(self.invoke())

    def test_directory_symlink_cannot_escape_but_contained_links_work(self):
        outside = self.directory / "outside"
        outside.mkdir()
        (outside / "case.md").write_text(fenced(CASE + "OUTSIDE_CONTENT: 73\n"), encoding="utf-8")
        escape = self.guide.parent / "escape"
        self.symlink(escape, outside, directory=True)
        self.assert_rejected(self.invoke(escape / "case.md"))
        self.guide.write_text(fenced() * 2, encoding="utf-8")
        alias = self.guide.parent / "alias.md"
        self.symlink(alias, self.guide)
        contained = self.root / "skills" / "alias"
        self.symlink(contained, self.guide.parent, directory=True)
        for path in (alias, contained / self.guide.name):
            with self.subTest(path=path):
                result = self.invoke("--require", path)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_symlink_aliases_cannot_disguise_readmes_or_non_markdown(self):
        for name in ("README.md", "case.txt"):
            target = self.guide.parent / name
            target.write_text(fenced() * 2, encoding="utf-8")
            alias = self.guide.parent / ("alias-" + name + ".md")
            self.symlink(alias, target)
            with self.subTest(target=target):
                self.assert_rejected(self.invoke(alias))

    def test_broken_and_looping_symlinks_are_failures(self):
        dangling = self.guide.parent / "dangling.md"
        looping = self.guide.parent / "loop.md"
        self.symlink(dangling, self.guide)
        self.symlink(looping, looping)
        for path in (dangling, looping):
            with self.subTest(path=path):
                self.assert_rejected(self.invoke(path))

    def test_symlinked_skills_root_cannot_expand_the_checkout_boundary(self):
        outside = self.directory / "outside"
        outside.mkdir()
        (outside / "case.md").write_text(fenced(CASE + "OUTSIDE_CONTENT: 73\n"), encoding="utf-8")
        (self.root / "skills").rename(self.root / "original-skills")
        self.symlink(self.root / "skills", outside, directory=True)
        self.assert_rejected(self.invoke(self.root / "skills" / "case.md"))
        self.assert_rejected(self.invoke())

    def test_require_checks_a_pair_without_a_slug_heuristic(self):
        for count in (0, 1, 2):
            with self.subTest(count=count):
                result = self.run_checker(fenced() * count, "--require")
                self.assertEqual(result.returncode, 0 if count == 2 else 1, result.stdout + result.stderr)

    def test_malformed_and_mismatched_cases_exit_nonzero(self):
        for text in (fenced(CASE.split("expected:")[0]), "```oa-check\n" + CASE,
                     fenced(CASE.replace("tiles: 24", "tiles: 25")),
                     fenced(CASE.replace("tiles: 24", "tiles: 25") + "tolerance: Infinity\n")):
            with self.subTest(text=text):
                result = self.run_checker(text)
                self.assertEqual(result.returncode, 1, result.stdout + result.stderr)

    def test_unmigrated_guide_without_blocks_does_not_claim_any_checks(self):
        result = self.run_checker("# Source guide without cases\n")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("0 oa-check blocks", result.stdout)

    def test_alternative_fences_cannot_escape_either_check_mode(self):
        bad_case = CASE.replace("tiles: 24", "tiles: 25")
        for opening, closing in (("````oa-check", "````"), ("~~~oa-check", "~~~"),
                                 ("~~~~oa-check", "~~~~"), ("``` oa-check", "```")):
            alternative = opening + "\n" + bad_case + closing + "\n"
            for prefix, args in (("", ()), (fenced() * 2, ("--require",))):
                with self.subTest(opening=opening, required=bool(args)):
                    result = self.run_checker(prefix + alternative, *args)
                    self.assertEqual(result.returncode, 1, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
