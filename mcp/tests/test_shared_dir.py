"""packages/_shared/ holds, once each, the files several packages list.

A guide there declares its own jurisdiction (the US federal set says US, the
workflow bases GLOBAL, the Canadian federal set CA), and a declared code wins
as it does everywhere. One that declared none must not inherit the code its
neighbours declare most often, which is US by the size of the federal set: it
belongs to no single package, so it is GLOBAL.
"""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from openaccountants_mcp import server


def _skill(name: str, jurisdiction: str | None = None) -> str:
    lines = ["---", f"name: {name}"]
    if jurisdiction:
        lines.append(f"jurisdiction: {jurisdiction}")
    lines += ["tier: 2", "last_updated: 2026-01-02", "---", "", f"# {name}", "", f"Body for {name}."]
    return "\n".join(lines) + "\n"


class SharedDirectoryTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.packages = Path(self._tmp.name)
        self._original_packages = server.PACKAGES_DIR
        server.PACKAGES_DIR = self.packages
        server._index.cache_clear()

    def tearDown(self) -> None:
        server.PACKAGES_DIR = self._original_packages
        server._index.cache_clear()
        self._tmp.cleanup()

    def _write(self, relpath: str, content: str) -> None:
        path = self.packages / relpath
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def test_shared_guides_keep_their_declared_code(self) -> None:
        self._write("_shared/us-form-1040.md", _skill("us-form-1040", "US"))
        self._write("_shared/us-qbi.md", _skill("us-qbi", "US"))
        self._write("_shared/ca-fed-t1.md", _skill("ca-fed-t1", "CA"))
        self._write("_shared/income-tax-workflow-base.md", _skill("income-tax-workflow-base", "GLOBAL"))
        self._write("us-ca/ca-income-tax.md", _skill("ca-540", "US-CA"))

        index = server._index()

        self.assertEqual(index["us-form-1040"]["jurisdiction"], "US")
        self.assertEqual(index["ca-fed-t1"]["jurisdiction"], "CA")
        self.assertEqual(index["income-tax-workflow-base"]["jurisdiction"], "GLOBAL")
        self.assertEqual(index["us-form-1040"]["relpath"], "_shared/us-form-1040.md")
        self.assertEqual({s["slug"] for s in server.list_skills(jurisdiction="US")["skills"]}, {"us-form-1040", "us-qbi"})

    def test_an_undeclared_shared_guide_is_global_not_its_neighbours_majority(self) -> None:
        self._write("_shared/us-form-1040.md", _skill("us-form-1040", "US"))
        self._write("_shared/us-qbi.md", _skill("us-qbi", "US"))
        self._write("_shared/global-router.md", _skill("global-router"))

        self.assertEqual(server._index()["global-router"]["jurisdiction"], "GLOBAL")
        self.assertIn("global-router", {s["slug"] for s in server.list_skills(jurisdiction="GLOBAL")["skills"]})
        self.assertNotIn("global-router", {s["slug"] for s in server.list_skills(jurisdiction="US")["skills"]})

    def test_a_country_package_still_inherits_its_siblings_code(self) -> None:
        self._write("malta/malta-vat.md", _skill("malta-vat", "MT"))
        self._write("malta/malta-intake.md", _skill("malta-intake"))

        self.assertEqual(server._index()["malta-intake"]["jurisdiction"], "MT")


if __name__ == "__main__":
    unittest.main()
