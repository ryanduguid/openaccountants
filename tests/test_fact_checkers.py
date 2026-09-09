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

    def test_solo_citations_rank_uncorroborated_instruments(self):
        # "lonely" leans on one instrument nobody else cites; "shared" cites an
        # instrument that appears in a second guide, so it is corroborated
        # inside the corpus and is not ranked however often it appears.
        lonely = "Regulated by Portaria n.º 999/2024/1. " * 9
        shared = "Under Lei n.º 82/2023 the regime applies. " * 9
        output = self.run_checker("list-solo-citations.py", {
            "lonely/guide.md": lonely,
            "shared/guide.md": shared,
            "other/guide.md": "See also Lei n.º 82/2023 for the enabling provision.\n",
        })
        self.assertRegex(output, r"9x\s+Portaria 999/2024/1")
        self.assertNotRegex(output, r"Lei 82/2023")
        self.assertIn("cited 8+ times in exactly one guide", output)
        # it ranks, it does not accuse
        self.assertIn("blast-radius ranking, not a defect report", output)

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

    def run_in_git(self, script, before, after, args=()):
        """Commit `before`, apply `after`, and run `script` against the commit.

        The incomplete-fix checker reads a diff rather than the tree, so it
        needs a real repository with a base commit to diff against. Everything
        else in this file can work from a bare temp directory.
        """
        with tempfile.TemporaryDirectory() as directory:
            def git(*argv):
                subprocess.run(["git"] + list(argv), cwd=directory, check=True,
                               capture_output=True, text=True)
            git("init", "-q", "-b", "work")
            git("config", "user.email", "t@example.invalid")
            git("config", "user.name", "T")
            for name, text in before.items():
                path = Path(directory, "skills", "international", name)
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(text, encoding="utf-8")
            git("add", "-A")
            git("commit", "-q", "-m", "base")
            # tag it: a branch name would move with the second commit and
            # `base...HEAD` would then be empty
            git("tag", "base")
            for name, text in after.items():
                Path(directory, "skills", "international", name).write_text(
                    text, encoding="utf-8")
            git("add", "-A")
            git("commit", "-q", "-m", "edit")
            result = subprocess.run(
                [sys.executable, "-X", "utf8", str(SCRIPTS / script),
                 "--base", "base"] + list(args),
                cwd=directory, capture_output=True, text=True, encoding="utf-8",
                timeout=30,
            )
        self.assertEqual(result.returncode, 0, result.stderr)
        return result.stdout

    def test_incomplete_fixes_selftest_passes(self):
        result = subprocess.run(
            [sys.executable, "-X", "utf8",
             str(SCRIPTS / "list-incomplete-fixes.py"), "--selftest"],
            capture_output=True, text=True, encoding="utf-8", timeout=30,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("known misses pass", result.stdout)

    def test_incomplete_fixes_reports_surviving_copies_of_a_removed_value(self):
        # The Pakistan shape: a table row is corrected from 45% to 35% while
        # three satellites elsewhere in the same file still say 45%. Two of
        # those satellites are untouched, so both must be reported with their
        # line numbers; the corrected row itself must not be.
        before = {"pk/tax.md": (
            "# Rates\n"
            "The top slab reaches 45% for the year.\n"
            "| top rate | 45% |\n"
            "Non-filers are charged at up to 45% under the same table.\n"
        )}
        after = {"pk/tax.md": (
            "# Rates\n"
            "The top slab reaches 45% for the year.\n"
            "| top rate | 35% |\n"
            "Non-filers are charged at up to 45% under the same table.\n"
        )}
        output = self.run_in_git("list-incomplete-fixes.py", before, after)
        self.assertIn("skills/international/pk/tax.md", output)
        self.assertRegex(output, r"\s+2\s+45%\s+The top slab reaches")
        self.assertRegex(output, r"\s+4\s+45%\s+Non-filers are charged")
        self.assertIn("still stands elsewhere: 1", output)
        # it ranks, it does not accuse
        self.assertIn("Read each surviving line before touching it", output)

    def test_incomplete_fixes_does_not_match_a_value_inside_a_longer_one(self):
        # Fiji: a removed "0%" matched inside "10%" two lines down and put a
        # correct guide on the worklist. Values match on token boundaries.
        before = {"fj/wht.md": (
            "- **Dividends** - 0% (position uncertain)\n"
            "- **Interest** - 10%\n"
            "- **Royalties** - 15%\n"
        )}
        after = {"fj/wht.md": (
            "- **Dividends** - 9% (confirmed with FRCS)\n"
            "- **Interest** - 10%\n"
            "- **Royalties** - 15%\n"
        )}
        output = self.run_in_git("list-incomplete-fixes.py", before, after)
        self.assertIn("still stands elsewhere: 0", output)
        self.assertNotIn("fj/wht.md\n", output)

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
