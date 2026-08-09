"""Regression tests for spreadsheet formula neutralisation."""

from __future__ import annotations

import unittest
from decimal import Decimal

from scripts.excel_safety import FORMULA_PREFIXES, excel_safe, safe_filename_component


class ExcelSafetyTests(unittest.TestCase):
    def test_every_formula_prefix_is_forced_to_text(self):
        for prefix in FORMULA_PREFIXES:
            value = prefix + "cmd|' /C calc'!A0"
            with self.subTest(prefix=repr(prefix)):
                self.assertEqual(excel_safe(value), "'" + value)

    def test_safe_text_and_native_numeric_values_are_preserved(self):
        for value in ("ordinary text", "'already text", 42, Decimal("1.25"), None):
            with self.subTest(value=value):
                self.assertIs(excel_safe(value), value)

    def test_workbook_filename_component_cannot_escape_output_directory(self):
        for value in ("US-FL", "MT", "ca_on", "tax.2026"):
            with self.subTest(value=value):
                self.assertEqual(safe_filename_component(value), value)

        for value in ("../escape", "US/FL", r"C:\\escape", "", ".", " space"):
            with self.subTest(value=value), self.assertRaisesRegex(
                ValueError, r"filename component"
            ):
                safe_filename_component(value)


if __name__ == "__main__":
    unittest.main()
