# US treaties: South Korea rules

The South Korea section cited arts 10, 11, 12 and 7 for dividends,
interest, royalties and services, while the convention uses arts 12, 13,
14 and 8. Its corporate dividend row omitted the holding-period and
payer-income tests. A blanket services zero rate omitted the separate
individual rules, and the construction row omitted the strict threshold
and other PE grounds. This correction starts from main `0152342cd832340b5fc4611276c117e866ed9417`
and advances `us-major-partners` from version 1.9 to 1.10. Its primary
figures remain for 2025; the guide remains tier 2 and `pending_review`.

I compared the [1976 convention][convention], including its related
notes, with the relevant [Treasury explanation][explanation], and read
the complete [2017 Article 3 arrangement][residency]. The [IRS treaty
index][index] and [arrangement index][arrangements] were inspected on
6 October 2026. The arrangement was signed on 7 March 2017 by Korea
and 10 April 2017 by the United States. The convention's cover and
proclamation record entry into force on 20 October 1979; art 31 applies
withholding provisions to payments from 1 January 1980. The explanation
corroborates the selected income and PE conditions; the convention
supplies the employment-condition wording.

| Document | Pages | SHA-256 |
| --- | --- | --- |
| Convention | 29 | `01557a1fa7058668e44c27ec945abd08e33bd75b08a779135ee07adf6b9aebb3` |
| Treasury explanation | 27 | `aecc34939e10c58358d9cc9e5240d500f493a5e9b480bd8a85205d530f79daef` |
| Residency arrangement | 2 | `4a8862dd150f3b2155b680e0232863995af1cf5880337d8898af0e8aa9af49eb` |

All three PDFs extracted natively with pdf-inspector 1.25.2, without OCR
flags or encoding warnings. Relevant complete convention and explanation
pages and the full arrangement were read, with PDF page markers retained.
Absence of extraction warnings does not establish exact transcription or
forensic authenticity. No authentic Korean text or page images were
independently compared.

| Correction | Primary evidence |
| --- | --- |
| Ordinary 15% and conditional corporate 10% gross dividend ceilings, with ownership periods and payer-income exclusions | Convention art 12(2)–(3), PDF page 17; explanation pages 14 to 15 |
| Defined 12% gross interest ceiling, specified governmental exemption, attribution and related-person excess | Convention art 13, pages 17 to 18; explanation pages 15 to 16 |
| Exact 10% copyright/reproduction/audiovisual category and 15% other defined royalty ceiling; know-how, specified rentals, contingent disposals, natural-resource exclusion and excess | Convention art 14, pages 18 to 19; explanation pages 16 to 17 |
| Payer, place-of-use, rental, services-performance and PE source rules | Convention art 6, pages 11 to 12; explanation pages 7 to 8 |
| Enterprise versus individual independent/employed services | Convention arts 8, 18 and 19, pages 13 to 14 and 20 to 21; explanation pages 10 to 11 and 18 to 19 |
| More-than-six-month project ground and separate fixed-place, contracting/stock agency and processing/purchase grounds | Convention art 9, pages 14 to 16; explanation pages 11 to 13 |
| Residence, saving clause and conjunctive holding-company restriction | Convention arts 3, 4 and 17; explanation of these articles |
| Sequential individual tie-breakers and dwelling with family in a permanent home in both states | Complete 2017 arrangement |

I compared these boundaries against the cited text. They identify treaty
elements and do not calculate a taxpayer's liability or withholding.

| Boundary | Result under the cited provision |
| --- | --- |
| Individual versus corporate dividend recipient | Only the corporation can use art 12(2)(b); every other condition remains |
| Voting holding of 9.99% versus 10% | Only 10% satisfies the at-least-10% element; a payment-date holding alone does not meet the period test |
| Relevant prior-year interest/dividend gross income of 25% versus more than 25% | Only 25% meets the not-more-than-25% element, after specified exclusions |
| Subsidiary voting holding of 49.99% versus 50% when interest/dividends are received | Only 50% meets that income-exclusion ownership element |
| No prior taxable year | Preserve 'if any'; do not invent a prior-year period or income denominator |
| Partly owned versus wholly owned governmental instrumentality | Only wholly owned meets that ownership element; beneficial derivation and tax-status conditions remain |
| Related-person excess interest/royalty | The respective article applies only to the amount payable to an unrelated person; other applicable provisions can affect excess |
| Independent individual present for 182 versus 183 days in the taxable year | Only 183 triggers that art 18 presence ground; income and fixed-base grounds remain separate |
| Independent-services income of exactly US$3,000 versus more | Only more triggers the art 18 income ground; other grounds remain |
| Fixed base maintained for 183 days | Art 18's fixed-base ground includes attribution; that limit does not restrict the separate presence or income grounds |
| Ordinary employee present exactly 183 days | Fails the art 19(2) less-than-183-day condition, subject to any separate applicable provision |
| Project exists exactly six months versus longer | Only longer meets art 9(2)(h); agency, fixed-place and paragraph 5 grounds can apply independently |
| Only one art 17 condition holds | The conjunctive denial is not established |
| Individual dwells with family in an otherwise qualifying permanent home in each state | The 2017 arrangement establishes homes in both; unresolved residence proceeds to the next sequential test |

The source and generated package retain the full conditional section.
MCP full-guide and section reads can preserve its context, while keyword
search excerpts can truncate conditions. The section requires fetching
its full text before application. Repository checks and runtime evidence
are recorded in the accompanying PR; they do not certify taxpayer outcomes.

Current domestic source/classification/tax rules, withholding/forms/refunds,
claimant eligibility, art 17 corporate facts, scientific-copyright or
mixed-payment classification, reciprocal Korean-source use, complete
later-instrument and authentic-language comparisons, professional sign-off,
taxpayer end-to-end use and whole-corpus accuracy remain unverified. No
social-security conclusion is made from these selected income provisions.

[convention]: https://www.irs.gov/pub/irs-trty/korea.pdf
[explanation]: https://www.irs.gov/pub/irs-trty/koreatech.pdf
[residency]: https://www.irs.gov/pub/irs-lbi/us-korea-competent-authority-residency-arrangement.pdf
[index]: https://www.irs.gov/businesses/international-businesses/korea-tax-treaty-documents
[arrangements]: https://www.irs.gov/individuals/international-taxpayers/competent-authority-arrangements
