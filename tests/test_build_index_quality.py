"""Synthetic tests for the index's accountant-reviewed count."""

from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path
from unittest import mock


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "build-index.py"
SPEC = importlib.util.spec_from_file_location("build_index", SCRIPT)
build_index = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(build_index)


class BuildIndexQualityTests(unittest.TestCase):
    def test_count_requires_tier_one_and_a_real_reviewer(self) -> None:
        cases = (
            ("tier-one-current", "1", "Alex Example, CPA", None),
            ("tier-one-legacy", "1", None, "Alex Example, CPA"),
            ("pending-review", "1", "pending_review", None),
            ("tier-two-research", "2", "Research Reviewer", None),
            ("tier-two-invalid-verification", "2", None, "Alex Example, CPA"),
            ("missing-tier", None, "Alex Example, CPA", None),
            ("invalid-tier", "01", "Alex Example, CPA", None),
        )
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            paths = []
            for slug, tier, reviewed_by, verified_by in cases:
                path = root / f"{slug}.md"
                lines = ["---", f"name: {slug}", "jurisdiction: XX"]
                if tier is not None:
                    lines.append(f"tier: {tier}")
                if reviewed_by is not None:
                    lines.append(f"reviewed_by: {reviewed_by}")
                if verified_by is not None:
                    lines.append(f"verified_by: {verified_by}")
                lines.extend(("---", f"# {slug}"))
                path.write_text("\n".join(lines), encoding="utf-8")
                paths.append(path.name)

            with (
                mock.patch.object(build_index, "REPO_ROOT", str(root)),
                mock.patch.object(build_index, "guide_files", return_value=paths),
            ):
                result = build_index.build_index()

        self.assertEqual(result["counts"]["guides"], len(cases))
        self.assertEqual(result["counts"]["accountant_reviewed"], 2)
        self.assertEqual(
            {guide["slug"]: guide["tier"] for guide in result["guides"]},
            {
                "invalid-tier": "01",
                "missing-tier": None,
                "pending-review": 1,
                "tier-one-current": 1,
                "tier-one-legacy": 1,
                "tier-two-invalid-verification": 2,
                "tier-two-research": 2,
            },
        )


if __name__ == "__main__":
    unittest.main()
