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
           body: str = "Body.") -> str:
    return (
        "---\n"
        f"name: {name}\n"
        f"jurisdiction: {jurisdiction}\n"
        f"category: {category}\n"
        "tier: 2\n"
        "last_updated: 2026-01-02\n"
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

    def test_an_empty_catalogue_keeps_the_page_shape(self) -> None:
        server.PACKAGES_DIR = self.packages / "missing"
        server._index.cache_clear()
        result = server.list_skills(limit=5, offset=3)
        self.assertEqual(
            (result["total"], result["returned"], result["offset"], result["limit"], result["next_offset"]),
            (0, 0, 3, 5, None),
        )
        self.assertIn("error", result)


class SearchSkillsTests(ToolTreeCase):
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
        self.assertEqual(server.search_skills("mechanism")["total"], 1)
        (self.packages / "xx" / "xx-income-tax.md").write_text(
            _skill("xx-income-tax", "XX Income Tax", body="Rewritten without the word."), encoding="utf-8",
        )
        self.assertEqual(server.search_skills("mechanism")["total"], 1,
                         "served from the corpus read at the first search")
        server._index.cache_clear()
        self.assertEqual(server.search_skills("mechanism")["total"], 0)


if __name__ == "__main__":
    unittest.main()
