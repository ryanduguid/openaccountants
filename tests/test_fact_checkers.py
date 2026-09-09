import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"


class FactCheckerTests(unittest.TestCase):
    def run_checker(self, script, guides):
        with tempfile.TemporaryDirectory() as directory:
            for name, text in guides.items():
                path = Path(directory, "skills", "international", name)
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
