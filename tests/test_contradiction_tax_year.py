"""Tests for contradiction-scanner tax-year selection and binding."""

from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "detect-contradictions.py"
SPEC = importlib.util.spec_from_file_location("detect_contradictions", SCRIPT)
scanner = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(scanner)


class ContradictionTaxYearTests(unittest.TestCase):
    def test_selects_newest_valid_rate_year(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "rates.2025.json").write_text(
                json.dumps({"tax_year": 2025}), encoding="utf-8"
            )
            (root / "rates.2026.json").write_text(
                json.dumps({"tax_year": 2026}), encoding="utf-8"
            )
            (root / "rates.latest.json").write_text("not json", encoding="utf-8")

            self.assertEqual(scanner.resolve_tax_year(rates_dir=directory), 2026)
            self.assertEqual(scanner.available_rate_years(directory), [2025, 2026])

    def test_explicit_year_overrides_rate_files(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            self.assertEqual(scanner.resolve_tax_year(2042, directory), 2042)
            with self.assertRaisesRegex(ValueError, "positive four-digit"):
                scanner.resolve_tax_year(999, directory)

    def test_missing_rate_directory_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(ValueError, "no valid rates"):
                scanner.resolve_tax_year(rates_dir=directory)

    def test_malformed_or_mismatched_canonical_rate_file_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "rates.2025.json").write_text(
                json.dumps({"tax_year": 2025}), encoding="utf-8"
            )
            (root / "rates.2026.json").write_text("not json", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, r"invalid JSON.*rates\.2026\.json"):
                scanner.resolve_tax_year(rates_dir=directory)

            (root / "rates.2026.json").write_text(
                json.dumps({"tax_year": 2025}), encoding="utf-8"
            )
            with self.assertRaisesRegex(ValueError, r"rates\.2026\.json.*tax_year 2026"):
                scanner.resolve_tax_year(rates_dir=directory)

    def test_frontmatter_year_wins_and_missing_year_uses_default(self) -> None:
        compiled = scanner.compile_concepts()
        stats = {
            "claims": 0,
            "multivalue_lines_skipped": 0,
            "ambiguous_year_dropped": 0,
            "historical_dropped": 0,
        }

        def claim(frontmatter_year: str) -> dict:
            text = (
                "---\nname: test\njurisdiction: DE\ncategory: international\n"
                f"{frontmatter_year}---\n\n# Rules\nThe Grundfreibetrag is EUR 12,000.\n"
            )
            return scanner.extract_claims(
                "synthetic.md", text, "DE", compiled, stats, 2026
            )[0]

        self.assertEqual(claim("")["year"], 2026)
        self.assertEqual(claim("tax_year: 2025\n")["year"], 2025)


if __name__ == "__main__":
    unittest.main()
