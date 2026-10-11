"""Country presence must not count global topics, states or unsigned drafts as review."""

import importlib.util
from contextlib import redirect_stdout
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))
spec = importlib.util.spec_from_file_location("country_coverage", SCRIPTS / "check-country-coverage.py")
country_coverage = importlib.util.module_from_spec(spec)
spec.loader.exec_module(country_coverage)


class CountryCoverageTests(unittest.TestCase):
    def setUp(self):
        self.catalogue = {
            "source_url": "https://example.invalid/countries",
            "retrieved_on": "2026-10-11",
            "countries": [{"code": "DE", "name": "Germany"}, {"code": "US", "name": "United States"}],
            "additional_jurisdictions": [{"code": "XK", "name": "Kosovo"}],
        }

    def test_state_and_global_guides_do_not_fill_a_missing_country(self):
        rows = country_coverage.coverage(self.catalogue, [
            {"jurisdiction": "US-DE"}, {"jurisdiction": "GLOBAL"}, {"jurisdiction": "INTL"}])
        self.assertEqual([row["guide_count"] for row in rows], [0, 0, 0])

    def test_one_country_is_counted_once_with_all_its_guides(self):
        rows = country_coverage.coverage(self.catalogue, [
            {"jurisdiction": "DE", "tier": 2, "reviewed_by": "Contributor, CPA"},
            {"jurisdiction": "DE", "tier": 1, "reviewed_by": "Reviewer, CPA"},
            {"jurisdiction": "DE", "tier": 1, "reviewed_by": "pending"},
            {"jurisdiction": "XK", "tier": 2}])
        self.assertEqual(len(rows), 3)
        self.assertEqual(rows[0]["guide_count"], 3)
        self.assertEqual(rows[0]["accountant_reviewed"], 1)
        self.assertEqual(rows[2]["guide_count"], 1)

    def test_duplicate_codes_cannot_inflate_the_denominator(self):
        self.catalogue["additional_jurisdictions"].append({"code": "DE", "name": "Duplicate"})
        with self.assertRaisesRegex(ValueError, "duplicate"):
            country_coverage.coverage(self.catalogue, [])

    def test_report_separates_inventory_from_verified_coverage(self):
        report = country_coverage.render(self.catalogue, country_coverage.coverage(self.catalogue, []))
        self.assertIn("0 of 3 target areas", report)
        self.assertIn("does not establish comprehensive topic coverage", report)
        self.assertIn("| XK | Kosovo | 0 | 0 |", report)
        self.assertTrue(report.endswith("\n"))

    def test_cli_markdown_is_read_only_and_report_check_detects_drift(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            catalogue = root / "catalogue.json"
            saved_report = root / "coverage.md"
            catalogue.write_text(json.dumps(self.catalogue), encoding="utf-8")
            (root / "index.json").write_text('{"guides": []}', encoding="utf-8")
            with patch.object(country_coverage, "ROOT", root), \
                 patch.object(country_coverage, "CATALOGUE", catalogue), \
                 patch.object(country_coverage, "REPORT", saved_report):
                output = io.StringIO()
                with redirect_stdout(output):
                    self.assertEqual(country_coverage.main(["--markdown"]), 0)
                self.assertFalse(saved_report.exists())
                self.assertIn("| DE | Germany | 0 | 0 |", output.getvalue())
                saved_report.write_text(output.getvalue(), encoding="utf-8")
                with redirect_stdout(io.StringIO()):
                    self.assertEqual(country_coverage.main(["--check-report"]), 0)
                    (root / "index.json").write_text(
                        '{"guides": [{"jurisdiction": "DE", "tier": 2}]}', encoding="utf-8")
                    self.assertEqual(country_coverage.main(["--check-report"]), 1)


if __name__ == "__main__":
    unittest.main()
