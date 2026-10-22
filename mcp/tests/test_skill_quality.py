"""Regression tests for fail-closed MCP quality metadata."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest import mock

from openaccountants_mcp import server


class SkillQualityTests(unittest.TestCase):
    def test_tier_one_with_named_reviewer_is_accountant_verified(self) -> None:
        meta = {"tier": 1, "reviewed_by": "Alex Example, CPA"}

        self.assertEqual(server._quality_tier(meta), "accountant-verified")

    def test_legacy_verified_by_field_still_supports_tier_one(self) -> None:
        meta = {"tier": "1", "verified_by": "Alex Example, CPA"}

        self.assertEqual(server._quality_tier(meta), "accountant-verified")

    def test_tier_two_remains_research_even_with_reviewer_name(self) -> None:
        meta = {"tier": 2, "reviewed_by": "Alex Example, CPA"}

        self.assertEqual(server._quality_tier(meta), "research-verified")

    def test_tier_one_without_real_reviewer_fails_closed(self) -> None:
        for reviewer in (None, "", " \t\n", "pending", "pending_review", "none", "n/a", "-",
                         True, 42, ["Alex"], {"name": "Alex"}):
            with self.subTest(reviewer=reviewer):
                meta = {"tier": 1, "reviewed_by": reviewer}
                self.assertEqual(server._quality_tier(meta), "research-verified")

    def test_placeholder_and_blank_current_fields_allow_a_legacy_reviewer(self) -> None:
        for reviewer in ("pending_review", " \t\n", True, ["Alex"]):
            with self.subTest(reviewer=reviewer):
                meta = {"tier": 1, "reviewed_by": reviewer, "verified_by": "Ann Legacy"}
                self.assertEqual(server._quality_tier(meta), "accountant-verified")
                self.assertEqual(server._real_verifier(meta), "Ann Legacy")

    def test_reviewer_name_does_not_replace_missing_tier(self) -> None:
        meta = {"verified_by": "Alex Example, CPA"}

        self.assertEqual(server._quality_tier(meta), "research-verified")

    def test_invalid_tier_values_fail_closed(self) -> None:
        for tier in (0, 3, "one", "draft"):
            with self.subTest(tier=tier):
                meta = {"tier": tier, "reviewed_by": "Alex Example, CPA"}
                self.assertEqual(server._quality_tier(meta), "research-verified")


class IndexVerifierExposureTests(unittest.TestCase):
    """A non-tier-1 row must not publish a reviewer name in ``verified_by``.

    The ``_quality_tier`` tests above do not cover this: deleting the
    conditional in ``_index`` that nulls the field leaves every one of them
    passing while the server still hands callers a tier 2 guide's reviewer as
    its verifier.
    """

    GUIDE = """---
name: {slug}
tier: {tier}
jurisdiction: MT
reviewed_by: Alex Example, CPA
---

# {slug}
"""

    def _row_for(self, slug: str, tier: int, *, closer="---", newline="\n", reviewer="Alex Example, CPA") -> dict:
        """Build a one-guide packages tree and return that guide's index row."""
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        package = Path(tmp.name) / "malta"
        package.mkdir(parents=True)
        text = self.GUIDE.format(slug=slug, tier=tier).replace("\n---\n", f"\n{closer}\n")
        text = text.replace("reviewed_by: Alex Example, CPA", "reviewed_by: " + reviewer)
        (package / f"{slug}.md").write_bytes(text.replace("\n", newline).encode("utf-8"))
        self.addCleanup(server._index.cache_clear)
        with mock.patch.object(server, "PACKAGES_DIR", Path(tmp.name)):
            server._index.cache_clear()
            return server._index()[slug]

    def test_tier_two_row_does_not_expose_its_reviewer(self) -> None:
        row = self._row_for("tier-two-guide", 2)

        self.assertEqual(row["quality_tier"], "research-verified")
        self.assertIsNone(row["verified_by"])

    def test_tier_one_row_still_publishes_its_verifier(self) -> None:
        row = self._row_for("tier-one-guide", 1)

        self.assertEqual(row["quality_tier"], "accountant-verified")
        self.assertEqual(row["verified_by"], "Alex Example, CPA")

    def test_document_end_closer_publishes_the_same_quality_row(self) -> None:
        for newline in ("\n", "\r\n"):
            for closer in ("---", "...", "... \t"):
                with self.subTest(newline=newline, closer=closer):
                    row = self._row_for("quality-guide", 1, closer=closer, newline=newline)
                    self.assertEqual(row["quality_tier"], "accountant-verified")
                    self.assertEqual(row["verified_by"], "Alex Example, CPA")

    def test_rows_use_decoded_reviewer_strings(self) -> None:
        for raw, expected in ((r'"\t"', None), (r'"p\x65nding"', None),
                              (r'"\u0020"', None), ("pending_review", None),
                              (r'"Alex\x20Example, CPA"', "Alex Example, CPA"),
                              (">\n  Alex Example,\n  CPA", "Alex Example, CPA")):
            with self.subTest(raw=raw):
                row = self._row_for("quality-guide", 1, reviewer=raw)
                self.assertEqual(row["verified_by"], expected)
                self.assertEqual(row["quality_tier"], "accountant-verified" if expected else "research-verified")


class FrontmatterBoundaryTests(unittest.TestCase):
    def test_complete_closers_and_body_boundary(self) -> None:
        for newline in ("\n", "\r\n"):
            for closer in ("---", "...", "--- \t", "... \t"):
                with self.subTest(newline=newline, closer=closer):
                    header = newline.join(("---", "name: synthetic", "tier: 1",
                                           "reviewed_by: Alex Example, CPA", closer))
                    meta, body = server._parse_frontmatter(header + newline + newline + "# Body" + newline)
                    self.assertEqual(meta["name"], "synthetic")
                    self.assertEqual(server._quality_tier(meta), "accountant-verified")
                    self.assertEqual(body, "# Body" + newline)
                    self.assertEqual(server._parse_frontmatter(header), (meta, ""))

    def test_partial_or_indented_delimiters_do_not_publish_metadata(self) -> None:
        for newline in ("\n", "\r\n"):
            for opener, closer in (("---", "---invalid"), ("---", "...invalid"),
                                   ("---", " ---"), ("---", " ..."),
                                   ("---invalid", "---"), (" ---", "---")):
                with self.subTest(newline=newline, opener=opener, closer=closer):
                    text = newline.join((opener, "name: synthetic", "tier: 1",
                                         "reviewed_by: Alex Example, CPA", closer, "# Body"))
                    meta, body = server._parse_frontmatter(text)
                    self.assertEqual(meta, {})
                    self.assertEqual(body, text)
                    self.assertEqual(server._quality_tier(meta), "research-verified")

    def test_empty_block_closes_and_indented_scalar_markers_stay_in_metadata(self) -> None:
        self.assertEqual(server._parse_frontmatter("---\n...\n# Body\n"), ({}, "# Body\n"))
        meta, body = server._parse_frontmatter("---\nname: synthetic\ndescription: |\n  ---\n  ...\n...\n# Body\n")
        self.assertEqual(meta["description"], "---\n...\n")
        self.assertEqual(body, "# Body\n")


class AssuranceEvidenceTests(unittest.TestCase):
    def _row(self, fields: str) -> dict:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        root = Path(temporary.name)
        (root / "malta").mkdir()
        text = "---\nname: synthetic\njurisdiction: MT\n" + fields + "\n---\n# Body\nUnchanged guidance.\n"
        (root / "malta/synthetic.md").write_text(text, encoding="utf-8")
        (root / "malta/neighbour.md").write_text(
            "---\nname: neighbour\ntier: 1\nreviewed_by: Ann Legacy\n---\n# Neighbour\n", encoding="utf-8")
        self.addCleanup(server._index.cache_clear)
        with mock.patch.object(server, "PACKAGES_DIR", root):
            server._index.cache_clear()
            rows = server._index()
            self.assertEqual(set(rows), {"synthetic", "neighbour"})
            self.assertEqual(rows["neighbour"]["verified_by"], "Ann Legacy")
            self.assertEqual(server._read_skill("synthetic")[1], "# Body\nUnchanged guidance.\n")
            return rows["synthetic"]

    def _assert_withheld(self, fields: str) -> None:
        row = self._row(fields)
        self.assertEqual(row["quality_tier"], "research-verified")
        self.assertIsNone(row["verified_by"])
        self.assertEqual(row["review_status"], "")

    def test_duplicates_and_merge_collisions_never_authorise_assurance(self) -> None:
        base = "tier: 1\nreviewed_by: Alex Example, CPA\nreview_status: current"
        cases = ["nested: {a: 1, a: 2}", '"reviewed_\\u0062y": Alex Example, CPA',
                 "<<: {reviewed_by: Ann Legacy}", "<<: [{x: 1}, {x: 2}]",
                 "<<: {x: 1}\n<<: {y: 2}", "[a, b]: value", "42: value",
                 "name: >-\n  synthetic", "<<:\n  <<: {a: 1}\n  <<: {b: 2}",
                 "<<:\n  - <<: {a: 1}\n    <<: {b: 2}",
                 "<<:\n  <<:\n    <<: {a: 1}\n    <<: {b: 2}"]
        for key, values in (("tier", ("1", "2")),
                            ("reviewed_by", ("pending", "Alex Example, CPA")),
                            ("verified_by", ("pending", "Ann Legacy")),
                            ("review_status", ("current", "pending_review")),
                            ("description", ("a", "b"))):
            for left, right in (values, tuple(reversed(values)), (values[0], values[0])):
                cases.append(f"{key}: {left}\n{key}: {right}")
        for fields in cases:
            with self.subTest(fields=fields):
                self._assert_withheld(base + "\n" + fields)

    def test_file_field_types_override_the_direct_dict_fallback(self) -> None:
        for key in ("reviewed_by", "verified_by"):
            other = "verified_by" if key == "reviewed_by" else "reviewed_by"
            for raw in ("true", "42", "null", "[Alex]", "{name: Alex}"):
                with self.subTest(key=key, raw=raw):
                    self._assert_withheld(f"tier: 1\n{key}: {raw}\n{other}: Ann Legacy")
        for extra in ("description: true", "depends_on: - workflow-base", "depends_on: [null]",
                      "depends_on: ['']", "review_status: [current]", "review_status:",
                      "review_status: unknown", "review_status: CURRENT"):
            with self.subTest(extra=extra):
                self._assert_withheld("tier: 1\nreviewed_by: Alex Example, CPA\n" + extra)

    def test_tier_requires_a_canonical_direct_mapping_entry(self) -> None:
        for entry in ("tier: 01", "tier: 0x1", "tier: +1", "tier: 1.0", "tier: true",
                      "tier: 1\n  extra", "tier: 2\n  extra",
                      'tier: "\\u0031"', 'tier: "1" # comment', "tier: &one 1",
                      "one: &one 1\ntier: *one", "tier: !!int 1", "tier: |\n  1",
                      "<<: {tier: 1}", '"tier": 1',
                      'description: "Synthetic description.\ntier: 1\ncontinued."',
                      'description: "Synthetic description.\ntier: 1\ncontinued."\ntier: 2'):
            with self.subTest(entry=entry):
                self._assert_withheld(entry + "\nreviewed_by: Alex Example, CPA\nreview_status: current\n_trusted: true")
        for raw in ("1", '"1"', "'1'", '" 1 "', "1 # comment"):
            with self.subTest(raw=raw):
                row = self._row("tier: " + raw + "\nreviewed_by: Alex Example, CPA")
                self.assertEqual(row["quality_tier"], "accountant-verified")
                self.assertEqual(row["verified_by"], "Alex Example, CPA")

    def test_scalar_construction_and_salvage_failures_remain_local(self) -> None:
        for extra in ("last_updated: 2026-02-30", "last_updated: !!int nonsense",
                      "extra: !!bool nonsense", 'extra: !!int ""', 'extra: !!float ""',
                      "last_updated: !!timestamp nonsense", 'extra: !!timestamp\n  =: "2026-01-02"',
                      'extra: "bad\x00value"', 'extra: "bad\x01value"'):
            for malformed in ("", "description: bad: colon\n"):
                with self.subTest(extra=extra, malformed=malformed):
                    self._assert_withheld("tier: 1\nreviewed_by: Alex Example, CPA\nreview_status: current\n" +
                                          malformed + extra)

    def test_valid_freshness_and_nonconflicting_merge_keep_signoff(self) -> None:
        for fields, status in (("tier: 1\n<<: {reviewed_by: Alex Example, CPA}", ""),
                               ("tier: 1\nreviewed_by: pending\nverified_by: Ann Legacy", ""),
                               ("tier: 1\nreviewed_by: Alex Example, CPA\nreview_status: >\n  current", "current"),
                               ("tier: 1\nreviewed_by: Alex Example, CPA\nreview_status: pending_review", "pending_review")):
            with self.subTest(fields=fields):
                row = self._row(fields)
                self.assertEqual(row["quality_tier"], "accountant-verified")
                self.assertIsInstance(row["verified_by"], str)
                self.assertEqual(row["review_status"], status)

    def test_constructor_bypasses_and_wrong_node_shapes_withhold_assurance(self) -> None:
        base = "tier: 1\nreviewed_by: Alex Example, CPA\nreview_status: current\n"
        for extra in ('extra: !!str\n  =: kept\n  repeated: first\n  repeated: second',
                      'extra: !!str\n  =: kept\n  ignored: {repeated: first, repeated: second}',
                      'extra: !!omap\n  - repeated: first\n  - "repe\\u0061ted": second',
                      'extra: !!omap\n  - [first]: one\n  - [first]: two',
                      'extra: !!set [x]', 'extra: !!set []', 'extra: !!set scalar',
                      'extra: !!map [x]', 'extra: !!map []'):
            with self.subTest(extra=extra):
                self._assert_withheld(base + extra)

    def test_valid_scalar_mapping_and_ordered_map_keep_assurance(self) -> None:
        block = ('tier: 1\nreviewed_by: Alex Example, CPA\nreview_status: current\n'
                 'extra: !!str\n  =: kept\n  ignored: {valid: true}\n'
                 'ordered: !!omap\n  - [first]: 1\n  - [second]: 2\n'
                 'pairs: !!pairs\n  - repeated: first\n  - repeated: second\n')
        meta, _ = server._load_assurance_metadata(block)
        self.assertEqual(meta["extra"], "kept")
        self.assertEqual(meta["ordered"], [(["first"], 1), (["second"], 2)])
        self.assertEqual(meta["pairs"], [("repeated", "first"), ("repeated", "second")])
        row = self._row(block)
        self.assertEqual(row["quality_tier"], "accountant-verified")
        self.assertEqual(row["verified_by"], "Alex Example, CPA")
        self.assertEqual(row["review_status"], "current")

    def test_completed_alias_values_decide_ordered_map_assurance(self) -> None:
        prefix = ('tier: 1\nreviewed_by: Alex Example, CPA\nreview_status: current\n'
                  'anchor: &a {first: 1}\nextra: !!str\n  =: kept\n  ignored: !!omap\n    - *a: one\n')
        row = self._row(prefix + '    - {}: two\n')
        self.assertEqual(row["quality_tier"], "accountant-verified")
        self.assertEqual(row["verified_by"], "Alex Example, CPA")
        self.assertEqual(row["review_status"], "current")
        self._assert_withheld(prefix + '    - {first: 1}: two\n')
        base = 'tier: 1\nreviewed_by: Alex Example, CPA\nreview_status: current\n'
        for first, second in (('*a', '[x]'), ('[x]', '*a'), ('[*a]', '[[x]]')):
            with self.subTest(first=first, second=second):
                self._assert_withheld(base + f'prior: [&a [x]]\nextra: !!omap\n  - {first}: one\n  - {second}: two\n')
        for first, second in (('*a', '*b'), ('*b', '*a')):
            with self.subTest(first=first, second=second):
                row = self._row(base + f'prior: [&a [x], &b [y]]\nextra: !!omap\n  - {first}: one\n  - {second}: two\n')
                self.assertEqual(row['quality_tier'], 'accountant-verified')
                self.assertEqual(row['verified_by'], 'Alex Example, CPA')

    def test_nested_scalar_projections_keep_values_and_assurance(self) -> None:
        for tag in ('', ' !!str'):
            for depth in (1, 2):
                nested = ''.join('  ' * level + '=:' + tag + '\n' for level in range(1, depth + 1))
                block = 'extra: !!str\n' + nested + '  ' * (depth + 1) + '=: kept\n'
                base = 'tier: 1\nreviewed_by: Alex Example, CPA\nreview_status: current\n'
                with self.subTest(tag=tag, depth=depth):
                    meta, _ = server._load_assurance_metadata(base + block)
                    self.assertEqual(meta['extra'], 'kept')
                    self.assertEqual(self._row(base + block)['quality_tier'], 'accountant-verified')
                    for invalid in ('ignored: {repeated: first, repeated: second}',
                                    'ignored: !!bool nonsense'):
                        with self.subTest(invalid=invalid):
                            self._assert_withheld(base + block + '  ' * (depth + 1) + invalid + '\n')

    def test_aliased_projection_keys_preserve_values_and_assurance(self) -> None:
        base = 'tier: 1\nreviewed_by: Alex Example, CPA\nreview_status: current\n'
        block = ('first: !!str\n  ? &default =\n  : kept-one\n'
                 'second: !!str\n  ? *default\n  : kept-two\n')
        meta, _ = server._load_assurance_metadata(base + block)
        self.assertEqual((meta['first'], meta['second']), ('kept-one', 'kept-two'))
        self.assertEqual(self._row(base + block)['quality_tier'], 'accountant-verified')
        for invalid in ('ignored: {repeated: first, repeated: second}',
                        'ignored: !!bool nonsense'):
            with self.subTest(invalid=invalid):
                self._assert_withheld(base + block + '  ' + invalid + '\n')
        self._assert_withheld(base + 'first: {&literal "=": kept-one}\n'
                              'second: !!str\n  ? *literal\n  : kept-two\n')

    def test_discarded_recursive_collections_preserve_assurance(self) -> None:
        base = 'tier: 1\nreviewed_by: Alex Example, CPA\nreview_status: current\n'
        for recursive in ('&loop [*loop]', '&loop {self: *loop}'):
            block = base + 'extra: !!str\n  =: kept\n  ignored: ' + recursive + '\nretained: *loop\n'
            with self.subTest(recursive=recursive):
                meta, _ = server._load_assurance_metadata(block)
                self.assertEqual(meta['extra'], 'kept')
                key = 0 if isinstance(meta['retained'], list) else 'self'
                self.assertIs(meta['retained'][key], meta['retained'])
                self.assertEqual(self._row(block)['quality_tier'], 'accountant-verified')
                for invalid in ('repeated: first, repeated: second', 'invalid: !!bool nonsense'):
                    with self.subTest(invalid=invalid):
                        self._assert_withheld(base + 'extra: !!str\n  =: kept\n'
                                              '  ignored: &loop {self: *loop, ' + invalid + '}\n')

    def test_aliases_to_the_document_root_preserve_identity_and_assurance(self) -> None:
        block = ('&root\nname: recursive-root\ntier: 1\n'
                 'reviewed_by: Alex Example, CPA\nreview_status: current\n'
                 'extra: *root\nnested: {root: *root}\n')
        metadata, tier = server._load_assurance_metadata(block)
        self.assertIs(metadata['extra'], metadata)
        self.assertIs(metadata['nested']['root'], metadata)
        self.assertEqual(tier, '1')
        metadata['after_load'] = 'visible through the alias'
        self.assertEqual(metadata['extra']['after_load'], metadata['after_load'])
        parsed, body = server._parse_frontmatter('---\n' + block + '---\nBody.')
        self.assertIs(parsed['extra'], parsed)
        self.assertEqual(server._quality_tier(parsed), 'accountant-verified')
        self.assertEqual(server._real_verifier(parsed), 'Alex Example, CPA')
        self.assertEqual(body, 'Body.')

    def test_merged_keys_cannot_authorise_scalar_projections(self) -> None:
        base = 'tier: 1\nreviewed_by: Alex Example, CPA\nreview_status: current\n'
        for block in ('extra: !!str\n  <<: {=: kept}\n',
                      'anchor: &a\n  <<: {=: kept}\nlater:\n  extra: !!str\n    =: *a\n'):
            with self.subTest(block=block):
                self._assert_withheld(base + block)
        self.assertEqual(self._row(base + 'extra: {<<: {original: kept}, additional: value}\n')
                         ['quality_tier'], 'accountant-verified')

    def test_yaml_recursion_failures_remain_local_to_the_file(self) -> None:
        base = 'tier: 1\nreviewed_by: Alex Example, CPA\nreview_status: current\n'
        for block in ('extra: !!str\n  =: &loop\n    =: *loop\n',
                      'extra: ' + '[' * 1000 + ']' * 1000 + '\n'):
            for malformed in ('', 'description: bad: colon\n'):
                with self.subTest(block=block, malformed=malformed):
                    self._assert_withheld(base + malformed + block)

    def test_scalar_recovery_roots_cannot_abort_neighbour_catalogue(self) -> None:
        for tag in ('!!int', '!!null'):
            block = tag + ' {=: 1, repeated: first, repeated: second}'
            with self.subTest(tag=tag), tempfile.TemporaryDirectory() as tmp:
                text = '---\n' + block + '\n---\n# Body\n'
                self.assertEqual(server._parse_frontmatter(text), ({}, '# Body\n'))
                root = Path(tmp)
                (root / 'malta').mkdir()
                (root / 'malta/invalid.md').write_text(text, encoding='utf-8')
                (root / 'malta/neighbour.md').write_text(
                    '---\nname: neighbour\ntier: 1\nreviewed_by: Ann Legacy\n---\n# Neighbour\n', encoding='utf-8')
                self.addCleanup(server._index.cache_clear)
                with mock.patch.object(server, 'PACKAGES_DIR', root):
                    server._index.cache_clear()
                    rows = server._index()
                    self.assertEqual(set(rows), {'neighbour'})
                    self.assertEqual(rows['neighbour']['verified_by'], 'Ann Legacy')

    def test_recursive_ordered_key_comparison_cannot_abort_neighbour_inventory(self) -> None:
        self._assert_withheld('tier: 1\nreviewed_by: Alex Example, CPA\nreview_status: current\n'
                              'left: &left {self: *left, marker: 1}\nright: &right {self: *right, marker: 2}\n'
                              'extra: !!omap\n  - *left: one\n  - *right: two\n')
        meta, _ = server._load_assurance_metadata('name: synthetic\nextra: &ordered !!omap\n  - *ordered: value\n')
        self.assertIs(meta["extra"][0][0], meta["extra"])

    def test_unrelated_projection_errors_are_not_yaml_failures(self) -> None:
        text = "---\nname: synthetic\ntier: 1\nreviewed_by: Alex Example, CPA\nreview_status: current\n---\nBody."
        for error in (ValueError("projection failure"), RuntimeError("projection failure"),
                      KeyError("projection failure"), IndexError("projection failure"),
                      AttributeError("projection failure"), TypeError("projection failure"),
                      RecursionError("projection failure")):
            with self.subTest(error=type(error)), mock.patch.object(server, "_real_verifier", side_effect=error):
                with self.assertRaisesRegex(type(error), "projection failure"):
                    server._parse_frontmatter(text)


if __name__ == "__main__":
    unittest.main()
