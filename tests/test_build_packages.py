"""Tests for scripts/build-packages.py, the generator behind packages/.

It is the largest script in the repository and had no tests; CHANGELOG.md
records a rebuild that wiped the hand-authored packages/us-federal/. These
tests build a synthetic skills/ tree into a scratch packages/ directory and
pin the properties that matter: hand-authored packages survive a rebuild
byte for byte, stale generated files are removed, a package carries the
bases its guides declare, `--out` builds elsewhere and leaves packages/
alone, the argument guards refuse the dangerous cases, and the generator
fails closed on its own malformed output.
"""

from __future__ import annotations

import contextlib
import importlib.util
import io
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = REPO_ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

SPEC = importlib.util.spec_from_file_location("build_packages_for_tests", SCRIPTS / "build-packages.py")
assert SPEC is not None and SPEC.loader is not None
build_packages = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(build_packages)


def frontmatter(name: str, extra: str = "") -> str:
    return (
        f"---\nname: {name}\ndescription: Synthetic guide for the generator tests.\n"
        f"jurisdiction: ZZ\ntier: 2\ntax_year: 2026\nlast_updated: 2026-01-02\n{extra}---\n"
    )


#: Long enough not to be skipped as a stub, and free of the redirect words.
GUIDE = frontmatter("zz-vat", "depends_on:\n  - vat-workflow-base\n") + "\n# Synthetic VAT guide\n\nLine.\nLine.\nLine.\nLine.\n"
BASE = frontmatter("vat-workflow-base") + "\n# VAT workflow base\n\nLine.\nLine.\nLine.\n"
FEDERAL_GUIDE = frontmatter("us-form-1040") + "\n# Hand-authored federal guide\n\nLine.\nLine.\nLine.\n"


class SyntheticTreeCase(unittest.TestCase):
    def setUp(self) -> None:
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        self.skills = self.root / "skills"
        self.packages = self.root / "packages"
        self.write({
            "skills/international/zzland/zz-vat.md": GUIDE,
            "skills/foundation/vat-workflow-base.md": BASE,
            "packages/us-federal/us-form-1040.md": FEDERAL_GUIDE,
            "packages/us-federal/rates.2026.json": '{"tax_year": 2026}\n',
            "packages/zzland/stale.md": frontmatter("stale") + "\nLeft over from an earlier build.\n",
            "packages/stray.txt": "not a package\n",
        })

    def write(self, files: dict[str, str]) -> None:
        for rel, text in files.items():
            path = self.root / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")

    def build(self, *argv: str) -> str:
        out = io.StringIO()
        with contextlib.ExitStack() as stack:
            stack.enter_context(mock.patch.object(build_packages, "SKILLS_DIR", str(self.skills)))
            stack.enter_context(mock.patch.object(build_packages, "PACKAGES_DIR", str(self.packages)))
            stack.enter_context(mock.patch.object(sys, "argv", ["build-packages.py", *argv]))
            stack.enter_context(contextlib.redirect_stdout(out))
            build_packages.main()
        return out.getvalue()


class RebuildTests(SyntheticTreeCase):
    def test_hand_authored_packages_survive_and_stale_output_is_removed(self) -> None:
        output = self.build()
        self.assertEqual((self.packages / "us-federal" / "us-form-1040.md").read_text(encoding="utf-8"), FEDERAL_GUIDE)
        self.assertEqual((self.packages / "us-federal" / "rates.2026.json").read_text(encoding="utf-8"), '{"tax_year": 2026}\n')
        self.assertEqual(sorted(p.name for p in (self.packages / "us-federal").iterdir()), ["rates.2026.json", "us-form-1040.md"])
        self.assertFalse((self.packages / "zzland" / "stale.md").exists())
        self.assertFalse((self.packages / "stray.txt").exists())
        self.assertIn("generated frontmatter validated", output)

    def test_country_package_carries_its_guides_bases_and_scaffolding(self) -> None:
        self.build()
        names = sorted(p.name for p in (self.packages / "zzland").iterdir())
        self.assertEqual(names, ["README.md", "foundation.md", "intake.md", "vat-workflow-base.md", "zz-vat.md"])
        self.assertEqual((self.packages / "zzland" / "zz-vat.md").read_text(encoding="utf-8"), GUIDE)
        self.assertEqual((self.packages / "zzland" / "vat-workflow-base.md").read_text(encoding="utf-8"), BASE)

    def test_every_state_and_province_package_and_both_indexes_are_written(self) -> None:
        self.build()
        for code in build_packages.US_STATE_CODES:
            self.assertTrue((self.packages / f"us-{code}" / "README.md").is_file(), code)
        for code in build_packages.CA_PROVINCE_CODES:
            self.assertTrue((self.packages / f"ca-{code}" / "README.md").is_file(), code)
        self.assertTrue((self.packages / "canada" / "README.md").is_file())
        self.assertTrue((self.packages / "us" / "README.md").is_file())

    def test_a_rebuild_is_idempotent(self) -> None:
        self.build()
        first = {p.relative_to(self.packages): p.read_bytes() for p in self.packages.rglob("*") if p.is_file()}
        self.build()
        second = {p.relative_to(self.packages): p.read_bytes() for p in self.packages.rglob("*") if p.is_file()}
        self.assertEqual(first, second)

    def test_out_builds_elsewhere_and_leaves_packages_alone(self) -> None:
        out_dir = self.root / "fresh"
        self.build("--out", str(out_dir))
        self.assertTrue((out_dir / "zzland" / "zz-vat.md").is_file())
        self.assertFalse((out_dir / "us-federal").exists(), "--out never copies the hand-authored packages")
        self.assertTrue((self.packages / "zzland" / "stale.md").is_file(), "packages/ was not rebuilt")
        self.assertTrue((self.packages / "stray.txt").is_file())

    def test_malformed_generated_frontmatter_fails_the_build(self) -> None:
        self.write({"skills/international/zzland/zz-broken.md": "---\nname: [unclosed\n---\n\nLine.\nLine.\nLine.\nLine.\nLine.\n"})
        err = io.StringIO()
        with contextlib.redirect_stderr(err), self.assertRaises(SystemExit) as caught:
            self.build()
        self.assertEqual(caught.exception.code, 1)
        self.assertIn("packages/zzland/zz-broken.md: invalid YAML frontmatter", err.getvalue())


class ArgumentGuardTests(SyntheticTreeCase):
    def test_out_requires_an_empty_or_missing_directory(self) -> None:
        self.assertIsNone(build_packages.output_dir([]))
        self.assertEqual(build_packages.output_dir(["--out", str(self.root / "new")]), str(self.root / "new"))
        empty = self.root / "empty"
        empty.mkdir()
        self.assertEqual(build_packages.output_dir(["--out", str(empty)]), str(empty))
        for argv in (["--out"], ["--out", "--us-only"], ["--out", str(self.packages)], ["--out", str(self.root / "packages" / "stray.txt")]):
            with self.subTest(argv=argv), self.assertRaises(SystemExit) as caught:
                build_packages.output_dir(argv)
            self.assertIn("--out", str(caught.exception))

    def test_out_cannot_be_combined_with_us_only(self) -> None:
        with self.assertRaises(SystemExit) as caught:
            self.build("--us-only", "--out", str(self.root / "new"))
        self.assertIn("cannot be combined", str(caught.exception))
        self.assertTrue((self.packages / "zzland" / "stale.md").is_file(), "nothing was rebuilt")


class DeclaredBasesTests(SyntheticTreeCase):
    def bases(self, text: str) -> list[str]:
        path = self.root / "skills" / "international" / "zzland" / "probe.md"
        path.write_text(text, encoding="utf-8")
        with mock.patch.object(build_packages, "SKILLS_DIR", str(self.skills)):
            return build_packages.declared_foundation_bases([str(path)])

    def test_list_and_legacy_flat_forms_name_existing_bases(self) -> None:
        self.assertEqual(self.bases(frontmatter("p", "depends_on:\n  - vat-workflow-base\n")), ["vat-workflow-base.md"])
        self.assertEqual(self.bases(frontmatter("p", "depends_on: - vat-workflow-base\n")), ["vat-workflow-base.md"])

    def test_missing_bases_paths_and_docs_are_ignored(self) -> None:
        self.assertEqual(self.bases(frontmatter("p", "depends_on:\n  - no-such-base\n  - ../vat-workflow-base\n")), [])
        self.assertEqual(self.bases("# Not a guide\n\n---\n\ndepends_on: vat-workflow-base\n"), [])
        self.assertEqual(self.bases(frontmatter("p", "depends_on: [unclosed\n")), [], "malformed frontmatter declares nothing")


class GeneratedFrontmatterValidationTests(SyntheticTreeCase):
    def test_reports_malformed_and_unclosed_blocks_and_skips_readmes(self) -> None:
        self.write({
            "packages/x/bad.md": "---\nname: [unclosed\n---\n",
            "packages/x/open.md": "---\nname: never closed\n",
            "packages/x/README.md": "---\nname: [readmes are docs\n---\n",
            "packages/x/good.md": frontmatter("good") + "\nBody.\n",
        })
        with mock.patch.object(build_packages, "PACKAGES_DIR", str(self.packages)):
            failures = build_packages.validate_generated_frontmatter()
        self.assertEqual(
            [f.split(":")[0] for f in failures],
            ["packages/x/bad.md", "packages/x/open.md"],
        )
        self.assertIn("invalid YAML frontmatter", failures[0])
        self.assertIn("never closes", failures[1])


if __name__ == "__main__":
    unittest.main()
