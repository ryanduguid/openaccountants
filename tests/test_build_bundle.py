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
import ntpath
import os
import re
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

    def write_manifest(self, document) -> None:
        (self.packages / "bundles.json").write_text(json.dumps(document), encoding="utf-8")

    def assert_rejected_before_output(self, document, message) -> None:
        self.write_manifest(document)
        for existing in (False, True):
            output = self.root / ("existing" if existing else "absent")
            if existing:
                output.mkdir(exist_ok=True)
            with self.subTest(existing=existing), self.assertRaisesRegex(SystemExit, message):
                build_bundle.assemble("zzland", str(self.packages), str(output))
            if existing:
                self.assertEqual(list(output.iterdir()), [])
            else:
                self.assertFalse(output.exists())

    def test_duplicate_destinations_are_rejected_before_copying(self) -> None:
        original = self.bundles()
        for kind in ("own", "shared", "both"):
            with self.subTest(kind=kind):
                document = json.loads(json.dumps(original))
                entry = document["packages"]["zzland"]
                if kind == "own":
                    entry["files"].append(entry["files"][0])
                elif kind == "shared":
                    entry["shared"].append(entry["shared"][0])
                else:
                    name = entry["shared"][0]
                    (self.packages / "zzland" / name).write_text("Own copy.")
                    entry["files"].append(name)
                self.assert_rejected_before_output(document, "appears twice")

    def test_manifest_filenames_cannot_escape_or_use_nonportable_paths(self) -> None:
        (self.packages / "escape.md").write_text("Outside the selected package.")
        outside = self.root / "outside.md"
        outside.write_text("Outside packages.")
        original = self.bundles()
        for name in ("../escape.md", "..\\escape.md", str(outside), "C:escape.md",
                     "C:\\escape.md", "\\\\host\\share\\escape.md", "", ".", "..", "bad\0name", "guide.md:stream"):
            for field in ("files", "shared"):
                with self.subTest(name=name, field=field):
                    document = json.loads(json.dumps(original))
                    document["packages"]["zzland"][field] = [name]
                    self.assert_rejected_before_output(document, "filename")
        self.assertEqual(outside.read_text(), "Outside packages.")
        self.assertFalse((self.root / "escape.md").exists())

    def test_malformed_manifest_shapes_report_an_error_before_writing(self) -> None:
        for document in (None, [], {}, {"packages": []}):
            with self.subTest(document=document):
                self.assert_rejected_before_output(document, "manifest")
        for entry in (None, [], {"files": None, "shared": []}, {"files": "x", "shared": []},
                      {"files": [], "shared": [1]}, {"shared": []}):
            with self.subTest(entry=entry):
                self.assert_rejected_before_output({"packages": {"zzland": entry}}, "manifest")

    def test_package_and_shared_directory_names_are_single_components(self) -> None:
        for shared_dir in ("../elsewhere", "..\\elsewhere", str(self.root), None):
            with self.subTest(shared_dir=shared_dir):
                document = self.bundles()
                document["shared_dir"] = shared_dir
                self.assert_rejected_before_output(document, "shared directory")
        document = {"packages": {"../zzland": {"files": [], "shared": []}}}
        self.write_manifest(document)
        with self.assertRaisesRegex(SystemExit, "package name"):
            build_bundle.assemble("../zzland", str(self.packages), str(self.root / "absent"))
        self.assertFalse((self.root / "absent").exists())

    def symlink(self, path, target, *, directory=False) -> None:
        try:
            path.symlink_to(target, target_is_directory=directory)
        except OSError as exc:
            self.skipTest(f"symlinks unavailable: {exc}")

    def test_a_source_symlink_cannot_leave_its_own_source_directory(self) -> None:
        outside = self.root / "outside.md"
        outside.write_text("Outside packages.")
        self.symlink(self.packages / "zzland" / "escaped.md", outside)
        document = self.bundles()
        document["packages"]["zzland"]["files"].append("escaped.md")
        self.assert_rejected_before_output(document, "outside")

    def test_a_shared_directory_symlink_cannot_leave_packages(self) -> None:
        shared = self.packages / "_shared"
        outside = self.root / "outside-shared"
        shared.rename(outside)
        self.symlink(shared, outside, directory=True)
        self.assert_rejected_before_output(self.bundles(), "outside")

    def test_a_contained_source_symlink_keeps_working(self) -> None:
        self.symlink(self.packages / "zzland" / "linked.md", self.packages / "zzland" / "zz-vat.md")
        document = self.bundles()
        document["packages"]["zzland"]["files"].append("linked.md")
        self.write_manifest(document)
        output = self.root / "bundle"
        build_bundle.assemble("zzland", str(self.packages), str(output))
        self.assertEqual((output / "linked.md").read_text(encoding="utf-8"), GUIDE)

    @unittest.skipUnless(os.name == "nt", "case collisions use the host filesystem rules")
    def test_windows_case_collisions_are_rejected_before_copying(self) -> None:
        document = self.bundles()
        document["packages"]["zzland"]["files"].append("ZZ-VAT.MD")
        self.assert_rejected_before_output(document, "appears twice")

    @unittest.skipUnless(os.name == "nt", "Windows path aliases")
    def test_windows_aliases_and_invalid_names_are_rejected_before_copying(self) -> None:
        for name in ("NUL.md", "con", "COM1.txt", "lpt9", "guide.md.", "guide.md ", "bad?.md"):
            with self.subTest(name=name):
                document = self.bundles()
                document["packages"]["zzland"]["files"].append(name)
                self.assert_rejected_before_output(document, "filename")

    def test_a_bundle_holds_the_package_and_its_shared_files(self) -> None:
        out_dir = self.root / "dist" / "zzland"
        out_dir.mkdir(parents=True)
        output = self.run_main("zzland", "--out", str(out_dir))
        self.assertEqual(
            sorted(p.name for p in out_dir.iterdir()),
            ["README.md", "foundation.md", "intake.md", "vat-workflow-base.md", "zz-vat.md"],
        )
        self.assertEqual((out_dir / "zz-vat.md").read_text(encoding="utf-8"), GUIDE)
        self.assertEqual((out_dir / "vat-workflow-base.md").read_text(encoding="utf-8"), BASE)
        self.assertIn("zzland: 5 files -> ", output)

    def test_the_bundled_readme_links_to_the_files_beside_it(self) -> None:
        out_dir = self.root / "dist" / "zzland"
        self.run_main("zzland", "--out", str(out_dir))
        readme = (out_dir / "README.md").read_text(encoding="utf-8")
        self.assertNotIn("../_shared/", readme)
        self.assertIn("are included in this folder:", readme)
        self.assertIn("- [`vat-workflow-base.md`](vat-workflow-base.md)", readme)
        self.assertIn("(the shared files listed above are included)", readme)
        for target in re.findall(r"\]\(([^)]+)\)", readme):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            self.assertTrue((out_dir / target).is_file(), f"README links to {target}, which the bundle lacks")
        # the checked-in README keeps the repository's layout
        checked_in = (self.packages / "zzland" / "README.md").read_text(encoding="utf-8")
        self.assertIn("](../_shared/vat-workflow-base.md)", checked_in)

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
            "file output": (["zzland", "--out", str(self.packages / "bundles.json")], "must not exist or must be empty"),
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

    def test_every_bundle_has_unique_destinations_on_windows(self) -> None:
        for package, entry in self.bundles["packages"].items():
            names = entry["files"] + entry["shared"]
            with self.subTest(package=package):
                self.assertEqual(len(names), len({ntpath.normcase(name) for name in names}))

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
