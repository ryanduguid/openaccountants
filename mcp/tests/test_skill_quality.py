"""Regression tests for fail-closed MCP quality metadata."""

from __future__ import annotations

import unittest

from openaccountants_mcp import server


class SkillQualityTests(unittest.TestCase):
    def test_tier_one_with_named_reviewer_is_accountant_verified(self) -> None:
        meta = {"tier": 1, "reviewed_by": "Alex Example, CPA"}

        self.assertEqual(server._quality_tier(meta), "accountant-verified")

    def test_tier_two_remains_research_even_with_reviewer_name(self) -> None:
        meta = {"tier": 2, "reviewed_by": "Alex Example, CPA"}

        self.assertEqual(server._quality_tier(meta), "research-verified")

    def test_tier_one_without_real_reviewer_fails_closed(self) -> None:
        for reviewer in (None, "", "pending", "n/a"):
            with self.subTest(reviewer=reviewer):
                meta = {"tier": 1, "reviewed_by": reviewer}
                self.assertEqual(server._quality_tier(meta), "research-verified")

    def test_reviewer_name_does_not_replace_missing_tier(self) -> None:
        meta = {"verified_by": "Alex Example, CPA"}

        self.assertEqual(server._quality_tier(meta), "research-verified")


if __name__ == "__main__":
    unittest.main()
