# Country source readiness: Cook Islands, Niue and Caribbean Netherlands

These source checks record progress towards comprehensive country packs and
identify evidence still needed. They were performed on 12 October 2026 in
Australia/Sydney, using captures from 11 October UTC. They establish document
identity and the selected observations below. Current-law completeness,
professional sign-off and taxpayer calculations remain unverified.

## Cook Islands: signed contribution Orders

The official archive supplied the signed, two-page *Cook Islands National
Superannuation Fund (Contribution Rate) Order 2021* (No 9) and its two-page
*Contribution Rate Amendment Order 2021* (No 11). The [No 9 archive record](https://cookislandslaws.gov.ck/api/show_pdf_lawsaspublished/680)
and [No 11 archive record](https://cookislandslaws.gov.ck/api/show_pdf_lawsaspublished/661)
return JSON containing the PDF bytes. The decoded bytes matched the retained
PDFs. Both pages of each PDF were processed with offline Small OCR and compared
with their source images. Raw extraction was preserved.

The signed No 9 recital cites section 39(3) of the principal Act. The captured
[consolidated Order](https://cookislandslaws.gov.ck/#/InternalConsolidatedLaws?legalId=LOCI.NSA)
instead prints references to sections 1(3) and 36(1). The signed text was made
on 7 September 2021; clause 2 commences it the following day. No 11 was made
on 7 December 2021, also commencing the following day. Its clause 4 replaces
only clause 4(b) of No 9 with the close of 28 February 2022. The earlier
revocation condition in clause 4(a) is not replaced. These are historical
instrument observations and do not establish a contribution rate for 2026.

Source PDF SHA-256 hashes:

- No 9: `4b2fe004f7d593ee661971def0ffe12627a30a23f054af05331849663adec1d4`.
- No 11: `7687597e340448a75b43b11f6a04b232d18236fae9f6ba22259098ff20a9355b`.

The separate actual 2021 COVID contribution-extension Order, later variations
or repeals and the complete current contribution-law chain remain unresolved.
The official consolidated Employment Relations Schedule 2 was retrieved, but
the original Act's archive endpoint returned HTTP 500. Consolidated material
and the archive's status labels do not establish the complete operative chain.

## Niue: the full consumption-tax amendment is missing

The current [government legislation index](https://www.gov.nu/information)
still labels a link as the Niue Consumption Tax Amendment Act 2025, No 381,
while directing it to the Act 380 income-tax amendment PDF. The current index
card was captured; the known wrong PDF was not downloaded again. See the
[document-identity check](2026-10-12-source-evidence-limits.md) for the earlier
retrieved-file comparison.

Four 2026 Gazette publications were retrieved:

| Issue | Publication date | Pages | Source |
|---|---|---|---|
| 01 | 31 March 2026 | 4 | [Official PDF](https://www.gov.nu/media/pages/gazette/5ecafc8089-1778704675/ngg-01-2026-land-court-14-april-issued-31-march.pdf) |
| 02 | 23 June 2026 | 6 | [Official PDF](https://www.gov.nu/media/pages/gazette/806e7bda9f-1782432383/ngg-issue-02-2026-23-june-2026.pdf) |
| 03 | 7 July 2026 | 10 | [Official PDF](https://www.gov.nu/media/pages/gazette/5b3f599c53-1783548094/ngg-issue-03-2026-7-july-2026.pdf) |
| 04 | 3 September 2026 | 4 | [Official PDF](https://www.gov.nu/media/pages/gazette/24328f15ec-1788836399/ngg-issue-04-2026-3.9.26-land-court-22-sept-2026.pdf) |

Native extraction covered all 24 pages, and first-page header images were
compared. They contain court schedules or assessor notices; the retained native
text has no match for 381, consumption or tax. Detailed tables, footnotes and
remaining page images were not visually checked. This bounded search does not
establish legal absence or supply the full Act 381 amendment provisions.

The full Act 381, intervening amendments and applicable subsidiary instruments
remain required before a current consumption-tax guide can be verified.

## Caribbean Netherlands: employer-premium rounding remains open

The [2026 calculation rules](https://english.belastingdienst-cn.nl/site/binaries/site-content/collections/documents/belastingdienst/lh/tabellen-en-rekenregels-2026/calculation-rules-2026/rekenregels-tabellen-lb-en-premies-2026.pdf)
and selected employer sections of the
[2026 payroll handbook](https://www.belastingdienst-cn.nl/site/binaries/site-content/collections/documents/belastingdienst/lh/2026/handboek-loonheffingen-2026/bes-handboek-loonheffingen-2026.pdf)
were checked in native text, selected OCR and full page images. The employee
withholding rounding sentence precedes a separate employer-premium heading.
It does not establish employer-premium precision. The reviewed employer
sections and wage-statement columns do not resolve that rule.

Selected declaration provisions in the
[Uitvoeringsregeling Belastingwet BES](https://wetten.overheid.nl/BWBR0029332/2025-01-01)
and the [4 February 2026 handbook announcement](https://www.belastingdienst-cn.nl/actueel/nieuws/2026/februari/04/handboek-loonheffingen-2026)
also did not resolve employer-premium cent rounding or explain the retained
payroll-source discrepancies. The declaration instructions, full delegated
instrument chain and discrepancy resolution remain open. Unmatched native
text does not prove that no rule or correction exists elsewhere.

## Verification boundary

Source bytes, raw extraction, image-review scope, retrieval receipts and hashes
were retained. A source inventory or historical amendment does not complete a
country pack. No tax-guide tier, accountant-review claim or country-presence
count is advanced by this record.
