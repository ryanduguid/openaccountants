"""Protect the named producer slots used by return assemblers."""

from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]


class ReturnAssemblyContractTests(unittest.TestCase):
    def execution_producers(self, name):
        text = (ROOT / "skills" / "orchestrator" / name).read_text(encoding="utf-8")
        section = re.search(
            r"^## Section 2\b[^\n]*\n(.*?)^## Section 3\b",
            text,
            flags=re.MULTILINE | re.DOTALL,
        )
        self.assertIsNotNone(section, "execution-order section is required")
        return re.findall(
            r"^0\. \*\*(?:Run )?([a-z0-9-]+) (?:first|second|third|fourth|fifth|step)\*\*",
            section.group(1),
            flags=re.MULTILINE,
        )

    def test_australian_named_producer_slots_keep_dependency_order(self):
        self.assertEqual(
            self.execution_producers("au-return-assembly.md"),
            [
                "australia-gst",
                "au-individual-return",
                "au-super-guarantee",
                "au-medicare-levy",
                "au-payg-instalments",
            ],
        )

    def test_indian_named_sequence_keeps_tds_credit_reconciliation(self):
        self.assertEqual(
            self.execution_producers("in-return-assembly.md"),
            ["india-gst", "in-income-tax", "in-advance-tax", "in-tds-freelance"],
        )


if __name__ == "__main__":
    unittest.main()
