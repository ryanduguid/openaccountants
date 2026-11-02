"""Executable cases must assert results and fail on malformed arithmetic."""

import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
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
                path = Path(directory) / "case.md"
                path.write_text(text, encoding="utf-8")
                self.assertTrue(checker.check_file(path)[1])


class ExampleCliTests(unittest.TestCase):
    def run_checker(self, text, *args):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "au-case.md"
            path.write_text(text, encoding="utf-8")
            return subprocess.run([sys.executable, str(SCRIPT), *args, str(path)],
                                  capture_output=True, text=True, timeout=10)

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
