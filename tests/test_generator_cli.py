"""Generator arguments cannot start work or replace output before validation."""

import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
GENERATORS = {
    "build-index.py": "index.json",
    "build-llms-full.py": "llms-full.txt",
    "build-partners.py": "PARTNERS.md",
    "build-form-register.py": "docs/FORM-REGISTER.md",
}
OUTPUT_GENERATORS = tuple(name for name in GENERATORS if name != "build-form-register.py")
SENTINEL = b"OWNED SYNTHETIC OUTPUT SENTINEL\n"
BLOCK_WORK = (
    "import builtins, os, runpy, sys\n"
    "def unexpected(*args, **kwargs):\n"
    "    raise AssertionError('unexpected generation or file access')\n"
    "builtins.open = os.walk = unexpected\n"
    "sys.argv = sys.argv[1:]\n"
    "runpy.run_path(sys.argv[0], run_name='__main__')\n"
)
LOAD_GENERATOR = (
    "import importlib.util, sys\n"
    "spec = importlib.util.spec_from_file_location('generator', sys.argv[1])\n"
    "mod = importlib.util.module_from_spec(spec)\n"
    "spec.loader.exec_module(mod)\n"
)


class GeneratorCliTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name) / "checkout with spaces"
        scripts = self.root / "scripts"
        shutil.copytree(SCRIPTS / "oa_tools", scripts / "oa_tools",
                        ignore=shutil.ignore_patterns("__pycache__"))
        for name in GENERATORS:
            shutil.copyfile(SCRIPTS / name, scripts / name)
        folder = self.root / "skills/international/example"
        folder.mkdir(parents=True)
        for name in ("first", "second"):
            (folder / (name + ".md")).write_text(
                "---\nname: example-" + name + "\njurisdiction: XX\ntier: 2\n"
                "category: international\nlast_updated: 2026-10-07\n---\n"
                "Synthetic Form X123.\n", encoding="utf-8")
        (self.root / "docs").mkdir()
        (self.root / "docs/partners.json").write_text("{}\n", encoding="utf-8")
        self.inputs = {
            "llms.txt": b"Synthetic entry point.\n",
            "START-HERE.md": b"Synthetic instructions.\n",
            "docs/QUALITY-TIERS.md": b"Synthetic quality definitions.\n",
            "PARTNERS.md": b"Synthetic roster input.\n",
            "index.json": json.dumps({
                "counts": {"guides": 1, "jurisdictions": 1, "accountant_reviewed": 0},
                "guides": [{"slug": "synthetic", "jurisdiction": "XX", "tier": 2}],
            }).encode("utf-8"),
        }
        self.restore_inputs()
        self.nested = self.root / "nested"
        self.nested.mkdir()
        self.foreign = Path(temporary.name) / "foreign caller"
        self.foreign.mkdir()
        (self.foreign / "docs").mkdir()
        (self.foreign / "index.json").write_bytes(b"foreign inventory\n")
        (self.foreign / "docs/FORM-REGISTER.md").write_bytes(b"foreign register\n")

    def restore_inputs(self):
        for path, data in self.inputs.items():
            (self.root / path).write_bytes(data)

    def run_generator(self, name, argv, cwd=None, *, blocked=False, optimised=False):
        command = [sys.executable, "-X", "utf8"]
        if optimised:
            command.append("-OO")
        if blocked:
            command += ["-c", BLOCK_WORK]
        return subprocess.run(
            [*command, str(self.root / "scripts" / name), *argv],
            cwd=cwd or self.root, capture_output=True, timeout=30,
        )

    def assert_no_write(self, name, argv, expected, cwd, *, blocked=True):
        target = self.root / GENERATORS[name]
        before = target.read_bytes() if target.exists() else None
        explicit = cwd / "existing output.txt"
        explicit.write_bytes(SENTINEL)
        result = self.run_generator(name, argv, cwd, blocked=blocked)
        self.assertEqual(result.returncode, expected, result.stderr.decode("utf-8"))
        self.assertNotIn(b"Traceback", result.stderr)
        self.assertEqual(target.read_bytes() if target.exists() else None, before)
        self.assertEqual(explicit.read_bytes(), SENTINEL)
        if expected == 0:
            self.assertIn(b"usage:", result.stdout)
            self.assertEqual(result.stderr, b"")
        else:
            self.assertEqual(result.stdout, b"")
            self.assertIn(b"error:", result.stderr)

    def test_help_skips_generation_from_each_caller(self):
        for name in GENERATORS:
            for cwd in (self.root, self.nested, self.foreign):
                for argv in (["--help"], ["-h"]):
                    with self.subTest(name=name, cwd=cwd.name, argv=argv):
                        self.assert_no_write(name, argv, 0, cwd)

    def test_unknown_arguments_fail_before_help_or_generation(self):
        for name in GENERATORS:
            for argv in (["--unknown"], ["--he"], ["unexpected"],
                         ["--help", "--unknown"], ["--unknown", "--help"],
                         ["--help", "unexpected"], ["--", "--help"]):
                with self.subTest(name=name, argv=argv):
                    self.assert_no_write(name, argv, 2, self.foreign)

    def test_invalid_output_arguments_do_not_replace_either_path(self):
        for name in OUTPUT_GENERATORS:
            for argv in (["--out"], ["--out", "--help"], ["--out", ""], ["--out="],
                         ["--out", "existing output.txt", "--out", "second.txt"],
                         ["--out", "existing output.txt", "--out", "existing output.txt"],
                         ["--out=existing output.txt", "--out=second.txt"],
                         ["--out", "existing output.txt", "--out=second.txt", "--help"],
                         ["--help", "--out"], ["--out", "--unknown"]):
                with self.subTest(name=name, argv=argv):
                    self.assert_no_write(name, argv, 2, self.foreign)
                    self.assertFalse((self.foreign / "second.txt").exists())

    def test_valid_help_with_output_does_not_write(self):
        for name in OUTPUT_GENERATORS:
            for argv in (["--out", "existing output.txt", "--help"],
                         ["--help", "--out=existing output.txt"],
                         ["--out", "missing parent/output.txt", "--help"]):
                with self.subTest(name=name, argv=argv):
                    self.assert_no_write(name, argv, 0, self.foreign)

    def test_docstring_free_entrypoints_validate_and_generate(self):
        for name in GENERATORS:
            for argv, expected in ((["--help"], 0), (["--unknown"], 2),
                                   (["--help", "--unknown"], 2)):
                with self.subTest(name=name, argv=argv):
                    target = self.root / GENERATORS[name]
                    before = target.read_bytes() if target.exists() else None
                    result = self.run_generator(name, argv, self.foreign,
                                                blocked=True, optimised=True)
                    self.assertEqual(result.returncode, expected, result.stderr)
                    self.assertNotIn(b"Traceback", result.stderr)
                    self.assertEqual(target.read_bytes() if target.exists() else None, before)
                    if expected == 0:
                        self.assertIn(b"usage:", result.stdout)
                        self.assertEqual(result.stderr, b"")
                    else:
                        self.assertEqual(result.stdout, b"")
                        self.assertIn(b"error:", result.stderr)
            for cwd in (self.root, self.nested, self.foreign):
                with self.subTest(name=name, cwd=cwd.name):
                    self.restore_inputs()
                    target = self.root / GENERATORS[name]
                    target.unlink(missing_ok=True)
                    normal = self.run_generator(name, [], cwd)
                    self.assertEqual(normal.returncode, 0, normal.stderr)
                    self.assertTrue(target.is_file())
                    expected = target.read_bytes()
                    self.restore_inputs()
                    target.unlink()
                    result = self.run_generator(name, [], cwd, optimised=True)
                    self.assertEqual(result.returncode, 0, result.stderr)
                    self.assertEqual(result.stdout, normal.stdout)
                    self.assertEqual(result.stderr, normal.stderr)
                    self.assertTrue(target.is_file())
                    actual = target.read_bytes()
                    if name == "build-index.py":
                        before, after = json.loads(expected), json.loads(actual)
                        before.pop("generated_at")
                        after.pop("generated_at")
                        self.assertEqual(after, before)
                    else:
                        self.assertEqual(actual, expected)
                    self.assertEqual((self.foreign / "index.json").read_bytes(), b"foreign inventory\n")
                    self.assertEqual((self.foreign / "docs/FORM-REGISTER.md").read_bytes(),
                                     b"foreign register\n")

    def test_successful_output_is_relative_to_the_caller(self):
        for name in OUTPUT_GENERATORS:
            self.restore_inputs()
            default = self.run_generator(name, [])
            self.assertEqual(default.returncode, 0, default.stderr)
            expected = (self.root / GENERATORS[name]).read_bytes()
            for cwd in (self.root, self.nested, self.foreign):
                for path, equal_form in (("result with spaces.txt", False), ("-legacy.txt", False),
                                         ("-h", False), ("-", False), ("-result.txt", True),
                                         ("--help", True), ("résult=out.txt", False)):
                    with self.subTest(name=name, cwd=cwd.name, path=path):
                        self.restore_inputs()
                        argv = ["--out=" + path] if equal_form else ["--out", path]
                        result = self.run_generator(name, argv, cwd)
                        self.assertEqual(result.returncode, 0, result.stderr)
                        self.assertTrue((cwd / path).is_file(), "explicit output missing")
                        actual = (cwd / path).read_bytes()
                        if name == "build-index.py":
                            before, after = json.loads(expected), json.loads(actual)
                            before.pop("generated_at")
                            after.pop("generated_at")
                            self.assertEqual(after, before)
                        else:
                            self.assertEqual(actual, expected)

    def test_missing_llms_input_preserves_existing_output(self):
        for missing in self.inputs:
            for argv in ([], ["--out", "existing output.txt"]):
                for exists in (True, False):
                    with self.subTest(missing=missing, argv=argv, exists=exists):
                        self.restore_inputs()
                        (self.root / missing).unlink()
                        target = self.root / ("existing output.txt" if argv else "llms-full.txt")
                        if exists:
                            target.write_bytes(SENTINEL)
                        elif target.exists():
                            target.unlink()
                        result = self.run_generator("build-llms-full.py", argv)
                        self.assertNotEqual(result.returncode, 0)
                        self.assertIn(("required file missing: " + missing).encode(),
                                      result.stderr.replace(b"\\", b"/"))
                        self.assertEqual(result.stdout, b"")
                        self.assertEqual(target.read_bytes() if target.exists() else None,
                                         SENTINEL if exists else None)

    def test_malformed_llms_input_preserves_existing_output(self):
        variants = (("index.json", b"{invalid json", b"JSONDecodeError"),
                    ("index.json", b"{}", b"KeyError"),
                    ("llms.txt", b"\xff", b"UnicodeDecodeError"),
                    ("PARTNERS.md", b"\xff", b"UnicodeDecodeError"))
        for path, data, error in variants:
            with self.subTest(path=path, data=data):
                self.restore_inputs()
                (self.root / path).write_bytes(data)
                target = self.root / "existing output.txt"
                target.write_bytes(SENTINEL)
                result = self.run_generator("build-llms-full.py", ["--out", target.name])
                self.assertNotEqual(result.returncode, 0)
                self.assertIn(error, result.stderr)
                self.assertEqual(result.stdout, b"")
                self.assertEqual(target.read_bytes(), SENTINEL)

    def test_form_selftest_still_parses_complete_arguments(self):
        result = self.run_generator("build-form-register.py", ["--selftest"], blocked=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(b"selftest: refusal codes excluded, real forms kept", result.stdout)
        for argv in (["--selftest", "--unknown"], ["--unknown", "--selftest"],
                     ["--selftest", "unexpected"]):
            with self.subTest(argv=argv):
                self.assert_no_write("build-form-register.py", argv, 2, self.root)
        self.assert_no_write("build-form-register.py", ["--selftest", "--help"], 0, self.root)
        self.assert_no_write("build-form-register.py", ["--out", "existing output.txt"], 2, self.root)

    def test_later_llms_read_failure_preserves_existing_output(self):
        driver = LOAD_GENERATOR + (
            "original = mod.read_text\n"
            "def read(path):\n"
            "    if path == 'PARTNERS.md':\n"
            "        raise OSError('synthetic later input failure')\n"
            "    return original(path)\n"
            "mod.read_text = read\n"
            "sys.argv = [sys.argv[1], '--out', sys.argv[2]]\n"
            "mod.main()\n"
        )
        target = self.root / "existing output.txt"
        target.write_bytes(SENTINEL)
        result = subprocess.run(
            [sys.executable, "-X", "utf8", "-c", driver,
             str(self.root / "scripts/build-llms-full.py"), str(target)],
            cwd=self.foreign, capture_output=True, timeout=30,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn(b"OSError: synthetic later input failure", result.stderr)
        self.assertEqual(result.stdout, b"")
        self.assertEqual(target.read_bytes(), SENTINEL)

    def test_empty_index_preserves_existing_output(self):
        for guide in (self.root / "skills").rglob("*.md"):
            guide.write_text("Plain synthetic text without frontmatter.\n", encoding="utf-8")
        for argv in ([], ["--out", "existing output.txt"]):
            with self.subTest(argv=argv):
                target = self.root / ("existing output.txt" if argv else "index.json")
                target.write_bytes(SENTINEL)
                result = self.run_generator("build-index.py", argv)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn(b"no guides found", result.stderr)
                self.assertEqual(result.stdout, b"")
                self.assertEqual(target.read_bytes(), SENTINEL)

    def test_direct_main_calls_preserve_returns_and_supplied_lists(self):
        driver = LOAD_GENERATOR + (
            "import contextlib, io, json\n"
            "path, output, name, mode = sys.argv[1:]\n"
            "args = [] if mode == 'empty' else ['--out', output]\n"
            "before = list(args)\n"
            "sys.argv = [path, '--unknown'] if name == 'build-form-register.py' or mode == 'empty' else [path, *args]\n"
            "with contextlib.redirect_stdout(io.StringIO()):\n"
            "    code = mod.main(args) if name == 'build-partners.py' else mod.main()\n"
            "print(json.dumps({'return': code, 'arguments': args, 'before': before}))\n"
        )
        variants = [(name, "explicit") for name in GENERATORS] + [("build-partners.py", "empty")]
        for name, mode in variants:
            with self.subTest(name=name, mode=mode):
                self.restore_inputs()
                output = self.root / "direct output.txt"
                target = self.root / GENERATORS[name] if name == "build-form-register.py" or mode == "empty" else output
                target.unlink(missing_ok=True)
                result = subprocess.run(
                    [sys.executable, "-X", "utf8", "-c", driver,
                     str(self.root / "scripts" / name), str(output), name, mode],
                    cwd=self.foreign, capture_output=True, timeout=30,
                )
                self.assertEqual(result.returncode, 0, result.stderr)
                record = json.loads(result.stdout)
                self.assertEqual(record["return"], 0 if name == "build-partners.py" else None)
                self.assertEqual(record["arguments"], record["before"])
                self.assertTrue(target.is_file())

    def test_partner_parser_preserves_whitespace_without_path_probes(self):
        driver = LOAD_GENERATOR + (
            "import contextlib, io, json\n"
            "args = ['--out', sys.argv[2]]\n"
            "opened = []\n"
            "def output(path, *a, **kw):\n"
            "    opened.append(path)\n"
            "    return io.StringIO()\n"
            "mod.open = output\n"
            "with contextlib.redirect_stdout(io.StringIO()):\n"
            "    code = mod.main(args)\n"
            "print(json.dumps({'return': code, 'opened': opened, 'args': args}))\n"
        )
        for path in (" leading and trailing ", "   "):
            with self.subTest(path=path):
                result = subprocess.run(
                    [sys.executable, "-X", "utf8", "-c", driver,
                     str(self.root / "scripts/build-partners.py"), path],
                    cwd=self.foreign, capture_output=True, timeout=30,
                )
                self.assertEqual(result.returncode, 0, result.stderr)
                record = json.loads(result.stdout)
                self.assertEqual(record["return"], 0)
                self.assertEqual(record["opened"], [path])
                self.assertEqual(record["args"], ["--out", path])


if __name__ == "__main__":
    unittest.main()
