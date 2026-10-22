# Palau: corporation regulations and commencement sources

The captured corporation regulations record distinct adoption, approval and
effective dates. They leave the revised Act's commencement chain unresolved. I
checked the retained sources on 15 October 2026 in Australia/Sydney; the captures
were made on 14 October UTC.

## Regulation dates require the signing pages

The Financial Institutions Commission publishes
[Corporation Regulation CR-01](https://ropfic.org/wp-content/uploads/2026/02/Corporations_Regulation_CR_01_Effective_January_19_2025-crossout.pdf)
and [Corporation Regulation CR-02](https://ropfic.org/wp-content/uploads/2026/02/Corporation_Regulation_CR_02-_Other_Business_Association_Effective_April_26_2025-Crossout.pdf).
The captured copies have 16 and 12 physical pages respectively, including their
fee schedules. Their signing pages record:

| Document and physical pages | Adoption | Presidential approval | Explicit effective date |
|---|---|---|---|
| CR-01, pages 10 and 11 | 20 December 2024 | 9 January 2025 | 19 January 2025 |
| CR-02, pages 7 and 8 | 27 March 2025 | 3 April 2025 | 26 April 2025 |

These are literal observations of labelled fields. CR-01's approval day and month,
and CR-02's adoption and effective-date fields, required image review after text
extraction omitted them. The last physical page of CR-02 is schedule page 4, not
the approval page.

CR-01 has native text except on physical pages 10 and 11. Its aggregate native
text matches the earlier captured copy despite different PDF bytes. CR-02 has no
usable native text; all 12 pages were processed with offline Small OCR and read.
Different PDF hashes and matching extracted text do not establish identical
graphics, strikeouts or fee-table alignment. No schedule amount was qualified by
this check.

## The revised Act uses a promulgation trigger

The [original RPPL 11-40](https://palauregistries.pw/Documentation/PW/RPPL%2011-40.pdf)
has 71 scanned pages. Complete OCR was retained, but reading covered selected
formation, reporting and closing provisions. Physical page 71 records passage on
24 December 2024 and approval on 26 December 2024. The first-page heading says
November 2023; that discrepancy remains recorded.

On physical page 65, section 4 repeals RPPL 11-10 section 4. Section 5 requires
regulations within three months after the Act's effective date and connects their
promulgation to the RPPL 11-10 section 3 repealer and transition provision. The
clause also describes failure to comply. It does not state that the revised regime
automatically commences when the three-month period ends.

The enacted original of RPPL 11-10, its signed approval fields, the complete
amendment chain and evidence of qualifying promulgation remain unverified. The
regulation date fields alone do not settle those questions or current legal force.

## Verification boundary

The captured SHA-256 values are:

- CR-01: `96abf52633e5d60c64e646699f6afcbb93ff13fc74f5e77f54ceb85a0e0e9045`.
- CR-02: `811017e53f7e1dcafe5ace47f660738b4047aebfa12bb0457fd64fe67b0d8068`.
- RPPL 11-40: `505fc3cabd4d21b4edc245912be95ad6489d3e1a0d615dedbb83158c096a57c5`.

The two new regulatory OCR jobs completed successfully using the default offline
Small route at 200 DPI, with no reported rotation or review warning. Original and
OCR hashes matched the retained transfer and terminal-job records. Poppler rendered
selected pages because pdf-inspector cannot render standalone page images.

This entry records source evidence; no filing calendar, fee calculation or current
tax treatment was selected. Professional sign-off and comprehensive Palau coverage
remain unfinished. The [earlier investment and reporting limits](2026-10-13-palau-investment-source-boundaries.md)
also remain relevant.
