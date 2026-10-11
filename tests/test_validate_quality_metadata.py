"""Synthetic tests for canonical guide quality-metadata validation."""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "validate-guides.py"
SPEC = importlib.util.spec_from_file_location("validate_guides", SCRIPT)
validate_guides = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(validate_guides)


def errors_for(tier=None, reviewed_by=None, verified_by=None, review_status=None):
    errors = []
    validate_guides.check_quality_metadata(
        "skills/example.md",
        {"tier": tier, "reviewed_by": reviewed_by, "verified_by": verified_by,
         "review_status": review_status},
        errors,
    )
    return errors


class QualityMetadataValidationTests(unittest.TestCase):
    def test_rejects_missing_or_invalid_tier(self) -> None:
        self.assertIn("missing required", errors_for()[0])
        self.assertIn("must be 1 or 2", errors_for("3")[0])

    def test_tier_one_requires_a_real_reviewer(self) -> None:
        for placeholder in (None, "", " \t\n", "pending", "pending_review", "n/a", "tbd",
                            True, 42, ["Alex"], {"name": "Alex"}):
            with self.subTest(placeholder=placeholder):
                self.assertIn("tier 1 requires", errors_for("1", placeholder)[0])

    def test_tier_one_accepts_current_and_legacy_reviewer_fields(self) -> None:
        self.assertEqual(errors_for("1", reviewed_by="Alex Example, CPA"), [])
        self.assertEqual(errors_for("1", verified_by="Alex Example, CPA"), [])

    def test_tier_two_allows_research_review_but_not_verification(self) -> None:
        self.assertEqual(errors_for("2", reviewed_by="Alex Example, CPA"), [])
        self.assertEqual(errors_for("2", verified_by="pending"), [])
        self.assertIn(
            "must not claim accountant verification",
            errors_for("2", verified_by="Alex Example, CPA")[0],
        )

    def test_review_status_is_freshness_with_two_values(self) -> None:
        """Either value on a reviewed guide; a tier-2 guide can only be pending."""
        reviewer = "Alex Example, CPA"
        self.assertEqual(errors_for("1", reviewed_by=reviewer, review_status="current"), [])
        self.assertEqual(errors_for("1", reviewed_by=reviewer, review_status="pending_review"), [])
        self.assertEqual(errors_for("2", review_status="pending_review"), [])
        self.assertEqual(errors_for("2", reviewed_by=reviewer, review_status="pending_review"), [])
        self.assertEqual(errors_for("2"), [], "the key is optional")
        for bad in ("reviewed", "Current", "pending", ""):
            with self.subTest(value=bad):
                self.assertIn(
                    "must be current or pending_review",
                    errors_for("1", reviewed_by=reviewer, review_status=bad)[0],
                )

    def test_current_on_a_tier_two_guide_is_an_error(self) -> None:
        """`current` with `tier: 2` was the combination that read as reviewed
        everywhere else; a name in `reviewed_by` does not change that."""
        self.assertIn("claims a sign-off", errors_for("2", review_status="current")[0])
        errors = errors_for("2", reviewed_by="Alex Example, CPA", review_status="current")
        self.assertEqual(len(errors), 1)
        self.assertIn("use pending_review", errors[0])
        # The tier error comes first and the status error still fires beside it.
        errors = errors_for("2", verified_by="Alex Example, CPA", review_status="current")
        self.assertEqual(len(errors), 2)
        self.assertIn("must not claim accountant verification", errors[0])
        self.assertIn("claims a sign-off", errors[1])


if __name__ == "__main__":
    unittest.main()
