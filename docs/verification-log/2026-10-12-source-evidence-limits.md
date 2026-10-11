# Source evidence: PDF omissions and document identity

The Caribbean Netherlands and Niue source checks found text omissions and a
misdirected official download link. These checks were performed on 12 October
2026 in Australia/Sydney, using captures from 11 October UTC. They establish
the limits below; they do not establish complete current law or a taxpayer's
liability.

## Native PDF extraction omitted a footnote

The Caribbean Netherlands' [2026 payroll calculation rules](https://english.belastingdienst-cn.nl/site/binaries/site-content/collections/documents/belastingdienst/lh/tabellen-en-rekenregels-2026/calculation-rules-2026/rekenregels-tabellen-lb-en-premies-2026.pdf)
contain an italic footnote on physical page 1 about the end amounts used in
the table. It is absent from both retained native text and native Markdown
outputs from pdf-inspector 1.25.2. The page image confirms its presence.
The document was classified as text based, with no page flagged for OCR.
Those results therefore did not establish complete content.

Both raw extraction variants and the reviewed page image were preserved.
No payroll calculation was derived from the omitted passage in this check.

Source PDF SHA-256:
`297492f8081b6d953cac39884ee68604ae3fdc422907577cd590dbcde146a0a9`.

## OCR omitted a statutory list

Niue's [Tax Administration Act 2025, No 379](https://www.gov.nu/media/pages/information/b29c7ba832-1784584144/act-379-tax-adminstration-act-2025.pdf)
is a 93-page scanned PDF. Native extraction returned no text. Selected pages
were processed with pdf-inspector's offline PP-OCRv6 Small route at 200 DPI.
On physical page 92, the OCR output retained the Schedule 3 heading and
introductory sentence but omitted all four listed Acts.

Review of that page image identified the list: this Act, the Income Tax Act
1961, the Niue Consumption Tax Act 2009 and the Departure Tax Act 1996.
The omission was recorded separately without altering the raw OCR output.
The full Act, later amendments and other applicable instruments were not
reviewed.

Source PDF SHA-256:
`2c9878effed5bc5996bdeeb4d0fdfd7fe9868d8f7123524eb909dbcee6edf3ae`.

## An official link supplied a different Act

The captured [Government of Niue legislation index](https://www.gov.nu/information)
labels a download as the Niue Consumption Tax Amendment Act 2025, No 381.
Its target duplicates the preceding Income Tax Amendment Act 2025, No 380
download. The retrieved PDF identifies itself as No 380. The captured visible
index text and download links preserve that mismatch.

No content for No 381 was inferred from the linked PDF. Its text, the complete
later amendment chain and current subsidiary rules remain unverified.
