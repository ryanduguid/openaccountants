"""Guided workflows must not restate figures their guides own.

`workflows/` is hand-written and the gate checkers read only `skills/`, so a
rate restated there goes wrong without anything saying so: the UK workflow
offered 2025/26 and told the reader to apply the Class 4 rate of 2023/24. This
gate finds money amounts, percentages, comma numbers, decimals, integers with
a unit or too long for a year or form number, 4-digit amounts stated for a
cap, allowance or threshold, and business-day deadlines, in workflow prose
and inline code, outside fenced code and URLs. Any figure fails until it is
replaced by a pointer to a guide. Every guide slug a workflow names must
exist, or the pointer leads nowhere; `tests/test_docs_links.py` does the same
for link targets. `make test` runs this file, so `make check` does too.
"""

from __future__ import annotations

import importlib.util
import json
import re
import unittest
from decimal import Decimal
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = REPO_ROOT / "workflows"
UK_GUIDES = REPO_ROOT / "skills" / "international" / "uk"

SPEC = importlib.util.spec_from_file_location(
    "check_examples", REPO_ROOT / "scripts" / "check-examples.py")
check_examples = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(check_examples)

FENCED = re.compile(r"^(```|~~~).*?^\1", re.MULTILINE | re.DOTALL)
LINK_TARGET = re.compile(r"\]\([^)\s]*\)")
BARE_URL = re.compile(r"https?://\S+")
# shortcut: a 4-digit integer with no unit reads the same as a year or form
# number, so it is a figure only straight after a fiscal noun, as in `threshold
# is 5000` or `capped at 5000`. `A 5000 threshold`, words between the noun and
# the amount, and `limit of 2000`, which reads as a year, still pass, as does a
# bare `5000`. Add the phrasing below if one turns up.
FIGURE = re.compile(
    r"(?:(?:A\$|US\$|[£€$])\s?|\b(?:R|EUR|GBP|USD|AUD|ZAR)\s?)\d[\d,]*(?:\.\d+)?"
    r"(?:\s?(?:million|billion|m|k)\b)?"
    r"|\b\d[\d,]*(?:\.\d+)?\s?"
    r"(?:[%£€]|(?:[Pp]er\s?cent|euros?|pounds?|dollars?|rand|EUR|GBP|USD|AUD|ZAR|cents?"
    r"|(?:business\s)?kms?|kilometres?|miles?)\b)"
    r"|\b\d{1,3}(?:,\d{3})+(?:\.\d+)?\b"
    r"|\b\d+\.\d+\b(?!\s?[ap]\.?m\b)"
    r"|\b\d{5,}\b"
    r"|\b\d+[\s-](?:business|working)[\s-]days?\b"
    r"|(?i:\b(?:caps?|capped|ceilings?|limits?|limited|thresholds?|allowances?"
    r"|deductions?|exemptions?|offsets?)"
    r"(?:\s+(?:is|are|at)\s+|[\s*]*[:=|][\s*]*|\s+(?:of|to)\s+(?!(?:19|20)\d\d\b))"
    r"\d{4}\b(?![-\u2013/]\w))"
)
SLUG = re.compile(r"`(?![\d-]+`)([a-z0-9]+(?:-[a-z0-9]+)+)`")

# A sole trader's result under the guides' rates. Each figure in `expected` was
# worked by hand from the rates the test reads out of the guides.
SOLE_TRADER = """name: Wexler McGill, sole trader, 2025-26
inputs:
  profit: {profit}
  allowance: {allowance}
  basic_limit: {basic_limit}
  basic_rate: {basic_rate}
  higher_rate: {higher_rate}
  lower_limit: {lower_limit}
  upper_limit: {upper_limit}
  main_rate: {main_rate}
  additional_rate: {additional_rate}
steps:
  - basic_tax: pct(min(profit, basic_limit) - allowance, basic_rate)
  - higher_tax: pct(max(profit - basic_limit, 0), higher_rate)
  - class_4_main: pct(min(profit, upper_limit) - lower_limit, main_rate)
  - class_4_additional: pct(max(profit - upper_limit, 0), additional_rate)
  - class_4: class_4_main + class_4_additional
  - total: basic_tax + higher_tax + class_4
expected:
  basic_tax: {basic_tax}
  higher_tax: {higher_tax}
  class_4: {class_4}
  total: {total}
"""


def blanked(pattern: re.Pattern[str], text: str) -> str:
    """Blank each match but keep its newlines, so line numbers survive."""
    return pattern.sub(lambda match: re.sub(r"[^\n]", " ", match.group(0)), text)


def prose(text: str) -> str:
    """The text a reader sees, with fenced code and URLs blanked."""
    for pattern in (FENCED, LINK_TARGET, BARE_URL):
        text = blanked(pattern, text)
    return text


def figures_in(text: str) -> list[tuple[int, str]]:
    """Each figure in the text, with its 1-based line number."""
    text = prose(text)
    return [
        (text.count("\n", 0, match.start()) + 1, " ".join(match.group(0).split()))
        for match in FIGURE.finditer(text)
    ]


def figures(text: str) -> list[str]:
    return [figure for _, figure in figures_in(text)]


def workflow_figures() -> dict[tuple[str, str], list[int]]:
    found: dict[tuple[str, str], list[int]] = {}
    for path in sorted(WORKFLOWS.glob("*.md")):
        for line, figure in figures_in(path.read_text(encoding="utf-8")):
            found.setdefault((path.name, figure), []).append(line)
    return found


def named_slugs(text: str) -> set[str]:
    """Slugs in inline code; a workflow's own MCP prompt name is not a guide."""
    return {
        slug
        for line in text.splitlines()
        if not line.startswith("**MCP prompt name:**")
        for slug in SLUG.findall(line)
    }


def table_cell(path: Path, label: str, year: str) -> tuple[str, str]:
    """The label and `year` cells of the first comparison-table row under a `year` column."""
    column = None
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|"):
            continue
        cells = [cell.strip(" *") for cell in line.strip().strip("|").split("|")]
        if any(cell.startswith(year) for cell in cells):
            column = next(i for i, cell in enumerate(cells) if cell.startswith(year))
        elif column is not None and cells[0].startswith(label):
            return cells[0], cells[column]
    raise AssertionError(f"{path.name}: no {label!r} row under a {year} column")


def amount(text: str) -> Decimal:
    return Decimal(re.search(r"\d[\d,]*(?:\.\d+)?", text).group(0).replace(",", ""))


def guide_rates(year: str = "2025-26") -> dict[str, Decimal]:
    """The rates a 2025-26 sole trader needs, read from the two guides."""
    income_tax = UK_GUIDES / "uk-income-tax-sa100.md"
    nic = UK_GUIDES / "uk-national-insurance.md"
    basic_label, basic_limit = table_cell(income_tax, "Basic rate band", year)
    higher_label, _ = table_cell(income_tax, "Higher rate band", year)
    return {
        "allowance": amount(table_cell(income_tax, "Personal allowance", year)[1]),
        "basic_limit": amount(basic_limit),
        "basic_rate": amount(basic_label),
        "higher_rate": amount(higher_label),
        "lower_limit": amount(table_cell(nic, "Class 4 Lower Profits Limit", year)[1]),
        "upper_limit": amount(table_cell(nic, "Class 4 Upper Profits Limit", year)[1]),
        "main_rate": amount(table_cell(nic, "Class 4 main rate", year)[1]),
        "additional_rate": amount(table_cell(nic, "Class 4 additional rate", year)[1]),
    }


class WorkflowFigureTests(unittest.TestCase):
    def test_no_figures_in_workflow_prose(self) -> None:
        self.assertEqual(workflow_figures(), {},
                         "replace each figure with a pointer to the guide that owns it")

    def test_detection_reads_inline_code_but_not_fences_or_urls(self) -> None:
        self.assertEqual(figures("Apply the £1,234.50 cap and a 9.5% rate."), ["£1,234.50", "9.5%"])
        self.assertEqual(figures("A 12 per cent loading above €14,500 or R350,000."),
                         ["12 per cent", "€14,500", "R350,000"])
        self.assertEqual(figures("A £1 million limit, EUR 12,000 or $150k."),
                         ["£1 million", "EUR 12,000", "$150k"])
        self.assertEqual(figures("Run `pay --rate 11%` at `9%`."), ["11%", "9%"])
        self.assertEqual(figures("From 14,500€ or 14,500 euros to 3 pounds."),
                         ["14,500€", "14,500 euros", "3 pounds"])
        self.assertEqual(figures("Band of 50,270, coefficient 0.35."), ["50,270", "0.35"])
        self.assertEqual(figures("Load `us-form-1040-individual-return` and `uk-sa100`."), [])
        self.assertEqual(figures("```\n£500\n```\nNo figure."), [])
        self.assertEqual(figures("[ruling](https://x.test/view?docid=TXR%2FTR20223)"), [])
        self.assertEqual(figures("See https://x.test/a%20b for detail."), [])
        self.assertEqual(figures("Section 26-50, Rule 8 and 7.30 pm on 12 May 2026."), [])

    def test_clock_times_are_not_decimals(self) -> None:
        self.assertEqual(figures("By 7.30 pm, 11.15am or 9.45 a.m."), [])
        self.assertEqual(figures("A rate of 7.30 applies."), ["7.30"])

    def test_integers_with_a_unit_or_threshold_length_are_figures(self) -> None:
        self.assertEqual(figures("Travel 5000 km or 5000 business km."), ["5000 km", "5000 business km"])
        self.assertEqual(figures("88 cents per kilometre over 300 kilometres."),
                         ["88 cents", "300 kilometres"])
        self.assertEqual(figures("Register above 50000 in turnover."), ["50000"])

    def test_four_digit_amounts_after_a_fiscal_noun_are_figures(self) -> None:
        self.assertEqual(figures("The threshold is 5000."), ["threshold is 5000"])
        self.assertEqual(figures("The threshold is 2000."), ["threshold is 2000"])
        self.assertEqual(figures("Capped at 5000 km."), ["Capped at 5000"])
        self.assertEqual(figures("Capped at 2500, an allowance of 1200 and limited to 9000."),
                         ["Capped at 2500", "allowance of 1200", "limited to 9000"])
        self.assertEqual(figures("**Cap:** 1200 and | Threshold | 5000 |"),
                         ["Cap:** 1200", "Threshold | 5000"])

    def test_years_forms_and_sections_after_a_fiscal_noun_are_not_figures(self) -> None:
        self.assertEqual(figures("The 2026 threshold, the allowance for 2026, the limit of 2025 "
                                 "and the cap of 2025-26, 2025–26 or 2025/26."), [])
        self.assertEqual(figures("The limit on Form 8829, the threshold is Form 1040 and the "
                                 "offset of 1099-NEC."), [])
        self.assertEqual(figures("The cap in s 1202 and the allowance of section 1231."), [])

    def test_business_day_deadlines_are_figures(self) -> None:
        self.assertEqual(figures("Paid within 7 business days, a 10-business-day notice or 5 working days."),
                         ["7 business days", "10-business-day", "5 working days"])
        self.assertEqual(figures("On the next business day, within 7 days or by day 28."), [])

    def test_years_forms_and_sections_are_not_figures(self) -> None:
        self.assertEqual(figures("Form 1040, Form 8829, 1099-NEC and Schedule 2F for 2026-27."), [])
        self.assertEqual(figures("Section 199A, s 100A, s 25-130 and 30 June 2026, within 7 days."), [])

    def test_line_numbers_survive_blanked_code(self) -> None:
        self.assertEqual(figures_in("```\ncode\n```\n`x`\n\nApply 9%.\n"), [(6, "9%")])


class WorkflowSlugTests(unittest.TestCase):
    def test_every_named_guide_exists(self) -> None:
        index = json.loads((REPO_ROOT / "index.json").read_text(encoding="utf-8"))
        slugs = {guide["slug"] for guide in index["guides"]}
        missing = {
            (path.name, slug)
            for path in WORKFLOWS.glob("*.md")
            for slug in named_slugs(path.read_text(encoding="utf-8")) - slugs
        }
        self.assertEqual(missing, set())

    def test_a_prompt_name_is_not_a_slug(self) -> None:
        self.assertEqual(named_slugs("**MCP prompt name:** `uk-self-employed`\n- `uk-national-insurance`\n"),
                         {"uk-national-insurance"})

    def test_a_numeric_identifier_is_not_a_slug(self) -> None:
        self.assertEqual(named_slugs("`2025-26`, `25-130`, `26-50-2`, `1099-nec` and `uk-sa100`"),
                         {"1099-nec", "uk-sa100"})


class SoleTraderWorkedCheck(unittest.TestCase):
    """Rates read from the guides, in the repository's oa-check case format."""

    def test_2025_26_sole_trader(self) -> None:
        rates = guide_rates()
        cases = {
            30000: {"basic_tax": "3486", "higher_tax": "0", "class_4": "1045.80", "total": "4531.80"},
            60000: {"basic_tax": "7540", "higher_tax": "3892", "class_4": "2456.60", "total": "13888.60"},
        }
        for profit, expected in cases.items():
            with self.subTest(profit=profit):
                block = check_examples.parse_block(SOLE_TRADER.format(profit=profit, **rates, **expected))
                self.assertEqual(check_examples.run_block(block), [])

    def test_class_2_is_treated_as_paid_at_these_profits(self) -> None:
        guide = UK_GUIDES / "uk-national-insurance.md"
        self.assertEqual(table_cell(guide, "Class 2 status", "2025-26")[1], "Abolished (voluntary only)")
        rule = next(line for line in guide.read_text(encoding="utf-8").splitlines()
                    if line.startswith("- **Class 2 treatment for all three years**"))
        self.assertIn("are treated as paid automatically", rule)
        self.assertLess(amount(table_cell(guide, "Small Profits Threshold", "2025-26")[1]), 30000)


if __name__ == "__main__":
    unittest.main()
