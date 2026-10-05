# US treaties: Ireland rules

The Ireland section presented interest and royalties as complete exemptions,
gave technical services a generic zero rate and repeated a bilateral 5/0/0
summary. It omitted the amended RIC/REIT restrictions, interest exceptions
and Ireland's PE rules. This correction starts from clean main `ec0781b`,
advances `us-major-partners` to version 1.7 and covers conditional US-source
treaty treatment for Irish residents for tax year 2025. The ordinary 15%/5%
dividend ceilings and ordinary interest/royalty exemptions remain. The guide
is tier 2 with `pending_review` status.

I compared the [Revenue convention and Protocol][convention], [IRS
convention][irs-convention], [1997 Treasury explanation][explanation],
both governments' [1999][amendment] [amendment texts][irs-amendment] and
the [2006 common-contractual-fund agreement][ccf]. The [IRS index][index]
and [Revenue country page][revenue-index] were read on 6 October 2026.
Both amendments replace only art 10(4). The 1997 convention and explanation
must therefore be read with the amended fund-dividend rule. Historical
domestic rates and Irish-credit examples do not establish 2025 treatment.

| Document | Pages | SHA-256 |
| --- | --- | --- |
| IRS 1997 convention | 41 | `1396fb82bdcb5ab3c6da7c607c39bf0b8d4a616d1ddcdfb210ca2f44d58f1b8f` |
| Treasury explanation | 100 | `562eca0bf454be588f2c6db72f6506c1ca751a6435c78dfd5902327d2a7849df` |
| IRS 1999 amendment | 2 | `86edb68bf258750cf53e667bd925093ac0ac10f91c5343c704a854344bfb2098` |
| Revenue 1999 amendment | 2 | `a2bca765daaf9e5532d32d79c7e877e2f26e5ac71987f0244aebddbebfe84ccd` |
| Revenue CCF agreement | 3 | `26b6de7c6b773b1ec5cb3b8f3659bbff087b8ca264952c4d013083206c9488bf` |
| Revenue 1997 convention | 49 | `58bcb6fd6caf1d15e3b1ab00feee46620d36665bc33d4a37cca458bb3cce00ae` |

All six PDFs extracted natively through pdf-inspector without OCR. Revenue
numbers the branch-excess-interest rule as art 11(6), while the IRS PDF
prints a second paragraph 4; the explanation discusses paragraph 6.
Revenue's art 13(1) refers to art 6, while the IRS text says art 4. The guide
uses Revenue's relevant operative numbering and cross-reference. This is a
focused comparison, not a complete authentic-text or later-instrument audit.

The [Irish Treaty Series][force] records the amendment's entry on
13 July 2000. Amendment art 2(2) applies it to dividends from the first day
of the second month following entry, giving 1 September 2000. The
[Revenue dates table][dates] records the same application date. The
[Senate report's explanation][report] confirms the three amended REIT
alternatives but supplies no numerical diversification measurement in the
checked passage. Its historical statutory rate is not a current tax result.

| Correction | Primary evidence |
| --- | --- |
| US resident payer's ordinary 15% and qualifying corporate 5% ceilings | Arts 10(1)-(2), 10(6), 23 and 24(6) |
| Direct voting ownership; conditional proportionate transparent holdings | Treasury explanation of art 10(2); Protocol paragraph 1 |
| RIC/REIT 5% exclusion; three independent conditional REIT 15% routes | 1999 amendment art I, replacing art 10(4) |
| Defined/source-tested interest; attribution and arm's-length limits; branch excess | Art 11(1)-(6) |
| Specified profit-determined interest up to 15%; REMIC domestic-law reservation | Protocol paragraph 6 |
| Defined royalties, including specified audiovisual copyrights and contingent alienation; attribution, excess and routing | Art 12(1)-(5) |
| Separate enterprise PE and individual fixed-base rules; deferred attribution | Arts 5, 7 and 14; Protocol paragraphs 4 and 7 |
| Third-state PE restriction, Irish exemption prerequisite, tax comparison and active-business exception | Art 23(7) |
| Remittance-limited relief for an individual taxed on that basis | Art 24(6) |
| Offshore exploration/exploitation and independent-service distinctions | Art 21(1)-(5) |
| Other dividend payers and separate branch-tax base/ceiling | Arts 22 and 10(7)-(8) |

I checked these boundaries manually against the primary text. They are
conditional rule comparisons, not taxpayer calculations or a new test suite.

| Boundary | Result under the cited provision |
| --- | --- |
| Ordinary company owns 9.99% versus 10% voting stock | The 5% route requires at least 10%; general entitlement and fund/attribution limits still apply |
| Corporate-tier indirect or direct non-voting holdings | Excluded from the explanation's 5% test; transparent holdings require proportionate ownership and agreement analysis |
| Individual owns 10% versus more than 10% of a REIT | The amended individual alternative includes 10%; exceeding it fails only that alternative |
| Publicly traded class; person owns 5% versus more than 5% of any class | The public-class alternative includes 5%; the other alternatives remain separate |
| Person owns no more than 10%, diversification unestablished | The treaty supplies a conditional route; eligibility remains unresolved |
| No REIT alternative established | No art 10(2) ceiling; this review selects no domestic rate |
| Third-state PE profits not exempt in Ireland | Art 23(7)'s exemption prerequisite fails |
| Combined tax equals 50% versus 49.99% of the comparator | Exactly 50% fails the less-than test; 49.99% satisfies that element only |
| Connected active PE business versus investment management | The exception excludes making/managing investments unless qualifying banking or insurance |
| Construction exactly 12 months versus more than 12 | Only the latter satisfies art 5(3); other PE grounds remain separate |
| Enterprise offshore exploration 120 versus 121 aggregate days | The art 21(3) exception includes 120, not 121, in any twelve months |
| Associated similar exploration: 80 plus 40 versus 80 plus 41 non-concurrent days | Aggregates are 120 and 121; concurrent days are not counted twice |
| Offshore exploitation for one day | No exploration 120-day exception; enterprise PE or independent fixed-base rule applies |
| Individual offshore exploration exactly 120 days | Fixed base is deemed, but exploration income is exempt under art 21(4); enterprise aggregation is not automatically imported |
| Deferred receipt after cessation | Protocol paragraph 4 preserves taxation where income was attributable during the PE/fixed base's existence |
| Remittance-basis individual receives/remits 40 of 100 | Art 24(6) limits relief to 40, assuming its conditions; remaining domestic treatment is unresolved |
| Non-US payer with debt incurred in connection with and borne by US PE/fixed base | Art 11(4) can still deem the interest US-arising |

The 2006 agreement denies CCF treaty residence and benefits in its own
right. It gives Irish resident unit holders benefits subject to art 23.
Current vehicle qualification and later CCF guidance were not verified.
The diversification measurement, current domestic classification/rates,
branch calculations, withholding/forms/refunds, claimant entitlement,
reciprocal Irish taxation, complete later-agreement inventory, professional
sign-off, taxpayer end-to-end use and other corridors remain unreviewed.
Repository checks and publication readiness are recorded in the accompanying
pull request; those checks do not establish financial accuracy.

[convention]: https://www.revenue.ie/en/tax-professionals/documents/double-taxation-treaties/u/usa-1997.pdf
[irs-convention]: https://www.irs.gov/pub/irs-trty/ireland.pdf
[explanation]: https://www.irs.gov/pub/irs-trty/iretech.pdf
[amendment]: https://www.revenue.ie/en/tax-professionals/documents/double-taxation-treaties/u/usa-protocol.pdf
[irs-amendment]: https://www.irs.gov/pub/irs-trty/amending_convention_ireland_treaty_24_sept_1999.pdf
[ccf]: https://www.revenue.ie/en/tax-professionals/documents/double-taxation-treaties/u/usa.pdf
[index]: https://www.irs.gov/businesses/international-businesses/ireland-tax-treaty-documents
[revenue-index]: https://www.revenue.ie/en/tax-professionals/tax-agreements/double-taxation-treaties/U/usa.aspx
[force]: https://www.gov.ie/en/irish-treaty-series/treaty-series/irish-treaty-series-no-24-of-2000/
[dates]: https://www.revenue.ie/en/tax-professionals/tax-agreements/dates-of-effect/index.aspx
[report]: https://www.govinfo.gov/content/pkg/CRPT-106erpt11/html/CRPT-106erpt11.htm
