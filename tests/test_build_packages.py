"""Tests for scripts/build-packages.py, the generator behind packages/.

It is the largest script in the repository and had no tests; CHANGELOG.md
records a rebuild that wiped the hand-authored packages/us-federal/. These
tests build a synthetic skills/ tree into a scratch packages/ directory and
pin the properties that matter: hand-authored packages survive a rebuild
byte for byte, stale generated files are removed, a package holds only its
own files and lists the shared ones (written once to packages/_shared/ and
recorded in packages/bundles.json), `--out` builds elsewhere and leaves
packages/ alone, the argument guards refuse the dangerous cases, and the
generator fails closed on its own malformed output.
"""

from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import shutil
import subprocess
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
            "packages/_shared/stale-base.md": frontmatter("stale-base") + "\nLeft over from an earlier build.\n",
            "packages/stray.txt": "not a package\n",
        })

    def write(self, files: dict[str, str]) -> None:
        for rel, text in files.items():
            path = self.root / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8", newline="\n")

    def build(self, *argv: str) -> str:
        out = io.StringIO()
        with contextlib.ExitStack() as stack:
            stack.enter_context(mock.patch.object(build_packages, "SKILLS_DIR", str(self.skills)))
            stack.enter_context(mock.patch.object(build_packages, "PACKAGES_DIR", str(self.packages)))
            stack.enter_context(mock.patch.object(sys, "argv", ["build-packages.py", *argv]))
            stack.enter_context(contextlib.redirect_stdout(out))
            build_packages.main()
        return out.getvalue()

    def bundles(self, packages: Path | None = None) -> dict:
        return json.loads(((packages or self.packages) / "bundles.json").read_text(encoding="utf-8"))


class RebuildTests(SyntheticTreeCase):
    def test_generated_text_is_utf8_with_lf_on_every_platform(self) -> None:
        self.build()
        for path in self.packages.rglob("*"):
            if path.is_file():
                with self.subTest(path=path.relative_to(self.packages)):
                    content = path.read_bytes()
                    content.decode("utf-8")
                    self.assertNotIn(b"\r\n", content)

    def test_hand_authored_packages_survive_and_stale_output_is_removed(self) -> None:
        output = self.build()
        self.assertEqual((self.packages / "us-federal" / "us-form-1040.md").read_text(encoding="utf-8"), FEDERAL_GUIDE)
        self.assertEqual((self.packages / "us-federal" / "rates.2026.json").read_text(encoding="utf-8"), '{"tax_year": 2026}\n')
        self.assertEqual(sorted(p.name for p in (self.packages / "us-federal").iterdir()), ["rates.2026.json", "us-form-1040.md"])
        self.assertFalse((self.packages / "zzland" / "stale.md").exists())
        self.assertFalse((self.packages / "_shared" / "stale-base.md").exists())
        self.assertFalse((self.packages / "stray.txt").exists())
        self.assertIn("generated frontmatter validated", output)

    def test_country_package_holds_its_own_files_and_lists_the_shared_ones(self) -> None:
        self.build()
        names = sorted(p.name for p in (self.packages / "zzland").iterdir())
        self.assertEqual(names, ["README.md", "intake.md", "zz-vat.md"])
        self.assertEqual((self.packages / "zzland" / "zz-vat.md").read_text(encoding="utf-8"), GUIDE)
        readme = (self.packages / "zzland" / "README.md").read_text(encoding="utf-8")
        self.assertIn("## Shared files this package needs", readme)
        self.assertIn("[`vat-workflow-base.md`](../_shared/vat-workflow-base.md)", readme)
        self.assertIn("[`foundation.md`](../_shared/foundation.md)", readme)
        self.assertIn("Upload ALL files in this folder AND the shared files listed above", readme)
        self.assertIn("make bundle JURISDICTION=<folder>", readme)

    def test_shared_files_are_written_once_and_recorded_in_bundles_json(self) -> None:
        self.build()
        shared = self.packages / "_shared"
        self.assertEqual((shared / "vat-workflow-base.md").read_text(encoding="utf-8"), BASE)
        self.assertTrue((shared / "foundation.md").is_file())
        shared_readme = (shared / "README.md").read_text(encoding="utf-8")
        self.assertIn("`vat-workflow-base.md` — skills/foundation/vat-workflow-base.md; listed by 1 package\n", shared_readme)
        self.assertRegex(shared_readme, r"`foundation\.md` — generated by scripts/build-packages\.py; listed by \d+ packages\n")

        bundles = self.bundles()
        self.assertEqual(bundles["shared_dir"], "_shared")
        entry = bundles["packages"]["zzland"]
        self.assertEqual(entry["jurisdiction"], "ZZ")
        self.assertEqual(entry["files"], ["intake.md", "zz-vat.md", "README.md"])
        self.assertEqual(entry["shared"], ["foundation.md", "vat-workflow-base.md"])
        self.assertNotIn("us-federal", bundles["packages"], "hand-authored data is not a bundle")
        self.assertNotIn("_shared", bundles["packages"])
        for name, package in bundles["packages"].items():
            with self.subTest(package=name):
                self.assertEqual(sorted(package["files"]), sorted(p.name for p in (self.packages / name).iterdir()))
                for shared_name in package["shared"]:
                    self.assertTrue((shared / shared_name).is_file(), shared_name)
                self.assertFalse(set(package["files"]) & set(package["shared"]), "a file is both own and shared")

    def test_no_package_carries_a_copy_of_a_shared_file(self) -> None:
        self.build()
        shared_names = {p.name for p in (self.packages / "_shared").iterdir()} - {"README.md"}
        self.assertTrue(shared_names)
        for package in self.packages.iterdir():
            if not package.is_dir() or package.name in ("_shared", "us-federal"):
                continue
            own = {p.name for p in package.iterdir()}
            self.assertFalse(own & shared_names, f"{package.name} holds a copy of {sorted(own & shared_names)}")

    def test_one_shared_name_cannot_carry_two_contents(self) -> None:
        build_packages._SHARED.clear()
        self.addCleanup(build_packages._SHARED.clear)
        self.assertEqual(build_packages.share("x.md", text="a"), "x.md")
        self.assertEqual(build_packages.share("x.md", text="a"), "x.md")  # the same content again is fine
        with self.assertRaises(SystemExit) as caught:
            build_packages.share("x.md", text="b")
        self.assertIn("'x.md' registered with two different contents", str(caught.exception))

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
        out_dir.mkdir()
        self.build("--out", str(out_dir))
        self.assertTrue((out_dir / "zzland" / "zz-vat.md").is_file())
        self.assertTrue((out_dir / "_shared" / "vat-workflow-base.md").is_file())
        self.assertIn("zzland", self.bundles(out_dir)["packages"])
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
        for argv in (["--out"], ["--out", "--verbose"], ["--out", str(self.packages)], ["--out", str(self.root / "packages" / "stray.txt")]):
            with self.subTest(argv=argv), self.assertRaises(SystemExit) as caught:
                build_packages.output_dir(argv)
            self.assertIn("--out", str(caught.exception))

    def test_an_unknown_option_is_refused_rather_than_ignored(self) -> None:
        # --us-only went with the shared directory: a partial build cannot
        # write a bundles.json that describes the whole tree.
        for argv in (["--us-only"], ["--us-only", "--out", str(self.root / "new")]):
            with self.subTest(argv=argv), self.assertRaises(SystemExit) as caught:
                self.build(*argv)
            self.assertIn("unknown option --us-only", str(caught.exception))
        self.assertTrue((self.packages / "zzland" / "stale.md").is_file(), "nothing was rebuilt")


class DependencyPreflightTests(SyntheticTreeCase):
    def setUp(self) -> None:
        super().setUp()
        result = subprocess.run(
            [sys.executable, "-I", "-S", "-c", "import yaml"],
            capture_output=True, encoding="utf-8", timeout=30,
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("ModuleNotFoundError: No module named 'yaml'", result.stderr)

    def copy_generator(self) -> Path:
        scripts = self.root / "scripts"
        helpers = scripts / "oa_tools"
        helpers.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(SCRIPTS / "build-packages.py", scripts / "build-packages.py")
        for name in ("__init__.py", "paths.py", "frontmatter.py"):
            shutil.copyfile(SCRIPTS / "oa_tools" / name, helpers / name)
        return scripts / "build-packages.py"

    def run_without_dependencies(self, *argv: str) -> subprocess.CompletedProcess:
        return subprocess.run(
            [sys.executable, "-I", "-S", str(self.copy_generator()), *argv],
            capture_output=True, encoding="utf-8", timeout=30,
        )

    def package_bytes(self) -> dict[Path, bytes]:
        return {path.relative_to(self.packages): path.read_bytes()
                for path in self.packages.rglob("*") if path.is_file()}

    def test_missing_dependency_preserves_existing_generated_and_hand_authored_files(self) -> None:
        before = self.package_bytes()
        result = self.run_without_dependencies()
        self.assertEqual(result.returncode, 1)
        self.assertIn("yaml", result.stderr.lower())
        self.assertEqual(self.package_bytes(), before)

    def test_missing_dependency_does_not_create_an_out_directory(self) -> None:
        before = self.package_bytes()
        parent = self.root / "missing-parent"
        target = parent / "new"
        result = self.run_without_dependencies("--out", str(target))
        self.assertEqual(result.returncode, 1)
        self.assertIn("yaml", result.stderr.lower())
        self.assertFalse(target.exists())
        self.assertFalse(parent.exists())
        self.assertEqual(self.package_bytes(), before)

    def test_missing_dependency_leaves_an_existing_empty_out_directory_empty(self) -> None:
        before = self.package_bytes()
        target = self.root / "empty"
        target.mkdir()
        result = self.run_without_dependencies("--out", str(target))
        self.assertEqual(result.returncode, 1)
        self.assertIn("yaml", result.stderr.lower())
        self.assertEqual(list(target.iterdir()), [])
        self.assertEqual(self.package_bytes(), before)

    def test_invalid_arguments_take_precedence_over_the_missing_dependency(self) -> None:
        before = self.package_bytes()
        target = self.root / "new"
        for argv, message in (
            (("--unknown",), "unknown option --unknown"),
            (("--out", str(target), "--unknown"), "unknown option --unknown"),
            (("--out",), "--out requires a directory path"),
            (("--out", "--unknown"), "unknown option --unknown"),
            (("--out", str(self.packages)), "must not exist or must be empty"),
            (("--out", str(self.packages / "stray.txt")), "must not exist or must be empty"),
        ):
            with self.subTest(argv=argv):
                result = self.run_without_dependencies(*argv)
                self.assertEqual(result.returncode, 1)
                self.assertIn(message, result.stderr)
                self.assertNotIn("yaml", result.stderr.lower())
                self.assertFalse(target.exists())
                self.assertEqual(self.package_bytes(), before)

    def test_reader_initialisation_failure_precedes_output_and_state_changes(self) -> None:
        marker = object()

        def unavailable(block):
            self.assertEqual(build_packages.PACKAGES_DIR, str(self.packages))
            self.assertEqual(build_packages._SHARED, {"sentinel": marker})
            raise ModuleNotFoundError("No module named 'yaml'", name="yaml")

        with mock.patch.dict(build_packages._SHARED, {"sentinel": marker}, clear=True), \
                mock.patch.object(build_packages, "load_frontmatter", side_effect=unavailable), \
                mock.patch.object(build_packages.os, "makedirs") as make_directory:
            with self.assertRaises(ModuleNotFoundError):
                self.build("--out", str(self.root / "new"))
            make_directory.assert_not_called()
            self.assertEqual(build_packages._SHARED, {"sentinel": marker})

    def test_cold_generator_import_and_tolerant_reader_do_not_import_yaml(self) -> None:
        code = '''
import builtins
import importlib.util
import sys

attempts = []
original_import = builtins.__import__

def tracked_import(name, *args, **kwargs):
    if name == "yaml" or name.startswith("yaml."):
        attempts.append(name)
    return original_import(name, *args, **kwargs)

builtins.__import__ = tracked_import
spec = importlib.util.spec_from_file_location("generator", sys.argv[1])
generator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(generator)
from oa_tools import frontmatter
text = "---\\nname: x\\nname: y\\nbroken: [\\n---\\n"
block = frontmatter.extract_frontmatter(text)
if frontmatter.parse_known_keys(block)["name"] != "x":
    raise RuntimeError("Tolerant block parsing changed")
if frontmatter.read_frontmatter(text, strict=False)["name"] != "x":
    raise RuntimeError("Tolerant document parsing changed")
if attempts:
    raise RuntimeError("Import or tolerant reading attempted a YAML import")
try:
    frontmatter.load_frontmatter("name: generator-preflight\\n")
except ModuleNotFoundError as exc:
    if exc.name != "yaml":
        raise
else:
    raise RuntimeError("Strict reader did not fail without PyYAML")
if attempts != ["yaml"]:
    raise RuntimeError("Strict reader did not attempt the YAML import")
'''
        result = subprocess.run(
            [sys.executable, "-I", "-S", "-c", code, str(self.copy_generator())],
            capture_output=True, encoding="utf-8", timeout=30,
        )
        self.assertEqual(result.returncode, 0, result.stderr)


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


class PackagingCompletenessTests(SyntheticTreeCase):
    """Every guide under skills/ reaches a package.

    Until 2026-09-29 57 indexed guides reached none: orchestrators were found
    through a hand-kept map of twelve countries, a redirect heuristic dropped
    a short guide that said "consolidated revenue", the cross-border bundle
    read only its top level and treaty-corridors/, and financial-reporting/,
    patterns/ and intelligence/ had no bundle at all.
    """

    BODY = "\n# Guide\n\nLine.\nLine.\nLine.\nLine.\n"

    def test_orchestrators_are_found_by_the_package_code(self) -> None:
        self.write({
            "skills/orchestrator/zz-freelance-intake.md": frontmatter("zz-freelance-intake") + self.BODY,
            "skills/orchestrator/zz-return-assembly.md": frontmatter("zz-return-assembly") + self.BODY,
            "skills/orchestrator/zy-freelance-intake.md": frontmatter("zy-freelance-intake") + self.BODY,
        })
        self.build()
        names = sorted(p.name for p in (self.packages / "zzland").iterdir())
        self.assertEqual(names, ["README.md", "intake.md", "zz-vat.md", "zzland-guided-intake.md", "zzland-return-assembly.md"])
        self.assertEqual(
            (self.packages / "zzland" / "zzland-guided-intake.md").read_text(encoding="utf-8"),
            (self.skills / "orchestrator" / "zz-freelance-intake.md").read_text(encoding="utf-8"),
        )
        self.assertIn("zzland-return-assembly.md", self.bundles()["packages"]["zzland"]["files"])

    def test_a_short_guide_that_mentions_consolidation_is_packaged(self) -> None:
        self.write({
            "skills/international/zzland/zz-cit.md": frontmatter("zz-cit")
            + "\n# CIT\n\nGroups with consolidated revenue above the threshold are in scope.\nLine.\nLine.\n",
        })
        self.build()
        self.assertTrue((self.packages / "zzland" / "zz-cit.md").is_file())

    def test_domain_bundles_take_nested_guides_and_disambiguate_shared_basenames(self) -> None:
        self.write({
            "skills/cross-border/README.md": "# Source-tree notes, not a guide\n",
            "skills/cross-border/top.md": frontmatter("top") + self.BODY,
            "skills/cross-border/us-expat/us-feie.md": frontmatter("us-feie") + self.BODY,
            "skills/cross-border/treaty-corridors/x-y/dtt-summary.md": frontmatter("x-y-dtt-corridor") + self.BODY,
            "skills/cross-border/treaty-corridors/x-z/dtt-summary.md": frontmatter("x-z-dtt-corridor") + self.BODY,
            "skills/cross-border/treaty-corridors/_templates/dtt-template.md": frontmatter("dtt-template") + self.BODY,
            "skills/financial-reporting/leases/ifrs16.md": frontmatter("ifrs16") + self.BODY,
            "skills/patterns/README.md": "# Source-tree notes\n",
            "skills/patterns/global-saas.md": frontmatter("global-saas") + self.BODY,
            "skills/intelligence/deadline-engine.md": frontmatter("deadline-engine") + self.BODY,
        })
        self.build()
        self.assertEqual(
            sorted(p.name for p in (self.packages / "_cross-border").iterdir()),
            ["README.md", "top.md", "us-feie.md", "x-y-dtt-summary.md", "x-z-dtt-summary.md"],
        )
        bundles = self.bundles()["packages"]
        self.assertEqual(bundles["_cross-border"]["jurisdiction"], "CROSS-BORDER")
        self.assertEqual(bundles["_cross-border"]["files"],
                         ["top.md", "us-feie.md", "x-y-dtt-summary.md", "x-z-dtt-summary.md", "README.md"])
        self.assertEqual(bundles["_financial-reporting"]["files"], ["ifrs16.md", "README.md"])
        self.assertEqual(bundles["_patterns"]["files"], ["global-saas.md", "README.md"])
        self.assertEqual(bundles["_intelligence"]["files"], ["deadline-engine.md", "README.md"])
        self.assertIn("# Financial Reporting Skills",
                      (self.packages / "_financial-reporting" / "README.md").read_text(encoding="utf-8"))

    def test_two_guides_that_would_share_a_packaged_name_fail_the_build(self) -> None:
        self.write({
            "skills/patterns/p-x.md": frontmatter("p-x") + self.BODY,
            "skills/patterns/p/x.md": frontmatter("px") + self.BODY,
            "skills/patterns/q/x.md": frontmatter("qx") + self.BODY,
        })
        with self.assertRaises(SystemExit) as caught:
            self.build()
        self.assertIn("two guides would be packaged under one name", str(caught.exception))


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
