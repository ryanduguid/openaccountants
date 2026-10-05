# US treaties: Netherlands rules

The Netherlands section labelled interest and royalties as complete
exemptions, gave technical services a blanket zero rate and repeated bare
bilateral 5/0/0 figures. It omitted parent and pension exemptions, fund
restrictions and a Netherlands PE row. This correction starts from clean
main `615e925`, advances `us-major-partners` to version 1.6 and covers
US-source income paid to Netherlands residents for tax year 2025. It
remains tier 2 and pending qualified professional review.

I compared the [1992 Convention and 1993 Protocol][convention],
[original explanation][original-te], [2004 Protocol][protocol],
[2004 explanation][te] and [2004 exchange of notes/Understanding][notes].
The [IRS treaty index][irs-index] still linked those documents when read
on 6 October 2026. Among the changes relevant here, the 2004 Protocol
replaces arts 10 and 26 and amends arts 4, 11 and 24. The accompanying
exchange of notes supplies the superseding 2004 Understanding, replacing
the 1992 Understanding and related 1993 notes. Original explanations are
interpretive evidence for retained provisions; obsolete LOB references
and domestic examples do not establish current rules.

| Document | Pages | SHA-256 |
| --- | --- | --- |
| Convention and 1993 Protocol | 74 | `337c5b3ee9da65ddc5a2ee9fc988553f716b92f6898370bb0da8f602c99e75ad` |
| 2004 Protocol | 19 | `7e5ad0804d0da718c70ffab1414f6db81430b29b485efdf2c76339bf41b5822f` |
| 2004 explanation | 42 | `429e65256c38fdb764c32bdaea436427496325c0fe4ce1ab4330c15c7efcb144` |
| 2004 notes and Understanding | 23 | `4aeefbf5b2e587bc8b83a3d6db35d836868678371395fa3224379ccb76dcadac` |
| 2003 pension hybrid arrangement | 1 | `4953a99b4ca2d9643266992e7d9a8ac25c44294e84e13a2e38d7da5c5bc9bae3` |
| 2010 pension certification amendment | 1 | `463e6740f9ab4150edf49e8b83c5509eef64ffd7cb0253f662f6f35428207c1f` |

All PDFs extracted through pdf-inspector. The first four diplomatic-note
pages required local offline OCR; their remaining substantive Understanding
pages extracted natively. The OCR text confirms the supersession statement;
imperfect signatures do not support any financial conclusion. The other
five PDFs extracted natively without OCR. Source provenance records retain
HTTP observations, original hashes and extraction results.

The [Dutch treaty database][database] lists the 1993 and 2004 child
protocols and no termination date. Its modifications view had no entries.
The current [Dutch government consolidation][consolidated] resolves to
the version valid from 28 December 2004 and includes authentic English
and Dutch text. I compared its English dividend, branch-tax, interest,
royalty, independent-services, offshore and pension provisions with the
US packet. This closes the focused Dutch-side instrument-status gap;
it does not certify a complete bilingual or later-agreement audit. An
initial date-qualified consolidation URL returned 404; the canonical
URL returned HTTP 200 and the current version.

[US Treasury's announcement][force] records entry into force on
28 December 2004, application to other taxable periods from 1 January
2005 and withholding application from 1 February 2005. The amended
provisions therefore apply for the guide's 2025 scope.

| Earlier statement or omission | Correction and primary pinpoint |
| --- | --- |
| Substantial dividends at 5% without category limits | Art 10(1)–(2) requires a US-resident payer for this directional table and a Netherlands resident company beneficial owner directly holding at least 10% voting power; it is a maximum on gross dividends, subject to entitlement and paragraph 4/7 exceptions. Art 10(8) separately prevents the specified US secondary tax on dividends paid by Netherlands-resident companies. |
| No parent category | Art 10(3) requires direct ownership of at least 80% for twelve months ending on declaration, plus historical pre-1 October 1998 ownership, art 26(2)(c), item-specific art 26(3), or an actual paragraph 7 determination for this relief. General entitlement still applies. |
| No fund boundary | Art 10(4) removes the 5% ceiling and parent exemption for US RIC/REIT dividends; REIT access to the 15% ceiling has four alternatives, including qualifying Dutch beleggingsinstellingen. |
| No pension category | Art 35, including the 1993 amendment, is separate from ordinary fund rules. Art 26(2)(d), Understanding XXXVII and the 2003/2007 agreements add qualification, related-person, hybrid and distribution boundaries. |
| Interest completely exempt | Art 12(1) relief depends on paragraphs 2 to 8. Profit-participating debt uses art 10(6); REMIC excess inclusions lose paragraph 1 exemption. Attribution and special-relationship excess have separate rules. |
| Royalties completely exempt | Art 13(2) defines the covered property and contingent gains, excludes the specified film/broadcast works, and paragraphs 3 to 6 constrain relief. The third-jurisdiction exception differs from interest. |
| Technical services always zero | Arts 7 and 15 separately govern enterprises and independent individuals; classification and art 27 offshore rules can change the result. |
| No Netherlands PE row | Art 5(3) uses more than twelve months; art 27 has different aggregate enterprise and continuous independent-activity thresholds. |

I compared the following boundaries manually, assuming the remaining
article conditions are met. These are paragraph comparisons, not taxpayer
calculations or tests that prove prose by matching the desired answer.

| Boundary | Primary comparison |
| --- | --- |
| Corporate holding exactly 10% directly | Meets art 10(2)(a)'s ownership bound; below 10% does not. The explanation's conditional proportionate transparent-entity interpretation for this paragraph is not extended to the direct 80% parent test. |
| Parent owns exactly 80% for twelve months ending on declaration | Meets the numerical/duration bounds; payment-date measurement or general active-business eligibility alone does not establish art 10(3). Its additional entitlement route remains necessary. |
| REIT individual owns exactly 25% | Meets paragraph 4(c)(i)'s bound; exceeding it requires another alternative. Publicly traded/5%, diversified/10% and eligible fund-to-fund alternatives are separate. |
| Pension participants exactly 50% resident in either state | Does not meet art 26(2)(d)(i)'s more-than-50% limb; the official 2004 explanation measures it at the close of the preceding taxable year and treats beneficiaries as persons receiving benefits. An entitled sponsor is a separate route. |
| REIT diversification includes foreclosure property or partnership holdings | The official 2004 explanation disregards foreclosure property and looks through partnership holdings proportionately when applying the single-property 10% bound. |
| Related payer ownership exactly 80% | Does not meet Understanding XXXVII's more-than-80% bound. Vote or value of any class is tested; the trade/business exclusion still applies. |
| Third-jurisdiction PE aggregate tax exactly 60% of the Netherlands general company-tax rate | Does not meet arts 12(8)/13(6)'s less-than-60% condition. Below it permits at most 15% of gross, subject to each article's distinct exception. The comparison is combined residence/third-jurisdiction tax, not an absolute 60% tax rate. |
| Active third-jurisdiction investment management | Does not automatically qualify for the interest exception. Qualifying bank/insurer activities are distinguished; Understanding XXI includes group financing and portfolio investment. |
| Intangible produced or developed by the third-jurisdiction PE | Falls within art 13(6)'s stated exception; merely having an active business does not substitute for that condition. |
| Construction exactly twelve months | Does not pass art 5(3)'s duration limb; other PE grounds remain relevant. |
| Enterprise offshore activity exactly 30 aggregate days in the calendar year | Does not pass art 27(3)'s duration limb; more than 30 does. Same-project continuing associated activity is aggregated using the one-third capital test, subject to paragraph 4 exclusions. Understanding XXX and art 3(1)(h) prevent treating a Netherlands enterprise's operation solely between US places, including the specified offshore locations, as international traffic. |
| Independent offshore activity exactly 30 continuous days | Meets art 27(5)'s duration bound; scattered days cannot replace its continuous-period test. Art 5/15 grounds are checked first. |
| Services performed in the Netherlands | Do not satisfy art 15's not-performed-in-residence-state condition for US taxation. Services elsewhere still require attribution to a regularly available US fixed base. |

Art 24(4) derivation through transparent persons is limited to the portion
treated as resident income by residence-state law. It does not establish
beneficial ownership or LOB entitlement. Art 24(1)'s saving clause and
art 24(3)'s deferred attribution remain visible. Amended art 11(3) keeps
separate additional branch tax within the 5% ceiling, with its own
historical, public-company, derivative or discretionary exemption routes.
Article 11(5) separately prohibits the additional tax on art 14(1) income
from disposing of shares or comparable corporate rights. Article 11(1)'s
tax and net-equity adjustments define its treaty base. Those rules do not
determine current domestic branch-tax calculations. Amended arts 4 and
24 are cited with their Protocol amendments and current consolidation.

The [IRS competent-authority index][caa-index] lists the
[2003 hybrid arrangement][pension-2003], [2007 qualification agreement][pension-2007]
and [2010 certification amendment][pension-2010]. The 2007 agreement
distinguishes RIC/REIT real-property gains from amounts deemed dividends
under the referenced US provision, and recognises specified qualifying
Dutch pension vehicles subject to entitlement and art 35(2). The 2010
amendment concerns US funds claiming Dutch relief; it is outside the
US-source table. Their historical form/certification statements are not
current instructions. Current Dutch vehicle status, distribution
classification and the art 35/REMIC interaction remain unverified. The
pension table and summary exclude REMIC excess inclusions from their
exemption conclusion, pending separate current-law and art 35 analysis.

The source guide, generated mirror, index, this entry and the log index
are the five changed paths. Thirteen other partner bodies, all other
summary rows and the exact disclaimer/CTA are byte-protected against
the base. Generators and existing gates verify repository consistency;
they do not establish treaty interpretation or financial accuracy.
The existing Windows checks passed with the repository's Python 3.14.7
environment: all nineteen recorded invocations exited zero. The root
suite ran 375 tests with nine local platform skips; all 77 MCP tests
passed without skips. The four generators reproduced the tracked
content; only the dynamic index timestamp differed, and that difference
was proved before restoring the committed timestamp.

At pre-repair head `e93a16300f2e39a7f24d9492bfb643c2630f5406`, the
complementary Linux Python 3.11.17 run passed all ten checks: full
validation, six gates, the offline cited-host selftest, 375 root tests
with three Windows-only skips and 77 MCP tests without skips. The owned
managed job returned `result=success`, `code=exited`, `status=0`; five
committed path hashes matched its snapshot. That snapshot had no Git
metadata, so Git-dependent deletion and changed-head checks were covered
on Windows. These results establish repository consistency, not treaty
interpretation. The independent financial review then identified the
qualification and citation omissions repaired above. The repaired
candidate's checks and the same reviewer's recheck belong in the pull
request's verification record.

| Repository command, from the documented working directory | Result |
| --- | --- |
| `python scripts/build-packages.py`, `build-index.py`, `build-partners.py`, `build-llms-full.py` | All four passed; counts remain 1,875 guides, 243 jurisdictions and 164 accountant-reviewed guides. |
| `python scripts/validate-guides.py` | Passed with the existing five jurisdiction omissions in one warning group. |
| `python scripts/validate-guides.py --changed-only --no-index-check` | Passed. |
| `python scripts/check-sync-integrity.py --base 615e925236fe0ae7a6b76566f2bba8595e04f0f7 --head HEAD --mode audit --strict-metadata` | Passed for the changed source guide. |
| `python scripts/check-{arithmetic,bracket-tables,expired-rules,fact-conflicts,coverage-claims,sourcing-floor}.py`, each run separately | All six passed; no baseline change. Accepted findings remain 35, 40, 27, 132, zero and 1,235 respectively. |
| `python scripts/check-cited-hosts.py --selftest` | Offline selftest passed; this does not validate live links. |
| `python -m unittest discover -s tests -p "test_*.py"`, at root and separately in `mcp/` | Passed with the counts above. |
| `python scripts/list-incomplete-fixes.py --base origin/main` | Read the surviving figures in other partner bodies and the generated mirror; they are outside this Netherlands correction. |
| `python scripts/list-midyear-changes.py --since 2025` | No lines reported; this is advisory. |
| `git diff --check 615e925236fe0ae7a6b76566f2bba8595e04f0f7 HEAD` | Passed. |

Named professional sign-off, taxpayer facts, current domestic tax,
withholding/forms/refunds, reciprocal Dutch treatment, complete
later-agreement or bilingual review, taxpayer end-to-end use and
whole-corpus financial/network citation accuracy remain unverified.
Aikido code scanning is not applicable to this content-only correction.

[convention]: https://www.irs.gov/pub/irs-trty/nether.pdf
[original-te]: https://www.irs.gov/businesses/international-businesses/netherlands-technical-explanation
[protocol]: https://home.treasury.gov/system/files/131/Treaty-Netherlands-Protocol-3-8-2004.pdf
[te]: https://www.irs.gov/pub/irs-trty/netherte04.pdf
[notes]: https://home.treasury.gov/system/files/131/Treaty-Netherlands-Protocol-Note-3-8-2004.pdf
[irs-index]: https://www.irs.gov/businesses/international-businesses/netherlands-tax-treaty-documents
[database]: https://verdragenbank.overheid.nl/en/Treaty/Details/005134.html
[consolidated]: https://wetten.overheid.nl/BWBV0001109/2004-12-28
[force]: https://home.treasury.gov/news/press-releases/js2172
[caa-index]: https://www.irs.gov/individuals/international-taxpayers/competent-authority-arrangements
[pension-2003]: https://www.irs.gov/pub/irs-news/ir-03-37.pdf
[pension-2007]: https://www.irs.gov/irb/2007-36_IRB
[pension-2010]: https://www.irs.gov/pub/irs-lbi/dutch_certification_pensions_agreement.pdf
