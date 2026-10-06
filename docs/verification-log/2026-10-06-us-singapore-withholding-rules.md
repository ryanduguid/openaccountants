# US payments to Singapore: withholding defaults

The Singapore section called 30% the default, but its interest row did not
name domestic exemptions and its source and withholding notes lacked primary
links. This change keeps the ordinary 30% chapter 3 defaults and adds their
payment, source and recipient boundaries for tax year 2025. It starts from
main `5c54f264`, advances `us-major-partners` to version 1.8 and retains
tier 2 with `pending_review` status.

I compared selected paragraphs in [IRS Pub. 515 (2025)][p515] and
[Pub. 519 (2025)][p519], the [personal-service source page][services] and
the operative July 1988 [limited transport agreement][transport]. The
[IRS comprehensive treaty index][irs-index] and [IRAS registry][iras-index]
were read on 6 October 2026. Singapore is absent from the IRS list; IRAS's
two US entries are an in-force EOI Arrangement and Limited DTA. This is an
observed classification, not a complete historical or later-instrument
inventory.

| Document | Pages | SHA-256 |
| --- | --- | --- |
| Pub. 515 (2025) | 87 | `6a892182fed47dbe5b5404002b305e49d6e34438e618c398d330200fda9ed3c3` |
| Pub. 519 (2025) | 95 | `c220ed64473d9f26b09784e45d5c4e05b052caace1263278bb6dc2060796ed85` |
| IRAS limited agreement, including historical annexes | 12 | `e2ac01a1659ec5747902afb7c28dab19899796a7c786799e5a27872f2eb4afd0` |

All three PDFs returned HTTP 200 and produced native text without pages
flagged for OCR. Pub. 515's cover says 5 February 2025; its internal file
timestamp says 6 February 2025. Pub. 519 is for 2025 returns and is dated
19 February 2026. Pub. 519 corroborates individual-interest treatment; it
does not supply foreign-corporation rules. No independent page-image
comparison was performed.

The direct official US Code 2025 view returned an UnderMaintenance page
and supplied no statutory text. Current 2026 search previews were not
used as 2025 authority. The statements below are bounded comparisons with
official IRS guidance and the agreement, not a complete verification of
controlling 2025 statutes, regulations or later legislation.

| Change | Primary passage and boundary |
| --- | --- |
| Keep 30% as selected chapter 3 defaults | Pub. 515, Amounts Subject to Chapter 3 Withholding and Income Not Effectively Connected: ordinary US-source FDAP to foreign persons, outside ECI, subject to applicable exceptions. Singapore residence alone does not decide the recipient's status. |
| Restrict the dividend row | Pub. 515, Dividends paid by US corporations: distinguish ordinary cash dividends from fund, real-property, return-of-capital, exchange/redemption and foreign-corporation cases. The row does not classify those distributions. |
| Name deposit and portfolio-interest exceptions | Pub. 515, Interest on deposits and Portfolio interest; Pub. 519, Interest Income. Specified deposit interest not connected with a US trade or business and qualifying portfolio interest can avoid chapter 3 withholding. Instrument, owner and documentation conditions remain for separate analysis. |
| Separate chapter 4 and reporting | Pub. 515, Portfolio interest and Interest on deposits: a chapter 3 exception can leave chapter 4 or reporting questions. Royalties are nonfinancial payments excluded from chapter 4 withholdable payments; chapter 3 and reporting remain separate. |
| Narrow the service-source note | IRS personal-service source page and Pub. 515, Chart B: actual performance place generally sources personal-service compensation; mixed-location pay needs allocation. Patent/copyright royalties generally follow property use, and vessel/aircraft services have special rules. An invoice label does not decide character. |
| Describe limited transport scope | July 1988 notes, MFA 560/88 and No. 297/88: conditional international ship/aircraft income, including specified rentals, incidental containers, pools and disposals. The notes contain status and corporate conditions. No current eligibility result is selected. |

The July notes amend the March 1988 agreement and state application to
taxable years beginning from 1 January 1987. The March notes in Annex A
and 1985 agreement in Annex B were read as historical predecessors.
Current statutory/regulatory implementation and taxpayer qualification
were not established from those historical texts.

These manual comparisons guide the source edit; they are not taxpayer
calculations or new executable exemption tests:

| Comparison | Expected reading |
| --- | --- |
| Ordinary US domestic-corporation cash dividend versus a fund or return-of-capital distribution | The ordinary case reaches the stated default only within its scope; the special case stops for separate classification. |
| Ordinary US-source non-ECI interest versus specified deposit or potential portfolio interest | The former retains the default absent an exception; the latter routes to the cited qualification rules. |
| Modern registered debt versus historical bearer or foreign-targeted debt | Documentation where required; no statement that documentation is invariably required or that a supplied form establishes eligibility. |
| Deposit or portfolio chapter 3 exception versus reporting/chapter 4 | A chapter 3 outcome does not determine the separate consequences. |
| Singapore-only personal services versus mixed-location work or US-use licence royalties | The service-source statement follows actual work and character; mixed work needs allocation and licence payments need royalty analysis. |
| Specified international ship rental versus a generic transport payment | Agreement categories and conditions require analysis; no automatic resident or company exemption. |

The required financial plan recommended a concise clarification and source
routing. I accepted that recommendation against the passages above. The
fuller portfolio checklist was omitted because the packet does not establish
a complete statutory, regulatory or documentation entitlement test. The
original note's use of default is recorded; 30% itself was not demonstrated
to be a wrong ordinary rate. The cover/build date distinction was checked
against the native IRS extract.

Repository validation and tests check structure, generation and software
behaviour. Independent financial review follows those checks and does not
replace a qualified accountant's sign-off. Professional review, claimant
and instrument facts, complete 2025 legislative and later-instrument
inventories, current law/forms/reporting procedures, transport implementing
rules and eligibility, reciprocal Singapore taxation, authentic-language
comparison, taxpayer end-to-end use and whole-corpus financial/network
accuracy remain unverified.

[p515]: https://www.irs.gov/pub/irs-prior/p515--2025.pdf
[p519]: https://www.irs.gov/pub/irs-prior/p519--2025.pdf
[services]: https://www.irs.gov/individuals/international-taxpayers/source-of-income-personal-service-income
[transport]: https://www.iras.gov.sg/media/docs/default-source/dtas/singaporeusalimiteddta.pdf?sfvrsn=f20a8c9f_7
[irs-index]: https://www.irs.gov/businesses/international-businesses/united-states-income-tax-treaties-a-to-z
[iras-index]: https://www.iras.gov.sg/taxes/international-tax/international-tax-agreements-concluded-by-singapore/list-of-dtas-limited-dtas-and-eoi-arrangements?indexCategories=all&pg=11
