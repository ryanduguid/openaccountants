---
name: se-corporate-income-tax
description: >
  Sweden corporate income tax reference for an ordinary resident aktiebolag
  with a calendar financial year in 2026. Covers the 20.6% rate, accounting
  reconciliation, depreciation, interest, pensions, reserves, losses, conditional
  credits, preliminary tax and INK2 filing. Trigger on Swedish company tax,
  bolagsskatt, aktiebolag tax, Inkomstdeklaration 2 or Swedish corporate losses.
  Includes a fictional computation and screens for withholding, transfer pricing,
  CFC, DAC6 and Pillar Two. Requires the corporate workflow base and actual
  supporting records. This Tier 2 draft awaits professional review; specialist
  calculations and filing readiness remain subject to explicit holds.
jurisdiction: SE
category: international
tax_year: 2026
tax_year_notes: "Ordinary resident AB; calendar financial year 1 January to 31 December 2026. Primary sources retrieved by 1 November 2026; future filing service availability and taxpayer-specific positions require confirmation."
tier: 2
last_updated: 2026-11-02
version: 0.4
review_status: pending_review
depends_on:
  - corporate-income-tax-workflow-base
  - workflow-base
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Sweden Corporate Income Tax: Ordinary Resident Aktiebolag, 2026 v0.4

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Use this guide to prepare a supported tax reconciliation for an ordinary Swedish resident aktiebolag (AB) with a financial year from 1 January to 31 December 2026. Load `corporate-income-tax-workflow-base` and `workflow-base`: their intake, outputs, checks and canonical refusal messages apply in full. This guide fills all 9 country sections; a populated section does not establish that every transaction is covered.

**Status:** Tier 2, pending professional review. A worked example is illustrative. No actual taxpayer calculation, election, filing or payment has been approved. A missing fact or unresolved applicable rule requires **Needs Input**; do not replace it with zero or a convenient assumption.

The ordinary computation below requires a solvent resident AB, an established accounting framework, completed accounts and a verified calendar financial year. Swedish legal persons' tax year generally follows their financial year; a Swedish legal person is generally subject to unlimited tax liability for Swedish and foreign income. Residence, treaty relief and a foreign permanent establishment still need their own analysis. [IL, 1:15 and 6:3–4](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json)

## Ask the client first

The following 5 questions group the records needed for this guide. They do not replace any of the 26 mandatory foundation fields.

1. What are the registered entity, residence, actual financial year and accounting framework, and which foundation refusal triggers fire?
2. Where are the signed accounts, trial balance, book profit before and after tax, prior returns, assessments, preliminary decisions and tax account postings?
3. What do the asset, inventory, debt, leasing, pension and reserve records establish, including dates, bases, agreements and vintages?
4. What do ownership and loss histories, related-party transactions, foreign tax records, gift approvals and receipts establish?
5. What are the group revenue, reporting roles and elections, actual filing service, attachment route and signatory rights?

The 26 foundation intake fields remain mandatory. Also obtain the registration and residence analysis; signed accounts and trial balance; book profit before and after current income tax; prior returns and assessments; preliminary tax decisions and tax account transactions; fixed asset and inventory registers; interest and leasing schedules; pension agreements and payments; reserve vintages; ownership and loss history; related-party transactions; foreign tax evidence; gift receipts and recipient approvals; and group revenue, reporting roles and elections. Confirm an item is absent from the records before treating its value as zero.

## The method, step by step

### [REGIME IDENTIFICATION] [Official source](https://data.riksdagen.se/dokumentstatus/sfs-2011-1244.json)

| Item | Ordinary calendar 2026 AB |
| --- | --- |
| Jurisdiction | SE; an aktiebolag is a legal person. Entity classification must be established, rather than inferred from a business name. [IL, 6:3–4](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) |
| Main law | Inkomstskattelagen (1999:1229), abbreviated IL; Skatteförfarandelagen (2011:1244), abbreviated SFL. Accounts follow the applicable accounting law and framework. [IL](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) [SFL](https://data.riksdagen.se/dokumentstatus/sfs-2011-1244.json) [ÅRL](https://data.riksdagen.se/dokumentstatus/sfs-1995-1554.json) |
| Authority | Skatteverket; use its [company return guidance](https://www.skatteverket.se/foretag/inkomstdeklaration/deklareraatettaktiebolagellerenekonomiskforening/saharlamnarduinochfylleriinkomstdeklarationen.4.262c54c219391f2e96322d7.html) to reach the authorised service. |
| Ordinary return | Inkomstdeklaration 2 (INK2), including INK2R accounts and INK2S tax adjustments, plus applicable schedules. [Skatteverket](https://www.skatteverket.se/foretag/inkomstdeklaration/deklareraatettaktiebolagellerenekonomiskforening/saharlamnarduinochfylleriinkomstdeklarationen.4.262c54c219391f2e96322d7.html) |
| Statutory filing date | For a 31 December 2026 year end, 1 July 2027 under SFL 32:2. A qualifying wholly electronic return has an extra month under 32:2, second paragraph; 1 August 2027 is a Sunday, so the adjusted date is **2 August 2027**. All parts, including accounts and attachments, must satisfy the electronic condition. [SFL](https://data.riksdagen.se/dokumentstatus/sfs-2011-1244.json) [Holiday rule, 2 §](https://data.riksdagen.se/dokumentstatus/sfs-1930-173.json) [Skatteverket filing guidance](https://www4.skatteverket.se/rattsligvagledning/edition/2026.14/325640.html) |
| Extension | Obtain an actual extension decision where applicable. Legal persons need the exceptional grounds in SFL 36:4; do not assume an adviser or bureau extension. [SFL](https://data.riksdagen.se/dokumentstatus/sfs-2011-1244.json) |
| Preliminary tax | Follow the current F-tax decision. For an ordinary full-year decision, equal monthly instalments run from the tax year's second month to the month after it ends. The statutory dates are normally the 12th, and the 17th in January and August; the August date is the 12th for the specified VAT taxable base over SEK 40 million. Late or changed decisions have separate allocation rules. Apply the business-day rule and actual decision. [SFL, 62:4–7](https://data.riksdagen.se/dokumentstatus/sfs-2011-1244.json) [Holiday rule](https://data.riksdagen.se/dokumentstatus/sfs-1930-173.json) |
| Final payment | Separate the return date from the tax account due date. The statutory final balance date is the first specified due date after 90 days from the final tax decision; use the actual notice, posting and interest rules. Payment counts when posted to the tax account. [SFL, 62:2 and 62:8, ch. 65](https://data.riksdagen.se/dokumentstatus/sfs-2011-1244.json) |

Reconcile the preliminary tax credited in the assessment with both the decision and actual tax account payments. Debited preliminary tax is not evidence that cash was paid. Interest may start before the final payment date. Current guidance for a December 2026 year end gives 12 February 2027 for the portion over SEK 30,000 and 3 May 2027 for the remaining portion to avoid cost interest. These are interest avoidance dates, not the filing deadline or a substitute for the final notice. Verify the actual balance and then-current interest rate. [SFL, chs. 56, 62 and 65](https://data.riksdagen.se/dokumentstatus/sfs-2011-1244.json) [Skatteverket company guidance](https://www.skatteverket.se/foretag/drivaforetag/foretagsformer/aktiebolag.4.5c13cb6b1198121ee8580002546.html)


**Governing source wording.** Read dates are the recorded selected readings; apply the conditions and version limits above.

| Figure or rule | Exact official wording | Read on | Source |
| --- | --- | --- | --- |
| Ordinary and electronic filing dates | '2 § Andra juridiska personer än dödsbon ska lämna inkomstdeklaration för ett beskattningsår enligt följande uppställning: Om beskattningsåret går ska deklaration ha kommit in ut den senast den 31 december 1 juli 30 april 1 november 30 juni 15 december 31 augusti 1 mars Den som lämnar inkomstdeklaration elektroniskt får lämna deklaration en månad senare än vad som följer av första stycket.' | 2026-11-01 | [SFL 32:2](https://data.riksdagen.se/dokumentstatus/sfs-2011-1244.json) |
| F-tax instalments, 12th/17th and SEK 40m branch | 'Huvudregeln 4 § F-skatt och särskild A-skatt ska betalas med lika stora belopp varje månad. Betalning ska göras från och med beskattningsårets andra månad till och med månaden efter beskattningsårets utgång. Förfallodagarna är - den 17 i januari och augusti, och - den 12 i övriga månader. I augusti är förfallodagen dock den 12 för den som redovisar mervärdesskatt på beskattningsunderlag som exklusive unionsinterna förvärv och import för beskattningsåret beräknas sammanlagt överstiga 40 miljoner kronor.' | 2026-11-01 | [SFL 62:4](https://data.riksdagen.se/dokumentstatus/sfs-2011-1244.json) |
| Final balance, first specified date after 90 days | '8 § Slutlig skatt beräknad enligt 56 kap. 9 § och skatt beräknad enligt 56 a kap. 5 eller 6 § ska betalas senast den förfallodag som infaller närmast efter det att 90 dagar har gått från den dag då beslut om slutlig skatt eller beslut om tilläggsskatt fattades.' | 2026-11-01 | [SFL 62:8](https://data.riksdagen.se/dokumentstatus/sfs-2011-1244.json) |
| Deadline next-business-day rule | 'Infaller den tid, då enligt lag eller särskild författning en åtgärd senast ska vidtas, på en söndag, annan allmän helgdag, lördag, midsommarafton, julafton eller nyårsafton, får åtgärden vidtas nästa vardag.' | 2026-11-01 | [Time computation Act (1930:173), 2 §](https://data.riksdagen.se/dokumentstatus/sfs-1930-173.json) |
| Final-tax interest and SEK 30,000 timing rule | 'På debiterad preliminär skatt som ska betalas den 12 i andra månaden efter beskattningsåret eller senare beräknas inte kostnadsränta från och med den 13 i andra månaden efter beskattningsåret till och med den 3 i femte månaden efter beskattningsåret på belopp till och med 30 000 kronor. Detsamma gäller slutlig skatt som ska betalas.' | 2026-11-01 | [SFL 65:4, second paragraph](https://data.riksdagen.se/dokumentstatus/sfs-2011-1244.json) |
| Interest start dates and weekend shifts | '18 § Om den 12 i andra månaden efter beskattningsåret är en lördag eller söndag, ska ränta som ska beräknas från och med den 13 i den månaden i stället beräknas från och med närmast följande tisdag. Om den 3 i femte månaden efter beskattningsåret är en lördag eller söndag, ska ränta som ska beräknas från och med den 4 i den månaden i stället beräknas från och med närmast följande tisdag. Om den 12 i femtonde månaden efter beskattningsårets utgång är en lördag eller söndag, ska ränta som ska beräknas från och med den 13 i den månaden i stället beräknas från och med närmast följande tisdag. Lag (2023:880).' | 2026-11-01 | [SFL 65:18](https://data.riksdagen.se/dokumentstatus/sfs-2011-1244.json) |

### [RATES] [Official source](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json)

| Item | Rate or treatment | Tax year | Official URL |
| --- | --- | --- | --- |
| Ordinary national corporate income tax | **20.6%** of taxable business income for the scoped year; IL 65:10. The transition applies this rate to tax years starting after 31 December 2020. Do not use the earlier 21.4% period. [IL and SFS 2018:1206 transition, points 2 and 11](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) | 2026 | https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json |
| Ordinary small AB | The same IL 65:10 rate applies. The ordinary rate provision does not give a separate small-company band. [IL](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) | 2026 | https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json |
| Ordinary regional surcharge | No regional surcharge is included in this national ordinary AB computation. An actual sectoral levy or other tax needs its own basis and source. [IL, 65:10](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) | 2026 | https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json |
| Pension payroll tax | Separate **24.26%** charge on the statutory pension cost base; it is not an additional 24.26% of taxable business profit. See pensions below. [SLP, 1–2 §§](https://data.riksdagen.se/dokumentstatus/sfs-1991-687.json) | 2026 | https://data.riksdagen.se/dokumentstatus/sfs-1991-687.json |
| Activity, IP, R&D or investment incentives | No reduced income tax rate or credit for these activities has been qualified by this guide. Hold any claim pending its legislation, eligibility and period analysis; do not infer that no other support exists. | 2026 | unverified: no rate qualified for this outside-scope or held branch |
| Branch profits or remittance tax | Outside the resident AB scope. No branch rate or treaty result is supplied. | 2026 | unverified: no rate qualified for this outside-scope or held branch |
| Pillar Two | A separate conditional top-up system, screened below. A 20.6% headline rate does not establish a 15% jurisdictional effective rate. [Top-up Tax Act, chs. 1–2](https://data.riksdagen.se/dokumentstatus/sfs-2023-875.json) | 2026 | https://data.riksdagen.se/dokumentstatus/sfs-2023-875.json |

For the ordinary AB, determine net business income and round taxable income **down to a full SEK 10** under IL 1:7 before applying 65:10. Do not impose an unsupported additional rounding convention on individual adjustments or the tax assessment. A deficit is tracked under the loss rules, not multiplied into a negative current tax refund. [IL, 1:7, 40:2 and 65:10](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json)


**Governing source wording.** Read dates are the recorded selected readings; apply the conditions and version limits above.

| Figure or rule | Exact official wording | Read on | Source |
| --- | --- | --- | --- |
| SEK 10 taxable-income rounding | 'Det återstående beloppet avrundas nedåt till helt tiotal kronor och är den fastställda och den beskattningsbara inkomsten.' | 2026-11-01 | [IL 1:7](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) |
| 20.6% ordinary rate | '10 § För juridiska personer är den statliga inkomstskatten 20,6 procent av den beskattningsbara inkomsten. Lag (2018:1206).' | 2026-11-01 | [IL 65:10](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) |
| SLP 24.26% | '1 § Den som utfäst en tjänstepension skall till staten betala särskild löneskatt med 24,26 procent på kostnaden för pensionsutfästelsen, beräknad enligt 2 §. Lag (1997:941).' | 2026-11-01 | [SLP 1 §](https://data.riksdagen.se/dokumentstatus/sfs-1991-687.json) |
| 21.4% transition ends before 2021 start years | '11. Vid tillämpning av 65 kap. 10 § i den nya lydelsen ska avseende beskattningsår som börjar efter den 31 december 2018 men före 1 januari 2021 för juridiska personer den statliga inkomstskatten vara 21,4 procent av den beskattningsbara inkomsten i stället för 20,6 procent.' | 2026-11-01 | [SFS 2018:1206, transition point 11](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) |

### [ADJUSTMENTS] [Official source](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json)

#### Reconcile the accounts once

Tax timing generally follows accrual accounting and good accounting practice unless IL supplies a different rule. Establish the applicable accounting framework; do not assume that every small AB may use K2. ÅRL governs the annual report, and BFN's current guidance identifies K2 exclusions and changed application dates for financial years starting after 31 December 2025. For the specified new companies, the same list also applies where the first financial year starts after 30 June 2025 and ends on 31 December 2026 or later. The list's entity/activity and relief conditions remain essential. Actual framework eligibility and the complete BFNAR requirements remain to be verified. [IL, 14:2–5](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) [ÅRL, chs. 1–2](https://data.riksdagen.se/dokumentstatus/sfs-1995-1554.json) [BFN](https://www.bfn.se/fragor-och-svar/arsredovisning/)

1. Start the computation from approved **profit before current income tax**. If starting instead from INK2R's booked net profit or loss, bridge to that starting point by adding back booked Swedish current income tax and resolving any deferred tax entries. Do not add the same tax twice.
2. Add expenses disallowed by tax law and taxable income omitted from book profit.
3. Remove exempt book income and amounts taxable in another period, and replace book depreciation or other timing items with the supported tax amount.
4. Reconcile booked and tax group contributions, reserve releases and provisions. Do not duplicate a contribution or reserve already included in the starting result.
5. Apply reserve, interest and restricted-loss rules in their statutory order. Keep separate schedules for each pool and vintage.
6. Calculate the taxable surplus or deficit, ordinary tax, conditional relief and separate taxes. Reconcile the tax account and produce the foundation outputs, including unresolved items and the reviewer brief.

Each row of the reconciliation needs the book entry, sign, amount, applicable provision, tax period and evidence reference. The underlying rules are IL chs. 9 and 14–16 and the specific provisions below. [IL](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json)

#### Common permanent and timing differences

| Item | Ordinary treatment and required condition |
| --- | --- |
| General Swedish income tax | Non-deductible; reconcile booked current and deferred tax separately. Certain business-related special taxes are deductible under IL 16:17, with an adjustment if reduced. Do not disallow every levy as income tax. [IL, 9:4–5 and 16:17](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) |
| Gifts, fines, bribes and membership charges | Apply the specific disallowances in IL ch. 9, including gifts and fines. Separate an otherwise deductible service payment from a non-deductible membership fee. A qualifying gift credit does not make the gift deductible. [IL, 9:2 and 9–10](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) |
| Representation and mixed expenditure | Establish the business connection, type and statutory limit before deducting; no unverified standard allowance is provided. [IL, 16:1–2](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) |
| Dividends and share disposals | Test business-related share status and all exceptions; see below. Taxable and exempt share classes must not share an undifferentiated loss pool. [IL, 24:32–42 and ch. 25a](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) |
| Inventory | Apply the statutory lower-value rules and the imported ÅRL definitions. The alternative 97% of aggregate acquisition cost has asset exclusions; it is not a blanket 3% deduction from every inventory value. The 97% fixed-price work rule is limited to qualifying building, civil engineering and craft work. [IL, 17:2–4 and 27](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) [ÅRL, 4:9](https://data.riksdagen.se/dokumentstatus/sfs-1995-1554.json) |
| Property and capital losses | Separate taxable gains, depreciation recapture and ring-fenced property losses. IL ch. 26 can recapture specified repair costs from the disposal year and the preceding 5 tax years; do not net all property entries into an ordinary trading loss. [IL, 25:12 and ch. 26](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) |

**Business-related shares:** for a qualifying owner and capital asset, IL 24:32–33 can cover an unlisted share, a holding of at least 10% of votes or a holding related to the owner's business. These are alternative routes, not a universal 10% exemption. Listed-share holding periods, foreign entity equivalence, EU conditions, deductible dividends, hybrids and shell-company rules can alter the result. Exempt gains generally imply non-deductible losses under IL 25a:5, but read the full exceptions. Taxable shell-company treatment does not by itself make the corresponding loss deductible. This guide does not qualify an actual foreign share or treaty claim. [IL, 24:32–42 and 25a:5, 9 and 23a](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json)

#### Depreciation and asset basis

Maintain an opening tax basis, additions, disposals, insurance recoveries, book depreciation and closing tax basis for each asset class. A purchase cost is not automatically a tax deduction.

| Asset or method | Qualified rule |
| --- | --- |
| Low-value or short-life equipment | Immediate deduction can apply where acquisition value is **strictly below half the applicable price base amount**, excluding VAT, or economic life is at most 3 years. Aggregate connected acquisitions. The immediate rule does not cover the acquired rights excluded by IL 18:4. The 2026 ordinary price base amount is **SEK 59,200**, so the low-value route requires a value **below SEK 29,600**, rather than at that amount. Do not substitute the higher statutory price base amount used for other purposes. [IL, 2:27 and 18:3–4](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) [2026 price-base ordinance, 1 §](https://data.riksdagen.se/dokumentstatus/sfs-2025-872.json) |
| Equipment, book-conforming method | IL 18:13 permits up to 30% of the statutory basis; 18:14 requires orderly closed accounts and correspondence with book depreciation. The complementary rule in 18:17 can permit the acquisition cost less 20% for each elapsed year. Use the method's actual conditions and a reconciliation, not both deductions. [IL, 18:13–17](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) |
| Equipment, residual-value method | Up to 25% of the tax residual basis under IL 18:13. The basis includes the prescribed opening value and qualifying current-year assets still held at year end, less the specified deductions for disposals and related events. Short or long years require proportional adjustment. [IL, 18:13 and 15–16](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) |
| Buildings | Deduct by the statutory plan based on economic life, with separate repairs and improvements. No universal building percentage is qualified here. The conditional primary deduction for buildings classified as hyreshus is 12% over 6 years, 2 percentage points a year, subject to completion dates and remaining-period rules. [IL, 19:2–5a; SFS 2018:1206, point 3](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) |
| Land improvements | The statutory categories include 10% for qualifying drainage and forest roads and 5% for other qualifying improvements. Land itself is not this depreciable asset. [IL, 20:4–5](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) |
| Entry into Swedish taxation | IL ch. 20a has separate entry-value rules. Its percentages do not replace the ordinary annual depreciation rules. [IL](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) |

#### Interest and finance leases

First identify interest and equivalent amounts under IL ch. 24 and apply targeted related-party and other specific denials. The amended related-party provisions in IL 24:18, 19a and 20 apply first to financial years starting after 31 December 2025. Apply the actual debt, counterparty, commercial reason and legal tests; a group loan is neither automatically deductible nor automatically denied. [IL, 24:2–20](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) [SFS 2025:1333](https://svenskforfattningssamling.se/sites/default/files/sfs/2025-11/SFS2025-1333.pdf)

The general negative net interest rule allows the statutory **30% deduction basis** route or the alternative ceiling of **SEK 5 million**, shared across the relevant statutory group. The basis is the tax-law computation, not accounting EBITDA. Apply the group definitions, allocation, loss and reserve interactions in IL 24:21–29. Qualifying disallowed negative net interest can carry forward for **6 years**, with current-year and ordering rules; the carryforward does not preserve every targeted denial or an amount excluded under the simplified ceiling. Ownership changes can extinguish it. [IL](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json)

Finance leases require IL ch. 24a's classification and interest computation where applicable. The exception for aggregate leasing charges below **SEK 1 million** for the company and relevant statutory group is a conditional scope rule, not an extra interest allowance. Hybrids under ch. 24b need their own screen before a deduction. Do not issue a final interest deduction without the complete calculation and group allocation. [IL, chs. 24a–24b](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json)

#### Pensions and the separate payroll tax

For the ordinary pension deduction, verify the employee, pensionable remuneration under the agreement, permitted pension arrangement and actual secured cost. IL 28:5 limits the ordinary deduction per employee to **35%** of that remuneration for the current or preceding tax year, with a maximum of **10 price base amounts**. Use the price base amount for the calendar year in which the tax year ends: the scoped 2026 maximum is **SEK 592,000**, using the ordinary **SEK 59,200** amount. This maximum does not override the lower remuneration limit or establish a deductible cost. The deduction also depends on the permitted security method and its particular conditions. [IL, 2:27 and 28:2–6, 13–15](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) [2026 price-base ordinance, 1 §](https://data.riksdagen.se/dokumentstatus/sfs-2025-872.json)

The complementary rule for specified early retirement or insufficiently secured promises requires the statutory benefit, service, prior security and offset calculations. It is not an unrestricted catch-up allowance. Transfers, reimbursements, provision releases and cessation have separate rules. Pension insurance must satisfy the applicable IL ch. 58 conditions; this guide does not qualify historic changes to a policy. [IL, 28:7–12 and 16–26; ch. 58](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json)

Compute special payroll tax on pension costs separately under lag (1991:687), abbreviated SLP. The **24.26%** rate applies to its statutory additions less deductions; a premium disallowed under the income tax pension ceiling can still enter that base. Use accrual timing and all applicable items. A negative base reduces the following year's base under the statute, rather than creating an immediate refund. Item j is a reduction using **85%** of the qualifying opening provision and the average government borrowing rate for the calendar year before the tax year begins, floored at zero. For the scoped calendar 2026 year, that average is **2.36%** for 2025 under SKV A 2026:1. Apply the year-length adjustment and the adjustment if the provision is fully released during the year. Do not apply this formula to every pension cost. Current SLP is generally deductible as a business tax, but a provision for future SLP is not thereby deductible. [SLP, 1–3 §§](https://data.riksdagen.se/dokumentstatus/sfs-1991-687.json) [IL, 16:17](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) [SKV A 2026:1](https://www4.skatteverket.se/rattsligvagledning/edition/2026.14/468722.html) [Skatteverket pensions guidance](https://www.skatteverket.se/foretag/drivaforetag/foretagsformer/aktiebolag/sarskildloneskatt.4.6e8a1495181dad540843a8.html)

#### Periodisation funds

A legal person's deduction for a periodiseringsfond requires the corresponding provision in its accounts and is capped at **25%** of the statutory pre-deduction business surplus. Each tax year's fund is separate. Include the deemed income on opening funds using the government borrowing rate at the end of November in the year before the calendar year in which the tax year ends, subject to a **0.5% floor** and year-length adjustment. For the scoped calendar 2026 year, use the end-November 2025 rate of **2.55%**, which exceeds that floor. This is different from the **2.36%** annual average used for the pension provision item above. [IL, 30:3, 5–6a](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) [Skatteverket reference-rate table](https://www4.skatteverket.se/rattsligvagledning/edition/2026.14/341469.html)

Release a fund no later than the **6th tax year after the deduction**, applying the oldest-first rule and earlier release triggers. Maintain original deduction years and any lawful succession. For a release in a tax year starting after 31 December 2020, the transition scales deductions from years starting before 1 January 2019 to **106%**, and those from years starting after 31 December 2018 but before 1 January 2021 to **104%**. Do not apply these multipliers to all funds or assume an old balance remains lawful in 2026. [IL, 30:7–10a; SFS 2018:1206, point 5](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json)


**Governing source wording.** Read dates are the recorded selected readings; apply the conditions and version limits above.

| Figure or rule | Exact official wording | Read on | Source |
| --- | --- | --- | --- |
| 97% inventory alternative | '4 § Lagret får tas upp till lägst 97 procent av lagertillgångarnas sammanlagda anskaffningsvärde. Detta gäller dock inte lager av 1. fastigheter och liknande tillgångar, 2. aktier, obligationer, lånefordringar och liknande tillgångar, 3. elcertifikat, samt 4. utsläppsrätter, utsläppsminskningsenheter och certifierade utsläppsminskningar. Lag (2006:620).' | 2026-11-01 | [IL 17:4](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) |
| 97% qualifying fixed-price work | '27 § Pågående arbeten som utförs till fast pris och som inte har slutredovisats får inte tas upp till ett lägre värde än det lägsta av anskaffningsvärdet och nettoförsäljningsvärdet. För byggnads-, anläggnings- och hantverksrörelse får de pågående arbetena trots bestämmelserna i första stycket tas upp till lägst 97 procent av det sammanlagda anskaffningsvärdet. Lag (2003:1102).' | 2026-11-01 | [IL 17:27](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) |
| Property repair recapture, prior 5 years | '5. avdrag som avser beskattningsåret och de fem föregående beskattningsåren för utgifter för förbättrande reparationer och underhåll av byggnader och markanläggningar.' | 2026-11-01 | [IL 26:2](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) |
| 10% voting-share route | '33 § Andelen ska vara en kapitaltillgång och uppfylla någon av följande förutsättningar: 1. Andelen är inte marknadsnoterad. 2. Det sammanlagda röstetalet för ägarföretagets samtliga andelar i det ägda företaget motsvarar tio procent eller mer av röstetalet för samtliga andelar i företaget. 3. Innehavet av andelen betingas av rörelse som bedrivs av ägarföretaget eller av ett företag som med hänsyn till äganderättsförhållanden eller organisatoriska förhållanden kan anses stå det nära.' | 2026-11-01 | [IL 24:33](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) |
| Short life 3 years and below half PBB | '4 § För inventarier som är av mindre värde eller kan antas ha en ekonomisk livslängd på högst tre år, får hela utgiften dras av omedelbart. Detta gäller dock inte sådana rättigheter m.m. som avses i 1 § andra stycket. Med mindre värde avses att anskaffningsvärdet exklusive mervärdesskatt understiger ett halvt prisbasbelopp. Finns det ett naturligt samband mellan flera inventarier, ska de anses vara inventarier av mindre värde bara om det sammanlagda anskaffningsvärdet understiger ett halvt prisbasbelopp. Detsamma gäller i det fall förvärv av olika inventarier kan anses ingå som ett led i en större inventarieanskaffning. Lag (2009:547).' | 2026-11-01 | [IL 18:4](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) |
| 2026 ordinary price base SEK 59,200 | '1 § Prisbasbeloppet och det förhöjda prisbasbeloppet enligt 2 kap. 6-8 §§ socialförsäkringsbalken ska vara 59 200 kronor respektive 60 500 kronor för år 2026.' | 2026-11-01 | [SFS 2025:872, 1 §](https://data.riksdagen.se/dokumentstatus/sfs-2025-872.json) |
| 30% and 25% equipment depreciation | '13 § Värdeminskningsavdrag får för ett visst beskattningsår göras vid räkenskapsenlig avskrivning med högst 30 procent och vid restvärdesavskrivning med högst 25 procent per år av avskrivningsunderlaget.' | 2026-11-01 | [IL 18:13](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) |
| 20% complementary depreciation | '17 § Oavsett vad som föreskrivs i 13, 15 och 16 §§ får vid räkenskapsenlig avskrivning dras av ett så högt belopp att det skattemässiga värdet inte överstiger anskaffningsvärdet av inventarierna minskat med en beräknad årlig avskrivning med 20 procent. Avdraget får göras särskilt för varje sådant slag av inventarier som avses i 1 § första stycket, andra stycket 1 respektive andra stycket 2.' | 2026-11-01 | [IL 18:17](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) |
| 12% primary building deduction over 6 years | '5 a § För en byggnad som indelas som hyreshus ska värdeminskningsavdrag även göras med tolv procent av utgifterna för ny-, till- eller ombyggnad (primäravdrag). Primäravdrag ska göras inom avskrivningsplanen och beräknas från den tidpunkt då hyreshuset eller den till- eller ombyggda delen av hyreshuset färdigställs. Avdragen ska fördelas med två procentenheter per år under sex år från färdigställandet. Om ett hyreshus förvärvas genom köp, byte eller på liknande sätt inom sex år från det att hyreshuset färdigställts, ska primäravdrag göras för den delen av sexårsperioden från färdigställandet som återstår vid förvärvet. Ett sådant avdrag beräknas från den tidpunkt då hyreshuset förvärvas och på förvärvarens anskaffningsvärde. Lag (2018:1206).' | 2026-11-01 | [IL 19:5a](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) |
| 10% and 5% land-improvement limits | '5 § Värdeminskningsavdragen ska beräknas enligt avskrivningsplan till högst tio procent per år av anskaffningsvärdet för täckdiken och skogsvägar och till högst fem procent per år av anskaffningsvärdet för andra markanläggningar. Beräkningen ska göras från den tidpunkt då anläggningen färdigställs. Lag (2007:1419).' | 2026-11-01 | [IL 20:5](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) |
| 30% interest route or shared SEK 5m ceiling | '24 § Ett företag får bara dra av ett negativt räntenetto med högst 30 procent av avdragsunderlaget (avdragsutrymmet). Ett negativt räntenetto får, i stället för vad som sägs i första stycket, dras av upp till fem miljoner kronor. Om företaget ingår i en intressegemenskap, får de sammanlagda avdragen för negativa räntenetton inom intressegemenskapen då inte överstiga fem miljoner kronor.' | 2026-11-01 | [IL 24:24](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) |
| 6-year qualifying interest carryforward | '26 § Ett företag som enligt 24 § första stycket eller 25 a § inte har kunnat dra av ett tidigare beskattningsårs negativa räntenetto i sin helhet får dra av återstående del (kvarstående negativt räntenetto) högst med ett belopp som motsvarar avdragsutrymmet, minskat med avdrag för negativt räntenetto enligt 24 §. Avdrag ska göras inom sex år efter det beskattningsår då det kvarstående negativa räntenettot uppkom. Ett tidigare uppkommet kvarstående negativt räntenetto ska dras av före ett senare uppkommet sådant. Lag (2020:1077).' | 2026-11-01 | [IL 24:26](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) |
| Finance leases below SEK 1m | '2 § Bestämmelserna i detta kapitel tillämpas inte om de sammanlagda leasingavgifter som företaget, eller företag som ingår i samma intressegemenskap, har för finansiella leasingavtal är mindre än en miljon kronor för beskattningsåret. Lag (2018:1206).' | 2026-11-01 | [IL 24a:2](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) |
| Pension 35% and 10 price base amounts | '5 § Tryggande av sådana pensionsutfästelser som avses i 3 § ska dras av som kostnad. Avdraget får dock inte för någon arbetstagare överstiga 35 procent av lönen och inte heller 10 prisbasbelopp. Lag (2007:1419). 6 § Som lön räknas vid tillämpning av detta kapitel sådan pensionsgrundande ersättning enligt pensionsavtal som hänför sig till beskattningsåret eller det föregående beskattningsåret.' | 2026-11-01 | [IL 28:5–6](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) |
| SLP provision item j 85% and zero floor | 'j) 85 procent av avsättning under rubriken Avsatt till pensioner enligt lagen om tryggande av pensionsutfästelse m.m. eller i sådan delpost som avses i 8 a § samma lag vid beskattningsårets ingång multiplicerad med den genomsnittliga statslåneräntan under kalenderåret närmast före ingången av beskattningsåret, dock lägst 0 procent,' | 2026-11-01 | [SLP 2 §, item j](https://data.riksdagen.se/dokumentstatus/sfs-1991-687.json) |
| 2025 average rate 2.36% | 'Den genomsnittliga statslåneräntan under år 2025 bör anses vara 2,36 procent.' | 2026-11-01 | [SKV A 2026:1](https://www4.skatteverket.se/rattsligvagledning/edition/2026.14/468722.html) |
| 2026 application of the average-rate advice | 'Dessa allmänna råd tillämpas för beskattningsår som påbörjats under år 2026.' | 2026-11-01 | [SKV A 2026:1, application](https://www4.skatteverket.se/rattsligvagledning/edition/2026.14/468722.html) |
| 25% periodisation-fund ceiling | '5 § Juridiska personer får dra av högst ett belopp som motsvarar 25 procent av överskottet av näringsverksamheten före avdraget.' | 2026-11-01 | [IL 30:5](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) |
| Fund deemed income and 0.5% floor | '6 a § En juridisk person som har gjort avdrag för avsättning till en periodiseringsfond ska ta upp en schablonintäkt. Intäkten ska beräknas till statslåneräntan vid utgången av november månad året närmast före det kalenderår under vilket beskattningsåret går ut multiplicerad med summan av gjorda avdrag för avsättningar till sådana periodiseringsfonder som den juridiska personen har vid beskattningsårets ingång. Statslåneräntan ska dock som lägst anses vara 0,5 procent. Om beskattningsåret är längre eller kortare än tolv månader, ska schablonintäkten justeras i motsvarande mån. Lag (2018:1206).' | 2026-11-01 | [IL 30:6a](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) |
| 6th-year fund release and oldest first | '7 § Avdrag för avsättning till en periodiseringsfond ska återföras senast det sjätte beskattningsåret efter det beskattningsår då avdraget gjordes. När återföring av avdrag för avsättning till periodiseringsfond sker, ska det tidigast gjorda avdraget återföras först.' | 2026-11-01 | [IL 30:7](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) |
| 106% and 104% fund transitions | '5. Vid tillämpning av 30 kap. 7, 8 och 10 a §§ ska avdrag för avsättning till periodiseringsfond som har gjorts vid beskattningsår som börjar före den 1 januari 2019 återföras med 103 procent av avdraget, om återföringen görs av en juridisk person vid beskattningsår som börjar efter den 31 december 2018 men före den 1 januari 2021 och med 106 procent av avdraget om återföringen görs vid beskattningsår som börjar efter den 31 december 2020. Vid tillämpning av samma bestämmelser ska även avdrag för avsättning till periodiseringsfond som görs vid beskattningsår som börjar efter den 31 december 2018 men före den 1 januari 2021 återföras med 104 procent av avdraget, om återföringen görs av en juridisk person vid beskattningsår som börjar efter den 31 december 2020.' | 2026-11-01 | [SFS 2018:1206, transition point 5](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) |
| 2025 end-November reference rate 2.55% | 'Kalenderåret SLR vid utgången av november (%) 2025 2,55' | 2026-11-01 | [Reference-rate table, end-November 2025](https://www4.skatteverket.se/rattsligvagledning/edition/2026.14/341469.html) |
| 2026 related-party interest application | '1. Denna lag träder i kraft den 1 januari 2026. 2. Lagen tillämpas första gången för beskattningsår, eller i fråga om svenska handelsbolag räkenskapsår, som börjar efter den 31 december 2025.' | 2026-11-01 | [SFS 2025:1333, transition](https://svenskforfattningssamling.se/sites/default/files/sfs/2025-11/SFS2025-1333.pdf) |
| Primary building deduction application | '3. Den nya bestämmelsen i 19 kap. 5 a § tillämpas för utgifter för ny-, till- eller ombyggnad av hyreshus som har färdigställts efter den 31 december 2016. Har färdigställandet skett senare men före den 1 januari 2019 får primäravdrag bara göras för den delen av sexårsperioden från färdigställandet som återstår den 1 januari 2019.' | 2026-11-01 | [SFS 2018:1206, transition point 3](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) |
| BFN specified-list ordinary application boundary | 'För räkenskapsår som inleds efter den 31 december 2025' | 2026-11-01 | [BFN annual-report FAQ, listed K3 categories](https://www.bfn.se/fragor-och-svar/arsredovisning/) |
| BFN specified-list first-year start boundary | 'efter den 30 juni 2025' | 2026-11-01 | [BFN annual-report FAQ, specified new companies](https://www.bfn.se/fragor-och-svar/arsredovisning/) |
| BFN specified-list first-year end boundary | 'den 31 december 2026 eller senare' | 2026-11-01 | [BFN annual-report FAQ, specified new companies](https://www.bfn.se/fragor-och-svar/arsredovisning/) |

### [LOSSES] [Official source](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json)

| Question | Ordinary rule and control |
| --- | --- |
| Carryforward period and ordinary profit cap | IL 40:2 generally permits deduction of the prior year's deficit, subject to the chapter and imported restrictions. It supplies no general fixed expiry or percentage-of-current-profit cap for an otherwise unrestricted ordinary loss. Prove the chain of returns and restrictions rather than assuming every historic balance survives. [IL](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) |
| Carryback | No general ordinary AB carryback entitlement has been qualified in the sources used here. Do not create a current refund by carrying a loss back; any asserted special entitlement needs its own source. |
| Ownership changes | Screen IL 40:10–17a and the actual control/aggregation rules. The current amount restriction can cap surviving pre-change losses at **300%** of the adjusted acquisition expenditure. Capital contributions can reduce that expenditure; group acquisitions have allocation rules. The anti-loss-buying rule can extinguish the whole prior balance. [IL](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) |
| Group contribution restriction | IL 40:18–19 restricts use of affected old losses against specified group contributions in the change year and the following 5 tax years, with statutory exceptions and interactions. Do not treat this as expiry of all losses or permission to use every contribution. [IL](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) |
| Debt relief, insolvency and reorganisations | Apply the relevant IL 40 restrictions and imported chapters, including debt relief. Liquidation, insolvency or a material tax-free reorganisation also activates the foundation's refusal rules. [IL, 40:1–2 and 20–24](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) |
| Separate restricted pools | Keep property losses, share losses, carried interest and foreign tax relief in their own schedules. They are not freely interchangeable with the ordinary deficit. [IL, 25:12, 48:26 and ch. 24](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) [Foreign Tax Credit Act](https://data.riksdagen.se/dokumentstatus/sfs-1986-468.json) |
| Group relief | IL ch. 35 provides conditional group contributions, not a consolidated group return. The ordinary ownership condition is **more than 90%**; whole-year or qualifying start-up ownership, actual value transfer, open matching disclosure, tax liability, dividend and treaty conditions also matter. Obtain the full group facts before a claim. [IL, 35:1–6](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) |

Use the actual year of the ownership change and applicable transition text. A current consolidated percentage does not establish the rule for a historic acquisition. For a current loss, preserve the calculation and any blocked amounts separately; do not report the blocked part as an available current deduction.


**Governing source wording.** Read dates are the recorded selected readings; apply the conditions and version limits above.

| Figure or rule | Exact official wording | Read on | Source |
| --- | --- | --- | --- |
| 300% ownership-change loss cap | '15 § Beloppsspärren innebär att underskottsföretaget inte får dra av underskott som uppkommit före det beskattningsår då spärren inträder till den del underskotten överstiger 300 procent av utgiften för att förvärva 1. det bestämmande inflytandet över underskottsföretaget i sådana fall som avses i 10 och 11 §§, eller 2. andelar som representerar mer än 50 procent av rösterna i underskottsföretaget i sådana fall som avses i 12 §. Om förvärvet omfattar flera underskottsföretag i samma koncern, ska avdragsutrymmet fördelas på dessa efter deras andel av koncernens sammanlagda underskott. Lag (2024:1131).' | 2026-11-01 | [IL 40:15](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) |
| Change-year plus 5-year group restriction | '18 § Koncernbidragsspärren innebär att underskottsföretaget inte får dra av underskott som uppkommit före det beskattningsår då spärren inträder, med högre belopp än beskattningsårets överskott före avdragsbegränsning för negativt räntenetto enligt 24 kap. 24 § och före avdrag för kvarstående negativt räntenetto enligt 24 kap. 26 § samt beräknat utan hänsyn till avdragen för underskott och till sådana mottagna koncernbidrag som ska tas upp enligt 35 kap. Om en del av underskotten inte får dras av på grund av beloppsspärren, gäller första stycket för den återstående delen. Belopp som på grund av bestämmelsen i första stycket eller bestämmelsen i 19 a § inte har kunnat dras av ska dras av det följande beskattningsåret, om det inte finns någon begränsning då. Koncernbidragsspärren gäller till och med femte beskattningsåret efter det beskattningsår då spärren inträdde. Lag (2020:1077).' | 2026-11-01 | [IL 40:18](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) |
| More than 90% group ownership | '2 § Med moderföretag avses i detta kapitel ett företag som äger mer än 90 procent av andelarna i ett svenskt aktiebolag eller en svensk ekonomisk förening och som är - ett svenskt aktiebolag, - en svensk ekonomisk förening, - en svensk sparbank, - ett svenskt ömsesidigt försäkringsföretag, - en svensk stiftelse som inte omfattas av bestämmelserna om undantag från skattskyldighet i 7 kap., eller - en svensk ideell förening som inte omfattas av bestämmelserna om undantag från skattskyldighet i 7 kap.' | 2026-11-01 | [IL 35:2](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) |

### [CREDITS] [Official source](https://data.riksdagen.se/dokumentstatus/sfs-1986-468.json)

Compute ordinary tax before conditional relief. Keep separate evidence, limits, carryforwards and ordering. No credit is assumed merely because an expense or foreign payment appears in the accounts.

**Foreign tax relief:** lag (1986:468) om avräkning av utländsk skatt requires qualifying foreign tax, income inclusion, source and any treaty conditions. For the ordinary route, calculate the Swedish limitation on net foreign income, the available Swedish tax and any deduction interaction. The statutory minimum limitation of **SEK 500** does not create a refund beyond available tax. Unused qualifying foreign tax can be carried to the following **5 tax years**, subject to claim, proof, ordering and the current-year limitation. Special pension, CFC and other branches need separate treatment. Do not credit a gross foreign withholding amount without establishing that it is legally borne, final where required and eligible. [Foreign Tax Credit Act, ch. 2](https://data.riksdagen.se/dokumentstatus/sfs-1986-468.json)

**Legal-person gift credit:** for qualifying money gifts paid after 31 December 2025 to an approved recipient for social assistance or scientific research, the relevant rules include a minimum **SEK 2,000 per gift**, a maximum qualifying basis of **SEK 800,000 per calendar year** and the IL 65:10 rate of **20.6%**. Verify the recipient's actual approval, gift purpose, payment date and all exclusions. Use the legal-person rules, not the individual's 25% rate. IL 67:23 governs the return claim; do not invent a 'next return' rule for a non-calendar company. The gift remains non-deductible, and an owner's exemption needs its own statutory conditions. The gift credit also affects available Swedish income tax for foreign tax limitation purposes. [IL, 9:2 and 67:20–26a](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) [SFS 2025:1361, including transition point 4](https://svenskforfattningssamling.se/sites/default/files/sfs/2025-11/SFS2025-1361.pdf) [Foreign Tax Credit Act, 2:9–10](https://data.riksdagen.se/dokumentstatus/sfs-1986-468.json)

**R&D, IP and investment support:** this source set does not qualify a standalone corporate income tax credit, IP rate or investment credit. Obtain the specific legislation and eligibility before a claim. A payroll contribution reduction, grant or ordinary expense deduction is not automatically an income tax credit. No such relief is included in the example.

**Withholding and prepayments:** reconcile Swedish preliminary tax under SFL separately from foreign tax relief. Dividend coupon tax and a treaty refund have their own taxpayer and procedure; they are not automatically credits against the distributing AB's ordinary income tax. [SFL, ch. 56](https://data.riksdagen.se/dokumentstatus/sfs-2011-1244.json) [Coupon Tax Act](https://data.riksdagen.se/dokumentstatus/sfs-1970-624.json)


**Governing source wording.** Read dates are the recorded selected readings; apply the conditions and version limits above.

| Figure or rule | Exact official wording | Read on | Source |
| --- | --- | --- | --- |
| SEK 500 foreign-tax limitation floor | 'Spärrbeloppet ska anses uppgå till minst 500 kronor. Spärrbeloppet får dock inte överstiga summan av den skattskyldiges 1. statliga och kommunala inkomstskatt, och 2. avkastningsskatt som tas ut enligt 2 § första stycket 4 lagen (1990:661) om avkastningsskatt på pensionsmedel.' | 2026-11-01 | [Foreign Tax Credit Act, 2:9](https://data.riksdagen.se/dokumentstatus/sfs-1986-468.json) |
| 5-year foreign-tax carryforward | '17 § Till den del avräkning från den svenska skatt som beräknas för ett visst beskattningsår inte kunnat ske det år som anges i 7 § andra stycket, därför att summan avräkningsbar utländsk skatt enligt 8 § överstiger det enligt 9 § beräknade spärrbeloppet, är den skattskyldige efter begäran berättigad att senast för det femte beskattningsåret efter ovan nämnda beskattningsår få avräkning av det överskjutande beloppet. För ett visst år får dock det sammanlagda belopp för vilket avräkning högst får ske inte överstiga det årets spärrbelopp enligt 9 §. Om den skattskyldige begär avräkning av utländska skatter som enligt 7 § andra stycket är hänförliga till olika år, ska avräkning ske så att utländska skatter hänförliga till tidigare år avräknas före utländska skatter hänförliga till senare år. Lag (2011:1275).' | 2026-11-01 | [Foreign Tax Credit Act, 2:17](https://data.riksdagen.se/dokumentstatus/sfs-1986-468.json) |
| SEK 2,000 minimum legal-person gift | '21 § Med gåva avses vid tillämpningen av detta kapitel en gåva i pengar som lämnas av 1. en fysisk person och som vid ett och samma gåvotillfälle uppgår till minst 200 kronor, eller 2. en juridisk person och som vid ett och samma gåvotillfälle uppgår till minst 2 000 kronor. Lag (2025:1361).' | 2026-11-01 | [IL 67:21](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) |
| SEK 800,000 basis and ordinary-rate gift credit | '26 a § Skattereduktionen för juridiska personer uppgår till underlaget multiplicerat med procentsatsen enligt 65 kap. 10 §. Underlaget för skattereduktion får dock uppgå till högst 800 000 kronor för ett kalenderår. Lag (2025:1361).' | 2026-11-01 | [IL 67:26a](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) |
| Individual gift-credit comparison, not the AB rate | '26 § Skattereduktionen för fysiska personer uppgår till 25 procent av underlaget.' | 2026-11-01 | [IL 67:26](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) |
| Legal-person gift application after 2025 | '4. Bestämmelserna i 11 kap. 49 §, 24 kap. 5 §, 42 kap. 12 a §, 67 kap. 21– 26 a §§ tillämpas på gåvor som lämnas efter den 31 december 2025.' | 2026-11-01 | [SFS 2025:1361, transition point 4](https://svenskforfattningssamling.se/sites/default/files/sfs/2025-11/SFS2025-1361.pdf) |

### [FILING MECHANICS] [Official source](https://www.skatteverket.se/foretag/inkomstdeklaration/deklareraatettaktiebolagellerenekonomiskforening/saharlamnarduinochfylleriinkomstdeklarationen.4.262c54c219391f2e96322d7.html)

Prepare INK2, INK2R and INK2S. The official blank calendar 2026 form examined for this guide bears the 2026P4 identifiers; obtain the correct version for the actual return before use. The verified ordinary mapping is:

| Return field | Mapping or check |
| --- | --- |
| INK2R 3.26 or 3.27 | Booked net profit or loss transfers to INK2S 4.1 or 4.2. This is after booked income tax, unlike the foundation's profit-before-tax starting point. |
| INK2S 4.3a | Add back booked income tax, with the sign and deferred tax reconciliation checked. Avoid a second addback if the working paper already starts before tax. |
| INK2S 4.14a–c | Reconcile prior losses and statutory reductions. A blocked prior loss is not an unrestricted deduction. |
| INK2S 4.15 and 4.16 | Taxable surplus transfers to INK2 1.1; the specified deficit/blocked-loss amounts feed 1.2 under the form instructions. Keep the underlying loss schedules. |
| INK2 1.4 and 1.5 | Positive or negative special pension payroll tax base. Do not substitute wages, the pension deduction or supplemental pension cost information at 4.21. |
| INK2 1.16 | Qualifying legal-person gift basis, subject to the credit rules above. |

These are selected field checks, not a complete BAS account or SRU schema implementation. Read the current form and instructions for every used field and attachment. [Skatteverket filing guidance](https://www.skatteverket.se/foretag/inkomstdeklaration/deklareraatettaktiebolagellerenekonomiskforening/saharlamnarduinochfylleriinkomstdeklarationen.4.262c54c219391f2e96322d7.html) [Official form service](https://www.skatteverket.se/4.39f16f103821c58f680006188.html)

Skatteverket's current guidance describes **Inkomstdeklaration 2, 3 och 4**, filing software and SRU file transfer routes for a complete return. A file upload receipt is not the signed declaration receipt: complete the required signature step and retain both. Digital authority can include a registered signatory authorised to sign alone, the CEO or a declaration agent, subject to the service rules. Paper signatures follow the actual representation rights, including any joint signatures; a declaration agent cannot sign the paper declaration. [Skatteverket](https://www.skatteverket.se/foretag/inkomstdeklaration/deklareraatettaktiebolagellerenekonomiskforening/saharlamnarduinochfylleriinkomstdeklarationen.4.262c54c219391f2e96322d7.html)

The legacy **Inkomstdeklaration 2** service handles the first page, with other parts sent separately, and is scheduled to close on **29 December 2026**. Do not use it to promise a complete electronic 2027 filing or the extra electronic month. At the source check, the current guide's open periods extended only through August 2026; availability for a December 2026 year end and the actual 2027 filing must be confirmed. [Skatteverket](https://www.skatteverket.se/foretag/inkomstdeklaration/deklareraatettaktiebolagellerenekonomiskforening/saharlamnarduinochfylleriinkomstdeklarationen.4.262c54c219391f2e96322d7.html)

Apply attachment triggers, including N3B for relevant partnership interests, N4 for relevant share losses or deferrals, N7 for the relevant takeover items, N8 for forest/substance deductions and N9 for interest limitation information. The current guidance introduces **N12** for replacement funds for financial years ending in September 2026 or later; confirm the supported service/attachment route for the actual return. An annual report is not automatically a mandatory income tax return attachment. An attachment's absence from this list does not establish that it is unnecessary. [Skatteverket](https://www.skatteverket.se/foretag/inkomstdeklaration/deklareraatettaktiebolagellerenekonomiskforening/saharlamnarduinochfylleriinkomstdeklarationen.4.262c54c219391f2e96322d7.html)

**Audit:** a private AB may provide in its articles that it has no auditor only where the statutory exception is available. It cannot use that exception if it exceeds more than one of these conditions in each of the latest 2 financial years: average employees over **3**, balance sheet total over **SEK 1.5 million** or net turnover over **SEK 3 million**. A parent also applies the statutory group test with the required eliminations. A private AB with an auditor registered at financial year end must have the audit report for that year. Check the actual articles, register, group and any special rules; this does not exempt it from preparing accounts or filing. [Aktiebolagslagen (2005:551), 9:1–1a; SFS 2010:834 transition](https://data.riksdagen.se/dokumentstatus/sfs-2005-551.json)

#### Penalties and interest [Official source](https://data.riksdagen.se/dokumentstatus/sfs-2011-1244.json)

Keep late filing, an incorrect return, estimated assessment and tax-account interest separate. Establish the applicable obligation, actual receipt and decision dates before a charge. The following ordinary AB rules are not a determination of a company's liability.

| Event | Ordinary rule and conditions | Official URL |
| --- | --- | --- |
| Late INK2 | SFL 48:6 sets **SEK 6,250** per fee. Under 48:7 a second fee follows if the obligation is still unfulfilled after **3 months**, and a third after a further **2 months**: at most **SEK 18,750** for these 3 fees before any relief. For the repeat-fee clock, 48:7 expressly disregards the extra electronic filing month. Establish the ordinary statutory date and any actual extension; do not count every interval from the later electronic deadline. | https://data.riksdagen.se/dokumentstatus/sfs-2011-1244.json |
| Incomplete or unsigned return | A return so deficient that it plainly cannot support assessment is not treated as filed under 48:2. Section 48:4 requires a direction to cure a missing signature and permits a fee on that ground only if it is not obeyed. This cure rule does not make an unsigned upload a completed filing or repair other substantive defects. | https://data.riksdagen.se/dokumentstatus/sfs-2011-1244.json |
| Incorrect information | Apply the definition and exceptions in SFL 49:4–5. The ordinary final-income-tax surcharge under 49:11 is **40% of the tax shortfall** that the incorrect information would have caused, not 40% of omitted income. A qualifying timing error uses **10%** under 49:13. An erroneous loss unused in that year instead uses **one quarter of the wrongly credited loss** as the base under 49:14 before applying the relevant surcharge rate. Issue-specific computation and ordering in 49:19–21 still apply. | https://data.riksdagen.se/dokumentstatus/sfs-2011-1244.json |
| Estimated assessment after no return | Apply SFL 49:6–8 and 15–17, including the prescribed written-information and loss adjustments. Under 49:7 the initial estimated-assessment surcharge is removed if INK2 reaches Skatteverket or an administrative court within **4 months from the end of the decision month**, with a separate proven delayed-knowledge rule. A later declaration does not undo the additional surcharge on agency-initiated reconsideration governed by 49:8 after that cure window. | https://data.riksdagen.se/dokumentstatus/sfs-2011-1244.json |
| Exceptions and relief | Test all applicable SFL 49:10 exceptions, including qualifying reconciliation information, correction on the taxpayer's own initiative and an insignificant tax amount. Correction linked to an announced general control is not on the taxpayer's own initiative if made only after **2 months from the end of the announcement month**, subject to all statutory conditions. Under 51:1 Skatteverket must grant full or partial special-fee relief where the full charge is unreasonable, applying the specified circumstances, proportionality and delay tests. Relief is not automatic. | https://data.riksdagen.se/dokumentstatus/sfs-2011-1244.json |

The amended incorrect-information provisions in SFS 2026:110 commenced on **1 April 2026**; SFS 2026:303's changes, including 49:8, commenced on **1 May 2026**. Use the provision applicable to the actual procedural event. These rules do not extend the return deadline or remove the need to correct the underlying assessment. [SFS 2026:110](https://svenskforfattningssamling.se/sites/default/files/sfs/2026-02/SFS2026-110.pdf) [SFS 2026:303](https://svenskforfattningssamling.se/sites/default/files/sfs/2026-03/SFS2026-303.pdf)

Tax-account interest is calculated daily on the relevant balance and posted monthly under SFL 65:2. Ordinary low cost interest follows the statutory base rate under 65:4; unpaid tax after its due date generally bears the base rate plus **15 percentage points**, until the enforcement-registration event specified in 65:13, after which the base rate applies. SFS 2026:146 commenced on **2 April 2026**. Final-tax interest can start before the final payment deadline; retain the SEK 30,000 timing rule and the scoped 2027 dates above. Partial payments first reduce the debt bearing the highest interest under 65:14. Interest relief under 65:15 requires **exceptional grounds (synnerliga skäl)**, a different test from special-fee relief. [SFL, 65:2–6 and 13–18](https://data.riksdagen.se/dokumentstatus/sfs-2011-1244.json) [SFS 2026:146](https://svenskforfattningssamling.se/sites/default/files/sfs/2026-02/SFS2026-146.pdf)

At the **2 November 2026** source check, Skatteverket states low cost interest of **2.5%** and high cost interest of **17.5%**, effective from **1 December 2024**. Its exact wording is: 'Från den 1 december 2024 är den låga kostnadsräntan 2,5 procent och den höga kostnadsräntan 17,5 procent.' These variable rates are a dated snapshot. They do not establish the rates for the company's 2027 settlement. Recheck each applicable period and reconcile actual account postings; the authority page's individual-taxpayer payment example does not set an AB's deadline. [Skatteverket tax-account interest](https://www.skatteverket.se/rantapaskattekontot)


**Governing source wording.** Read dates are the recorded selected readings; apply the conditions and version limits above.

| Figure or rule | Exact official wording | Read on | Source |
| --- | --- | --- | --- |
| Late INK2 fee SEK 6,250 | '6 § Förseningsavgiftens storlek framgår av följande uppställning. Om förseningsavgiften gäller uppgår den till aktiebolags eller ekonomisk förenings inkomstdeklarationer 6 250 kronor' | 2026-11-02 | [SFL 48:6](https://data.riksdagen.se/dokumentstatus/sfs-2011-1244.json) |
| Second/third fees, 3+2 months and electronic exception | '7 § Om den som utan föreläggande ska lämna en inkomstdeklaration, tilläggsskattedeklaration, tilläggsskatterapport eller särskilda uppgifter inte har gjort det inom tre månader från den tidpunkt då skyldigheten enligt denna lag skulle ha fullgjorts, ska en andra förseningsavgift tas ut. Om skyldigheten inte har fullgjorts efter ytterligare två månader, ska en tredje förseningsavgift tas ut. Vid tillämpningen av första stycket ska hänsyn inte tas till den senarelagda deklarationstidpunkt som gäller för andra juridiska personer än dödsbon som lämnar deklaration elektroniskt.' | 2026-11-02 | [SFL 48:7](https://data.riksdagen.se/dokumentstatus/sfs-2011-1244.json) |
| Ordinary surcharge 40% of final-tax shortfall | '11 § Skattetillägg på sådan skatt som avses i 56 kap. 3 § 1-4 och 6 (skattetillägg på slutlig skatt) och 56 a kap. 3 § 1-3 (skattetillägg på tilläggsskatt) är 40 procent av den skatt som, om den oriktiga uppgiften hade godtagits, inte skulle ha bestämts för den som har lämnat uppgiften.' | 2026-11-02 | [SFL 49:11](https://data.riksdagen.se/dokumentstatus/sfs-2011-1244.json) |
| 10% timing-error final-tax surcharge | '13 § Om den oriktiga uppgiften består i att ett belopp har hänförts eller kan antas komma att hänföras till fel beskattningsår eller fel redovisningsperiod, är 1. skattetillägget på slutlig skatt och skattetillägget på tilläggsskatt 10 procent,' | 2026-11-02 | [SFL 49:13](https://data.riksdagen.se/dokumentstatus/sfs-2011-1244.json) |
| Unused erroneous loss: quarter-loss base | '14 § Om en oriktig uppgift skulle ha medfört ett sådant underskott av en näringsverksamhet eller i inkomstslaget tjänst som inte utnyttjas samma beskattningsår, ska skattetillägget inte beräknas på skatt utan i stället på en fjärdedel av det underskott som, om den oriktiga uppgiften hade godtagits, felaktigt skulle ha tillgodoräknats den som har lämnat uppgiften.' | 2026-11-02 | [SFL 49:14](https://data.riksdagen.se/dokumentstatus/sfs-2011-1244.json) |
| Estimated-assessment cure, 4 months | '7 § Ett beslut om skattetillägg vid skönsbeskattning på grund av att den deklarationsskyldige inte har lämnat någon skattedeklaration, inkomstdeklaration eller tilläggsskattedeklaration ska undanröjas om 1. en skattedeklaration lämnas inom två månader från utgången av den månad då beslutet meddelades, eller 2. en inkomstdeklaration eller tilläggsskattedeklaration lämnas inom fyra månader från utgången av den månad då beslutet meddelades.' | 2026-11-02 | [SFL 49:7](https://data.riksdagen.se/dokumentstatus/sfs-2011-1244.json) |
| Voluntary correction and 2-month control limitation | '10 § Skattetillägg får inte tas ut om 1. den oriktiga uppgiften framgår av avstämningsuppgifter som har varit tillgängliga för Skatteverket inom ett år från utgången av beskattningsåret, 2. den uppgiftsskyldige på eget initiativ har rättat den oriktiga uppgiften eller lämnat uppgift om att skatteavdrag inte har gjorts, eller 3. det skattebelopp som kunde ha undandragits genom felaktigheten eller passiviteten är obetydligt. En rättelse anses inte vara på eget initiativ om 1. Skatteverket har informerat om att verket ska genomföra en generell kontroll, 2. rättelsen har en koppling till den generella kontrollen, och 3. rättelsen görs först två månader efter utgången av den månad då Skatteverket informerade om den generella kontrollen. Lag (2018:562).' | 2026-11-02 | [SFL 49:10](https://data.riksdagen.se/dokumentstatus/sfs-2011-1244.json) |
| Full/partial special-fee relief | '1 § Skatteverket ska besluta om hel eller delvis befrielse från en särskild avgift om det är oskäligt att avgiften tas ut med fullt belopp. Vid bedömningen ska det särskilt beaktas om 1. den felaktighet eller passivitet som har lett till avgiften kan antas ha a) berott på ålder, hälsa eller liknande förhållande, b) berott på en felbedömning av en regel eller betydelsen av de faktiska förhållandena, eller c) föranletts av vilseledande eller missvisande kontrolluppgifter eller uppgifter om betalningsmottagare i arbetsgivardeklarationer, 2. avgiften inte står i rimlig proportion till felaktigheten eller passiviteten, eller 3. en oskäligt lång tid har gått efter det att Skatteverket har funnit anledning att anta att avgift ska tas ut utan att den som avgiften gäller kan lastas för dröjsmålet. Lag (2020:858).' | 2026-11-02 | [SFL 51:1](https://data.riksdagen.se/dokumentstatus/sfs-2011-1244.json) |
| Daily balance and monthly posting | '2 § Ränta ska beräknas dagligen på skattekontots saldo. Ränta som ska påföras (kostnadsränta) ska beräknas när det finns ett underskott på skattekontot och ränta som ska tillgodoräknas (intäktsränta) när kontot uppvisar ett överskott. Ränta på skatt eller avgift som ska betalas enligt ett beslut om ansvar enligt 59 kap. ska dock beräknas utan hänsyn till skattekontots saldo enligt bestämmelserna i 19 och 20 §§. Ränta ska påföras eller tillgodoräknas varje månad.' | 2026-11-01 | [SFL 65:2](https://data.riksdagen.se/dokumentstatus/sfs-2011-1244.json) |
| Late interest, base plus 15 points | 'Om skatt eller avgift inte betalas i rätt tid, ska kostnadsränta beräknas från och med dagen efter den dag då beloppet senast skulle ha betalats. Kostnadsränta ska beräknas efter en räntesats som motsvarar basräntan plus 15 procentenheter till och med den dag då ett beslut om att lämna beloppet till Kronofogdemyndigheten för indrivning eller för verkställighet av betalningssäkring registreras hos Kronofogdemyndigheten. Därefter beräknas kostnadsräntan efter en räntesats som motsvarar basräntan. Denna lag träder i kraft den 2 april 2026.' | 2026-11-02 | [SFL 65:13; SFS 2026:146](https://svenskforfattningssamling.se/sites/default/files/sfs/2026-02/SFS2026-146.pdf) |
| Audit exception, 2 years and 3/1.5m/3m thresholds | 'I bolagsordningen för ett privat aktiebolag får det anges att bolaget inte ska ha någon revisor. Andra stycket gäller inte om bolaget uppfyller mer än ett av följande villkor: 1. medelantalet anställda i bolaget har under vart och ett av de två senaste räkenskapsåren uppgått till mer än 3, 2. bolagets redovisade balansomslutning har för vart och ett av de två senaste räkenskapsåren uppgått till mer än 1,5 miljoner kronor, 3. bolagets redovisade nettoomsättning har för vart och ett av de två senaste räkenskapsåren uppgått till mer än 3 miljoner kronor. Tredje stycket gäller även för moderbolag i en koncern, om koncernen uppfyller mer än ett av de villkor som anges där. Vid tillämpningen ska fordringar och skulder mellan koncernföretag, liksom internvinster, elimineras. Detsamma gäller för intäkter och kostnader som hänför sig till transaktioner mellan koncernföretag, liksom förändring av internvinst. Om ett privat aktiebolag vid utgången av ett räkenskapsår har en revisor registrerad i aktiebolagsregistret, ska bolaget alltid ha en revisor som lämnar en revisionsberättelse för det räkenskapsåret. Lag (2010:834).' | 2026-11-01 | [ABL 9:1](https://data.riksdagen.se/dokumentstatus/sfs-2005-551.json) |
| Legacy filing service closure | 'Tjänsten Inkomstdeklaration 2 avvecklas 29 december 2026' | 2026-11-01 | [Skatteverket, legacy service closure](https://www.skatteverket.se/foretag/inkomstdeklaration/deklareraatettaktiebolagellerenekonomiskforening/saharlamnarduinochfylleriinkomstdeklarationen.4.262c54c219391f2e96322d7.html) |
| Current observed service-period label | 'Januari–augusti 2026' | 2026-11-01 | [Skatteverket, observed open periods](https://www.skatteverket.se/foretag/inkomstdeklaration/deklareraatettaktiebolagellerenekonomiskforening/saharlamnarduinochfylleriinkomstdeklarationen.4.262c54c219391f2e96322d7.html) |
| N12 first eligible year-end wording | 'september 2026 eller senare' | 2026-11-01 | [Skatteverket, N12 attachment eligibility](https://www.skatteverket.se/foretag/inkomstdeklaration/deklareraatettaktiebolagellerenekonomiskforening/saharlamnarduinochfylleriinkomstdeklarationen.4.262c54c219391f2e96322d7.html) |
| Incorrect-information amendment commencement | 'Denna lag träder i kraft den 1 april 2026.' | 2026-11-02 | [SFS 2026:110, commencement](https://svenskforfattningssamling.se/sites/default/files/sfs/2026-02/SFS2026-110.pdf) |
| SFL 2026:303 commencement | 'Denna lag träder i kraft den 1 maj 2026.' | 2026-11-01 | [SFS 2026:303, commencement](https://svenskforfattningssamling.se/sites/default/files/sfs/2026-03/SFS2026-303.pdf) |

### [ANTI-AVOIDANCE] [Official source](https://data.riksdagen.se/dokumentstatus/sfs-1995-575.json)

| Screen | Conditions requiring evidence or referral |
| --- | --- |
| GAAR | Lag (1995:575) requires the cumulative statutory conditions: a substantial tax benefit, participation, the tax benefit as the predominant reason and an assessment contrary to the legislation's purpose. Application follows the statutory court procedure on Skatteverket's request. A tax benefit alone is not a concluded GAAR finding. [2–4 §§](https://data.riksdagen.se/dokumentstatus/sfs-1995-575.json) |
| CFC | IL ch. 39a uses its own associated-person and **25%** capital/vote tests and a low-tax comparison of **55%** of the Swedish counterfactual AB tax, with special adjustments. Do not substitute a foreign nominal rate. Annex, indirect ownership, exempt-income and EEA substance conditions need analysis; no country annex list or actual inclusion has been qualified here. [IL, 39a:2–9 and 13a](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) |
| Hybrid mismatches | IL ch. 24b covers specified mismatches and structured arrangements. Its **25% or 50%** association tests depend on the provision; do not import the interest, loss or CFC group definition. A triggered hybrid also invokes R-CIT-12. [IL](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) |
| Transfer pricing | IL 14:19 requires its 3 statutory conditions for an adjustment. SFL ch. 39 has separate documentation definitions. The SME documentation exception requires fewer than **250 employees** and turnover at most **SEK 450 million** or balance sheet total at most **SEK 400 million** for the relevant prior year and group. The below **SEK 5 million** annual aggregate test concerns the relevant counterparty or establishment, not each transaction; intangibles require their own immateriality condition. A documentation exception does not remove arm's-length obligations. [IL, 14:19–20](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) [SFL, 39:15–16f](https://data.riksdagen.se/dokumentstatus/sfs-2011-1244.json) |
| Other international minimum-tax claims | No separate BEAT or GILTI calculation has been qualified. Route a foreign parent inclusion or other foreign minimum tax to its actual law; do not infer its treatment from Sweden's ordinary rate. |

Interest, shell-company and loss anti-avoidance provisions also apply as screened above. Refer an aggressive position under R-CIT-7 before computing it.


**Governing source wording.** Read dates are the recorded selected readings; apply the conditions and version limits above.

| Figure or rule | Exact official wording | Read on | Source |
| --- | --- | --- | --- |
| CFC 25% owner/control screen | '2 § En skattskyldig anses vid tillämpning av detta kapitel som delägare i en utländsk juridisk person om vid utgången av delägarens beskattningsår andelar med tillsammans minst 25 procent av den utländska juridiska personens kapital eller röster, direkt eller indirekt genom andra utländska juridiska personer, innehas eller kontrolleras av delägaren eller av delägaren och personer i intressegemenskap med delägaren.' | 2026-11-01 | [IL 39a:2](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) |
| CFC 55% low-tax comparison | '5 § Nettoinkomsten hos en utländsk juridisk person ska anses lågbeskattad om den inte beskattats eller beskattats lindrigare än den beskattning som skulle ha skett i Sverige om 55 procent av denna inkomst utgjort överskott av näringsverksamhet för ett svenskt aktiebolag som bedriver motsvarande verksamhet i Sverige.' | 2026-11-01 | [IL 39a:5](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) |
| Hybrid 25% association and 50% substitution | '3 § Företag ska vid tillämpning av detta kapitel och 6 kap. 11 § första stycket 8 anses vara i intressegemenskap om 1. företagen ingår i en koncern av sådant slag som anges i 1 kap. 4 § årsredovisningslagen (1995:1554), 2. ett av företagen, direkt eller indirekt, innehar minst 25 procent av kapitalet eller rösterna i det andra företaget eller har rätt till minst 25 procent av vinsten i det andra företaget, eller 3. en och samma person, direkt eller indirekt, innehar minst 25 procent av kapitalet eller rösterna i företagen. Vid bedömningen av om företagen är i intressegemenskap ska personer som agerar tillsammans i fråga om innehav av kapitalet eller rösterna i ett annat företag behandlas som en enda person. Vid tillämpning av 8-11, 13 och 14 §§ och 6 kap. 11 § första stycket 8 ska, i stället för 25 procent i första stycket 2-3, 50 procent gälla. Lag (2021:473).' | 2026-11-01 | [IL 24b:3](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) |
| TP documentation SME thresholds | '16 a § Ett företag är inte dokumentationsskyldigt enligt 16 § om det året före beskattningsåret ingår i en intressegemenskap som har mindre än 250 anställda och antingen har en omsättning som inte överstiger 450 miljoner kronor eller en balansomslutning som inte överstiger 400 miljoner kronor. Lag (2017:185).' | 2026-11-01 | [SFL 39:16a](https://data.riksdagen.se/dokumentstatus/sfs-2011-1244.json) |
| TP SEK 5m aggregate immateriality and intangibles | 'Om det sammanlagda värdet av transaktionerna med det begränsat skattskyldiga företaget i fall som avses i 16 § 1 och 2 understiger 5 000 000 kronor under räkenskapsåret, räknas transaktionerna alltid som oväsentliga. Detsamma gäller om det sammanlagda värdet av de transaktioner som ska anses hänförliga till det fasta driftstället i fall som avses i 16 § 3-5 understiger 5 000 000 kronor under räkenskapsåret. Undantagen i första och andra styckena gäller upplåtelse och överlåtelse av immateriella tillgångar endast om tillgångarna är oväsentliga för verksamheten. Lag (2017:185).' | 2026-11-01 | [SFL 39:16c](https://data.riksdagen.se/dokumentstatus/sfs-2011-1244.json) |

### [PILLAR TWO OVERLAY] [Official source](https://data.riksdagen.se/dokumentstatus/sfs-2023-875.json)

Sweden's lag (2023:875) om tilläggsskatt contains domestic top-up tax, IIR and UTPR mechanisms. The original act generally applies from financial years starting after 31 December 2023; the specified UTPR provisions generally start after 31 December 2024, with statutory exceptions. These mechanisms therefore require screening for the scoped 2026 year; the ordinary AB rate does not switch them off. [Top-up Tax Act, chs. 1–2 and 6, original transition points 1–3](https://data.riksdagen.se/dokumentstatus/sfs-2023-875.json)

Test consolidated group revenue of at least **EUR 750 million in at least 2 of the preceding 4 financial years**, including the statutory treatment of excluded entities' revenue, non-standard years and currency conversion. Establish all group members, excluded entities, jurisdictional allocation and the relevant parent/constituent roles. The **15%** minimum is based on adjusted jurisdictional income and covered taxes, rather than book profit times the domestic headline rate. QDMTT, IIR and UTPR have distinct charging and allocation rules. [Top-up Tax Act, chs. 1–2 and 6](https://data.riksdagen.se/dokumentstatus/sfs-2023-875.json)

The temporary CbCR safe harbour in the reviewed text concerns financial years starting after 2023 but before 2027 and ending by **30 June 2028**, subject to the complete conditions and elections. Its simplified effective tax test uses **15%, 16% or 17%** for years starting in 2024, 2025 or 2026 respectively; the other tests and the ordinary de minimis rule have different bases and periods. Do not assume that satisfying a test removes every return obligation or that an unqualified extension applies. [Top-up Tax Act, ch. 8](https://data.riksdagen.se/dokumentstatus/sfs-2023-875.json)

SFL ch. 33d governs the top-up information return. The ordinary period is **15 months**, extended to **18 months** for the first year the act applies to the group, with a special earliest-date rule for the specified early periods. Confirm notification, local filing or qualifying exchange, tax return and payment obligations separately. The 2026:303 and 2026:305 amendments took effect on **1 May 2026**; this is not a blanket exemption for a financial year starting earlier. No complete top-up calculation, actual election, foreign qualified-regime conclusion or filing-ready return is supplied by this guide. [SFL, 33d](https://data.riksdagen.se/dokumentstatus/sfs-2011-1244.json) [Top-up Tax Act and 2026:305 transition](https://data.riksdagen.se/dokumentstatus/sfs-2023-875.json)


**Governing source wording.** Read dates are the recorded selected readings; apply the conditions and version limits above.

| Figure or rule | Exact official wording | Read on | Source |
| --- | --- | --- | --- |
| Pillar Two EUR 750m, 2 of 4 years | '3 § Denna lag ska tillämpas när en svensk koncernenhet ingår i en koncern som har en årlig intäkt på minst 750 miljoner euro enligt moderföretagets koncernredovisning under minst två av de fyra räkenskapsår som föregår det aktuella räkenskapsåret. Lagen ska inte tillämpas på undantagna enheter. Intäkter för undantagna enheter ska dock ingå i de intäkter som avses i första stycket. Om ett eller flera av de fyra räkenskapsåren är längre eller kortare än tolv månader, ska beloppsgränsen i första stycket justeras proportionellt för vart och ett av dessa räkenskapsår.' | 2026-11-01 | [Top-up Tax Act, 1:3](https://data.riksdagen.se/dokumentstatus/sfs-2023-875.json) |
| Pillar Two 15% minimum | '25 § Med minimiskattesats avses en skattesats om 15 procent.' | 2026-11-01 | [Top-up Tax Act, 2:25](https://data.riksdagen.se/dokumentstatus/sfs-2023-875.json) |
| Temporary safe-harbour time limits | '2 § Bestämmelserna i 3-13 §§ gäller för koncernenheter i en stat för tid som - motsvarar de räkenskapsår som gäller för enheternas moderföretag, och - börjar närmast efter den 31 december 2023 men före den 1 januari 2027. Bestämmelserna gäller dock inte för räkenskapsår som avslutas efter den 30 juni 2028. Lag (2024:1248).' | 2026-11-01 | [Top-up Tax Act, 8:2](https://data.riksdagen.se/dokumentstatus/sfs-2023-875.json) |
| Safe-harbour 15%, 16% and 17% | 'Procentsatsen enligt första stycket ska vara - 15 procent för räkenskapsår som börjar under 2024, - 16 procent för räkenskapsår som börjar under 2025, och - 17 procent för räkenskapsår som börjar under 2026.' | 2026-11-01 | [Top-up Tax Act, 8:4](https://data.riksdagen.se/dokumentstatus/sfs-2023-875.json) |
| Top-up report 15/18 months | '13 § En tilläggsskatterapport och en anmälan som avses i 3 § andra stycket och 4 § tredje stycket ska ha kommit in till Skatteverket inom 15 månader efter utgången av det beskattningsår som rapporten eller anmälan avser. Om det är första gången lagen (2023:875) om tilläggsskatt ska tillämpas på koncernen, ska rapporten och anmälan i stället ha kommit in till Skatteverket inom 18 månader efter utgången av det beskattningsår som rapporten eller anmälan avser.' | 2026-11-01 | [SFL 33d:13](https://data.riksdagen.se/dokumentstatus/sfs-2011-1244.json) |
| Pillar Two original 2024/2025 application | '1. Denna lag träder i kraft den 1 januari 2024. 2. Lagen tillämpas första gången för beskattningsår som börjar närmast efter den 31 december 2023 eller, i fråga om svenska handelsbolag, räkenskapsår som börjar närmast efter den 31 december 2023. 3. Bestämmelserna i 6 kap. 9-15 §§ ska dock tillämpas på svenska koncernenheter första gången för beskattningsår som börjar närmast efter den 31 december 2024 eller, i fråga om svenska handelsbolag, räkenskapsår som börjar närmast efter den 31 december 2024. Detta gäller dock inte om koncernenhetens moderföretag är ett sådant moderföretag som avses i 6 kap. 5 § 2.' | 2026-11-01 | [Top-up Tax Act, original transition points 1–3](https://data.riksdagen.se/dokumentstatus/sfs-2023-875.json) |
| Pillar Two 2026:305 commencement | 'Denna lag träder i kraft den 1 maj 2026.' | 2026-11-01 | [SFS 2026:305, commencement](https://svenskforfattningssamling.se/sites/default/files/sfs/2026-03/SFS2026-305.pdf) |

### [CROSS-REFERENCES] [Official source](https://data.riksdagen.se/dokumentstatus/sfs-1970-624.json)

| Related work | Route and limit |
| --- | --- |
| Withholding matrix: dividend to a foreign recipient | The domestic coupon tax headline is **30%**, subject to taxpayer, recipient, establishment nexus, exemptions, treaty and anti-abuse conditions. The EU capital-holding route includes a **10%** condition and further requirements, not an automatic exemption. Qualify the event and law version. [Coupon Tax Act, 1 and 4–5 §§](https://data.riksdagen.se/dokumentstatus/sfs-1970-624.json) |
| Dividend responsibility, reporting and payment | Determine issuer, CSD or nominee responsibilities. A non-CSD AB generally has the specified **4-month** reporting/remittance period, no later than **15 January** of the following year, subject to the actual event and rules. Coupon tax uses a separate process, not ordinary INK2 settlement. The ordinary refund claim limit is the end of the **5th calendar year** after the event, subject to the statute and proof. [Coupon Tax Act, 7–15 and 27 §§](https://data.riksdagen.se/dokumentstatus/sfs-1970-624.json) |
| Dividend law changes | SFS 2025:1353 applies its change to dividends paid after 31 December 2025. SFS 2026:840 took effect on 1 July 2026 and applies to specified events after commencement; an event on the boundary date needs its own analysis. No actual treaty, refund or securities-lending result is qualified. [SFS 2025:1353](https://svenskforfattningssamling.se/sites/default/files/sfs/2025-11/SFS2025-1353.pdf) [SFS 2026:840](https://svenskforfattningssamling.se/sites/default/files/sfs/2026-05/SFS2026-840.pdf) |
| Interest or royalty payment | Do not generalise the dividend rate to other payments. Qualify recipient, source, beneficial entitlement, permanent establishment and treaty/legislation before determining any withholding or recipient tax. No general rate matrix has been established here. |
| Pillar Two | Use the section above and the complete international workflow. A safe harbour screen is not the full calculation. |
| DAC6 / MDR | Lag (2020:434) and SFL ch. 33b require a reportable-arrangement and role analysis. The main-benefit test applies only to the specified hallmarks, not all of them. The ordinary **30-day** trigger runs from the day after the relevant statutory event; assistance and quarterly update rules differ. Privilege and client notification require current analysis. [Reportable Arrangements Act](https://data.riksdagen.se/dokumentstatus/sfs-2020-434.json) [SFL](https://data.riksdagen.se/dokumentstatus/sfs-2011-1244.json) |
| CbCR | Distinguish the Swedish preceding-year **SEK 7 billion** exemption from the **EUR 750 million** test used for the specified secondary-parent-jurisdiction condition. Establish parent, surrogate, exchange and local roles. The report generally has a **12-month** period; ordinary notification is before year end. The 2025:1382 application rule concerns information for calendar 2026, not simply every report sent in 2026. [SFL, ch. 33a and transition](https://data.riksdagen.se/dokumentstatus/sfs-2011-1244.json) [CbCR exchange act](https://data.riksdagen.se/dokumentstatus/sfs-2017-182.json) |
| IP, R&D and free-zone claims | No income tax rate, credit or zone exemption has been qualified here. Require the specific source and complete eligibility before use. |
| Transfer pricing | Load `transfer-pricing-workflow-base` for its workflow, then supply the Swedish legal and factual analysis. Do not treat a documentation exemption as a pricing exemption. |
| Bookkeeping, payroll and owners | The repository's Swedish bookkeeping, payroll, social contributions, personal income and capital gains guides concern adjacent work. Verify their date, entity scope and claims independently. An owner's personal capital rate is not the AB's company rate; an AB's pension payroll tax is not an ordinary wage contribution. |


**Governing source wording.** Read dates are the recorded selected readings; apply the conditions and version limits above.

| Figure or rule | Exact official wording | Read on | Source |
| --- | --- | --- | --- |
| Coupon tax 30% | '5 § Kupongskatt utgår med trettio procent av utdelningen.' | 2026-11-01 | [Coupon Tax Act, 5 §](https://data.riksdagen.se/dokumentstatus/sfs-1970-624.json) |
| EU dividend 10% capital condition | 'Skattskyldighet gäller inte heller för en juridisk person i en främmande stat som är medlem i Europeiska unionen, om den innehar 10 procent eller mer av andelskapitalet i det utdelande bolaget och uppfyller villkoren i artikel 2 i rådets direktiv 2011/96/EU av den 30 november 2011 om ett gemensamt beskattningssystem för moderbolag och dotterbolag hemmahörande i olika medlemsstater.' | 2026-11-01 | [Coupon Tax Act, 4 §](https://data.riksdagen.se/dokumentstatus/sfs-1970-624.json) |
| Non-CSD AB 4 months/15 January | '15 § Aktiebolag skall senast fyra månader efter utdelningstillfället, dock senast den 15 januari påföljande år, lämna Skatteverket de blanketter med uppgifter om utdelning som inkommit till bolaget samt inbetala kupongskatt för dels den utdelning för vilken med hänsyn till innehållet i uppgifterna skatt skolat innehållas, dels den utdelning för vilken uppgift ännu ej inkommit till bolaget, och dels den utdelning för vilken inkommit uppgifter som befunnits ofullständiga. Lag (2003:647).' | 2026-11-01 | [Coupon Tax Act, 15 §](https://data.riksdagen.se/dokumentstatus/sfs-1970-624.json) |
| Written refund claim, 5th following calendar year | 'Ansökan om återbetalning ska göras skriftligen hos Skatteverket senast vid utgången av femte kalenderåret efter utdelningstillfället.' | 2026-11-01 | [Coupon Tax Act, 27 §](https://data.riksdagen.se/dokumentstatus/sfs-1970-624.json) |
| DAC6 30-day adviser trigger | '19 § De uppgifter som en rådgivare ska lämna enligt 16 § ska ha kommit in till Skatteverket inom 30 dagar från och med dagen efter den av följande dagar som inträffar först: 1. den dag rådgivaren gjorde arrangemanget tillgängligt, 2. den dag arrangemanget blev klart för genomförande, eller 3. den dag rådgivaren påbörjade genomförandet av arrangemanget. Om uppgifterna ska lämnas av en rådgivare som avses i 6 § andra stycket, räknas tiden i stället från och med dagen efter den dag då denne tillhandahöll sina tjänster avseende arrangemanget. Lag (2020:437).' | 2026-11-01 | [SFL 33b:19](https://data.riksdagen.se/dokumentstatus/sfs-2011-1244.json) |
| CbCR Swedish SEK 7bn and secondary EUR 750m conditions | '6 § En multinationell koncern är undantagen från skyldigheten att lämna land-för-land-rapport om den enligt sin koncernredovisning har sammanlagda intäkter på mindre än 7 miljarder kronor för det räkenskapsår som omedelbart föregår det räkenskapsår som rapporten skulle omfatta. En enhet som avses i 5 § är undantagen från skyldigheten att lämna en land-för-land-rapport om moderföretaget är undantaget från sådan rapporteringsskyldighet i den stat eller jurisdiktion där det hör hemma till följd av att de sammanlagda intäkter som avses i första stycket understiger 750 miljoner euro eller motsvarande belopp i lokal valuta.' | 2026-11-01 | [SFL 33a:6](https://data.riksdagen.se/dokumentstatus/sfs-2011-1244.json) |
| CbCR 12 months and year-end notification | '11 § En land-för-land-rapport ska ha kommit in till Skatteverket inom tolv månader efter utgången av det rapporterade räkenskapsåret. Lag (2017:185). 12 § Underrättelser enligt 8 § och 9 § första stycket ska ha kommit in till Skatteverket före det rapporterade räkenskapsårets utgång.' | 2026-11-01 | [SFL 33a:11–12](https://data.riksdagen.se/dokumentstatus/sfs-2011-1244.json) |
| 2025 coupon amendment application | '1. Denna lag träder i kraft den 1 januari 2026. 2. Lagen tillämpas på utdelning som lämnas efter den 31 december 2025.' | 2026-11-01 | [SFS 2025:1353, transition](https://svenskforfattningssamling.se/sites/default/files/sfs/2025-11/SFS2025-1353.pdf) |
| 2026 coupon amendment application | '1. Denna lag träder i kraft den 1 juli 2026. 2. Lagen tillämpas första gången på utdelning där utdelningstillfället inträffar efter ikraftträdandet.' | 2026-11-01 | [SFS 2026:840, transition](https://svenskforfattningssamling.se/sites/default/files/sfs/2026-05/SFS2026-840.pdf) |
| CbCR amendment information-year application | '2. Lagen tillämpas första gången för uppgifter som avser kalenderåret 2026.' | 2026-11-01 | [SFS 2025:1382, transition point 2](https://svenskforfattningssamling.se/sites/default/files/sfs/2025-11/SFS2025-1382.pdf) |

## Worked cases

All facts below are fictional and expressly fixed for this illustration. The company is an ordinary resident AB with a calendar 2026 year, no foundation refusal trigger, no group or international overlay and completed accounts. Profit before current income tax is **SEK 1,000,000**, including a **SEK 20,000 fine** disallowed under IL 9:9 and a **SEK 100,000 dividend** whose business-related share exemption and all relevant exceptions have been independently established. There are no other book/tax differences, losses, funds, restricted interest, pension payroll tax or credits. Those zero amounts are example facts, not defaults for a real company. [IL, 9:9, 24:32–42 and 65:10](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json)

| Computation | SEK |
| --- | ---: |
| Profit before current income tax | 1,000,000 |
| Add non-deductible fine | 20,000 |
| Remove verified exempt dividend | (100,000) |
| Taxable surplus before rounding | 920,000 |
| Taxable surplus rounded down to full SEK 10 | 920,000 |
| Ordinary tax: 920,000 × 20.6% | **189,520** |

With no other tax entries, book profit after current tax is **SEK 810,480**. The form bridge starts at INK2R 3.26 / INK2S 4.1: 810,480 + 189,520 current tax addback + 20,000 fine − 100,000 exempt dividend = **920,000**, reported through 4.15 to 1.1. Starting the working paper before tax at 1,000,000 and adding 189,520 again would overstate the base. The example does not determine a final tax account payment, which also needs preliminary decisions, payments, other assessments and interest. [Skatteverket filing guidance](https://www.skatteverket.se/foretag/inkomstdeklaration/deklareraatettaktiebolagellerenekonomiskforening/saharlamnarduinochfylleriinkomstdeklarationen.4.262c54c219391f2e96322d7.html) [SFL, chs. 56, 62 and 65](https://data.riksdagen.se/dokumentstatus/sfs-2011-1244.json)


```oa-check
name: Ordinary 2026 AB reconciliation and after-tax bridge
inputs:
  book_profit_before_tax: 1000000
  non_deductible_fine: 20000
  verified_exempt_dividend: 100000
  rate_percent: 20.6
steps:
  - surplus: book_profit_before_tax + non_deductible_fine - verified_exempt_dividend
  - taxable_income: floor(surplus / 10) * 10
  - current_tax: pct(taxable_income, rate_percent)
  - book_profit_after_tax: book_profit_before_tax - current_tax
  - form_bridge: book_profit_after_tax + current_tax + non_deductible_fine - verified_exempt_dividend
expected:
  taxable_income: 920000
  current_tax: 189520
  book_profit_after_tax: 810480
  form_bridge: 920000
```

### Separate illustrations of the 2026 amounts

These are independent fictional cases, not additions to the ordinary computation above. They assume the scoped calendar 2026 year and expressly verified eligibility and records. Do not transfer those assumptions to an actual company.

| Case | Calculation and boundary |
| --- | --- |
| Equipment low-value boundary | For unrelated qualifying equipment with a life over 3 years, an acquisition value of SEK 29,599 excluding VAT is below the SEK 29,600 boundary; a value of SEK 29,600 is not. Connected acquisitions must still be aggregated. Failure of this route does not determine another depreciation or short-life route. [IL, 18:3–4](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) [2026 ordinance](https://data.riksdagen.se/dokumentstatus/sfs-2025-872.json) |
| Ordinary pension premium and SLP | Assume one employee has SEK 2,000,000 of pensionable remuneration under the agreement and a qualifying secured premium of SEK 650,000. The ordinary deduction is the lowest of the cost, 35% of remuneration (SEK 700,000) and 10 ordinary price base amounts (SEK 592,000): **SEK 592,000**. Add back **SEK 58,000** if the whole premium was expensed. If that premium is the only SLP base item, with no exclusion or other adjustment, SLP is 650,000 × 24.26% = **SEK 157,690**. The deduction ceiling does not reduce this separate base. [IL, 28:2–6 and 13–15](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) [SLP, 1–2 §§](https://data.riksdagen.se/dokumentstatus/sfs-1991-687.json) [2026 ordinance](https://data.riksdagen.se/dokumentstatus/sfs-2025-872.json) |
| Periodisation-fund deemed income | Assume valid opening funds total SEK 100,000 for the full 12-month 2026 year. Deemed income is 100,000 × 2.55% = **SEK 2,550**. It is an income adjustment, not the tax charge or the new fund deduction. [IL, 30:6a](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) [Reference-rate table](https://www4.skatteverket.se/rattsligvagledning/edition/2026.14/341469.html) |
| Pension provision item j | Assume a qualifying opening provision of SEK 100,000, a full 12-month 2026 year and no full release during that year. The item-j reduction is 100,000 × 85% × 2.36% = **SEK 2,006**. Other statutory base items still determine the total SLP base; this is not a deduction from every premium or from SLP itself. [SLP, 2 §](https://data.riksdagen.se/dokumentstatus/sfs-1991-687.json) [SKV A 2026:1](https://www4.skatteverket.se/rattsligvagledning/edition/2026.14/468722.html) |

```oa-check
name: Ordinary pension deduction and separate SLP base, 2026
inputs:
  pensionable_remuneration: 2000000
  qualifying_premium: 650000
  ordinary_price_base_amount: 59200
steps:
  - remuneration_limit: pct(pensionable_remuneration, 35)
  - price_base_limit: ordinary_price_base_amount * 10
  - deductible_premium: min(qualifying_premium, remuneration_limit, price_base_limit)
  - add_back: qualifying_premium - deductible_premium
  - separate_slp: pct(qualifying_premium, 24.26)
expected:
  deductible_premium: 592000
  add_back: 58000
  separate_slp: 157690
```

### Decision case: compare 2 eligible equipment methods

This independent fictional comparison fixes the opening statutory equipment basis at SEK 100,000, a full 12-month 2026 year, no additions, disposals or other basis adjustments and a taxable business surplus before the illustrated depreciation of SEK 100,000. Assume separately established eligibility for each method, with orderly closed accounts and the required accounting correspondence for the book-conforming alternative. The complementary method and every other adjustment, loss, reserve, relief and separate tax are absent by explicit example assumption. These are not defaults for a company. [IL, 18:13–17 and 65:10](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json)

At the stated maxima, book-conforming depreciation is SEK 30,000 and residual-value depreciation is SEK 25,000. Their taxable incomes are SEK 70,000 and SEK 75,000; ordinary current tax is SEK 14,420 and SEK 15,450 respectively. The book-conforming alternative therefore reduces this illustrated year's ordinary tax by SEK 1,030. It is the lower current-tax result only if that method and its accounting conditions are available. This comparison does not establish total lifetime savings, future rates, cash payment or a permitted method change; refer those decisions with the actual records. [IL, 18:13–17 and 65:10](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json)



The governing wording, read on 1 November 2026, is:

> Värdeminskningsavdrag får för ett visst beskattningsår göras vid räkenskapsenlig avskrivning med högst 30 procent och vid restvärdesavskrivning med högst 25 procent per år av avskrivningsunderlaget.

[IL 18:13](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json). The source continues with the statutory basis and conditions; the scoped assumptions above do not remove them.

> För juridiska personer är den statliga inkomstskatten 20,6 procent av den beskattningsbara inkomsten.

[IL 65:10](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json); use the application-period qualifications in the rates section.

```oa-check
name: Conditional 2026 equipment method decision, current tax only
inputs:
  opening_statutory_basis: 100000
  surplus_before_illustrated_depreciation: 100000
steps:
  - book_conforming_deduction: pct(opening_statutory_basis, 30)
  - residual_value_deduction: pct(opening_statutory_basis, 25)
  - book_conforming_taxable: floor((surplus_before_illustrated_depreciation - book_conforming_deduction) / 10) * 10
  - residual_value_taxable: floor((surplus_before_illustrated_depreciation - residual_value_deduction) / 10) * 10
  - book_conforming_tax: pct(book_conforming_taxable, 20.6)
  - residual_value_tax: pct(residual_value_taxable, 20.6)
  - current_tax_difference: residual_value_tax - book_conforming_tax
expected:
  book_conforming_deduction: 30000
  residual_value_deduction: 25000
  book_conforming_tax: 14420
  residual_value_tax: 15450
  current_tax_difference: 1030
```

### Separate penalty cases with fixed facts

These 4 fictional cases are independent. In the first case, omitted taxable income is SEK 100,000, the ordinary 20.6% rate applies and the entire amount creates a tax shortfall. The ordinary incorrect-information surcharge conditions are established, with no timing error, exception, relief, other issue or loss interaction: tax shortfall is **SEK 20,600** and the 40% surcharge is **SEK 8,240**. In the second case, the same SEK 20,600 tax shortfall is instead wholly a qualifying statutory timing error: the 10% surcharge is **SEK 2,060**. The lower rate is not an election. In the third case, a wrongly credited SEK 100,000 deficit is wholly unused that year and the ordinary 40% rate applies to the quarter-loss base: **SEK 10,000**, without treating the deficit as a current tax shortfall. In the fourth case, all 3 ordinary late-INK2 fees have validly arisen and no relief applies: 3 × 6,250 = **SEK 18,750**. None of these assumptions establishes liability for a taxpayer. [IL, 65:10](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) [SFL, 48:6–7 and 49:11–14](https://data.riksdagen.se/dokumentstatus/sfs-2011-1244.json)

```oa-check
name: Independent ordinary AB penalty cases, fixed conditions
inputs:
  omitted_taxable_income: 100000
  wrongly_credited_unused_loss: 100000
  late_fee_count: 3
steps:
  - tax_shortfall: pct(omitted_taxable_income, 20.6)
  - ordinary_surcharge: pct(tax_shortfall, 40)
  - timing_error_surcharge: pct(tax_shortfall, 10)
  - unused_loss_base: wrongly_credited_unused_loss / 4
  - unused_loss_surcharge: pct(unused_loss_base, 40)
  - combined_late_fees: late_fee_count * 6250
expected:
  tax_shortfall: 20600
  ordinary_surcharge: 8240
  timing_error_surcharge: 2060
  unused_loss_surcharge: 10000
  combined_late_fees: 18750
```

## When to refuse or refer

Apply R-CIT-1 to R-CIT-12 from the foundation, using its complete canonical code and message when a trigger fires. Do not replace those messages with the descriptions in this guide. Record the cleared and fired triggers. In addition, hold the following work for a qualified practitioner and the missing sources:

| Case | Required action |
| --- | --- |
| Another financial year, a non-resident branch or a special entity or regime | Requalify the entity, law version and application dates before computing. |
| An actual treaty claim, foreign establishment, CFC inclusion, shell-company transaction or group relief claim | Complete the relevant transaction and international analysis; the screens in this guide do not produce that result. |
| A triggered Pillar Two group | Obtain a complete top-up calculation, elections and separate reporting/payment analysis. Ordinary corporate tax can be a component, but is not the group result. |
| An unqualified asset basis, pension promise, reserve vintage, loss history or credit | Obtain the required ledger and legal treatment. Continue only the separable work whose inputs are established. |
| A future service, attachment route, signatory or payment instruction not confirmed for the actual return | Prepare the reconciliation; retain the filing or payment hold. |

## Completion checklist

Run all foundation domain and universal checks. In addition, the reviewer must be able to trace these items:

1. Entity, residence, 2026 financial year, accounting framework and the complete refusal screen.
2. Signed accounts, book result before/after tax and one reconciled bridge to INK2S; no duplicated income tax, group contribution or fund.
3. Evidence and application dates for every adjustment; separate asset, interest, pension, reserve, loss and credit schedules.
4. Reserve rates and vintages, price base amount where used, ownership history, group allocations and any statutory ordering.
5. Taxable-base rounding, current tax, credit limitation and a separately supported pension payroll tax base.
6. International, CFC, hybrid, TP, DAC6, CbCR and Pillar Two screens, with triggered analyses referred rather than assumed clear.
7. All return parts and attachments, actual service availability, representation rights, signature and both receipts; separate accounting/audit obligations.
8. Filing date and any decision-based extension; preliminary decisions, tax account cash postings, interest and final notice.
9. Late-return fee clocks, surcharge definition/base/exceptions, correction history, any relief grounds and the actual rates for each interest period.

Record an unresolved item's amount or affected step, missing evidence, owner and effect on calculation, filing or payment. Do not label the return ready whilst a required item is unresolved. This guide does not implement full BFNAR accounting, technical BAS/SRU mapping, specialist international computations, treaty entitlement, historical transactions or the actual 2027 service. A live computation also needs an authoritative check for later applicable amendments.

## Sources

The initial sources were retrieved by **1 November 2026**; the procedure statute, selected penalty provisions, 2 original amendments and the tax-account interest page were checked on **2 November 2026**. Riksdagen's API reproductions were read as dated statutory text, including relevant reproduced transitions and selected original SFS instruments. They do not prove a complete historical amendment chain. In particular, the IL reproduction contains future wording and omitted annexes: use the provision applicable to the scoped year, not every paragraph returned by the API. Foreign annex eligibility, actual approvals and taxpayer facts remain unqualified.


The read dates identify the selected statutory and official-guidance readings recorded in the 1 November 2026 source qualification rounds, including the separate numeric-source check. They do not claim a complete reading of every long act or approval of future service availability. The 2 November rows identify the additional live and selected-text checks; older rows retain their actual earlier read dates. The version and reading limits below remain material.

| Source | URL | Read on | Version used or qualification |
| --- | --- | --- | --- |
| [IL (1999:1229)](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) | https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json | 2026-11-01 | Riksdagen reproduction through SFS 2026:1393; includes future provisions. Selected original changes and reproduced transitions support the ordinary 2026 rules stated here. Part read: Selected sections 1:7, 1:15, 2:27 and 6:3–4; business-income, asset, interest, pension, fund, loss, credit and international provisions cited in the method, with selected complete chapters and reproduced transitions. |
| [SFL (2011:1244)](https://data.riksdagen.se/dokumentstatus/sfs-2011-1244.json) | https://data.riksdagen.se/dokumentstatus/sfs-2011-1244.json | 2026-11-01 | Reproduction through SFS 2026:1305; use the actual reporting period and application clauses. Part read: Selected sections 3:5, 32:2 and 36:4, return/reporting provisions in chapters 33a–33d and 39, and assessment/payment/interest provisions in chapters 56, 62 and 65. |
| [ÅRL (1995:1554)](https://data.riksdagen.se/dokumentstatus/sfs-1995-1554.json) | https://data.riksdagen.se/dokumentstatus/sfs-1995-1554.json | 2026-11-01 | Reproduction through SFS 2026:780; selected accounting definitions and annual-report requirements, not a complete accounting implementation. Part read: Selected sections in chapters 1, 2 and 4 on entity/group definitions, annual reports and imported valuation definitions. |
| [Aktiebolagslagen (2005:551)](https://data.riksdagen.se/dokumentstatus/sfs-2005-551.json) | https://data.riksdagen.se/dokumentstatus/sfs-2005-551.json | 2026-11-01 | Reproduction through SFS 2026:783; audit provisions 9:1–1a and reproduced SFS 2010:834 transition. Actual registration and special rules need confirmation. Part read: Sections 9:1–1a and reproduced SFS 2010:834 transition. |
| [SLP (1991:687)](https://data.riksdagen.se/dokumentstatus/sfs-1991-687.json) | https://data.riksdagen.se/dokumentstatus/sfs-1991-687.json | 2026-11-01 | Reproduction through SFS 2019:874; complete statutory base and selected pension income-tax provisions read. Part read: Complete operative sections 1–5 and reproduced transitions, including the entire section 2 base and its adjustments. |
| [2026 price-base ordinance (2025:872)](https://data.riksdagen.se/dokumentstatus/sfs-2025-872.json) | https://data.riksdagen.se/dokumentstatus/sfs-2025-872.json | 2026-11-01 | Complete retained API text sets the ordinary price base amount at SEK 59,200 for 2026. The separate higher amount is not used in the calculations above. Part read: Complete short ordinance, including section 1 ordinary price base amount. |
| [SKV A 2026:1](https://www4.skatteverket.se/rattsligvagledning/edition/2026.14/468722.html) and [reference-rate table](https://www4.skatteverket.se/rattsligvagledning/edition/2026.14/341469.html) | https://www4.skatteverket.se/rattsligvagledning/edition/2026.14/468722.html<br>https://www4.skatteverket.se/rattsligvagledning/edition/2026.14/341469.html | 2026-11-01 | Current edition 2026.14 checked against the earlier edition. The advice sets the 2025 annual average at 2.36% for tax years starting in 2026; the table separately records 2.55% at the end of November 2025. Part read: Complete SKV A 2026:1 advice and the separate 2025 end-November row of the government-borrowing-rate table. |
| [Foreign Tax Credit Act (1986:468)](https://data.riksdagen.se/dokumentstatus/sfs-1986-468.json) | https://data.riksdagen.se/dokumentstatus/sfs-1986-468.json | 2026-11-01 | Reproduction through SFS 2025:1354; ordinary route qualified, historic truncated transition and special routes held. Part read: Selected ordinary-relief provisions in chapter 2, including sections 9–10 and carryforward/limitation interaction; special and historical branches held. |
| [GAAR (1995:575)](https://data.riksdagen.se/dokumentstatus/sfs-1995-575.json) | https://data.riksdagen.se/dokumentstatus/sfs-1995-575.json | 2026-11-01 | Reproduction through SFS 2011:1372; complete short act read. Part read: Complete short act, sections 1–4 and reproduced transition. |
| [Top-up Tax Act (2023:875)](https://data.riksdagen.se/dokumentstatus/sfs-2023-875.json) | https://data.riksdagen.se/dokumentstatus/sfs-2023-875.json | 2026-11-01 | Reproduction through SFS 2026:305; perimeter, selected safe harbours and reporting screens, not a full calculation. Part read: Selected perimeter, charging, safe-harbour and reporting provisions in chapters 1, 2, 6 and 8 and their cited transitions. |
| [Coupon Tax Act (1970:624)](https://data.riksdagen.se/dokumentstatus/sfs-1970-624.json) | https://data.riksdagen.se/dokumentstatus/sfs-1970-624.json | 2026-11-01 | Reproduction through SFS 2026:840, with the selected original 2025 and 2026 amendments read. Part read: Selected sections 1, 4–5, 7–15 and 27, plus selected original 2025/2026 amendments and their application clauses. |
| [BFN annual-report guidance](https://www.bfn.se/fragor-och-svar/arsredovisning/) | https://www.bfn.se/fragor-och-svar/arsredovisning/ | 2026-11-01 | Page updated 25 September 2026; actual K2/K3 eligibility still requires the applicable framework. Part read: Selected annual-report FAQ entries on K2/K3 framework eligibility and changed application dates. |
| [Skatteverket return guidance](https://www.skatteverket.se/foretag/inkomstdeklaration/deklareraatettaktiebolagellerenekonomiskforening/saharlamnarduinochfylleriinkomstdeklarationen.4.262c54c219391f2e96322d7.html) | https://www.skatteverket.se/foretag/inkomstdeklaration/deklareraatettaktiebolagellerenekonomiskforening/saharlamnarduinochfylleriinkomstdeklarationen.4.262c54c219391f2e96322d7.html | 2026-11-01 | Current service, authority, signature and attachment rules; future open periods require confirmation. The official blank calendar-2026 form was also examined. Part read: Selected return preparation, INK2R/INK2S mapping, service, authority, signature, attachment and acceptance sections; blank calendar-2026 form fields described in the method. |
| DAC6 | https://data.riksdagen.se/dokumentstatus/sfs-2020-434.json | 2026-11-01 | Part read: Selected sections on hallmarks, roles and main-benefit conditions; read with SFL ch. 33b, not a concluded arrangement. |
| CBCR | https://data.riksdagen.se/dokumentstatus/sfs-2017-182.json | 2026-11-01 | Part read: Selected sections and reproduced transition for calendar-2026 information; reporting and parent/exchange roles remain conditional. |
| HOLIDAY | https://data.riksdagen.se/dokumentstatus/sfs-1930-173.json | 2026-11-01 | Part read: Complete short act; section 2 business-day adjustment used for the illustrated statutory date. |
| INTEREST-2025 | https://svenskforfattningssamling.se/sites/default/files/sfs/2025-11/SFS2025-1333.pdf | 2026-11-01 | Part read: SFS 2025:1333, amended IL interest provisions and complete commencement/application clauses. |
| GIFT-2025 | https://svenskforfattningssamling.se/sites/default/files/sfs/2025-11/SFS2025-1361.pdf | 2026-11-01 | Part read: SFS 2025:1361, selected legal-person gift-credit provisions and complete transition, including point 4. |
| KUP-2025 | https://svenskforfattningssamling.se/sites/default/files/sfs/2025-11/SFS2025-1353.pdf | 2026-11-01 | Part read: SFS 2025:1353, operative coupon-tax change and complete transition for dividends paid after 31 December 2025. |
| KUP-2026 | https://svenskforfattningssamling.se/sites/default/files/sfs/2026-05/SFS2026-840.pdf | 2026-11-01 | Part read: SFS 2026:840, operative coupon-tax changes and complete commencement/application provisions; boundary events held. |
| SKV-AB | https://www.skatteverket.se/foretag/drivaforetag/foretagsformer/aktiebolag.4.5c13cb6b1198121ee8580002546.html | 2026-11-01 | Part read: Selected sections on ordinary AB tax, preliminary/final tax and scoped interest avoidance dates; live balance and rates remain unconfirmed. |
| SKV-DATES | https://www4.skatteverket.se/rattsligvagledning/edition/2026.14/325640.html | 2026-11-01 | Part read: Selected filing-date table and sections on the wholly electronic condition, all return parts and year-end date adjustment. |
| SKV-PENSION | https://www.skatteverket.se/foretag/drivaforetag/foretagsformer/aktiebolag/sarskildloneskatt.4.6e8a1495181dad540843a8.html | 2026-11-01 | Part read: Selected sections on ordinary pension costs, separate SLP base and return guidance; individual arrangement remains unconfirmed. |
| FORM | https://www.skatteverket.se/4.39f16f103821c58f680006188.html | 2026-11-01 | Part read: Official form service and the retained blank calendar-2026 INK2/INK2R/INK2S, selected fields described above; future service/schema acceptance unconfirmed. |
| SFL ordinary penalties and relief | https://data.riksdagen.se/dokumentstatus/sfs-2011-1244.json | 2026-11-02 | Current API statutory text was compared byte for byte with the retained 1 November reproduction and is unchanged. Part read: Complete chapters 48, 49 and 51, plus the selected interest/payment provisions cited above; ordinary AB scope, not a whole-law attestation. |
| SFS 2026:110 | https://svenskforfattningssamling.se/sites/default/files/sfs/2026-02/SFS2026-110.pdf | 2026-11-02 | Complete one-page original amendment to SFL 49:4–5 and its 1 April 2026 commencement clause read. |
| SFS 2026:146 | https://svenskforfattningssamling.se/sites/default/files/sfs/2026-02/SFS2026-146.pdf | 2026-11-02 | Complete one-page original amendment to SFL 65:13 and its 2 April 2026 commencement clause read. The gazette identifies a law; use it for identity and commencement where the consolidated reproduction labels its amendment marker 'Förordning (2026:146)'. |
| SFS 2026:303 | https://svenskforfattningssamling.se/sites/default/files/sfs/2026-03/SFS2026-303.pdf | 2026-11-01 | Part read: Complete retained original amendment, including SFL 49:8, the selected top-up provisions and 1 May 2026 commencement clause. |
| Skatteverket tax-account interest | https://www.skatteverket.se/rantapaskattekontot | 2026-11-02 | Part read: Daily balance/monthly posting explanation, low/high cost-interest rates and effective date, and their pre-due/post-due/enforcement boundaries. The page's individual-taxpayer payment example is not imported into this AB guide. Rates are a dated snapshot, not a 2027 forecast. |

Not yet confirmed: complete historical amendment chains and omitted annex eligibility; actual entity, treaty, group, asset, pension, reserve, loss and credit positions; a complete BFNAR/BAS/SRU implementation; actual 2027 service, schema, attachments, representation, acceptance and payment details; actual penalty liability, procedural dates, exceptions and relief, and the rates and postings for each actual interest period; specialist calculations and professional sign-off. Conditional examples establish none of those facts. Keep the applicable calculation, filing and payment holds.

[IL]: https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json
[SFL]: https://data.riksdagen.se/dokumentstatus/sfs-2011-1244.json
[ARL]: https://data.riksdagen.se/dokumentstatus/sfs-1995-1554.json
[ABL]: https://data.riksdagen.se/dokumentstatus/sfs-2005-551.json
[SLP]: https://data.riksdagen.se/dokumentstatus/sfs-1991-687.json
[PBB-2026]: https://data.riksdagen.se/dokumentstatus/sfs-2025-872.json
[SLR-AVERAGE-2025]: https://www4.skatteverket.se/rattsligvagledning/edition/2026.14/468722.html
[SLR-TABLE]: https://www4.skatteverket.se/rattsligvagledning/edition/2026.14/341469.html
[FTC]: https://data.riksdagen.se/dokumentstatus/sfs-1986-468.json
[GAAR]: https://data.riksdagen.se/dokumentstatus/sfs-1995-575.json
[P2]: https://data.riksdagen.se/dokumentstatus/sfs-2023-875.json
[KUP]: https://data.riksdagen.se/dokumentstatus/sfs-1970-624.json
[DAC6]: https://data.riksdagen.se/dokumentstatus/sfs-2020-434.json
[CBCR]: https://data.riksdagen.se/dokumentstatus/sfs-2017-182.json
[HOLIDAY]: https://data.riksdagen.se/dokumentstatus/sfs-1930-173.json
[INTEREST-2025]: https://svenskforfattningssamling.se/sites/default/files/sfs/2025-11/SFS2025-1333.pdf
[GIFT-2025]: https://svenskforfattningssamling.se/sites/default/files/sfs/2025-11/SFS2025-1361.pdf
[KUP-2025]: https://svenskforfattningssamling.se/sites/default/files/sfs/2025-11/SFS2025-1353.pdf
[KUP-2026]: https://svenskforfattningssamling.se/sites/default/files/sfs/2026-05/SFS2026-840.pdf
[SKV-AB]: https://www.skatteverket.se/foretag/drivaforetag/foretagsformer/aktiebolag.4.5c13cb6b1198121ee8580002546.html
[SKV-DATES]: https://www4.skatteverket.se/rattsligvagledning/edition/2026.14/325640.html
[SKV-FILING]: https://www.skatteverket.se/foretag/inkomstdeklaration/deklareraatettaktiebolagellerenekonomiskforening/saharlamnarduinochfylleriinkomstdeklarationen.4.262c54c219391f2e96322d7.html
[SKV-PENSION]: https://www.skatteverket.se/foretag/drivaforetag/foretagsformer/aktiebolag/sarskildloneskatt.4.6e8a1495181dad540843a8.html
[BFN]: https://www.bfn.se/fragor-och-svar/arsredovisning/
[FORM]: https://www.skatteverket.se/4.39f16f103821c58f680006188.html

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained in the
[ryanduguid/openaccountants fork](https://github.com/ryanduguid/openaccountants).
Check its quality tier, recorded review status and cited sources before use.
Choose a practitioner whose credentials and engagement scope you have verified.
The links below are optional upstream services; they do not publish or verify
this fork's changes.

- Upstream connection service: https://www.openaccountants.com/connect
- Upstream accountant network: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
