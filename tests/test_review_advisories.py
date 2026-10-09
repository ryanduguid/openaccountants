"""Review aids find known issues from any working directory."""

import os
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
CASES = {
    "check-amount-conflicts.py": ((), 0, "state differently: 1"),
    "check-currency-of-account.py": ((), 0, "outliers: 1"),
    "check-effective-dates.py": ((), 0, "rates a jurisdiction dates two different ways: 1"),
    "check-filing-deadlines.py": ((), 0, "different calendar deadlines: 1"),
    "check-quick-formula.py": ((), 0, "quick-formula tables checked: 1 ; broken boundaries: 2"),
    "check-research-gap-conflicts.py": ((), 0, "stated in a sibling: 1"),
    "check-stale-futures.py": (("--today", "2026-10-07"), 0, "date now past: 1"),
    "check-statute-citations.py": ((), 0, "different provisions: 1"),
    "check-tax-authority.py": ((), 0, "outliers: 1"),
    "list-solo-citations.py": ((), 0, "cited 8+ times in exactly one guide (verify these first): 1"),
    "list-source-mix.py": ((), 0, "jurisdictions with any external citation: 1"),
    "list-withholding-scope.py": ((), 1, "jurisdictions naming a withholding head: 1"),
}
FIRST = (
    "---\ntax_year: 2020\n---\n"
    "- **VAT registration threshold** - EUR 12,345\n"
    "[RESEARCH GAP -- reviewer to confirm] The allowance is 12,345.\n"
    "From 1 January 2020 the rate is 10%.\n"
    "Form X123 is due 31 March.\n"
    "TA24 applies under Article 4.\n"
    "A change is proposed from 2025.\n"
    "- **Withholding tax on dividends** - 10%\n"
    "https://taxsummaries.pwc.com/example\n"
    "| Taxable income | Rate | Deduction |\n| --- | --- | --- |\n"
    "| 0 - 100 | 10% | 0 |\n| 101 - 200 | 20% | 20 |\n"
    "| 201 - 300 | 30% | 30 |\n"
) + "ATO EUR 5000\n" * 10 + "Notice 2026-12\n" * 8
SECOND = (
    "- **VAT registration threshold** - EUR 23,456\n"
    "The allowance is 12,345.\n"
    "From 1 February 2020 the rate is 10%.\n"
    "Form X123 is due 30 April.\n"
    "TA24 applies under Article 5.\n"
) + "ATO EUR 5000\n" * 10
THIRD = "IRS GBP 5000\n" * 5

CITATION_LOADER = (
    "import importlib.util, sys\n"
    "spec = importlib.util.spec_from_file_location('rot', sys.argv[1])\n"
    "rot = importlib.util.module_from_spec(spec)\n"
    "spec.loader.exec_module(rot)\n"
)
OFFLINE_CITATION_DRIVER = CITATION_LOADER + (
    "rot.fetch = lambda *a, **kw: (200, 'Buy this domain today.')\n"
    "rot.get = lambda *a, **kw: (200, 'Buy this domain today.')\n"
    "sys.exit(rot.main(sys.argv[2:]))\n"
)
NO_REVIEW_DRIVER = CITATION_LOADER + (
    "def unexpected(*args, **kwargs):\n"
    "    raise AssertionError('unexpected review work')\n"
    "rot.fetch = rot.get = rot.cited_hosts = unexpected\n"
    "rot.grade = rot.collect_hosts = unexpected\n"
    "sys.exit(rot.main(sys.argv[2:]))\n"
)
NETWORK_BLOCKED_ENTRY_DRIVER = (
    "import runpy, socket, sys, urllib.request\n"
    "def unexpected(*args, **kwargs):\n"
    "    raise AssertionError('unexpected network call')\n"
    "socket.getaddrinfo = urllib.request.urlopen = unexpected\n"
    "sys.argv = sys.argv[1:]\n"
    "runpy.run_path(sys.argv[0], run_name='__main__')\n"
)


class AdvisoryCase(unittest.TestCase):
    cases = CASES

    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name) / "checkout with spaces"
        scripts = self.root / "scripts"
        shutil.copytree(SCRIPTS / "oa_tools", scripts / "oa_tools",
                        ignore=shutil.ignore_patterns("__pycache__"))
        for name in self.cases:
            shutil.copyfile(SCRIPTS / name, scripts / name)
        (self.root / "docs").mkdir()
        self.make_corpus(self.root)
        self.nested = self.root / "nested"
        self.nested.mkdir()
        self.unrelated = Path(temporary.name) / "unrelated"
        self.make_corpus(self.unrelated, "foreign")
        (self.unrelated / "docs").mkdir()
        (self.unrelated / "docs" / "FORM-REGISTER.md").write_text("foreign register\n")

    def make_corpus(self, root, jurisdiction="example"):
        folder = root / "skills" / "international" / jurisdiction
        folder.mkdir(parents=True)
        for name, text in (("first.md", FIRST), ("second.md", SECOND), ("third.md", THIRD)):
            (folder / name).write_text(text, encoding="utf-8")

    def run_advisory(self, name, cwd, args=(), expected_code=None):
        if expected_code is None:
            expected_code = self.cases[name][1]
        result = subprocess.run(
            [sys.executable, "-X", "utf8", str(self.root / "scripts" / name), *args],
            cwd=cwd, capture_output=True, text=True, encoding="utf-8", timeout=30,
        )
        self.assertEqual(result.returncode, expected_code, result.stderr)
        self.assertEqual(result.stderr, "")
        return result.stdout

    def assert_default_scans(self):
        for name, (args, _, summary) in self.cases.items():
            outputs = []
            for cwd in (self.root, self.nested, self.unrelated):
                with self.subTest(script=name, cwd=cwd.name):
                    output = self.run_advisory(name, cwd, args)
                    outputs.append(output)
                    self.assertIn(summary, output)
                    self.assertNotIn("foreign", output)
                    self.assertNotIn(str(self.root), output)
            with self.subTest(script=name, comparison=True):
                self.assertEqual(outputs, outputs[:1] * 3, name)

    def assert_scopes_without_skills(self, renamed=False):
        corpus = self.root / "skills"
        if renamed:
            corpus = self.unrelated / "international" / "skills" / "copied guides"
            shutil.copytree(self.root / "skills", corpus)
            source = next((self.root / "skills").rglob("first.md")).parent
            for tree in ("foundation", "orchestrator", "cross-border"):
                shutil.copytree(source, corpus / tree)
        folder = corpus / next((self.root / "skills").rglob("first.md")).parent.relative_to(
            self.root / "skills")
        scopes = [(corpus, "."), (folder, ".")]
        if renamed:
            scopes.extend((self.unrelated, root) for root in (
                str(corpus), str(folder), os.path.relpath(corpus, self.unrelated),
                os.path.relpath(folder, self.unrelated)))
        if os.name == "nt":
            scopes.extend((self.unrelated, str(path).upper()) for path in (corpus, folder))
        for name, (args, _, summary) in self.cases.items():
            if not name.startswith("check-") or name in (
                    "check-quick-formula.py", "check-stale-futures.py"):
                continue
            baseline = self.run_advisory(name, self.root, args)
            self.assertIn(summary, baseline)
            for cwd, root in scopes:
                with self.subTest(script=name, cwd=str(cwd), root=root):
                    output = self.run_advisory(name, cwd, (*args, root))
                    self.assertIn(summary, output)
                    selected = (cwd / root).resolve()
                    for source in corpus.rglob("*.md"):
                        if source.is_relative_to(selected):
                            display = os.path.join(root, os.path.relpath(source, selected))
                            canonical = os.path.join("skills", os.path.relpath(source, corpus))
                            output = output.replace(display, canonical)
                    self.assertEqual(
                        [" ".join(line.split()) for line in output.splitlines()],
                        [" ".join(line.split()) for line in baseline.splitlines()])


class ReviewAdvisoryTests(AdvisoryCase):
    def test_owned_directory_scopes_can_omit_skills(self):
        self.assert_scopes_without_skills()

    def test_copied_guide_trees_can_have_another_root_name(self):
        self.assert_scopes_without_skills(renamed=True)

    def test_default_scans_find_the_same_issues_from_all_directories(self):
        self.assert_default_scans()

    def test_explicit_directory_still_selects_the_callers_corpus(self):
        for name, (args, _, summary) in CASES.items():
            if name.startswith("list-"):
                continue  # These CLIs accept filters, not a directory.
            with self.subTest(script=name):
                output = self.run_advisory(name, self.unrelated, (*args, "skills"))
                self.assertIn(summary, output)
                self.assertIn("foreign", output)
                self.assertNotIn("example", output)

    def test_multiple_relative_and_absolute_trees_work_for_glob_advisories(self):
        for name, args, summary in (
            ("check-quick-formula.py", (), "quick-formula tables checked: 2 ; broken boundaries: 4"),
            ("check-stale-futures.py", ("--today", "2026-10-07"), "date now past: 2"),
        ):
            roots = (os.path.relpath(self.root / "skills", self.unrelated),
                     str(self.unrelated / "skills"))
            output = self.run_advisory(name, self.unrelated, (*args, *roots))
            self.assertIn(summary, output)
            self.assertIn(os.path.join(roots[0], "international", "example", "first.md"), output)
            self.assertIn(os.path.join(roots[1], "international", "foreign", "first.md"), output)

    def test_walk_checkers_group_jurisdictions_independently_of_root_spelling(self):
        for filename, text in (("first.md", "$ 5000\n" * 10),
                               ("second.md", "$ 5000\n" * 10),
                               ("third.md", "£ 5000\n" * 5)):
            path = self.root / "skills" / "international" / "example" / filename
            path.write_text(path.read_text(encoding="utf-8") + text, encoding="utf-8")
        names = [name for name in CASES
                 if name.startswith("check-") and name not in (
                     "check-quick-formula.py", "check-stale-futures.py")]
        prefixes = ((self.root, os.path.join(".", "skills")),
                    (self.nested, os.path.join("..", "skills")),
                    (self.unrelated, str(self.root / "skills")))
        for name in names:
            baseline = self.run_advisory(name, self.root, ("skills",))
            if name == "check-currency-of-account.py":
                self.assertIn("jurisdictions with a house symbol: 1   outliers: 1", baseline)
            for cwd, prefix in prefixes:
                for suffix in ("", "international", os.path.join("international", "example")):
                    scope = os.path.join(prefix, suffix) if suffix else prefix
                    with self.subTest(script=name, scope=scope):
                        output = self.run_advisory(name, cwd, (scope,))
                        normalised = output.replace(prefix, "skills")
                        self.assertEqual(
                            [" ".join(line.split()) for line in normalised.splitlines()],
                            [" ".join(line.split()) for line in baseline.splitlines()])

    def test_filters_also_scan_the_checkout_from_another_directory(self):
        for name, args, code, expected in (
            ("list-source-mix.py", ("--jurisdiction", "example"), 0, "example: 0 authority, 1 secondary"),
            ("list-source-mix.py", ("--unclassified",), 0, "example"),
            ("list-source-mix.py", ("--load-bearing",), 0, "queue on their own (0)"),
            ("list-solo-citations.py", ("--min", "2"), 0, "Notice 2026-12"),
            ("list-withholding-scope.py", ("--show", "example"), 0, "Withholding tax on dividends"),
            ("list-withholding-scope.py", ("--classic-only",), 1, "1 of 1 jurisdictions"),
        ):
            with self.subTest(script=name, args=args):
                baseline = self.run_advisory(name, self.root, args, code)
                elsewhere = self.run_advisory(name, self.unrelated, args, code)
                self.assertIn(expected, elsewhere)
                self.assertNotIn("foreign", elsewhere)
                self.assertEqual(baseline, elsewhere)


class FlatFolderReviewTests(AdvisoryCase):
    cases = {name: case for name, case in CASES.items()
             if name.startswith("check-") and name not in (
                 "check-quick-formula.py", "check-stale-futures.py")}
    cases.update({
        "list-source-mix.py": CASES["list-source-mix.py"],
        "list-withholding-scope.py": CASES["list-withholding-scope.py"],
        "list-registration-thresholds.py": ((), 0, "jurisdictions stating a registration threshold: 1"),
        "list-withholding-rates.py": ((), 0, "jurisdictions stating a withholding rate: 1"),
        "list-midyear-changes.py": (("--since", "2025"), 0, "1 line(s) across 1"),
        "list-single-source-blocks.py": (("--jurisdiction", "federal"), 0,
                                         "guides with 4+ sourced numeric facts: 1"),
    })

    def make_corpus(self, root, jurisdiction="example"):
        folder = root / "skills" / "federal"
        folder.mkdir(parents=True)
        facts = (FIRST + "$ 5000\n" * 10 +
                 "| Tax year | Calendar year |\n"
                 "- **Levy rate** - 21% from 1 August 2025\n" +
                 "- **Levy band** - 100 _(Income Tax Act - https://rivermate.com/example)_\n" * 4,
                 SECOND + "$ 5000\n" * 10, THIRD + "£ 5000\n" * 5)
        for filename, text in zip(("first.md", "second.md", "third.md"), facts):
            (folder / filename).write_text(
                text if jurisdiction == "example" else "Foreign corpus has no claims.\n",
                encoding="utf-8")

    def test_flat_folders_find_sibling_issues_from_every_working_directory(self):
        self.assert_default_scans()

    def test_owned_directory_scopes_can_omit_skills(self):
        self.assert_scopes_without_skills()

    def test_copied_guide_trees_can_have_another_root_name(self):
        self.assert_scopes_without_skills(renamed=True)

    def test_flat_folder_scopes_keep_one_group_and_both_currency_modes(self):
        for name, (args, _, summary) in self.cases.items():
            if not name.startswith("check-"):
                continue
            baseline = self.run_advisory(name, self.root, args)
            self.assertIn(summary, baseline)
            self.assertIn("federal", baseline)
            if name == "check-currency-of-account.py":
                self.assertIn("jurisdictions with a house symbol: 1   outliers: 1", baseline)
            for cwd, prefix in ((self.root, os.path.join(".", "skills")),
                                (self.nested, os.path.join("..", "skills")),
                                (self.unrelated, str(self.root / "skills"))):
                for scope in (prefix, os.path.join(prefix, "federal")):
                    with self.subTest(script=name, scope=scope):
                        output = self.run_advisory(name, cwd, (*args, scope))
                        self.assertEqual(
                            [" ".join(line.split()) for line in output.replace(prefix, "skills").splitlines()],
                            [" ".join(line.split()) for line in baseline.splitlines()])

    def test_flat_folder_filters_show_the_claims_counted_by_the_summary(self):
        for name, args, expected in (
            ("list-source-mix.py", ("--jurisdiction", "federal"), "federal: 0 authority, 5 secondary"),
            ("list-withholding-scope.py", ("--show", "federal"), "1 withholding-labelled line(s) in federal"),
        ):
            with self.subTest(script=name):
                output = self.run_advisory(name, self.unrelated, args, 0)
                self.assertIn(expected, output)

    def test_shared_workflow_trees_do_not_create_jurisdiction_findings(self):
        baselines = {name: self.run_advisory(name, self.root, args)
                     for name, (args, _, _) in self.cases.items()}
        for tree in ("orchestrator", "cross-border", "foundation", "integrations",
                     "intelligence", "templates", "financial-reporting/revenue-recognition"):
            shutil.copytree(self.root / "skills" / "federal", self.root / "skills" / tree)
        for name, (args, _, _) in self.cases.items():
            with self.subTest(script=name):
                self.assertEqual(self.run_advisory(name, self.root, args), baselines[name])


class RemainingReviewAdvisoryTests(AdvisoryCase):
    cases = {
        "check-headline-cit.py": ((), 0, "disagreeing with themselves:                  1"),
        "check-form-jurisdiction.py": ((), 0, "candidates: 1"),
        "check-deadline-rules.py": ((), 0, "rules disagreeing with the date beside them: 1"),
        "check-superseded-rates.py": ((), 0, "superseded-rate leads: 1"),
        "list-filing-deadlines.py": ((), 0, "jurisdictions stating an annual return deadline: 1"),
        "list-hedged-claims.py": ((), 0, "hedged figures on labelled facts: 1"),
        "list-midyear-changes.py": (("--since", "2025"), 0, "1 line(s) across 1"),
        "list-registration-thresholds.py": ((), 0, "jurisdictions stating a registration threshold: 1"),
        "list-single-source-blocks.py": ((), 0, "guides with 4+ sourced numeric facts: 1"),
        "list-statute-links.py": ((), 0, "across 1 jurisdictions"),
        "list-withholding-rates.py": ((), 0, "jurisdictions stating a withholding rate: 1"),
        "list-vat-rates.py": ((), 0, "<-- guides disagree"),
        "build-form-register.py": ((), 0, "1 jurisdictions, 1 shared form identifiers"),
    }

    def make_corpus(self, root, jurisdiction="example"):
        folder = root / "skills" / "international" / jurisdiction
        folder.mkdir(parents=True)
        (folder / "first.md").write_text(
            "- **Standard corporate tax rate** - 20%\n"
            "- **Standard VAT rate** - 12% from 1 January 2026 (was 10% in 2025)\n"
            "| Tax year | Calendar year |\n"
            "- **Levy rate** - 21% from 1 August 2025\n"
            "- **Annual personal income tax return deadline** - 31 March\n"
            "Within 6 months of the close of the financial year "
            "(31 July for calendar-year companies).\n"
            "- **VAT registration threshold** - EUR 12,345\n"
            "- **Withholding tax on dividends** - 10% ((approx - confirm))\n"
            "File Form X123.\n" +
            "- **Levy band** - 100 _(Income Tax Act - https://rivermate.com/example)_\n" * 4,
            encoding="utf-8",
        )
        (folder / "second.md").write_text(
            "- **Standard corporate tax rate** - 25%\n"
            "- **Standard VAT rate** - 10%\n"
            "Use Form X123.\n", encoding="utf-8",
        )
        for state, count in (("home", 6), (jurisdiction, 1)):
            path = root / "skills" / "us-states" / state / "forms.md"
            path.parent.mkdir(parents=True)
            path.write_text("Form X888\n" * count, encoding="utf-8")

    def test_remaining_defaults_find_known_issues_from_all_directories(self):
        self.assert_default_scans()

    def test_filters_use_the_checkout_from_another_directory(self):
        for name, args, expected in (
            ("check-headline-cit.py", ("--show-skipped",), "skipped (sector, band"),
            ("list-hedged-claims.py", ("example",), "example: 1 hedged figures"),
            ("list-statute-links.py", ("--jurisdiction", "example"), "rivermate.com"),
            ("list-single-source-blocks.py", ("--jurisdiction", "example", "--all"), "first.md"),
        ):
            with self.subTest(script=name):
                baseline = self.run_advisory(name, self.root, args)
                elsewhere = self.run_advisory(name, self.unrelated, args)
                self.assertIn(expected, elsewhere)
                self.assertNotIn("foreign", elsewhere)
                self.assertEqual(baseline, elsewhere)

    def test_form_register_is_written_into_its_checkout(self):
        self.run_advisory("build-form-register.py", self.unrelated)
        register = (self.root / "docs" / "FORM-REGISTER.md").read_text(encoding="utf-8")
        self.assertIn("## example", register)
        self.assertIn("`Form X123`", register)
        self.assertNotIn("foreign", register)
        self.assertEqual((self.unrelated / "docs" / "FORM-REGISTER.md").read_text(),
                         "foreign register\n")

    def test_tied_source_hosts_produce_a_stable_report(self):
        path = self.root / "skills" / "international" / "example" / "first.md"
        path.write_text(
            "- **Levy band** - 100 https://revenue.example.gov/rates "
            "https://taxsummaries.pwc.com/example\n" * 4, encoding="utf-8",
        )
        outputs = []
        for seed in ("0", "1", "2", "3"):
            result = subprocess.run(
                [sys.executable, "-X", "utf8",
                 str(self.root / "scripts" / "list-single-source-blocks.py"), "--all"],
                cwd=self.unrelated, env={"PYTHONHASHSEED": seed},
                capture_output=True, text=True, encoding="utf-8", timeout=30,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("revenue.example.gov", result.stdout)
            outputs.append(result.stdout)
        self.assertEqual(outputs, [outputs[0]] * 4)

    def test_citation_rot_uses_checkout_citations_with_offline_responses(self):
        script = self.root / "scripts" / "list-citation-rot.py"
        shutil.copyfile(SCRIPTS / script.name, script)
        for args in ((), ("--jurisdiction", "example", "--hosts", "rivermate.com", "--limit", "1")):
            outputs = []
            for cwd in (self.root, self.nested, self.unrelated):
                result = subprocess.run(
                    [sys.executable, "-X", "utf8", "-c", OFFLINE_CITATION_DRIVER, str(script), *args],
                    cwd=cwd, capture_output=True, text=True, encoding="utf-8", timeout=30,
                )
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertIn("checking 1 hosts", result.stderr)
                self.assertIn("rivermate.com  -- 4 citation(s) in example", result.stdout)
                self.assertNotIn("foreign", result.stdout)
                outputs.append(result.stdout)
            self.assertEqual(outputs, [outputs[0]] * 3)

    def test_citation_rot_filters_and_labels_flat_guides(self):
        script = self.root / "scripts" / "list-citation-rot.py"
        shutil.copyfile(SCRIPTS / script.name, script)
        shutil.copytree(self.root / "skills" / "international" / "example",
                        self.root / "skills" / "federal")
        for args, expected in (
            ((), "rivermate.com  -- 8 citation(s) in example, federal"),
            (("--jurisdiction", "federal"), "rivermate.com  -- 4 citation(s) in federal"),
        ):
            for cwd in (self.root, self.nested, self.unrelated):
                with self.subTest(args=args, cwd=cwd):
                    result = subprocess.run(
                        [sys.executable, "-X", "utf8", "-c", OFFLINE_CITATION_DRIVER,
                         str(script), *args], cwd=cwd, capture_output=True, text=True,
                        encoding="utf-8", timeout=30,
                    )
                    self.assertEqual(result.returncode, 0, result.stderr)
                    self.assertIn("checking 1 hosts", result.stderr)
                    self.assertIn(expected, result.stdout)

    def test_citation_discovery_applies_filters_and_template_exclusion_to_explicit_roots(self):
        script = self.root / "scripts" / "list-citation-rot.py"
        shutil.copyfile(SCRIPTS / script.name, script)
        shutil.copytree(self.root / "skills" / "international" / "example",
                        self.root / "skills" / "federal")
        templates = self.root / "skills" / "templates"
        templates.mkdir()
        (templates / "ignored.md").write_text("https://excluded.example.gov/source\n")
        driver = CITATION_LOADER + (
            "import json\n"
            "where = rot.cited_hosts(root=sys.argv[2], only=sys.argv[3] or None)\n"
            "print(json.dumps({host: len(cites) for host, cites in where.items()}))\n"
        )
        for cwd, root in ((self.root, "skills"), (self.root / "skills", "."),
                          (self.unrelated, str(self.root / "skills"))):
            for only, count in (("", 8), ("federal", 4), ("example", 4)):
                with self.subTest(root=root, only=only):
                    result = subprocess.run(
                        [sys.executable, "-X", "utf8", "-c", driver, str(script), root, only],
                        cwd=cwd, capture_output=True, text=True, encoding="utf-8", timeout=30,
                    )
                    self.assertEqual(result.returncode, 0, result.stderr)
                    self.assertEqual(result.stderr, "")
                    self.assertEqual(json.loads(result.stdout), {"rivermate.com": count})

    def test_network_review_help_and_selftests_do_no_review_work(self):
        for name in ("list-citation-rot.py", "check-cited-hosts.py"):
            script = self.root / "scripts" / name
            shutil.copyfile(SCRIPTS / name, script)
            for arg in ("--help", "-h", "--selftest"):
                for cwd in (self.root, self.nested, self.unrelated):
                    with self.subTest(script=name, arg=arg, cwd=cwd):
                        result = subprocess.run(
                            [sys.executable, "-X", "utf8", "-c", NO_REVIEW_DRIVER, str(script), arg],
                            cwd=cwd, capture_output=True, text=True, encoding="utf-8", timeout=30,
                        )
                        self.assertEqual(result.returncode, 0, result.stderr)
                        self.assertEqual(result.stderr, "")
                        self.assertIn("selftest:" if arg == "--selftest" else "usage:", result.stdout)
            for arg in ("--help", "--selftest"):
                with self.subTest(script=name, entry_point=arg):
                    result = subprocess.run(
                        [sys.executable, "-X", "utf8", "-c", NETWORK_BLOCKED_ENTRY_DRIVER,
                         str(script), arg], cwd=self.unrelated, capture_output=True,
                        text=True, encoding="utf-8", timeout=30,
                    )
                    self.assertEqual(result.returncode, 0, result.stderr)
                    self.assertEqual(result.stderr, "")
                    self.assertIn("selftest:" if arg == "--selftest" else "usage:", result.stdout)

    def test_network_review_rejects_invalid_arguments_before_work(self):
        invalid = {
            "list-citation-rot.py": (
                ("--limti", "1"), ("extra",), ("--jurisdiction",), ("--hosts",),
                ("--limit",), ("--limit", "bad"), ("--limit", "-1"),
                ("--jobs",), ("--jobs", "bad"), ("--jobs", "0"), ("--jobs", "-1"),
            ),
            "check-cited-hosts.py": (
                ("--grad", "hard"), ("extra",), ("--grade",), ("--grade", "unknown"),
            ),
        }
        for name, cases in invalid.items():
            script = self.root / "scripts" / name
            shutil.copyfile(SCRIPTS / name, script)
            for args in cases:
                with self.subTest(script=name, args=args):
                    result = subprocess.run(
                        [sys.executable, "-X", "utf8", "-c", NO_REVIEW_DRIVER, str(script), *args],
                        cwd=self.unrelated, capture_output=True, text=True, encoding="utf-8", timeout=30,
                    )
                    self.assertEqual(result.returncode, 2, result.stderr)
                    self.assertEqual(result.stdout, "")
                    self.assertIn("error:", result.stderr)
                    self.assertNotIn("Traceback", result.stderr)
                    self.assertNotIn("unexpected review work", result.stderr)

    def test_citation_zero_limit_checks_no_citation_hosts(self):
        script = self.root / "scripts" / "list-citation-rot.py"
        shutil.copyfile(SCRIPTS / script.name, script)
        for cwd in (self.root, self.nested, self.unrelated):
            with self.subTest(cwd=cwd):
                result = subprocess.run(
                    [sys.executable, "-X", "utf8", "-c", OFFLINE_CITATION_DRIVER,
                     str(script), "--limit", "0"], cwd=cwd, capture_output=True,
                    text=True, encoding="utf-8", timeout=30,
                )
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertIn("checking 0 hosts", result.stderr)
                self.assertNotIn("rivermate.com", result.stdout)
                self.assertNotIn("citation(s) in", result.stdout)

    def test_network_review_valid_options_preserve_their_effects(self):
        script = self.root / "scripts" / "list-citation-rot.py"
        shutil.copyfile(SCRIPTS / script.name, script)
        result = subprocess.run(
            [sys.executable, "-X", "utf8", "-c", OFFLINE_CITATION_DRIVER,
             str(script), "--limit", "1", "--jobs", "1", "--hosts", "rivermate.com",
             "--jurisdiction", "example"], cwd=self.unrelated, capture_output=True,
            text=True, encoding="utf-8", timeout=30,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("checking 1 hosts with 1 workers", result.stderr)
        self.assertIn("rivermate.com  -- 4 citation(s) in example", result.stdout)
        script = self.root / "scripts" / "check-cited-hosts.py"
        shutil.copyfile(SCRIPTS / script.name, script)
        driver = CITATION_LOADER + (
            "hosts = {kind: {kind + '.md'} for kind in ('hard', 'deep-link', 'reserved')}\n"
            "rot.collect_hosts = lambda: (hosts, 3)\n"
            "rot.grade = lambda host: (host, 'synthetic ' + host)\n"
            "sys.exit(rot.main(sys.argv[2:]))\n"
        )
        for args in (("--no-network",), ("--grade", "hard"),
                     ("--grade", "deep-link"), ("--grade", "reserved")):
            with self.subTest(args=args):
                result = subprocess.run(
                    [sys.executable, "-X", "utf8", "-c", driver, str(script), *args],
                    cwd=self.unrelated, capture_output=True, text=True, encoding="utf-8", timeout=30,
                )
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(result.stderr, "")
                self.assertIn("scanned 3 files; 3 unique hostnames cited", result.stdout)
                if args[0] == "--no-network":
                    self.assertIn("nothing resolved", result.stdout)
                    self.assertNotIn("synthetic", result.stdout)
                else:
                    self.assertIn("synthetic " + args[1], result.stdout)
                    self.assertEqual(result.stdout.count("synthetic"), 1)


class ReviewCLIArgumentTests(AdvisoryCase):
    directory_cases = {name: case for name, case in CASES.items() if name.startswith("check-")}
    fixed_cases = {name: case for name, case in RemainingReviewAdvisoryTests.cases.items()
                   if name.startswith("check-")}
    cases = {**directory_cases, **fixed_cases}
    multiple_roots = ("check-quick-formula.py", "check-stale-futures.py")
    selftests = ("check-amount-conflicts.py", "check-deadline-rules.py",
                 "check-superseded-rates.py", "check-stale-futures.py")
    blocked_scan_driver = (
        "import builtins, glob, os, runpy, sys\n"
        "def unexpected(*args, **kwargs):\n"
        "    raise AssertionError('unexpected scan before argument validation')\n"
        "builtins.open = os.walk = glob.glob = unexpected\n"
        "sys.argv = sys.argv[1:]\n"
        "runpy.run_path(sys.argv[0], run_name='__main__')\n"
    )

    def run_without_scan(self, name, args, expected_code):
        result = subprocess.run(
            [sys.executable, "-X", "utf8", "-c", self.blocked_scan_driver,
             str(self.root / "scripts" / name), *args],
            cwd=self.unrelated, capture_output=True, text=True, encoding="utf-8", timeout=30,
        )
        self.assertEqual(result.returncode, expected_code, result.stderr)
        self.assertNotIn("Traceback", result.stderr)
        if expected_code:
            self.assertIn("error:", result.stderr)
            self.assertEqual(result.stdout, "")
        else:
            self.assertEqual(result.stderr, "")
        return result

    def test_unknown_options_fail_before_scanning(self):
        for name in self.cases:
            variants = [("--not-an-option",)]
            if name in self.selftests:
                variants.extend((("--not-an-option", "--selftest"), ("--self",)))
            for args in variants:
                with self.subTest(script=name, args=args):
                    self.run_without_scan(name, args, 2)

    def test_missing_and_file_roots_fail_before_scanning(self):
        file = self.unrelated / "file.md"
        file.write_text("Synthetic file argument.\n", encoding="utf-8")
        valid = str(self.unrelated / "skills")
        for name in self.directory_cases:
            roots = [(str(self.unrelated / "missing"),), (str(file),),
                     ("--", str(self.unrelated / "missing")), ("--", str(file))]
            if name in self.multiple_roots:
                roots.extend(((valid, str(file)), (str(file), valid)))
            for args in roots:
                with self.subTest(script=name, args=args):
                    self.run_without_scan(name, args, 2)

    def test_unsupported_positional_arguments_fail_before_scanning(self):
        valid = str(self.unrelated / "skills")
        for name in self.cases:
            if name in self.multiple_roots:
                continue
            args = (valid,) if name in self.fixed_cases else (valid, valid)
            with self.subTest(script=name):
                self.run_without_scan(name, args, 2)

    def test_help_does_not_scan(self):
        for name in self.cases:
            with self.subTest(script=name):
                result = self.run_without_scan(name, ("--help",), 0)
                self.assertIn("usage:", result.stdout)
                self.assertIn(name, result.stdout)

    def test_selftests_do_not_scan(self):
        for name in self.selftests:
            with self.subTest(script=name):
                result = self.run_without_scan(name, ("--selftest",), 0)
                self.assertIn("selftest:", result.stdout)

    def test_invalid_today_is_a_cli_error_before_scanning(self):
        for args in (("--today",), ("--today", "invalid"),
                     ("--today", "2026-02-30"), ("--today", "2026-13-01")):
            with self.subTest(args=args):
                self.run_without_scan("check-stale-futures.py", args, 2)

    def test_existing_empty_directories_remain_valid(self):
        empty = self.unrelated / "empty"
        empty.mkdir()
        for name, (args, _, _) in self.directory_cases.items():
            with self.subTest(script=name):
                self.run_advisory(name, self.unrelated, (*args, str(empty)))

    def test_today_can_appear_before_between_or_after_directory_arguments(self):
        roots = (str(self.root / "skills"), str(self.unrelated / "skills"))
        date = ("--today", "2026-10-07")
        outputs = []
        for args in ((*date, *roots), (roots[0], *date, roots[1]), (*roots, *date)):
            with self.subTest(args=args):
                output = self.run_advisory("check-stale-futures.py", self.unrelated, args)
                self.assertIn("date now past: 2", output)
                outputs.append(output)
        self.assertEqual(outputs, outputs[:1] * 3)

    def test_option_separator_allows_a_directory_name_starting_with_dash(self):
        shutil.copytree(self.root / "skills", self.unrelated / "--guides")
        for name, (args, _, summary) in self.directory_cases.items():
            with self.subTest(script=name):
                output = self.run_advisory(name, self.unrelated, (*args, "--", "--guides"))
                self.assertIn(summary, output)
        roots = (str(self.root / "skills"), str(self.unrelated / "skills"))
        date = ("--today", "2026-10-07")
        outputs = []
        for args in ((*date, *roots, "--", "--guides"),
                     (roots[0], *date, roots[1], "--", "--guides")):
            output = self.run_advisory("check-stale-futures.py", self.unrelated, args)
            self.assertIn("date now past: 3", output)
            outputs.append(output)
        self.assertEqual(*outputs)


class ListCLIArgumentTests(AdvisoryCase):
    cases = {name: case for name, case in
             {**CASES, **RemainingReviewAdvisoryTests.cases}.items()
             if name.startswith("list-")}
    make_corpus = RemainingReviewAdvisoryTests.make_corpus
    blocked_scan_driver = ReviewCLIArgumentTests.blocked_scan_driver
    run_without_scan = ReviewCLIArgumentTests.run_without_scan
    selftests = tuple(name for name in cases if name != "list-vat-rates.py")

    def test_unknown_options_fail_before_scan(self):
        for name in self.cases:
            variants = [("--not-an-option",)]
            if name in self.selftests:
                variants.extend((("--not-an-option", "--selftest"), ("--self",)))
            for args in variants:
                with self.subTest(script=name, args=args):
                    self.run_without_scan(name, args, 2)

    def test_help_does_not_scan(self):
        for name in self.cases:
            with self.subTest(script=name):
                result = self.run_without_scan(name, ("--help",), 0)
                self.assertIn("usage:", result.stdout)
                self.assertIn(name, result.stdout)

    def test_selftests_do_not_scan(self):
        for name in self.selftests:
            with self.subTest(script=name):
                result = self.run_without_scan(name, ("--selftest",), 0)
                self.assertIn("selftest:", result.stdout)

    def test_unsupported_positionals_fail_before_scan(self):
        for name in self.cases:
            args = ("example", "extra") if name == "list-hedged-claims.py" else ("extra",)
            with self.subTest(script=name):
                self.run_without_scan(name, args, 2)

    def test_missing_values_and_bad_numbers_fail_before_scan(self):
        invalid = {
            "list-statute-links.py": [("--jurisdiction",)],
            "list-source-mix.py": [("--jurisdiction",)],
            "list-withholding-scope.py": [("--show",)],
            "list-solo-citations.py": [("--min",), ("--min", "bad"), ("--min", "-1")],
            "list-midyear-changes.py": [("--since",), ("--since", "bad")],
            "list-single-source-blocks.py": [
                ("--jurisdiction",), ("--min-facts",), ("--min-facts", "bad"),
                ("--min-facts", "-1"), ("--share",), ("--share", "bad"),
                ("--share", "nan"), ("--share", "inf"), ("--share", "-0.1"),
                ("--share", "1.1"), ("--share", "1.1", "--selftest"),
            ],
        }
        for name, cases in invalid.items():
            for args in cases:
                with self.subTest(script=name, args=args):
                    self.run_without_scan(name, args, 2)

    def test_conflicting_selections_fail_before_scan(self):
        cases = {
            "list-source-mix.py": [
                ("--unclassified", "--load-bearing"),
                ("--unclassified", "--jurisdiction", "example"),
                ("--load-bearing", "--jurisdiction", "example"),
            ],
            "list-withholding-scope.py": [("--show", "example", "--classic-only")],
        }
        for name, variants in cases.items():
            for args in variants:
                with self.subTest(script=name, args=args):
                    self.run_without_scan(name, args, 2)

    def test_valid_count_and_share_boundaries_select_reports(self):
        name = "list-single-source-blocks.py"
        file = self.root / "skills/international/example/three-facts.md"
        file.write_text("- **Rate** - 20% _(https://rivermate.com/r)_\n" * 3,
                        encoding="utf-8")
        for share in ("0", "0.75", "1"):
            with self.subTest(share=share):
                output = self.run_advisory(name, self.unrelated,
                    ("--min-facts", "0", "--share", share, "--all"))
                self.assertIn("three-facts.md", output)
        output = self.run_advisory(name, self.unrelated, ("--min-facts", "4", "--all"))
        self.assertNotIn("three-facts.md", output)
        self.assertIn("guides with 4+ sourced numeric facts: 1", output)
        output = self.run_advisory("list-solo-citations.py", self.unrelated, ("--min", "0"))
        self.assertIn("cited 0+ times", output)

    def test_unknown_jurisdiction_remains_a_valid_empty_selection(self):
        cases = {
            "list-statute-links.py": (("--jurisdiction", "no-such-group"), "across 0 jurisdictions"),
            "list-source-mix.py": (("--jurisdiction", "no-such-group"), "no external citations recorded"),
            "list-single-source-blocks.py": (("--jurisdiction", "no-such-group"), "guides with 4+ sourced numeric facts: 0"),
            "list-hedged-claims.py": (("no-such-group",), "no-such-group: 0 hedged figures"),
            "list-withholding-scope.py": (("--show", "no-such-group"), "no withholding-labelled lines found"),
        }
        for name, (args, summary) in cases.items():
            with self.subTest(script=name):
                output = self.run_advisory(name, self.unrelated, args, expected_code=0)
                self.assertIn(summary, output)


class IncompleteFixesArgumentTests(AdvisoryCase):
    name = "list-incomplete-fixes.py"
    cases = {name: ((), 0, "files changed in the diff:")}
    blocked_scan_driver = (
        "import builtins, glob, os, runpy, subprocess, sys\n"
        "def unexpected(*args, **kwargs):\n"
        "    raise AssertionError('unexpected Git or scan before argument validation')\n"
        "builtins.open = os.walk = glob.glob = subprocess.run = unexpected\n"
        "sys.argv = sys.argv[1:]\n"
        "runpy.run_path(sys.argv[0], run_name='__main__')\n"
    )
    run_without_scan = ReviewCLIArgumentTests.run_without_scan

    def make_corpus(self, root, jurisdiction="example"):
        folder = root / "skills" / "international" / jurisdiction
        folder.mkdir(parents=True)
        value = "20%" if jurisdiction == "foreign" else "12.5%"
        (folder / "first.md").write_text(
            "Changed value " + value + "\nUnchanged copy " + value + "\n", encoding="utf-8")

    def setUp(self):
        super().setUp()
        self.hooks = self.root.parent / "empty-hooks"
        self.hooks.mkdir()
        for root in (self.root, self.unrelated):
            self.init_git(root)

    def git(self, root, *args, input=None, check=True):
        return subprocess.run(
            ["git", "-c", "user.email=t@example.invalid", "-c", "user.name=T",
             "-c", "commit.gpgsign=false", "-c", "tag.gpgsign=false",
             "-c", "core.autocrlf=false", "-c", "core.hooksPath=" + str(self.hooks),
             "-c", "init.templateDir=" + str(self.hooks), *args],
            cwd=root, input=input, capture_output=True, text=input is None,
            encoding="utf-8" if input is None else None,
            timeout=30, check=check,
        )

    def init_git(self, root, object_format=None):
        flags = [] if object_format is None else ["--object-format=" + object_format]
        result = self.git(root, "init", "-q", "-b", "work", *flags, check=False)
        if result.returncode:
            if object_format:
                self.skipTest("installed Git cannot initialise a " + object_format + " repository")
            self.fail(result.stderr)
        self.git(root, "add", "skills")
        self.git(root, "commit", "-q", "-m", "base")
        self.git(root, "tag", "base")
        self.git(root, "tag", "-a", "annotated", "-m", "synthetic tag")
        self.git(root, "branch", "named-base")
        self.git(root, "update-ref", "refs/remotes/origin/main", "base")
        path = next((root / "skills").rglob("first.md"))
        before = path.read_text(encoding="utf-8")
        old = "20%" if "20%" in before else "12.5%"
        new = "25%" if old == "20%" else "15%"
        path.write_text(before.replace("Changed value " + old, "Changed value " + new), encoding="utf-8")
        self.git(root, "add", "skills")
        self.git(root, "commit", "-q", "-m", "edit")

    def run_cli(self, args=(), cwd=None):
        return subprocess.run(
            [sys.executable, "-X", "utf8", str(self.root / "scripts" / self.name), *args],
            cwd=cwd or self.unrelated, capture_output=True, timeout=30,
        )

    def assert_git_failure(self, result):
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertEqual(result.stdout, b"")
        self.assertTrue(result.stderr)
        self.assertNotIn(b"Traceback", result.stderr)

    def test_invalid_arguments_fail_before_git_or_scanning(self):
        variants = (("--not-an-option",), ("--bas", "base"), ("base",), ("--base",),
                    ("--base=",), ("--base=--stat",),
                    ("--base", "base", "--base", "HEAD"))
        for args in variants:
            for mode in ((), ("--selftest",), ("--help",)):
                with self.subTest(args=args, mode=mode):
                    self.run_without_scan(self.name, (*args, *mode), 2)

    def test_help_and_selftest_do_not_call_git_or_scan(self):
        help_result = self.run_without_scan(self.name, ("--help",), 0)
        self.assertIn("usage:", help_result.stdout)
        for args in (("--selftest",), ("--selftest", "--base", "no-such-revision")):
            result = self.run_without_scan(self.name, args, 0)
            self.assertIn("known misses pass", result.stdout)

    def test_git_output_options_cannot_overwrite_an_existing_file(self):
        path = self.unrelated / "skills" / "international" / "foreign" / "first.md"
        path.write_text(path.read_text(encoding="utf-8") + "Uncommitted value 23.5%\n", encoding="utf-8")
        prefix = self.unrelated / "owned-output"
        target = Path(str(prefix) + "...HEAD")
        value = "--output=" + str(prefix)
        for args, expected in ((("--base", value), 2), (("--base=" + value,), 2), (None, 1)):
            with self.subTest(args=args):
                target.write_bytes(b"OWNED SYNTHETIC SENTINEL\n")
                if args is None:
                    result = subprocess.run(
                        [sys.executable, "-X", "utf8", "-c",
                         CITATION_LOADER + "sys.exit(rot.main(sys.argv[2]))\n",
                         str(self.root / "scripts" / self.name), value],
                        cwd=self.unrelated, capture_output=True, timeout=30,
                    )
                else:
                    result = self.run_cli(args)
                self.assertEqual(target.read_bytes(), b"OWNED SYNTHETIC SENTINEL\n")
                self.assertEqual(result.returncode, expected, result.stderr)
                self.assertEqual(result.stdout, b"")
                self.assertTrue(result.stderr)
                self.assertNotIn(b"Traceback", result.stderr)
                self.assertEqual(set(self.unrelated.glob("owned-output*")), {target})

    def test_revision_spellings_keep_the_caller_repository_report(self):
        expected = self.run_cli()
        self.assertEqual(expected.returncode, 0, expected.stderr)
        self.assertIn(b"20%", expected.stdout)
        self.assertNotIn(b"12.5%", expected.stdout)
        commit = self.git(self.unrelated, "rev-parse", "base").stdout.strip()
        for base in ("base", "named-base", "origin/main", "annotated", commit, commit[:12],
                     "HEAD~1", "HEAD^", "base^{commit}", ":/base", ":/^base"):
            for args in (("--base", base), ("--base=" + base,)):
                with self.subTest(args=args):
                    result = self.run_cli(args)
                    self.assertEqual(result.returncode, 0, result.stderr)
                    self.assertEqual(result.stderr, b"")
                    self.assertEqual(result.stdout, expected.stdout)
        primary = self.run_cli(("--base", "base"), self.root)
        self.assertEqual(primary.returncode, 0, primary.stderr)
        self.assertIn(b"12.5%", primary.stdout)
        empty = self.run_cli(("--base", "HEAD"))
        self.assertEqual(empty.returncode, 0, empty.stderr)
        self.assertIn(b"files changed in the diff: 0", empty.stdout)
        self.assertNotEqual(empty.stdout, expected.stdout)
        equal_form = self.run_cli(("--base=HEAD",))
        self.assertEqual(equal_form.returncode, 0, equal_form.stderr)
        self.assertEqual(equal_form.stderr, b"")
        self.assertEqual(equal_form.stdout, empty.stdout)
        self.assert_git_failure(self.run_cli(("--base=no-such-revision",)))

    def test_git_operational_failures_are_not_successful_reviews(self):
        tree = self.git(self.unrelated, "rev-parse", "HEAD^{tree}").stdout.strip()
        orphan = self.git(self.unrelated, "commit-tree", tree, "-m", "unrelated history").stdout.strip()
        for base in ("no-such-revision", "HEAD:skills/international/foreign/first.md", "HEAD^{tree}", orphan):
            with self.subTest(base=base):
                self.assert_git_failure(self.run_cli(("--base", base)))
        outside = self.root.parent / "not-a-repository"
        outside.mkdir()
        self.assert_git_failure(self.run_cli(("--base", "base"), outside))
        self.git(self.unrelated, "update-ref", "-d", "refs/remotes/origin/main")
        self.assert_git_failure(self.run_cli())
        driver = CITATION_LOADER + (
            "def missing(*args, **kwargs):\n"
            "    raise OSError('synthetic unavailable Git')\n"
            "rot.subprocess.run = missing\n"
            "sys.exit(rot.main('base'))\n"
        )
        result = subprocess.run(
            [sys.executable, "-X", "utf8", "-c", driver, str(self.root / "scripts" / self.name)],
            cwd=outside, capture_output=True, timeout=30,
        )
        self.assert_git_failure(result)
        self.assertIn(b"synthetic unavailable Git", result.stderr)

    def test_three_dot_diff_and_empty_committed_diff_are_preserved(self):
        expected = self.run_cli(("--base", "base")).stdout
        path = self.unrelated / "skills" / "international" / "foreign" / "first.md"
        self.git(self.unrelated, "checkout", "-q", "-b", "divergent", "base")
        path.write_text(path.read_text(encoding="utf-8").replace("Changed value 20%", "Changed value 22.5%"), encoding="utf-8")
        self.git(self.unrelated, "add", "skills")
        self.git(self.unrelated, "commit", "-q", "-m", "divergent edit")
        self.git(self.unrelated, "checkout", "-q", "work")
        result = self.run_cli(("--base", "divergent"))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, expected)
        path.write_text(path.read_text(encoding="utf-8") + "Staged value 99%\n", encoding="utf-8")
        self.git(self.unrelated, "add", "skills")
        path.write_text(path.read_text(encoding="utf-8") + "Unstaged value 98%\n", encoding="utf-8")
        empty = self.run_cli(("--base", "HEAD"))
        self.assertEqual(empty.returncode, 0, empty.stderr)
        self.assertIn(b"files changed in the diff: 0", empty.stdout)

    def test_commit_context_abbreviations_and_sha256_repositories_work(self):
        import hashlib
        expected = self.run_cli(("--base", "base")).stdout
        commit = self.git(self.unrelated, "rev-parse", "base").stdout.strip()
        prefix = commit[:4]
        hash_object = hashlib.sha1 if len(commit) == 40 else hashlib.sha256
        for number in range(1000000):
            data = ("Synthetic collision %d\n" % number).encode()
            oid = hash_object(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
            if oid.startswith(prefix):
                break
        else:
            self.fail("synthetic collision search bound exhausted")
        blob = self.git(self.unrelated, "hash-object", "-w", "--stdin", input=data).stdout.decode().strip()
        self.assertEqual(blob, oid)
        result = self.run_cli(("--base", prefix))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, expected)
        sha_root = self.root.parent / "sha256"
        self.make_corpus(sha_root, "foreign")
        self.init_git(sha_root, "sha256")
        sha_commit = self.git(sha_root, "rev-parse", "base").stdout.strip()
        self.assertEqual(len(sha_commit), 64)
        sha_result = self.run_cli(("--base", sha_commit), sha_root)
        self.assertEqual(sha_result.returncode, 0, sha_result.stderr)
        self.assertEqual(sha_result.stdout, expected)


if __name__ == "__main__":
    unittest.main()
