"""Pin Australian guide facts against the primary sources they were checked with.

Each test finds one line of a source guide by a marker that must occur exactly
once, splits it into sentences and requires a single sentence to carry every
part of the fact, so an unrelated sentence on the same line cannot satisfy it.
Sources were read on 11 November 2026 and are named above each test. Read the
source guides only: generated packages are rebuilt from them.
"""

from decimal import Decimal
from pathlib import Path
import re
import unittest


SKILLS = Path(__file__).resolve().parents[1] / "skills"
AU = SKILLS / "international" / "australia"
ORCHESTRATOR = SKILLS / "orchestrator"

# A sentence ends at a full stop, semicolon or table cell boundary followed by
# space; decimals such as 8.27% and $1.3m contain no space after the point.
SENTENCE_END = re.compile(r"(?<=[.;|])\s+")


def guide_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def marked_line(test: unittest.TestCase, path: Path, marker: str) -> str:
    lines = [line for line in guide_text(path).splitlines() if marker in line]
    test.assertEqual(len(lines), 1, f"{path.name}: expected one line with {marker!r}")
    return lines[0]


def sentences(text: str) -> list[str]:
    return [part for part in SENTENCE_END.split(" ".join(text.split())) if part]


def assert_sentence(test: unittest.TestCase, text: str, *patterns: str) -> re.Match:
    """Require one sentence to match every pattern; return the first pattern's match."""
    for sentence in sentences(text):
        matches = [re.search(pattern, sentence) for pattern in patterns]
        if all(matches):
            return matches[0]
    test.fail(f"no single sentence matches all of {patterns!r}")


class FixedAustralianFactsTest(unittest.TestCase):
    """Facts corrected to agree with their primary sources."""

    def test_bas_preparation_rcti_controls(self) -> None:
        # GSTR 2000/10W notice of withdrawal (28 July 2026) paras 2-3; draft GSTR 2026/D2;
        # A New Tax System (Goods and Services Tax): Recipient Created Tax Invoice
        # Determination 2023 (F2023L00785) ss 6-9; ATO, Tax invoices.
        text = guide_text(AU / "au-bas-preparation.md")
        section = text.split("#### 3.1 Invoice population and evidence register", 1)
        self.assertEqual(len(section), 2, "the invoice evidence register section is missing")
        body = section[1].split("### Section 4", 1)[0]
        assert_sentence(self, body, r"GSTR 2000/10 was withdrawn on 29 July 2026", r"on or before 14 June 2023")
        assert_sentence(self, body, r"GSTR 2026/D2", r"\bdraft\b")
        assert_sentence(self, body, r"supplier and recipient must be GST registered", r"when the RCTI is issued")
        assert_sentence(self, body, r"s 6\(2\)", r"must determine the value of the supply")

    def test_queensland_deduction_phases_out(self) -> None:
        # Queensland Revenue Office, Deductions: $1 for every $7 over $1.3m, nil at $10.4m.
        line = marked_line(self, AU / "australia-payroll.md", "| QLD, current at ")
        match = assert_sentence(
            self, line, r"\$1 for every \$7 of Australian taxable wages above \$([\d.]+)m", r"nil at \$([\d.]+)m"
        )
        threshold = Decimal(match[1])
        nil_point = Decimal(re.search(r"nil at \$([\d.]+)m", line)[1])
        self.assertEqual(threshold, Decimal("1.3"))
        self.assertEqual(threshold + 7 * threshold, nil_point)

    def test_fbt_loan_benchmark_is_dated(self) -> None:
        # ATO, Fringe benefits tax rates and thresholds, Table 10.
        line = marked_line(self, AU / "au-fbt-year.md", "| Loans to employees")
        self.assertRegex(line, r"8\.62%[^;|%]*31 March 2026")
        self.assertRegex(line, r"8\.27%[^;|%]*31 March 2027")

    def test_digital_currency_exclusion_application_year(self) -> None:
        # Treasury Laws Amendment (2022 Measures No. 4) Act 2023 Sch 2 item 15(2).
        text = guide_text(AU / "au-forex-gains-losses.md")
        assert_sentence(self, text, r"s 995-1 excludes digital currency", r"income year that includes 1 July 2021", r"later income years")
        for sentence in sentences(text):
            if "s 995-1 excludes digital currency" in sentence:
                self.assertNotIn("starting on or after 1 July 2021", sentence)

    def test_bas_q2_date_rolls_past_wa_labour_day(self) -> None:
        # ATO, Lodgment and payment dates on weekends or public holidays, 2027 table:
        # 1 March (Mon) Labour Day (WA), first business day 2 March (Tue).
        line = marked_line(self, ORCHESTRATOR / "au-return-assembly.md", "BAS Q2 (Oct-Dec): lodge and pay by")
        assert_sentence(self, line, r"28 February 2027", r"Labour Day in WA", r"Tuesday 2 March 2027")
        self.assertNotIn("so Monday 1 March 2027", line)

    def test_sgc_clean_history_lookback(self) -> None:
        # Superannuation Guarantee (Administration) Regulations 2018 reg 13C(1) and (3),
        # compilation of 1 July 2026.
        for path, marker in (
            (AU / "au-super-guarantee.md", "**Redesigned SGC (QE days from 1 July 2026)**"),
            (AU / "australia-payroll.md", "**SGC redesign components**"),
        ):
            with self.subTest(guide=path.name):
                line = marked_line(self, path, marker)
                assert_sentence(self, line, r"clean 24-month", r"1 July 2026 to 30 June 2028", r"reg 13C\(3\)")
                self.assertNotRegex(line, r"clean 2-year")

    def test_g15_includes_non_deductible_purchases(self) -> None:
        # ATO, Step 4: calculating purchases using the calculation worksheet, G15.
        line = marked_line(self, AU / "australia-gst.md", "| G15 |")
        self.assertIn("private use or not income tax deductible", line)
        self.assertIn("G10 or G11", line)

    def test_help_repayment_income_nets_exempt_foreign_income(self) -> None:
        # Higher Education Support Act 2003 s 154-5(1), (4) and (5), compilation 105.
        for path, marker in (
            (AU / "au-individual-return.md", "- **Repayment income** "),
            (AU / "au-rates-2026-27.md", "- **Repayment income definition** "),
            (ORCHESTRATOR / "au-return-assembly.md", "**Check AU11 "),
        ):
            with self.subTest(guide=path.name):
                line = marked_line(self, path, marker)
                assert_sentence(
                    self,
                    line,
                    r"First Home Super Saver",
                    r"exempt foreign employment income \([^)]*non-capital losses and outgoings[^)]*not below zero\)",
                )


class DividendSubstitutionSharePlanTest(unittest.TestCase):
    """au-dssp, ported from upstream with its dangling 'Section 1' reference resolved."""

    def test_every_cited_section_exists(self) -> None:
        text = guide_text(AU / "au-dssp.md")
        headings = set(re.findall(r"^## Section (\d+)\b", text, flags=re.MULTILINE))
        cited = set(re.findall(r"\bSection (\d+)\b", text))
        self.assertIn("1", cited)
        self.assertEqual(cited - headings, set())

    def test_worked_example_reallocates_without_increasing_cost(self) -> None:
        # ATO, Guide to capital gains tax 2025 (NAT 4151-06.2025), Example 35, page 92.
        line = marked_line(self, AU / "au-dssp.md", "| Later parcel's first element |")
        match = re.search(r"\$([\d,]+) ÷ \((\d+) \+ (\d+)\) = \$([\d.]+)", line)
        self.assertIsNotNone(match, "the allocation must state cost, original and bonus shares and the result")
        cost, original, bonus, per_share = (Decimal(part.replace(",", "")) for part in match.groups())
        self.assertEqual((cost, original, bonus), (Decimal(300), Decimal(300), Decimal(300)))
        self.assertEqual(cost / (original + bonus), per_share)
        line = marked_line(self, AU / "au-dssp.md", "| Cost reconciliation, derived from those inputs |")
        parts = re.findall(r"(\d+) × \$([\d.]+) = \$([\d,]+)", line)
        self.assertEqual(len(parts), 2, "original and bonus shares each need a product")
        for quantity, price, amount in parts:
            self.assertEqual(Decimal(quantity) * Decimal(price), Decimal(amount.replace(",", "")))
        combined = Decimal(re.search(r"combined: \$([\d,]+)", line)[1].replace(",", ""))
        self.assertEqual(sum(Decimal(amount.replace(",", "")) for _, _, amount in parts), combined)
        self.assertEqual(combined, cost)


class PortedAustralianPinsTest(unittest.TestCase):
    """Upstream's Australian figure pins, adapted to where this fork states them."""

    def test_super_guarantee_rate_from_july_2025(self) -> None:
        # ATO, Super guarantee: 12.00% from 1 July 2025; 11.50% for 2024-25.
        line = marked_line(self, AU / "au-not-for-profit.md", "The general SG rate is 12% from 1 July 2025.")
        assert_sentence(self, line, r"12% from 1 July 2025")
        line = marked_line(self, AU / "australia-formation.md", "**R-AU-F4")
        assert_sentence(self, line, r"general SG rate is 12% \(11\.5% for 2024-25\)")

    def test_cents_per_km_rates_and_caps(self) -> None:
        # ATO, Cents per kilometre method: 91c for 2026-27, 88c for 2025-26, 5,000 km.
        line = marked_line(self, AU / "australia-tax-optimization.md", "**Cents-per-km alternative**")
        expected = {"2026-27": (Decimal("91"), Decimal("4550")), "2025-26": (Decimal("88"), Decimal("4400"))}
        for year, (rate, cap) in expected.items():
            with self.subTest(year=year):
                match = assert_sentence(self, line, rf"For {year}[^:]*: ([\d.]+)c/km", r"max(?: 5,000 business km =)? \$([\d,]+)")
                self.assertEqual(Decimal(match[1]), rate)
                stated_cap = Decimal(re.search(rf"For {year}[^.]*?\$([\d,]+)", line)[1].replace(",", ""))
                self.assertEqual(stated_cap, cap)
                self.assertEqual(Decimal(5000) * rate / 100, cap)

    def test_act_and_nt_payroll_tax_2026_27(self) -> None:
        # ACT Revenue Office, About payroll tax, Table 1; NT Treasury, Payroll tax rates and thresholds.
        act = marked_line(self, AU / "australia-payroll.md", "| ACT, 2026-27 |")
        self.assertIn("| $1,750,000 |", act)
        self.assertRegex(act, r"up to \$20m, 6\.75%.*over \$150m, 8\.75%")
        nt = marked_line(self, AU / "australia-payroll.md", "| NT, 2026-27 |")
        self.assertIn("| $2,500,000 |", nt)
        self.assertRegex(nt, r"6\.5% for employers or groups with Australia-wide wages of at least \$100m; 5\.5% otherwise")
        card = marked_line(self, AU / "au-rates-2026-27.md", "| Other states |")
        self.assertIn("ACT 6.75% to 8.75% tiered/$1.75m", card)
        self.assertIn("NT 5.5% (6.5% at $100m+)/$2.5m", card)

    def test_2026_27_resident_rate_and_thresholds(self) -> None:
        # ATO, Tax rates - Australian residents 2026-27; ATO, MLS income thresholds and rates
        # 2026-27; ATO, How we calculate your PAYG instalment amount or rate; Crimes (Amount of
        # a Penalty Unit) Instrument 2026 (F2026N00424) s 5.
        band = marked_line(self, AU / "au-rates-2026-27.md", "| $18,201 -- $45,000 |")
        match = re.search(r"\| \$([\d,]+) -- \$([\d,]+) \| ([\d.]+)% \| \*\*([\d.]+)%\*\* \|", band)
        self.assertIsNotNone(match, "the band must give its bounds and both years' rates")
        low, high, _, rate = (Decimal(part.replace(",", "")) for part in match.groups())
        self.assertEqual(rate, Decimal(15))
        totals = marked_line(self, AU / "au-rates-2026-27.md", "**Tax on full bands and rate change:**")
        tax_at_top = Decimal(re.search(r"2026-27: \$([\d,]+) /", totals)[1].replace(",", ""))
        self.assertEqual((high - (low - 1)) * rate / 100, tax_at_top)
        single = marked_line(self, AU / "au-rates-2026-27.md", "| MLS tiers (single) |")
        self.assertIn("Base $105,000 or less", single)
        family = marked_line(self, AU / "au-rates-2026-27.md", "| MLS tiers (family) |")
        self.assertIn("Base $210,000 or less", family)
        gdp = marked_line(self, AU / "au-payg-instalments.md", "| GDP adjustment factor |")
        assert_sentence(self, gdp, r"5% for 2026-27")
        penalty = marked_line(self, AU / "au-payg-instalments.md", "**Late BAS lodgement penalty:**")
        dated = assert_sentence(
            self,
            penalty,
            r"\$(\d+) from 1 July 2023 to 6 November 2024, \$(\d+) from 7 November 2024 to 30 June 2026, and \$(\d+) from 1 July 2026",
        )
        self.assertEqual(dated.groups(), ("313", "330", "364"))
        five = assert_sentence(self, penalty, r"Five units are respectively \$([\d,]+), \$([\d,]+) and \$([\d,]+)")
        for unit, maximum in zip(dated.groups(), five.groups()):
            with self.subTest(unit=unit):
                self.assertEqual(5 * int(unit), int(maximum.replace(",", "")))


if __name__ == "__main__":
    unittest.main()
