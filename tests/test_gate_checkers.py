"""The six gate checkers, driven over throwaway corpora.

Each checker is run as CI runs it, as a subprocess from the corpus root (the
checkers resolve `skills/` against the working directory), with an explicit
`--baseline` inside the corpus so the repository's own baselines stay out of
the picture. What is pinned: a planted defect is a finding with the documented
path, key and detail; `--json` describes it; `--update-baseline` records it
and the next run passes; fixing it makes the baseline entry stale and fails
the gate until the baseline is regenerated; a clean corpus passes.
"""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from oa_tools import roster  # noqa: E402

GUIDE_HEAD = "---\nname: {name}\njurisdiction: ZZ\ntier: 2\nlast_updated: 2026-01-02\n---\n\n# {name}\n\n"


def guide(name: str, body: str) -> str:
    return GUIDE_HEAD.format(name=name) + body


class GateCheckerMixin:
    """The corpus fixture and the shared scenarios; concrete cases set ``script``."""

    script = ""

    def setUp(self) -> None:
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        self.baseline = self.root / "baseline.txt"

    def write(self, files: dict[str, str]) -> None:
        for rel, text in files.items():
            path = self.root / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")

    def run_checker(self, *args: str, baseline: bool = True) -> subprocess.CompletedProcess:
        argv = [sys.executable, "-X", "utf8", str(SCRIPTS / self.script), *args]
        if baseline:
            argv += ["--baseline", str(self.baseline)]
        return subprocess.run(argv, cwd=self.root, capture_output=True, text=True, encoding="utf-8", timeout=120)

    def run_json(self, *args: str, baseline: bool = True) -> tuple[int, dict]:
        result = self.run_checker("--json", *args, baseline=baseline)
        self.assertEqual(result.stderr, "", result.stderr)
        return result.returncode, json.loads(result.stdout)

    # Shared scenarios, parameterised by one planted defect per checker.

    def assert_gate_lifecycle(self, planted: dict[str, str], fixed: dict[str, str], path: str, key_part: str) -> None:
        """Planted defect fails; recording it passes; fixing it goes stale; regenerating passes."""
        self.write(planted)
        code, document = self.run_json()
        self.assertEqual(code, 1, document)
        self.assertFalse(document["ok"])
        self.assertIsNone(document["baseline"])
        self.assertEqual(document["counts"]["findings"], 1, document)
        finding = document["findings"][0]
        self.assertEqual(finding["path"], path)
        self.assertIn(key_part, finding["key"])
        self.assertTrue(finding["new"])
        fingerprint = finding["fingerprint"]

        text = self.run_checker()
        self.assertEqual(text.returncode, 1, text.stderr)
        self.assertIn("gate: FAIL", text.stdout)
        self.assertIn("no baseline", text.stdout)

        recorded = self.run_checker("--update-baseline")
        self.assertEqual(recorded.returncode, 0, recorded.stderr)
        self.assertIn("baseline written: 1 fingerprint(s)", recorded.stdout)
        self.assertIn(fingerprint, self.baseline.read_text(encoding="utf-8").splitlines())

        code, document = self.run_json()
        self.assertEqual(code, 0, document)
        self.assertEqual(document["counts"], {"findings": 1, "new": 0, "known": 1, "stale_baseline": 0})
        self.assertEqual(self.run_checker(baseline=False, *["--no-baseline"]).returncode, 1)

        self.write(fixed)
        code, document = self.run_json()
        self.assertEqual(code, 1, document)
        self.assertEqual(document["counts"]["findings"], 0)
        self.assertEqual(document["stale_baseline"], [fingerprint])
        text = self.run_checker()
        self.assertIn("no longer reproduce", text.stdout)

        self.assertEqual(self.run_checker("--update-baseline").returncode, 0)
        self.assertEqual(self.run_checker().returncode, 0)

    def test_help_documents_the_gate_flags(self) -> None:
        result = self.run_checker("--help", baseline=False)
        self.assertEqual(result.returncode, 0, result.stderr)
        for flag in ("--json", "--baseline", "--no-baseline", "--update-baseline"):
            self.assertIn(flag, result.stdout)


class ArithmeticGateTests(GateCheckerMixin, unittest.TestCase):
    script = "check-arithmetic.py"

    def test_lifecycle_of_a_wrong_sum(self) -> None:
        wrong = {"skills/international/zz/zz-vat.md": guide("zz-vat", "- Tax due: 100 x 10% = 20\n")}
        right = {"skills/international/zz/zz-vat.md": guide("zz-vat", "- Tax due: 100 x 10% = 10\n")}
        self.assert_gate_lifecycle(wrong, right, "skills/international/zz/zz-vat.md", "100 x 10% = 20")

    def test_scoped_runs_and_root_spellings_agree_with_the_baseline(self) -> None:
        """Qodo's three findings on the first cut, as one scenario: record two
        directories, then scan one of them, spell the root differently, and
        update the baseline from the scoped run."""
        self.write({
            "skills/federal/f.md": guide("f", "- Tax: 100 x 10% = 20\n"),
            "skills/international/zz/i.md": guide("i", "- Tax: 200 x 10% = 30\n"),
        })
        self.assertEqual(self.run_checker("--update-baseline").returncode, 0)
        recorded = set(self.baseline.read_text(encoding="utf-8").splitlines()) - set()
        self.assertIn("skills/federal/f.md::100 x 10% = 20", recorded)
        self.assertIn("skills/international/zz/i.md::200 x 10% = 30", recorded)

        for root in ("skills/federal", "./skills/federal", "skills/../skills/federal/"):
            code, document = self.run_json(root)
            self.assertEqual(code, 0, (root, document))
            self.assertEqual(document["counts"], {"findings": 1, "new": 0, "known": 1, "stale_baseline": 0}, root)
            self.assertEqual(document["findings"][0]["path"], "skills/federal/f.md", root)
        code, document = self.run_json("./skills")
        self.assertEqual(code, 0, document)
        self.assertEqual(document["counts"]["known"], 2)

        self.write({"skills/federal/f.md": guide("f", "- Tax: 100 x 10% = 10\n")})
        code, document = self.run_json("skills/federal")
        self.assertEqual(code, 1)
        self.assertEqual(document["stale_baseline"], ["skills/federal/f.md::100 x 10% = 20"])
        update = self.run_checker("skills/federal", "--update-baseline")
        self.assertEqual(update.returncode, 0, update.stderr)
        self.assertIn("(1 outside the scanned roots kept)", update.stdout)
        self.assertEqual(
            [line for line in self.baseline.read_text(encoding="utf-8").splitlines() if not line.startswith("#")],
            ["skills/international/zz/i.md::200 x 10% = 30"],
        )
        self.assertEqual(self.run_checker().returncode, 0, "the full-tree gate still passes")

    def test_a_misspelled_root_is_an_error_and_touches_nothing(self) -> None:
        self.write({"skills/federal/f.md": guide("f", "- Tax: 100 x 10% = 20\n")})
        self.assertEqual(self.run_checker("--update-baseline").returncode, 0)
        before = self.baseline.read_text(encoding="utf-8")
        for args in (("skills/fedral",), ("skills", "nowhere"), ("skills/fedral", "--update-baseline"), ("skills/fedral", "--json")):
            with self.subTest(args=args):
                result = self.run_checker(*args)
                self.assertNotEqual(result.returncode, 0, args)
                self.assertIn("not a directory", result.stderr)
                self.assertNotIn("gate: PASS", result.stdout)
                self.assertEqual(result.stdout, "", "nothing is scanned or reported")
        self.assertEqual(self.baseline.read_text(encoding="utf-8"), before, "the baseline was not rewritten")

    def test_finding_detail_and_correct_arithmetic(self) -> None:
        self.write({"skills/international/zz/zz-vat.md": guide("zz-vat", "- Tax due: 100 x 10% = 20\n- Ok: 100 x 10% = 10\n")})
        code, document = self.run_json()
        self.assertEqual(code, 1)
        finding = document["findings"][0]
        self.assertEqual(finding["line"], 10)
        self.assertEqual(finding["detail"], {"expression": "100 x 10% = 20", "values": [10.0, 20.0]})
        self.assertIn("expressions evaluated: 2", document["notes"])


class BracketTablesGateTests(GateCheckerMixin, unittest.TestCase):
    script = "check-bracket-tables.py"

    TABLE = (
        "| Taxable income | Rate |\n"
        "|---|---|\n"
        "| 0 - 10,000 | 10% |\n"
        "| 10,001 - 20,000 | 20% |\n"
        "| 20,001 - 30,000 | {third} |\n"
        "| over 30,000 | 30% |\n"
    )

    def test_lifecycle_of_a_repeated_rate(self) -> None:
        path = "skills/international/zz/zz-income-tax.md"
        self.assert_gate_lifecycle(
            {path: guide("zz-income-tax", self.TABLE.format(third="20%"))},
            {path: guide("zz-income-tax", self.TABLE.format(third="25%"))},
            path, "| 10,001 - 20,000 | 20% | / | 20,001 - 30,000 | 20% |",
        )

    def test_finding_detail(self) -> None:
        self.write({"skills/international/zz/zz-income-tax.md": guide("zz-income-tax", self.TABLE.format(third="20%"))})
        code, document = self.run_json()
        self.assertEqual(code, 1)
        detail = document["findings"][0]["detail"]
        self.assertEqual(detail["header"], "Taxable income")
        self.assertEqual(detail["rows"], ["| 10,001 - 20,000 | 20% |", "| 20,001 - 30,000 | 20% |"])
        text = self.run_checker().stdout
        self.assertIn("under: Taxable income", text)
        self.assertIn("adjacent same-rate band pairs: 1", text)

    CUMULATIVE = (
        "| Taxable income | Tax |\n"
        "|---|---|\n"
        "| 0 - 10,000 | 10% |\n"
        "| 10,001 - 20,000 | 1,000 + 20% of excess over 10,000 |\n"
        "| over 20,000 | {fixed} + 30% of excess over 20,000 |\n"
    )

    def test_lifecycle_of_a_cumulative_amount(self) -> None:
        path = "skills/international/zz/zz-income-tax.md"
        self.assert_gate_lifecycle(
            {path: guide("zz-income-tax", self.CUMULATIVE.format(fixed="3,500"))},
            {path: guide("zz-income-tax", self.CUMULATIVE.format(fixed="3,000"))},
            path, "cumulative: | 10,001 - 20,000 | 1,000 + 20% of excess over 10,000 | / | over 20,000 | 3,500 + 30% of excess over 20,000 |",
        )

    def test_cumulative_detail_and_a_band_written_another_way(self) -> None:
        self.write({"skills/international/zz/zz-income-tax.md": guide("zz-income-tax", self.CUMULATIVE.format(fixed="3,500"))})
        code, document = self.run_json()
        self.assertEqual(code, 1)
        detail = document["findings"][0]["detail"]
        self.assertEqual((detail["stated"], detail["expected"]), (3500.0, 3000.0))
        self.assertEqual(detail["rows"][1], "| over 20,000 | 3,500 + 30% of excess over 20,000 |")
        text = self.run_checker().stdout
        self.assertIn("stated 3500, expected 3000 from the previous band", text)
        self.assertIn("cumulative amount mismatches: 1", text)
        # A band written as a flat percentage between two cumulative rows is not bridged.
        self.write({"skills/international/zz/zz-stamp-duty.md": guide(
            "zz-stamp-duty",
            "| Dutiable value | Duty |\n"
            "|---|---|\n"
            "| 0 - 25,000 | 1.4% of the value |\n"
            "| 25,001 - 130,000 | 350 + 2.4% over 25,000 |\n"
            "| 130,001 - 960,000 | 5.5% of the whole value |\n"
            "| over 960,000 | 52,800 + 6.5% over 960,000 |\n",
        )})
        code, document = self.run_json()
        self.assertEqual([f["path"] for f in document["findings"]], ["skills/international/zz/zz-income-tax.md"])


    def test_a_changed_preceding_band_is_a_new_finding(self) -> None:
        # The fingerprint carries both rows: a baseline that accepted one
        # mismatch does not accept the different mismatch that appears when
        # the band above changes while the failing row stays as it was.
        path = "skills/international/zz/zz-income-tax.md"
        self.write({path: guide("zz-income-tax", self.CUMULATIVE.format(fixed="3,500"))})
        self.assertEqual(self.run_checker("--update-baseline").returncode, 0)
        self.assertEqual(self.run_checker().returncode, 0)
        self.write({path: guide("zz-income-tax", self.CUMULATIVE.format(fixed="3,500").replace("1,000 + 20%", "1,000 + 15%"))})
        code, document = self.run_json()
        self.assertEqual(code, 1, document)
        self.assertEqual(document["counts"]["new"], 1, document)
        self.assertEqual(len(document["stale_baseline"]), 1)
        self.assertEqual(document["findings"][0]["detail"]["expected"], 2500.0)


class SourcingFloorGateTests(GateCheckerMixin, unittest.TestCase):
    script = "check-sourcing-floor.py"

    TABLE = (
        "| Taxable income | Rate |\n"
        "|---|---|\n"
        "| 0 - 10,000 | 10% |\n"
        "| 10,001 - 20,000 | 20% |\n"
        "| over 20,000 | 30% |\n"
        "\nSource: {source}\n"
    )

    TABLE_KEY = ("rate table without a tax-authority or statute citation: "
                 "| Taxable income | Rate | / | 0 - 10,000 | 10% |")
    SECOND_TABLE = (
        "| Contribution | Employee | Employer |\n"
        "|---|---|---|\n"
        "| Pension | 6% | 12% |\n"
        "| Health | 2% | 4% |\n"
        "| Unemployment | 1% | 1% |\n"
    )

    def test_lifecycle_of_a_table_without_an_authority(self) -> None:
        path = "skills/international/zz/zz-income-tax.md"
        self.assert_gate_lifecycle(
            {path: guide("zz-income-tax", self.TABLE.format(source="https://taxsummaries.pwc.com/zz"))},
            {path: guide("zz-income-tax", self.TABLE.format(source="https://taxsummaries.pwc.com/zz and https://www.zz.gov/rates"))},
            path, self.TABLE_KEY,
        )

    def test_a_second_unsourced_table_is_a_new_finding(self) -> None:
        # One finding per table, keyed on its rows: a table added to a guide
        # already in the queue is not covered by the guide's existing entry.
        path = "skills/international/zz/zz-income-tax.md"
        self.write({path: guide("zz-income-tax", self.TABLE.format(source="https://taxsummaries.pwc.com/zz"))})
        self.assertEqual(self.run_checker("--update-baseline").returncode, 0)
        self.assertEqual(self.run_checker().returncode, 0)
        self.write({path: guide("zz-income-tax", self.SECOND_TABLE + "\n" + self.TABLE.format(source="https://taxsummaries.pwc.com/zz"))})
        code, document = self.run_json()
        self.assertEqual(code, 1, document)
        self.assertEqual(document["counts"]["new"], 1, document)
        self.assertEqual(document["stale_baseline"], [])
        new = [f for f in document["findings"] if f["new"]][0]
        self.assertEqual(new["detail"]["rows"], ["| Contribution | Employee | Employer |", "| Pension | 6% | 12% |"])
        # one authority link clears both tables: two stale entries, nothing new
        self.assertEqual(self.run_checker("--update-baseline").returncode, 0)
        self.write({path: guide("zz-income-tax", self.SECOND_TABLE + "\n" + self.TABLE.format(source="https://www.zz.gov/rates"))})
        code, document = self.run_json()
        self.assertEqual((code, document["counts"]["new"], len(document["stale_baseline"])), (1, 0, 2), document)

    def test_what_clears_the_floor_and_what_is_not_a_rate_table(self) -> None:
        self.write({
            # a statute republisher clears it, like an authority
            "skills/federal/zz-a.md": guide("zz-a", self.TABLE.format(source="https://www.law.cornell.edu/uscode/text/26/1")),
            # an allowlisted authority on a bare national domain clears it
            "skills/international/zz/zz-b.md": guide("zz-b", self.TABLE.format(source="https://emta.ee/x")),
            # a quick-reference table with a rate on three of eight rows is not a rate table
            "skills/international/zz/zz-c.md": guide("zz-c", (
                "| Field | Value |\n|---|---|\n| Country | ZZ |\n| Currency | ZZD |\n| VAT | 20% |\n"
                "| CIT | 25% |\n| WHT | 15% |\n| Filing | 31 March |\n| Portal | e-tax |\n| Authority | ZRA |\n"
                "\nSource: https://taxsummaries.pwc.com/zz\n")),
            # the corpus's own links are not sources, so this one has no sources at all
            "skills/international/zz/zz-d.md": guide("zz-d", self.TABLE.format(source="https://www.openaccountants.com/connect")),
            # file templates and platform guides are skipped
            "skills/templates/zz-e.md": guide("zz-e", self.TABLE.format(source="https://taxsummaries.pwc.com/zz")),
            # a bullet-form schedule is a rate list, and a publisher is not an authority
            "skills/international/zz/zz-f.md": guide("zz-f", (
                "- **Income up to 12,000** — 0%  _(https://taxsummaries.pwc.com/zz)_\n"
                "- **Income 12,001–30,000** — 10%  _(https://taxsummaries.pwc.com/zz)_\n"
                "- **Income above 30,000** — 20%  _(https://taxsummaries.pwc.com/zz)_\n"
                "- **Filing deadline** — 31 March  _(https://taxsummaries.pwc.com/zz)_\n")),
            # three rates among twelve bullets are not a schedule
            "skills/international/zz/zz-g.md": guide("zz-g", "".join(
                "- **Fact %d** — %s  _(https://taxsummaries.pwc.com/zz)_\n" % (n, "10%" if n < 3 else "text")
                for n in range(12))),
            # a government label inside someone else's domain is not a government host
            "skills/international/zz/zz-h.md": guide("zz-h", self.TABLE.format(source="https://irs.gov.example.com/rates")),
            # percentages in the label or the prose are not rates: business advice, worked arithmetic
            "skills/verticals/zz-i.md": guide("zz-i", (
                "- **>50% from one platform:** vulnerable to algorithm changes — diversify\n"
                "- **>50% from sponsorships:** vulnerable to budget cycles — build owned revenue\n"
                "- **>50% from one client:** possible worker-classification issues — diversify\n"
                "- Employer contribution 1.5% × 300,000 = 4,500\n"
                "- Employee contribution 1.0% × 300,000 = 3,000\n"
                "- Net pay = 300,000 − 3,000 − 30,000 = 267,000\n")),
        })
        code, document = self.run_json()
        self.assertEqual(code, 1, document)
        self.assertEqual([f["path"] for f in document["findings"]],
                         ["skills/international/zz/zz-d.md", "skills/international/zz/zz-f.md",
                          "skills/international/zz/zz-h.md"])
        self.assertEqual(document["findings"][0]["detail"],
                         {"kind": "table", "rows": ["| Taxable income | Rate |", "| 0 - 10,000 | 10% |"], "hosts": []})
        self.assertEqual(document["findings"][1]["detail"], {
            "kind": "list",
            "rows": ["- **Income up to 12,000** — 0%  _(https://taxsummaries.pwc.com/zz)_",
                     "- **Income 12,001–30,000** — 10%  _(https://taxsummaries.pwc.com/zz)_"],
            "hosts": ["taxsummaries.pwc.com"]})
        self.assertEqual(document["findings"][2]["detail"]["hosts"], ["irs.gov.example.com"])
        text = self.run_checker().stdout
        self.assertIn("rate table without a tax-authority or statute citation (| Taxable income | Rate |); "
                      "the guide cites 0 host(s), none a tax authority or statute", text)
        self.assertIn("the guide cites 1 host(s), none a tax authority or statute: taxsummaries.pwc.com", text)
        self.assertIn("guides scanned: 8; with a rate table or list: 5; "
                      "without an authority or statute citation: 3 (3 table(s) or list(s))", text)

    def test_which_bullets_are_rate_lines(self) -> None:
        spec = importlib.util.spec_from_file_location("check_sourcing_floor", SCRIPTS / "check-sourcing-floor.py")
        module = importlib.util.module_from_spec(spec)
        assert spec.loader is not None
        spec.loader.exec_module(module)
        rate_line = module.rate_line
        for line in ("- **Standard rate** — 20%  _(Act s 5)_",
                     "- **Reduced rate** — 5% (food, books)",
                     "- 10% on the first 1,000",
                     "- Dividends: 0% if the beneficial owner holds at least 10% of the capital; 5% otherwise",
                     "* Income TOP 12,001-30,000 -- 10%",
                     "- **Standard rate** — 10%  _(Income Tax Act 1970 (https://www.gov.im/x))_"):
            self.assertTrue(rate_line(line), line)
        for line in ("- **>50% from one platform:** vulnerable to algorithm changes — diversify",
                     "- Employer contribution 1.5% × 300,000 = 4,500",
                     "- The standard rate of 20% applies to most supplies of goods and services",
                     "- **Filing deadline** — 31 March",
                     "- [ ] Flat rate of 4.95% applied (not a graduated rate)"):
            self.assertFalse(rate_line(line), line)


class ExpiredRulesGateTests(GateCheckerMixin, unittest.TestCase):
    script = "check-expired-rules.py"

    def test_lifecycle_of_an_expired_rule(self) -> None:
        path = "skills/international/zz/zz-payroll.md"
        self.assert_gate_lifecycle(
            {path: guide("zz-payroll", "Apply the 2020 constants until the 2021 figures are published.\n")},
            {path: guide("zz-payroll", "Apply the 2021 constants (published 20 January 2021).\n")},
            path, "until the 2021 figures are published",
        )

    def test_waited_on_year_and_a_future_rule_is_not_expired(self) -> None:
        self.write({"skills/international/zz/zz-payroll.md": guide(
            "zz-payroll",
            "Apply the 2020 constants until the 2021 figures are published.\n"
            "Apply the 2098 constants until the 2099 figures are published.\n",
        )})
        code, document = self.run_json()
        self.assertEqual(code, 1)
        self.assertEqual(document["counts"]["findings"], 1)
        self.assertEqual(document["findings"][0]["detail"], {"waited_on": 2021})
        self.assertEqual(document["findings"][0]["line"], 10)

    def test_selftest_still_runs(self) -> None:
        result = self.run_checker("--selftest", baseline=False)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("selftest:", result.stdout)


class FactConflictsGateTests(GateCheckerMixin, unittest.TestCase):
    script = "check-fact-conflicts.py"

    def test_lifecycle_of_a_conflict_inside_one_pack(self) -> None:
        overview = "skills/international/zz/zz-overview.md"
        vat = "skills/international/zz/zz-vat.md"
        self.assert_gate_lifecycle(
            {overview: guide("zz-overview", "- **Standard rate** - 20%\n"), vat: guide("zz-vat", "| Standard rate | 21% |\n")},
            {overview: guide("zz-overview", "- **Standard rate** - 21%\n"), vat: guide("zz-vat", "| Standard rate | 21% |\n")},
            "skills/international/zz", "standard",
        )

    def test_detail_lists_every_site_and_a_single_file_never_conflicts_with_itself(self) -> None:
        self.write({
            "skills/international/zz/zz-overview.md": guide("zz-overview", "- **Standard rate** - 20%\n- **Standard rate** - 22%\n"),
            "skills/international/zz/zz-vat.md": guide("zz-vat", "| Standard rate | 21% |\n"),
            "skills/international/yy/yy-vat.md": guide("yy-vat", "- **Standard rate** - 5%\n- **Standard rate** - 7%\n"),
        })
        code, document = self.run_json()
        self.assertEqual(code, 1)
        self.assertEqual(document["counts"]["findings"], 1, "yy disagrees only with itself")
        finding = document["findings"][0]
        self.assertEqual(finding["path"], "skills/international/zz")
        self.assertEqual(finding["key"], "standard")
        self.assertEqual(finding["detail"]["values"], [20.0, 21.0, 22.0])
        self.assertEqual({site["path"] for site in finding["detail"]["sites"]},
                         {"skills/international/zz/zz-overview.md", "skills/international/zz/zz-vat.md"})
        self.assertIn("keys where files disagree: 1", "\n".join(document["notes"]))


class CoverageClaimsGateTests(GateCheckerMixin, unittest.TestCase):
    script = "check-coverage-claims.py"

    INDEX = {
        "counts": {"guides": 2, "jurisdictions": 2, "accountant_reviewed": 1},
        "guides": [
            {"slug": "zz-vat", "path": "skills/international/zz/zz-vat.md", "name": "zz-vat", "jurisdiction": "ZZ",
             "tier": 1, "verified_by": None, "reviewed_by": "Jane Doe, CPA", "tax_year": 2026, "last_updated": "2026-01-02"},
            {"slug": "ca-income-tax", "path": "skills/us-states/ca/ca-income-tax.md", "name": "ca-income-tax",
             "jurisdiction": "US-CA", "tier": 2, "verified_by": None, "reviewed_by": None, "tax_year": 2026,
             "last_updated": "2026-01-02"},
        ],
    }
    ROWS = [
        ("Guide files indexed", 2),
        ("Distinct `jurisdiction` codes", 2),
        ("`tier: 1` (accountant-reviewed)", 1),
        ("`tier: 2` (source-cited draft)", 1),
        ("Distinct `reviewed_by` values", 1),
        ("Country directories under `skills/international/`", 1),
        ("US jurisdiction codes (`US` + 50 states + DC)", 1),
        ("Generated bundles under `packages/`", 1),
    ]

    PROFILES = {"reviewers": {"Jane Doe, CPA": {"public_record": "https://example.test/jane"}}}

    def corpus(self, **overrides) -> dict[str, str]:
        rows = []
        for label, value in self.ROWS:
            value = overrides.get(label, value)
            suffix = " (1 people)" if label.startswith("Distinct `reviewed_by`") else ""
            rows.append(f"| {label} | **{value}**{suffix} |")
        coverage = (
            "# Coverage\n\n## This repository (derived from `index.json`)\n\n"
            "| Measure | This tree |\n|---|---|\n" + "\n".join(rows) + "\n\n## Upstream\n\nFrozen.\n"
        )
        correct = "**2 Guides** across **2 jurisdictions** · **1 accountant-reviewed** · **1 named accountants**"
        partners, _ = roster.render_partners(self.INDEX, self.PROFILES["reviewers"])
        return {
            "index.json": json.dumps(self.INDEX),
            "docs/COVERAGE.md": coverage,
            # the headline line sits under prose that also says "Guides" and
            # "accountant-reviewed", as it does in the real files
            "README.md": "# Repo\n\nTax Guides, some accountant-reviewed.\n\n" + overrides.get("headline", correct) + "\n",
            "llms.txt": "# Repo\n\n" + overrides.get("llms", correct) + "\n",
            "docs/QUALITY-TIERS.md": "# Tiers\n\n## Current inventory\n\n" + overrides.get("tiers", correct) + "\n",
            "docs/partners.json": json.dumps(self.PROFILES),
            "PARTNERS.md": partners,
            "skills/international/zz/zz-vat.md": guide("zz-vat", "Body.\n"),
            "packages/zz/zz-vat.md": guide("zz-vat", "Body.\n"),
        }

    def test_lifecycle_of_a_drifted_row(self) -> None:
        self.assert_gate_lifecycle(
            self.corpus(**{"Guide files indexed": 3}), self.corpus(), "docs/COVERAGE.md", "Guide files indexed",
        )

    def test_matching_claims_pass_without_any_baseline(self) -> None:
        self.write(self.corpus())
        code, document = self.run_json(baseline=False)
        self.assertEqual(code, 0, document)
        self.assertEqual(document["counts"]["findings"], 0)
        self.assertIn("claims disagreeing with the tree: 0", document["notes"])

    def test_every_headline_file_is_checked_by_the_bold_figures(self) -> None:
        self.write(self.corpus(
            llms="**5 Guides** across **2 jurisdictions** · **1 accountant-reviewed** · **1 named accountants**",
            tiers="No figures here, only the words Guides and accountant-reviewed.",
        ))
        code, document = self.run_json(baseline=False)
        self.assertEqual(code, 1)
        keys = {(f["path"], f["key"]) for f in document["findings"]}
        self.assertEqual(keys, {("llms.txt", "Guides"), ("docs/QUALITY-TIERS.md", "headline")})

    def test_a_hand_edited_roster_and_a_ghost_profile_are_findings(self) -> None:
        files = self.corpus()
        files["PARTNERS.md"] = files["PARTNERS.md"].replace("| Jane Doe, CPA |", "| Jane Doe, CPA (edited) |")
        files["docs/partners.json"] = json.dumps({"reviewers": {
            **self.PROFILES["reviewers"], "Ghost": {"public_record": "https://example.test/ghost"},
        }})
        self.write(files)
        code, document = self.run_json(baseline=False)
        self.assertEqual(code, 1)
        keys = {(f["path"], f["key"]) for f in document["findings"]}
        self.assertEqual(keys, {("PARTNERS.md", "stale"), ("docs/partners.json", "Ghost")})

    def test_headline_and_row_drift_are_separate_findings(self) -> None:
        self.write(self.corpus(**{
            "`tier: 1` (accountant-reviewed)": 5,
            "headline": "**9 Guides** across **2 jurisdictions** · **1 accountant-reviewed** · **1 named accountants**",
        }))
        code, document = self.run_json(baseline=False)
        self.assertEqual(code, 1)
        by_path = {(f["path"], f["key"]): f["detail"] for f in document["findings"]}
        self.assertEqual(by_path[("docs/COVERAGE.md", "`tier: 1` (accountant-reviewed)")], {"claimed": 5, "actual": 1})
        self.assertEqual(by_path[("README.md", "Guides")], {"claimed": 9, "actual": 2})
        self.assertEqual(len(by_path), 2)

    def test_missing_doc_is_a_finding(self) -> None:
        files = self.corpus()
        del files["docs/COVERAGE.md"]
        self.write(files)
        code, document = self.run_json(baseline=False)
        self.assertEqual(code, 1)
        self.assertEqual(document["findings"][0]["key"], "missing")


if __name__ == "__main__":
    unittest.main()
