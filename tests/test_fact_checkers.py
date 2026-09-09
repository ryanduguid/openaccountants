import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"


class FactCheckerTests(unittest.TestCase):
    def run_checker(self, script, guides, root="international"):
        with tempfile.TemporaryDirectory() as directory:
            Path(directory, "docs").mkdir()
            for name, text in guides.items():
                path = Path(directory, "skills", root, name)
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(text, encoding="utf-8")
            result = subprocess.run(
                [sys.executable, "-X", "utf8", str(SCRIPTS / script)],
                cwd=directory, capture_output=True, text=True, encoding="utf-8",
                timeout=30,
            )
        self.assertEqual(result.returncode, 0, result.stderr)
        return result.stdout

    def test_percentage_conflicts_include_tables_and_bullets(self):
        output = self.run_checker("check-fact-conflicts.py", {
            "example/overview.md": "- **Standard VAT rate** - 20%\n",
            "example/vat.md": "| Standard VAT rate | 25% |\n",
            "other/overview.md": "| Standard VAT rate | 30% |\n",
        })
        self.assertIn("labelled percentage facts extracted: 3", output)
        self.assertIn("keys where files disagree: 1", output)
        self.assertIn('int:example :: "standard vat"', output)

    def test_corporate_conflicts_group_by_country(self):
        output = self.run_checker("check-headline-cit.py", {
            "example/overview.md": "- **Standard corporate tax rate** - 20%\n",
            "example/cit.md": "- **Standard corporate tax rate** - 25%\n",
            "other/overview.md": "- **Standard corporate tax rate** - 30%\n",
        })
        self.assertIn("unqualified standard CIT rate: 2", output)
        self.assertRegex(output, r"CONFLICT\s+example\s+20, 25")
        self.assertNotRegex(output, r"CONFLICT\s+other\b")

    def test_form_register_groups_federal_guides(self):
        output = self.run_checker("build-form-register.py", {
            "issuance.md": "File Form 1099-NEC.\n",
            "payments.md": "Use Form 1099-NEC.\n",
        }, root="federal")
        self.assertIn("1 jurisdictions, 1 shared form identifiers", output)

    def test_registration_list_excludes_direct_taxes(self):
        output = self.run_checker("list-registration-thresholds.py", {
            "or/or-cat.md": "| CAT registration threshold | USD 750,000 |\n",
            "py/paraguay-payroll.md": "| IRP registration threshold | PYG 80,000,000 |\n",
            "cn/china-vat.md": "| Registration threshold | CNY 500,000 |\n",
        })
        self.assertNotIn("USD 750,000", output)
        self.assertNotIn("PYG 80,000,000", output)
        self.assertIn("CNY 500,000", output)

    def test_withholding_table_context_and_shared_rate(self):
        output = self.run_checker("list-withholding-rates.py", {
            "ng/wht.md": "## Withholding tax\n\n| Payment type | Rate |\n"
                          "| --- | --- |\n| Dividends | 10% |\n| Interest | 10% |\n"
                          "## Corporate income tax\n\n| Royalties | 30% |\n",
            "bs/overview.md": "- **WHT on dividends, interest and royalties** - 0%\n",
        })
        self.assertRegex(output, r"ng\s+dividends/unspecified\s+10%")
        self.assertRegex(output, r"ng\s+interest/unspecified\s+10%")
        self.assertNotRegex(output, r"ng\s+royalties")
        for kind in ("dividends", "interest", "royalties"):
            self.assertRegex(output, rf"bs\s+{kind}/unspecified\s+0%")
