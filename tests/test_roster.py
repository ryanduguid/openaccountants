"""One counting rule for accountant review, and PARTNERS.md derived from it.

Four files published who had reviewed what, with three different rules:
PARTNERS.md counted a reviewer's name on any tier (so a reviewer with five
tier-2 guides had a row and four reviewers with 43 tier-1 guides had none),
llms.txt carried hand-copied figures, and README.md and build-index.py each
had a private copy of the tier-1-plus-name test. scripts/oa_tools/roster.py is
the single definition now; these tests pin the rule, the roster rows and the
rendered file, and that build-partners.py writes exactly that render.
"""

from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = REPO_ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from oa_tools import roster  # noqa: E402


def _load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / filename)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


build_partners = _load("build_partners_for_roster_tests", "build-partners.py")
build_index = _load("build_index_for_roster_tests", "build-index.py")
coverage = _load("coverage_for_roster_tests", "check-coverage-claims.py")


def g(slug, tier, reviewed_by=None, verified_by=None, jurisdiction="ZZ", last_updated="2026-01-02",
      review_status=None):
    return {
        "slug": slug, "path": f"skills/international/zz/{slug}.md", "name": slug,
        "jurisdiction": jurisdiction, "category": None, "tier": tier,
        "verified_by": verified_by, "reviewed_by": reviewed_by, "review_status": review_status,
        "tax_year": 2026, "last_updated": last_updated,
    }


WITHHELD = "A licensed accountant (name withheld at their request)"

GUIDES = [
    g("zz-vat", 1, reviewed_by="Jane Doe, CPA", last_updated="2026-03-01", review_status="current"),
    g("zz-income-tax", 1, reviewed_by="Jane Doe, CPA", last_updated="2026-05-01", review_status="pending_review"),
    g("zz-payroll", 1, verified_by="Ann Legacy", last_updated="2026-02-02"),
    g("yy-vat", 1, reviewed_by=WITHHELD, jurisdiction="YY"),
    g("yy-income-tax", 1, reviewed_by="Jane Doe, CPA", jurisdiction="YY"),
    g("xx-vat", 2, reviewed_by="Bob Attribution", jurisdiction="XX", review_status="pending_review"),
    g("xx-payroll", 1, reviewed_by="pending", jurisdiction="XX"),
    g("ww-vat", 1, verified_by="TBD", jurisdiction="WW"),
    g("vv-vat", 2, jurisdiction="VV"),
]
INDEX = {"counts": {"guides": 9, "jurisdictions": 5, "accountant_reviewed": 5}, "guides": GUIDES}
PROFILES = {"Jane Doe, CPA": {"public_record": "https://example.test/jane", "label": "profile"},
            WITHHELD: {"public_record": "https://example.test/anon", "note": "Named elsewhere."}}


class RuleTests(unittest.TestCase):
    def test_tier_one_with_a_name_is_reviewed(self) -> None:
        self.assertEqual(roster.reviewer_of(g("a", 1, reviewed_by="Jane Doe, CPA")), "Jane Doe, CPA")
        self.assertEqual(roster.reviewer_of(g("a", "1", reviewed_by=" Jane Doe, CPA ")), "Jane Doe, CPA")
        self.assertEqual(roster.reviewer_of(g("a", 1, verified_by="Ann Legacy")), "Ann Legacy")
        self.assertEqual(roster.reviewer_of(g("a", 1, reviewed_by="Jane", verified_by="pending")), "Jane")

    def test_a_name_on_a_tier_two_guide_is_attribution_not_review(self) -> None:
        self.assertIsNone(roster.reviewer_of(g("a", 2, reviewed_by="Bob Attribution")))
        self.assertIsNone(roster.reviewer_of(g("a", None, reviewed_by="Bob Attribution")))
        self.assertEqual(roster.reviewer_name(g("a", 2, reviewed_by="Bob Attribution")), "Bob Attribution")

    def test_placeholders_are_nobody(self) -> None:
        for marker in ("pending", "pending_review", "None", "no", "FALSE", "-", "n/a", "tbd",
                       "", " \t\n", None, True, 42, ["Alex"], {"name": "Alex"}):
            self.assertIsNone(roster.reviewer_of(g("a", 1, reviewed_by=marker)), marker)
            self.assertIsNone(roster.reviewer_of(g("a", 1, verified_by=marker)), marker)
            self.assertEqual(roster.reviewer_of(g("a", 1, reviewed_by=marker, verified_by="Ann Legacy")),
                             "Ann Legacy", marker)

    def test_the_withheld_reviewer_counts_as_a_reviewer_but_not_a_person(self) -> None:
        self.assertEqual(roster.reviewer_of(g("a", 1, reviewed_by=WITHHELD)), WITHHELD)
        self.assertFalse(roster.is_named(WITHHELD))
        self.assertTrue(roster.is_named("Jane Doe, CPA"))

    def test_pending_review_is_the_edited_since_review_flag_not_a_tier(self) -> None:
        """review_status is freshness: a reviewed guide edited after its sign-off
        stays reviewed, and a tier-2 guide pending review is not reviewed."""
        edited = g("a", 1, reviewed_by="Jane Doe, CPA", review_status="pending_review")
        self.assertTrue(roster.edited_since_review(edited))
        self.assertEqual(roster.reviewer_of(edited), "Jane Doe, CPA")
        self.assertFalse(roster.edited_since_review(g("a", 1, reviewed_by="Jane Doe, CPA", review_status="current")))
        self.assertFalse(roster.edited_since_review(g("a", 1, reviewed_by="Jane Doe, CPA")))
        self.assertIsNone(roster.reviewer_of(g("a", 2, reviewed_by="Bob Attribution", review_status="pending_review")))

    def test_headline_figures_and_line(self) -> None:
        figures = roster.headline(GUIDES)
        self.assertEqual(figures, {"Guides": 9, "jurisdictions": 5, "accountant-reviewed": 5, "named accountants": 2})
        self.assertEqual(
            roster.headline_line({"Guides": 1867, "jurisdictions": 243, "accountant-reviewed": 164, "named accountants": 22}),
            "**1,867 Guides** across **243 jurisdictions** · **164 accountant-reviewed** · **22 named accountants**",
        )

    def test_build_index_counts_with_the_same_rule(self) -> None:
        """index.json's accountant_reviewed is this rule, not a private copy."""
        self.assertIs(build_index.roster, roster)
        with tempfile.TemporaryDirectory() as tmp:
            tree = Path(tmp)
            (tree / "skills").mkdir()
            head = "---\nname: {name}\njurisdiction: ZZ\ntier: {tier}\nreviewed_by: {who}\nlast_updated: 2026-01-02\n---\n\n# x\n"
            (tree / "skills" / "a.md").write_text(head.format(name="a", tier=1, who="Jane Doe, CPA"), encoding="utf-8")
            (tree / "skills" / "b.md").write_text(head.format(name="b", tier=2, who="Bob Attribution"), encoding="utf-8")
            (tree / "skills" / "c.md").write_text(head.format(name="c", tier=1, who="pending"), encoding="utf-8")
            with mock.patch.object(build_index, "REPO_ROOT", str(tree)):
                index = build_index.build_index()
        self.assertEqual(index["counts"]["accountant_reviewed"], 1)
        self.assertEqual(index["counts"]["accountant_reviewed"], roster.headline(index["guides"])["accountant-reviewed"])

    def test_index_publishes_yaml_reviewer_values_to_roster_and_coverage(self) -> None:
        cases = {
            "tab": ('"\\t"', None),
            "space": ('"\\u0020"', None),
            "pending": ('"p\\x65nding"', "pending"),
            "pending-review": ('"pending_review"', "pending_review"),
            "name": ('"Alex\\x20Example, CPA"', "Alex Example, CPA"),
            "folded": (">\n  Alex Example,\n  CPA", "Alex Example, CPA"),
        }
        with tempfile.TemporaryDirectory() as tmp:
            tree = Path(tmp)
            (tree / "skills").mkdir()
            for slug, (raw, _) in cases.items():
                (tree / "skills" / f"{slug}.md").write_text(
                    f"---\nname: {slug}\njurisdiction: ZZ\ntier: 1\nreviewed_by: {raw}\n"
                    "last_updated: 2026-01-02\n---\n# Body\n", encoding="utf-8")
            with mock.patch.object(build_index, "REPO_ROOT", str(tree)):
                index = build_index.build_index()
        rows = {row["slug"]: row for row in index["guides"]}
        self.assertEqual({slug: row["reviewed_by"] for slug, row in rows.items()},
                         {slug: expected for slug, (_, expected) in cases.items()})
        self.assertEqual(index["counts"]["accountant_reviewed"], 2)
        self.assertEqual(roster.headline(index["guides"])["named accountants"], 1)
        self.assertEqual([row["reviewer"] for row in roster.roster(index["guides"])], ["Alex Example, CPA"])
        metrics, people = coverage.actual(index)
        self.assertEqual(metrics["Distinct `reviewed_by` values"], 1)
        self.assertEqual(len(people), 1)
        rendered, _ = roster.render_partners(index, {"Alex Example, CPA": {"public_record": "https://example.test/alex"}})
        self.assertIn("| Alex Example, CPA | ZZ | 2 |", rendered)
        self.assertIn("[profile](https://example.test/alex)", rendered)

    def test_index_keeps_invalid_rows_without_reviewer_claims(self) -> None:
        cases = ("reviewed_by: pending\nreviewed_by: Alex Example, CPA",
                 "reviewed_by: Alex Example, CPA\nreviewed_by: pending",
                 "reviewed_by: true", "reviewed_by: 42", "reviewed_by: [Alex]",
                 "reviewed_by: {name: Alex}", "reviewed_by: Alex\nqualifier: bad: colon",
                 "reviewed_by: Alex Example, CPA\nextra: !!set\n  repeated:\n  repeated:")
        with tempfile.TemporaryDirectory() as tmp:
            tree = Path(tmp)
            (tree / "skills").mkdir()
            for i, fields in enumerate(cases):
                (tree / "skills" / f"bad-{i}.md").write_text(
                    f"---\nname: bad-{i}\njurisdiction: ZZ\ntier: 1\nreview_status: current\n{fields}\n---\n# Body\n",
                    encoding="utf-8")
            stderr = io.StringIO()
            with mock.patch.object(build_index, "REPO_ROOT", str(tree)), contextlib.redirect_stderr(stderr):
                index = build_index.build_index()
        self.assertEqual(index["counts"]["guides"], len(cases))
        self.assertEqual(index["counts"]["accountant_reviewed"], 0)
        self.assertTrue(all(row["reviewed_by"] is None and row["verified_by"] is None for row in index["guides"]))
        self.assertEqual(stderr.getvalue().count("omitting reviewer claims"), len(cases))
        problems = []
        coverage.index_integrity(lambda *args, **kwargs: problems.append((args, kwargs)), index)
        self.assertEqual(len(problems), len(cases))
        self.assertEqual(coverage.actual(index)[0]["`tier: 1` (accountant-reviewed)"], len(cases))

    def test_index_preserves_reviewers_for_shared_keys_and_recursive_extensions(self) -> None:
        cases = ('first: !!str\n  ? &default =\n  : kept-one\n'
                 'second: !!str\n  ? *default\n  : kept-two\n',
                 'extra: !!str\n  =: kept\n  ignored: &loop [*loop]\nretained: *loop\n',
                 'extra: !!str\n  =: kept\n  ignored: &loop {self: *loop}\nretained: *loop\n')
        for fields in cases:
            with self.subTest(fields=fields), tempfile.TemporaryDirectory() as tmp:
                tree = Path(tmp)
                (tree / 'skills').mkdir()
                texts = {}
                for slug, extra in (('extension', fields), ('neighbour', '')):
                    text = (f'---\nname: {slug}\njurisdiction: ZZ\ntier: 1\n'
                            'reviewed_by: Alex Example, CPA\nreview_status: current\n'
                            + extra + f'---\n# {slug}\n')
                    path = tree / 'skills' / (slug + '.md')
                    path.write_text(text, encoding='utf-8')
                    texts[path] = text
                diagnostics = io.StringIO()
                with mock.patch.object(build_index, 'REPO_ROOT', str(tree)), contextlib.redirect_stderr(diagnostics):
                    index = build_index.build_index()
                rows = {row['slug']: row for row in index['guides']}
                self.assertEqual(set(rows), {'extension', 'neighbour'})
                self.assertEqual(index['counts']['accountant_reviewed'], 2)
                self.assertEqual(diagnostics.getvalue(), '')
                for slug, row in rows.items():
                    self.assertEqual(row['reviewed_by'], 'Alex Example, CPA')
                    self.assertEqual(row['path'], f'skills/{slug}.md')
                self.assertEqual({path: path.read_text(encoding='utf-8') for path in texts}, texts)

    def test_index_withholds_merged_projections_and_contains_projection_cycles(self) -> None:
        cases = ('extra: !!str\n  <<: {=: kept}\n',
                 'anchor: &a\n  <<: {=: kept}\nlater:\n  extra: !!str\n    =: *a\n',
                 'extra: !!str\n  =: &loop\n    =: *loop\n',
                 'extra: ' + '[' * 1000 + ']' * 1000 + '\n')
        for fields in cases:
            with self.subTest(fields=fields), tempfile.TemporaryDirectory() as tmp:
                tree = Path(tmp)
                (tree / 'skills').mkdir()
                for slug, extra in (('invalid', fields), ('neighbour', '')):
                    (tree / 'skills' / (slug + '.md')).write_text(
                        f'---\nname: {slug}\njurisdiction: ZZ\ntier: 1\n'
                        'reviewed_by: Alex Example, CPA\nreview_status: current\n'
                        + extra + f'---\n# {slug}\n', encoding='utf-8')
                diagnostics = io.StringIO()
                with mock.patch.object(build_index, 'REPO_ROOT', str(tree)), contextlib.redirect_stderr(diagnostics):
                    index = build_index.build_index()
                rows = {row['slug']: row for row in index['guides']}
                self.assertEqual(set(rows), {'invalid', 'neighbour'})
                self.assertEqual(index['counts']['accountant_reviewed'], 1)
                self.assertIsNone(rows['invalid']['reviewed_by'])
                self.assertIsNone(rows['invalid']['verified_by'])
                self.assertEqual(rows['neighbour']['reviewed_by'], 'Alex Example, CPA')
                self.assertIn('omitting reviewer claims', diagnostics.getvalue())

    def test_index_retains_scalar_failures_and_the_valid_reviewed_row(self) -> None:
        cases = ("last_updated: 2026-02-30", "extra: !!bool nonsense", 'extra: !!int ""',
                 'extra: !!float ""', "last_updated: !!timestamp nonsense",
                 'extra: !!timestamp\n  =: "2026-01-02"', 'extra: "bad\x00value"',
                 'extra: "bad\x01value"')
        for invalid in cases:
            with self.subTest(invalid=invalid), tempfile.TemporaryDirectory() as tmp:
                tree = Path(tmp)
                (tree / "skills").mkdir()
                for slug, fields in (("bad-scalar", invalid), ("good-date", "last_updated: 2026-02-28")):
                    (tree / "skills" / f"{slug}.md").write_text(
                        f"---\nname: {slug}\njurisdiction: MT\ntier: 1\n"
                        f"reviewed_by: Alex Example, CPA\n{fields}\n---\n# Body\n", encoding="utf-8")
                stderr = io.StringIO()
                with mock.patch.object(build_index, "REPO_ROOT", str(tree)), contextlib.redirect_stderr(stderr):
                    index = build_index.build_index()
                rows = {row["slug"]: row for row in index["guides"]}
                self.assertEqual(set(rows), {"bad-scalar", "good-date"})
                self.assertIsNone(rows["bad-scalar"]["reviewed_by"])
                self.assertIsNone(rows["bad-scalar"]["verified_by"])
                self.assertEqual(rows["good-date"]["reviewed_by"], "Alex Example, CPA")
                self.assertEqual(index["counts"]["accountant_reviewed"], 1)
                self.assertIn("skills/bad-scalar.md", stderr.getvalue())
                self.assertEqual(stderr.getvalue().count("omitting reviewer claims"), 1)
                if invalid == cases[0]:
                    self.assertRegex(stderr.getvalue(), "day.*range")

    def test_coverage_reviewed_by_metric_remains_distinct_from_signoff_and_legacy(self) -> None:
        guides = [g("attribution", 2, reviewed_by="Alex Example, CPA"),
                  g("legacy", 1, reviewed_by="pending_review", verified_by="Ann Legacy"),
                  g("bad", 1, reviewed_by=["Alex"])]
        metrics, people = coverage.actual({"guides": guides})
        self.assertEqual(metrics["Distinct `reviewed_by` values"], 1)
        self.assertEqual(people, {coverage.normalise("Alex Example, CPA")})
        self.assertEqual(metrics["`tier: 1` (accountant-reviewed)"], 2)
        self.assertEqual(roster.headline(guides)["accountant-reviewed"], 1)

    def test_index_only_converts_canonical_tier_values(self) -> None:
        values = ("1", '"1"', "2", '"2"', "01", "1.0", "true", "[1]", "3")
        with tempfile.TemporaryDirectory() as tmp:
            tree = Path(tmp)
            (tree / "skills").mkdir()
            for i, value in enumerate(values):
                (tree / "skills" / f"tier-{i}.md").write_text(
                    f"---\nname: tier-{i}\ntier: {value}\nreviewed_by: Alex Example, CPA\n---\n# Body\n",
                    encoding="utf-8")
            with mock.patch.object(build_index, "REPO_ROOT", str(tree)):
                index = build_index.build_index()
        self.assertEqual([row["tier"] for row in index["guides"]],
                         [1, 1, 2, 2, "01", "1.0", "true", "[1]", "3"])
        self.assertEqual(index["counts"]["accountant_reviewed"], 2)

    def test_constructor_failures_keep_diagnostic_rows_and_valid_neighbour(self) -> None:
        cases = ('extra: !!str\n  =: kept\n  repeated: first\n  repeated: second',
                 'extra: !!str\n  =: kept\n  ignored: {repeated: first, repeated: second}',
                 'extra: !!omap\n  - repeated: first\n  - repeated: second',
                 'extra: !!set [x]', 'extra: !!set []', 'extra: !!map [x]',
                 'anchor: &a {first: 1}\nextra: !!str\n  =: kept\n  ignored: !!omap\n    - *a: one\n    - {first: 1}: two',
                 'left: &left {self: *left, marker: 1}\nright: &right {self: *right, marker: 2}\n'
                 'extra: !!omap\n  - *left: one\n  - *right: two')
        for extra in cases:
            with self.subTest(extra=extra), tempfile.TemporaryDirectory() as tmp:
                tree = Path(tmp)
                (tree / "skills").mkdir()
                for slug, fields in (("bad", extra), ("neighbour", "extra: {valid: true}")):
                    (tree / "skills" / f"{slug}.md").write_text(
                        f"---\nname: {slug}\njurisdiction: MT\ntier: 1\n"
                        f"reviewed_by: Alex Example, CPA\nreview_status: current\n{fields}\n---\n# Body\n",
                        encoding="utf-8")
                stderr = io.StringIO()
                with mock.patch.object(build_index, "REPO_ROOT", str(tree)), contextlib.redirect_stderr(stderr):
                    index = build_index.build_index()
                rows = {row["slug"]: row for row in index["guides"]}
                self.assertEqual(set(rows), {"bad", "neighbour"})
                self.assertIsNone(rows["bad"]["reviewed_by"])
                self.assertIsNone(rows["bad"]["verified_by"])
                self.assertEqual(rows["neighbour"]["reviewed_by"], "Alex Example, CPA")
                self.assertEqual(index["counts"]["accountant_reviewed"], 1)
                self.assertEqual(stderr.getvalue().count("omitting reviewer claims"), 1)

    def test_index_tier_comes_from_the_mapping_not_quoted_continuation_text(self) -> None:
        for actual, expected in (("2", 2), (None, None), ("01", "01"), ("0x1", "0x1"),
                                 ('"1"', 1), ('"1" # comment', '"1" # comment'),
                                 ("1\n  extra", None), ("2\n  extra", None),
                                 ("&review-tier 1", "&review-tier 1"), ("!!int 1", "!!int 1")):
            with self.subTest(actual=actual), tempfile.TemporaryDirectory() as tmp:
                tree = Path(tmp)
                (tree / "skills").mkdir()
                text = ('---\nname: synthetic\ndescription: "Synthetic description.\n'
                        'tier: 1\nContinued description."\nreviewed_by: Alex Example, CPA\n')
                if actual is not None:
                    text += f"tier: {actual}\n"
                (tree / "skills/synthetic.md").write_text(text + "---\n# Body\n", encoding="utf-8")
                with mock.patch.object(build_index, "REPO_ROOT", str(tree)):
                    index = build_index.build_index()
                self.assertEqual(index["guides"][0]["tier"], expected)
                reviewed = int(expected == 1)
                self.assertEqual(index["counts"]["accountant_reviewed"], reviewed)
                partners, _ = roster.render_partners(index, {})
                self.assertEqual("| Alex Example, CPA |" in partners, bool(reviewed))


class RosterTests(unittest.TestCase):
    def test_rows_are_per_reviewer_most_guides_first(self) -> None:
        rows = roster.roster(GUIDES)
        self.assertEqual([r["reviewer"] for r in rows], ["Jane Doe, CPA", WITHHELD, "Ann Legacy"])
        jane = rows[0]
        self.assertEqual(jane["guides"], 3)
        self.assertEqual(jane["edited_since_review"], 1, "zz-income-tax is pending_review")
        self.assertEqual(dict(jane["jurisdictions"]), {"ZZ": 2, "YY": 1})
        self.assertEqual(jane["latest"], "2026-05-01")
        self.assertEqual(jane["slugs"], ["yy-income-tax", "zz-income-tax", "zz-vat"])
        self.assertTrue(jane["named"])
        self.assertFalse(rows[1]["named"])
        self.assertEqual([r["edited_since_review"] for r in rows[1:]], [0, 0])

    def test_by_jurisdiction(self) -> None:
        table = roster.by_jurisdiction(GUIDES)
        self.assertEqual(set(table), {"ZZ", "YY"})
        self.assertEqual(dict(table["YY"]), {WITHHELD: 1, "Jane Doe, CPA": 1})


class RenderTests(unittest.TestCase):
    def test_reviewer_table_cells_escape_multiline_and_pipe_names(self) -> None:
        name = "Alex | Example\\Practice\nCPA"
        guides = [g("synthetic", 1, reviewed_by=name)]
        index = {"guides": guides, "counts": {"jurisdictions": 1}}
        text, unused = roster.render_partners(index, {name: {"public_record": "https://example.test/alex"}})
        self.assertEqual(unused, [])
        escaped = "Alex \\| Example\\\\Practice<br>CPA"
        self.assertIn(f"| {escaped} | ZZ | 1 |", text)
        self.assertIn(f"| ZZ | 1 | {escaped} (1) |", text)
        self.assertNotIn("\nCPA |", text)
        self.assertIn("[profile](https://example.test/alex)", text)

    def test_render_is_derived_from_the_index_and_the_profiles(self) -> None:
        text, unused = roster.render_partners(INDEX, PROFILES)
        self.assertEqual(unused, [])
        self.assertTrue(text.startswith("# Partners: the accountants on record\n\n" + roster.GENERATED_MARKER))
        self.assertIn("**5 accountant-reviewed guides · 3 reviewers (2 named) · 2 of 5 jurisdictions"
                      " · 1 reviewed guide edited since its review.**", text)
        self.assertIn("| Reviewer (as recorded in the guides) | Jurisdictions | Guides | Edited since review "
                      "| Latest guide update | Public record |", text)
        self.assertIn("| Jane Doe, CPA | ZZ (2), YY (1) | 3 | 1 | 2026-05-01 | [profile](https://example.test/jane) |", text)
        self.assertIn("| Ann Legacy | ZZ | 1 | — | 2026-02-02 | — |", text)
        self.assertIn(f"| {WITHHELD} | YY | 1 | — | 2026-01-02 | [profile](https://example.test/anon) |", text)
        self.assertIn("| ZZ | 3 | Jane Doe, CPA (2); Ann Legacy (1) |", text)
        self.assertIn("The other 3 jurisdictions", text)
        self.assertIn(f"- **{WITHHELD}:** Named elsewhere.", text)
        self.assertNotIn("Bob Attribution", text, "a tier-2 name is not on the roster")

    def test_the_edited_since_review_note_counts_and_pluralises(self) -> None:
        untouched = [dict(guide, review_status=None) for guide in GUIDES]
        text, _ = roster.render_partners({**INDEX, "guides": untouched}, {})
        self.assertIn("· 2 of 5 jurisdictions.**", text)
        self.assertNotIn("edited since", text.split("## Reviewers")[0])
        two = [dict(guide, review_status="pending_review" if guide["slug"].startswith("zz-") else None)
               for guide in GUIDES]
        text, _ = roster.render_partners({**INDEX, "guides": two}, {})
        self.assertIn("· 3 reviewed guides edited since their review.**", text)
        self.assertIn("| Jane Doe, CPA | ZZ (2), YY (1) | 3 | 2 | 2026-05-01 | — |", text)
        self.assertIn("| Ann Legacy | ZZ | 1 | 1 | 2026-02-02 | — |", text)

    def test_a_profile_for_nobody_on_the_roster_is_reported_not_rendered(self) -> None:
        text, unused = roster.render_partners(INDEX, {**PROFILES, "Bob Attribution": {"public_record": "https://x"}})
        self.assertEqual(unused, ["Bob Attribution"])
        self.assertNotIn("https://x", text)

    def test_no_notes_section_without_notes(self) -> None:
        text, _ = roster.render_partners(INDEX, {})
        self.assertNotIn("## Notes recorded", text)
        self.assertNotIn("[profile]", text)


class CliTests(unittest.TestCase):
    def test_out_writes_the_render_and_reports_ghost_profiles(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            index_path = Path(tmp) / "index.json"
            profiles_path = Path(tmp) / "partners.json"
            out_path = Path(tmp) / "PARTNERS.md"
            index_path.write_text(json.dumps(INDEX), encoding="utf-8")
            profiles_path.write_text(json.dumps({"reviewers": {**PROFILES, "Ghost": {"public_record": "https://x"}}}),
                                     encoding="utf-8")
            stdout, stderr = io.StringIO(), io.StringIO()
            with mock.patch.object(roster, "INDEX_PATH", str(index_path)), \
                    mock.patch.object(roster, "PROFILES_PATH", str(profiles_path)), \
                    contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
                code = build_partners.main(["--out", str(out_path)])
            self.assertEqual(code, 0)
            expected, _ = roster.render_partners(INDEX, PROFILES)
            self.assertEqual(out_path.read_text(encoding="utf-8"), expected)
            self.assertIn("accountant-reviewed guides: 5", stdout.getvalue())
            self.assertIn("'Ghost'", stderr.getvalue())

    def test_unknown_option_and_missing_out_path_are_errors(self) -> None:
        with self.assertRaises(SystemExit):
            build_partners.main(["--out"])
        with self.assertRaises(SystemExit):
            build_partners.main(["--us-only"])


if __name__ == "__main__":
    unittest.main()
