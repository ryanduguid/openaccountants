# US treaties: Switzerland rules

The Switzerland section described headline zero rates for interest and
royalties as complete exemptions and gave services a zero rate with only
a no-PE note. It did not distinguish payment definitions, conditional
exceptions or enterprise and individual service rules. It omitted the amended pension
exemption and fund restrictions, and included Swiss refund procedures in
a US-source section.
This correction started from clean main `5c54f264` and incorporates the
Singapore merge `627f400d`. It advances `us-major-partners` from version
1.8 to 1.9 and records conditional Swiss treaty treatment for tax year 2025.
The guide remains tier 2 with `pending_review` status.

I compared the [1996 convention][convention] and [Treasury explanation][explanation],
the [2009 protocol][original-protocol], [corrected protocol and English
notes][corrected], [2009 explanation][protocol-explanation], [2020
arrangement][usmca] and [2024 pension arrangement][pension]. The [IRS
treaty index][index] and arrangement index were inspected on 6 October 2026.
The later pension arrangement supersedes the May 2021 arrangement and
preserves all additional treaty requirements. The original convention
already exempted qualifying pension dividends; the amendment expanded its
scope to individual retirement savings plans.

| Document | Pages | SHA-256 |
| --- | --- | --- |
| convention | 45 | `0893b73e0aa8671480441779b4f0887b53eac950cfad7c39038b66159e24fcf6` |
| explanation | 99 | `1f28a9a398b5b31ebcd1c20a2bc2995bfb0eddc15617203956f21c5fbbbe81d6` |
| protocol-corrected | 28 | `325c6ea090454a3fda77b57ed2dea6afa469b2665ee6766b69f8d904caccd5fc` |
| protocol-explanation | 12 | `35e8f27739c130aaf5a3d26eb8f893a2d9d051a068076a5d9dc70edf5ab94681` |
| protocol-original | 5 | `602ec9e4e69c867eeaf9a6d2ba1658210fe82d098b279cd0e8a22220a751dabe` |
| nafta-2020 | 1 | `51d4e89fb675a0cb9dd609a4b77e633baccdddd1d13a560f82eaa60cdd9aea7a` |
| pension-2024 | 4 | `f1cf60e8dbd71ca42ea1f6ede83fb1669206723ddef42433198e5b069a5396d0` |

Six PDFs extracted natively with pdf-inspector. The corrected Senate
document needed offline OCR on PDF pages 9 to 28; the managed Linux job
completed success/exited/0. The scanned pension provision was compared
with native Treasury protocol text and the 2024 arrangement. No OCR page
carried a hosted-review recommendation, which does not prove exact
transcription. Page images and German notes were not independently verified.
The 1996 explanation has apparent paragraph/article cross-reference slips;
the convention supplies art 11(6) for the interest exception, art 14 for
independent services and art 15 for dependent services.

[Treasury's announcement][force] records protocol entry on
20 September 2019. Corrected Protocol art 5(2)(a), including the November
2010 English correction from 'the first January' to 'the first of January',
applies withholding provisions from 1 January 2020. The 2024 arrangement
expressly operates for dividends paid from 1 January 2020. This focused
instrument check is not a complete authentic-language comparison.

| Correction | Primary evidence |
| --- | --- |
| Ordinary 15% ceiling and qualifying direct corporate 5% ceiling | Convention art 10(1)-(2); 1996 explanation of art 10(2) |
| RIC 5% exclusion and REIT individual holding strictly below 10% | Convention art 10(2); paragraph 3 pension treatment is separate |
| Conditional pension/individual-plan exemption, specific LOB test and current arrangement | Protocol art 1; 2009 explanation of art 1; convention art 22(2); 2024 arrangement paras 1 and 4 to 6, 8 |
| Defined interest, attribution, arm's-length limit, specified contingent interest and REMIC reservation | Convention art 11(1)-(6) |
| Defined royalties, audiovisual exclusion, contingent disposal, attribution and excess | Convention arts 7(8), 12 and 13(4) |
| Enterprise PE versus individual fixed-base/services-location rules | Convention arts 5, 7 and 14 |
| Residence, saving clause, LOB, third-jurisdiction restriction and USMCA interpretation | Convention arts 1, 4 and 22; 2020 arrangement |
| Deferred PE/fixed-base attribution, other dividend payers and separate branch-tax base/ceiling | Convention arts 28(3), 10(6)-(8), 13(1) and (3); 1996 explanation of arts 10, 11, 12 and 14 |

I checked the following distinctions against the cited text. These are
conditional rule comparisons, not taxpayer calculations or withholding
instructions.

| Boundary | Result under the cited provision |
| --- | --- |
| Qualifying company holds 9.99% versus 10% voting stock | Only 10% satisfies the at-least-10% element; direct holding, entitlement and category conditions remain |
| Corporate-tier or non-voting holding | Does not satisfy the explanation's direct voting test; transparent holdings require proportionate ownership and agreement analysis |
| Individual holds 9.99% versus 10% in a REIT | Only 9.99% satisfies the paragraph 2 less-than-10% element; paragraph 3 pension treatment remains separate |
| Pension or plan controls the payer | The amended paragraph 3 exemption does not apply |
| Article 22(2) entitled beneficiaries, members or participants are exactly half versus more than half | Only more than half satisfies the stated numerical element, if there are any; the 2009 explanation requires this test for art 10(3), with particular individual-plan characterisation left for review |
| Unlisted retirement plan | The arrangement's list is nonexclusive; correspondence can require competent-authority verification |
| Qualifying pension receives a RIC/REIT dividend | Paragraph 2 restrictions alone do not deny paragraph 3 relief; dividend character and all additional requirements remain |
| Pension dividend attributable to a PE or fixed base | Interaction of art 10(3) and (5) remains unresolved in the retained later instruments |
| Profit-linked interest meets portfolio-interest qualification | That qualification defeats the specified art 11(6)(a) exception only; other tests remain |
| REMIC excess inclusion | US domestic-law taxation is preserved; no current domestic rate is selected |
| Combined third-jurisdiction/residence tax is 60% versus 59.99% of the comparator | Only 59.99% satisfies the below-60% element of art 22(4); the stated exceptions need separate analysis |
| Construction lasts exactly 12 months versus longer | Only the latter satisfies art 5(3); other PE grounds remain separate |
| Natural-resource extraction place | Art 5(2) separately lists mines, wells, quarries and extraction places; the project threshold is not a general exemption |
| Individual has a regularly available US fixed base but services are performed elsewhere | Art 14 also requires income attributable to services performed in the US for that source-state taxation |
| Motion-picture or broadcasting reproduction payment | Excluded from art 12 and included in art 7(8) business profits; other conditions remain |
| Additional US branch tax | The 5% ceiling applies to the defined dividend-equivalent amount, not all branch receipts or ordinary PE tax |

Current domestic rates, branch calculations, forms and withholding/refunds,
claimant facts, particular-plan characterisation/correspondence/control, mixed-payment
classification, reciprocal Swiss-source use, professional sign-off,
taxpayer end-to-end use and whole-corpus accuracy remain unverified.
Repository checks and remaining delivery gates are recorded in the
accompanying PR; they do not establish financial accuracy.

[convention]: https://www.irs.gov/pub/irs-trty/swiss.pdf
[explanation]: https://www.irs.gov/pub/irs-trty/swistech.pdf
[original-protocol]: https://home.treasury.gov/system/files/136/archive-documents/US-SwissProtocol.pdf
[corrected]: https://www.congress.gov/112/cdoc/tdoc1/CDOC-112tdoc1.pdf
[protocol-explanation]: https://home.treasury.gov/system/files/131/Treaty-Switzerland-Protocol-TE-9-23-2009.pdf
[pension]: https://www.irs.gov/pub/irs-lbi/switzerland-caa-pension-plans-tax-treaty-benefits-2024.pdf
[usmca]: https://www.irs.gov/pub/irs-lbi/switzerland_competent_authority_arrangement.pdf
[index]: https://www.irs.gov/businesses/international-businesses/switzerland-tax-treaty-documents
[force]: https://home.treasury.gov/news/press-releases/sm781
