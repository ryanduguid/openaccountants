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


def g(slug, tier, reviewed_by=None, verified_by=None, jurisdiction="ZZ", last_updated="2026-01-02"):
    return {
        "slug": slug, "path": f"skills/international/zz/{slug}.md", "name": slug,
        "jurisdiction": jurisdiction, "category": None, "tier": tier,
        "verified_by": verified_by, "reviewed_by": reviewed_by,
        "tax_year": 2026, "last_updated": last_updated,
    }


WITHHELD = "A licensed accountant (name withheld at their request)"

GUIDES = [
    g("zz-vat", 1, reviewed_by="Jane Doe, CPA", last_updated="2026-03-01"),
    g("zz-income-tax", 1, reviewed_by="Jane Doe, CPA", last_updated="2026-05-01"),
    g("zz-payroll", 1, verified_by="Ann Legacy", last_updated="2026-02-02"),
    g("yy-vat", 1, reviewed_by=WITHHELD, jurisdiction="YY"),
    g("yy-income-tax", 1, reviewed_by="Jane Doe, CPA", jurisdiction="YY"),
    g("xx-vat", 2, reviewed_by="Bob Attribution", jurisdiction="XX"),
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
        for marker in ("pending", "None", "no", "FALSE", "-", "n/a", "tbd", "", None):
            self.assertIsNone(roster.reviewer_of(g("a", 1, reviewed_by=marker)), marker)
            self.assertIsNone(roster.reviewer_of(g("a", 1, verified_by=marker)), marker)

    def test_the_withheld_reviewer_counts_as_a_reviewer_but_not_a_person(self) -> None:
        self.assertEqual(roster.reviewer_of(g("a", 1, reviewed_by=WITHHELD)), WITHHELD)
        self.assertFalse(roster.is_named(WITHHELD))
        self.assertTrue(roster.is_named("Jane Doe, CPA"))

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


class RosterTests(unittest.TestCase):
    def test_rows_are_per_reviewer_most_guides_first(self) -> None:
        rows = roster.roster(GUIDES)
        self.assertEqual([r["reviewer"] for r in rows], ["Jane Doe, CPA", WITHHELD, "Ann Legacy"])
        jane = rows[0]
        self.assertEqual(jane["guides"], 3)
        self.assertEqual(dict(jane["jurisdictions"]), {"ZZ": 2, "YY": 1})
        self.assertEqual(jane["latest"], "2026-05-01")
        self.assertEqual(jane["slugs"], ["yy-income-tax", "zz-income-tax", "zz-vat"])
        self.assertTrue(jane["named"])
        self.assertFalse(rows[1]["named"])

    def test_by_jurisdiction(self) -> None:
        table = roster.by_jurisdiction(GUIDES)
        self.assertEqual(set(table), {"ZZ", "YY"})
        self.assertEqual(dict(table["YY"]), {WITHHELD: 1, "Jane Doe, CPA": 1})


class RenderTests(unittest.TestCase):
    def test_render_is_derived_from_the_index_and_the_profiles(self) -> None:
        text, unused = roster.render_partners(INDEX, PROFILES)
        self.assertEqual(unused, [])
        self.assertTrue(text.startswith("# Partners: the accountants on record\n\n" + roster.GENERATED_MARKER))
        self.assertIn("**5 accountant-reviewed guides · 3 reviewers (2 named) · 2 of 5 jurisdictions.**", text)
        self.assertIn("| Jane Doe, CPA | ZZ (2), YY (1) | 3 | 2026-05-01 | [profile](https://example.test/jane) |", text)
        self.assertIn("| Ann Legacy | ZZ | 1 | 2026-02-02 | — |", text)
        self.assertIn(f"| {WITHHELD} | YY | 1 | 2026-01-02 | [profile](https://example.test/anon) |", text)
        self.assertIn("| ZZ | 3 | Jane Doe, CPA (2); Ann Legacy (1) |", text)
        self.assertIn("The other 3 jurisdictions", text)
        self.assertIn(f"- **{WITHHELD}:** Named elsewhere.", text)
        self.assertNotIn("Bob Attribution", text, "a tier-2 name is not on the roster")

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
