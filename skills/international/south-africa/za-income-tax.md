---
name: za-income-tax
description: Use this skill whenever asked about South African income tax for self-employed individuals. Trigger on phrases like "how much tax do I pay", "ITR12", "income tax return", "SARS", "tax brackets", "provisional tax", "IRP6", "rebates", "medical credits", "retirement deduction", "turnover tax", "eFiling", or any question about filing or computing income tax for a self-employed or sole proprietor client in South Africa. ALWAYS read this skill before touching any South African income tax work.
version: 2.0
jurisdiction: ZA
category: international
tax_year: 2026
tax_year_notes: "2026/27"
last_updated: 2026-09-29
reviewed_by: Werner Britz
review_status: pending_review
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# ZA Income Tax

## South African Income Tax -- Self-Employed Skill v2.0

> **Accountant-reviewed.** Rates and thresholds reviewed against the cited authorities by **Werner Britz** on 2026-06-12; the sign-off is recorded in the frontmatter (`reviewed_by`) and on the roster in `PARTNERS.md`. The verified figures are stated in the sections below with their sources (the separate "Verified rates & thresholds" list that carried them was folded into the body on 2026-09-29). Items the review flagged for clarification are excluded from that sign-off and remain marked in the text. On 2026-09-29 the 2026/27 income tax table, the secondary and tertiary rebates and the 65+ tax thresholds were corrected against SARS's published tables, which differ from the Budget-day figures the review recorded (bounds R245,100 not R245,200, R383,100 not R383,000, R887,000 not R887,100, R1,878,600 not R1,878,300; rebates R9,765 and R3,249; thresholds R153,250 and R171,300), the worked example was recomputed, and Section 10 was added from the review's own list of missing rules; `review_status` is therefore `pending_review` until the reviewer confirms the corrected text.

## Section 1 -- Quick reference

**Quick reference field table**

| Field | Value |
| --- | --- |
| Country | South Africa |
| Tax type | Income tax (normal tax) on trade income |
| Primary legislation | Income Tax Act 58 of 1962 |
| Supporting legislation | Tax Administration Act 28 of 2011; Sixth Schedule (Turnover Tax); Fourth Schedule (Provisional Tax) |
| Tax authority | SARS (South African Revenue Service) |
| Filing portal | SARS eFiling (https://www.sarsefiling.co.za); the authority site is https://www.sars.gov.za |
| Currency | ZAR only |
| Tax year | 1 March -- 28 February |
| Return form | ITR12 |
| Filing season (2026 year of assessment, 1 March 2025 -- 28 February 2026) | Auto-assessment notices 1--12 July 2026; manual filing opens 13 July 2026; non-provisional taxpayers file by 23 October 2026; provisional taxpayers and trusts by 22 January 2027. Disagreeing with an auto-assessment does not extend the date (SARS Filing Season 2026 notice) |
| Provisional tax | IRP6 (1st: 31 Aug, 2nd: last day Feb, 3rd voluntary: 30 Sep) |
| Primary rebate (2026/27) | R17,820 |
| Secondary rebate (65+, additional) | R9,765 |
| Tertiary rebate (75+, additional) | R3,249 |
| Retirement fund deduction | 27.5% of the greater of remuneration or taxable income, capped at R430,000 for years of assessment commencing on or after 1 March 2026 (R350,000 before) |
| Turnover tax | Micro businesses other than personal service providers, taxable turnover up to R2,300,000 from 1 March 2026 |
| Contributor | Open Accountants Community |
| Validated by | Werner Britz CA(SA), Spurwing CFO |
| Validation date | May 2026 |

**Progressive tax table (2026/2027 year of assessment, 1 March 2026 -- 28 February 2027)**  _(SARS, Rates of tax for individuals, 2027 year of assessment)_

| Taxable income (ZAR) | Rate |
| --- | --- |
| 1--245,100 | 18% |
| 245,101--383,100 | R44,118 + 26% above R245,100 |
| 383,101--530,200 | R79,998 + 31% above R383,100 |
| 530,201--695,800 | R125,599 + 36% above R530,200 |
| 695,801--887,000 | R185,215 + 39% above R695,800 |
| 887,001--1,878,600 | R259,783 + 41% above R887,000 |
| 1,878,601+ | R666,339 + 45% above R1,878,600 |

The 2025/26 table was unchanged from 2024/25 (no inflation adjustment in Budget 2025); the 2026/27 bounds and fixed amounts above are SARS's published figures, which differ from the Budget-day figures the June 2026 review recorded (see the provenance note at the top of this guide).

**Tax thresholds (below = no tax)**  _(SARS, Rates of tax for individuals, 2027)_

| Age | Threshold |
| --- | --- |
| Below 65 | R99,000 |
| 65--74 | R153,250 |
| 75+ | R171,300 |

**Medical tax credits (s6A, 2026/2027)**  _(s6A; SARS, Medical scheme fees tax credit rates, 2027)_

| Member | Monthly |
| --- | --- |
| Main member | R376 |
| First dependant | R376 (SARS states the two-person figure as R752) |
| Each additional | R254 |

**Turnover tax table (Sixth Schedule, 2026/2027)**  _(Sixth Schedule; SARS, Turnover tax rates, 2027)_

| Taxable turnover (ZAR) | Rate |
| --- | --- |
| 0--600,000 | 0% |
| 600,001--950,000 | 1% above R600,000 |
| 950,001--1,400,000 | R3,500 + 2% above R950,000 |
| 1,400,001--2,300,000 (the qualifying turnover limit) | R12,500 + 3% above R1,400,000 |

The bands were re-set from 1 March 2026 (2025/26: 0% to R335,000; 1% to R500,000; R1,650 + 2% to R750,000; R6,650 + 3% above), and the qualifying turnover limit rose from R1,000,000 to R2,300,000 in line with the VAT registration threshold.

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown age | STOP -- age determines rebates and threshold |
| Unknown expense category | Not deductible |
| Unknown business-use proportion | 0% |
| Unknown whether home office qualifies | Not deductible (IN 28 strict) |
| Entertainment expenses | Critically review under s 11(a) and s 23(g); conservatively disallow if no clear nexus to income production |

**Read this whole section before classifying anything.**

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

- **Minimum viable inputs** — Bank statement for the tax year (1 March -- 28 February). Acceptable from: FNB (First National Bank), Standard Bank, Nedbank, Absa, Capitec, Investec, Discovery Bank, TymeBank, or fintech (Revolut, Wise).
- **Recommended inputs** — Invoices, IRP6 payment records, medical aid statements, RA contribution certificates, vehicle logbook.
- **Ideal inputs** — Complete bookkeeping, prior year ITR12, IT34 (assessment), asset register.

### Refusal catalogue

- **R-ZA-1 -- Company/CC/Trust** — This skill covers sole proprietors only. Companies file ITR14 at 27% corporate rate. Trusts file ITR12T. (Trigger: client is a company, close corporation, or trust.)
- **R-ZA-2 -- Foreign income** — Foreign income and DTA analysis are outside scope; consult a registered tax practitioner. (Trigger: significant foreign income.) For the record: the s 10(1)(o)(ii) exemption is for employment income earned outside South Africa during more than 183 days (60 of them continuous) in any 12-month period, capped at R1.25 million since 1 March 2020; it does not cover a sole proprietor's trade income, which a resident is taxed on worldwide with relief under s 6quat and the relevant DTA (Section 10.15 and 10.16).  _(Income Tax Act s 10(1)(o)(ii), s 6quat)_
- **R-ZA-3 -- Capital gains tax** — The CGT computation is outside scope, but flag every CGT trigger: sale of a vehicle, equipment, the practice, or property used in trade, and cessation of trade with assets retained (Section 10.1). (Trigger: disposal of capital assets.)  _(Income Tax Act Eighth Schedule)_
- **R-ZA-4 -- Age unknown** — I cannot compute without knowing your age -- it determines rebates and tax threshold. (Trigger: age not provided.)

## Section 3 -- Transaction pattern library (the lookup table)

### 3.1 South African banks (fees and interest)

**South African banks (fees and interest)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| FNB, FIRST NATIONAL BANK | Bank charges: deductible | Business account fees |
| STANDARD BANK, SBSA | Bank charges: deductible | Same |
| NEDBANK | Bank charges: deductible | Same |
| ABSA | Bank charges: deductible | Same |
| CAPITEC | Bank charges: deductible | Same |
| INVESTEC | Bank charges: deductible | Same |
| DISCOVERY BANK, TYMEBANK | Bank charges: deductible | Same |
| REVOLUT, WISE (fees) | Deductible | Fintech fees |
| INTEREST (credit) | Taxable income up to exemption (R23,800 <65; R34,500 65+); excess = taxable | Interest exemption applies |
| INTEREST (debit) | Deductible if business loan | Personal: NOT deductible |
| LOAN, HOME LOAN (principal) | EXCLUDE | Principal movement |

### 3.2 SA government and statutory bodies

**SA government and statutory bodies**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SARS | EXCLUDE | Tax payment (provisional/income) |
| UIF, UNEMPLOYMENT INSURANCE | Deductible if employer contribution | Employee-related |
| COIDA, COMPENSATION FUND | Deductible | Workers compensation |
| CIPC | Deductible only for fees of the ongoing trade (annual returns, name changes); incorporation fees are capital and not deductible (s 23(g)) | A sole proprietor does not register with CIPC; a CIPC debit usually means a company, which is outside scope (R-ZA-1) |

### 3.3 SA utilities and telecoms

**SA utilities and telecoms**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ESKOM, CITY POWER, CITY OF [JHB/CPT/DBN] | Split the bill: electricity, water and refuse are deductible to the extent used in the production of income; property rates only in proportion to the part of the property used for trade (the qualifying office area for a home office) | A municipal bill bundles rates with electricity, water and refuse; apportion each line (s 11(a); IN 28) |
| RAND WATER | Deductible if business premises | Water |
| VODACOM, MTN, CELL C, TELKOM, RAIN | Deductible: business phone/internet | Mixed: apportion |

### 3.4 Insurance

**Insurance**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| HOLLARD, SANTAM, OLD MUTUAL, MOMENTUM, OUTSURANCE | Short-term asset and liability cover for the trade (vehicles, premises, public liability): deductible under s 11(a); proceeds for damaged business assets are recouped under s 8(4)(a) to the extent of allowances claimed. Personal cover: NOT deductible | Key-person and other risk policies follow s 11(w): premiums are deductible only under a "conforming" s 11(w)(ii) policy (pure risk, no surrender value, owned by the employer, policy states that s 11(w)(ii) applies), and its proceeds are then gross income; a non-conforming policy, the default, has non-deductible premiums and proceeds exempt under s 10(1)(gH). Income protection premiums are not deductible (s 23(p)) and the benefits are exempt (s 10(1)(gI)). Personal life cover: not deductible; an RA is deductible only under s 11F |
| DISCOVERY HEALTH, BONITAS, GEMS, MEDIHELP | NOT deductible from income | Medical = s6A/s6B credits (against tax, not income) |

### 3.5 SaaS and software -- international

**SaaS and software -- international**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| GOOGLE, MICROSOFT, ADOBE, META | Deductible expense | Foreign SaaS |
| GITHUB, OPENAI, ANTHROPIC | Deductible expense | Non-EU |
| SLACK, ZOOM, ATLASSIAN | Deductible expense | Check entity |

### 3.6 Professional services (SA)

**Professional services (SA)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ACCOUNTANT, AUDIT, CA(SA) | Deductible | Accounting/audit fees |
| ATTORNEY, ADVOCATE, LAW FIRM | Deductible where the fees relate to trade income (debt recovery, a customer dispute, a regulatory matter: s 11(a) and s 11(c)); NOT deductible where capital in nature (acquiring a business, defending title to a capital asset, s 23(g)) or personal | Legal fees (Port Elizabeth Electric Tramway Co Ltd v CIR; SARS IN 12) |
| TAX PRACTITIONER | Deductible | Tax advisory |

### 3.7 Retirement contributions

**Retirement contributions**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ALLAN GRAY, CORONATION, 10X, SYGNIA, NINETY ONE | s11F deduction: 27.5% of taxable income, cap R430,000 | RA contributions |
| OLD MUTUAL RA, MOMENTUM RA, LIBERTY RA | Same | RA fund |

### 3.8 Transport and travel

**Transport and travel**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| FLYSAFAIR, LIFT, CEMAIR, AIRLINK (FLYAIRLINK), SAA, FLYNAMIBIA | Full ticket cost deductible to the extent of business travel (s 11(a)); keep the business-purpose evidence | Kulula (2022) and Mango (2021) no longer operate. VAT cross-reference: input VAT on a domestic ticket must be split by component (base fare, fuel, PSC and insurance carry 15%; SACAA, ATNS and Air Passenger Tax carry none); the income tax deduction does not depend on that split |
| UBER, BOLT | Deductible to the extent of trade use; keep the invoice and the business purpose | VAT cross-reference: the fare is exempt under s 12(g) of the VAT Act, so no input VAT is claimable on it even by a VAT-registered rider |
| ENGEN, SHELL, BP, SASOL, CALTEX, TOTAL | Deductible: business vehicle portion only | Fuel; requires logbook |
| AVIS, EUROPCAR, HERTZ | Deductible to the extent of business use | Rental car. VAT cross-reference: input VAT on the rental of a "motor car" is blocked under s 17(2)(c) of the VAT Act |
| SANRAL toll plazas (N1, N2, N3 and others) | Deductible: business travel portion | Gauteng e-tolls were discontinued on 12 April 2024; toll plaza fees still apply |

### 3.9 Office and supplies

**Office and supplies**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| INCREDIBLE CONNECTION, MATRIX, TAKEALOT | Item costing R7,000 or less: full write-off in the year of acquisition (BGR 7). Above R7,000: wear-and-tear under s 11(e), straight-line over the IN 47 useful life (computers 3 years, office furniture 6, office equipment 5, cellular phones 2, printers 3), apportioned for part-year use | The R7,000 test is applied to a set: items that function as one unit (a configured computer with its monitor, keyboard and mouse; matching furniture) are aggregated and cannot be split to get under the limit; independently functional items bought together (five laptops for five staff) are tested one by one (s 11(e); BGR 7; IN 47 Issue 5) |
| OFFICE NATIONAL, WALTONS | Deductible | Stationery |
| POSTNET, THE COURIER GUY (TCG), SA POST OFFICE | Deductible | Postage/courier. The SA Post Office went into business rescue in 2023 and provisional liquidation in 2025, so its availability is limited |
| MAKRO, GAME | Deductible if business supplies | Verify business purpose |

### 3.10 Food and entertainment

**Food and entertainment**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| PICK N PAY, WOOLWORTHS, CHECKERS, SPAR, SHOPRITE | Test under s 11(a) read with s 23(g). Deductible where a genuine trade purpose exists: office tea, coffee, milk and biscuits for clients in meetings or staff during working hours, bottled water for a meeting room, refreshments at a training session, catering for a business-development function, resale stock of a catering business. NOT deductible: personal grocery shopping, family meals, alcohol without a trade purpose | Keep itemised receipts and a note of the purpose; SARS queries large grocery claims by individuals. VAT cross-reference: even where income tax allows the deduction, the VAT input is blocked under s 17(2)(a) unless the vendor is in the entertainment trade |
| RESTAURANT (any) | Review under s 11(a)/s 23(g) | Bona fide business meals may be deductible; VAT input blocked under s 17(2)(a) |

### 3.11 Internal transfers and exclusions

**Internal transfers and exclusions**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| OWN TRANSFER, INTERNAL | EXCLUDE | Internal movement |
| DRAWINGS, OWNER | EXCLUDE | Personal drawings |
| DEPOSIT, OWN DEPOSIT | EXCLUDE | Capital injection |

## Section 4 -- Worked examples

### Example 1 -- Standard self-employed, mid-range

**Input:** Age 35, revenue R600,000, expenses R180,000, RA R80,000, medical R3,500/mo (main + 1 dependant), provisional paid R40,000.
**Computation (2026/27 rates):** Net profit R420,000. s11F = 27.5% x R420,000 = R115,500 (within the R430,000 cap). Taxable = R304,500. Tax = R44,118 + 26% x (R304,500 - R245,100 = R59,400) = R44,118 + R15,444 = R59,562. Less primary rebate R17,820 = R41,742. Less medical credit R9,024 (R376 x 2 x 12) = R32,718. Less provisional tax paid R40,000. Refund R7,282.

### Example 2 -- Turnover tax

**Input:** Non-professional sole proprietor, turnover R650,000.
**Computation:** R650,000 turnover falls within 2026/27 bracket R600,001--R950,000 at 1% above R600,000. Tax = 1% x R50,000 = R500.

### Example 3 -- Entertainment disallowed

**Input:** Client claims R15,000 client entertainment dinners. **Result:** Review under s 11(a) and s 23(g). If bona fide business development with evidence of business purpose, may be deductible. If no clear nexus to income production, disallow. s 23(m) does NOT apply to sole proprietors. VAT input on entertainment is separately blocked under s 17(2)(a) VAT Act.

### Example 4 -- Retirement cap exceeded

**Input:** Taxable income R2,000,000, RA R600,000.
**Computation:** 27.5% x R2,000,000 = R550,000 but cap R430,000. Deduction = R430,000. Excess R170,000 carries forward.

## Section 5 -- Tier 1 rules (deterministic)

### 5.1 Progressive rates

- **Progressive rates application** — Apply rate table to taxable income. One table for all individuals regardless of marital status.  _(Income Tax Act, rates schedule.)_

### 5.2 Rebates

- **Rebates (2026/27)** — Primary R17,820 (all). Secondary R9,765 (65+, additional: R27,585 in total). Tertiary R3,249 (75+, additional: R30,834 in total). Credits against tax, not deductions from income.  _(s6; SARS, Rates of tax for individuals, 2027)_

### 5.3 Interest exemption

- **Interest exemption** — R23,800 (under 65). R34,500 (65+). Excess is taxable.  _(s10(1)(i))_

### 5.4 s11F retirement deduction

- **s11F retirement deduction** — 27.5% of greater of remuneration or taxable income (before deduction). Cap R430,000. Excess carries forward or adds to tax-free retirement lump sum (R550,000).  _(s11F)_

### 5.5 Medical tax credits (s6A)

- **Medical tax credits (s6A)** — Main + first dependant: R376/mo each. Additional: R254/mo. Credit against tax. NOT a deduction from income.  _(s6A)_

### 5.6 Provisional tax (IRP6)

- **Provisional tax (IRP6)** — Based on estimated current year. 1st: 31 Aug (50%). 2nd: last day Feb (top-up to 100%). 3rd voluntary: 30 Sep. Under-estimation: 20% penalty if < 90% of actual (income < R1M) or 80% (> R1M). From years of assessment commencing on or after 1 March 2026, the basic-amount safe harbour threshold is R1,800,000 (up from R1,000,000).  _(Fourth Schedule)_

### 5.7 Turnover tax

- **Turnover tax** — Elective regime for a micro business with taxable turnover up to R2,300,000 (from 1 March 2026). The exclusion is for personal service providers and professional services as the Sixth Schedule and s 12E define them, not "non-professional services" loosely. It replaces income tax and CGT on the trade (and carries its own rules for dividends paid by a micro business company); it does NOT replace VAT, though a micro business below the VAT threshold would normally not register. No normal deductions are claimed against the turnover.  _(Sixth Schedule; s 12E)_

### 5.8 Wear-and-tear (s11(e))

- **Wear-and-tear (s11(e))** — Straight-line over the useful life per SARS IN 47 (Issue 5). Items costing R7,000 or less: full write-off in year of acquisition under BGR 7 (small-value assets). Items above R7,000: straight-line over IN 47 useful life (computers 3 years; office furniture 6 years; office equipment 5 years; cellular phones 2 years; printers 3 years).  _(s 11(e), SARS IN 47, BGR 7)_

### 5.9 Entertainment

- **Entertainment** — Sole proprietor entertainment is tested under the general deduction formula: s 11(a) (actually incurred in the production of income) plus s 23(g) (not of a domestic, private, or capital nature). Bona fide client business development meals with evidence of business purpose may be deductible. s 23(m) does NOT apply to sole proprietors -- it restricts deductions against employment income only. Note: VAT input on entertainment is separately blocked under s 17(2)(a) of the VAT Act regardless of income tax treatment.  _(s 11(a), s 23(g). Cross-reference: VAT Act s 17(2)(a).)_

### 5.10 Home office

- **Home office** — Four requirements under s 23(b): (1) part of a residence occupied for the trade; (2) specifically equipped for the trade; (3) regularly and exclusively used for the trade (a dual-use room gets NO deduction; IN 28 is strict); (4) for a salaried employee only, the duties are mainly performed there. Permitted expenses, apportioned by A/B where A is the office area and B the total area of the residence: rent OR bond interest (never capital repayments), rates and taxes, levies, electricity, water, cleaning, and repairs to the office portion; wear-and-tear on office-only equipment is claimed in full. Warning: the area used for trade is "tainted" for CGT. On disposal of the residence the primary residence exclusion does not apply to the tainted portion; the gain is apportioned by area and by the period of trade use, and that portion is fully subject to CGT with only the annual exclusion available. Practitioners must warn clients before they first claim home office, since the CGT on sale can exceed the lifetime income tax saved.  _(s 11(a), s 23(b); SARS IN 28 (Issue 3, March 2022); Eighth Schedule para 47)_

### 5.11 Record keeping

- **Record keeping** — 5 years from submission. Invoices, receipts, bank statements, logbooks, asset register.  _(TAA s29-32)_

## Section 6 -- Tier 2 catalogue

### 6.1 Home office qualification

- **Home office qualification** — *Why:* IN 28 requires regular and exclusive use. *Default:* NOT deductible. *Question:* "Is there a dedicated room used only for business?"

### 6.2 Motor vehicle logbook

- **Motor vehicle logbook** — *Why:* Business km unknown. *Default:* 0% business use. *Question:* "Do you have a logbook with date, destination, km, and purpose for each trip?"

### 6.3 Turnover tax vs normal tax

- **Turnover tax vs normal tax** — *Why:* Depends on expense level and qualification. *Default:* Present both. *Question:* "What are your total business expenses? Are you providing professional services?"

### 6.4 s6B additional medical expenses

- **s6B additional medical expenses** — *Why:* Depends on age and disability. *Rule:* (a) Taxpayer 65 or older, or with a qualifying disability (self, spouse or child): credit of 33.3% of medical scheme contributions in excess of 3 x the s 6A credit, PLUS 33.3% of qualifying out-of-pocket medical expenses. (b) Under 65 without disability: credit of 25% of (medical scheme contributions in excess of 4 x the s 6A credit, plus qualifying out-of-pocket expenses) to the extent that total exceeds 7.5% of taxable income. *Default:* Compute with the rule; ask for the medical scheme certificate and the out-of-pocket receipts. *Question:* "Age 65+? Disability? Out-of-pocket medical expenses?"  _(s 6B)_

### 6.5 Bad debts

- **Bad debts** — *Rule:* s 11(i) allows a bad debt only where the amount was previously included in income, so an accrual-basis taxpayer can claim it and a cash-basis taxpayer cannot. A doubtful debt allowance under s 11(j) (formulaic since 2019: 25% of debts 60 to 90 days in arrears, 40% of debts more than 90 days in arrears, subject to the conditions) reverses in the following year. *Default:* Do not claim until the debt is shown to have been in income and to be irrecoverable. *Question:* "Was this debt previously included in income? Is it truly irrecoverable?"  _(s 11(i), s 11(j); SARS Notice 1209 of 15 November 2019)_

### 6.6 Wear-and-tear and small assets

- **Wear-and-tear decision** — *Walk through:* (a) Is it a capital asset used in the trade? If not, it is either an expense under s 11(a) or private. (b) Cost R7,000 or less (per item, or per set that functions as one unit): full write-off in the year of acquisition under BGR 7. (c) Above R7,000: s 11(e) straight-line over the IN 47 useful life, apportioned for part-year use. (d) New or unused plant used in a process of manufacture: s 12C at 40/20/20/20 (used plant: 20% a year over five years). (e) Section 12E's 100% allowance on new manufacturing plant belongs to Small Business Corporations, which are companies and close corporations, not sole proprietors (Section 10.8).  _(s 11(e), s 12C, s 12E; SARS IN 47 (Issue 5, March 2023); BGR 7)_

### 6.7 Motor vehicle used in the trade

- **Vehicle costs** — *Rule:* A sole proprietor using a personal vehicle for trade deducts the business portion of the actual costs (fuel, repairs, insurance, finance interest, wear-and-tear on the vehicle) as shown by a logbook. The deemed-cost tables in the annual Government Gazette notice and the travel allowance rules of s 8(1)(b) belong to employees with a travel allowance and are outside scope. *Default:* 0% business use without a logbook. *Question:* "Do you have a logbook with date, destination, kilometres and purpose for each trip?"  _(s 11(a); SARS Guide for Employers in respect of Allowances)_

## Section 7 -- Excel working paper template

### Sheet "Transactions"

Columns: Date, Counterparty, Description, Amount (ZAR), Category (Revenue/Expense/Wear-and-tear/RA/Medical/EXCLUDE), Deductible amount, Default?, Question, Notes.

### Sheet "ITR12 Computation"

Step-by-step per Section 5: gross income, deductions, taxable income, tax, rebates, medical credits, provisional tax offset.

## Section 8 -- Bank statement reading guide

**CSV formats.** FNB exports use comma CSV with DD/MM/YYYY. Standard Bank uses semicolons. Nedbank and Absa offer various formats. Common columns: Date, Description, Amount, Balance.

**SA-specific patterns.** "DEBICHECK" = authenticated debit order. "MAGTAPE" = batch payment. "SASWITCH" = ATM network. "PREPAID" = likely personal (airtime top-up). "MUNICIPALITY" = rates and taxes.

**Provisional tax.** Two/three payments per year to SARS. These are tax payments, not expenses. EXCLUDE.

**Medical aid.** Monthly debits to Discovery/Bonitas/etc. These are NOT deductible from income -- they generate s6A credits against tax.

**RA contributions.** Monthly debits to Allan Gray/Coronation/etc. Deductible under s11F with cap.

## Section 9 -- Onboarding fallback

### 9.1 Age

- **Age** — *Inference:* Not inferable. Always ask. *Fallback:* "What is your age at 28 February 2027?"

### 9.2 Residency

- **Residency** — *Inference:* SA bank accounts suggest resident. *Fallback:* "Are you a South African tax resident?"

### 9.3 Business type

- **Business type** — *Inference:* From counterparty patterns. *Fallback:* "What is your trade/profession?"

### 9.4 Turnover tax election

- **Turnover tax election** — *Inference:* Not inferable. *Fallback:* "Have you elected turnover tax?"

### 9.5 Medical aid

- **Medical aid** — *Inference:* Monthly medical aid debits. *Fallback:* "Are you on medical aid? How many dependants?"

### 9.6 RA contributions

- **RA contributions** — *Inference:* Monthly RA debits. *Fallback:* "Do you contribute to a retirement annuity?"

### 9.7 Provisional tax paid

- **Provisional tax paid** — *Inference:* SARS payments in statement. *Fallback:* "What IRP6 amounts have you paid?"

## Section 10 -- Further rules and flags (added from the review of 2026-06-12)

The reviewer listed these as missing from the guide. Each is stated as a rule to apply or a trigger to flag, with the reviewer's citations; where a 2026/27 figure could not be confirmed against a SARS table on 2026-09-29 it says so.

### 10.1 CGT events

- **CGT triggers** — Sole proprietor work routinely produces CGT events: sale of business equipment, disposal of a vehicle, sale of the practice, sale of trade premises, cessation of trade with assets retained, and death. Flag a large CREDIT from a VEHICLE TRADER, AUCTION HOUSE or BUSINESS BUYER as "review for CGT". Individuals: inclusion rate 40%, so a maximum effective rate of 18% at the 45% marginal rate. The Eighth Schedule figures in force through 2025/26: annual exclusion R40,000 (R300,000 in the year of death); primary residence exclusion R2 million of gain (not of proceeds); small business exclusion (para 57) R1.8 million lifetime for a person aged 55 or older disposing of a small business with a market value up to R10 million. The review recorded Budget 2026 increases from 1 March 2026 (annual exclusion R50,000; year of death R440,000; primary residence R3 million; small business R2.7 million and R15 million): confirm them against the Eighth Schedule as amended and SARS's CGT tables before use.  _(Income Tax Act Eighth Schedule paras 5, 45 and 57; s 10(1)(zJ))_

### 10.2 Section 18A donations

- **s 18A deduction** — Cash or in-kind donations to an approved Public Benefit Organisation, public institution or conduit PBO are deductible up to 10% of taxable income (taxable income computed after the other deductions, s 11F included, and before s 18A); the excess carries forward. The donor must hold a valid s 18A receipt showing the PBO or PI number, the date, the amount or description, and the confirmation that the donation will be used solely for s 18A purposes. Since 1 March 2023 the PBO files IT3(d) returns and the donations are pre-populated on the donor's ITR12. Bank patterns: GIVENGAIN, BACKABUDDY, a named charity.  _(Income Tax Act s 18A; SARS Guide for Approved PBOs)_

### 10.3 Residential rental income

- **Rental income** — Rent from residential property is gross income of the individual. Deductible against it: bond interest (not capital), rates, levies, repairs (not improvements), insurance and agent commission. Patterns: CREDIT from "TENANT", "RENT", "PAYPROP", "RENT PROPERTY MANAGEMENT". A rental trade that runs at a loss may be ring-fenced under s 20A (Section 10.12).  _(Income Tax Act s 11(a), s 23(g), s 20A)_

### 10.4 Other income sources, spouse and dependants

- **Ask about every source** — Dividends (Section 10.21), rental (10.3), royalties, annuities, foreign income (10.15 and 10.16), capital gains (10.1) and the sale of a business all enter taxable income. Spouse status affects the medical credits (often combined), donations between spouses (Section 10.17), the primary residence exclusion (one per family unit) and other reliefs.  _(Income Tax Act s 6A, s 56; Eighth Schedule)_

### 10.5 Pre-trade expenditure (s 11A)

- **s 11A** — Expenditure incurred before the trade commenced is deductible in the year the trade starts, to the extent it would have been deductible under s 11 had the trade been carried on: market research, initial professional fees, the deductible part of lease deposits, opening stock, and similar. The deduction is limited to the income from that trade in the year, and the unused balance carries forward as an assessed loss. A common new-sole-proprietor issue.  _(Income Tax Act s 11A; SARS IN 51 (Issue 5))_

### 10.6 Legal expenses (s 11(c)) and restraint of trade (s 11(cA))

- **s 11(c)** — Legal expenses, arbitration costs included, actually incurred in respect of a claim, dispute or action at law arising in the course of trade or in connection with income are deductible: recovering a trade debt, defending a customer claim, a regulatory matter. Capital-nature legal costs (acquiring a business, defending title to a capital asset) are not.  _(Income Tax Act s 11(c); SARS IN 12)_
- **s 11(cA)** — A restraint-of-trade payment to a natural person, a labour broker or a personal service provider is deductible in equal annual instalments over the lesser of the restraint period and three years; the recipient includes it in gross income under para (cA). For a sole proprietor this arises when buying a practice or buying out a competitor.  _(Income Tax Act s 11(cA); para (cA) of the "gross income" definition)_

### 10.7 Research and development (s 11D) and energy efficiency (s 12L)

- **s 11D** — 150% deduction (100% plus 50%) for qualifying R&D expenditure, subject to pre-approval by the Department of Science and Innovation; sunset 31 December 2033. Rarely relevant to a typical sole proprietor, valuable for engineering, scientific and software work producing genuinely new technology.  _(Income Tax Act s 11D; SARS IN 50)_
- **s 12L** — 95 cents per kWh of verified energy savings, on SANEDI certification. A specialist claim for manufacturing and processing operations.  _(Income Tax Act s 12L; Regulations on the allowance for energy efficiency savings)_

### 10.8 Small Business Corporations (s 12E), a cross-reference

- **s 12E** — Only a company or close corporation can be a Small Business Corporation: gross income not above R20 million, all shareholders natural persons holding no interests in other companies, not a personal service provider, and not more than 20% of receipts from investment income or personal services. An SBC pays graduated rates and writes off new manufacturing plant at 100%. For the year of assessment ending in the twelve months to 31 March 2027: 0% to R99,000; 7% on the amount above R99,000 to R365,000; R18,620 + 21% above R365,000 to R550,000; R57,470 + 27% above R550,000. A sole proprietor weighing incorporation should weigh these against the 27% company rate and dividends tax.  _(Income Tax Act s 12E; SARS, Companies, trusts and small business corporations, 2027)_

### 10.9 Renewable energy (s 12B) and manufacturing plant (s 12C)

- **s 12B** — Plant and machinery used to generate renewable energy: solar PV below 1 MW is written off at 100% in the year it is brought into use (s 12B(1)(h)); solar PV of 1 MW or more, wind, hydro below 30 MW and biomass at 50/30/20 over three years. The temporary s 12BA 125% allowance for solar PV applied only to assets brought into use from 1 March 2023 to 28 February 2025 and has expired. A sole proprietor with a home office deducts only the business share (by the IN 28 floor-area ratio); the household share is private, and the business share is recouped on disposal, the sale of the house included.  _(Income Tax Act s 12B, s 12BA; SARS Renewable Energy Tax Incentive FAQ)_
- **s 12C** — New or unused plant and machinery used in a process of manufacture: 40% in the year of acquisition and 20% in each of the next three years; used plant 20% a year over five years. Recoupment under s 8(4)(a) on disposal to the extent of the allowances claimed. Workshops, food processing and light manufacturing qualify; consultants do not.  _(Income Tax Act s 12C; SARS IN 14)_

### 10.10 Learnership allowance (s 12H)

- **s 12H** — An employer, a sole proprietor with staff included, who enters into a registered learnership agreement with a SETA under the Skills Development Act claims an annual allowance (pro-rated for part of a year) and a completion allowance, in addition to the s 11(a) deduction for the learner's salary. For years of assessment ending on or after 1 March 2024: NQF levels 1 to 6, R40,000 annual plus R40,000 completion; NQF levels 7 to 10, R20,000 plus R20,000; a learner with a disability, R60,000 plus R60,000 (NQF 1 to 6) or R50,000 plus R50,000 (NQF 7 to 10). Requirements: registration with the SETA before commencement (or within 12 months of year-end), a learnership pursuant to the employer's trade, a formal employment contract, and the claim by the lead employer. Sunset 31 March 2027.  _(Income Tax Act s 12H; SARS IN 20 (Issue 9, April 2025); SARS Guide on the Tax Incentive for Learnership Agreements)_

### 10.11 Building allowances (s 13, 13quat, 13quin, 13sex)

- **Buildings** — s 13: 5% a year, straight-line, on new buildings used wholly or mainly for manufacturing, research or hotel operations. s 13quin: 5% on new commercial buildings (offices, retail, warehouses) for costs incurred from 1 April 2007. s 13sex: 5% (10% for low-cost units) on new and unused residential units, or improvements to them, owned by the taxpayer and let in a trade, where the taxpayer owns at least five such units; the cost basis is acquisition cost and the allowance is recouped on disposal. s 13quat (urban development zones) expired on 31 March 2025. All apportion for part-year use.  _(Income Tax Act s 13, s 13quat, s 13quin, s 13sex)_

### 10.12 Assessed losses (s 20) and ring-fencing (s 20A)

- **s 20** — An assessed loss from a trade carries forward and is set off against future income from any trade, provided the taxpayer carries on a trade in the year of set-off (s 20(2A)) or an exception applies. The 80%-of-taxable-income limit on set-off (greater of R1 million and 80%) applies to companies for years commencing on or after 1 April 2022, not to natural persons.  _(Income Tax Act s 20)_
- **s 20A** — Ring-fencing applies to a natural person whose taxable income before the set-off exceeds the top marginal threshold (R1,878,600 for 2026/27) who carries on a suspect trade (farming, animal showing, residential rental, sport, art, racing, gambling, dealing in collectibles, rental of vehicles, aircraft or boats) or a trade that showed losses in three of the last five years: the loss is set off only against future profits of that trade. Important for high-income sole proprietors with side activities.  _(Income Tax Act s 20A)_

### 10.13 Pre-paid expenses (s 23H) and contingent liabilities (s 23(e))

- **s 23H** — Where the benefit of a pre-paid expense extends more than six months after year-end, only the part relating to the current year is deductible and the rest is deferred, unless the aggregate of such pre-payments is R100,000 or less for the year. Annual subscriptions, insurance and rent paid in advance are the usual cases.  _(Income Tax Act s 23H)_
- **s 23(e)** — Provisions for warranties, leave pay, bonuses and other amounts not unconditionally due are not deductible until actually incurred; a sole proprietor working from accounting records adds the provisions back.  _(Income Tax Act s 23(e); Edgars Stores Ltd v CIR)_

### 10.14 Personal service provider detection

- **PSP** — A sole proprietor who incorporates and then serves one client in an employment-like relationship may have created a personal service provider under the Fourth Schedule: PAYE at 27% (45% for a trust) is deducted from its fees and its deductions are restricted under s 23(k) to the direct cost of the services, salaries, training, refunds, retirement fund contributions and premises costs. Indicators: the work is done mainly at the client's premises under the client's control, and the entity has three or fewer full-time employees.  _(Income Tax Act Fourth Schedule, definition of "personal service provider"; s 23(k); SARS Guide on Personal Service Providers)_

### 10.15 Tax residence

- **Resident** — A natural person is resident if ordinarily resident in South Africa (settled home, family, intentions) or if present for more than 91 days in the current year of assessment, more than 91 days in each of the five preceding years, and more than 915 days in aggregate over those five years. Residents are taxed on worldwide income, non-residents on South African-source income only. Ceasing residence triggers a deemed disposal under s 9H (the exit charge), immovable property in South Africa and a few other items excluded. Ask about time abroad and intentions.  _(Income Tax Act s 1 (definition of "resident"), s 9H; SARS IN 4 (Issue 5))_

### 10.16 Foreign tax credit (s 6quat)

- **s 6quat** — A resident credits foreign tax paid on foreign-source income against the South African tax attributable to that income; an excess carries forward for seven years, and s 6quat(1C) allows a deduction instead in limited cases (South African-source income taxed abroad). Common for foreign clients, foreign rental property and foreign dividends.  _(Income Tax Act s 6quat; SARS Guide on Foreign Tax Credits)_

### 10.17 Donations tax

- **Donations tax** — 20% of the value of property donated, on cumulative donations since 1 March 2018 up to R30 million, and 25% above that. The first R150,000 donated in a year of assessment by a natural person is exempt (raised from R100,000 with effect from 1 March 2026). Donations to a spouse, to an approved PBO and the other s 56 items are exempt; the review notes that Budget 2026 proposed limiting the spouse exemption to a spouse who is resident at the time of the donation, so confirm the current wording of s 56(1)(b). The donor files the IT144 declaration and pays by the end of the month following the month in which the donation takes effect; the donee is jointly liable if the donor does not pay. Transfers to family members or to a trust by a sole proprietor are the usual trigger.  _(Income Tax Act s 54 to s 64; SARS, Donations tax)_

### 10.18 Estate duty interaction

- **Estate duty** — Levied at 20% on the dutiable estate up to R30 million and 25% above, after the R3.5 million abatement (the unused part of which passes to a surviving spouse) and the s 4(q) deduction for bequests to a spouse. Business assets fall into the estate; life policies are deemed property under s 3(3) unless a key-person or buy-and-sell policy meets s 3(3)(a)(iA); future tax liabilities are deductible.  _(Estate Duty Act 45 of 1955 ss 3, 4, 4A; SARS, Estate duty)_

### 10.19 Tax-free investments (s 12T)

- **TFSA** — Contributions of up to R46,000 a year of assessment from 1 March 2026 (R36,000 for 2021 to 2026) and R500,000 over a lifetime; an unused annual limit is forfeited, returns inside the account are exempt, withdrawals do not restore the limits, and contributions above either limit are taxed at 40%. Available to any resident, sole proprietors included.  _(Income Tax Act s 12T; SARS, Tax-free investments)_

### 10.20 Attribution (s 7 and s 7C)

- **s 7** — Income arising from a donation, settlement or other disposition is taxed in the donor's hands where the split is tax-driven: s 7(2) for a donation to a spouse, s 7(3) and (4) for income applied for the benefit of a minor child, s 7(5) for a conditional donation, s 7(8) where the donor is non-resident. Splitting trade income with a spouse or minor children by gifting income-producing assets or making low-interest loans is caught.  _(Income Tax Act s 7)_
- **s 7C** — An interest-free or low-interest loan to a trust (or to a company owned by a trust) produces an annual deemed donation equal to the interest forgone, measured at the SARS official rate of interest (repo rate plus one percentage point; read the current rate from SARS's official-rate table).  _(Income Tax Act s 7C; SARS IN 96)_

### 10.21 Dividends and dividends tax

- **Dividends** — A dividend from a South African resident company (or a foreign company listed on the JSE) is exempt from income tax in the recipient's hands under s 10(1)(k); the company withholds dividends tax at 20% under s 64E to s 64N and the shareholder receives the net amount. Foreign dividends are not exempt but s 10B's partial exemption reduces the inclusion so that an individual's effective rate is at most 20%. A rental property held in a company pays out through dividends carrying the 20% tax.  _(Income Tax Act s 10(1)(k), s 10B, s 64E to s 64N)_

### 10.22 Skills Development Levy

- **SDL** — 1% of leviable payroll, paid monthly with PAYE and UIF on the EMP201, exempt where total annual payroll is below R500,000, and deductible under s 11(a). A sole proprietor without employees pays no SDL on their own drawings.  _(Skills Development Levies Act 9 of 1999; SARS, Skills Development Levy)_

### 10.23 Withholding taxes on payments to non-residents

- **Withholding** — A sole proprietor paying a non-resident may have to withhold and pay over to SARS by the end of the month after payment: 15% on royalties (s 49B, WTR return), 15% on South African-source interest (s 50B, WTI return; exemptions for government, bank and listed debt interest), 15% on payments to foreign entertainers and sportspersons (s 47B), and 7.5%, 10% or 15% of the price when buying immovable property from a non-resident seller (s 35A, withheld by the purchaser or conveyancer), each subject to the applicable DTA.  _(Income Tax Act s 35A, s 47A to s 47K, s 49A to s 49H, s 50A to s 50H)_

### 10.24 Trust distributions (s 25B)

- **Trusts** — A beneficiary of a discretionary trust is taxed on income the trust distributes in the year (the conduit principle, s 25B); income the trust retains is taxed in the trust at 45%; capital distributions follow para 80 of the Eighth Schedule; and s 7 can attribute distributed income back to the donor or settlor. Relevant wherever a sole proprietor's family structure involves a trust.  _(Income Tax Act s 25B, s 7; Eighth Schedule para 80)_

## Section 11 -- Reference material

### Test suite

**Test 1 -- Mid-range (2026/27 rates).** Age 35, R600K revenue, R180K expenses, R80K RA, medical R3,500/mo. Net tax R32,718.
**Test 2 -- Senior.** Age 68, R200K revenue, R50K expenses, R30K RA. Below threshold. R0 tax.
**Test 3 -- Turnover tax.** R650K turnover. Tax R500.
**Test 4 -- RA cap.** R2M taxable, R600K RA. Deduction R430,000. Excess carries forward.
**Test 5 -- Medical credits.** 6 members. R21,216/year credit (R376 x 2 + R254 x 4 = R1,768/mo x 12).
**Test 6 -- Under-estimation penalty.** R200K estimated, R450K actual. 20% penalty applies if estimate < 90% of actual (for income < R1,800,000 safe harbour threshold).

### Edge case registry

**EC1 -- Interest exemption.** R23,800 <65 / R34,500 65+. Excess taxable.
**EC2 -- Turnover tax + professional.** NOT eligible.
**EC3 -- RA exceeds cap.** Excess carries forward.
**EC4 -- Home office dual use.** NOT deductible. Where a home office does qualify, flag the CGT consequence on the residence (Section 5.10).
**EC5 -- Provisional under-estimation.** 20% penalty.
**EC6 -- Medical credits large family.** Compute per-member.
**EC7 -- Foreign income.** ESCALATE.
**EC8 -- Turnover tax exit mid-year.** Transition rules apply.
**EC9 -- Entertainment.** Sole proprietor entertainment is tested under s 11(a) and s 23(g); s 23(m) does NOT apply to sole proprietors.
**EC10 -- Assessed loss.** Carry forward under s 20; SARS may query. Ring-fencing under s 20A applies to a natural person whose taxable income before the set-off exceeds the top marginal threshold (R1,878,600 for 2026/27) and who carries on a suspect trade or one that showed losses in three of the last five years: the loss is then set off only against future profits of that trade (Section 10.12).

### Prohibitions

- NEVER compute without knowing age
- NEVER apply tax below age-threshold
- NEVER allow entertainment deductions without evidence of business purpose under s 11(a) and s 23(g)
- NEVER deduct RA above R430,000 cap
- NEVER allow turnover tax for professional services
- NEVER use prior year income for provisional tax (SA uses estimated current year)
- NEVER treat medical credits as income deductions
- NEVER allow home office for dual-use rooms
- NEVER claim home office without warning the client of the CGT consequence on disposal of the residence (Eighth Schedule para 47)
- NEVER allow income tax as a deduction
- NEVER present calculations as definitive

### Sources

1. Income Tax Act 58 of 1962 (with the Fourth, Sixth, Seventh and Eighth Schedules)
2. Tax Administration Act 28 of 2011
3. SARS, Rates of tax for individuals; Medical scheme fees tax credit rates; Turnover tax rates; Companies, trusts and small business corporations (the 2027 year-of-assessment tables, read 29 September 2026)
4. SARS Interpretation Notes: IN 28 (home office, Issue 3, March 2022); IN 47 (wear-and-tear, Issue 5, March 2023); IN 14 (allowances and reimbursements, Issue 4); IN 1 (provisional tax estimates); IN 33 (assessed losses); IN 4 (resident, Issue 5); IN 12 (legal expenses); IN 51 (pre-trade expenditure, Issue 5); IN 96 (s 7C)
5. SARS Binding General Rulings: BGR 7 (small-value assets); BGR 9 (utility apportionment); BGR 24 (allowances and reimbursements)
6. SARS eFiling -- https://www.sarsefiling.co.za; SARS -- https://www.sars.gov.za

### Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a registered tax practitioner, CA(SA), or equivalent licensed practitioner in South Africa) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

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
