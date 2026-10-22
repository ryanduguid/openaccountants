"""Tests for scripts/oa_tools/, the helpers every script shares.

The package replaced three copies of the frontmatter block scanner
(build-index.py, build-packages.py, normalize-cta-block.py), two ad-hoc
splitters in the review aids, the strict loader module they all imported, and
the importlib shims that loaded build-index.py by path to reach its parser.
Copies drift: the scanner in build-packages.py had already grown its own
regex. These tests pin the reader's rules and that the scripts bind the shared
functions rather than a copy.
"""

from __future__ import annotations

import datetime
import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = REPO_ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from oa_tools import frontmatter, guides, paths  # noqa: E402


def _load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / filename)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


build_index = _load("build_index_for_oa_tools_tests", "build-index.py")
build_packages = _load("build_packages_for_oa_tools_tests", "build-packages.py")
validate_guides = _load("validate_guides_for_oa_tools_tests", "validate-guides.py")
normalize_cta = _load("normalize_cta_for_oa_tools_tests", "normalize-cta-block.py")
detect_contradictions = _load("detect_contradictions_for_oa_tools_tests", "detect-contradictions.py")

GUIDE = (
    "---\n"
    "name: synthetic\n"
    "jurisdiction: MT\n"
    "tier: 2\n"
    "last_updated: 2026-01-02\n"
    "---\n"
    "\n"
    "# Body\n"
)
BLOCK = "name: synthetic\njurisdiction: MT\ntier: 2\nlast_updated: 2026-01-02\n"


def _tree(case: unittest.TestCase, files: dict[str, str]) -> Path:
    tmp = tempfile.TemporaryDirectory()
    case.addCleanup(tmp.cleanup)
    root = Path(tmp.name)
    for rel, text in files.items():
        path = root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    return root


class ExtractFrontmatterTests(unittest.TestCase):
    def test_block_is_the_lines_between_the_delimiters(self) -> None:
        self.assertEqual(frontmatter.extract_frontmatter(GUIDE), BLOCK)

    def test_docs_horizontal_rules_and_unclosed_blocks_are_not_frontmatter(self) -> None:
        for text in (
            "",
            "# Notes\n\n---\n\nprose\n",        # a rule, not an opener
            "--- not a delimiter\nname: x\n---\n",
            "---\nname: x\n",                   # never closed
            " ---\nname: x\n---\n",             # not at byte 0
        ):
            self.assertIsNone(frontmatter.extract_frontmatter(text), repr(text))

    def test_document_end_marker_closes_the_block(self) -> None:
        self.assertEqual(frontmatter.extract_frontmatter("---\nname: x\n...\nbody\n"), "name: x\n")

    def test_trailing_whitespace_or_a_stray_cr_on_the_closer_still_closes(self) -> None:
        self.assertEqual(frontmatter.extract_frontmatter("---\nname: x\n--- \nbody\n"), "name: x\n")
        self.assertEqual(frontmatter.extract_frontmatter("---\nname: x\n---\r\nbody\n"), "name: x\n")

    def test_closer_with_other_text_on_the_line_does_not_close(self) -> None:
        self.assertIsNone(frontmatter.extract_frontmatter("---\nname: x\n---- \nbody\n"))


class SplitFrontmatterTests(unittest.TestCase):
    def test_delimiters_stay_with_the_frontmatter_and_the_parts_reassemble(self) -> None:
        fm, body = frontmatter.split_frontmatter(GUIDE)
        self.assertEqual(fm, "---\n" + BLOCK + "---\n")
        self.assertEqual(body, "\n# Body\n")
        self.assertEqual(fm + body, GUIDE)

    def test_no_frontmatter_means_everything_is_body(self) -> None:
        self.assertEqual(frontmatter.split_frontmatter("# Notes\n"), (None, "# Notes\n"))
        self.assertEqual(frontmatter.split_frontmatter("---\nnever closed\n"), (None, "---\nnever closed\n"))

    def test_blank_lines_after_the_closer_belong_to_the_body(self) -> None:
        fm, body = frontmatter.split_frontmatter("---\nname: x\n---\n\n\nbody\n")
        self.assertEqual(fm, "---\nname: x\n---\n")
        self.assertEqual(body, "\n\nbody\n")

    def test_closer_at_end_of_file_without_a_newline(self) -> None:
        self.assertEqual(frontmatter.split_frontmatter("---\nname: x\n---"), ("---\nname: x\n---", ""))


class TolerantReaderTests(unittest.TestCase):
    def test_every_known_key_is_present_and_defaults_to_none(self) -> None:
        fields = frontmatter.parse_known_keys("name: x\n")
        self.assertEqual(list(fields), frontmatter.KNOWN_KEYS)
        self.assertEqual(fields["name"], "x")
        self.assertIsNone(fields["tier"])

    def test_quotes_comments_null_and_block_scalars(self) -> None:
        block = (
            'name: "quoted"  \n'
            "jurisdiction: MT # trailing comment\n"
            "description: >\n"
            "  folded text\n"
            "tier: 2\n"
            "reviewed_by: ~\n"
            "verified_by: null\n"
        )
        fields = frontmatter.parse_known_keys(block)
        self.assertEqual(fields["name"], "quoted")
        self.assertEqual(fields["jurisdiction"], "MT")
        self.assertEqual(fields["tier"], "2")
        self.assertIsNone(fields["reviewed_by"])
        self.assertIsNone(fields["verified_by"])

    def test_first_occurrence_wins_and_malformed_lines_are_skipped(self) -> None:
        fields = frontmatter.parse_known_keys(
            "tier: 1\nqualifier: bad: colon soup\ntier: 2\n  jurisdiction: indented\n"
        )
        self.assertEqual(fields["tier"], "1")
        self.assertIsNone(fields["jurisdiction"])

    def test_custom_key_list(self) -> None:
        self.assertEqual(
            frontmatter.parse_known_keys("version: 1.2\nname: x\n", keys=["version"]),
            {"version": "1.2"},
        )

    def test_empty_first_values_still_win_over_duplicates(self) -> None:
        for first in ("", "   ", "null", "NULL", "~", '""', "''", '" "',
                      ">", "|", ">-", "|-", ">+", "|+", "null # empty", '"null"', '"~"'):
            with self.subTest(first=first):
                block = f"reviewed_by: {first}\nreviewed_by: Alex Example, CPA\n"
                self.assertIsNone(frontmatter.parse_known_keys(block)["reviewed_by"])
                with self.assertRaises(frontmatter.FrontmatterError):
                    frontmatter.load_frontmatter(block)

    def test_custom_key_iterator_preserves_first_empty_value_and_order(self) -> None:
        fields = frontmatter.parse_known_keys(
            "version:\nname: original\nversion: 1.2\nname: replacement\n",
            keys=iter(("version", "name", "missing")),
        )
        self.assertEqual(list(fields), ["version", "name", "missing"])
        self.assertEqual(fields, {"version": None, "name": "original", "missing": None})


class ReadFrontmatterTests(unittest.TestCase):
    """The one entry point: tolerant by default, strict on request."""

    def test_no_frontmatter_is_none_either_way(self) -> None:
        self.assertIsNone(frontmatter.read_frontmatter("# doc\n"))
        self.assertIsNone(frontmatter.read_frontmatter("# doc\n", strict=True))

    def test_tolerant_returns_the_known_keys(self) -> None:
        fields = frontmatter.read_frontmatter(GUIDE)
        self.assertEqual(fields["name"], "synthetic")
        self.assertEqual(fields["tier"], "2")

    def test_strict_returns_the_typed_mapping(self) -> None:
        metadata = frontmatter.read_frontmatter(GUIDE, strict=True)
        self.assertEqual(metadata["name"], "synthetic")
        self.assertEqual(metadata["tier"], 2)
        self.assertEqual(metadata["last_updated"], datetime.date(2026, 1, 2))

    def test_strict_rejects_what_tolerant_shrugs_at(self) -> None:
        duplicated = "---\nname: x\nname: y\n---\n"
        self.assertEqual(frontmatter.read_frontmatter(duplicated)["name"], "x")
        with self.assertRaisesRegex(frontmatter.FrontmatterError, "duplicate key"):
            frontmatter.read_frontmatter(duplicated, strict=True)

    def test_tolerant_path_never_imports_pyyaml(self) -> None:
        """The tolerant reader and imports need only the standard library;
        strict parsing and full index generation require PyYAML."""
        code = (
            "import sys; sys.path.insert(0, 'scripts')\n"
            "from oa_tools import frontmatter, guides\n"
            "frontmatter.read_frontmatter('---\\nname: x\\n---\\n')\n"
            "assert 'yaml' not in sys.modules, 'tolerant reader imported PyYAML'\n"
        )
        result = subprocess.run(
            [sys.executable, "-c", code], cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_yaml_scalar_construction_errors_are_frontmatter_errors(self) -> None:
        for raw in ("2026-02-30", "2026-02-30T12:00:00Z", "!!int invalid",
                    "!!bool nonsense", '!!int ""', '!!float ""', "!!timestamp nonsense",
                    '!!timestamp\n  =: "2026-01-02"'):
            with self.subTest(raw=raw):
                with self.assertRaises(frontmatter.FrontmatterError):
                    frontmatter.load_frontmatter("last_updated: " + raw)

    def test_reader_initialisation_errors_are_frontmatter_errors(self) -> None:
        for character in ("\x00", "\x01"):
            with self.subTest(character=repr(character)):
                with self.assertRaises(frontmatter.FrontmatterError):
                    frontmatter.load_frontmatter(f'name: synthetic\nextra: "bad{character}value"\n')

    def test_repeated_merge_directives_are_duplicate_keys(self) -> None:
        for block in ("<<: {a: 1}\n<<: {b: 2}", "nested:\n  <<: {a: 1}\n  <<: {b: 2}",
                      "<<:\n  <<: {a: 1}\n  <<: {b: 2}",
                      "<<:\n  - <<: {a: 1}\n    <<: {b: 2}",
                      "<<:\n  <<:\n    <<: {a: 1}\n    <<: {b: 2}"):
            with self.subTest(block=block):
                with self.assertRaisesRegex(frontmatter.FrontmatterError, "duplicate merge key"):
                    frontmatter.load_frontmatter(block)
        self.assertEqual(frontmatter.load_frontmatter("<<: {a: 1}\nb: 2"), {"a": 1, "b": 2})

    def test_duplicate_set_entries_are_rejected_before_review_projection(self) -> None:
        for nested in ("extra: !!set\n  repeated:\n  repeated:\n",
                       "extra:\n  inner: !!set\n    repeated:\n    repeated:\n"):
            with self.subTest(nested=nested):
                block = "tier: 1\nreviewed_by: Alex Example, CPA\nreview_status: current\n" + nested
                with self.assertRaisesRegex(frontmatter.FrontmatterError, "duplicate key"):
                    frontmatter.load_frontmatter(block)
        valid = frontmatter.load_frontmatter("extra: !!set\n  first:\n  second:\n")
        self.assertEqual(valid["extra"], {"first", "second"})

    def test_continued_tier_is_not_projected_as_a_complete_canonical_value(self) -> None:
        for tier in ("1", "2"):
            with self.subTest(tier=tier):
                metadata = frontmatter.load_frontmatter(f"tier: {tier}\n  extra\nreviewed_by: Alex Example, CPA")
                before = metadata.copy()
                self.assertEqual(metadata["tier"], tier + " extra")
                self.assertIsNone(frontmatter.review_fields(metadata)["tier"])
                self.assertEqual(metadata, before)

    def test_scalar_mapping_and_ordered_map_duplicates_are_rejected(self) -> None:
        for extra in ('extra: !!str\n  =: kept\n  repeated: first\n  repeated: second\n',
                      'extra: !!str\n  =: kept\n  ignored: {repeated: first, repeated: second}\n',
                      'extra: !!omap\n  - repeated: first\n  - "repe\\u0061ted": second\n',
                      'extra: !!omap\n  - [first]: one\n  - [first]: two\n'):
            with self.subTest(extra=extra):
                with self.assertRaisesRegex(frontmatter.FrontmatterError, "duplicate key"):
                    frontmatter.load_frontmatter("name: synthetic\n" + extra)

    def test_wrong_shaped_mapping_tags_are_frontmatter_errors(self) -> None:
        for raw in ("!!set [x]", "!!set []", "!!set scalar", "!!map [x]", "!!map []"):
            with self.subTest(raw=raw):
                with self.assertRaisesRegex(frontmatter.FrontmatterError, "expected a mapping"):
                    frontmatter.load_frontmatter("name: synthetic\nextra: " + raw)

    def test_valid_scalar_mapping_and_ordered_map_keep_yaml_values(self) -> None:
        block = ('name: synthetic\nextra: !!str\n  =: kept\n  ignored: {valid: true}\n'
                 'ordered: !!omap\n  - [first]: 1\n  - [second]: 2\n'
                 'pairs: !!pairs\n  - repeated: first\n  - repeated: second\n')
        metadata = frontmatter.load_frontmatter(block)
        self.assertEqual(metadata["extra"], "kept")
        self.assertEqual(metadata["ordered"], [(["first"], 1), (["second"], 2)])
        self.assertEqual(metadata["pairs"], [("repeated", "first"), ("repeated", "second")])

    def test_ordered_map_keys_use_completed_alias_values(self) -> None:
        prefix = 'name: synthetic\nanchor: &a {first: 1}\nextra: !!str\n  =: kept\n  ignored: !!omap\n    - *a: one\n'
        valid = frontmatter.load_frontmatter(prefix + '    - {}: two\n')
        self.assertEqual(valid["extra"], "kept")
        with self.assertRaisesRegex(frontmatter.FrontmatterError, "duplicate key"):
            frontmatter.load_frontmatter(prefix + '    - {first: 1}: two\n')
        for first, second in (('*a', '[x]'), ('[x]', '*a'), ('[*a]', '[[x]]')):
            with self.subTest(first=first, second=second):
                with self.assertRaisesRegex(frontmatter.FrontmatterError, "duplicate key"):
                    frontmatter.load_frontmatter(
                        f'prior: [&a [x]]\nextra: !!omap\n  - {first}: one\n  - {second}: two\n')
        for first, second in (('*a', '*b'), ('*b', '*a')):
            with self.subTest(first=first, second=second):
                metadata = frontmatter.load_frontmatter(
                    f'prior: [&a [x], &b [y]]\nextra: !!omap\n  - {first}: one\n  - {second}: two\n')
                self.assertEqual([key for key, _ in metadata['extra']],
                                 [['x'], ['y']] if first == '*a' else [['y'], ['x']])

    def test_nested_scalar_projections_survive_mapping_validation(self) -> None:
        import yaml

        for tag in ("", " !!str"):
            for depth in (1, 2):
                nested = ''.join('  ' * level + '=:' + tag + '\n' for level in range(1, depth + 1))
                block = 'extra: !!str\n' + nested + '  ' * (depth + 1) + '=: kept\n'
                with self.subTest(tag=tag, depth=depth):
                    self.assertEqual(frontmatter.load_frontmatter(block), yaml.safe_load(block))
                    self.assertEqual(frontmatter.load_frontmatter(block)['extra'], 'kept')
                    for invalid in ('ignored: {repeated: first, repeated: second}',
                                    'ignored: !!bool nonsense'):
                        with self.subTest(invalid=invalid):
                            with self.assertRaises(frontmatter.FrontmatterError):
                                frontmatter.load_frontmatter(block + '  ' * (depth + 1) + invalid + '\n')

    def test_aliased_projection_keys_keep_each_mapping_value(self) -> None:
        import yaml

        block = ('first: !!str\n  ? &default =\n  : kept-one\n'
                 'second: !!str\n  ? *default\n  : kept-two\n')
        self.assertEqual(frontmatter.load_frontmatter(block), yaml.safe_load(block))
        for invalid in ('ignored: {repeated: first, repeated: second}',
                        'ignored: !!bool nonsense'):
            with self.subTest(invalid=invalid), self.assertRaises(frontmatter.FrontmatterError):
                frontmatter.load_frontmatter(block + '  ' + invalid + '\n')
        literal = 'first: {&literal "=": kept-one}\nsecond: !!str\n  ? *literal\n  : kept-two\n'
        with self.assertRaises(yaml.YAMLError):
            yaml.safe_load(literal)
        with self.assertRaises(frontmatter.FrontmatterError):
            frontmatter.load_frontmatter(literal)

    def test_discarded_recursive_collections_finish_validation(self) -> None:
        import yaml

        for recursive in ('&loop [*loop]', '&loop {self: *loop}'):
            block = 'extra: !!str\n  =: kept\n  ignored: ' + recursive + '\nretained: *loop\n'
            with self.subTest(recursive=recursive):
                metadata = frontmatter.load_frontmatter(block)
                ordinary = yaml.safe_load(block)
                self.assertEqual(metadata['extra'], ordinary['extra'])
                key = 0 if isinstance(metadata['retained'], list) else 'self'
                self.assertIs(metadata['retained'][key], metadata['retained'])
                for invalid in ('repeated: first, repeated: second', 'invalid: !!bool nonsense'):
                    with self.subTest(invalid=invalid), self.assertRaises(frontmatter.FrontmatterError):
                        frontmatter.load_frontmatter(
                            'extra: !!str\n  =: kept\n  ignored: &loop {self: *loop, ' + invalid + '}\n')

    def test_aliases_to_the_document_root_preserve_identity(self) -> None:
        import yaml

        block = ('&root\nname: recursive-root\ntier: 1\n'
                 'reviewed_by: Alex Example, CPA\nreview_status: current\n'
                 'extra: *root\nnested: {root: *root}\n')
        ordinary = yaml.safe_load(block)
        self.assertIs(ordinary['extra'], ordinary)
        metadata = frontmatter.load_frontmatter(block)
        self.assertIs(metadata['extra'], metadata)
        self.assertIs(metadata['nested']['root'], metadata)
        self.assertIs(type(metadata['nested']), dict)
        self.assertEqual(frontmatter.review_fields(metadata)['tier'], '1')
        metadata['after_load'] = 'visible through the alias'
        self.assertEqual(metadata['extra']['after_load'], metadata['after_load'])

    def test_merged_keys_do_not_create_scalar_projections(self) -> None:
        import yaml

        for block in ('extra: !!str\n  <<: {=: kept}\n',
                      'anchor: &a\n  <<: {=: kept}\nlater:\n  extra: !!str\n    =: *a\n'):
            with self.subTest(block=block):
                with self.assertRaises(yaml.YAMLError):
                    yaml.safe_load(block)
                with self.assertRaises(frontmatter.FrontmatterError):
                    frontmatter.load_frontmatter(block)
        valid = 'extra: {<<: {original: kept}, additional: value}\n'
        self.assertEqual(frontmatter.load_frontmatter(valid), yaml.safe_load(valid))

    def test_yaml_recursion_failures_raise_frontmatter_errors(self) -> None:
        import yaml

        for block in ('extra: !!str\n  =: &loop\n    =: *loop\n',
                      'extra: ' + '[' * 1000 + ']' * 1000 + '\n'):
            with self.subTest(block=block):
                with self.assertRaises(RecursionError):
                    yaml.safe_load(block)
                with self.assertRaises(frontmatter.FrontmatterError):
                    frontmatter.load_frontmatter(block)

    def test_recursive_ordered_keys_fail_locally_when_comparison_is_undefined(self) -> None:
        block = ('name: synthetic\nleft: &left {self: *left, marker: 1}\n'
                 'right: &right {self: *right, marker: 2}\nextra: !!omap\n  - *left: one\n  - *right: two\n')
        with self.assertRaisesRegex(frontmatter.FrontmatterError, "keys cannot be compared"):
            frontmatter.load_frontmatter(block)
        valid = frontmatter.load_frontmatter('name: synthetic\nextra: &ordered !!omap\n  - *ordered: value\n')
        self.assertIs(valid["extra"][0][0], valid["extra"])


class GuideDiscoveryTests(unittest.TestCase):
    def test_walks_only_the_guide_trees_skips_readmes_and_sorts(self) -> None:
        root = _tree(self, {
            "skills/a/README.md": "# readme",
            "skills/a/readme.md": "# readme",
            "skills/a/z-guide.md": GUIDE,
            "skills/a/a-guide.md": GUIDE,
            "skills/a/notes.txt": "not markdown",
            "packages/us-federal/rates.2026.json": "{}",   # hand-authored data, not a guide tree
            "packages/malta/mt-vat.md": GUIDE,   # generated: not a guide tree
            "packages/_shared/base.md": GUIDE,   # generated: not a guide tree
            "docs/page.md": GUIDE,
        })
        self.assertEqual(
            guides.guide_files(str(root)),
            ["skills/a/a-guide.md", "skills/a/z-guide.md"],
        )

    def test_a_missing_tree_is_skipped(self) -> None:
        root = _tree(self, {"skills/a/guide.md": GUIDE})
        self.assertEqual(guides.guide_files(str(root)), ["skills/a/guide.md"])
        self.assertEqual(guides.guide_files(str(root), trees=("nowhere",)), [])

    def test_paths_are_posix_and_root_relative(self) -> None:
        root = _tree(self, {"skills/deep/er/guide.md": GUIDE})
        self.assertEqual(guides.guide_files(str(root)), ["skills/deep/er/guide.md"])

    def test_read_text_replaces_undecodable_bytes(self) -> None:
        root = _tree(self, {})
        (root / "guide.md").write_bytes(b"---\nname: x\n---\n\xff\n")
        self.assertEqual(guides.read_text("guide.md", str(root)), "---\nname: x\n---\n�\n")

    def test_defaults_point_at_this_repository(self) -> None:
        self.assertEqual(paths.REPO_ROOT, str(REPO_ROOT))
        self.assertEqual(paths.repo_root(), str(REPO_ROOT))
        self.assertEqual(paths.GUIDE_TREES, ("skills",))
        self.assertEqual(paths.SKILLS_DIR, str(REPO_ROOT / "skills"))
        self.assertEqual(paths.PACKAGES_DIR, str(REPO_ROOT / "packages"))
        self.assertEqual(paths.HAND_AUTHORED_PACKAGES, frozenset({"us-federal"}))
        self.assertEqual(paths.rel(str(REPO_ROOT / "skills" / "x.md")), "skills/x.md")


class ReviewDiscoveryTests(unittest.TestCase):
    def test_default_reads_the_checkout_and_includes_readmes(self) -> None:
        root = _tree(self, {
            "skills/example/README.md": "Folder claims",
            "skills/example/guide.md": GUIDE,
            "skills/example/notes.txt": "Not Markdown",
            "packages/example/generated.md": GUIDE,
        })
        with mock.patch.object(guides, "REPO_ROOT", str(root)):
            found = list(guides.markdown_files())
        self.assertEqual(found, [
            (str(Path("skills/example/README.md")), str(root / "skills/example/README.md")),
            (str(Path("skills/example/guide.md")), str(root / "skills/example/guide.md")),
        ])

    def test_absolute_root_keeps_its_display_path_and_missing_roots_are_empty(self) -> None:
        root = _tree(self, {"requested/guide.md": GUIDE})
        source = str(root / "requested/guide.md")
        self.assertEqual(list(guides.markdown_files(root / "requested")), [(source, source)])
        self.assertEqual(list(guides.markdown_files(root / "missing")), [])


class ScriptsShareTheHelpersTests(unittest.TestCase):
    """Copies were the bug: each one drifted. The scripts must bind the shared
    objects, and no script may keep a private block scanner."""

    def test_build_index_re_exports_the_reader_and_walks_its_own_root(self) -> None:
        self.assertIs(build_index.extract_frontmatter, frontmatter.extract_frontmatter)
        self.assertIs(build_index.parse_known_keys, frontmatter.parse_known_keys)
        self.assertEqual(build_index.GUIDE_TREES, list(paths.GUIDE_TREES))
        root = _tree(self, {"skills/a/guide.md": GUIDE, "skills/a/README.md": "# r"})
        with mock.patch.object(build_index, "REPO_ROOT", str(root)):
            self.assertEqual(build_index.guide_files(), ["skills/a/guide.md"])
            self.assertEqual(build_index.build_index()["counts"]["guides"], 1)

    def test_build_packages_uses_the_shared_reader_and_hand_authored_list(self) -> None:
        self.assertIs(build_packages.extract_frontmatter, frontmatter.extract_frontmatter)
        self.assertIs(build_packages.load_frontmatter, frontmatter.load_frontmatter)
        self.assertIs(build_packages.HAND_AUTHORED_PACKAGES, paths.HAND_AUTHORED_PACKAGES)
        self.assertFalse(hasattr(build_packages, "_frontmatter_block"))

    def test_validator_reads_guides_through_the_package(self) -> None:
        bi = validate_guides.GuideTrees()
        self.assertIs(bi.extract_frontmatter, frontmatter.extract_frontmatter)
        self.assertIs(bi.parse_known_keys, frontmatter.parse_known_keys)
        root = _tree(self, {"skills/a/guide.md": GUIDE, "packages/malta/mt.md": GUIDE})
        with mock.patch.object(validate_guides, "REPO_ROOT", str(root)):
            self.assertEqual(bi.guide_files(), ["skills/a/guide.md"])
        for shim in ("load_build_index", "load_build_packages"):
            self.assertFalse(hasattr(validate_guides, shim), shim)

    def test_normalizer_and_contradiction_scanner_bind_the_shared_functions(self) -> None:
        self.assertIs(normalize_cta.split_frontmatter, frontmatter.split_frontmatter)
        self.assertIs(detect_contradictions.extract_frontmatter, frontmatter.extract_frontmatter)
        self.assertIs(detect_contradictions.parse_known_keys, frontmatter.parse_known_keys)

    def test_no_script_keeps_a_private_block_scanner_or_the_old_module(self) -> None:
        old_module = "frontmatter" + "_yaml"   # split so this file does not match itself
        offenders = []
        for path in sorted([*SCRIPTS.glob("*.py"), *(REPO_ROOT / "tests").glob("*.py")]):
            text = path.read_text(encoding="utf-8")
            if old_module in text:
                offenders.append(f"{path.name}: imports the removed {old_module} module")
            if path.parent == SCRIPTS and "first_nl" in text:
                offenders.append(f"{path.name}: carries a copy of the block scanner")
        self.assertEqual(offenders, [])

    def test_a_test_module_imports_on_its_own(self) -> None:
        """Regression: run alone, tests.test_validate_quality_metadata failed
        with ModuleNotFoundError because validate-guides.py relied on a sibling
        test having put scripts/ on sys.path first. Every script that imports
        oa_tools now puts its own directory there."""
        result = subprocess.run(
            [sys.executable, "-m", "unittest", "tests.test_validate_quality_metadata"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=120,
        )
        self.assertEqual(result.returncode, 0, result.stderr)


class BuildIndexCliTests(unittest.TestCase):
    def test_cold_help_and_tolerant_import_work_but_generation_requires_yaml(self) -> None:
        root = _tree(self, {"skills/a/guide.md": GUIDE})
        out = root / "index.json"
        runner = """import importlib.util, sys
spec = importlib.util.spec_from_file_location('cold_index', sys.argv[1])
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
assert 'yaml' not in sys.modules
assert mod.parse_known_keys('name: original\\nname: later\\n')['name'] == 'original'
mod.REPO_ROOT = sys.argv[2]
sys.argv = ['build-index.py', *sys.argv[3:]]
mod.main()
"""
        for argv, code in ((["--help"], 0), (["--out", str(out)], 1)):
            with self.subTest(argv=argv):
                result = subprocess.run(
                    [sys.executable, "-S", "-c", runner, str(SCRIPTS / "build-index.py"), str(root), *argv],
                    capture_output=True, text=True, timeout=30,
                )
                self.assertEqual(result.returncode, code, result.stderr)
                self.assertNotIn("Traceback", result.stderr)
                if code:
                    self.assertIn("requires PyYAML", result.stderr)
                else:
                    self.assertIn("usage:", result.stdout)
        self.assertFalse(out.exists())

    def test_out_without_a_path_is_an_error_not_a_traceback(self) -> None:
        for argv in (["--out"], ["--out", "--other"]):
            result = subprocess.run(
                [sys.executable, str(SCRIPTS / "build-index.py"), *argv],
                cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
            )
            self.assertNotEqual(result.returncode, 0, argv)
            self.assertIn("--out requires a file path", result.stderr, argv)
            self.assertNotIn("Traceback", result.stderr, argv)

    def test_refuses_to_write_an_empty_index(self) -> None:
        root = _tree(self, {"skills/a/README.md": "# only docs"})
        out = root / "index.json"
        with mock.patch.object(build_index, "REPO_ROOT", str(root)), \
                mock.patch.object(sys, "argv", ["build-index.py", "--out", str(out)]):
            with self.assertRaises(SystemExit) as caught:
                build_index.main()
        self.assertIn("no guides found", str(caught.exception))
        self.assertFalse(out.exists())


if __name__ == "__main__":
    unittest.main()
