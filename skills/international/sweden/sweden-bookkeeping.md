---
name: sweden-bookkeeping
description: Swedish bookkeeping reference for BAS account selection, bank reconciliation and working-paper presentation, with selected 2026 K2/K3 conditions and explicit holds for incomplete entity, tax and filing workflows. Load with bookkeeping-workflow-base; professional review is required.
version: 1.6
jurisdiction: SE
tax_year: 2026
tax_year_notes: "2026 BAS and selected accounting rules for financial years beginning after 31 December 2025; the extended-first-year selector is stated below. Earlier 2025 tax shortcuts are withdrawn from operative use pending qualification."
last_updated: 2026-11-03
review_status: pending_review
depends_on:
  - bookkeeping-workflow-base
category: bookkeeping
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Sweden Bookkeeping

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## What this file is

Load this reference with `bookkeeping-workflow-base`. Sweden uses SEK in these working papers; verify any other permitted presentation/bookkeeping currency separately. BFN means Bokföringsnämnden (the Swedish Accounting Standards Board). The BAS reference uses 4-digit account codes in financial-accounting classes 1–8. It supplies a checked BAS account subset, selected recognition and presentation conditions, bank-reconciliation controls and fictional working-paper cases. The reviewer is the customer of the outputs: trial balance, P&L, balance sheet, reviewer brief and transaction register. This is Tier 2 material pending professional review. It is not a return, a complete annual report or a filing instruction.

**Coverage year:** 2026 BAS and selected accounting rules for financial years beginning after 31 December 2025; the extended-first-year selector is stated below. Earlier 2025 tax shortcuts are withdrawn from operative use pending qualification.

The 2026 rules were selected from the cited primary editions. The Sources table distinguishes the parts read from unqualified framework, tax, bank-format and filing work. This version does not establish full conformance with every mandatory country slot of the workflow base.

## Scope

The supported core is BAS account selection and a controlled working-paper workflow for an ordinary Swedish private AB after its financial year, K2 eligibility, source documents and accounting policies have been established. K3, sole traders, partnerships, groups, first adoption and other legal forms remain in the overall coverage objective. Their incomplete recognition, tax and reporting workflows are held explicitly rather than inferred from the AB rules.

### Ask the client first

1. Confirm legal form, registration, ownership, group and foreign-branch facts, regulated activities and any crypto, share-based or compound-debt transactions; provide the 2 preceding annual accounts and framework decision.
2. Confirm the actual financial year, first-year or transition status, bookkeeping method, currency, VAT status and adopted recognition, materiality and depreciation policies.
3. Provide every source statement, invoice, receipt and journal, opening trial balance, subledgers and closing balances, with a complete period and evidence of duplicates and inter-account transfers.
4. Identify private/related-party transactions, fixed assets, inventory, payroll, pensions, taxes, reserves, commitments and subsequent events; supply their reconciliations and approval documents.
5. Specify the output and review purpose, intended annual-report/filing route and authorised reviewer. Obtain an actual export sample and field definitions before parsing bank or SIE data.

### Financial year and framework selector

A normal year is 12 calendar months. Natural persons, partnerships whose income is wholly or partly taxed to a natural person and the specified community-management entities normally use the calendar year. Other entities, including ABs, may use a non-calendar year. Entry or change can permit a shorter year or extension up to 18 months; cessation can shorten it. Apply the common-year and permission conditions before changing a period. ([BFL 3:1–6](https://data.riksdagen.se/dokumentstatus/sfs-1999-1078.json))

K2 BFNAR 2016:10 requires smaller status and the complete chapter 1 screen. Its 1.1A exclusions include public ABs, specified parents/groups, natural persons and estates, housing associations, foreign branches, specified share-based and compound financial instruments and crypto holdings subject to the narrow occasional-payment exception. Paragraph 1.1B adds the specified material deferred-tax-liability and building-revenue tests. Paragraph 1.1C supplies narrow relief from 1.1B only, not from 1.1A. Reassess the full conditions before using this guide. ([K2 1.1–1.1C and commentary, pp15–24](https://www.bfn.se/wp-content/uploads/vl16-10-k2ar-kons2025.pdf))

The cited K2 BFNAR 2025:2 edition ordinarily applies to years beginning after 31 December 2025. A business beginning after 30 June 2025 with an extended first year ending on 31 December 2026 or later has the specific earlier selector. New valuation methods apply only to new transactions and items remeasured each balance date; the previous year's statement figures are not restated and the lack of comparability is disclosed. Do not apply this edition indiscriminately to ordinary 2025 accounts. ([BFNAR 2025:2 transition points 1–2, p333](https://www.bfn.se/wp-content/uploads/vl16-10-k2ar-kons2025.pdf))

K3 is the ÅRL default within its scope, subject to the specified IFRS and RFR 2 alternatives and exclusions. RFR 2 concerns supplementary rules for legal persons; it is not a synonym for consolidated IFRS. Select that framework separately. ([K3 1.3 and BFNAR 2025:3–4 transitions](https://www.bfn.se/wp-content/uploads/vl12-1-k3-kons20251215.pdf))

## Filing requirements

Every AB must close its books with an annual report; low turnover does not permit an AB to choose simplified annual closing. Other entities need the complete BFL 6:1 screen before applying BFL 6:3. A statutory simplified-closing gate does not itself qualify every K1 mechanic. ([BFL 6:1–3](https://data.riksdagen.se/dokumentstatus/sfs-1999-1078.json))

For an AB, certified copies of the required documents must reach the registry within one month after the meeting adopts the balance sheet and income statement. A director or managing director certifies adoption, the adoption date and the profit/loss appropriation decision. The 7-month first-fee threshold is a separate conditional rule; the specified continued-meeting notification, fee and auditor-assurance conditions can extend that fee clock to 9 months. It does not replace the adoption-based filing deadline. Establish the exact required document set and review/audit facts. ([ÅRL 8:3 and 8:5–6](https://data.riksdagen.se/dokumentstatus/sfs-1995-1554.json))

**Filing hold:** this guide has not qualified the complete current Bolagsverket software/portal sequence, signers, submission fields, validation, acceptance receipt, correction route or fee/payment handling. Prepare working papers only. An actual annual report also needs the complete applicable statement formats, comparatives, notes, management report and signatures. Do not treat the short outlines below as filing templates.

Retain accounting information through the end of the seventh year after the calendar year in which the financial year ended, durably and accessibly in an orderly form. Sweden is the default storage location with conditional overseas routes. Transfer permits destruction of the former medium only under the statutory no-change/no-loss condition. No destruction is authorised by this reference. ([BFL 7:1–6](https://data.riksdagen.se/dokumentstatus/sfs-1999-1078.json))

## Rates and thresholds

These are accounting selectors, not automatic tax deductions or a general materiality allowance. BAS account names containing a percentage are account labels; their existence does not prove that rate applies to a transaction.

| Item | Amount and full selector | Period and primary source |
| --- | --- | --- |
| Payment-based ongoing recording | Annual net turnover normally at most SEK 3,000,000; all unpaid receivables and liabilities are still recorded at year end; the specified financial-sector exclusions apply | 2026 current text, [BFL 5:2–3](https://data.riksdagen.se/dokumentstatus/sfs-1999-1078.json) |
| Simplified annual closing statutory gate | Annual net turnover normally at most SEK 3,000,000 and no BFL 6:1 annual-report duty; verify the applicable K1 framework separately | 2026 current text, [BFL 6:1–3](https://data.riksdagen.se/dokumentstatus/sfs-1999-1078.json) |
| Larger-company numerical limb | More than one of the same criteria exceeds its threshold in each of the 2 relevant years: employees >50, assets >SEK 40,000,000, turnover >SEK 80,000,000; regulated-market status is a separate larger-company limb | Apply the relevant measurement and period definitions, [ÅRL 1:3](https://data.riksdagen.se/dokumentstatus/sfs-1995-1554.json) |
| K2 building-revenue exclusion | Buildings generate at least 75% of net turnover; use the latest completed annual accounts and assess the separate deferred-tax condition and narrow 1.1C relief | Post-2025 edition selector above, [K2 1.1B–1.1C](https://www.bfn.se/wp-content/uploads/vl16-10-k2ar-kons2025.pdf) |
| K2 1.1C numerical relief | At most one of the same criteria exceeds its threshold in each of the 2 relevant years: >3 employees, >SEK 1,500,000 assets, >SEK 3,000,000 turnover. This relieves only 1.1B; the separate existing-user normally-outside test is not blanket relief | Post-2025 edition selector above, [K2 1.1C](https://www.bfn.se/wp-content/uploads/vl16-10-k2ar-kons2025.pdf) |
| K2 income/expenditure accrual relief | Each income or expenditure must be strictly below SEK 7,000, testing the invoice/agreement transaction amount rather than the accrual adjustment. Aggregate artificial splits. Apply consistency and the individual/combined materiality restriction; advance payments have a separate rule | Post-2025 edition selector above, [K2 2.4–2.4B, pp31–32](https://www.bfn.se/wp-content/uploads/vl16-10-k2ar-kons2025.pdf) |
| Ordinary 2026 price base amount | SEK 59,200; half is the derived SEK 29,600, not the higher price base amount | 2026 only, [SFS 2025:872, section 1](https://data.riksdagen.se/dokumentstatus/sfs-2025-872.json) |
| K2 low-value tangible asset | Acquisition cost strictly below half the applicable price base amount with the specified addition for unrecoverable input VAT; related items/larger-investment purchases are tested together | Recognition rule, not automatic tax deduction, [K2 10.5](https://www.bfn.se/wp-content/uploads/vl16-10-k2ar-kons2025.pdf) |
| K2 short-life tangible asset | Expected economic life at most 3 years; establish the actual facts and keep the rule distinct from the low-value test | [K2 10.6](https://www.bfn.se/wp-content/uploads/vl16-10-k2ar-kons2025.pdf) |
| K2 recurring expenditure relief | Specified annually recurring non-personnel expenditure, normally expected variation at most 20%, an annual cost each year and the stated first-use exception; the combined materiality restriction still applies | [K2 7.9 and 2.4B](https://www.bfn.se/wp-content/uploads/vl16-10-k2ar-kons2025.pdf) |

## Computation rules

### Execute the workflow in order

1. Load the base and this country reference, then confirm that the supported rules cover the entity, period and job. Stop for a missing mandatory country slot; do not assume this partial reference completes it.
2. Read and count all source rows. Preserve document, page/row, currency, date, gross/net/VAT and voucher identifiers, original text, amounts and sign convention. Reconcile period coverage and duplicates before classifying.
3. Infer a provisional profile, obtain the base's confirmation and resolve the grouped intake facts above. A bank description alone is not proof of legal form, tax status, deductibility or ownership.
4. Establish opening balances, the actual chart and all customised/free accounts. Use the source-linked BAS subset below as a reference; do not silently renumber an existing ledger to the standard chart. Confirm subaccount, counterparty, nature, business/private split, recognition timing, framework, asset unit and applicable tax companion.
5. Classify only supported transactions. Record confidence, evidence and assumptions; route ambiguity to Needs Input in the reviewer brief. There is no approved sundry-account or transaction-size shortcut in this reference. The K2 accrual threshold is not permission to ignore invoices or source rows.
6. Post equal debit/credit entries. Match payments to receivables/payables instead of recording revenue/expense twice. Preserve payroll, VAT and tax controls separately. Record unresolved financial rows in the register with their hold; do not invent a balancing journal or erase a source payment.
7. Reconcile every bank/control account and subledger. Explain all unmatched items and movements, including transfers, loans, owner transactions, tax-account settlements and closing journals. Use the actual bank export's verified fields and signs.
8. Map each adjusted balance once to the selected statement format and the note/control schedules. Resolve contra assets, current debt portions, related-party captions, tax and reserve bridges and the closing status of 8999/2099. The retained outline alone cannot establish a complete annual report.
9. Produce all 5 base outputs and run all 12 base checks. Supply a trial balance, P&L, balance sheet, reviewer brief and transaction register together. Show source counts, confidence/holds, assumptions, questions/answers, bank and tax reconciliations and every reviewer action. Do not file or deliver an apparently complete set whilst a required balance or rule remains unqualified.

The source-recording and year-end adjustments distinguish ongoing payment-based recording from annual recognition. ([BFL 5:2–3](https://data.riksdagen.se/dokumentstatus/sfs-1999-1078.json)) The country/accounting rules below govern the classification and presentation; the base supplies output schemas and controls.

### Standard chart of accounts: checked BAS 2026 subset

The official file's cover says v1.1 despite its v2 URL. This subset contains main, group and selected subaccounts; it is not every BAS account or a continuous-code permission. The # legend says accounts carrying it must not be used under K2. No # does not establish recognition permission. Class 5 and class 6 are distinct classes even where they share external-cost treatment. Account types and normal directions below are derived working-paper controls, not authority to ignore an abnormal balance. ([BAS 2026 cover, legend and listed accounts](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf))

| Code | Official BAS 2026 label | Type, normal balance and condition | Primary source |
| --- | --- | --- | --- |
| 1010 # | Utvecklingsutgifter | Asset, normally debit; BAS # excludes K2 use | [BAS 2026, 1010](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 1020 | Koncessioner m.m. | Asset, normally debit; identify related contra balances separately | [BAS 2026, 1020](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 1030 | Patent | Asset, normally debit; identify related contra balances separately | [BAS 2026, 1030](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 1050 | Varumärken | Asset, normally debit; identify related contra balances separately | [BAS 2026, 1050](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 1070 | Goodwill | Asset, normally debit; identify related contra balances separately | [BAS 2026, 1070](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 1110 | Byggnader | Asset, normally debit; identify related contra balances separately | [BAS 2026, 1110](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 1120 | Förbättringsutgifter på annans fastighet | Asset, normally debit; identify related contra balances separately | [BAS 2026, 1120](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 1130 | Mark | Asset, normally debit; identify related contra balances separately | [BAS 2026, 1130](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 1210 | Maskiner och andra tekniska anläggningar | Asset, normally debit; identify related contra balances separately | [BAS 2026, 1210](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 1220 | Inventarier, verktyg och installationer | Asset, normally debit; identify related contra balances separately | [BAS 2026, 1220](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 1230 | (Fritt konto för Maskiner och andra tekniska anläggningar) | Asset candidate, normally debit; free account requires the entity's documented definition | [BAS 2026, 1230](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 1240 | (Fritt konto för Maskiner och andra tekniska anläggningar) | Asset candidate, normally debit; free account requires the entity's documented definition | [BAS 2026, 1240](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 1250 | (Fritt konto för Inventarier, verktyg och installationer) | Asset candidate, normally debit; free account requires the entity's documented definition | [BAS 2026, 1250](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 1290 | Övriga materiella anläggningstillgångar | Asset, normally debit; identify related contra balances separately | [BAS 2026, 1290](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 1310 | Andelar i koncernföretag | Asset, normally debit; identify related contra balances separately | [BAS 2026, 1310](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 1380 | Andra långfristiga fordringar | Asset, normally debit; identify related contra balances separately | [BAS 2026, 1380](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 1410 | Lager av råvaror | Asset, normally debit; identify related contra balances separately | [BAS 2026, 1410](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 1420 | Lager av tillsatsmaterial och förnödenheter | Asset, normally debit; identify related contra balances separately | [BAS 2026, 1420](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 1440 | Produkter i arbete | Asset, normally debit; identify related contra balances separately | [BAS 2026, 1440](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 1460 | Lager av handelsvaror | Asset, normally debit; identify related contra balances separately | [BAS 2026, 1460](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 1510 | Kundfordringar | Asset, normally debit; identify related contra balances separately | [BAS 2026, 1510](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 1610 | Kortfristiga fordringar hos anställda | Asset, normally debit; identify related contra balances separately | [BAS 2026, 1610](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 1630 | Avräkning för skatter och avgifter (skattekonto) | Tax-account control, debit or credit after reconciliation; not automatically a tax receivable | [BAS 2026, 1630](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 1640 | Skattefordringar | Asset, normally debit; identify related contra balances separately | [BAS 2026, 1640](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 1650 | Momsfordran | Asset, normally debit; identify related contra balances separately | [BAS 2026, 1650](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 1710 | Förutbetalda hyreskostnader | Asset, normally debit; identify related contra balances separately | [BAS 2026, 1710](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 1790 | Övriga förutbetalda kostnader och upplupna intäkter | Asset, normally debit; identify related contra balances separately | [BAS 2026, 1790](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 1910 | Kassa | Asset, normally debit; identify related contra balances separately | [BAS 2026, 1910](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 1920 | PlusGiro | Asset, normally debit; identify related contra balances separately | [BAS 2026, 1920](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 1930 | Företagskonto | Asset, normally debit; identify related contra balances separately | [BAS 2026, 1930](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 1940 | Övriga bankkonton | Asset, normally debit; identify related contra balances separately | [BAS 2026, 1940](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 2010 | Eget kapital | Owner/partner equity, normally credit; legal form and subaccount required, not generic AB equity | [BAS 2026, 2010](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 2013 | Övriga egna uttag | Owner equity movement, normally debit; not a generic AB expense | [BAS 2026, 2013](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 2018 | Övriga egna insättningar | Owner/partner equity, normally credit; legal form and subaccount required, not generic AB equity | [BAS 2026, 2018](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 2020 | Eget kapital | Owner/partner equity, normally credit; legal form and subaccount required, not generic AB equity | [BAS 2026, 2020](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 2030 | Eget kapital | Owner/partner equity, normally credit; legal form and subaccount required, not generic AB equity | [BAS 2026, 2030](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 2040 | Eget kapital | Owner/partner equity, normally credit; legal form and subaccount required, not generic AB equity | [BAS 2026, 2040](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 2081 | Aktiekapital | Liability/equity candidate, normally credit; actual nature and maturity control presentation | [BAS 2026, 2081](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 2085 | Uppskrivningsfond | Liability/equity candidate, normally credit; actual nature and maturity control presentation | [BAS 2026, 2085](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 2086 | Reservfond | Liability/equity candidate, normally credit; actual nature and maturity control presentation | [BAS 2026, 2086](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 2091 | Balanserad vinst eller förlust | Result/equity or closing transfer, debit or credit; reconcile once, never duplicate profit | [BAS 2026, 2091](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 2099 | Årets resultat | Result/equity or closing transfer, debit or credit; reconcile once, never duplicate profit | [BAS 2026, 2099](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 2110 | Periodiseringsfonder | Untaxed reserve, normally credit; eligibility and fund vintage required | [BAS 2026, 2110](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 2126 | Periodiseringsfond 2026 | Untaxed reserve, normally credit; eligibility and fund vintage required | [BAS 2026, 2126](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 2150 | Ackumulerade överavskrivningar | Untaxed reserve, normally credit; eligibility and fund vintage required | [BAS 2026, 2150](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 2310 | Obligations- och förlagslån | Liability/equity candidate, normally credit; actual nature and maturity control presentation | [BAS 2026, 2310](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 2350 | Andra långfristiga skulder till kreditinstitut | Liability/equity candidate, normally credit; actual nature and maturity control presentation | [BAS 2026, 2350](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 2390 | Övriga långfristiga skulder | Liability/equity candidate, normally credit; actual nature and maturity control presentation | [BAS 2026, 2390](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 2440 | Leverantörsskulder | Liability/equity candidate, normally credit; actual nature and maturity control presentation | [BAS 2026, 2440](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 2510 | Skatteskulder | Liability/equity candidate, normally credit; actual nature and maturity control presentation | [BAS 2026, 2510](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 2610 | Utgående moms, 25 % | Liability/equity candidate, normally credit; actual nature and maturity control presentation | [BAS 2026, 2610](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 2620 | Utgående moms, 12 % | Liability/equity candidate, normally credit; actual nature and maturity control presentation | [BAS 2026, 2620](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 2630 | Utgående moms, 6 % | Liability/equity candidate, normally credit; actual nature and maturity control presentation | [BAS 2026, 2630](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 2640 | Ingående moms | Input VAT control, normally debit for qualified recoverable input VAT; separate tax qualification and adjustment checks required | [BAS 2026, 2640](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 2650 | Redovisningskonto för moms | VAT settlement control, debit or credit according to the reconciled payable/receivable position | [BAS 2026, 2650](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 2710 | Personalskatt | Liability/equity candidate, normally credit; actual nature and maturity control presentation | [BAS 2026, 2710](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 2730 | Lagstadgade sociala avgifter och särskild löneskatt | Liability/equity candidate, normally credit; actual nature and maturity control presentation | [BAS 2026, 2730](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 2731 | Avräkning lagstadgade sociala avgifter | Liability/equity candidate, normally credit; actual nature and maturity control presentation | [BAS 2026, 2731](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 2790 | Övriga löneavdrag | Liability/equity candidate, normally credit; actual nature and maturity control presentation | [BAS 2026, 2790](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 2890 | Övriga kortfristiga skulder | Liability/equity candidate, normally credit; actual nature and maturity control presentation | [BAS 2026, 2890](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 2910 | Upplupna löner | Liability/equity candidate, normally credit; actual nature and maturity control presentation | [BAS 2026, 2910](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 2920 | Upplupna semesterlöner | Liability/equity candidate, normally credit; actual nature and maturity control presentation | [BAS 2026, 2920](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 2940 | Upplupna lagstadgade sociala och andra avgifter | Liability/equity candidate, normally credit; actual nature and maturity control presentation | [BAS 2026, 2940](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 2990 | Övriga upplupna kostnader och förutbetalda intäkter | Liability/equity candidate, normally credit; actual nature and maturity control presentation | [BAS 2026, 2990](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 3001 | Försäljning inom Sverige, 25 % moms | Revenue, normally credit; account label does not establish VAT treatment | [BAS 2026, 3001](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 3002 | Försäljning inom Sverige, 12 % moms | Revenue, normally credit; account label does not establish VAT treatment | [BAS 2026, 3002](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 3003 | Försäljning inom Sverige, 6 % moms | Revenue, normally credit; account label does not establish VAT treatment | [BAS 2026, 3003](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 3004 | Försäljning inom Sverige, momsfri | Revenue, normally credit; account label does not establish VAT treatment | [BAS 2026, 3004](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 3100 | Försäljning av varor utanför Sverige | Revenue, normally credit; account label does not establish VAT treatment | [BAS 2026, 3100](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 3105 | Försäljning varor till land utanför EU | Revenue, normally credit; account label does not establish VAT treatment | [BAS 2026, 3105](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 3106 | Försäljning varor till annat EU-land, momspliktig | Revenue, normally credit; account label does not establish VAT treatment | [BAS 2026, 3106](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 3108 | Försäljning varor till annat EU-land, momsfri | Revenue, normally credit; account label does not establish VAT treatment | [BAS 2026, 3108](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 3200 | Försäljning VMB och omvänd moms | Revenue, normally credit; account label does not establish VAT treatment | [BAS 2026, 3200](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 3300 | Försäljning av tjänster utanför Sverige | Revenue, normally credit; account label does not establish VAT treatment | [BAS 2026, 3300](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 3305 | Försäljning tjänster till land utanför EU | Revenue, normally credit; account label does not establish VAT treatment | [BAS 2026, 3305](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 3308 | Försäljning tjänster till annat EU-land | Revenue, normally credit; account label does not establish VAT treatment | [BAS 2026, 3308](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 3400 | Försäljning, egna uttag | Revenue, normally credit; account label does not establish VAT treatment | [BAS 2026, 3400](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 3900 | Övriga rörelseintäkter (gruppkonto) | Revenue, normally credit; account label does not establish VAT treatment | [BAS 2026, 3900](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 4010 | Inköp av handelsvaror i Sverige | Expense/cost candidate, normally debit; recognition, timing and tax deductibility are separate checks | [BAS 2026, 4010](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 4310 | Inköp av råvaror och material i Sverige | Expense/cost candidate, normally debit; recognition, timing and tax deductibility are separate checks | [BAS 2026, 4310](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 4500 | Inköp av råvaror och material, tjänster m.m. från utlandet (gruppkonto) | Expense/cost candidate, normally debit; recognition, timing and tax deductibility are separate checks | [BAS 2026, 4500](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 4600 | Inköp av tjänster, underentreprenader och legoarbeten i Sverige (gruppkonto) | Expense/cost candidate, normally debit; recognition, timing and tax deductibility are separate checks | [BAS 2026, 4600](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 4900 | Förändring av lager (gruppkonto) | Inventory movement, debit or credit by underlying movement | [BAS 2026, 4900](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 5010 | Lokalhyra | Expense/cost candidate, normally debit; recognition, timing and tax deductibility are separate checks | [BAS 2026, 5010](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 5020 | El | Expense/cost candidate, normally debit; recognition, timing and tax deductibility are separate checks | [BAS 2026, 5020](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 5060 | Städning och renhållning | Expense/cost candidate, normally debit; recognition, timing and tax deductibility are separate checks | [BAS 2026, 5060](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 5090 | Övriga lokalkostnader | Expense/cost candidate, normally debit; recognition, timing and tax deductibility are separate checks | [BAS 2026, 5090](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 5100 | Fastighetskostnader (gruppkonto) | Expense/cost candidate, normally debit; recognition, timing and tax deductibility are separate checks | [BAS 2026, 5100](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 5200 | Hyra av anläggningstillgångar (gruppkonto) | Expense/cost candidate, normally debit; recognition, timing and tax deductibility are separate checks | [BAS 2026, 5200](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 5210 | Hyra av maskiner och andra tekniska anläggningar, ej datorer och fordon | Expense/cost candidate, normally debit; recognition, timing and tax deductibility are separate checks | [BAS 2026, 5210](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 5250 | Hyra av datorer | Expense/cost candidate, normally debit; recognition, timing and tax deductibility are separate checks | [BAS 2026, 5250](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 5300 | Energikostnader för drift (gruppkonto) (ej råvaror och förnödenheter) | Expense/cost candidate, normally debit; recognition, timing and tax deductibility are separate checks | [BAS 2026, 5300](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 5400 | Förbrukningsinventarier och förbrukningsmaterial (gruppkonto) | Expense/cost candidate, normally debit; recognition, timing and tax deductibility are separate checks | [BAS 2026, 5400](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 5410 | Förbrukningsinventarier | Expense/cost candidate, normally debit; recognition, timing and tax deductibility are separate checks | [BAS 2026, 5410](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 5420 | Programvaror | Expense/cost candidate, normally debit; recognition, timing and tax deductibility are separate checks | [BAS 2026, 5420](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 5460 | Förbrukningsmaterial | Expense/cost candidate, normally debit; recognition, timing and tax deductibility are separate checks | [BAS 2026, 5460](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 5500 | Reparation och underhåll (gruppkonto) | Expense/cost candidate, normally debit; recognition, timing and tax deductibility are separate checks | [BAS 2026, 5500](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 5600 | Kostnader för transportmedel (gruppkonto) | Expense/cost candidate, normally debit; recognition, timing and tax deductibility are separate checks | [BAS 2026, 5600](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 5610 | Personbils- och mc-kostnader, m.m. | Expense/cost candidate, normally debit; recognition, timing and tax deductibility are separate checks | [BAS 2026, 5610](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 5700 | Frakter och transporter (gruppkonto) | Expense/cost candidate, normally debit; recognition, timing and tax deductibility are separate checks | [BAS 2026, 5700](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 5710 | Frakter och försäkringar vid varudistribution | Expense/cost candidate, normally debit; recognition, timing and tax deductibility are separate checks | [BAS 2026, 5710](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 5711 | Fraktkostnader | Expense/cost candidate, normally debit; recognition, timing and tax deductibility are separate checks | [BAS 2026, 5711](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 5800 | Resekostnader (gruppkonto) | Expense/cost candidate, normally debit; recognition, timing and tax deductibility are separate checks | [BAS 2026, 5800](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 5810 | Biljetter | Expense/cost candidate, normally debit; recognition, timing and tax deductibility are separate checks | [BAS 2026, 5810](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 5820 | Hyrbilskostnader | Expense/cost candidate, normally debit; recognition, timing and tax deductibility are separate checks | [BAS 2026, 5820](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 5830 | Kost och logi | Expense/cost candidate, normally debit; recognition, timing and tax deductibility are separate checks | [BAS 2026, 5830](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 5900 | Reklam och PR (gruppkonto) | Expense/cost candidate, normally debit; recognition, timing and tax deductibility are separate checks | [BAS 2026, 5900](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 5910 | Annonsering | Expense/cost candidate, normally debit; recognition, timing and tax deductibility are separate checks | [BAS 2026, 5910](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 5930 | Reklamtrycksaker och direktreklam | Expense/cost candidate, normally debit; recognition, timing and tax deductibility are separate checks | [BAS 2026, 5930](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 6000 | Övriga försäljningskostnader (gruppkonto) | Expense/cost candidate, normally debit; recognition, timing and tax deductibility are separate checks | [BAS 2026, 6000](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 6100 | Kontorsmateriel och trycksaker (gruppkonto) | Expense/cost candidate, normally debit; recognition, timing and tax deductibility are separate checks | [BAS 2026, 6100](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 6110 | Kontorsmateriel | Expense/cost candidate, normally debit; recognition, timing and tax deductibility are separate checks | [BAS 2026, 6110](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 6200 | Tele, data och post (gruppkonto) | Expense/cost candidate, normally debit; recognition, timing and tax deductibility are separate checks | [BAS 2026, 6200](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 6210 | Telekommunikation | Expense/cost candidate, normally debit; recognition, timing and tax deductibility are separate checks | [BAS 2026, 6210](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 6230 | Datakommunikation | Expense/cost candidate, normally debit; recognition, timing and tax deductibility are separate checks | [BAS 2026, 6230](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 6300 | Företagsförsäkringar och övriga riskkostnader (gruppkonto) | Expense/cost candidate, normally debit; recognition, timing and tax deductibility are separate checks | [BAS 2026, 6300](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 6310 | Företagsförsäkringar | Expense/cost candidate, normally debit; recognition, timing and tax deductibility are separate checks | [BAS 2026, 6310](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 6400 | Förvaltningskostnader (gruppkonto) | Expense/cost candidate, normally debit; recognition, timing and tax deductibility are separate checks | [BAS 2026, 6400](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 6500 | Övriga externa tjänster (gruppkonto) | Expense/cost candidate, normally debit; recognition, timing and tax deductibility are separate checks | [BAS 2026, 6500](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 6530 | Redovisningstjänster | Expense/cost candidate, normally debit; recognition, timing and tax deductibility are separate checks | [BAS 2026, 6530](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 6540 | IT-tjänster | Expense/cost candidate, normally debit; recognition, timing and tax deductibility are separate checks | [BAS 2026, 6540](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 6550 | Konsultarvoden | Expense/cost candidate, normally debit; recognition, timing and tax deductibility are separate checks | [BAS 2026, 6550](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 6570 | Bankkostnader | Expense/cost candidate, normally debit; recognition, timing and tax deductibility are separate checks | [BAS 2026, 6570](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 6900 | Övriga externa kostnader (gruppkonto) | Expense/cost candidate, normally debit; recognition, timing and tax deductibility are separate checks | [BAS 2026, 6900](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 7010 | Löner till kollektivanställda | Expense/cost candidate, normally debit; recognition, timing and tax deductibility are separate checks | [BAS 2026, 7010](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 7210 | Löner till tjänstemän | Expense/cost candidate, normally debit; recognition, timing and tax deductibility are separate checks | [BAS 2026, 7210](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 7220 | Löner till företagsledare | Expense/cost candidate, normally debit; recognition, timing and tax deductibility are separate checks | [BAS 2026, 7220](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 7310 | Kontanta extraersättningar | Expense/cost candidate, normally debit; recognition, timing and tax deductibility are separate checks | [BAS 2026, 7310](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 7380 | Kostnader för förmåner till anställda | Expense/cost candidate, normally debit; recognition, timing and tax deductibility are separate checks | [BAS 2026, 7380](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 7410 | Pensionsförsäkringspremier | Expense/cost candidate, normally debit; recognition, timing and tax deductibility are separate checks | [BAS 2026, 7410](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 7510 | Arbetsgivaravgifter 31,42 % | Expense/cost candidate, normally debit; recognition, timing and tax deductibility are separate checks | [BAS 2026, 7510](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 7570 | Premier för arbetsmarknadsförsäkringar | Expense/cost candidate, normally debit; recognition, timing and tax deductibility are separate checks | [BAS 2026, 7570](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 7610 | Utbildning | Expense/cost candidate, normally debit; recognition, timing and tax deductibility are separate checks | [BAS 2026, 7610](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 7690 | Övriga personalkostnader | Expense/cost candidate, normally debit; recognition, timing and tax deductibility are separate checks | [BAS 2026, 7690](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 7820 | Avskrivningar på byggnader och markanläggningar | Expense/cost candidate, normally debit; recognition, timing and tax deductibility are separate checks | [BAS 2026, 7820](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 7830 | Avskrivningar på maskiner respektive inventarier | Expense/cost candidate, normally debit; recognition, timing and tax deductibility are separate checks | [BAS 2026, 7830](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 7840 | Avskrivningar på förbättringsutgifter på annans fastighet | Expense/cost candidate, normally debit; recognition, timing and tax deductibility are separate checks | [BAS 2026, 7840](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 8310 | Ränteintäkter från omsättningstillgångar | Financial income, normally credit; actual source of return required | [BAS 2026, 8310](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 8311 | Ränteintäkter från bank | Financial income, normally credit; actual source of return required | [BAS 2026, 8311](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 8410 | Räntekostnader för långfristiga skulder | Financial cost/current-tax candidate, normally debit; separate tax qualification required | [BAS 2026, 8410](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 8415 | Räntekostnader för andra skulder till kreditinstitut | Financial cost/current-tax candidate, normally debit; separate tax qualification required | [BAS 2026, 8415](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 8420 | Räntekostnader för kortfristiga skulder | Financial cost/current-tax candidate, normally debit; separate tax qualification required | [BAS 2026, 8420](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 8421 | Räntekostnader till kreditinstitut | Financial cost/current-tax candidate, normally debit; separate tax qualification required | [BAS 2026, 8421](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 8490 | Övriga skuldrelaterade poster | Financial cost/current-tax candidate, normally debit; separate tax qualification required | [BAS 2026, 8490](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 8910 | Skatt som belastar årets resultat | Financial cost/current-tax candidate, normally debit; separate tax qualification required | [BAS 2026, 8910](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 8990 | Resultat | Result/equity or closing transfer, debit or credit; reconcile once, never duplicate profit | [BAS 2026, 8990](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |
| 8999 | Årets resultat | Result/equity or closing transfer, debit or credit; reconcile once, never duplicate profit | [BAS 2026, 8999](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) |

### Corrections to inherited account meanings

Keep original ledger codes and documents until an authorised mapping is agreed. The previous guide's goodwill/computers/vehicles/tax-receivable and depreciation labels do not match several 2026 codes. For the intended meanings, assess 1070 for goodwill, 1214/1224 for production/non-production computers, 1216/1226 for the specified vehicle uses, 1640 for tax receivables, 1440 for work in progress, 2890 for other current liabilities, 4310 for domestic raw materials, 5460 for consumable materials and 5710/5711 for distribution freight. Production use and transaction nature control the choice. Domestic sales use the appropriate 3001–3004 account; foreign goods and services use their distinct 3100/3300 families and subaccounts. None of these labels establishes VAT treatment. ([BAS 2026, respective accounts](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf))

7570 is labour-market-insurance premiums, not own social contributions. 7820 is depreciation on buildings/land improvements, 7830 on machinery/equipment and 7840 on improvements to another's property, rather than a generic vehicle-depreciation account. 8310 concerns current-asset interest, 8410 long-term-debt interest and 8420 short-term-debt interest. The specific bank/credit-institution subaccounts still require the actual loan facts. ([BAS 2026, 7570, 7820–7840, 8310 and 8410–8421](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf))

### Revenue recognition

K2 uses its risks/rewards, reliable-measurement and probable-benefits conditions together with the transaction-specific rules. Time-and-materials assignments recognise revenue as work is performed and materials are delivered/consumed; earned uninvoiced amounts and advance billing have their respective asset/liability treatment. Invoice date alone does not decide the year's revenue. Fixed-price work has the main percentage-of-completion method and the alternative substantial-completion method, with consistency, reliability, expected-loss and method-change conditions. Apply the actual contract and complete relevant paragraphs. ([K2 6.6–6.7 and 6.13–6.25, pp133–147](https://www.bfn.se/wp-content/uploads/vl16-10-k2ar-kons2025.pdf))

For the specified subscription/service agreements, revenue normally follows the agreed service period, with the dominant-activity and other transaction-specific exceptions. The small-amount relief cannot materially distort the accounts. ([K2 6.11, 6.26 and 2.4B](https://www.bfn.se/wp-content/uploads/vl16-10-k2ar-kons2025.pdf)) K3's reliable-outcome completion-stage treatment has a specified legal-person completion-method exception for the IL branches named in 23.31; it is not an unconditional rule for every long-term contract. ([K3 23.18 and 23.31–23.32](https://www.bfn.se/wp-content/uploads/vl12-1-k3-kons20251215.pdf))

### Expense recognition, assets and depreciation

A premises, electricity, accounting, insurance, advertising, office-supply, telecoms, bank-fee, software, travel, training or repair payment is first classified by its actual nature and period. Confirm asset, prepayment, business/private and VAT treatment before recognising expense. A BAS code does not establish a 100% tax deduction. ([K2 chapter 7 and relevant asset chapters](https://www.bfn.se/wp-content/uploads/vl16-10-k2ar-kons2025.pdf))

For K2 tangible assets, test acquisition cost, any related/larger-investment grouping, the applicable half-PBB input and unrecoverable VAT before using low-value expense treatment. A short-life asset is a separate possible route. Internally generated intangibles, including acquired components forming an inseparable part of such an asset, cannot be capitalised merely because an account exists. ([K2 10.4–10.6](https://www.bfn.se/wp-content/uploads/vl16-10-k2ar-kons2025.pdf))

K2 is not straight-line-only. Select a method reflecting consumption; its commentary describes linear, diminishing and production-based methods and the disclosure rule applies to non-linear allocation. Define the asset unit: specified land/building-related units and subsequent expenditure on them are separate; capitalised subsequent expenditure on other assets remains within the existing unit, with whole-asset useful-life reassessment and prospective depreciation of the combined carrying amount. ([K2 10.20–10.26 and 18.4](https://www.bfn.se/wp-content/uploads/vl16-10-k2ar-kons2025.pdf)) K3 requires separate significant components where consumption differs materially. Its permitted methods include straight line, diminishing balance and units of production; the method must reflect expected consumption and be reassessed when the specified indication of material change arises. ([K3 17.4, 17.13 and 17.20](https://www.bfn.se/wp-content/uploads/vl12-1-k3-kons20251215.pdf))

ABs and economic associations applying K2 can have narrowly permitted building/land revaluations under the framework caps and ÅRL conditions. Buildings and land are assessed separately; building revaluation is depreciated over remaining useful life. This is not permission to revalue other equipment, every legal form or an ineligible K2 entity. ([K2 10.40–10.42 and ÅRL 4:6](https://www.bfn.se/wp-content/uploads/vl16-10-k2ar-kons2025.pdf))

Accumulated excess depreciation is conditional on the relevant tax/bookkeeping method and tax value being below book value. Under-depreciation is not an untaxed reserve; the restvärde method does not recognise this book/tax difference. The book method need not be linear. ([K2 15.3 commentary, pp252–253](https://www.bfn.se/wp-content/uploads/vl16-10-k2ar-kons2025.pdf))

### P&L Format (Resultaträkning)

The retained by-nature outline is an orientation aid. K2 chapter 4 prescribes the applicable full or authorised abbreviated format and its separate captions. This outline does not replace those formats, comparatives, notes or the management report. [K2 chapter 4, pp45–62](https://www.bfn.se/wp-content/uploads/vl16-10-k2ar-kons2025.pdf)

#### Format (Kostnadsslagsindelad -- By Nature)

```
Nettoomsättning (Net turnover)                                 xxx
Förändring av varulager (Change in inventory)                  xxx
Aktiverat arbete för egen räkning                              xxx
Övriga rörelseintäkter (Other operating income)                xxx
                                                            -------
Summa rörelseintäkter                                          xxx

Råvaror och förnödenheter (Raw materials/consumables)         (xxx)
Övriga externa kostnader (Other external expenses)            (xxx)
Personalkostnader (Staff costs)                               (xxx)
Avskrivningar (Depreciation)                                  (xxx)
Nedskrivningar (Impairment)                                   (xxx)
Övriga rörelsekostnader (Other operating expenses)            (xxx)
                                                            -------
Rörelseresultat (Operating profit/loss)                        xxx

Finansiella intäkter (Financial income)                        xxx
Finansiella kostnader (Financial costs)                       (xxx)
                                                            -------
Resultat efter finansiella poster                              xxx

Bokslutsdispositioner (Appropriations)*                       (xxx)
  - Förändring periodiseringsfond                             (xxx)
  - Förändring överavskrivningar                              (xxx)
                                                            -------
Resultat före skatt (Profit before tax)                        xxx

Skatt på årets resultat (Income tax)                          (xxx)
                                                            -------
Årets resultat (Net profit/loss)                               xxx
```

*Bokslutsdispositioner (appropriations) are transfers to/from untaxed reserves under the applicable legal-person accounting framework.

### Balance Sheet Format (Balansräkning)

The retained vertical outline is an orientation aid, not a complete annual-report template. Use the applicable K2 full or authorised abbreviated format, its AB-specific captions and the conditional mapping controls below. [K2 chapter 4, pp63–94](https://www.bfn.se/wp-content/uploads/vl16-10-k2ar-kons2025.pdf)

#### Format

```
TILLGÅNGAR (Assets)

Anläggningstillgångar (Fixed assets)
  Immateriella anläggningstillgångar
    Goodwill                                                  xxx
    Patent och licenser                                       xxx
  Materiella anläggningstillgångar
    Byggnader och mark                                        xxx
    Maskiner och inventarier                                  xxx
  Finansiella anläggningstillgångar
    Aktier i dotterföretag                                    xxx
    Långfristiga fordringar                                   xxx
                                                           -------
  Summa anläggningstillgångar                                  xxx

Omsättningstillgångar (Current assets)
  Varulager                                                   xxx
  Kundfordringar                                              xxx
  Övriga fordringar                                           xxx
  Förutbetalda kostnader                                      xxx
  Kassa och bank                                              xxx
                                                           -------
  Summa omsättningstillgångar                                  xxx

SUMMA TILLGÅNGAR                                               xxx
                                                           =======

EGET KAPITAL OCH SKULDER (Equity and Liabilities)

Eget kapital (Equity)
  Aktiekapital                                                xxx
  Uppskrivningsfond                                           xxx
  Reservfond                                                  xxx
  Balanserat resultat                                         xxx
  Årets resultat                                              xxx
                                                           -------
  Summa eget kapital                                           xxx

Obeskattade reserver (Untaxed reserves)*
  Periodiseringsfonder                                        xxx
  Ackumulerade överavskrivningar                              xxx
                                                           -------
  Summa obeskattade reserver                                   xxx

Avsättningar (Provisions)                                     xxx

Långfristiga skulder (Long-term liabilities)
  Skulder till kreditinstitut                                 xxx
                                                           -------
  Summa långfristiga skulder                                   xxx

Kortfristiga skulder (Current liabilities)
  Leverantörsskulder                                          xxx
  Skatteskulder                                               xxx
  Övriga skulder                                              xxx
  Upplupna kostnader                                          xxx
                                                           -------
  Summa kortfristiga skulder                                   xxx

SUMMA EGET KAPITAL OCH SKULDER                                 xxx
                                                           =======
```

*Untaxed reserves (obeskattade reserver):* For an AB applying the cited 2026 K2/K3 rules, show untaxed reserves at their gross amount in the company's own balance sheet. Do not split that balance between equity and a separate deferred-tax liability. K2 presents the reserve, including its deferred-tax element, under untaxed reserves; K3 paragraph 29.37 requires gross presentation in a legal person's accounts and gross appropriations (bokslutsdispositioner) in its income statement. This K3 exception concerns tax attributable to untaxed reserves; other deferred-tax items follow chapter 29. Consolidated reporting requires a separate K3 assessment. Establish framework eligibility before applying these rules. Sources: [K2 paragraphs 15.2–15.3 and 16.4, updated 16 June 2025](https://www.bfn.se/wp-content/uploads/vl16-10-k2ar-kons2025.pdf) and [K3 paragraphs 29.15 and 29.37, updated 15 December 2025](https://www.bfn.se/wp-content/uploads/vl12-1-k3-kons20251215.pdf), for financial years beginning after 31 December 2025.

### Conditional mapping and closing controls

Use K2 chapter 4 and the transaction's recognition/measurement chapter, not a first-digit rule alone. Preserve gross asset cost and contra-asset depreciation/impairment, distinguish financial investment results from impairment, and classify operating versus financial currency and tax items by their rule. A pledge alone does not move cash out of Kassa och bank. Distinguish tax-account settlement, final-tax receivable/payable, VAT, withholding and social-contribution liabilities. Reconcile fund vintage and movement, current debt portions, free/restricted premium, prior/current profit and completed 8999/2099 transfers. Never count closing profit twice. ([K2 chapter 4, AB additions 4.10–4.12 and chapters 10–17](https://www.bfn.se/wp-content/uploads/vl16-10-k2ar-kons2025.pdf))

### Transaction-description signals

**Common Transaction Descriptions**

| Pattern | Classification |
| --- | --- |
| BG (Bankgiro), PG (Plusgiro) | Payment-channel signal; inspect underlying settlement and direction |
| AUTOGIRO | Direct-debit signal; inspect underlying invoice and period |
| SWISH | Mobile payment (check direction) |
| SKATTEVERKET, SKATTEKONTO | Tax-account movement; obtain assessment, payment and settlement breakdown |
| ARBETSGIVARAVG | Employer-charge signal; reconcile approved payroll and actual settlement |
| KORTKÖP, KORTTRANSAKTION | Card-payment signal; inspect invoice, ownership, business purpose and asset/expense treatment |
| INSÄTTNING | Deposit (potential income or transfer) |
| LÖN, LÖNEUTBETALNING | Payroll-payment signal; reconcile approved payroll and liabilities |
| HYRA, LOKALHYRA | Rental-payment signal; check contract, period and deposit element |
| RÄNTA | Interest (check debit/credit) |
| AVGIFT, SERVICEAVGIFT | Bank/service charges |
| FAKTURA, FAKT NR | Invoice payment (check context) |

The descriptions above are investigation signals. Match the actual payer/payee, document, period and settlement direction before choosing an account. A loan receipt, owner injection, transfer, refund or customer settlement is not automatically current revenue. A tax-account payment is not automatically a deductible expense. Exclude duplicate documents from posting with a linked reason; retain each source row in the register.

### Conditional transaction classification rules

Resolve entity, period, source document, recognised balance and approved accounting policy before applying a rule. Dr means debit and Cr credit. An account is a candidate, not permission to recognise an expense, deduct tax or recover VAT.

Source keys: **C** is the [BAS 2026 chart](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf), establishing account labels; **R** is the selected [K2 recognition guidance](https://www.bfn.se/wp-content/uploads/vl16-10-k2ar-kons2025.pdf) qualified above; **P** is [BFL chapter 5](https://data.riksdagen.se/dokumentstatus/sfs-1999-1078.json) on recording and traceability. Journal directions and matching controls below are derived working-paper rules, not verbatim BAS instructions. Other frameworks need their own recognition rules.

| ID | Required evidence and condition | Conditional treatment | Source |
| --- | --- | --- | --- |
| B01 | Receipt matches an already recognised customer receivable | Dr bank, Cr 1510 for settlement; separate fees/differences. Do not recognise the sale/VAT again | C; P |
| B02 | Payment matches an already recognised supplier payable | Dr 2440, Cr bank for settlement; separate differences. Do not recognise purchase/VAT again | C; P |
| B03 | Current business premises rent, without deposit/prepayment portion | Candidate 5010 in the correct period, with VAT separately qualified | C; R |
| B04 | Invoice establishes current business electricity consumption | Candidate 5020; distinguish heat, equipment, deposit and private use | C; R |
| B05 | Current telephone service is evidenced | Candidate 6210; separate hardware, private use and prepaid periods | C; R |
| B06 | Current data communication service is evidenced | Candidate 6230; distinguish software and equipment | C; R |
| B07 | Current business insurance cover is evidenced | Candidate 6310; allocate coverage period and separate pension/other components | C; R |
| B08 | Current external accounting work is evidenced | Candidate 6530; establish service period and business purpose | C; R |
| B09 | Statement/fee advice establishes a bank service fee | Candidate 6570; not principal, interest or an unidentified bank debit | C; P |
| B10 | Software invoice and approved policy establish a current expense | Candidate 5420; acquired rights, assets and prepayments require separate assessment | C; R |
| B11 | Approved payroll journal supplies gross wages and deductions | Candidate 7010/7210 by employee class, withholding 2710 and net wage liability 2911 as supported; bank text supplies none of the calculation | C; P |
| B12 | Bank payment settles a recognised net wage liability | Dr 2911, Cr bank; do not expense the net payment as a second gross wage | C; P |
| B13 | Approved payroll calculation establishes statutory employer charges | Candidate 7510 and liability 2731; the BAS label's rate does not establish an employee's actual rate/relief | C; P |
| B14 | Pension invoice identifies a pension-insurance premium | Candidate 7410; separate insurance, administration and any separately qualified pension tax | C; R |
| B15 | Payment is proved to be a transfer to the entity's tax account | Dr 1630, Cr bank; obtain the actual tax-account statement for subsequent allocations | C; P |
| B16 | Tax-account statement establishes settlement of a booked statutory liability | Reconcile 1630 against the specific liability, such as 2650, 2710 or 2731; no blanket income-tax expense | C; P |
| B17 | Tax-account refund matches a reconciled receivable/movement | Dr bank, Cr the supported balance, often 1630; distinguish 1640/1650 and avoid duplicate refund recognition | C; P |
| B18 | Contract establishes long-term credit-institution borrowing | Candidate 2350; split proceeds, principal, interest, fees and current portion | C; P |
| B19 | Contract establishes other short-term credit-institution borrowing | Candidate 2410; current portion/overdraft may instead require 2417/2480 | C; P |
| B20 | Contract establishes a loan from a related individual | Candidate 2393 long term or 2893 short term under actual terms; distinguish equity/reimbursement | C; P |
| B21 | Payment repays a recognised loan | Dr the actual liability, Cr bank for principal only; interest and fees separately qualified | C; P |
| B22 | AB subscription/registration evidence establishes registered capital | Candidate 2081; unregistered capital may require 2082. A receipt alone proves neither | C; P |
| B23 | Documented AB shareholder contribution is established | Candidate 2093 subject to legal terms/recognition; distinguish loan, subscription and reimbursement, not sole-trader drawings | C; P |
| B24 | Entity is a sole trader and private withdrawal is established | Candidate 2013 against bank, outside business P&L; this does not qualify full K1/NE mechanics | C; P |
| B25 | Entity is a sole trader and private introduction is established | Candidate 2018 against bank; not turnover or evidence of a deduction | C; P |
| B26 | Computer ownership, use and capitalisation are approved | Candidate 1214 production or 1224 non-production; any expense rule needs separate eligibility | C; R |
| B27 | Vehicle ownership, use and capitalisation are approved | Candidate 1216 work vehicle or 1226 non-production car/transport; leases, VAT and benefits are separate | C; R |
| B28 | Approved equipment depreciation schedule supplies the amount | Candidate Dr 7832, Cr 1229 for corresponding equipment; use the matching family/method, not this pair for all assets | C; R |
| B29 | Evidence and qualified VAT rules establish recoverable invoiced input VAT | Candidate 2641; the label itself establishes neither recovery nor reverse-charge/import treatment | C; P |
| B30 | Approved fund history and tax/book rules establish allocation/reversal | Candidate 8811 allocation or 8819 reversal against the correct year-specific reserve; reconcile gross amounts/vintage | C; R |
| B31 | Approved book/tax bridge establishes excess depreciation movement | Candidate 8850 against 2150; distinct from planned depreciation and the tax calculation | C; R |
| B32 | Two booked rows prove one own-account transfer in the same currency, with timing/cut-off resolved; hold unmatched, cross-period, FX or fee differences for separate treatment | One journal: Dr receiving bank, Cr sending bank, linked to both rows. No second posting, revenue/expense or generic 1990 clearing | C; P |

**Classification confidence:** high means the document, entity, amount, period, account and treatment are all resolved for the proposed entry; medium means a candidate has a named unresolved question; low means material alternatives cannot be distinguished. Record reasons, not a fabricated probability. These labels do not change guide Tier 2 status. Unresolved rows stay visible in the register and reviewer brief and do not enter an approved posting set.

### Counterparty investigation library

These 15 routes are investigation signals. A name may be truncated, identify an intermediary or cover several products. Confirm the actual legal counterparty and invoice/contract before applying B01–B32. Provider descriptions establish service categories, not a customer's transaction, deduction or VAT recovery.

| Name/text | Official source and investigation | Possible destination after qualification |
| --- | --- | --- |
| NORDEA | [Corporate services/formats](https://www.nordea.se/foretag/produkter/betala/programleverantorer/vara-tjanster-programleverantorer.html); match account, transfer, fee advice or financing contract | Transfer/settlement, 6570 fee or actual borrowing/interest |
| SWEDBANK | [Business services](https://www.swedbank.se/foretag.html); distinguish bank activity, payment service and financing | Bank/settlement, proved fee or liability |
| SEB | [Business banking](https://seb.se/foretag); obtain statement and service/loan terms | Transfer, fee, principal or interest separately evidenced |
| HANDELSBANKEN | [Business services](https://www.handelsbanken.se/sv/foretag); check product, including pension services | Bank/loan or identified pension/insurance component |
| DANSKE BANK | [Business banking](https://danskebank.se/foretag); match account and contract | Transfer, settlement or proved fee/loan component |
| LÄNSFÖRSÄKRINGAR | [Business bank/insurance](https://www.lansforsakringar.se/stockholm/foretag/); identify regional entity/product | Bank, 6310 insurance or another proved component |
| VATTENFALL | [Energy services](https://www.vattenfall.se/foretag/); distinguish electricity, heat, charging, equipment and projects | 5020 only for established electricity; other service/asset separately assessed |
| TELIA | [Business services](https://www.telia.se/foretag); split telephone/data, equipment and periods | 6210/6230, approved asset or prepayment |
| TELE2 | [Business services](https://www.tele2.se/foretag); inspect mobile, broadband and bundled components | 6210/6230 or another qualified component |
| SKATTEVERKET / SKATTEKONTO | [BAS tax-account labels](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf); obtain tax-account statement/assessment/settlement | 1630 transfer and specific statutory balance, not blanket expense |
| ALECTA | [Occupational pension](https://www.alecta.se/for-arbetsgivare/kort-om-itp/skaffa-tjanstepension-till-foretaget); inspect policy, invoice components and period | 7410 only for proved premium; other items separately assessed |
| FORA | [Employer insurance administration](https://www.fora.se/foretag/); obtain invoice and pension/insurance reconciliation | Split supported components/periods; no universal expense code |
| FORTNOX | [Software/other services](https://www.fortnox.se/); distinguish software/accounting work, settlement and financing | 5420/6530 only for current expense; otherwise actual asset/liability/settlement |
| MICROSOFT / MICROSOFT 365 | [Business applications](https://www.microsoft.com/sv-se/microsoft-365/business); confirm seller, licence/subscription, period, hardware and VAT jurisdiction | Qualified software expense, asset or prepayment; foreign VAT separately assessed |
| GOOGLE / GOOGLE WORKSPACE | [Business applications](https://workspace.google.com/intl/sv/); confirm supplier, period and VAT jurisdiction | Qualified software expense/prepayment, not inferred domestic VAT |

### Conservative defaults and exclusions

Keep every imported row, proposed journal, source link and excluded duplicate in the register. DUBBLETT, DUBLETT, KOPIA, ÖVERFÖRING, AUTOGIRO or a repeated amount signals investigation, not deletion. An invoice copy is not a second purchase; a second genuine equal payment is not a duplicate. Exclude from posting only with evidenced identity/duplicate relationship, retained original, file/row references, reason and reviewer status. Distinguish reversed, rejected, pending and booked movements rather than silently netting/discarding them.

Do not invent a small-payment/sundry-expense threshold. K2 accrual relief concerns recognition and materiality, not permission to omit a financial row. AB owner payments need their actual legal basis; sole-trader private movements stay outside P&L. Missing VAT evidence leaves VAT unresolved, not an assumed deduction/rate. For FX, deposits, mixed use, refunds and bundled payments, preserve components/questions until the applicable rules are established. Never force a balancing plug.

### Currency, number and import controls

BFL 4:6 requires transactions to be presentable in one bookkeeping currency, normally SEK. EUR is permitted for the specified AB, economic association, savings bank, insurance undertaking and occupational pension undertaking forms, not universally. Changes occur only at a new financial year; a subsequent change requires the specified permission. Branch exceptions need separate assessment. ÅRL 2:6 uses that currency for the annual report, allows supplementary presentation in another currency at the balance-date rate and specifies the ECB rate for a currency change. This is not a complete FX method. ([BFL 4:6](https://data.riksdagen.se/dokumentstatus/sfs-1999-1078.json), [ÅRL 2:6](https://data.riksdagen.se/dokumentstatus/sfs-1995-1554.json))

This K2 manual requires currency/unit disclosure: whole SEK or thousands of SEK, or whole EUR or hundreds of EUR. The management report may use those larger units even with whole-unit statements, but result appropriation always uses whole SEK/EUR. Preserve exact ledger values; document display rounding and reconcile displayed totals/comparatives. No statutory tie-breaking rounding convention is established here. Presentation scaling does not authorise rounding away bank cents or using scaled import amounts. ([K2 3.8–3.9](https://www.bfn.se/wp-content/uploads/vl16-10-k2ar-kons2025.pdf))

Swedish prose uses a decimal comma and spaces for 3-digit groups, preferably nonbreaking spaces. A file schema can differ. Preserve source strings; establish separator, grouping, sign, currency and scale before parsing. Reject ambiguous '1,234' rather than guessing. ([Isof decimals](https://frageladan.isof.se/faqs/21402), [grouping](https://frageladan.isof.se/faqs/30318))

**Bank exports.** Nordea lists FS1, EKK, MT940 and FINSTA; its Business file-handling page separately describes Corporate Access ISO 20022, including camt.053Extended, using .NDA extensions. The currently linked EKK description is v1.3, effective 20 February 2012: fixed-position records, not CSV, with account/currency boundaries, balances, transactions, continuation and terminal controls. An 88 continuation record is not a separate financial movement. Match the actual service/version before using the specification; current linkage does not establish the customer's file version. No EKK parser is implemented/tested here. ([Nordea formats](https://www.nordea.se/foretag/produkter/betala/programleverantorer/vara-tjanster-programleverantorer.html), [file handling](https://www.nordea.se/filhantering), [EKK v1.3](https://www.nordea.se/Images/154-16151/postbeskrivning-elektroniskt-kontoutdrag.pdf))

Revolut Business documents per-currency PDF, CSV, camt.053 XML and MT940 TXT statements, UTC by default and possible local/UTC CSV columns. Confirm actual timestamp fields/period before assigning dates. Available exports do not establish a universal CSV schema. ([Revolut statements](https://help.revolut.com/sv-SE/business/help/managing-my-business/viewing-my-account-statements/how-to-get-a-monthly-statement/))

For an actual file, obtain field definitions and an authorised sample. Record encoding, delimiter/quoting, timestamp/timezone, account/currency, amount/sign convention, status, identifier, row count and opening/closing balances. Preserve leading zeros/quoted fields. Establish separate versus netted fees. Reconcile each account/currency independently: opening plus signed booked movements equals closing. Account for headers, continuations and trailers under the actual format. A bank name/extension alone proves no schema. These are derived validation controls, not claimed bank-specific CSV definitions.

**SIE.** The publisher distinguishes types 1–3 balances, type 4 exports and type 4i import vouchers; SIE 5 is separate XML. The linked PDF cover says 4C, 6 August 2025, but its document-title metadata includes DRAFT; final-publication status remains unresolved. Selected classic rules specify CP437, decimal points, at most 2 fractional digits, leading minus without plus and YYYYMMDD dates. #VER contains balanced #TRANS rows; preserve account/dimension identities. Optional #VALUTA describes the whole file with a documented SEK default, but a receiver may ignore it. Confirm receiver currency support rather than relying on the tag. Read type-specific mandatory records, flags, corrections and the complete vendor contract before generating an import. No import/vendor acceptance or full SIE implementation has been tested. ([SIE overview](https://sie.se/format/), [linked 4C sections 4–6 and selected records](https://sie.se/wp-content/uploads/2026/02/SIE_filformat_ver_4C_2025-08-06.pdf))

### Worked case 1: bank movements and all working-paper outputs

This is an independent fictional bookkeeping fixture, not an annual report or taxpayer computation. SEK amounts and debit/credit directions are supplied facts. Opening bank 1930 is 100,000 debit against registered share capital 2081 of 100,000 credit. Voucher L1 is a documented long-term bank loan receipt of 20,000 into 1930, credited to 2350. Voucher R1 is a confirmed current-period premises-rent payment of 5,000, debited to 5010. Voucher F1 is a bank fee of 1,000, debited to 6570. For this fixture, the supplied expense amounts are the final book expense amounts after separately resolved VAT treatment; no VAT deduction, rate, return or actual tax liability is being computed. There are no other balances, transactions or closing transfers.

| Transaction register | Debit | Credit | SEK | Evidence and status |
| --- | --- | --- | --- | --- |
| L1 bank loan receipt | 1930 | 2350 | 20,000 | Fictional signed loan and statement row L1; confirmed |
| R1 rent payment | 5010 | 1930 | 5,000 | Fictional current-period rent invoice and statement row R1; confirmed |
| F1 bank fee | 6570 | 1930 | 1,000 | Fictional bank advice and statement row F1; confirmed |

| Trial balance, before closing transfer | Debit SEK | Credit SEK |
| --- | --- | --- |
| 1930 Företagskonto | 114,000 | 0 |
| 5010 Lokalhyra | 5,000 | 0 |
| 6570 Bankkostnader | 1,000 | 0 |
| 2081 Aktiekapital | 0 | 100,000 |
| 2350 Andra långfristiga skulder till kreditinstitut | 0 | 20,000 |
| Total | 120,000 | 120,000 |

P&L: no revenue; external costs 6,000; operating and net loss 6,000. Balance sheet: cash 114,000; long-term debt 20,000; share capital 100,000 less current loss 6,000 gives equity 94,000. Liabilities plus equity equal assets. The current loss is a statement result derived from the open expense accounts, not another posted 2099 balance.

Reviewer brief: 3 source financial rows, 3 register rows and 3 balanced journals. Opening balance is separately identified. No duplicate, unmatched, private, assumed or unresolved transaction occurs in this deliberately restricted fixture. Bank reconciliation is 100,000 + 20,000 − 5,000 − 1,000 = 114,000, matching the fictional closing statement. The loan is a non-revenue receipt. VAT check 12 is not run because no VAT return is computed; actual engagements need the relevant companion and reconciliation. The restricted fixture does not qualify omitted annual-report notes, tax or filing work.

```oa-check
name: Restricted bank reconciliation and trial balance
inputs:
  opening_bank: 100000
  loan_receipt: 20000
  rent: 5000
  bank_fee: 1000
  opening_capital: 100000
steps:
  - closing_bank: opening_bank + loan_receipt - rent - bank_fee
  - external_costs: rent + bank_fee
  - profit: 0 - external_costs
  - equity: opening_capital + profit
  - liabilities_and_equity: loan_receipt + equity
  - trial_balance_debits: closing_bank + external_costs
  - trial_balance_credits: opening_capital + loan_receipt
expected:
  closing_bank: 114000
  external_costs: 6000
  profit: -6000
  equity: 94000
  liabilities_and_equity: 114000
  trial_balance_debits: 120000
  trial_balance_credits: 120000
```

### Worked case 2: accrual decision, assessed both ways

This independent fictional eligible K2 AB has a 12-month calendar 2026 year under the post-2025 edition. A single real transaction in the fixture, an annual service agreement, costs SEK 6,000 excluding separately resolved VAT and covers July 2026 through June 2027 equally. It is not artificially split and has no other recognition exception. Profit before this cost is a fictional SEK 100,000. The actual accountant must establish the company's consistent policy and whether the individual and combined simplification effects are material before using any relief. These facts are not an election to alter the service period. ([K2 2.4–2.4B and 7.5–7.8](https://www.bfn.se/wp-content/uploads/vl16-10-k2ar-kons2025.pdf))

Under ordinary accrual, 6 of 12 service months belong to 2026: expense 3,000, prepayment 3,000 and profit 97,000. If the approved consistently applied relief is available and its individual/combined effect is not material, the qualifying below-7,000 transaction may instead produce expense 6,000, no prepayment and profit 94,000. The profit difference is 3,000. At exactly 7,000 the small-amount route is unavailable; a 3,000 accrual adjustment does not itself qualify an agreement costing 7,000 or more. If materiality, policy, aggregation or the period is unresolved, retain the ordinary supported treatment for the comparison and mark the relief decision Needs Input; do not choose it to obtain a preferred tax result.

```oa-check
name: Conditional K2 accrual and small-amount comparison
inputs:
  agreement_cost: 6000
  months_current_year: 6
  months_total: 12
  profit_before_cost: 100000
steps:
  - accrual_expense: agreement_cost * months_current_year / months_total
  - accrual_prepayment: agreement_cost - accrual_expense
  - accrual_profit: profit_before_cost - accrual_expense
  - relief_expense: agreement_cost
  - relief_profit: profit_before_cost - relief_expense
  - profit_difference: accrual_profit - relief_profit
expected:
  accrual_expense: 3000
  accrual_prepayment: 3000
  accrual_profit: 97000
  relief_expense: 6000
  relief_profit: 94000
  profit_difference: 3000
```

### Worked case 3: two banks, a linked transfer and a duplicate export row

This fictional SEK case opens with debit bank balances of 10,000 in 1930 and 2,000 in 1940, and credit capital of 12,000 in 2081. The same entity's own-account transfer is booked in the same period without FX or a transfer fee. A 100 bank fee and 200 current accounting-service expense are final book amounts after separately resolved VAT treatment. No other movements, liabilities, tax calculations or closing transfers occur.

| Register row | Source account | Signed SEK | Evidence and disposition | Journal |
| --- | --- | --- | --- | --- |
| A1 | 1930 | -3,000 | Own transfer proved by both statements/common reference | J1 sending side |
| A2 | 1930 | -100 | Statement establishes bank fee | J2 |
| A2-copy | 1930 | -100 | Same source transaction ID/identical row in overlapping second export; retained and excluded with link to A2 | No second journal |
| B1 | 1940 | 3,000 | Receiving side of the proved transfer | J1 receiving side |
| B2 | 1940 | -200 | Current accounting invoice and expense approved | J3 |

The 5 rows contain 4 distinct financial movements. J1 is Dr 1940 / Cr 1930 for 3,000 once; J2 is Dr 6570 / Cr 1930 for 100; J3 is Dr 6530 / Cr 1940 for 200. Equal amounts alone would justify neither the exclusion nor transfer match.

| Trial balance account | Debit SEK | Credit SEK |
| --- | --- | --- |
| 1930 | 6,900 | 0 |
| 1940 | 4,800 | 0 |
| 6530 | 200 | 0 |
| 6570 | 100 | 0 |
| 2081 | 0 | 12,000 |
| Total | 12,000 | 12,000 |

P&L: revenue 0, accounting expense 200 and bank fee 100 give a loss of 300. Balance sheet: bank assets 11,700 equal capital 12,000 less current loss 300; liabilities are 0. Carry the loss once, without a duplicate closing transfer.

Bank controls: 1930 is 10,000 - 3,000 - 100 = 6,900; 1940 is 2,000 + 3,000 - 200 = 4,800. The transfer nets to 0. The reviewer brief records duplicate proof, the two-row/one-journal relationship, expense/VAT assumptions and professional/filing holds. All 5 working-paper outputs are supplied above. This is not a complete annual report or actual bank/SIE import test.

```oa-check
name: Linked bank transfer and proven duplicate reconciliation
inputs:
  bank_a_open: 10000
  bank_b_open: 2000
  transfer: 3000
  bank_fee: 100
  accounting_service: 200
  opening_capital: 12000
  input_rows: 5
  proven_duplicate_rows: 1
steps:
  - bank_a_close: bank_a_open - transfer - bank_fee
  - bank_b_close: bank_b_open + transfer - accounting_service
  - transfer_net: transfer - transfer
  - total_bank: bank_a_close + bank_b_close
  - loss: bank_fee + accounting_service
  - equity: opening_capital - loss
  - tb_debits: total_bank + loss
  - tb_credits: opening_capital
  - balance_difference: total_bank - equity
  - distinct_movements: input_rows - proven_duplicate_rows
  - wrong_duplicate_bank_a: bank_a_close - bank_fee
  - duplicate_reconciliation_error: bank_a_close - wrong_duplicate_bank_a
expected:
  bank_a_close: 6900
  bank_b_close: 4800
  transfer_net: 0
  total_bank: 11700
  loss: 300
  equity: 11700
  tb_debits: 12000
  tb_credits: 12000
  balance_difference: 0
  distinct_movements: 4
  wrong_duplicate_bank_a: 6800
  duplicate_reconciliation_error: 100
```

## Edge cases and special rules

K2 has no separate deferred-tax asset or provision, but gross untaxed reserves include their tax element. This does not waive the eligibility test for a specified material deferred-tax liability. K3 has its own ordinary deferred-tax rules and its legal-person gross-reserve exception; consolidated reporting requires a separate assessment. ([K2 11.5, 13.3, 15.2–15.3 and 16.4](https://www.bfn.se/wp-content/uploads/vl16-10-k2ar-kons2025.pdf); [K3 29.15 and 29.37](https://www.bfn.se/wp-content/uploads/vl12-1-k3-kons20251215.pdf))

For K2, a reserve generally requires a statutory deduction condition that the corresponding amount is booked, apart from the specified replacement-fund exception under IL 31:10, 31:11 and 31:13. A label or BAS code is not evidence of eligibility. ([K2 15.3](https://www.bfn.se/wp-content/uploads/vl16-10-k2ar-kons2025.pdf))

### Periodiseringsfond: selected tax bridge

- **Deferral limit**: An eligible legal person may deduct at most 25% of business surplus before the fund deduction (IL 30:5).
- **Reversal period**: Reverse the oldest deduction first, no later than the sixth tax year after its deduction year. Earlier reversal triggers and legacy inclusion uplifts require a fund-vintage check (IL 30:7–8; SFS 2018:1206 transition point 5).
- **Accounting treatment**: Record an eligible gross reserve in the correct year-specific BAS family, with separate vintage and movement reconciliation; the 2120/2130 families are not a continuous set of interchangeable accounts
- **Taxpayer and book provision**: Apply the relevant legal-person or individual rules. Swedish partnership deductions and allocations are calculated separately for each partner (IL 30:2). A legal person required to prepare the specified annual accounts may deduct an allocation only with a corresponding book provision (IL 30:3).
- **Legal-person deemed income**: A legal person that has deducted a fund allocation must include schablonintäkt under IL 30:6a. Use the qualifying opening funds and the government borrowing rate at the end of November preceding the calendar year in which the tax year ends, with a 0.5% rate floor and an adjustment for a tax year longer or shorter than 12 months. Verify the actual rate and fund history before computing an amount.

These selected rules do not establish eligibility or a complete fund calculation for an actual entity. Validate the applicable period, fund vintages, historic inclusion uplifts, transfers and earlier reversal triggers. ([Inkomstskattelag (1999:1229), Chapter 30 and reproduced SFS 2018:1206 transition](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json))

### Tax and other-domain handoffs

For AB tax, load `se-corporate-income-tax` only with its base, applicable source/period qualification and professional review. That companion remains a draft; this reference does not confer sign-off or clear its filing/payment holds. `se-income-tax` concerns sole traders, not an AB. VAT, payroll, social contributions, invoicing and financial statements need their own qualified companions and complete outputs. A code containing a rate, or a profit from the bookkeeping case, does not supply any tax base, rate, return or election. The historical shortcuts withdrawn below stay unavailable until separately qualified.

### When to refuse or refer

Stop the affected calculation or deliverable for an unknown period/framework, incomplete mandatory country slot, unreadable/missing source rows, unsupported chart code, unresolved material transaction, unbalanced entry/control, unqualified tax treatment, incomplete statement/note mapping, going-concern uncertainty without the relevant assessment, or an unverified filing route. Keep the evidence, question and required reviewer action in the brief. Do not generate a plug, assume a professional approval, treat an AB as a sole trader or produce a filing-ready set from these outlines.

## Self-checks

Run all 12 base checks: trial balance equality, source completeness, journal equality, bank reconciliation, P&L-to-trial-balance, balance-sheet equality, balance-sheet-to-trial-balance, Tier 2/3 disclosures, no private P&L, revenue-to-receipts bridge, valid documented account codes and applicable VAT control reconciliation. Record an explicit not-run reason for a genuinely inapplicable check; a hold is not a pass. Trace every input and adjustment to its source document, every selected figure to its period and primary source and every unresolved edge case to the reviewer brief.

Confirm the 5 outputs agree, reserves are gross where required, final/current tax and other statutory controls remain distinct, contra assets and closing results are not duplicated and actual ledger codes have not been silently replaced. For a full annual report, verify all framework-specific statements, comparatives, notes, management report, signatures and filing acceptance before lifting the corresponding holds.

**Country-slot status:** this version supplies 32 conditional rules, 15 counterparty investigation routes, conservative defaults, selected currency/number rules, bank/SIE documentation routes and 3 fictional working-paper cases. Actual export/schema qualification, parsing/import acceptance, full entity-specific recognition/defaults, FX/rounding implementation and complete statement/note mapping remain unqualified. Full statutory and K1/K3/group workflows also remain incomplete. These additions do not establish operational conformance with every mandatory country slot.

## Sources

A read date applies to the identified selected parts, not to a claim that every page of a long act or manual was read. Current BFL and ÅRL API bytes were re-fetched on 2 November 2026 and match the retained primary captures. That identity check is separate from substantive reading. The post-2025 manuals carry publication/update dates in 2025; those dates are not the application year.

| Primary source | Parts actually read and qualification | Read on |
| --- | --- | --- |
| [Bokföringslag (1999:1078), through SFS 2024:342](https://data.riksdagen.se/dokumentstatus/sfs-1999-1078.json) | Selected 3:1–6, 4:6, 5:2–11, 6:1–3 and 7:1–6 for financial year, recording/closing and archive conditions; not whole-act qualification | 2026-11-02 |
| [Årsredovisningslag (1995:1554), through SFS 2026:780](https://data.riksdagen.se/dokumentstatus/sfs-1995-1554.json) | Selected 1:3, 2:6 and 8:3, 8:5–6 for size, certified copies and distinct deadline/fee clock; full statements, notes, audit and amendment chain not established | 2026-11-02 |
| [BFN K2 BFNAR 2016:10, consolidated through BFNAR 2025:2](https://www.bfn.se/wp-content/uploads/vl16-10-k2ar-kons2025.pdf) | Selected chapter 1, 2.4–2.4B, 3.8–3.9, the cited chapter 6 recognition paragraphs, 7.9, 10.4–10.6, 10.20–10.26, 10.40–10.42, selected tax/reserve paragraphs, 18.4 and transition p333; selected substantive reading, not complete K2 implementation | 2026-11-02 |
| [BFN K2 chapter 4 formats and AB additions](https://www.bfn.se/wp-content/uploads/vl16-10-k2ar-kons2025.pdf) | Retained selected format/caption and AB 4.10–4.12 readings and native page checks; this supports the conditional map and outline limitations, not a complete annual-report implementation. These are the earlier actual readings, not stamped as reread today | 2026-11-01 |
| [BFN K3 BFNAR 2012:1, updated 15 December 2025](https://www.bfn.se/wp-content/uploads/vl12-1-k3-kons20251215.pdf) | Selected 1.3, 17.4/17.13/17.20, 23.18/23.31–23.32 and 29.37; retained 29.15 and transition-selector context was read on 1 November 2026. No complete K3/group workflow | 2026-11-02 |
| [BAS 2026 official chart, actual cover v1.1](https://www.bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.pdf) | Cover/# legend and every code/label in the subset; not separate paid closing guidance, tax eligibility or automatic chart-to-statement mapping | 2026-11-02 |
| [SFS 2025:872, section 1: 2026 price base amounts](https://data.riksdagen.se/dokumentstatus/sfs-2025-872.json) | Ordinary SEK 59,200 distinguished from higher SEK 60,500; half amount is derived. Retained primary text read for the 2026 input | 2026-11-01 |
| [Inkomstskattelag (1999:1229), chapter 30 and SFS 2018:1206 transition](https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json) | Selected complete chapter 30 and fund-transition units retained for the legal-person/partner, book provision, floor, year-length and vintage conditions. No actual taxpayer fund calculation | 2026-11-01 |
| [SIE overview](https://sie.se/format/) and [linked 4C PDF](https://sie.se/wp-content/uploads/2026/02/SIE_filformat_ver_4C_2025-08-06.pdf) | Overview; selected types, file-format/mandatory-record units, #TRANS, #VALUTA, #VER and revision notes. Cover says 4C but title metadata includes DRAFT; final status unresolved. No complete implementation/acceptance | 2026-11-02 |
| [Nordea formats](https://www.nordea.se/foretag/produkter/betala/programleverantorer/vara-tjanster-programleverantorer.html), [file handling](https://www.nordea.se/filhantering) and [EKK description](https://www.nordea.se/Images/154-16151/postbeskrivning-elektroniskt-kontoutdrag.pdf) | Service/format descriptions and all 6 EKK v1.3 pages; layout-sensitive positions not implemented/certified. Actual customer/version compatibility held | 2026-11-02 |
| [Revolut statements](https://help.revolut.com/sv-SE/business/help/managing-my-business/viewing-my-account-statements/how-to-get-a-monthly-statement/) | Export routes, currency and UTC/local-time conditions; no complete CSV schema | 2026-11-02 |
| [Isof decimals](https://frageladan.isof.se/faqs/21402) and [grouping](https://frageladan.isof.se/faqs/30318) | Complete short language answers; prose conventions, not import schemas | 2026-11-02 |
| Official provider pages linked in the counterparty library | Selected service descriptions, investigation context only; no customer identity/accounting/tax conclusions. Skatteverket route uses BAS labels and requires actual statement evidence | 2026-11-02 |

Not yet confirmed: full country-slot completion; current K1 manual and historical 2025 qualification; complete K2/K3/group/other-entity annual-report workflows and transitions; going-concern assessment and disclosures; complete balanced statement/note mapping; current building-advice edition; tax-domain shortcuts listed below; actual bank/SIE schema/version qualification, parsing and acceptance; complete FX/rounding implementation; complete filing/software/portal, signature, confirmation, payment and correction mechanics; professional approval.

### Removed and why

The earlier guide's topics stay in scope. These inherited shortcuts have been withdrawn from operative use rather than carried forward as qualified rules. Their original text is preserved in the local before/after evidence inventory. Source-backed corrections above replace the false financial-year, invoice-date, K2 straight-line-only, no-revaluation, optional-grouping and chart-label assertions. No actual ledger has been recoded.

| Withdrawn shortcut or incomplete area | Disposition |
| --- | --- |
| Popularity and prevalence | unverified: No supporting primary evidence in this source set. These prevalence claims do not establish accounting treatment. |
| Unassigned or local chart codes | unverified: These are not established as assigned continuous official BAS 2026 codes. Actual local charts require definitions and an approved mapping, not silent recoding. |
| K1 mechanics | unverified: BFL supplies the simplified-closing gate, not these K1 recognition, accrual, inventory, depreciation-base or NE filing mechanics. Obtain the applicable K1 manual, tax source and period first. |
| Blanket tax deductions, representation and gifts | unverified: A BAS expense classification does not establish a tax deduction. The inherited 100% assertions and representation/gift ceilings are not qualified. Do not use them for a tax computation. |
| Vehicles and mileage | unverified: The inherited SEK 25/km unit and vehicle-benefit summaries lack qualified support here. Do not use the unit, infer a correction or calculate a deduction from this guide. |
| Tax depreciation and building categories | unverified: The inherited rate/base shortcuts, useful-life wording, building categories and universal land-improvement rate are not a complete qualified tax method. Use the separately qualified corporate tax guide and period-specific primary sources; the building-advice edition remains held. |
| Historical 2025 half-PBB and K1 base limits | unverified: Only the 2026 PBB input and the selected K2 recognition rule are used below. Earlier-year and K1 rules require their own primary period qualification. |
| Sole-trader tax, VAT and payroll shortcuts | unverified: These are different tax jobs. The inherited social-contribution age band, home-office amount, approximate own-contribution rate and VAT rate/filing summaries do not establish current eligibility, base, period or filing mechanics. Obtain the corresponding qualified companion and professional review. |
| Bank exports and SIE compatibility | Inherited generic format/compatibility claims stay withdrawn. Selected official bank/EKK/SIE documentation is described above with version/publication qualifications; actual file/schema qualification, parser and vendor acceptance remain unverified. |
| Inherited framework hierarchy | unverified: The old hierarchy conflated framework scope, listed/consolidated IFRS and RFR 2 and wrongly listed natural persons under this K2 manual. The current selected K2/K3 selectors replace it; unqualified K1 and IFRS/RFR workflows remain held. |

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon. The most up-to-date version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com).

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
