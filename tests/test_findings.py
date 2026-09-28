"""Tests for scripts/oa_tools/findings.py, the gate checkers' shared core.

The contract under test: a checker's findings are compared with a committed
baseline of fingerprints; a finding the baseline does not list fails the
gate, and so does a baseline entry that no longer reproduces, so the file can
only shrink as findings are fixed. `--json` is the machine-readable form and
`--update-baseline` the one sanctioned way to change the file.
"""

from __future__ import annotations

import argparse
import contextlib
import io
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from oa_tools import findings  # noqa: E402
from oa_tools.findings import Finding, Report  # noqa: E402


def _args(**overrides):
    values = {"json": False, "baseline": None, "no_baseline": False, "update_baseline": False, "roots": ["skills"]}
    values.update(overrides)
    return argparse.Namespace(**values)


class FindingTests(unittest.TestCase):
    def test_fingerprint_is_path_and_normalized_key(self) -> None:
        finding = Finding("skills" + os.sep + "x.md", "  100  x\n 10% =  20 ", "sum", line=7)
        self.assertEqual(finding.path, "skills/x.md")
        self.assertEqual(finding.fingerprint, "skills/x.md::100 x 10% = 20")
        self.assertEqual(finding.rendered(), "skills/x.md:7  sum")

    def test_equivalent_spellings_of_a_repository_path_share_one_fingerprint(self) -> None:
        """`./skills`, an absolute path and `../skills` from scripts/ name the
        same file as `skills`, so they must not make every baseline entry look
        stale and every finding new."""
        expected = "skills/x.md"
        spellings = [
            "skills/x.md",
            "./skills/x.md",
            "skills/../skills/x.md",
            os.path.join(str(REPO_ROOT), "skills", "x.md"),
            os.path.join(os.path.relpath(str(REPO_ROOT), os.getcwd()), "skills", "x.md"),
        ]
        for spelling in spellings:
            self.assertEqual(Finding(spelling, "k", "s").path, expected, spelling)
        self.assertEqual(findings.canonical_path("./skills"), "skills")
        self.assertEqual(findings.canonical_path(str(REPO_ROOT / "scripts" / ".." / "skills")), "skills")

    def test_paths_outside_the_repository_are_normalized_as_given(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            outside = os.path.join(tmp, "corpus", "skills", "x.md")
            self.assertEqual(Finding(outside, "k", "s").path, outside.replace(os.sep, "/"))
        self.assertEqual(findings.canonical_path("corpus/./skills/../skills/x.md"), "corpus/skills/x.md")

    def test_text_overrides_the_default_rendering_and_json_carries_everything(self) -> None:
        finding = Finding("a.md", "k", "s", detail={"values": [1, 2]}, text="custom\n    block")
        self.assertEqual(finding.rendered(), "custom\n    block")
        self.assertEqual(
            finding.as_dict(new=True),
            {"path": "a.md", "line": None, "key": "k", "summary": "s", "detail": {"values": [1, 2]},
             "fingerprint": "a.md::k", "new": True},
        )


class ArgumentParserTests(unittest.TestCase):
    def test_shared_flags_and_default_baseline(self) -> None:
        parser = findings.argument_parser("demo", "Demo checker.")
        args = parser.parse_args([])
        self.assertEqual(args.roots, ["skills"])
        self.assertEqual(args.baseline, str(REPO_ROOT / "scripts" / "baselines" / "demo.txt"))
        self.assertFalse(args.json or args.no_baseline or args.update_baseline)
        args = parser.parse_args(["packages", "agent-skills", "--json", "--no-baseline"])
        self.assertEqual(args.roots, ["packages", "agent-skills"])
        self.assertTrue(args.json and args.no_baseline)

    def test_checker_without_roots(self) -> None:
        parser = findings.argument_parser("demo", "Demo checker.", roots=False)
        self.assertFalse(hasattr(parser.parse_args([]), "roots"))
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
            parser.parse_args(["skills"])


class ReportTests(unittest.TestCase):
    def setUp(self) -> None:
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.baseline = os.path.join(tmp.name, "demo.txt")
        self.out = io.StringIO()

    def _report(self, **overrides):
        return Report("demo", _args(baseline=self.baseline, **overrides), out=self.out)

    def test_no_baseline_file_means_every_finding_fails(self) -> None:
        report = self._report()
        self.assertEqual(report.finish(), 0)
        self.assertIn("0 finding(s); no baseline", self.out.getvalue())
        self.assertIn("gate: PASS", self.out.getvalue())

        report = self._report()
        report.add(Finding("a.md", "k", "s", line=1))
        self.assertEqual(report.finish(), 1)
        self.assertIn("a.md:1  s", self.out.getvalue())
        self.assertIn("gate: FAIL", self.out.getvalue())

    def test_baseline_accepts_known_findings_and_flags_new_ones(self) -> None:
        findings.write_baseline(self.baseline, "demo", [Finding("a.md", "known", "s")])
        report = self._report()
        report.add(Finding("a.md", "known", "old one"))
        self.assertEqual(report.finish(), 0)
        text = self.out.getvalue()
        self.assertIn("a.md  old one", text)
        self.assertNotIn("NEW", text)
        self.assertIn("1 finding(s): 0 new, 1 in the baseline", text)

        self.out.seek(0), self.out.truncate()
        report = self._report()
        report.add(Finding("a.md", "known", "old one"))
        report.add(Finding("b.md", "fresh", "new one", line=3))
        self.assertEqual(report.finish(), 1)
        text = self.out.getvalue()
        self.assertIn("NEW b.md:3  new one", text)
        self.assertIn("2 finding(s): 1 new, 1 in the baseline", text)
        self.assertIn("--update-baseline", text)

    def test_stale_baseline_entries_fail_and_are_listed(self) -> None:
        findings.write_baseline(self.baseline, "demo", [Finding("skills/a.md", "fixed", "s")])
        report = self._report()
        self.assertEqual(report.finish(), 1)
        text = self.out.getvalue()
        self.assertIn("1 baseline entry no longer reproduce(s)", text)
        self.assertIn("    skills/a.md::fixed", text)
        self.assertIn("gate: FAIL", text)

    def test_no_baseline_flag_ignores_the_file(self) -> None:
        findings.write_baseline(self.baseline, "demo", [Finding("a.md", "known", "s")])
        report = self._report(no_baseline=True)
        report.add(Finding("a.md", "known", "s"))
        self.assertEqual(report.finish(), 1)
        self.assertIn("no baseline, so every finding fails the gate", self.out.getvalue())

    def test_update_baseline_writes_sorted_unique_fingerprints_and_passes(self) -> None:
        report = self._report(update_baseline=True)
        report.add(Finding("b.md", "z", "s"))
        report.add(Finding("a.md", "y", "s"))
        report.add(Finding("b.md", "z", "same fingerprint again"))
        self.assertEqual(report.finish(), 0)
        self.assertIn("baseline written: 2 fingerprint(s)", self.out.getvalue())
        lines = Path(self.baseline).read_text(encoding="utf-8").splitlines()
        self.assertTrue(lines[0].startswith("# Baseline for scripts/check-demo.py"))
        self.assertIn("python3 scripts/check-demo.py --update-baseline", "\n".join(lines[:4]))
        self.assertEqual([line for line in lines if not line.startswith("#")], ["a.md::y", "b.md::z"])
        self.assertEqual(findings.load_baseline(self.baseline), {"a.md::y", "b.md::z"})

        self.out.seek(0), self.out.truncate()
        report = self._report()
        report.add(Finding("a.md", "y", "s"))
        report.add(Finding("b.md", "z", "s"))
        self.assertEqual(report.finish(), 0)

    def test_scoped_run_judges_only_the_baseline_entries_under_its_roots(self) -> None:
        """`check-arithmetic.py skills/federal` must not call the international
        entries stale just because it did not scan them."""
        findings.write_baseline(self.baseline, "demo", [
            Finding("skills/federal/f.md", "k", "s"), Finding("skills/international/i.md", "k", "s"),
        ])
        report = self._report(roots=["skills/federal"])
        report.add(Finding("skills/federal/f.md", "k", "s"))
        self.assertEqual(report.finish(), 0, self.out.getvalue())
        self.assertNotIn("no longer reproduce", self.out.getvalue())

        self.out.seek(0), self.out.truncate()
        report = self._report(roots=["skills"])
        report.add(Finding("skills/federal/f.md", "k", "s"))
        self.assertEqual(report.finish(), 1, "a full-tree run still sees the missing international entry")
        self.assertIn("    skills/international/i.md::k", self.out.getvalue())

        self.out.seek(0), self.out.truncate()
        report = self._report(roots=["./skills/federal/"])
        report.add(Finding("skills/federal/f.md", "k", "s"))
        self.assertEqual(report.finish(), 0, "roots are canonicalized like paths")

    def test_scoped_update_keeps_the_entries_outside_its_roots(self) -> None:
        findings.write_baseline(self.baseline, "demo", [
            Finding("skills/federal/old.md", "k", "s"), Finding("skills/international/i.md", "k", "s"),
        ])
        report = self._report(roots=["skills/federal"], update_baseline=True)
        report.add(Finding("skills/federal/new.md", "k", "s"))
        self.assertEqual(report.finish(), 0)
        self.assertIn("baseline written: 2 fingerprint(s) (1 outside the scanned roots kept)", self.out.getvalue())
        self.assertEqual(
            findings.load_baseline(self.baseline),
            {"skills/federal/new.md::k", "skills/international/i.md::k"},
        )

    def test_checker_without_roots_covers_the_whole_baseline(self) -> None:
        findings.write_baseline(self.baseline, "demo", [Finding("docs/COVERAGE.md", "row", "s")])
        args = _args(baseline=self.baseline)
        del args.roots
        report = Report("demo", args, out=self.out)
        self.assertEqual(report.finish(), 1)
        self.assertIn("    docs/COVERAGE.md::row", self.out.getvalue())

    def test_load_baseline_skips_comments_and_blank_lines(self) -> None:
        Path(self.baseline).write_text("# header\n\na.md::k\n  \n# trailing\nb.md::k\n", encoding="utf-8")
        self.assertEqual(findings.load_baseline(self.baseline), {"a.md::k", "b.md::k"})
        self.assertIsNone(findings.load_baseline(self.baseline + ".missing"))

    def test_json_document(self) -> None:
        findings.write_baseline(self.baseline, "demo", [
            Finding("skills/a.md", "known", "s"), Finding("skills/z.md", "gone", "s"),
        ])
        report = self._report(json=True)
        report.note("scanned 2 files")
        report.add(Finding("skills/a.md", "known", "old", line=1, detail={"v": 1}))
        report.add(Finding("skills/b.md", "fresh", "new", line=2))
        self.assertEqual(report.finish(), 1)
        document = json.loads(self.out.getvalue())
        self.assertEqual(document["checker"], "demo")
        self.assertFalse(document["ok"])
        self.assertEqual(document["counts"], {"findings": 2, "new": 1, "known": 1, "stale_baseline": 1})
        self.assertEqual(document["notes"], ["scanned 2 files"])
        self.assertEqual(document["stale_baseline"], ["skills/z.md::gone"])
        self.assertEqual([f["new"] for f in document["findings"]], [False, True])
        self.assertEqual(document["findings"][0]["detail"], {"v": 1})
        self.assertEqual(document["roots"], ["skills"])
        self.assertTrue(document["baseline"].endswith("demo.txt"))
        self.assertNotIn("gate:", self.out.getvalue())

    def test_json_update_baseline_reports_what_it_wrote(self) -> None:
        report = self._report(json=True, update_baseline=True)
        report.add(Finding("a.md", "k", "s"))
        self.assertEqual(report.finish(), 0)
        self.assertEqual(json.loads(self.out.getvalue())["written"], 1)


if __name__ == "__main__":
    unittest.main()
