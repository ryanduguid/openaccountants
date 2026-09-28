"""Tests for scripts/build-bundle.py and for the shape of the checked-in packages/.

A package folder holds only the files specific to its jurisdiction; the files
it shares with other packages live once in packages/_shared/ and are listed
for it in packages/bundles.json. build-bundle.py puts the two together into
one upload-ready folder. The first class runs it on the synthetic tree that
tests/test_build_packages.py builds; the second pins, on the committed tree,
the invariants the assembler and the MCP server rely on: every listed file
exists, every package file is listed, every shared file is used, and no guide
is checked in twice.
"""

from __future__ import annotations

import contextlib
import hashlib
import importlib.util
import io
import json
import sys
import unittest
from collections import defaultdict
from pathlib import Path

from test_build_packages import BASE, GUIDE, SyntheticTreeCase

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = REPO_ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

SPEC = importlib.util.spec_from_file_location("build_bundle_for_tests", SCRIPTS / "build-bundle.py")
assert SPEC is not None and SPEC.loader is not None
build_bundle = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(build_bundle)


class AssembleTests(SyntheticTreeCase):
    def setUp(self) -> None:
        super().setUp()
        self.build()

    def run_main(self, *argv: str) -> str:
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            self.assertEqual(build_bundle.main([*argv, "--packages", str(self.packages)]), 0)
        return out.getvalue()

    def test_a_bundle_holds_the_package_and_its_shared_files(self) -> None:
        out_dir = self.root / "dist" / "zzland"
        output = self.run_main("zzland", "--out", str(out_dir))
        self.assertEqual(
            sorted(p.name for p in out_dir.iterdir()),
            ["README.md", "foundation.md", "intake.md", "vat-workflow-base.md", "zz-vat.md"],
        )
        self.assertEqual((out_dir / "zz-vat.md").read_text(encoding="utf-8"), GUIDE)
        self.assertEqual((out_dir / "vat-workflow-base.md").read_text(encoding="utf-8"), BASE)
        self.assertIn("zzland: 5 files -> ", output)

    def test_list_names_every_package_and_nothing_else(self) -> None:
        listed = self.run_main("--list").split()
        for name in ("zzland", "us-ca", "ca-on"):
            self.assertIn(name, listed)
        self.assertNotIn("_shared", listed)
        self.assertNotIn("us-federal", listed)

    def test_the_failure_cases_exit_with_a_reason(self) -> None:
        cases = {
            "unknown package": (["nowhere", "--out", str(self.root / "x")], "unknown package 'nowhere'"),
            "non-empty output": (["zzland", "--out", str(self.packages / "zzland")], "must not exist or must be empty"),
        }
        for label, (argv, message) in cases.items():
            with self.subTest(label), self.assertRaises(SystemExit) as caught:
                build_bundle.main([*argv, "--packages", str(self.packages)])
            self.assertIn(message, str(caught.exception))
        self.assertFalse((self.root / "x").exists())

    def test_a_listed_file_the_tree_lacks_is_an_error(self) -> None:
        (self.packages / "_shared" / "vat-workflow-base.md").unlink()
        with self.assertRaises(SystemExit) as caught:
            build_bundle.assemble("zzland", str(self.packages), str(self.root / "x"))
        self.assertIn("bundles.json names files the tree does not hold", str(caught.exception))
        self.assertFalse((self.root / "x").exists(), "nothing is written until every file is found")

    def test_without_bundles_json_it_says_to_build_first(self) -> None:
        (self.packages / "bundles.json").unlink()
        with self.assertRaises(SystemExit) as caught:
            build_bundle.main(["zzland", "--packages", str(self.packages)])
        self.assertIn("run python3 scripts/build-packages.py first", str(caught.exception))

    def test_a_package_name_or_list_is_required(self) -> None:
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
            build_bundle.main(["--packages", str(self.packages)])


class CheckedInTreeTests(unittest.TestCase):
    """The committed packages/ tree: what a reader, the assembler and the MCP server get."""

    PACKAGES = REPO_ROOT / "packages"

    @classmethod
    def setUpClass(cls) -> None:
        bundles_path = cls.PACKAGES / "bundles.json"
        if not bundles_path.is_file():
            raise unittest.SkipTest("packages/bundles.json is not built")
        cls.bundles = json.loads(bundles_path.read_text(encoding="utf-8"))
        cls.shared_dir = cls.PACKAGES / cls.bundles["shared_dir"]

    def test_every_listed_file_exists_and_every_package_file_is_listed(self) -> None:
        self.assertGreater(len(self.bundles["packages"]), 200)
        for name, entry in self.bundles["packages"].items():
            with self.subTest(package=name):
                self.assertEqual(sorted(entry["files"]), sorted(p.name for p in (self.PACKAGES / name).iterdir()))
                for shared in entry["shared"]:
                    self.assertTrue((self.shared_dir / shared).is_file(), shared)
                self.assertFalse(set(entry["files"]) & set(entry["shared"]), "a file is both own and shared")

    def test_every_shared_file_is_listed_by_a_package(self) -> None:
        listed = {s for entry in self.bundles["packages"].values() for s in entry["shared"]}
        on_disk = {p.name for p in self.shared_dir.iterdir()} - {"README.md"}
        self.assertEqual(on_disk, listed)

    def test_no_guide_is_checked_in_twice(self) -> None:
        """The point of the shared directory: 3,647 of 5,954 package files were
        copies before it. The one file that may still repeat is intake.md,
        which the builder renders per package from one template, identically
        for jurisdictions the template treats alike."""
        by_hash: dict[str, list[str]] = defaultdict(list)
        for path in self.PACKAGES.rglob("*.md"):
            rel = path.relative_to(self.PACKAGES).as_posix()
            if rel.startswith("us-federal/") or path.name == "README.md":
                continue
            by_hash[hashlib.sha256(path.read_bytes()).hexdigest()].append(rel)
        offenders = sorted(
            sorted(paths) for paths in by_hash.values()
            if len(paths) > 1 and any(not p.endswith("/intake.md") for p in paths)
        )
        self.assertEqual(offenders, [])


if __name__ == "__main__":
    unittest.main()
