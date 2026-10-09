"""Metadata editors validate commands before guide, Git or write work."""

import itertools
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from oa_tools.frontmatter import extract_frontmatter, load_frontmatter, split_frontmatter

EDITORS = ("backfill-metadata.py", "normalize-tax-year.py")
GUARDED = """import builtins, importlib.util, json, os, runpy, subprocess, sys
def unexpected(*args, **kwargs):
    raise AssertionError('unexpected metadata work')
entry, route, encoded = sys.argv[1:]
sys.argv = [entry, *json.loads(encoded)]
builtins.open = os.walk = subprocess.run = unexpected
if route == 'script':
    runpy.run_path(entry, run_name='__main__')
else:
    spec = importlib.util.spec_from_file_location('editor', entry)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.load_build_index = mod.process_file = unexpected
    if hasattr(mod, 'git_last_updated_map'):
        mod.git_last_updated_map = unexpected
    try:
        result = mod.main()
    except SystemExit as error:
        if error.code in (None, 0):
            raise AssertionError('successful main must return normally') from error
        raise
    if result is not None:
        raise AssertionError('successful main must return None')
"""
SUPPORTED = """import importlib.util, json, sys
entry, selected, inherited, dates, record = sys.argv[1:]
spec = importlib.util.spec_from_file_location('editor', entry)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
if hasattr(mod, 'git_last_updated_map'):
    mod.git_last_updated_map = lambda: json.loads(dates)
sys.argv = [entry, *json.loads(inherited)]
before_process = list(sys.argv)
argv = json.loads(selected)
before_selected = None if argv is None else list(argv)
try:
    result = mod.main(argv)
except SystemExit as error:
    raise AssertionError('successful main must return normally') from error
with open(record, 'w', encoding='utf-8') as handle:
    json.dump({'return': result, 'supplied_unchanged': argv == before_selected,
               'process_unchanged': sys.argv == before_process}, handle)
"""


class MetadataCliTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name) / "checkout with spaces"
        scripts = self.root / "scripts"
        shutil.copytree(SCRIPTS / "oa_tools", scripts / "oa_tools",
                        ignore=shutil.ignore_patterns("__pycache__"))
        for name in (*EDITORS, "build-index.py"):
            shutil.copyfile(SCRIPTS / name, scripts / name)
        self.nested = self.root / "nested"
        self.foreign = Path(temporary.name) / "foreign caller"
        self.nested.mkdir()
        self.foreign.mkdir()
        headers = {
            "lf.md": b'---\nname: synthetic-lf\ntax_year: "2025/26"\n---\n',
            "crlf.md": b'---\r\nname: synthetic-crlf\r\ntax_year: "2025"\r\n---\r\n',
            "existing.md": b'---\nname: synthetic-existing\ntax_year: 2025\njurisdiction: XX\ntier: 2\nlast_updated: 2020-01-02\n---\n',
            "conflict.md": b'---\nname: synthetic-conflict\ntax_year: "2025/26"\ntax_year_notes: "keep this"\njurisdiction: XX\ntier: 2\nlast_updated: 2020-01-02\n---\n',
            "empty.md": b'---\nname: synthetic-empty\ntax_year: 2025\njurisdiction:\ntier:\nlast_updated:\n---\n',
        }
        self.files = {"skills/federal/" + name: header + b"Synthetic body without a final newline."
                      for name, header in headers.items()}
        self.files["skills/federal/document.md"] = b"Synthetic document without frontmatter.\n"
        self.restore_inputs()
        self.dates = {name: "2020-01-03" for name in self.files}

    def restore_inputs(self):
        for name, data in self.files.items():
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)

    def run_guarded(self, name, argv, *, route="import", cwd=None, optimised=False):
        options = ["-OO"] if optimised else []
        return subprocess.run(
            [sys.executable, *options, "-X", "utf8", "-c", GUARDED,
             str(self.root / "scripts" / name), route, json.dumps(argv)],
            cwd=cwd or self.foreign, capture_output=True, timeout=30)

    def assert_no_work(self, name, argv, expected, **kwargs):
        result = self.run_guarded(name, argv, **kwargs)
        self.assertEqual(result.returncode, expected, result.stderr.decode("utf-8"))
        self.assertNotIn(b"Traceback", result.stderr)
        if expected == 0:
            self.assertIn(b"usage:", result.stdout)
            self.assertEqual(result.stderr, b"")
        else:
            self.assertEqual(result.stdout, b"")
            self.assertIn(b"error:", result.stderr)
        self.assertEqual({name: (self.root / name).read_bytes() for name in self.files}, self.files)

    def test_help_and_invalid_arguments_skip_all_editor_work(self):
        invalid = [[value] for value in ("--unknown", "unexpected", "--app", "--he", "-a",
                                         "--out", "--selftest", "--", "--apply=", "--apply=true",
                                         "--help=1", "-h=1")]
        invalid += [["--apply", "false"], ["--", "--apply"], ["--", "--help"],
                    ["--help", "--", "--apply"], ["--apply", "--", "--help"],
                    ["--apply", "--", "--apply"], ["--help", "--"], ["--apply", "--"]]
        for help_flag in ("-h", "--help"):
            invalid += [list(argv) for argv in itertools.permutations((help_flag, "--apply", "--unknown"))]
            invalid += [[help_flag, "--apply", value] for value in
                        ("--apply=", "--apply=true", "false", "--help=1", "-h=1")]
        valid_help = [["-hh"], ["--help", "--help"]]
        for help_flag in ("-h", "--help"):
            valid_help += [[help_flag], [help_flag, "--apply"], ["--apply", help_flag],
                           ["--apply", help_flag, "--apply"]]
        for name in EDITORS:
            for argv in invalid:
                with self.subTest(name=name, argv=argv):
                    self.assert_no_work(name, argv, 2)
            for argv in valid_help:
                with self.subTest(name=name, argv=argv):
                    self.assert_no_work(name, argv, 0)

    def test_cold_imports_and_scripts_work_from_each_caller_under_optimisation(self):
        for name, route, cwd, optimised in itertools.product(
                EDITORS, ("script", "import"), (self.root, self.nested, self.foreign), (False, True)):
            for argv, expected in ((["--help"], 0), (["--apply", "-h"], 0),
                                   (["--apply", "--help", "--unknown"], 2)):
                with self.subTest(name=name, route=route, cwd=cwd.name, optimised=optimised, argv=argv):
                    self.assert_no_work(name, argv, expected, route=route, cwd=cwd, optimised=optimised)

    def test_work_guards_are_reached_by_supported_commands(self):
        for name, route, optimised in itertools.product(EDITORS, ("script", "import"), (False, True)):
            for argv in ([], ["--apply"]):
                with self.subTest(name=name, route=route, optimised=optimised, argv=argv):
                    result = self.run_guarded(name, argv, route=route, optimised=optimised)
                    self.assertEqual(result.returncode, 1)
                    self.assertIn(b"unexpected metadata work", result.stderr)

    def run_supported(self, name, selected, inherited, *, optimised=False):
        options = ["-OO"] if optimised else []
        record = self.root / "main-result.json"
        record.unlink(missing_ok=True)
        result = subprocess.run(
            [sys.executable, *options, "-X", "utf8", "-c", SUPPORTED,
             str(self.root / "scripts" / name), json.dumps(selected), json.dumps(inherited),
             json.dumps(self.dates), str(record)],
            cwd=self.foreign, capture_output=True, timeout=30)
        self.assertEqual(result.returncode, 0, result.stderr.decode("utf-8"))
        self.assertEqual(result.stderr, b"")
        self.assertTrue(record.is_file(), "successful main must create a fresh API record")
        api = json.loads(record.read_text(encoding="utf-8"))
        self.assertIsNone(api["return"])
        self.assertTrue(api["supplied_unchanged"])
        self.assertTrue(api["process_unchanged"])
        return result.stdout, {name: (self.root / name).read_bytes() for name in self.files}

    def test_explicit_arguments_preserve_dry_run_apply_and_return_contracts(self):
        for name, optimised in itertools.product(EDITORS, (False, True)):
            outputs = []
            for selected, inherited in (([], ["--apply", "--unknown"]), (None, []),
                                        (["--apply"], ["--unknown"]),
                                        (["--apply", "--apply"], ["--unknown"])):
                with self.subTest(name=name, optimised=optimised, selected=selected):
                    self.restore_inputs()
                    stdout, files = self.run_supported(name, selected, inherited, optimised=optimised)
                    outputs.append((stdout, files))
                    if not selected:
                        self.assertIn(b"[DRY RUN]", stdout)
                        self.assertEqual(files, self.files)
                    else:
                        self.assertIn(b"[APPLY]", stdout)
                        self.assertNotEqual(files, self.files)
                        for path, before in self.files.items():
                            if before.startswith(b"---"):
                                self.assertEqual(files[path].split(b"---", 2)[2], before.split(b"---", 2)[2])
                            else:
                                self.assertEqual(files[path], before)
                        for path in ("skills/federal/existing.md", "skills/federal/conflict.md", "skills/federal/empty.md"):
                            self.assertEqual(files[path], self.files[path])
                        if name == "backfill-metadata.py":
                            self.assertIn(b"jurisdiction: US\ntier: 2\nlast_updated: 2020-01-03\n", files["skills/federal/lf.md"])
                            self.assertIn(b"jurisdiction: US\r\ntier: 2\r\nlast_updated: 2020-01-03\r\n", files["skills/federal/crlf.md"])
                        else:
                            self.assertIn(b'tax_year: 2025\ntax_year_notes: "2025/26"\n', files["skills/federal/lf.md"])
                            self.assertIn(b"tax_year: 2025\r\n", files["skills/federal/crlf.md"])
            self.assertEqual(len(outputs), 4)
            self.assertEqual(outputs[0], outputs[1])
            self.assertEqual(outputs[2], outputs[3])

    def test_backfill_never_infers_signoff_and_preserves_existing_metadata(self):
        for nl in (b"\n", b"\r\n"):
            for reviewed in (b"Alex Example, CPA", b'"Alex\\x20Example, CPA"', b'"\\t"', b"pending_review"):
                for existing in (None, b"", b"1", b"2", b"null", b"1\ntier: 2"):
                    with self.subTest(newline=nl, reviewer=reviewed, tier=existing):
                        name = "skills/federal/quality.md"
                        header = [b"---", b"name: synthetic-quality", b"jurisdiction: XX",
                                  b"last_updated: 2020-01-02", b"tax_year: 2025",
                                  b"reviewed_by: " + reviewed, b"verified_by: Ann Legacy"]
                        if existing is not None:
                            header += [b"tier: " + existing.replace(b"\n", nl)]
                        self.files[name] = nl.join([*header, b"---", b"Synthetic body without a final newline."])
                        self.restore_inputs()
                        _, files = self.run_supported("backfill-metadata.py", [], [])
                        self.assertEqual(files, self.files)
                        _, files = self.run_supported("backfill-metadata.py", ["--apply"], [])
                        expected = self.files[name]
                        if existing is None:
                            expected = expected.replace(b"tax_year: 2025" + nl,
                                                        b"tax_year: 2025" + nl + b"tier: 2" + nl)
                        self.assertEqual(files[name], expected)
                        _, repeated = self.run_supported("backfill-metadata.py", ["--apply"], [])
                        self.assertEqual(repeated, files)

    def test_backfill_protects_keys_after_indented_scalar_delimiters(self):
        name = "skills/federal/scalar-marker.md"
        for nl, closer, marker, tier in itertools.product(
                (b"\n", b"\r\n"), (b"---", b"..."), (b"---", b"..."),
                (None, b"1", b"", b"1\ntier: 2")):
            with self.subTest(newline=nl, closer=closer, marker=marker, tier=tier):
                header = [b"---", b"name: scalar-marker", b"jurisdiction: MT",
                          b"last_updated: 2026-01-02", b"description: |", b"  " + marker]
                if tier is not None:
                    header.append(b"tier: " + tier.replace(b"\n", nl))
                header.append(b"reviewed_by: Alex Example, CPA")
                self.files[name] = nl.join([*header, closer, b"Synthetic body without a final newline."])
                self.restore_inputs()
                _, dry = self.run_supported("backfill-metadata.py", [], [])
                self.assertEqual(dry, self.files)
                _, applied = self.run_supported("backfill-metadata.py", ["--apply"], [])
                expected = self.files[name]
                if tier is None:
                    expected = expected.replace(b"jurisdiction: MT" + nl,
                                                b"jurisdiction: MT" + nl + b"tier: 2" + nl)
                    before = load_frontmatter(extract_frontmatter(self.files[name].decode("utf-8")))
                    self.assertEqual(load_frontmatter(extract_frontmatter(applied[name].decode("utf-8"))),
                                     {**before, "tier": 2})
                self.assertEqual(applied[name], expected)

    def test_backfill_inserts_missing_tier_outside_multiline_anchor_values(self):
        name = "skills/federal/multiline-anchor.md"
        values = ('|\n  2025/26\n  transitional coverage',
                  '>\n  2025/26\n  transitional coverage',
                  '"2025/26\n  transitional coverage"',
                  '"2025/26\ntransitional coverage"',
                  '"2025/26\ntax_year: 2025\ntransitional coverage"',
                  '"2025/26\ntier: 1\ntransitional coverage"',
                  "'2025/26\ntax_year: 2025\ntransitional coverage'",
                  "'2025/26\ntier: 1\ntransitional coverage'",
                  '"2025/26 \\"quoted\\"\ntier: 1\ntransitional coverage"',
                  "'2025/26 ''quoted''\ntier: 1\ntransitional coverage'")
        for nl, closer, value in itertools.product(("\n", "\r\n"), ("---", "..."), values):
            with self.subTest(newline=nl, closer=closer, value=value):
                text = ("---\nname: multiline-anchor\njurisdiction: MT\nlast_updated: 2026-01-02\n"
                        "tax_year: 2025\ntax_year_notes: " + value + "\n" + closer +
                        "\nSynthetic body without a final newline.").replace("\n", nl)
                before = load_frontmatter(extract_frontmatter(text))
                self.files[name] = text.encode("utf-8")
                self.restore_inputs()
                _, dry = self.run_supported("backfill-metadata.py", [], [])
                self.assertEqual(dry, self.files)
                stdout, applied = self.run_supported("backfill-metadata.py", ["--apply"], [])
                after = applied[name].decode("utf-8")
                self.assertEqual(load_frontmatter(extract_frontmatter(after)), {**before, "tier": 2})
                self.assertEqual(split_frontmatter(after)[1], split_frontmatter(text)[1])
                prefix, body = text.rsplit(closer + nl, 1)
                self.assertEqual(after, prefix + "tier: 2" + nl + closer + nl + body)
                self.assertIn((name + "\n      + tier: 2").encode("utf-8"), stdout.replace(b"\r\n", b"\n"))
                _, repeated = self.run_supported("backfill-metadata.py", ["--apply"], [])
                self.assertEqual(repeated, applied)

    def test_backfill_reports_unsupported_values_without_writing(self):
        name = "skills/federal/unsupported.md"
        for value in ('!!str "2025/26\ntier: 1\ncoverage"',
                      '&notes "2025/26\ntier: 1\ncoverage"',
                      '["2025/26", "coverage"]', '"unfinished'):
            with self.subTest(value=value):
                self.files[name] = ("---\nname: unsupported\njurisdiction: MT\nlast_updated: 2026-01-02\n"
                                    "tax_year_notes: " + value + "\n---\nSynthetic body.").encode("utf-8")
                self.restore_inputs()
                for argv in ([], ["--apply"]):
                    stdout, files = self.run_supported("backfill-metadata.py", argv, [])
                    self.assertEqual(files[name], self.files[name])
                    self.assertIn(b"unsupported frontmatter (not touched)", stdout)
                    self.assertIn(name.encode("utf-8"), stdout)

    def test_cold_backfill_dry_run_needs_no_yaml(self):
        result = subprocess.run(
            [sys.executable, "-S", "-X", "utf8", "-c", SUPPORTED,
             str(self.root / "scripts" / "backfill-metadata.py"), "[]", "[]", json.dumps(self.dates),
             str(self.root / "cold-result.json")],
            cwd=self.foreign, capture_output=True, timeout=30)
        self.assertEqual(result.returncode, 0, result.stderr.decode("utf-8"))
        self.assertIn(b"[DRY RUN]", result.stdout)
        self.assertEqual({name: (self.root / name).read_bytes() for name in self.files}, self.files)

    def test_backfill_refuses_deferred_quoted_openers_without_changing_metadata(self):
        name = "skills/federal/deferred-quote.md"
        for nl, closer, quote, fake_key in itertools.product(
                ("\n", "\r\n"), ("---", "..."), ('"', "'"), ("tier: 1", "tax_year: 2025")):
            with self.subTest(newline=nl, closer=closer, quote=quote, fake_key=fake_key):
                text = ("---\nname: deferred-quote\njurisdiction: MT\nlast_updated: 2026-01-02\n"
                        "tax_year_notes:\n  " + quote + "2025/26\n" + fake_key + "\ncontinued" + quote +
                        "\n" + closer + "\nSynthetic body without a final newline.").replace("\n", nl)
                before = load_frontmatter(extract_frontmatter(text))
                self.files[name] = text.encode("utf-8")
                self.restore_inputs()
                for argv in ([], ["--apply"], ["--apply"]):
                    stdout, files = self.run_supported("backfill-metadata.py", argv, [])
                    self.assertEqual(files[name], self.files[name])
                    self.assertEqual(load_frontmatter(extract_frontmatter(files[name].decode("utf-8"))), before)
                    self.assertIn(b"unsupported frontmatter (not touched)", stdout)
                    self.assertIn(name.encode("utf-8"), stdout)

    def test_backfill_refuses_indented_root_mappings_without_writing(self):
        name = "skills/federal/indented-root.md"
        for nl, closer, indent in itertools.product(("\n", "\r\n"), ("---", "..."), ("  ", "    ")):
            with self.subTest(newline=nl, closer=closer, indent=indent):
                block = "".join(indent + line + "\n" for line in (
                    "name: indented-root", "jurisdiction: MT", "tier: 1", "last_updated: 2026-01-02"))
                text = ("---\n" + block + closer + "\nSynthetic body without a final newline.").replace("\n", nl)
                before = load_frontmatter(extract_frontmatter(text))
                self.files[name] = text.encode("utf-8")
                self.restore_inputs()
                for argv in ([], ["--apply"], ["--apply"]):
                    stdout, files = self.run_supported("backfill-metadata.py", argv, [])
                    self.assertEqual(files[name], self.files[name])
                    self.assertEqual(load_frontmatter(extract_frontmatter(files[name].decode("utf-8"))), before)
                    self.assertIn(b"unsupported frontmatter (not touched)", stdout)

    def test_backfill_refuses_nested_quoted_nodes_without_changing_values(self):
        name = "skills/federal/nested-quote.md"
        prefixes = ("  note: ", "  - ", "  - note: ", "  nested:\n    note: ", "  long key: ")
        for nl, closer, quote, prefix in itertools.product(
                ("\n", "\r\n"), ("---", "..."), ('"', "'"), prefixes):
            with self.subTest(newline=nl, closer=closer, quote=quote, prefix=prefix):
                text = ("---\nname: nested-quote\njurisdiction: MT\nlast_updated: 2026-01-02\n"
                        "extra:\n" + prefix + quote + "begin\ntax_year: 2025\ndescription: end" + quote +
                        "\n" + closer + "\nSynthetic body without a final newline.").replace("\n", nl)
                before = load_frontmatter(extract_frontmatter(text))
                self.files[name] = text.encode("utf-8")
                self.restore_inputs()
                for argv in ([], ["--apply"], ["--apply"]):
                    stdout, files = self.run_supported("backfill-metadata.py", argv, [])
                    self.assertEqual(files[name], self.files[name])
                    self.assertEqual(load_frontmatter(extract_frontmatter(files[name].decode("utf-8"))), before)
                    self.assertIn(b"unsupported frontmatter (not touched)", stdout)

    def test_backfill_preserves_supported_indented_continuations(self):
        name = "skills/federal/indented-values.md"
        blocks = ('description: |\n  note: "literal quote\n  - \'literal item\n',
                  'description: >-\n  note: "literal quote\n  - \'literal item\n',
                  "description: begin\n  plain continuation\n",
                  "description:\n  plain deferred value\n",
                  "depends_on:\n  - workflow-base\n  - mt-income-tax\n")
        for nl, closer, block in itertools.product(("\n", "\r\n"), ("---", "..."), blocks):
            with self.subTest(newline=nl, closer=closer, block=block):
                text = ("---\nname: indented-values\njurisdiction: MT\nlast_updated: 2026-01-02\n" +
                        block + closer + "\nSynthetic body without a final newline.").replace("\n", nl)
                before = load_frontmatter(extract_frontmatter(text))
                self.files[name] = text.encode("utf-8")
                self.restore_inputs()
                _, dry = self.run_supported("backfill-metadata.py", [], [])
                self.assertEqual(dry, self.files)
                _, applied = self.run_supported("backfill-metadata.py", ["--apply"], [])
                expected = text.replace("jurisdiction: MT" + nl, "jurisdiction: MT" + nl + "tier: 2" + nl)
                self.assertEqual(applied[name], expected.encode("utf-8"))
                self.assertEqual(load_frontmatter(extract_frontmatter(applied[name].decode("utf-8"))),
                                 {**before, "tier": 2})
                _, repeated = self.run_supported("backfill-metadata.py", ["--apply"], [])
                self.assertEqual(repeated, applied)

    def test_backfill_refuses_unclassified_root_keys_without_inserting_duplicates(self):
        name = "skills/federal/unclassified-root.md"
        for nl, closer, entry in itertools.product(
                ("\n", "\r\n"), ("---", "..."),
                ("tier : 1", "tier :", "jurisdiction : MT", "last_updated : 2026-01-02",
                 "<<: {tier: 1}", "<<:\n  tier: 1")):
            with self.subTest(newline=nl, closer=closer, entry=entry):
                text = ("---\nname: unclassified-root\n" + entry + "\n" + closer +
                        "\nSynthetic body without a final newline.").replace("\n", nl)
                self.files[name] = text.encode("utf-8")
                self.restore_inputs()
                for argv in ([], ["--apply"], ["--apply"]):
                    stdout, files = self.run_supported("backfill-metadata.py", argv, [])
                    self.assertEqual(files[name], self.files[name])
                    self.assertIn(b"unsupported frontmatter (not touched)", stdout)
                    self.assertIn(name.encode("utf-8"), stdout)

    def test_backfill_refuses_compact_plain_scalars_without_writing(self):
        name = "skills/federal/compact-plain.md"
        for nl, closer in itertools.product(("\n", "\r\n"), ("---", "...")):
            with self.subTest(newline=nl, closer=closer):
                text = ("---\nname:synthetic\n" + closer + "\nBody must remain unchanged.").replace("\n", nl)
                self.files[name] = text.encode("utf-8")
                self.restore_inputs()
                for argv in ([], ["--apply"], ["--apply"]):
                    stdout, files = self.run_supported("backfill-metadata.py", argv, [])
                    self.assertEqual(files[name], self.files[name])
                    self.assertIn(b"unsupported frontmatter (not touched)", stdout)
                self.files[name] = text.replace("name:synthetic", "name: synthetic").encode("utf-8")
                self.restore_inputs()
                _, applied = self.run_supported("backfill-metadata.py", ["--apply"], [])
                self.assertIn(("jurisdiction: US" + nl + "tier: 2" + nl).encode("utf-8"), applied[name])

    def test_backfill_preserves_literal_quotes_in_plain_continuations(self):
        name = "skills/federal/plain-quotes.md"
        for nl, closer, quote in itertools.product(("\n", "\r\n"), ("---", "..."), ('"', "'")):
            with self.subTest(newline=nl, closer=closer, quote=quote):
                text = ("---\nname: plain-quotes\njurisdiction: MT\nlast_updated: 2026-01-02\n"
                        "description: Coverage includes\n  " + quote + "2025/26" + quote + " and later.\n" +
                        closer + "\nBody must remain unchanged.").replace("\n", nl)
                before = load_frontmatter(extract_frontmatter(text))
                self.files[name] = text.encode("utf-8")
                self.restore_inputs()
                _, dry = self.run_supported("backfill-metadata.py", [], [])
                self.assertEqual(dry, self.files)
                _, applied = self.run_supported("backfill-metadata.py", ["--apply"], [])
                expected = text.replace("jurisdiction: MT" + nl, "jurisdiction: MT" + nl + "tier: 2" + nl)
                self.assertEqual(applied[name], expected.encode("utf-8"))
                self.assertEqual(load_frontmatter(extract_frontmatter(applied[name].decode("utf-8"))),
                                 {**before, "tier": 2})
                _, repeated = self.run_supported("backfill-metadata.py", ["--apply"], [])
                self.assertEqual(repeated, applied)


if __name__ == "__main__":
    unittest.main()
