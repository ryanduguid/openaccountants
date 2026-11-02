"""scripts/merge-main.py, driven over throwaway Git repositories.

Each repository holds copies of the real merge script, coverage checker and
index, roster and llms-full generators, the real .gitattributes, and a stub
package builder (the real one needs the whole corpus). Two branches that each
add an unrelated guide conflict on every derived file under a plain merge;
what is pinned: merge-main resolves and rebuilds those without help, stops
before touching them when a source file conflicts, and finishes with
--continue once that conflict is resolved.
"""

from __future__ import annotations

import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = REPO_ROOT / "scripts"
COPIED = ("merge-main.py", "check-coverage-claims.py", "check-arithmetic.py",
          "build-index.py", "build-partners.py", "build-llms-full.py")
BASELINE = "scripts/baselines/arithmetic.txt"
STUB_PACKAGES = (
    "import os, shutil\n"
    "root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))\n"
    "packages, skills = os.path.join(root, 'packages'), os.path.join(root, 'skills', 'international')\n"
    "shutil.rmtree(packages, ignore_errors=True)\n"
    "for name in sorted(os.listdir(skills)):\n"
    "    shutil.copytree(os.path.join(skills, name), os.path.join(packages, name))\n"
)
HEADLINE = "**1 Guides** across **1 jurisdictions** · **0 accountant-reviewed** · **0 named accountants**"
ROWS = (
    "Guide files indexed", "Distinct `jurisdiction` codes", "`tier: 1` (accountant-reviewed)",
    "`tier: 2` (source-cited draft)", "Distinct `reviewed_by` values",
    "Country directories under `skills/international/`", "US jurisdiction codes (`US` + 50 states + DC)",
    "Generated bundles under `packages/`",
)


def load_merge_main():
    spec = importlib.util.spec_from_file_location("merge_main", SCRIPTS / "merge-main.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def guide(name: str, code: str, body: str = "Body.\n") -> str:
    return (f"---\nname: {name}\njurisdiction: {code}\ntier: 2\ncategory: international\n"
            f"last_updated: 2026-10-07\n---\n\n# {name}\n\n{body}")


class MergeMainTests(unittest.TestCase):
    def setUp(self) -> None:
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name) / "repo"
        scripts = self.root / "scripts"
        shutil.copytree(SCRIPTS / "oa_tools", scripts / "oa_tools", ignore=shutil.ignore_patterns("__pycache__"))
        for name in COPIED:
            shutil.copyfile(SCRIPTS / name, scripts / name)
        (scripts / "build-packages.py").write_text(STUB_PACKAGES, encoding="utf-8")
        shutil.copyfile(REPO_ROOT / ".gitattributes", self.root / ".gitattributes")
        coverage = ("# Coverage\n\n## This repository (derived from `index.json`)\n\n| Measure | This tree |\n|---|---|\n"
                    + "".join(f"| {label} | **0** |\n" for label in ROWS)
                    + "\nAccountant-reviewed guides exist in 0 of the 0 jurisdiction codes;\n\n## How to update\n\nRun make build.\n")
        self.write({
            ".gitignore": "__pycache__/\n",
            "README.md": "# Repo\n\nA tagline.\n\n" + HEADLINE + "\n",
            "llms.txt": "# Repo\n\n" + HEADLINE + "\n",
            "docs/QUALITY-TIERS.md": "# Tiers\n\n" + HEADLINE + "\n",
            "docs/COVERAGE.md": coverage,
            "docs/partners.json": "{}\n",
            "START-HERE.md": "Start here.\n",
            "skills/international/aa/aa-vat.md": guide("aa-vat", "AA"),
        })
        self.git("init", "-q", "-b", "main")
        for key, value in (("user.name", "Test"), ("user.email", "test@example.test"), ("commit.gpgsign", "false"),
                           ("core.autocrlf", "false"), ("core.hooksPath", str(Path(tmp.name) / "no-hooks"))):
            self.git("config", key, value)
        # one real gate baseline, empty: the corpus has no arithmetic findings
        recorded = self.run_script("check-arithmetic.py", "--update-baseline")
        self.assertEqual(recorded.returncode, 0, recorded.stdout + recorded.stderr)
        self.build_and_commit("base")

    def write(self, files: dict[str, str]) -> None:
        for rel, text in files.items():
            path = self.root / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(text.encode("utf-8"))

    def git(self, *args: str, check: bool = True) -> subprocess.CompletedProcess:
        result = subprocess.run(["git", *args], cwd=self.root, capture_output=True, text=True, encoding="utf-8")
        if check:
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        return result

    def run_script(self, *args: str) -> subprocess.CompletedProcess:
        return subprocess.run([sys.executable, "-X", "utf8", str(self.root / "scripts" / args[0]), *args[1:]],
                              cwd=self.root, capture_output=True, text=True, encoding="utf-8", timeout=120)

    def build_and_commit(self, message: str) -> None:
        for step in load_merge_main().BUILD:
            result = self.run_script(*step)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.git("add", "-A")
        self.git("commit", "-q", "-m", message)

    def two_branches(self, ours: dict[str, str], theirs: dict[str, str]) -> None:
        """`feature` changes `ours`, main changes `theirs`, each rebuilt; leaves feature checked out."""
        self.git("checkout", "-q", "-b", "feature")
        self.write(ours)
        self.build_and_commit("feature")
        self.git("checkout", "-q", "main")
        self.write(theirs)
        self.build_and_commit("main")
        self.git("checkout", "-q", "feature")

    def unmerged(self) -> list[str]:
        return self.git("diff", "--name-only", "--diff-filter=U").stdout.split()

    def blocking(self, stdout: str) -> list[str]:
        """The paths merge-main says need a person."""
        listed = stdout.split("need a person", 1)[1].splitlines()
        return [line.strip() for line in listed if line.startswith("  ") and "merge-main.py" not in line]

    def assert_rebuilt(self, codes: list[str]) -> None:
        guides = len(codes)
        index = json.loads((self.root / "index.json").read_text(encoding="utf-8"))
        self.assertEqual(sorted(g["jurisdiction"] for g in index["guides"]), [c.upper() for c in codes])
        for rel in ("README.md", "llms.txt", "docs/QUALITY-TIERS.md"):
            self.assertIn(f"**{guides} Guides** across **{guides} jurisdictions**",
                          (self.root / rel).read_text(encoding="utf-8"), rel)
        self.assertIn(f"exist in 0 of the {guides} jurisdiction codes",
                      (self.root / "docs/COVERAGE.md").read_text(encoding="utf-8"))
        self.assertEqual(sorted(p.name for p in (self.root / "packages").iterdir()), codes)
        self.assertEqual(self.unmerged(), [])
        self.assertEqual(self.git("diff", "--name-only").stdout, "", "a rebuilt file was left unstaged")
        gate = self.run_script("check-coverage-claims.py")
        self.assertEqual(gate.returncode, 0, gate.stdout)

    def test_unrelated_guides_merge_and_rebuild_without_help(self) -> None:
        self.two_branches({"skills/international/bb/bb-vat.md": guide("bb-vat", "BB")},
                          {"skills/international/cc/cc-vat.md": guide("cc-vat", "CC"),
                           "skills/international/dd/dd-vat.md": guide("dd-vat", "DD")})
        plain = self.git("merge-tree", "--write-tree", "--name-only", "--no-messages", "feature", "main", check=False)
        self.assertEqual(plain.returncode, 1, "the fixture must conflict under a plain merge")
        self.assertIn("index.json", plain.stdout)
        self.assertIn("README.md", plain.stdout)

        result = self.run_script("merge-main.py", "main")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assert_rebuilt(["aa", "bb", "cc", "dd"])
        self.git("commit", "-q", "--no-edit")

    def test_a_source_conflict_stops_before_the_derived_files_and_continue_finishes(self) -> None:
        self.two_branches(
            {"skills/international/bb/bb-vat.md": guide("bb-vat", "BB"),
             "skills/international/aa/aa-vat.md": guide("aa-vat", "AA", "Feature body.\n")},
            {"skills/international/cc/cc-vat.md": guide("cc-vat", "CC"),
             "skills/international/dd/dd-vat.md": guide("dd-vat", "DD"),
             "skills/international/aa/aa-vat.md": guide("aa-vat", "AA", "Main body.\n")},
        )
        result = self.run_script("merge-main.py", "main")
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertEqual(self.blocking(result.stdout), ["skills/international/aa/aa-vat.md"])
        self.assertIn("index.json", self.unmerged(), "a derived file was resolved before the sources were")
        self.assertIn("README.md", self.unmerged())

        self.write({"skills/international/aa/aa-vat.md": guide("aa-vat", "AA", "Agreed body.\n")})
        self.git("add", "skills/international/aa/aa-vat.md")
        result = self.run_script("merge-main.py", "--continue")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assert_rebuilt(["aa", "bb", "cc", "dd"])
        self.assertIn("Agreed body.", (self.root / "packages/aa/aa-vat.md").read_text(encoding="utf-8"))

    def test_a_conflict_in_a_figures_file_outside_its_figures_needs_a_person(self) -> None:
        self.two_branches(
            {"skills/international/bb/bb-vat.md": guide("bb-vat", "BB"),
             "README.md": "# Repo\n\nThe feature tagline.\n\n" + HEADLINE + "\n"},
            {"skills/international/cc/cc-vat.md": guide("cc-vat", "CC"),
             "skills/international/dd/dd-vat.md": guide("dd-vat", "DD"),
             "README.md": "# Repo\n\nThe main tagline.\n\n" + HEADLINE + "\n"},
        )
        result = self.run_script("merge-main.py", "main")
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertEqual(self.blocking(result.stdout), ["README.md"])

    def test_every_baseline_is_gated_including_a_clean_merge_and_on_every_continue(self) -> None:
        stale = "skills/international/aa/aa-vat.md::1 + 1 = 3"
        baseline = (self.root / BASELINE).read_text(encoding="utf-8")
        self.two_branches({"skills/international/bb/bb-vat.md": guide("bb-vat", "BB")},
                          {"skills/international/cc/cc-vat.md": guide("cc-vat", "CC"),
                           "skills/international/dd/dd-vat.md": guide("dd-vat", "DD"),
                           BASELINE: baseline + stale + "\n"})
        result = self.run_script("merge-main.py", "main")
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("check-arithmetic.py failed on the merged tree", result.stdout)
        self.assertNotIn(BASELINE, self.unmerged(), "the fixture must merge the baseline cleanly")

        again = self.run_script("merge-main.py", "--continue")
        self.assertEqual(again.returncode, 1, again.stdout + again.stderr)
        self.assertIn("check-arithmetic.py failed on the merged tree", again.stdout)

    def test_refuses_to_start_over_uncommitted_changes(self) -> None:
        self.write({"START-HERE.md": "Edited.\n"})
        result = self.run_script("merge-main.py", "main")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("commit or stash", result.stderr)

    def test_refuses_to_start_over_untracked_derived_files(self) -> None:
        self.write({"packages/aa/notes.md": "Mine.\n", "scratch.txt": "Not derived.\n"})
        result = self.run_script("merge-main.py", "main")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("packages/aa/notes.md", result.stderr)
        self.assertNotIn("scratch.txt", result.stderr)
        self.assertEqual((self.root / "packages/aa/notes.md").read_text(encoding="utf-8"), "Mine.\n")
        self.assertNotEqual(self.git("rev-parse", "-q", "--verify", "MERGE_HEAD", check=False).returncode, 0)

    def test_continue_refuses_untracked_derived_files_too(self) -> None:
        self.two_branches(
            {"skills/international/aa/aa-vat.md": guide("aa-vat", "AA", "Feature body.\n")},
            {"skills/international/aa/aa-vat.md": guide("aa-vat", "AA", "Main body.\n")},
        )
        self.assertEqual(self.run_script("merge-main.py", "main").returncode, 1)
        self.write({"skills/international/aa/aa-vat.md": guide("aa-vat", "AA", "Agreed body.\n"),
                    "packages/aa/notes.md": "Mine.\n"})
        self.git("add", "skills/international/aa/aa-vat.md")
        result = self.run_script("merge-main.py", "--continue")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("packages/aa/notes.md", result.stderr)
        self.assertEqual((self.root / "packages/aa/notes.md").read_text(encoding="utf-8"), "Mine.\n")


class BaselineMergeTests(unittest.TestCase):
    def test_an_entry_either_side_removed_goes_and_one_either_side_added_stays(self) -> None:
        merge = load_merge_main().merge_entries
        base = {"kept", "fixed on ours", "fixed on theirs", "fixed on both"}
        ours = {"kept", "fixed on theirs", "added on ours", "added on both"}
        theirs = {"kept", "fixed on ours", "added on theirs", "added on both"}
        self.assertEqual(merge(base, ours, theirs), {"kept", "added on ours", "added on theirs", "added on both"})


if __name__ == "__main__":
    unittest.main()
