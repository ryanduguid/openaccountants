"""The reference advisory must scan its checkout from any working directory."""

import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class GuideReferenceTests(unittest.TestCase):
    def test_working_directory_does_not_change_the_scan(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "checkout"
            scripts = root / "scripts"
            helpers = scripts / "oa_tools"
            helpers.mkdir(parents=True)
            for name in ("__init__.py", "paths.py"):
                shutil.copyfile(REPO_ROOT / "scripts" / "oa_tools" / name, helpers / name)
            script = scripts / "check-guide-references.py"
            shutil.copyfile(REPO_ROOT / "scripts" / script.name, script)
            skills = root / "skills"
            skills.mkdir()
            (skills / "existing-tax.md").write_text("Existing guide\n", encoding="utf-8")
            (skills / "draft-tax.md").write_text(
                "Load `existing-tax` and `missing-tax`.\n", encoding="utf-8"
            )
            nested = root / "nested"
            nested.mkdir()
            unrelated = Path(directory) / "unrelated"
            (unrelated / "skills").mkdir(parents=True)
            (unrelated / "skills" / "outside-tax.md").write_text(
                "Load `outside-payroll`.\n", encoding="utf-8"
            )

            outputs = []
            for cwd in (root, nested, unrelated):
                with self.subTest(cwd=cwd.name):
                    result = subprocess.run(
                        [sys.executable, str(script)], cwd=cwd,
                        capture_output=True, text=True, encoding="utf-8", timeout=30,
                    )
                    outputs.append(result.stdout)
                    self.assertEqual(result.returncode, 0, result.stderr)
                    self.assertEqual(result.stderr, "")
                    self.assertIn("missing-tax", result.stdout)
                    self.assertIn(os.path.join("skills", "draft-tax.md") + ":1", result.stdout)
                    self.assertIn("distinct dangling references: 1   total uses: 1", result.stdout)
                    self.assertNotIn("existing-tax", result.stdout)
                    self.assertNotIn("outside-payroll", result.stdout)
            self.assertEqual(outputs, [outputs[0]] * 3)


if __name__ == "__main__":
    unittest.main()
