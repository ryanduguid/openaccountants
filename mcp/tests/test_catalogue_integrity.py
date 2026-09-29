"""The committed packages/ tree as the server catalogues it.

Every other test builds a synthetic tree. This one reads the real one, so a
pull request that reintroduces a duplicate slug (two guides with one `name`,
which the catalogue can only serve by dropping the slug) fails here as well as
in scripts/validate-guides.py. Until 2026-09-28 eight slugs were dropped this
way and nothing noticed.
"""

from __future__ import annotations

import json
import os
import unittest

from openaccountants_mcp import server

#: Indexed guides that no package carries, by design: the file templates, the
#: treaty-corridor template, the state references file, and a workflow base
#: no guide declares (the build shares only the declared ones).
def _unpackaged_by_design(path: str, shared_names: set[str]) -> bool:
    return (
        path.startswith("skills/templates/")
        or "/_templates/" in path
        or path == "skills/us-states/references.md"
        or (path.startswith("skills/foundation/") and os.path.basename(path) not in shared_names)
    )


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

    def test_the_catalogue_serves_every_indexed_guide_the_build_packages(self) -> None:
        """index.json is the inventory of the source tree and the catalogue is
        built from packages/; CI keeps the two in step, and this pins that
        nothing indexed is missing from the catalogue except the documented
        exclusions, and nothing catalogued is missing from the index. Until
        2026-09-29 the build silently left 57 indexed guides out."""
        index_path = server.REPO_ROOT / "index.json"
        if not index_path.is_file():
            raise unittest.SkipTest("index.json is not built in this checkout")
        guides = json.loads(index_path.read_text(encoding="utf-8"))["guides"]
        bundles = json.loads((server.PACKAGES_DIR / "bundles.json").read_text(encoding="utf-8"))
        shared_names = {name for package in bundles["packages"].values() for name in package["shared"]}
        indexed = {g["slug"] for g in guides}
        excluded = sorted(g["slug"] for g in guides if _unpackaged_by_design(g["path"], shared_names))
        missing = sorted(g["slug"] for g in guides
                         if g["slug"] not in self.index and g["slug"] not in excluded)
        self.assertEqual(missing, [], "indexed but served by no package")
        self.assertEqual(sorted(set(self.index) - indexed), [], "catalogued but not indexed")
        self.assertLessEqual(len(excluded), 12, excluded)

    def test_state_guides_carry_the_state_namespace_and_code(self) -> None:
        record = self.index["us-ca-540-individual-return"]
        self.assertEqual(record["jurisdiction"], "US-CA")
        self.assertEqual(record["relpath"], "us-ca/us-ca-540-individual-return.md")
        state_slugs = [s for s in self.index if s.startswith("us-") and self.index[s]["relpath"].startswith("us-")]
        self.assertGreater(len(state_slugs), 150)


if __name__ == "__main__":
    unittest.main()
