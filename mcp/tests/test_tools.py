"""list_skills pages, the category filter folds case, and search_skills ranks
matches from a corpus read once and caps its query.

Before 0.4.0 an unfiltered list_skills answered 360 KB in one response,
`category` was compared case-sensitively while `jurisdiction` was folded,
and every search re-read and re-parsed all 1,800 files (about 1.6 s), took
the first 25 matches in slug order with no ranking, and accepted a query of
any length.
"""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest import mock

from openaccountants_mcp import server


def _skill(name: str, title: str, jurisdiction: str = "XX", category: str = "international",
           body: str = "Body.", extra: str = "") -> str:
    return (
        "---\n"
        f"name: {name}\n"
        f"jurisdiction: {jurisdiction}\n"
        f"category: {category}\n"
        "tier: 2\n"
        "last_updated: 2026-01-02\n"
        f"{extra}"
        "---\n\n"
        f"# {title}\n\n{body}\n"
    )


class ToolTreeCase(unittest.TestCase):
    def setUp(self) -> None:
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.packages = Path(tmp.name)
        self._original = server.PACKAGES_DIR
        server.PACKAGES_DIR = self.packages
        server._index.cache_clear()
        self.addCleanup(self._restore)
        self.write({
            "xx/xx-vat.md": _skill("xx-vat", "XX VAT", body="The reverse charge applies. Reverse charge again."),
            "xx/xx-income-tax.md": _skill("xx-income-tax", "XX Income Tax", category="International",
                                          body="Nothing here about that mechanism."),
            "xx/xx-reverse-charge.md": _skill("xx-reverse-charge", "Reverse charge guide",
                                              body="One mention of the reverse charge."),
            "yy/yy-vat.md": _skill("yy-vat", "YY VAT", jurisdiction="YY",
                                   body="reverse charge, reverse charge, reverse charge, reverse charge."),
            "yy/yy-payroll.md": _skill("yy-payroll", "YY Payroll", jurisdiction="YY", category="payroll"),
        })

    def _restore(self) -> None:
        server.PACKAGES_DIR = self._original
        server._index.cache_clear()

    def write(self, files: dict[str, str]) -> None:
        for rel, text in files.items():
            path = self.packages / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")


class ListSkillsPagingTests(ToolTreeCase):
    def test_a_small_catalogue_fits_the_default_page(self) -> None:
        result = server.list_skills()
        self.assertEqual(
            (result["total"], result["returned"], result["offset"], result["limit"], result["next_offset"]),
            (5, 5, 0, server.LIST_DEFAULT_LIMIT, None),
        )
        self.assertEqual([s["slug"] for s in result["skills"]],
                         ["xx-income-tax", "xx-reverse-charge", "xx-vat", "yy-payroll", "yy-vat"])

    def test_pages_chain_through_next_offset(self) -> None:
        first = server.list_skills(limit=2)
        self.assertEqual([s["slug"] for s in first["skills"]], ["xx-income-tax", "xx-reverse-charge"])
        self.assertEqual((first["total"], first["returned"], first["next_offset"]), (5, 2, 2))
        self.assertIn("offset=2", first["next_action"])
        second = server.list_skills(limit=2, offset=first["next_offset"])
        self.assertEqual([s["slug"] for s in second["skills"]], ["xx-vat", "yy-payroll"])
        third = server.list_skills(limit=2, offset=second["next_offset"])
        self.assertEqual([s["slug"] for s in third["skills"]], ["yy-vat"])
        self.assertIsNone(third["next_offset"])
        self.assertNotIn("offset=", third["next_action"])

    def test_an_offset_past_the_end_is_empty_but_says_so(self) -> None:
        result = server.list_skills(offset=50)
        self.assertEqual((result["total"], result["returned"], result["next_offset"]), (5, 0, None))
        self.assertIn("past the last", result["next_action"])

    def test_invalid_pages_are_refused(self) -> None:
        for kwargs in ({"limit": 0}, {"limit": server.LIST_MAX_LIMIT + 1}, {"limit": True},
                       {"offset": -1}, {"limit": "10"}):
            with self.subTest(kwargs=kwargs), self.assertRaises(ValueError):
                server.list_skills(**kwargs)

    def test_category_filter_ignores_case_and_total_counts_every_match(self) -> None:
        listed = {s["slug"] for s in server.list_skills(category="INTERNATIONAL")["skills"]}
        self.assertEqual(listed, {"xx-vat", "xx-income-tax", "xx-reverse-charge", "yy-vat"})
        result = server.list_skills(jurisdiction="yy", category="Payroll", limit=1)
        self.assertEqual(result["total"], 1)
        self.assertEqual(result["skills"][0]["slug"], "yy-payroll")

    def test_legacy_category_names_select_the_canonical_category(self) -> None:
        # The names the catalogue served before 2026-09-29 keep working as
        # filters; results show only the canonical value.
        self.write({
            "us-ny/us-ny-sales-tax.md": _skill("us-ny-sales-tax", "NY sales tax", jurisdiction="US-NY",
                                               category="state-tax"),
            "us-federal/us-form-1040.md": _skill("us-form-1040", "Form 1040", jurisdiction="US",
                                                 category="federal"),
            "us-federal/us-lease-accounting.md": _skill("us-lease-accounting", "Leases", jurisdiction="US",
                                                        category="financial-statements"),
            "_shared/global-vendors.md": _skill("global-vendors", "Vendors", jurisdiction="GLOBAL",
                                                category="pattern"),
        })
        server._index.cache_clear()
        expected = {
            "state": "us-ny-sales-tax", "us-states": "us-ny-sales-tax", "STATE": "us-ny-sales-tax",
            "state-tax": "us-ny-sales-tax", "federal-tax": "us-form-1040", "federal": "us-form-1040",
            "financial-reporting": "us-lease-accounting", "financial-statements": "us-lease-accounting",
            "patterns": "global-vendors", "pattern": "global-vendors",
        }
        for requested, slug in expected.items():
            with self.subTest(category=requested):
                result = server.list_skills(category=requested)
                self.assertEqual([s["slug"] for s in result["skills"]], [slug])
                self.assertEqual(result["total"], 1)
                self.assertNotIn(result["skills"][0]["category"], server.LEGACY_CATEGORIES)

    def test_an_empty_catalogue_keeps_the_page_shape(self) -> None:
        server.PACKAGES_DIR = self.packages / "missing"
        server._index.cache_clear()
        result = server.list_skills(limit=5, offset=3)
        self.assertEqual(
            (result["total"], result["returned"], result["offset"], result["limit"], result["next_offset"]),
            (0, 0, 3, 5, None),
        )
        self.assertIn("error", result)


class ReviewStatusTests(ToolTreeCase):
    """review_status is review freshness, served beside quality_tier: `current`
    when the recorded sign-off covers the text, `pending_review` when the
    guide awaits one. It says nothing about the tier, which stays the one
    tier-1-plus-reviewer test."""

    def test_the_field_rides_the_catalogue_and_the_skill(self) -> None:
        reviewed = _skill("xx-stamp-duty", "XX Stamp Duty",
                          extra="reviewed_by: Alex Example, CPA\nreview_status: current\n")
        self.write({
            "xx/xx-cgt.md": _skill("xx-cgt", "XX CGT", extra="review_status: pending_review\n"),
            "xx/xx-stamp-duty.md": reviewed.replace("tier: 2\n", "tier: 1\n"),
        })
        server._index.cache_clear()
        listed = {s["slug"]: s for s in server.list_skills(jurisdiction="xx")["skills"]}
        self.assertEqual(listed["xx-cgt"]["review_status"], "pending_review")
        self.assertEqual(listed["xx-cgt"]["quality_tier"], "research-verified")
        self.assertEqual(listed["xx-stamp-duty"]["review_status"], "current")
        self.assertEqual(listed["xx-stamp-duty"]["quality_tier"], "accountant-verified")
        self.assertEqual(listed["xx-vat"]["review_status"], "", "absent is served as an empty string")
        self.assertEqual(server.get_skill("xx-cgt")["review_status"], "pending_review")
        self.assertEqual(server.get_skill("xx-stamp-duty")["review_status"], "current")

    def test_invalid_evidence_is_withheld_in_all_public_routes(self) -> None:
        slug = "xx-income-tax"
        valid = _skill(slug, "XX Income Tax", body="Assurance metadata needle. Alex Example contributed.",
                       extra="reviewed_by: Alex Example, CPA\nreview_status: current\n").replace("tier: 2\n", "tier: 1\n")

        def responses():
            listed = next(row for row in server.list_skills()["skills"] if row["slug"] == slug)
            hit = server.search_skills("assurance metadata needle")["results"][0]
            return {"list": listed, "search": hit, "full": server.get_skill(slug),
                    "sections": server.get_skill_sections(slug)}

        self.write({"xx/xx-income-tax.md": valid})
        server._index.cache_clear()
        baseline = responses()
        cases = (
            valid.replace("tier: 1\n", "tier: 2\ntier: 1\n"),
            valid.replace("tier: 1\n", "tier: 1\n  extra\n"),
            valid.replace("tier: 1\n", "tier: 2\n  extra\n"),
            valid.replace("tier: 1\n", "tier: 1\n<<:\n  <<: {a: 1}\n  <<: {b: 2}\n"),
            valid.replace("tier: 1\n", "tier: 01\n"),
            valid.replace("reviewed_by: Alex Example, CPA\n", "reviewed_by: true\nverified_by: Ann Legacy\n"),
            valid.replace("review_status: current\n", "review_status: [current]\n"),
            valid.replace("last_updated: 2026-01-02\n", "last_updated: 2026-02-30\n"),
            valid.replace("tier: 1\n", "tier: 1\ndescription: bad: colon\n"),
            valid.replace("tier: 1\n", "tier: 1\ndescription: true\n"),
            *(valid.replace("tier: 1\n", "tier: 1\n" + malformed + extra + "\n")
              for extra in ("extra: !!bool nonsense", 'extra: !!int ""', 'extra: !!float ""',
                            "last_updated: !!timestamp nonsense")
              for malformed in ("", "description: bad: colon\n")),
        )
        for text in cases:
            with self.subTest(text=text.split("---")[1]):
                self.write({"xx/xx-income-tax.md": text})
                server._index.cache_clear()
                actual = responses()
                for route, response in actual.items():
                    self.assertEqual(set(response), set(baseline[route]))
                    self.assertEqual(response["quality_tier"], "research-verified")
                    self.assertIsNone(response["verified_by"])
                    self.assertEqual(response["review_status"], "")
                footer = actual["full"]["markdown"].split("## Provenance & attribution", 1)[1]
                self.assertNotIn("**Verified by:**", footer)
                self.assertNotIn("verified by Alex", footer)
                self.assertIn("research-verified", footer)
                plan = server.start(intent="taxes", jurisdiction="XX")
                selected = next(row for row in plan["skills_to_load"] if row["slug"] == slug)
                self.assertEqual(selected["quality_tier"], "research-verified")

    def test_assurance_changes_refresh_only_after_clearing_both_caches(self) -> None:
        path = "xx/xx-income-tax.md"
        valid = _skill("xx-income-tax", "XX Income Tax", body="Assurance cache needle.",
                       extra="reviewed_by: Alex Example, CPA\nreview_status: current\n").replace("tier: 2\n", "tier: 1\n")
        invalid = valid.replace("tier: 1\n", "tier: 2\ntier: 1\n")
        self.write({path: valid})
        server._index.cache_clear()
        first = server.search_skills("assurance cache needle")["results"]
        self.assertEqual(first[0]["quality_tier"], "accountant-verified")
        self.write({path: invalid})
        self.assertEqual(server.search_skills("assurance cache needle")["results"], first)
        server._index.cache_clear()
        second = server.search_skills("assurance cache needle")["results"]
        self.assertEqual(second[0]["quality_tier"], "research-verified")
        self.assertIsNone(second[0]["verified_by"])
        self.write({path: valid})
        self.assertEqual(server.search_skills("assurance cache needle")["results"], second)
        server._index.cache_clear()
        self.assertEqual(server.search_skills("assurance cache needle")["results"], first)

    def test_search_and_sections_preserve_canonical_review_metadata(self) -> None:
        cases = (
            ("draft", 2, "reviewed_by: Alex Example, CPA\nreview_status: pending_review\n",
             "research-verified", None, "pending_review", "2026-01-02"),
            ("current", 1, "reviewed_by: Alex Example, CPA\nreview_status: current\n",
             "accountant-verified", "Alex Example, CPA", "current", "2026-01-02"),
            ("renewal", 1, "reviewed_by: Alex Example, CPA\nreview_status: pending_review\n",
             "accountant-verified", "Alex Example, CPA", "pending_review", "2026-01-02"),
            ("placeholder", 1, "reviewed_by: pending\nreview_status: pending_review\n",
             "research-verified", None, "pending_review", "2026-01-02"),
            ("legacy", 1, "verified_by: Alex Example, CPA\nreview_status: current\n",
             "accountant-verified", "Alex Example, CPA", "current", "2026-01-02"),
            ("missing", 2, "", "research-verified", None, "", ""),
        )
        fields = ("quality_tier", "verified_by", "review_status", "last_updated")
        for name, tier, extra, *_ in cases:
            text = _skill(f"xx-{name}", name, body="Review metadata needle.", extra=extra)
            text = text.replace("tier: 2\n", f"tier: {tier}\n")
            if name == "missing":
                text = text.replace("last_updated: 2026-01-02\n", "")
            self.write({f"xx/xx-{name}.md": text})
        server._index.cache_clear()
        hits = {r["slug"]: r for r in server.search_skills("review metadata needle")["results"]}
        for name, _, _, *values in cases:
            slug = f"xx-{name}"
            for route, response in (("full", server.get_skill(slug)),
                                    ("sections", server.get_skill_sections(slug)),
                                    ("search", hits[slug])):
                with self.subTest(guide=name, route=route):
                    self.assertEqual({key: response[key] for key in fields}, dict(zip(fields, values)))
                    for key, expected in zip(fields, values):
                        self.assertIs(type(response[key]), type(expected), key)


class SearchSkillsTests(ToolTreeCase):
    def test_search_requires_the_full_guide_before_applying_rules(self) -> None:
        action = server.search_skills("reverse charge")["next_action"]
        self.assertIn("snippets can omit conditions", action)
        self.assertIn("get_skill(slug)", action)
        self.assertIn("full guide", action)
        self.assertIn("before applying", action)

    def test_review_metadata_uses_the_cached_catalogue_until_cleared(self) -> None:
        path = "xx/xx-income-tax.md"
        self.write({path: _skill("xx-income-tax", "XX Income Tax", body="Metadata needle.",
                                extra="review_status: pending_review\n")})
        server._index.cache_clear()
        first = server.search_skills("metadata needle")["results"]
        self.assertEqual(first[0]["review_status"], "pending_review")
        self.write({path: _skill("xx-income-tax", "XX Income Tax", body="Metadata needle.",
                                extra="reviewed_by: Alex Example, CPA\nreview_status: current\n")
                    .replace("tier: 2\n", "tier: 1\n")
                    .replace("2026-01-02", "2026-02-03")})
        self.assertEqual(server.search_skills("metadata needle")["results"], first)
        server._index.cache_clear()
        fresh = server.search_skills("metadata needle")["results"][0]
        self.assertEqual(fresh["quality_tier"], "accountant-verified")
        self.assertEqual(fresh["verified_by"], "Alex Example, CPA")
        self.assertEqual(fresh["review_status"], "current")
        self.assertEqual(fresh["last_updated"], "2026-02-03")

    def test_search_names_the_enclosing_heading_and_a_heading_match_itself(self) -> None:
        self.write({"xx/xx-income-tax.md": _skill(
            "xx-income-tax", "XX Income Tax", body="Intro.\n\n## Allowances\nNeedle applies.",
        )})
        server._index.cache_clear()
        self.assertEqual(server.search_skills("needle")["results"][0]["matched_section"], "Allowances")
        self.assertEqual(server.search_skills("allowances")["results"][0]["matched_section"], "Allowances")

    def test_lowercase_expansion_does_not_shift_the_snippet_or_heading(self) -> None:
        self.write({"xx/xx-income-tax.md": _skill(
            "xx-income-tax", "XX Income Tax", body="İ" * 200 + "\n\n## Allowances\nNeedle applies.",
        )})
        server._index.cache_clear()
        result = server.search_skills("needle")["results"][0]
        self.assertEqual(result["matched_section"], "Allowances")
        self.assertIn("Needle applies.", result["snippet"])
        self.assertEqual(result["matches"], 1)

    def test_search_keeps_literal_lowercase_semantics(self) -> None:
        self.write({"xx/xx-income-tax.md": _skill("xx-income-tax", "XX Income Tax", body="Straße")})
        server._index.cache_clear()
        self.assertEqual(server.search_skills("STRASSE")["total"], 0)
        self.assertEqual(server.search_skills("STRAẞE")["total"], 1)

    def test_results_rank_by_occurrences_with_a_title_bonus_and_report_the_total(self) -> None:
        result = server.search_skills("reverse charge")
        self.assertEqual((result["total"], result["returned"]), (3, 3))
        # two hits (the H1 and one sentence) plus the title bonus (12) beat four
        # body hits, which beat two
        self.assertEqual([r["slug"] for r in result["results"]], ["xx-reverse-charge", "yy-vat", "xx-vat"])
        self.assertEqual([r["matches"] for r in result["results"]], [2, 4, 2])
        self.assertEqual(result["results"][1]["jurisdiction"], "YY")
        self.assertIn("reverse charge", result["results"][2]["snippet"].lower())

    def test_jurisdiction_filter_and_the_result_cap(self) -> None:
        result = server.search_skills("reverse charge", jurisdiction="yy")
        self.assertEqual([r["slug"] for r in result["results"]], ["yy-vat"])
        with mock.patch.object(server, "SEARCH_LIMIT", 2):
            result = server.search_skills("reverse charge")
        self.assertEqual((result["total"], result["returned"]), (3, 2))
        self.assertEqual([r["slug"] for r in result["results"]], ["xx-reverse-charge", "yy-vat"])

    def test_query_is_required_and_capped(self) -> None:
        with self.assertRaises(ValueError):
            server.search_skills("   ")
        with self.assertRaises(ValueError) as caught:
            server.search_skills("x" * (server.MAX_QUERY_CHARS + 1))
        self.assertIn("too long", str(caught.exception))
        self.assertEqual(server.search_skills("x" * server.MAX_QUERY_CHARS)["total"], 0)

    def test_the_corpus_is_read_once_and_cleared_with_the_catalogue(self) -> None:
        first = server.search_skills("mechanism")
        self.assertEqual(first["total"], 1)
        self.assertIn("mechanism", first["results"][0]["snippet"])
        (self.packages / "xx" / "xx-income-tax.md").write_text(
            _skill("xx-income-tax", "XX Income Tax", body="Rewritten without the word."), encoding="utf-8",
        )
        again = server.search_skills("mechanism")
        self.assertEqual(again["total"], 1, "served from the corpus read at the first search")
        self.assertEqual(again["results"], first["results"],
                         "the snippet is cut from the snapshot the count came from, not the live file")
        server._index.cache_clear()
        self.assertEqual(server.search_skills("mechanism")["total"], 0)


class MarkdownSectionsTests(ToolTreeCase):
    def test_heading_whitespace_preserves_titles_sections_and_snippets(self) -> None:
        cases = (
            ("# Alpha", "Alpha", "Alpha", 1),
            ("#   Alpha   ", "Alpha", "Alpha", 1),
            ("#\tAlpha", None, "Alpha", 1),
            ("## Alpha ###   ", None, "Alpha ###", 2),
            ("###\tCaf\u00e9\u2003 ", None, "Caf\u00e9", 3),
            ("#    ", None, "", None),
            ("####### Alpha", None, "", None),
        )
        for line, title, heading, level in cases:
            with self.subTest(line=line):
                body = line + "\nneedle"
                self.assertEqual(server._first_h1(body), title)
                expected = ([{"heading": heading, "level": level, "content": "needle"}]
                            if level else [])
                self.assertEqual(server._split_sections(body), expected)
                self.assertEqual(server._extract_match(body, "needle"),
                                 (heading, " ".join(body.split())))

    def test_a_long_whitespace_only_heading_is_rejected(self) -> None:
        body = "# " + " " * 100_000 + "\nneedle"
        self.assertEqual(list(server._iter_headings(body)), [])
        self.assertEqual(server._split_sections(body), [])
        self.assertEqual(server._extract_match(body, "needle")[0], "")

    def test_fenced_headings_remain_in_their_section_and_search_still_matches_code(self) -> None:
        for opener, closer in (("```python", "```"), ("~~~python", "~~~"),
                               ("   ````python", "   ````")):
            with self.subTest(opener=opener):
                body = f"## Example\nBefore.\n{opener}\n## Fake heading\nneedle\n{closer}\nAfter.\n## Next\nEnd."
                self.write({"xx/xx-income-tax.md": _skill("xx-income-tax", "XX Income Tax", body=body)})
                server._index.cache_clear()
                sections = server.get_skill_sections("xx-income-tax")["sections"]
                self.assertEqual([s["heading"] for s in sections], ["XX Income Tax", "Example", "Next"])
                self.assertEqual(sections[1]["content"],
                                 f"Before.\n{opener}\n## Fake heading\nneedle\n{closer}\nAfter.")
                result = server.search_skills("needle")["results"][0]
                self.assertEqual(result["matched_section"], "Example")
                self.assertEqual(result["matches"], 1)

    def test_a_short_wrong_or_suffixed_closer_keeps_the_fence_open(self) -> None:
        for false_closer in ("```", "~~~~", "```` trailing"):
            with self.subTest(false_closer=false_closer):
                body = f"# Outer\n````markdown\n{false_closer}\n## Fake\nneedle\n````\n## Real\nDone."
                sections = server._split_sections(body)
                self.assertEqual([s["heading"] for s in sections], ["Outer", "Real"])
                self.assertIn("## Fake\nneedle", sections[0]["content"])
                self.assertEqual(server._extract_match(body, "needle")[0], "Outer")

    def test_an_unclosed_fence_runs_to_the_end(self) -> None:
        sections = server._split_sections("# Outer\n~~~\n## Fake\nneedle\n")
        self.assertEqual(sections, [{"heading": "Outer", "level": 1,
                                     "content": "~~~\n## Fake\nneedle"}])

    def test_backticks_in_an_opening_info_string_do_not_open_a_fence(self) -> None:
        sections = server._split_sections("# Outer\n```invalid`info\n## Real\nContent.")
        self.assertEqual([s["heading"] for s in sections], ["Outer", "Real"])

    def test_ordinary_section_whitespace_and_preamble_are_preserved(self) -> None:
        body = "Preamble.\r\n# Outer\r\n\r\nFirst.\r\n\r\n## Next\r\nLast.\r\n"
        self.assertEqual(server._split_sections(body), [
            {"heading": "Outer", "level": 1, "content": "First."},
            {"heading": "Next", "level": 2, "content": "Last."},
        ])


if __name__ == "__main__":
    unittest.main()
