"""The committed packages/ tree as the server catalogues it.

Every other test builds a synthetic tree. This one reads the real one, so a
pull request that reintroduces a duplicate slug (two guides with one `name`,
which the catalogue can only serve by dropping the slug) fails here as well as
in scripts/validate-guides.py. Until 2026-09-28 eight slugs were dropped this
way and nothing noticed.
"""

from __future__ import annotations

import unittest

from openaccountants_mcp import server


class CatalogueIntegrityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        if not (server.PACKAGES_DIR / "bundles.json").is_file():
            raise unittest.SkipTest("packages/ is not built in this checkout")
        server._index.cache_clear()
        cls.index, cls.ambiguous, cls.report = server._catalogue()

    @classmethod
    def tearDownClass(cls) -> None:
        server._index.cache_clear()

    def test_the_tree_holds_skills(self) -> None:
        self.assertGreater(self.report["skill_files"], 1000)
        self.assertEqual(self.report["slugs"], len(self.index))

    def test_no_slug_is_ambiguous(self) -> None:
        self.assertEqual(self.ambiguous, {})
        self.assertEqual(self.report["ambiguous_slugs"], 0)

    def test_no_slug_is_carried_by_two_files(self) -> None:
        self.assertEqual(self.report["duplicate_slugs"], 0)

    def test_state_guides_carry_the_state_namespace_and_code(self) -> None:
        record = self.index["us-ca-540-individual-return"]
        self.assertEqual(record["jurisdiction"], "US-CA")
        self.assertEqual(record["relpath"], "us-ca/us-ca-540-individual-return.md")
        state_slugs = [s for s in self.index if s.startswith("us-") and self.index[s]["relpath"].startswith("us-")]
        self.assertGreater(len(state_slugs), 150)


if __name__ == "__main__":
    unittest.main()
