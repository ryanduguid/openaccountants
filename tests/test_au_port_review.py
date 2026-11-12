"""Regression contracts for source-cited Australian port corrections."""

from decimal import Decimal
from pathlib import Path
import re
import unittest


AU = Path(__file__).resolve().parents[1] / "skills" / "international" / "australia"


class AustralianPortReviewTests(unittest.TestCase):
    def test_exactly_four_point_five_tonne_vehicle_keeps_acquisition_exception(self):
        text = (AU / "au-fuel-tax-credits.md").read_text(encoding="utf-8")
        step = text.split("### Step 3:", 1)[1].split("### Step 4:", 1)[0]
        self.assertRegex(step, r"except a vehicle of exactly 4\.5 tonnes acquired before 1 July 2006")
        self.assertIn("Establish the acquisition date before excluding", step)
        self.assertIn("PCG 2021/2 para 4", step)
        # A later acquisition remains within the <=4.5-tonne exclusion; the
        # exception must not be widened to all vehicles at that weight.
        self.assertIn("4.5 tonnes or less travelling on a public road", step)
        self.assertIn("GVM over 4.5 tonnes, or 4.5 tonnes or more if acquired before 1 July 2006", text)
        self.assertIn("| GVM unknown | No credit pending GVM evidence and, if exactly 4.5 tonnes, acquisition-date evidence; flag |", text)

    def test_ess_variant_states_and_sums_all_four_income_components(self):
        text = (AU / "au-employee-share-schemes.md").read_text(encoding="utf-8")
        variant = text.split("**Decision variant: the income test fails.**", 1)[1].split("\n\n", 1)[0]
        self.assertIn("total net investment loss nil", variant)
        values = []
        for label in ["taxable income before the reduction is", "reportable fringe benefits total", "reportable superannuation contributions"]:
            match = re.search(rf"{label} \$([\d,]+)", variant)
            self.assertIsNotNone(match, label)
            values.append(Decimal(match[1].replace(",", "")))
        total = re.search(r"test total is \$([\d,]+)", variant)
        self.assertIsNotNone(total)
        self.assertEqual(sum(values, Decimal(0)), Decimal(total[1].replace(",", "")))


if __name__ == "__main__":
    unittest.main()
