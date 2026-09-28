# 12 September 2026: Andorra form 900 and correction of the earlier IGI correction

> Entry of 2026-09-12 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

The government IGI portal links form 900. Web retrieval of the government's
three-page PDF exposes its complete numbered text. The missing domestic 0%
output pair is **9 (base) and 10 (tax)**; domestic 0% input is 37/38. The form
uses numerical fields 1–64. The guides' old A/B/C map, including B5/B6 for fixed
assets and C1/C2/C5 for settlement, did not describe this published form.

Source: [government form 900](https://www.govern.ad/documents/1898932/2636954/9002016.pdf/859a97d4-bf7c-9920-a4a4-40c965232ec2?download=true&t=1743750068213&version=2.0),
also published at [the canonical document path](https://www.govern.ad/documents/d/guest/9002016?download=true).
The local government host returned a DNS failure. No local PDF bytes, hash,
PyMuPDF extraction or rendered page reading were obtained for this form. Web
PDF text was available; attempted web screenshots did not return viewable image
content. The mapping is supported by that text, with visual confirmation and
comparison to the authenticated electronic return still outstanding. The older
printed legal references are not proof that the form reflects every later law
amendment. No access control or TLS setting was bypassed.

All numbered fields were compared with both editable IGI guides. Output 1–20,
import deduction 21–28, domestic deduction 29–44 and settlement 45–64 are now
mapped. The ordinary balance is box 20 minus boxes 28 and 44; prior credit is 46.
Reverse charge uses 11/12 and, if deductible, 39/40. Import and banking examples
now use 21/22 and 29/30. A qualifying healthcare example explicitly uses 9/10.
The paper export refund section is conditional on negative box 49; it is not a
general export-sales field. Box 56 prints abs(49 - 55), which conflicts with a
simple subtraction of a positive refund from the available credit. The guides
flag the sign convention for authority confirmation and do not automate it.
The general electronic export field remains unverified.

The BOPA full 2019 consolidation includes articles omitted from the previously
read fragment. It changes the earlier legal conclusion:

- Article 14 expressly exempts qualifying goods exports and related operations.
  Article 42(2)(a) locates transported goods where transport begins. The previous
  correction that described exports generally as outside the territory and
  suggested the law contained only import exemptions was wrong and is withdrawn.
- Article 6(10) excludes specified interest and non-commission financial
  operations from the charge; article 6(11) excludes insurance and its specified
  intermediation. Searching only rate articles 57–60 could not settle that issue.
- Articles 57, 58, 59, 60 and 60 bis confirm rates of 4.5%, 1%, 0%, 9.5% and 2.5%.
  Public or qualifying non-profit cultural supplies can fall under article 59;
  article 60 bis covers its listed cultural supplies outside those conditions.
  Healthcare under article 59(2) needs the provider, patient and reimbursement
  conditions. The rates were right; several classifications and pinpoints were wrong.
- Input eligibility is in articles 61–65. Article 63 contains the relevant
  vehicle presumptions; article 64 contains exclusions and exceptions; article
  65 requires documentary support for every claim. The old article 60 citation,
  blanket vehicle denial and EUR 500 invoice threshold were unsupported.
- Article 78 confirms turnover-based filing frequency, part-year annualisation
  and quarterly startup filing, subject to the simplified-regime exception.
  The portal's form 940 is specific to the financial sector; it does not support
  an annual return for every IGI taxpayer.

The source guide and agent guide now agree on these points. Supplier names and
bank descriptions remain classification clues requiring documentary checks.
Customs amounts in the worked import example are explicit assumptions. Later
amendments to the 2019 consolidation, specialist refunds and the current
electronic field layout have not been fully verified.

Local primary-source retrieval records:

- https://bopadocuments.blob.core.windows.net/bopa-documents/031055/html/GD20190614_13_50_37.html: 359,444 bytes; SHA-256 `fbc64694435d41bee9174aa9b65b1fe0877534f613899c6e7a5673c150522006`.

- https://bopadocuments.blob.core.windows.net/bopa-documents/031055/html/1_GD20190614_13_50_37.html: 128,006 bytes; SHA-256 `c9daeb82d24f402fad3020932284a9954158a045a7c19f2abd186af77c6c88ec`.

- https://bopadocuments.blob.core.windows.net/bopa-documents/031055/html/2_GD20190614_13_50_37.html: 103,448 bytes; SHA-256 `c34c0381afce7cd3221c36ae1dd640a0cd6479813ba67c1a9f5a21afdeb55a33`.

- https://www.e-tramits.ad/tramits/impostos/igi: 138,546 bytes; SHA-256 `5b810ea7ee87ebd16acc11c94f8e1b35fe14c9d2b29314d6fa12f0b82374a5ae`.

The unprefixed BOPA HTML contains the full consolidation. The `1_` and `2_`
documents overlap portions of it and begin or end within articles. They are not
individually complete statutes. The UTF-16 decoding succeeded. A corpus search
found the detailed rate/frequency table in `ad-income-tax.md` already consistent
on those figures and conditions; no duplicate numerical correction was needed.
