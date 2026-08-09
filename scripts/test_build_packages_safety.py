"""Safety regression tests for the destructive package-builder entry point."""

from __future__ import annotations

import contextlib
import importlib.util
import io
import tempfile
import unittest
from pathlib import Path

BUILD_SCRIPT = Path(__file__).resolve().parent / "build-packages.py"


def _load_builder():
    spec = importlib.util.spec_from_file_location("_build_packages_safety", BUILD_SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class BuildPackagesSafetyTests(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name)
        self.packages = self.root / "packages"
        self.skills = self.root / "skills"
        self.packages.mkdir()
        self.builder = _load_builder()
        self.builder.PACKAGES_DIR = str(self.packages)
        self.builder.SKILLS_DIR = str(self.skills)

    def tearDown(self):
        self.tempdir.cleanup()

    def _make_required_us_sources(self):
        for relative in ("foundation", "orchestrator", "federal", "us-states"):
            (self.skills / relative).mkdir(parents=True, exist_ok=True)

    def test_unknown_argument_fails_before_any_package_cleanup(self):
        sentinel = self.packages / "keep-me.txt"
        sentinel.write_text("unchanged", encoding="utf-8")

        with self.assertRaisesRegex(SystemExit, r"unknown argument"):
            self.builder.main(["--us_only"])

        self.assertEqual(sentinel.read_text(encoding="utf-8"), "unchanged")

    def test_missing_sources_fail_before_any_package_cleanup(self):
        sentinel = self.packages / "keep-me.txt"
        sentinel.write_text("unchanged", encoding="utf-8")

        with self.assertRaisesRegex(RuntimeError, r"Refusing to alter packages"):
            self.builder.main([])

        self.assertEqual(sentinel.read_text(encoding="utf-8"), "unchanged")

    def test_us_only_does_not_rebuild_or_touch_canadian_packages(self):
        self._make_required_us_sources()
        canadian_sentinel = self.packages / "ca-on" / "keep-me.txt"
        canadian_sentinel.parent.mkdir()
        canadian_sentinel.write_text("unchanged", encoding="utf-8")
        canadian_skill = canadian_sentinel.parent / "untouched-skill.md"
        canadian_skill.write_text("Canadian content", encoding="utf-8")
        calls = {"us": 0, "canada": 0}

        def build_us():
            calls["us"] += 1
            return []

        def build_canada():
            calls["canada"] += 1
            return []

        self.builder.build_all_us_packages = build_us
        self.builder.build_all_canada_packages = build_canada

        with contextlib.redirect_stdout(io.StringIO()):
            self.builder.main(["--us-only"])

        self.assertEqual(calls, {"us": 1, "canada": 0})
        self.assertEqual(canadian_sentinel.read_text(encoding="utf-8"), "unchanged")
        self.assertEqual(canadian_skill.read_text(encoding="utf-8"), "Canadian content")

    def test_national_us_package_uses_canonical_name_and_practitioner(self):
        source = self.skills / "international" / "us"
        source.mkdir(parents=True)
        (source / "us-example.md").write_text(
            "---\nname: us-example\njurisdiction: US\n---\n\n# US example\n",
            encoding="utf-8",
        )

        result = self.builder.build_package("us", str(source))

        self.assertEqual(result["jurisdiction"], "US")
        self.assertEqual(result["name"], "United States")
        readme = (self.packages / "us" / "README.md").read_text(encoding="utf-8")
        self.assertIn("# United States — AI Accounting Assistant", readme)
        self.assertIn("qualified CPA or EA", readme)
        self.assertNotIn("qualified qualified", readme)

    def test_generic_practitioner_wording_is_not_duplicated(self):
        readme = self.builder.build_readme(
            "Exampleland",
            ["example.md"],
            "tax professional",
            "ZZ",
        )
        self.assertIn("qualified tax professional", readme)
        self.assertNotIn("qualified qualified", readme)


if __name__ == "__main__":
    unittest.main()
