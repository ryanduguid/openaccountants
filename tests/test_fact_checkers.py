import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"


class FactCheckerTests(unittest.TestCase):
    def run_checker(self, script, guides, expect_code=0):
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
        self.assertEqual(result.returncode, expect_code, result.stderr)
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

    def test_withholding_scope_queues_classic_only_jurisdictions(self):
        # "thin" states the three classic heads and nothing else, which is the
        # shape North Macedonia had while its statute charged eight heads.
        # "broad" names a service and a rent head as well, so it is not queued.
        output = self.run_checker("list-withholding-scope.py", {
            "thin/cit.md": (
                "- **Withholding tax on dividends** - 10%\n"
                "- **Withholding tax on interest** - 10%\n"
                "- **Withholding tax on royalties** - 10%\n"
            ),
            "broad/cit.md": (
                "- **Withholding tax on dividends** - 10%\n"
                "- **Withholding tax on management and professional fees** - 20%\n"
                "- **Withholding tax on rent paid to non-residents** - 30%\n"
            ),
        }, expect_code=1)
        self.assertIn("naming only classic heads: 1", output)
        self.assertIn("nothing else anywhere (the queue): 1", output)
        self.assertRegex(output, r"queue:\s+thin\b")
        self.assertNotRegex(output, r"queue:\s+broad\b")
        self.assertRegex(output, r"\bbroad\s+dividends, rent, services")

    def test_withholding_scope_excludes_zero_rate_jurisdictions(self):
        # "nowht" charges nothing, so it names no service or rent head because
        # there is nothing to name. That is a complete guide, not a thin one,
        # and it must not sit in the same queue as "thin", which charges 10%
        # on royalties and says nothing about anything else.
        output = self.run_checker("list-withholding-scope.py", {
            "nowht/cit.md": (
                "- **Withholding tax on dividends** - 0% (no withholding tax "
                "on dividends)\n"
                "- **Withholding tax on interest and royalties** - None\n"
            ),
            "thin/cit.md": (
                "- **Withholding tax on dividends** - 0%\n"
                "- **Withholding tax on royalties** - 10%\n"
            ),
        }, expect_code=1)
        self.assertIn("withholding nothing at all (complete, not thin): 1", output)
        self.assertRegex(output, r"zero-wht:\s+nowht\b")
        self.assertIn("nothing else anywhere (the queue): 1", output)
        self.assertRegex(output, r"queue:\s+thin\b")
        self.assertNotRegex(output, r"queue:\s+nowht\b")

    def test_withholding_scope_separates_body_mentions_from_bare_entries(self):
        # "bare" names only the classic three and nothing else anywhere.
        # "mentions" also names only classic heads in its labels, but a bullet
        # body names a service head, so it is cheaper to triage than research
        # and is counted separately rather than sitting in the same queue.
        output = self.run_checker("list-withholding-scope.py", {
            "bare/cit.md": (
                "- **Withholding tax on dividends** - 10%\n"
                "- **Withholding tax on royalties** - 10%\n"
            ),
            "mentions/cit.md": (
                "- **Withholding tax on dividends** - 10%\n"
                "- **Withholding tax on royalties** - 10%, and management "
                "service fees are dealt with separately\n"
            ),
        }, expect_code=1)
        self.assertIn("naming only classic heads: 2", output)
        self.assertIn("nothing else anywhere (the queue): 1", output)
        self.assertIn("bullet body (triage first): 1", output)
        self.assertRegex(output, r"queue:\s+bare\b")
        self.assertRegex(output, r"triage:\s+mentions\s+body mentions services")

    def test_withholding_scope_ignores_prose_and_cross_references(self):
        # Prose naming every head is not a charge, and a withholding label that
        # commits to no rate is a pointer to another section.
        output = self.run_checker("list-withholding-scope.py", {
            "broad/cit.md": (
                "Withholding taxes apply to dividends, interest and royalties.\n"
                "- **Withholding tax on services** - see the section below\n"
                "- **Withholding tax on dividends** - 10%\n"
                "- **Withholding tax on insurance premiums** - 4%\n"
            ),
        })
        self.assertIn("naming only classic heads: 0", output)
        # only the two labelled bullets that commit to a rate are counted, so
        # the interest and royalties named in the prose do not appear
        self.assertRegex(output, r"\bbroad\s+dividends, insurance\b")
        self.assertIn("heads named per jurisdiction: 2:1", output)
