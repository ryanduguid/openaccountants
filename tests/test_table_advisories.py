"""Table advisories scan their checkout by default and honour explicit trees."""

import os
import shutil
import subprocess  # nosec B404 - executes only the interpreter and copied fixture scripts.
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
CASES = {
    "check-band-continuity.py": (
        "| Taxable income | Rate |\n| --- | --- |\n"
        "| 0 - 100 | 10% |\n| 110 - 200 | 20% |\n| 201 - 300 | 30% |\n",
        "GAP of 9",
        ("bracket tables with a gap or overlap: {count}",),
    ),
    "check-derived-columns.py": (
        "| Taxable income | Rate | Cumulative tax |\n| --- | --- | --- |\n"
        "| 0 - 100 | 10% | 10 |\n| 101 - 200 | 20% | 28 |\n"
        "| 201 - 300 | 30% | 60 |\n",
        "bands give 30.00, column says 28.00",
        ("derived columns verified: {count}", "derived-column mismatches: {count}"),
    ),
    "check-total-rows.py": (
        "| Component | Rate |\n| --- | --- |\n"
        "| Pension | 10% |\n| Health | 20% |\n| Total | 40% |\n\n"
        "- **Total employer pension** - 20%\n"
        "- **Employer pension first pillar** - 5%\n"
        "- **Employer pension second pillar** - 10%\n",
        "components since the last total sum to 30.00%, row says 40%",
        ("total rows checked: {count} ; not equal to their components: {count}",
         "bullet totals checked: {count} ; not equal to their components: {count}"),
    ),
}


class TableAdvisoryTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name) / "checkout with spaces"
        scripts = self.root / "scripts"
        helpers = scripts / "oa_tools"
        helpers.mkdir(parents=True)
        for name in ("__init__.py", "paths.py"):
            shutil.copyfile(REPO_ROOT / "scripts" / "oa_tools" / name, helpers / name)
        for name in CASES:
            shutil.copyfile(REPO_ROOT / "scripts" / name, scripts / name)
        self.nested = self.root / "nested"
        self.nested.mkdir()
        self.unrelated = Path(temporary.name) / "unrelated"
        (self.unrelated / "skills").mkdir(parents=True)

    def run_advisory(self, name, cwd, args=()):
        # Arguments name only the interpreter and paths created in this fixture; no shell is used.
        # nosemgrep: python.lang.security.audit.dangerous-subprocess-use-audit.dangerous-subprocess-use-audit
        result = subprocess.run(  # nosec B603 - fixture paths, no external input.
            [sys.executable, str(self.root / "scripts" / name), *args], cwd=cwd,
            capture_output=True, text=True, encoding="utf-8", timeout=30,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr, "")
        return result.stdout

    def test_default_scan_is_independent_of_working_directory(self):
        for name, (text, finding, counters) in CASES.items():
            source = self.root / "skills" / "example" / "source.md"
            source.parent.mkdir(parents=True, exist_ok=True)
            source.write_text(text, encoding="utf-8")
            (self.unrelated / "skills" / "outside.md").write_text(text, encoding="utf-8")
            outputs = []
            for cwd in (self.root, self.nested, self.unrelated):
                with self.subTest(script=name, cwd=cwd.name):
                    output = self.run_advisory(name, cwd)
                    outputs.append(output)
                    self.assertIn(finding, output)
                    self.assertIn(os.path.join("skills", "example", "source.md"), output)
                    self.assertNotIn("outside.md", output)
                    self.assertNotIn(str(self.root), output)
                    for counter in counters:
                        self.assertIn(counter.format(count=1), output)
            with self.subTest(script=name, comparison="all directories"):
                self.assertEqual(outputs, [outputs[0]] * 3)

    def test_explicit_relative_and_absolute_directories_are_honoured(self):
        for name, (text, finding, counters) in CASES.items():
            default = self.root / "skills" / "default.md"
            default.parent.mkdir(parents=True, exist_ok=True)
            default.write_text(text, encoding="utf-8")
            requested = [self.root / "requested one", self.root / "requested two"]
            for index, tree in enumerate(requested):
                tree.mkdir(exist_ok=True)
                (tree / f"custom-{index}.md").write_text(text, encoding="utf-8")
            for mode in ("relative", "absolute"):
                with self.subTest(script=name, mode=mode):
                    args = [os.path.relpath(tree, self.unrelated) if mode == "relative"
                            else str(tree) for tree in requested]
                    output = self.run_advisory(name, self.unrelated, args)
                    self.assertIn(finding, output)
                    self.assertNotIn("default.md", output)
                    for index, arg in enumerate(args):
                        self.assertIn(os.path.join(arg, f"custom-{index}.md"), output)
                    for counter in counters:
                        self.assertIn(counter.format(count=2), output)


if __name__ == "__main__":
    unittest.main()
