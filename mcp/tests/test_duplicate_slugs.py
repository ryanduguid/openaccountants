"""Golden cases for deterministic and fail-closed duplicate handling."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from openaccountants_mcp import server


def _skill(name: str, title: str, jurisdiction: str = "XX") -> str:
    return (
        "---\n"
        f"name: {name}\n"
        f"jurisdiction: {jurisdiction}\n"
        "category: international\n"
        "tier: 2\n"
        "---\n\n"
        f"# {title}\n\nBody for {title}.\n"
    )


class DuplicateSlugTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.packages = Path(self._tmp.name)
        self._original_packages = server.PACKAGES_DIR
        server.PACKAGES_DIR = self.packages
        server._catalogue.cache_clear()

    def tearDown(self) -> None:
        server.PACKAGES_DIR = self._original_packages
        server._catalogue.cache_clear()
        self._tmp.cleanup()

    def _write(self, relpath: str, content: str) -> None:
        path = self.packages / relpath
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def test_byte_identical_aliases_collapse_to_sorted_path(self) -> None:
        content = _skill("shared-skill", "Shared")
        self._write("z/shared.md", content)
        self._write("a/shared.md", content)

        record = server._index()["shared-skill"]

        self.assertEqual(record["relpath"], "a/shared.md")
        self.assertEqual(server._duplicate_report()["identical_aliases"], 1)

    def test_hand_authored_us_federal_copy_has_documented_precedence(self) -> None:
        self._write("us-ca/federal.md", _skill("federal-skill", "Generated", "US-CA"))
        self._write("us-federal/federal.md", _skill("federal-skill", "Federal", "US"))

        record = server._index()["federal-skill"]

        self.assertEqual(record["relpath"], "us-federal/federal.md")
        self.assertEqual(server._duplicate_report()["federal_precedence"], 1)

    def test_divergent_generated_copies_are_omitted_and_fail_closed(self) -> None:
        self._write("country-a/collision.md", _skill("collision", "Country A", "AA"))
        self._write("country-b/collision.md", _skill("collision", "Country B", "BB"))
        self._write("country-c/safe.md", _skill("safe", "Safe", "CC"))

        self.assertNotIn("collision", server._index())
        self.assertIn("safe", server._index())
        self.assertNotIn("collision", {s["slug"] for s in server.list_skills()["skills"]})
        self.assertNotIn(
            "collision",
            {r["slug"] for r in server.search_skills("Body")["results"]},
        )
        with self.assertRaisesRegex(ValueError, "packaged copies differ"):
            server.get_skill("collision")

        self.assertEqual(
            server._duplicate_report(),
            {
                "skill_files": 3,
                "slugs": 2,
                "duplicate_slugs": 1,
                "identical_aliases": 0,
                "federal_precedence": 0,
                "ambiguous_slugs": 1,
                "ambiguous": [
                    {
                        "slug": "collision",
                        "paths": [
                            "country-a/collision.md",
                            "country-b/collision.md",
                        ],
                    }
                ],
            },
        )


if __name__ == "__main__":
    unittest.main()
