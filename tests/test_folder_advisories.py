"""Folder advisories inspect their checkout independently of the caller's cwd."""

import os
import shutil
import subprocess  # nosec B404 - runs only the interpreter and copied repository scripts.
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class FolderAdvisoryTests(unittest.TestCase):
    def make_checkout(self, directory, script_names):
        root = Path(directory) / "checkout"
        scripts = root / "scripts"
        helpers = scripts / "oa_tools"
        helpers.mkdir(parents=True)
        for name in ("__init__.py", "paths.py", "frontmatter.py"):
            shutil.copyfile(REPO_ROOT / "scripts" / "oa_tools" / name, helpers / name)
        for name in script_names:
            shutil.copyfile(REPO_ROOT / "scripts" / name, scripts / name)
        folder = root / "skills" / "international" / "example"
        folder.mkdir(parents=True)
        for name, code in (("listed-tax", "AA"), ("hidden-payroll", "AA"), ("misplaced-tax", "BB")):
            (folder / (name + ".md")).write_text(
                f"---\njurisdiction: {code}\n---\nGuide\n", encoding="utf-8"
            )
        (folder / "README.md").write_text(
            "# Files\n`listed-tax`\n`missing-tax`\n`shared-example`\n"
            "## What's NOT covered\n- Payroll\n", encoding="utf-8"
        )
        docs = root / "docs"
        docs.mkdir()
        (docs / "shared-example.md").write_text("Shared document\n", encoding="utf-8")
        state = root / "skills" / "us-states" / "wa"
        state.mkdir(parents=True)
        (state / "arizona-sales-tax.md").write_text(
            "---\njurisdiction: US-WA\n---\nGuide\n", encoding="utf-8"
        )
        for index in (root / "skills" / "README.md", state.parent / "README.md"):
            index.write_text("`missing-index-tax`\n", encoding="utf-8")
        nested = root / "nested"
        nested.mkdir()
        unrelated = Path(directory) / "unrelated"
        foreign = unrelated / "skills" / "international" / "foreign"
        foreign.mkdir(parents=True)
        (foreign / "foreign-tax.md").write_text(
            "---\njurisdiction: CC\n---\nGuide\n", encoding="utf-8"
        )
        (foreign / "README.md").write_text("`foreign-missing-tax`\n", encoding="utf-8")
        return scripts, (root, nested, unrelated)

    def test_advisories_scan_their_own_checkout(self):
        summaries = {
            "check-readme-inventory.py": (
                'folders checked: 1 ; phantom entries: 1 ; omitted guides: 2 ; '
                'false "not covered" claims: 1'
            ),
            "check-jurisdiction-placement.py": (
                "directories scanned: 2 ; misplaced guides: 2"
            ),
        }
        with tempfile.TemporaryDirectory() as directory:
            scripts, working_directories = self.make_checkout(directory, summaries)

            for name, summary in summaries.items():
                outputs = []
                for cwd in working_directories:
                    with self.subTest(script=name, cwd=cwd.name):
                        # The interpreter and script path are fixed locally; cwd is a private fixture.
                        # nosemgrep: python.lang.security.audit.dangerous-subprocess-use-audit.dangerous-subprocess-use-audit
                        result = subprocess.run(  # nosec B603 - controlled paths, no shell or external input.
                            [sys.executable, str(scripts / name)], cwd=cwd,
                            capture_output=True, text=True, encoding="utf-8", timeout=30,
                        )
                        outputs.append(result.stdout)
                        self.assertEqual(result.returncode, 0, result.stderr)
                        self.assertEqual(result.stderr, "")
                        self.assertIn(summary, result.stdout)
                        self.assertNotIn("foreign", result.stdout)
                        self.assertNotIn("shared-example", result.stdout)
                        self.assertNotIn("missing-index-tax", result.stdout)
                        if name == "check-readme-inventory.py":
                            self.assertIn(os.path.join("skills", "international", "example", "README.md"), result.stdout)
                            self.assertIn("lists files that do not exist: missing-tax", result.stdout)
                            self.assertIn("omits guides that are in the folder: hidden-payroll, misplaced-tax", result.stdout)
                            self.assertIn("but the folder has: hidden-payroll", result.stdout)
                        else:
                            self.assertIn("jurisdiction BB, but its directory is 2 x AA", result.stdout)
                            self.assertIn("named for Arizona (AZ) but sits under us-states/wa", result.stdout)
                with self.subTest(script=name, comparison="working directories"):
                    self.assertEqual(outputs, [outputs[0]] * 3)


if __name__ == "__main__":
    unittest.main()
