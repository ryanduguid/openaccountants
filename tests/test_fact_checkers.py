import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"


class FactCheckerTests(unittest.TestCase):
    def run_checker(self, script, guides, expect_code=0, root="international",
                    extra_args=()):
        with tempfile.TemporaryDirectory() as directory:
            Path(directory, "docs").mkdir()
            for name, text in guides.items():
                path = Path(directory, "skills", root, name)
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(text, encoding="utf-8")
            result = subprocess.run(
                [sys.executable, "-X", "utf8", str(SCRIPTS / script), *extra_args],
                cwd=directory, capture_output=True, text=True, encoding="utf-8",
                timeout=30,
            )
        self.assertEqual(result.returncode, expect_code, result.stderr)
        return result.stdout

    def test_percentage_conflicts_include_tables_and_bullets(self):
        output = self.run_checker("check-fact-conflicts.py", {
            "example/overview.md": "- **Standard VAT rate** - 20%\n",
            "example/vat.md": "| Standard VAT rate | 25% |\n",
            "other/overview.md": "| Standard VAT rate | 30% |\n",
        })
        self.assertIn("labelled percentage facts extracted: 3", output)
        self.assertIn("keys where files disagree: 1", output)
        self.assertIn('int:example :: "standard vat"', output)

    def test_corporate_conflicts_group_by_country(self):
        output = self.run_checker("check-headline-cit.py", {
            "example/overview.md": "- **Standard corporate tax rate** - 20%\n",
            "example/cit.md": "- **Standard corporate tax rate** - 25%\n",
            "other/overview.md": "- **Standard corporate tax rate** - 30%\n",
        })
        self.assertIn("unqualified standard CIT rate: 2", output)
        self.assertRegex(output, r"CONFLICT\s+example\s+20, 25")
        self.assertNotRegex(output, r"CONFLICT\s+other\b")

    def test_form_register_groups_federal_guides(self):
        output = self.run_checker("build-form-register.py", {
            "issuance.md": "File Form 1099-NEC.\n",
            "payments.md": "Use Form 1099-NEC.\n",
        }, root="federal")
        self.assertIn("1 jurisdictions, 1 shared form identifiers", output)

    def test_registration_list_excludes_direct_taxes(self):
        output = self.run_checker("list-registration-thresholds.py", {
            "or/or-cat.md": "| CAT registration threshold | USD 750,000 |\n",
            "py/paraguay-payroll.md": "| IRP registration threshold | PYG 80,000,000 |\n",
            "cn/china-vat.md": "| Registration threshold | CNY 500,000 |\n",
        })
        self.assertNotIn("USD 750,000", output)
        self.assertNotIn("PYG 80,000,000", output)
        self.assertIn("CNY 500,000", output)

    def test_withholding_table_context_and_shared_rate(self):
        output = self.run_checker("list-withholding-rates.py", {
            "ng/wht.md": "## Withholding tax\n\n| Payment type | Rate |\n"
                          "| --- | --- |\n| Dividends | 10% |\n| Interest | 10% |\n"
                          "## Corporate income tax\n\n| Royalties | 30% |\n",
            "bs/overview.md": "- **WHT on dividends, interest and royalties** - 0%\n",
        })
        self.assertRegex(output, r"ng\s+dividends/unspecified\s+10%")
        self.assertRegex(output, r"ng\s+interest/unspecified\s+10%")
        self.assertNotRegex(output, r"ng\s+royalties")
        for kind in ("dividends", "interest", "royalties"):
            self.assertRegex(output, rf"bs\s+{kind}/unspecified\s+0%")

    def test_withholding_scope_queues_classic_only_jurisdictions(self):
        # "thin" states the three classic heads and nothing else, which is the
        # shape North Macedonia had while its statute charged eight heads.
        # "broad" names a service and a rent head as well, so it is not queued.
        output = self.run_checker("list-withholding-scope.py", {
            "thin/cit.md": (
                "- **Withholding tax on dividends** - 10%\n"
                "- **Withholding tax on interest** - 10%\n"
                "- **Withholding tax on royalties** - 10%\n"
            ),
            "broad/cit.md": (
                "- **Withholding tax on dividends** - 10%\n"
                "- **Withholding tax on management and professional fees** - 20%\n"
                "- **Withholding tax on rent paid to non-residents** - 30%\n"
            ),
        }, expect_code=1)
        self.assertIn("naming only classic heads: 1", output)
        self.assertIn("nothing else anywhere (the queue): 1", output)
        self.assertRegex(output, r"queue:\s+thin\b")
        self.assertNotRegex(output, r"queue:\s+broad\b")
        self.assertRegex(output, r"\bbroad\s+dividends, rent, services")

    def test_source_mix_flags_jurisdictions_with_no_authority_citation(self):
        # "onlypwc" rests entirely on a secondary summary; "mixed" also cites
        # the authority. Only the first is listed. The CTA block every guide
        # ends with must not count as a source either way.
        cta = ("\n\n[openaccountants.com](https://www.openaccountants.com) "
               "and https://calendly.com/oa/intro\n")
        output = self.run_checker("list-source-mix.py", {
            "onlypwc/cit.md": (
                "- **Rate** - 20% _(https://taxsummaries.pwc.com/x/corporate)_\n"
                "- **WHT** - 10% _(https://rivermate.com/guides/x)_\n" + cta
            ),
            "mixed/cit.md": (
                "- **Rate** - 20% _(https://taxsummaries.pwc.com/y/corporate)_\n"
                "- **WHT** - 10% _(https://www.irs.gov/pub/notice)_\n" + cta
            ),
        })
        self.assertRegex(output, r"2 secondary, 0 authority\s+onlypwc")
        self.assertNotRegex(output, r"\bmixed\b")
        self.assertIn("citing no authority domain at all: 1", output)
        self.assertIn("citations: 1 authority, 3 secondary", output)
        # it ranks, it does not accuse
        self.assertIn("ranks exposure, not diligence", output)

    def test_source_mix_counts_a_collection_agent_as_an_authority(self):
        # NCCPL computes and deducts Pakistan's securities CGT, so its
        # notification outranks any summary of it — but it is a .com, so a
        # bare government-domain test would score it as secondary.
        output = self.run_checker("list-source-mix.py", {
            "pk/cgt.md": "- **CGT** - 15% _(https://www.nccpl.com.pk/notice)_\n",
        })
        self.assertIn("citing no authority domain at all: 0", output)
        self.assertIn("citations: 1 authority, 0 secondary", output)

    def test_source_mix_matches_subdomains_of_known_authorities(self):
        # etax.atk-ks.org is the Kosovo tax administration's own filing portal
        # and info.altinn.no is Norway's reporting portal. An exact-match test
        # scored both as commercial sites, which is how Kosovo stayed on the
        # zero-authority list while citing its own revenue service.
        output = self.run_checker("list-source-mix.py", {
            "xk/vat.md": "- **VAT** - 18% _(https://etax.atk-ks.org/filing)_\n",
        })
        self.assertIn("citing no authority domain at all: 0", output)
        self.assertIn("citations: 1 authority, 0 secondary", output)

    def test_unclassified_lists_what_a_zero_authority_jurisdiction_cites(self):
        # The candidate filters — three citations, a two-letter TLD — hid every
        # authority found this session. So for a jurisdiction the script is
        # claiming cites no authority, the filters are skipped entirely: one
        # cited domain there is the difference between the claim and its
        # opposite, however rarely it appears.
        output = self.run_checker("list-source-mix.py", {
            "ad/vat.md": "- **IGI** - 4.5% _(https://www.impostos-example.ad/x)_\n",
        }, extra_args=["--unclassified"])
        self.assertIn("zero-authority", output)
        self.assertIn("impostos-example.ad (1)", output)

    def test_a_site_about_a_countrys_tax_is_not_that_countrys_authority(self):
        # manao.mg went on the allowlist as a "Madagascar tax portal", from its
        # name. Manao sells accounting software. It was the only domain scoring
        # as an authority for Madagascar, so one unchecked entry removed a
        # jurisdiction from the queue this script exists to produce — the
        # failure the allowlist can cause and never report.
        output = self.run_checker("list-source-mix.py", {
            "mg/vat.md": "- **TVA** - 20% _(https://manao.mg/fr/tva)_\n",
        })
        self.assertIn("citations: 0 authority, 1 secondary", output)
        self.assertIn("citing no authority domain at all: 1", output)

    def test_load_bearing_names_the_entry_a_jurisdiction_rests_on(self):
        # A missing allowlist entry over-reports risk and someone notices. A
        # wrong one under-reports it silently. --load-bearing ranks the entries
        # by what they are holding up, so the expensive mistakes get reviewed.
        output = self.run_checker("list-source-mix.py", {
            "bi/cit.md": (
                "- **CIT** - 30% _(https://www.obr.bi/rates)_\n"
                "- **VAT** - 18% _(https://taxatlas.io/burundi)_\n"
            ),
            "ee/pit.md": (
                "- **PIT** - 22% _(https://www.emta.ee/rates)_\n"
                "- **Filing** - March _(https://www.eesti.ee/filing)_\n"
            ),
        }, extra_args=["--load-bearing"])
        self.assertIn("obr.bi", output)
        self.assertRegex(output, r"bi\s+cited 1 time;")
        # Estonia cites two authorities, so neither is load-bearing alone.
        self.assertNotIn("emta.ee", output)

    def test_show_prints_the_rows_the_scan_counts(self):
        # heads_in() learned that a dedicated withholding guide does not repeat
        # the word in every row label; show() kept the old label-only test, so
        # `--show` dropped the entire rate table it was meant to display. A
        # diagnostic that under-reports against its own checker reads as proof
        # the rows are absent.
        guide = (
            "| Payment type | Default rate | Section |\n"
            "| Services -- individuals | 30% | 164 |\n"
            "| Rent -- commercial | 35% | 170 |\n"
        )
        output = self.run_checker("list-withholding-scope.py", {
            "il/il-tax-withholding.md": guide,
        }, extra_args=["--show", "il"])
        self.assertIn("Services -- individuals", output)
        self.assertIn("Rent -- commercial", output)
        self.assertIn("2 withholding-labelled line(s) in il", output)

    def test_midyear_changes_uses_each_jurisdictions_own_tax_year(self):
        # 1 August is mid-year for a calendar-year country and gets reported;
        # 1 July is the first day of Australia's year and does not. Without the
        # per-jurisdiction year start the second line is a false positive.
        output = self.run_checker("list-midyear-changes.py", {
            "cal/vat.md": (
                "| Tax year | Calendar year (1 January -- 31 December) |\n"
                "- **VAT standard rate** - **21%** from 1 August 2025\n"
            ),
            "aus/cit.md": (
                "| Tax year | 1 July 2025 - 30 June 2026 |\n"
                "- **Company rate** - **25%** from 1 July 2025\n"
            ),
        })
        self.assertRegex(output, r"cal\s+\(year starts 1/1\)")
        self.assertNotRegex(output, r"aus\s+\(year starts")
        self.assertIn("no stated split (since", output)

    def test_midyear_changes_accepts_a_split_stated_elsewhere_in_the_file(self):
        # Romania's shape: the rate row is terse and the return-mapping table
        # further down carries "21% from Aug 2025 / 19% before". Testing the
        # line alone reported four Romanian lines that were all fine.
        output = self.run_checker("list-midyear-changes.py", {
            "ro/vat.md": (
                "| Tax year | Calendar year |\n"
                "| 11% | Reduced (from 1 August 2025) replacing the former 9% "
                "and 5% categories | Fiscal Code |\n"
                "| Row 2 | Domestic supplies at reduced rate (11% from Aug 2025 "
                "/ 9% before) | 11%/9% |\n"
            ),
        })
        self.assertIn("no stated split (since 2025): 0 line(s)", output)

    def test_statute_links_spare_recognised_publishers(self):
        # The corpus convention is [Instrument name](where I read it), and
        # naming the Act while citing a summary of it is honest — so a link to
        # a recognised tax publisher is not reported. A link to an HR platform
        # is: a reader clicking it has no signal they have left the law behind.
        output = self.run_checker("list-statute-links.py", {
            "trap/cit.md": (
                "- **Rate** - 30% _([Code Général des Impôts (Bénin)]"
                "(https://www.rivermate.com/guides/benin))_\n"
            ),
            "convention/cit.md": (
                "- **Rate** - 30% _([Income Tax Act]"
                "(https://taxsummaries.pwc.com/x/corporate))_\n"
            ),
            "right/cit.md": (
                "- **Rate** - 30% _([Value Added Tax Act 1991]"
                "(https://frcs.org.fj/vat))_\n"
            ),
        })
        self.assertRegex(output, r"trap\s+1")
        self.assertNotRegex(output, r"\bconvention\b")
        self.assertNotRegex(output, r"\bright\b")
        self.assertIn("across 1 jurisdictions", output)
        self.assertIn("as described at", output)

    def test_statute_links_see_the_trailer_shape_not_only_markdown(self):
        # The generated fact blocks cite as `_(Instrument — https://host/path)_`
        # with no markdown link in it. Scanning only `[...](...)` missed that
        # shape entirely: the queue read 1 while 528 citations across 78
        # jurisdictions made the same misdirection. Madagascar names the Code
        # Général des Impôts 65 times and none of them was visible.
        output = self.run_checker("list-statute-links.py", {
            "mg/vat.md": (
                "- **VAT filing** - monthly  _(Code Général des Impôts "
                "(Madagascar) — TVA — https://manao.mg/fr/tva)_\n"
            ),
            "ok/vat.md": (
                "- **VAT rate** - 20%  _(Code Général des Impôts — "
                "https://taxsummaries.pwc.com/x)_\n"
            ),
        })
        self.assertRegex(output, r"mg\s+1")
        self.assertNotRegex(output, r"\bok\b")
        self.assertIn("across 1 jurisdictions", output)

    def test_a_trailer_around_a_markdown_link_is_one_citation(self):
        # Both patterns see the same line. The bare-URL pattern must not
        # re-match a URL that is already a markdown link target, or every
        # existing citation would be counted twice and the fix would look
        # like it had doubled the problem it measured.
        output = self.run_checker("list-statute-links.py", {
            "bj/cit.md": (
                "- **Rate** - 30% _([Code Général des Impôts (Bénin)]"
                "(https://www.rivermate.com/guides/benin))_\n"
            ),
        })
        self.assertIn("recognised tax publisher: 1 across 1 jurisdictions", output)

    def test_statute_links_see_past_a_plain_link_on_the_same_line(self):
        # The checker once stopped scanning a line at the first link that named
        # no instrument. 39 lines in the corpus open with a plain link, so every
        # statute link behind one was invisible — a false negative, which is the
        # kind that survives because the checker keeps looking clean.
        output = self.run_checker("list-statute-links.py", {
            "behind/cit.md": (
                "- See the [country guide](https://www.rivermate.com/benin) and "
                "_([Code Général des Impôts](https://www.rivermate.com/guides/benin))_\n"
            ),
        })
        self.assertRegex(output, r"behind\s+1")

    def test_statute_links_know_instruments_outside_common_law(self):
        # Ethiopia and Eritrea legislate by Proclamation and nothing else. A
        # vocabulary of Act/Code/Law/Decree silently exempts them: 18 of
        # Eritrea's citations were out of scope for no reason but wording.
        output = self.run_checker("list-statute-links.py", {
            "horn/cit.md": (
                "- **Rate** - 30% _([Income Tax Proclamation No. 24/2011]"
                "(https://taxatlas.io/country/eritrea))_\n"
            ),
            "lusophone/cit.md": (
                "- **Rate** - 25% _([Lei das Contribuições](https://remotepeople.com/x))_\n"
            ),
        })
        self.assertRegex(output, r"horn\s+1")
        self.assertRegex(output, r"lusophone\s+1")

    def test_a_scheme_publishing_its_own_ceiling_is_an_authority(self):
        # vinhi.vg is the BVI National Health Insurance scheme, not a marketing
        # site: its own bulletin sets the ceiling the guide quotes. Same class
        # as NCCPL and FRCS — the body that collects the charge, publishing the
        # table it collects under. Reporting it would condemn a good citation.
        output = self.run_checker("list-statute-links.py", {
            "vg/social.md": (
                "- **NHI ceiling** - US$102,000 _([National Health Insurance "
                "Regulations](https://www.vinhi.vg/nhi-contribution-breakdown/))_\n"
            ),
        })
        self.assertNotRegex(output, r"\bvg\b")
        self.assertIn("across 0 jurisdictions", output)

    def test_solo_citations_rank_uncorroborated_instruments(self):
        # "lonely" leans on one instrument nobody else cites; "shared" cites an
        # instrument that appears in a second guide, so it is corroborated
        # inside the corpus and is not ranked however often it appears.
        lonely = "Regulated by Portaria n.º 999/2024/1. " * 9
        shared = "Under Lei n.º 82/2023 the regime applies. " * 9
        output = self.run_checker("list-solo-citations.py", {
            "lonely/guide.md": lonely,
            "shared/guide.md": shared,
            "other/guide.md": "See also Lei n.º 82/2023 for the enabling provision.\n",
        })
        self.assertRegex(output, r"9x\s+Portaria 999/2024/1")
        self.assertNotRegex(output, r"Lei 82/2023")
        self.assertIn("cited 8+ times in exactly one guide", output)
        # it ranks, it does not accuse
        self.assertIn("blast-radius ranking, not a defect report", output)

    def test_withholding_scope_excludes_zero_rate_jurisdictions(self):
        # "nowht" charges nothing, so it names no service or rent head because
        # there is nothing to name. That is a complete guide, not a thin one,
        # and it must not sit in the same queue as "thin", which charges 10%
        # on royalties and says nothing about anything else.
        output = self.run_checker("list-withholding-scope.py", {
            "nowht/cit.md": (
                "- **Withholding tax on dividends** - 0% (no withholding tax "
                "on dividends)\n"
                "- **Withholding tax on interest and royalties** - None\n"
            ),
            "thin/cit.md": (
                "- **Withholding tax on dividends** - 0%\n"
                "- **Withholding tax on royalties** - 10%\n"
            ),
        }, expect_code=1)
        self.assertIn("withholding nothing at all (complete, not thin): 1", output)
        self.assertRegex(output, r"zero-wht:\s+nowht\b")
        self.assertIn("nothing else anywhere (the queue): 1", output)
        self.assertRegex(output, r"queue:\s+thin\b")
        self.assertNotRegex(output, r"queue:\s+nowht\b")

    def test_withholding_scope_separates_body_mentions_from_bare_entries(self):
        # "bare" names only the classic three and nothing else anywhere.
        # "mentions" also names only classic heads in its labels, but a bullet
        # body names a service head, so it is cheaper to triage than research
        # and is counted separately rather than sitting in the same queue.
        output = self.run_checker("list-withholding-scope.py", {
            "bare/cit.md": (
                "- **Withholding tax on dividends** - 10%\n"
                "- **Withholding tax on royalties** - 10%\n"
            ),
            "mentions/cit.md": (
                "- **Withholding tax on dividends** - 10%\n"
                "- **Withholding tax on royalties** - 10%, and management "
                "service fees are dealt with separately\n"
            ),
        }, expect_code=1)
        self.assertIn("naming only classic heads: 2", output)
        self.assertIn("nothing else anywhere (the queue): 1", output)
        self.assertIn("bullet body (triage first): 1", output)
        self.assertRegex(output, r"queue:\s+bare\b")
        self.assertRegex(output, r"triage:\s+mentions\s+body mentions services")

    def run_in_git(self, script, before, after, args=()):
        """Commit `before`, apply `after`, and run `script` against the commit.

        The incomplete-fix checker reads a diff rather than the tree, so it
        needs a real repository with a base commit to diff against. Everything
        else in this file can work from a bare temp directory.
        """
        with tempfile.TemporaryDirectory() as directory:
            def git(*argv):
                subprocess.run(["git"] + list(argv), cwd=directory, check=True,
                               capture_output=True, text=True)
            git("init", "-q", "-b", "work")
            git("config", "user.email", "t@example.invalid")
            git("config", "user.name", "T")
            git("config", "commit.gpgsign", "false")
            git("config", "tag.gpgsign", "false")
            for name, text in before.items():
                path = Path(directory, "skills", "international", name)
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(text, encoding="utf-8")
            git("add", "-A")
            git("commit", "-q", "-m", "base")
            # tag it: a branch name would move with the second commit and
            # `base...HEAD` would then be empty
            git("tag", "base")
            for name, text in after.items():
                Path(directory, "skills", "international", name).write_text(
                    text, encoding="utf-8")
            git("add", "-A")
            git("commit", "-q", "-m", "edit")
            result = subprocess.run(
                [sys.executable, "-X", "utf8", str(SCRIPTS / script),
                 "--base", "base"] + list(args),
                cwd=directory, capture_output=True, text=True, encoding="utf-8",
                timeout=30,
            )
        self.assertEqual(result.returncode, 0, result.stderr)
        return result.stdout

    def test_incomplete_fixes_selftest_passes(self):
        result = subprocess.run(
            [sys.executable, "-X", "utf8",
             str(SCRIPTS / "list-incomplete-fixes.py"), "--selftest"],
            capture_output=True, text=True, encoding="utf-8", timeout=30,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("known misses pass", result.stdout)

    def test_incomplete_fixes_reports_surviving_copies_of_a_removed_value(self):
        # The Pakistan shape: a table row is corrected from 45% to 35% while
        # three satellites elsewhere in the same file still say 45%. Two of
        # those satellites are untouched, so both must be reported with their
        # line numbers; the corrected row itself must not be.
        before = {"pk/tax.md": (
            "# Rates\n"
            "The top slab reaches 45% for the year.\n"
            "| top rate | 45% |\n"
            "Non-filers are charged at up to 45% under the same table.\n"
        )}
        after = {"pk/tax.md": (
            "# Rates\n"
            "The top slab reaches 45% for the year.\n"
            "| top rate | 35% |\n"
            "Non-filers are charged at up to 45% under the same table.\n"
        )}
        output = self.run_in_git("list-incomplete-fixes.py", before, after)
        self.assertIn("skills/international/pk/tax.md", output)
        self.assertRegex(output, r"\s+2\s+45%\s+The top slab reaches")
        self.assertRegex(output, r"\s+4\s+45%\s+Non-filers are charged")
        self.assertIn("still stands elsewhere: 1", output)
        # it ranks, it does not accuse
        self.assertIn("Read each surviving line before touching it", output)

    def test_incomplete_fixes_does_not_match_a_value_inside_a_longer_one(self):
        # Fiji: a removed "0%" matched inside "10%" two lines down and put a
        # correct guide on the worklist. Values match on token boundaries.
        before = {"fj/wht.md": (
            "- **Dividends** - 0% (position uncertain)\n"
            "- **Interest** - 10%\n"
            "- **Royalties** - 15%\n"
        )}
        after = {"fj/wht.md": (
            "- **Dividends** - 9% (confirmed with FRCS)\n"
            "- **Interest** - 10%\n"
            "- **Royalties** - 15%\n"
        )}
        output = self.run_in_git("list-incomplete-fixes.py", before, after)
        self.assertIn("still stands elsewhere: 0", output)
        self.assertNotIn("fj/wht.md\n", output)

    def test_withholding_scope_ignores_prose_and_cross_references(self):
        # Prose naming every head is not a charge, and a withholding label that
        # commits to no rate is a pointer to another section.
        output = self.run_checker("list-withholding-scope.py", {
            "broad/cit.md": (
                "Withholding taxes apply to dividends, interest and royalties.\n"
                "- **Withholding tax on services** - see the section below\n"
                "- **Withholding tax on dividends** - 10%\n"
                "- **Withholding tax on insurance premiums** - 4%\n"
            ),
        })
        self.assertIn("naming only classic heads: 0", output)
        # only the two labelled bullets that commit to a rate are counted, so
        # the interest and royalties named in the prose do not appear
        self.assertRegex(output, r"\bbroad\s+dividends, insurance\b")
        self.assertIn("heads named per jurisdiction: 2:1", output)


def _load(script):
    """Import a scripts/*.py module by path, for checkers with no CLI-only API."""
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        script.replace("-", "_").removesuffix(".py"), SCRIPTS / script)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class CitationRotTests(unittest.TestCase):
    """Offline tests for list-citation-rot.py.

    The script fetches the network, so the CLI is not exercised here; `judge`
    is the part that decides what a response means and it is pure.
    """

    def setUp(self):
        self.rot = _load("list-citation-rot.py")

    def test_a_live_domain_can_stop_being_the_ministry(self):
        # Benin cited its tax year to a PDF on finances.bj, the Ministry of
        # Finance's domain. It answers 200 and serves an Indonesian casino site.
        # A status-code check passes it, which is why the body is read.
        kind, evidence = self.rot.judge(
            200, "PRIMATOTO Akses Resmi Toto Slot Togel Situs Toto 4D BANDAR SLOT")
        self.assertEqual(kind, "rot")
        self.assertIn("togel", evidence.lower())

    def test_a_waf_turning_a_script_away_is_not_a_dead_citation(self):
        # impots.finances.gouv.bj -- Benin's real, live tax authority -- answers
        # curl with 406, and onrc.ro with a rejection page. Calling those dead
        # would bury the real findings under healthy sites.
        for code in (401, 403, 405, 406, 429, 451):
            with self.subTest(code=code):
                self.assertEqual(self.rot.judge(code, "Request Rejected")[0],
                                 "blocked")

    def test_an_institutional_page_is_demoted_not_dropped(self):
        # This is the test that matters most. The first draft SUPPRESSED a
        # squatter match when the page also read institutional, on the theory
        # that a gaming regulator legitimately uses those words. On the very
        # first real run that rule would have silently hidden the sharpest
        # finding in the corpus: Benin's own tax authority is serving injected
        # casino spam. Demoting to a printed bucket keeps it visible.
        kind, evidence = self.rot.judge(
            200, "Direction Générale des Impots BENIN -- Melbet Jordan Mol "
                 "Casino Online Casino Maldives ronybet Tomi Club Maldives")
        self.assertEqual(kind, "check")
        self.assertIn("casino", evidence.lower())

    def test_an_authority_serving_a_crash_is_not_ok(self):
        # obr.bi is Burundi's Revenue Office AND an entry on the authority
        # allowlist, and it answers HTTP 200 with a Joomla fatal. Status fine,
        # no squatter words, so every other rule here scored it `ok` -- a false
        # negative on exactly the kind of host this corpus most relies on.
        kind, evidence = self.rot.judge(
            200, 'Error displaying the error page: Application Instantiation '
                 'Error: Failed to start the session because headers have '
                 'already been sent by /home/obr/public_html/index.php')
        self.assertEqual(kind, 'broken')
        self.assertIn('instantiation', evidence.lower())
        self.assertEqual(
            self.rot.judge(200, 'Error establishing a database connection')[0],
            'broken')

    def test_a_parked_domain_reports_and_an_ordinary_page_does_not(self):
        self.assertEqual(self.rot.judge(200, "Buy this domain today.")[0], "rot")
        self.assertEqual(
            self.rot.judge(200, "Fiji Revenue and Customs Service VAT")[0], "ok")

    def test_nothing_answering_is_dead(self):
        for status in (None, 404, 410, 503):
            with self.subTest(status=status):
                self.assertEqual(self.rot.judge(status, "")[0], "dead")

    def test_the_corpus_own_site_is_not_a_citation_to_check(self):
        # Every guide ends with a CTA block linking openaccountants.com and a
        # Calendly booking page: thousands of citations, three hosts, nothing to
        # learn, and fetching them on every run is pure noise.
        import os
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory, "skills", "international", "x", "a.md")
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(
                "- **Rate** - 20%  _(Act — https://revenue.example.gov/x)_\n"
                "See [us](https://www.openaccountants.com/connect) or book at\n"
                "https://calendly.com/openaccountants/30min\n", encoding="utf-8")
            cwd = os.getcwd()
            try:
                os.chdir(directory)
                found = self.rot.cited_hosts()
            finally:
                os.chdir(cwd)
        self.assertEqual(sorted(found), ["revenue.example.gov"])
