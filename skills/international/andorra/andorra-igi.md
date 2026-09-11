---
name: andorra-igi
description: "Use this draft when preparing or reviewing an Andorran IGI return, classifying sales and purchases, or reconciling import tax, reverse charges and prior credits. It maps the numbered fields of the government-published form 900, including the domestic 0% rate, and explains how the filing period depends on turnover. The cited 2019 consolidated law distinguishes taxable supplies, export exemptions and operations outside the charge. The current electronic form, later legal amendments and specialist refund calculations still require verification. Obtain local professional review before filing or relying on a tax computation."
version: 2.1
jurisdiction: AD
tax_year: 2025
last_updated: 2026-09-12
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Andorra IGI

## Section 1: Quick reference

| Field | Value |
|---|---|
| Country | Principality of Andorra |
| Tax | Impost General Indirecte (IGI) |
| Standard rate | 4.5%, article 57 |
| Reduced rate | 1%, article 58: qualifying food excluding alcohol, water and publications |
| Special rate | 2.5%, article 60 bis: passenger transport except cable transport, specified cultural services outside the article 59 provider conditions, art, collectors' items and antiques |
| Increased rate | 9.5%, article 60: banking and financial services within the charge |
| Super-reduced rate | 0%, article 59: qualifying health, education, social, sporting and cultural services, residential letting, reimbursable medicines and other listed supplies; conditions apply |
| Export exemption | Qualifying goods exports and related services under article 14; keep distinct from article 59's 0% domestic supplies |
| Operations outside the charge | Article 6 includes specified interest/non-commission financial services and insurance activities; this is a separate category from exemption |
| Return | Form 900, Autoliquidació de l'IGI |
| Portal | [Government IGI filing page](https://www.e-tramits.ad/tramits/impostos/igi) |
| Authority | Departament de Tributs i de Fronteres |
| Currency | EUR |
| Frequency | Prior-year net turnover below EUR 250,000: half-yearly; EUR 250,000 to below EUR 3,600,000: quarterly; EUR 3,600,000 or more: monthly |
| Filing months | Half-yearly: July and January; quarterly: April, July, October and January; monthly: following month. Start-ups generally file quarterly, with a half-yearly exception under the simplified regime |
| Review | Source-cited draft, pending a licensed Andorran practitioner's review |

Sources: [Llei 11/2012, consolidated text published in June 2019, articles 6, 14,
57–65 and 78](https://bopadocuments.blob.core.windows.net/bopa-documents/031055/html/GD20190614_13_50_37.html); [current government filing guidance](https://www.e-tramits.ad/tramits/impostos/igi).
The former general annual-summary deadline of 31 March has no verified basis in
these sources and is withdrawn. The separate financial-sector annual form 940
does not establish that obligation for every filer.

### Published form 900 fields

The [government-published PDF](https://www.govern.ad/documents/d/guest/9002016?download=true) uses numeric boxes. The former A/B/C map
was unsupported. Its 0% domestic supply fields are **9 for the base and 10 for
the tax**, which is zero. The three-page PDF's text was retrieved through web
access on 12 September 2026; local download and browser access failed because
the government host did not resolve. Local PDF rendering and the logged-in
electronic form remain unverified. Confirm the live form before filing.

Each paired row below lists the base box first and the tax box second.

| Boxes | Published meaning |
|---|---|
| 1 / 2 | Output at 9.5% |
| 3 / 4 | Output at 4.5% |
| 5 / 6 | Output at 2.5% |
| 7 / 8 | Output at 1% |
| 9 / 10 | Output at 0% |
| 11 / 12 | Other output, including self-assessment under article 52(1)(b) |
| 13 / 14 | Real-estate output at 4.5% |
| 15 / 16 and 17 / 18 | Used-goods output at 4.5% and 1% respectively |
| 19 / 20 | Total output base / tax |
| 21 / 22 | Import base / tax at 4.5% |
| 23 / 24 | Import base / tax at 1% |
| 25 / 26 | Other import base / tax |
| 27 / 28 | Total import base / tax |
| 29 / 30 | Domestic input at 9.5% |
| 31 / 32 | Domestic input at 4.5% |
| 33 / 34 | Domestic input at 2.5% |
| 35 / 36 | Domestic input at 1% |
| 37 / 38 | Domestic input at 0% |
| 39 / 40 | Other domestic input, including corresponding self-assessment |
| 41 / 42 | Domestic real-estate input at 4.5% |
| 43 / 44 | Total domestic input base / tax |
| 45 | Output tax less input tax: `20 - (28 + 44)` |
| 46 | Credit from previous periods |
| 47 | Credit from modifications of earlier tax amounts |
| 48 | Credit for earlier indirect taxes under transitional provisions |
| 49 | Subtotal after boxes 46–48 |
| 50 / 51 | Transitional inventory credit applied / resulting balance |
| 52 / 53 / 54 | Prior-year exports / current-year exports / exports subject to refund |
| 55 / 56 | Export refund / credit for later periods; specialist calculation below |
| 57 / 58 | Box 51 balance / real-estate output tax already paid through a notary |
| 59 | Amount payable if `51 - 58` is positive |
| 60 / 61 | Credit carried forward / refund where `51 - 58` is negative, subject to the applicable refund conditions |
| 62 | Transitional inventory credit left for later periods |
| 63 / 64 | Original / final differential tax for an additional declaration |

The PDF also asks for the declarant's NRT, name, representative and identity
document, filing frequency, year and period, and the original declaration number
for an additional return. Payment/refund details and a dated signature follow.
Populate these from verified records.

**Form limits:** the export-refund section applies only when box 49 is negative.
It prints box 55 as 4.5% of box 54, capped at the absolute value of box 49, and
box 56 as the absolute value of `49 - 55`. That last expression needs confirmation:
subtracting a positive refund from a negative balance increases its absolute value.
Do not turn it into an automatic carry-forward calculation. The PDF's housing
footnote cites article 59.10, while the 2019 consolidation places qualifying
housing transfers at article 59(11). Confirm current instructions for these cases.

### Unresolved inputs

| Missing fact | Treatment before review |
|---|---|
| Rate or supply category | Hold the classification until the relevant legal conditions are checked |
| Supplier location or establishment | Obtain the invoice and supplier details before applying domestic or reverse-charge treatment |
| Deduction evidence | Hold the claim until article 65 evidence is available |
| Business use | Apply articles 63–64, including any statutory vehicle presumption, and record the evidence |
| SaaS billing entity | Check the actual supplier and place of supply; a brand name alone does not establish reverse charge |

### Internal review thresholds

These are workflow flags, not statutory thresholds: a transaction above EUR 10,000;
a provisional tax difference above EUR 500; one counterparty above 40% of input or
output; more than four unresolved classifications; or a net tax balance below EUR 5,000.

## Section 2 — Required inputs and refusal catalogue

### Required inputs

Obtain the invoice register, the client's NRT and the filing period. Each input
claim needs the invoice, customs document or other evidence required by article
65, regardless of value. Bank statements support reconciliation but do not prove
the tax base, rate or right to deduct. Obtain the prior return and evidence for
any credit carried into box 46. Hold unsupported claims for review.

### Andorra-specific refusal catalogue

- **R-AD-1 — Below registration threshold** — Trigger: the article 5(4) annual turnover measure does not exceed EUR 40,000 (EUR 150,000 for agricultural and livestock activities), and no voluntary election applies. Message: "Below the mandatory IGI registration threshold. If not voluntarily registered, no IGI return is required."  _(R-AD-1)_
- **R-AD-2 — Financial services at 9.5%** — Trigger: complex financial services classification needed. Message: "Banking and financial services at 9.5% require specialist analysis to distinguish taxable services from article 6 exclusions. Flag for reviewer."  _(R-AD-2)_
- **R-AD-3 — Partial exemption (proportional deduction)** — Trigger: mixed activities with different deduction rights. Message: "Check deduction rights under articles 61–65 and any special regime. An export exemption or domestic 0% rate alone does not establish blocked input tax. Flag for reviewer."  _(R-AD-3)_
- **R-AD-4 — Real property transactions** — Trigger: sale of real property. Message: "Sale of real property may be subject to IGI or to the Impost sobre les Transmissions Patrimonials. Specialist analysis required."  _(R-AD-4)_
- **R-AD-5 — Tourist IGI refund scheme** — Trigger: retail sales to tourists claiming refund. Message: "Tourist refund scheme has specific procedures and thresholds. Flag for reviewer."  _(R-AD-5)_

## Section 3 — Supplier pattern library (the lookup table)

### 3.1 Andorran banks (article 6 exclusions and taxable fees)

**Andorran banks pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ANDBANK | 9.5% for fee-based services; EXCLUDE for interest | Taxable fees at increased rate; check article 6(10) for interest |
| CREAND, CREDI ANDORRA | Same | Same |
| MORABANC | Same | Same |
| VALL BANC | Same | Same |
| INTERESSI, INTERES | EXCLUDE | Interest: check article 6(10) exclusion |

### 3.2 Andorran government (exclude)

**Andorran government pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| GOVERN D'ANDORRA | EXCLUDE | Government fee, sovereign act |
| TRIBUTS I FRONTERES | EXCLUDE | Tax payment |
| DUANA, CUSTOMS | EXCLUDE for duty; check import IGI for boxes 22/24/26 |  |
| CASS | EXCLUDE | Social security |

### 3.3 Andorran utilities

**Andorran utilities pattern table**

| Pattern | Treatment | Box | Notes |
| --- | --- | --- | --- |
| FEDA, FORCES ELECTRIQUES D'ANDORRA | Domestic 4.5% | 31/32 | Electricity |
| ANDORRA TELECOM, STA | Domestic 4.5% | 31/32 | Telecoms |

### 3.4 Insurance (article 6(11))

**Insurance pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ASSEGURANCES, SEGUROS | EXCLUDE | Insurance activity outside the IGI charge under article 6(11) |

### 3.5 Food retail

**Food retail pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| PYRENEENNE, SUPERMERCAT | Domestic 1% for basic food | Reduced rate |
| RESTAURANT, CAFE | Default BLOCK input IGI | Check article 64 restrictions and exceptions |

### 3.6 SaaS — non-resident suppliers (reverse charge)

**SaaS non-resident pattern table**

| Pattern | Billing entity | Box | Notes |
| --- | --- | --- | --- |
| GOOGLE, MICROSOFT, ADOBE, META | Verify supplier and establishment | 11/12 and 39/40 if self-assessment applies | Check article 52(1)(b), rate and deduction evidence |
| ZOOM, SLACK, NOTION, ANTHROPIC, OPENAI | Verify supplier and establishment | 11/12 and 39/40 if self-assessment applies | Check article 52(1)(b), rate and deduction evidence |
| AWS, AMAZON WEB SERVICES | Verify supplier and establishment | 11/12 and 39/40 if self-assessment applies | Check article 52(1)(b), rate and deduction evidence |

### 3.7 Spanish and French suppliers (imports)

**Spanish and French suppliers pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| Spanish entity (ES-) | Import: industrial goods via customs agreement (no duty, IGI at applicable rate) | Agricultural goods: full duty + IGI |
| French entity (FR-) | Same as Spain | Same treatment at border |

### 3.8 Professional services (Andorra)

**Professional services pattern table**

| Pattern | Treatment | Box | Notes |
| --- | --- | --- | --- |
| ADVOCAT, NOTARI, ASSESSOR FISCAL | Domestic 4.5% | 31/32 | Professional services |

### 3.9 Internal transfers and exclusions

**Internal transfers and exclusions pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TRANSFERENCIA PROPIA, TRASPAS | EXCLUDE | Internal movement |
| DIVIDEND, PRESTEC | EXCLUDE | Out of scope |
| RETIRADA CAIXER | Ask | Default exclude; ask purpose |

## Section 4 — Worked examples

### Example 1 — Non-resident service reverse charge (Spanish consulting)

**Input line:**
`05.04.2026 ; CONSULTORIA BARCELONA SL ; DEBIT ; Consulting services ; EUR 5,000`

**Reasoning:**
Assume the consulting service is supplied to an Andorran business, is located in Andorra under the applicable service rule, and the supplier is not established there. Article 52(1)(b) self-assessment applies at 4.5%. Output boxes 11/12 = EUR 5,000/EUR 225; input boxes 39/40 = EUR 5,000/EUR 225 if fully deductible. Net zero under that assumption.

**Output table**

| Date | Counterparty | Gross | Net | IGI | Rate | Box (input) | Box (output) | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 05.04.2026 | CONSULTORIA BARCELONA SL | -5,000 | -5,000 | 225 | 4.5% | 39/40 | 11/12 | N | — | — |

### Example 2 — Banking service at 9.5%

**Input line:**
`10.04.2026 ; ANDBANK ; DEBIT ; Account management fee Q1 ; -150`

**Reasoning:**
Banking fee at the 9.5% increased rate. Input IGI = 150 / 1.095 * 0.095 = 13.01. Deductible if for business use.

**Output table**

| Date | Counterparty | Gross | Net | IGI | Rate | Box | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10.04.2026 | ANDBANK | -150 | -136.99 | -13.01 | 9.5% | 29/30 | N | — | — |

### Example 3 — Food sale at 1% reduced rate

**Input line:**
`12.04.2026 ; CASH SALE ; CREDIT ; Daily bakery sales ; +2,020`

**Reasoning:**
Bread and basic food at 1% reduced rate. Net = 2,020 / 1.01 = 2,000. IGI = 20.

**Output table**

| Date | Counterparty | Gross | Net | IGI | Rate | Box | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 12.04.2026 | CASH SALE | +2,020 | +2,000 | 20 | 1% | 7/8 | N | — | — |

### Example 4 — Import of industrial goods from Spain

**Input line:**
`18.04.2026 ; SPANISH MACHINERY SL ; DEBIT ; Customs entry — CNC machine ; -30,000`

**Reasoning:**
Assume the customs assessment establishes a EUR 30,000 IGI base and EUR 1,350 IGI at 4.5%, with no customs duty due in this example. The bank payment alone does not establish those amounts or eligibility for customs relief. Claim the assessed import IGI only if articles 61–65 permit deduction and the customs document supports it.

**Output table**

| Date | Counterparty | Gross | Net | IGI | Rate | Box | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 18.04.2026 | SPANISH MACHINERY SL | -30,000 | -30,000 | -1,350 | 4.5% | 21/22 | N | Q1 | "Confirm if capital good" |

### Example 5 — Entertainment, blocked

**Input line:**
`22.04.2026 ; RESTAURANT LA BORDA ; DEBIT ; Client dinner ; -209`

**Reasoning:**
Treat this client dinner as an unresolved article 64 claim until its purpose and any applicable exception are checked. A bank description alone does not settle deduction.

**Output table**

| Date | Counterparty | Gross | Net | IGI | Rate | Box | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 22.04.2026 | RESTAURANT LA BORDA | -209 | -209 | 0 | — | — | Y | Q2 | "Article 64 review required" |

### Example 6 — Export of goods

**Input line:**
`28.04.2026 ; UK CUSTOMER LTD ; CREDIT ; Invoice AD-2026-012 electronics ; +12,000`

**Reasoning:**
Assume the goods are shipped from Andorra and satisfy article 14 export conditions. Output is exempt, with evidence required. Assess input recovery separately under articles 61–65. The general electronic export field remains unverified; do not assign domestic 0% box 9.

**Output table**

| Date | Counterparty | Gross | Net | IGI | Rate | Box | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 28.04.2026 | UK CUSTOMER LTD | +12,000 | +12,000 | 0 | Export exemption | Pending form confirmation | N | Verify field | No |

### Example 7: Qualifying healthcare at 0%

Assume a health professional has a current CASS agreement, the patient is
affiliated to CASS, and CASS reimburses at least part of the act. For an eligible
EUR 1,000 service under article 59(2), record EUR 1,000 in output box 9 and zero
tax in box 10. Retain evidence of those conditions; a healthcare description
alone does not establish the 0% rate.

---

## Section 5: Classification rules

### 5.1 Standard rate
Article 57 sets the residual 4.5% rate. Use output boxes 3/4 and, where deductible,
domestic input boxes 31/32.

### 5.2 Reduced rate
Article 58 sets 1% for its listed food, water and publication supplies. Alcohol is
excluded. Use output boxes 7/8. Cultural performances do not qualify at 1% merely
because they are cultural.

### 5.3 Special rate
Article 60 bis sets 2.5% for passenger transport except cable transport, specified
cultural services outside the article 59 provider conditions, and qualifying art,
collectors' items and antiques. Use output boxes 5/6. The former general inclusion
of optical and para-pharmaceutical products was unsupported.

### 5.4 Banking, finance and insurance
Article 60 sets 9.5% for banking and financial services within the charge: output
boxes 1/2 and deductible domestic input boxes 29/30. Article 6(10) excludes specified
capital remuneration and non-commission financial services. Article 6(11) excludes
insurance activities and the specified intermediation. Classify the actual service.

### 5.5 Domestic 0% supplies
Article 59 sets the super-reduced 0% rate. Output belongs in boxes 9/10. Examples
include qualifying health and education services and residential letting. Health
professional services under article 59(2) require a current CASS agreement, an
affiliated or beneficiary recipient and at least partial reimbursement of the act.
Listed cultural services by the specified public or non-profit providers may also
qualify at 0%. Check the complete conditions. Input recovery remains subject to
articles 61–65; a 0% output rate does not itself block deduction.

### 5.6 Exports and other exemptions
Article 14 exempts qualifying goods exports and directly related services. Keep
export evidence and analyse input recovery under articles 61–65 and the applicable
refund provisions. A goods shipment beginning in Andorra is not automatically
outside the territorial scope: article 42(2)(a) locates it in Andorra, with article
14 then providing the qualifying export exemption. Other services require their
own place-of-supply analysis. Do not put every export in the domestic 0% boxes.
The PDF identifies export amounts in boxes 52–54 for its conditional refund
section; the general electronic reporting field for other exports remains unverified.

### 5.7 Non-resident services
Where articles 43 and 52(1)(b) require the Andorran business recipient to self-assess,
use output boxes 11/12 and corresponding deductible input boxes 39/40. Net tax
is zero only to the extent that the input tax is deductible.

### 5.8 Goods imports
Use the customs document and applicable rate: boxes 21/22, 23/24 or 25/26. Deduct
only eligible input tax. A foreign supplier payment alone does not evidence import
IGI or establish a customs-duty exemption.

### 5.9 Capital goods
The PDF has no general fixed-asset boxes matching the former B5/B6 labels. Classify
the acquisition by domestic/import route and rate, including the separate real-estate
fields where relevant. Apply the investment-goods use and adjustment rules separately.

### 5.10 Input restrictions and evidence
Articles 63–65 govern deduction, not article 60. Article 63(2)(b) presumes 50%
business use for relevant passenger vehicles used in the activity, and 100% for
specified categories, subject to contrary evidence. A blanket 0% vehicle rule is wrong.
Article 64 lists blocked expenditure and exceptions, including conditions for
travel, hotel and restaurant services and goods acquired for the business's own
taxable supplies. Article 65 requires qualifying invoice, customs or notarial evidence.
Check those conditions before accepting or denying a claim.

Source: [2019 consolidated IGI Law](https://bopadocuments.blob.core.windows.net/bopa-documents/031055/html/GD20190614_13_50_37.html). Later amendments to these provisions
have not been exhaustively checked in this form-mapping pass.

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Vehicle costs

- **Vehicle costs default/question** — Default: Apply the article 63 vehicle presumptions and check contrary evidence. Question: "Is this a personal or business-only vehicle?"

### 6.2 Entertainment

- **Entertainment default/question** — Default: block. Question: "Confirm purpose, evidence and any article 64 exception."

### 6.3 Financial services classification

- **Financial services default/question** — Default: 9.5% for taxable banking fees; check article 6(10) for interest. Question: "Is this a fee-based service (9.5%) or operation outside the charge under article 6?"

### 6.4 EU customs agreement classification

- **EU customs classification default/question** — Default: flag for borderline products. Question: "Confirm HS code — industrial (chapters 25-97, no duty) or agricultural (chapters 1-24, full duty)?"

### 6.5 Tourist refund claims

- **Tourist refund default/question** — Default: flag for reviewer. Question: "Are exports to tourists documented with refund scheme paperwork?"

### 6.6 Real property

- **Real property default/question** — Default: flag for reviewer. Question: "Is this subject to IGI or the property transfer tax (ITP)?"

### 6.7 Mixed-use expenses

- **Mixed-use expenses default/question** — Default: hold the claim until article 63 determines eligibility and allocation, including any applicable vehicle presumption. Question: "What business percentage?"

## Section 7: Working paper and return reconciliation

Keep the original bank debit/credit signs in the transaction record. Map verified
tax bases and eligible tax amounts to the numbered return boxes as positive
amounts, except where an actual credit note or adjustment calls for a reduction.
A payment can require both a base and a tax field, and reverse charge requires
both output and input entries. Do not use one undifferentiated signed SUMIFS total.

For an ordinary return with no special refund or transitional claim:

```text
box 20 = total output tax in boxes 2, 4, 6, 8, 10, 12, 14, 16 and 18
box 28 = eligible import tax in boxes 22, 24 and 26
box 44 = eligible domestic input tax in boxes 30, 32, 34, 36, 38, 40 and 42
box 45 = box 20 - box 28 - box 44
box 49 = box 45 - box 46 - box 47 - box 48
box 51 = box 49 - eligible transitional inventory credit applied in box 50
box 57 = box 51
final balance = box 51 - eligible real-estate tax already paid in box 58
positive final balance -> box 59 payable
negative final balance -> establish carry-forward or refund eligibility for boxes 60/61
```

Reconcile box 46 to the prior return before applying it. The old C1/C2/C5 formula
could omit an existing credit when the current period already had a credit. Export
refunds, transitional inventory credits, additional declarations and real-estate
payments require their specific instructions; the ordinary calculation above does
not automate those cases or divide one credit between carry-forward and refund.

## Section 8 — Andorra bank statement reading guide

**Format conventions.** Andorran banks (Andbank, Creand, MoraBanc) typically export in CSV with DD/MM/YYYY dates. EUR currency only.

**Language.** Descriptions in Catalan (official), Spanish, or French. Treat equivalently.

**Internal transfers.** "Traspas entre comptes", "transferencia propia". Always exclude.

**Customs entries.** Goods arrive via Spanish (southern) or French (northern) border only. Look for "duana" entries.

## Section 9 — Onboarding fallback (only when inference fails)

### 9.1 Entity type

- **Entity type inference/fallback** — Inference: SL, SA in name = company. Individual name = sole trader. Fallback: "Entity type?"

### 9.2 IGI registration

- **IGI registration inference/fallback** — Inference: if asking for IGI return, registered. Fallback: "Are you registered for IGI (above EUR 40,000 turnover)?"

### 9.3 NRT

- **NRT fallback** — Fallback: "What is your NRT?"

### 9.4 Period

- **Period inference/fallback** — Inference: from statement dates. Fallback: "Which filing period and frequency?"

### 9.5 Industry

- **Industry inference/fallback** — Inference: counterparty mix. Fallback: "What does the business do?"

### 9.6 Prior credit

- **Prior credit fallback** — Always ask: "Do you have IGI credit from previous filing period? (box 46)"

## Section 10 — Reference material

### Sources

- **Sources list** — 1. Llei 11/2012, del 21 de juny, de l'Impost General Indirecte — Articles 4, 50, 57, 58, 59, 60, 78, 85 2. Reglament de l'IGI 3. Llei 21/2014 and Llei 3/2019 (amendments) 4. EU Customs Agreement Decision 90/680/EEC  _(Llei 11/2012, del 21 de juny, de l'Impost General Indirecte)_

### Known gaps

1. Tourist IGI refund scheme procedures and current thresholds need practitioner verification.
2. Financial services and insurance require the article 6 scope tests and any applicable special regime.
3. EU customs agreement product classification for borderline goods.

### Change log

- **v2.1 (12 September 2026):** Replaced unsupported box labels with published form 900 fields; corrected 0%, export, input-tax and filing-period instructions. Current electronic fields and PDF rendering remain unverified.
- **v2.0 (April 2026):** Full rewrite to 10-section architecture.
- **v1.0:** Initial skill.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
