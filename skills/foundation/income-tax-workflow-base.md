---
name: income-tax-workflow-base
description: Universal income tax computation workflow base for individuals, sole traders, freelancers and other taxpayers whose income is taxed at the personal level in any jurisdiction. Defines the order of operations from document intake to a reviewer-ready computation — profile confirmation, income and expense classification, the ladder from gross income to taxable income, the country rate schedule, allowances, credits, withholding, prepayments and the balance due — plus the classification tiers, five-output specification, twelve self-checks and the country skill contract. Contains no rates, no brackets, no allowances, no thresholds, no form references. MUST be loaded alongside a country-specific income tax skill (for example albania-income-tax, uk-income-tax-sa100 or jp-income-tax) that supplies the rules. This file alone cannot produce any output.
version: 1.0
category: foundation
jurisdiction: GLOBAL
tier: 2
last_updated: 2026-09-28
---

# Income Tax Workflow Base Skill v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## What this file is, and what it is not

**This file contains workflow architecture only.** It defines how Claude should approach an income tax computation for an individual, sole trader, freelancer, landlord, investor, or any other taxpayer whose income is taxed at the personal level: the order of operations, how to classify income and expenses from the documents provided, how to move from gross income to the balance due or refundable, how to handle ambiguity, what to produce, and what to check before delivering. It contains no tax rates, no brackets, no allowances, no thresholds, no deduction rules, no filing deadlines, no form names, no year-specific figures of any kind.

**This file must always be loaded with a country-specific income tax skill** that provides the rate schedule, the allowances and credits, the income categories and their treatment, the deductible-expense rules, the transaction pattern library, the filing forms and deadlines, and the refusal catalogue (e.g., `albania-income-tax`, `uk-income-tax-sa100`, `jp-income-tax`). This file alone cannot produce a tax computation, a working paper, or a filing calendar. Loading it without a companion is a configuration error and Claude must refuse to proceed.

**This file is the contract.** When a country income tax skill says it conforms to v1.0 of this base, it means: it fills the country slots specified in Section 6, it produces outputs in the format specified in Section 3, its computations can be validated by the self-checks in Section 5, and it participates in the workflow in Section 1.

**Where this base sits among the others.**

- Corporations file under `corporate-income-tax-workflow-base`, not this one. A company's profit computation, group relief, and deferred tax are that base's job.
- US federal and state returns follow `us-tax-workflow-base`, which carries the IRC-specific form structure this base deliberately omits.
- Employer-side withholding and payslips belong to `payroll-workflow-base`. The employee's annual position — which consumes the withholding certificates that payroll produces — belongs here.
- Social security and health contributions have their own lifecycle in `social-contributions-workflow-base`. This base consumes the contribution figures where the country skill makes them deductible from income or creditable against tax.
- Cross-border facts (foreign-source income, treaty relief, dual residence, split years) hand off to `cross-border-workflow-base`. This base computes the domestic position and flags every foreign item.
- Crypto-asset disposals and crypto income are computed under `crypto-tax-workflow-base`; the resulting figures come back into the computation ladder here as income or gains in the category the country skill assigns.

---

## Section 1 — The workflow (read this first, follow exactly)

You are helping an individual, sole trader, or freelancer prepare an income tax computation for one tax year. The output will be reviewed by a qualified accountant or tax adviser before anything is filed or paid. Your job is to do the mechanical classification and computation work and produce a complete, cited working paper plus a reviewer brief that makes the human reviewer's job fast and accurate.

Execute these nine steps in order. Do not skip. Do not reorder. Do not classify a single transaction before the profile in step 4 is confirmed. Do not build any output files before step 8.

### Step 1 — Confirm the companion skills are loaded

This workflow base requires a country-specific income tax skill providing the rate schedule, allowances, credits, income categories, expense rules, transaction patterns, filing mechanics, and refusals.

If no country-specific skill is loaded, stop and tell the user: "I need a country-specific income tax skill loaded alongside this workflow base. Which jurisdiction and which tax year is this computation for?" Do not proceed without it.

Check that the country skill's declared tax year matches the year being computed. Rates and thresholds from the wrong year are the single most common error in an income tax computation. If the years differ, stop and say so; do not extrapolate figures.

If a payroll, bookkeeping, social contributions, or crypto tax skill is also loaded, note its presence. Consume the outputs those skills produce (net pay and withholding, the trial balance, contribution totals, disposal gains) rather than recomputing them here.

### Step 2 — Establish the tax year, residency, and filing unit

From the documents and the user's instructions, establish:

- The **tax year** and, for business income, the **basis period** — calendar year, fiscal year, or the accounting period the country skill maps onto the tax year.
- **Residency** for the year, under the test the country skill states. This base handles full-year residents taxed on the basis the country skill describes. A non-resident, a split-year resident, or a dual resident is either in the country skill's refusal catalogue or a hand-off to `cross-border-workflow-base`.
- The **filing unit** — individual, joint or household return, or income splitting between spouses — per the country skill.
- The **taxpayer type** — employee, self-employed or sole trader, partner in a transparent partnership (that partner's share only), landlord, investor, or a mix. A corporation is a stop: load `corporate-income-tax-workflow-base` instead.

If any of these cannot be established from the documents, queue the question for Step 4. Do not guess residency or the filing unit.

### Step 3 — Read the documents

The user will provide bank statements, sales and purchase invoices, receipts, payroll or withholding certificates, a prior-year return, prepayment or instalment receipts, contribution statements, broker or exchange reports, rental agreements, loss schedules, or a combination. Read every document provided. Do not skim.

Extract: gross receipts by source; tax withheld at source; prepayments and instalments already paid; expense lines and their counterparties; capital items purchased or disposed of; contributions paid; losses brought forward and other carryforwards from the prior return; elections visible on the prior return; and every item with a foreign counterparty, currency, or address (flag these — they are not classified until Step 5).

Every line on a bank statement is one of: income, expense, capital, transfer or exclusion, or unknown. Nothing is skipped because it is small.

If no documents are provided at all, stop and tell the user what is needed.

### Step 4 — Infer and confirm the taxpayer profile (one round trip)

Produce a one-line profile:

> "[Taxpayer reference] — [taxpayer type], [residency status], tax year [YYYY], sources: [list], accounting basis: [cash / accrual], registrations: [VAT/GST or none], prepayments made: [amount], losses brought forward: [amount]"

Present it, then in the same message ask **only** the questions the documents did not answer — typically business-use percentages, elections made, whether this is the first year of trading, whether a spouse has income, and the Tier 3 items queued in Steps 2 and 3:

> "Here is what I have inferred from your documents:
>
> [profile line]
>
> Is this correct? I also need: [numbered questions]. Reply with corrections and answers and I will proceed."

Wait for confirmation. If the user corrects anything, update and re-confirm. Do not re-ask what the documents already answered.

### Step 5 — Classify income by source

Use the income categories the country skill defines (typically employment, business or professional, rental or property, investment, capital gains, and other) and its transaction pattern library. For every credit on the bank statement and every invoice or certificate:

- Assign exactly one category, or an exclusion: transfer between the taxpayer's own accounts, loan drawdown, refund of the taxpayer's own money, capital introduced, VAT or GST collected on behalf of the authority, or disposal proceeds tracked in the capital schedule.
- Where the country skill says a receipt arrives **net of withholding**, gross it up and record the withholding credit beside it. The gross amount is income; the withholding is settled in Step 7.
- Where the system is **schedular**, keep the categories separate through the whole ladder; where it is **global**, aggregate at the point the country skill specifies.
- Record the tier (Section 2) of every classification decision.

### Step 6 — Classify expenses, deductions, allowances, and reliefs

For every debit on the bank statement and every purchase invoice:

- **Deductible business expense** — assign the country skill's category.
- **Partially deductible** — apportion by the business-use percentage confirmed in Step 4, or by the country skill's statutory fraction.
- **Capital item** — do not deduct; add it to the capital schedule and apply the country skill's capital allowance or depreciation method.
- **Non-deductible** — record it with the rule that disallows it. The reviewer needs to see it was considered, not silently dropped.
- **Personal or exclusion** — drawings, private spending, transfers, loan repayments (principal), tax payments themselves.

Then apply the personal-level items the country skill lists: contributions paid, pension or retirement contributions, insurance, family and dependant deductions, the personal allowance and any taper. Apply them in the **order the country skill specifies** — under progressive rates the sequence of deductions, allowances, and credits changes the answer.

**Losses.** Apply current-year loss relief and losses brought forward only as the country skill permits: per source, per period, and subject to any cap. Never net a loss against a source the country skill does not allow. Keep a loss memorandum showing what was used and what carries forward.

### Step 7 — Compute the tax

Walk this ladder. Every line carries its source figure, the rule applied, and the citation from the country skill.

1. **Gross income by source** (from Step 5).
2. Less allowable expenses and capital allowances per source → **net income by source**.
3. Less loss relief → **total income**.
4. Less deductions and personal allowances → **taxable income**.
5. Apply the rate schedule (Section 4) per band, or per schedule for schedular items → **gross tax**.
6. Less non-refundable credits, floored at zero unless the country skill says otherwise.
7. Plus surcharges, levies, and local or municipal taxes the country skill layers on top → **tax liability**.
8. Less refundable credits, withholding suffered, and prepayments made → **balance due or refundable**.
9. **Next-year prepayments or instalments**, where the country skill derives them from this year's liability.

Do not skip a rung because it is zero; show it as zero. Do not combine rungs.

### Step 8 — Build the outputs

Produce the five outputs specified in Section 3. All five are mandatory. Never produce one without the others.

### Step 9 — Self-checks and delivery

Run the twelve checks in Section 5 against all outputs. If any check fails, fix and re-run all twelve. Only present outputs to the user when all checks pass. Deliver with the reviewer brief first.

---

## Section 2 — Classification tiers

Every classification and computation decision falls into one of three tiers.

### Tier 1 — Confident

The documents, the confirmed profile, and the country skill's rules point to one and only one treatment. The invoice says what was sold, the country skill says which category that is, the rate is in the table. A competent preparer would make the same call without hesitation.

**Action:** Classify and compute silently. Do not narrate. Do not flag.

### Tier 2 — Assumed

The documents provide clues but not certainty. A competent preparer would make an assumption, note it, and move on.

**Action:** Apply the conservative default (below), flag it in the reviewer brief with the alternative treatment and its cash impact, and record the assumption in the working paper.

Conservative defaults for income tax — always the treatment that produces **more** tax:

- **Receipt of uncertain character:** taxable, in the highest-taxed category the facts allow.
- **Expense of uncertain character:** personal — not deducted.
- **Business-use proportion unknown:** 0% business use.
- **Revenue or capital unclear:** capital — relieved over time under the country skill's allowances, never written off immediately.
- **Election unknown:** not made.
- **Withholding without a certificate:** no credit claimed; the reviewer brief asks for the certificate.
- **Prepayment without a receipt or authority statement:** not credited.
- **Allowance eligibility unknown (dependants, age, disability, family status):** not claimed.
- **Loss availability unknown (no prior return seen):** not used.
- **Deduction cap or threshold test undeterminable:** the cap applies.

### Tier 3 — Needs Input

The computation cannot proceed without information only the user possesses, and a conservative default would be a guess about the person rather than about a transaction.

**Action:** Queue for the user question in Step 4. Do not guess. Do not apply a default until the user has been asked and either answered or said "don't know" — then apply the conservative default and disclose it.

Examples:

- Residency or day counts are unclear.
- Whether an activity is a business, an occasional sideline, or a hobby.
- Whether the person is an employee or self-employed for a given engagement (misclassification is severe in both directions).
- Whether the taxpayer trades personally or through a company.
- Which year a large receipt or payment belongs to, when the accounting basis makes that a choice.
- Any foreign-source income, foreign account, or foreign tax paid.
- Whether a significant asset was disposed of during the year.

---

## Section 3 — Output specification

Five outputs per computation. All five are mandatory. Never produce one without the others.

### Output 1 — Transaction classification register

One row per bank statement line, invoice, or certificate line. Format:

| Date | Description | Amount | Direction | Category (country skill code) | Business % | Amount allowed | Tier | Rule / citation | Note |
|---|---|---|---|---|---|---|---|---|---|

The register's credits, debits, and exclusions must reconcile to the statement's total movement. Exclusions are rows, not omissions.

### Output 2 — Income tax computation working paper

The ladder from Step 7, one line per rung, with the source of every figure. Format:

```
INCOME TAX COMPUTATION — [taxpayer reference], tax year [YYYY], [currency]

A. INCOME BY SOURCE
   Business / professional receipts                    [amount]
   Less allowable expenses                            ([amount])
   Less capital allowances / depreciation             ([amount])
   Net business income                                 [amount]
   Employment income (gross, per certificates)         [amount]
   Rental income (net of allowable costs)              [amount]
   Investment income                                   [amount]
   Other income                                        [amount]
   Less loss relief                                   ([amount])
   TOTAL INCOME                                        [amount]

B. DEDUCTIONS AND ALLOWANCES (in the country skill's order)
   [Deduction line, per country skill]                ([amount])
   Personal allowance (after taper)                   ([amount])
   TAXABLE INCOME                                      [amount]

C. TAX
   Band 1: [lower]–[upper] @ [rate]                    [amount]
   Band n: ...                                         [amount]
   [Schedular / flat-rate items]                       [amount]
   GROSS TAX                                           [amount]
   Less non-refundable credits                        ([amount])
   Plus surcharges / levies / local taxes              [amount]
   TAX LIABILITY                                       [amount]

D. SETTLEMENT
   Less withholding suffered (per certificates)       ([amount])
   Less prepayments / instalments paid                ([amount])
   Less refundable credits                            ([amount])
   BALANCE DUE / (REFUNDABLE)                          [amount]
   Next-year prepayments (per country skill)           [amount]
```

The country skill supplies the form and line references that each rung maps onto, if its return is line-numbered.

### Output 3 — Filing and payment calendar

| Filing / payment | Amount | Due date | Authority / portal |
|---|---|---|---|
| Annual return | N/A | [date] | [portal] |
| Balance due | [amount] | [date] | [authority] |
| Prepayment / instalment 1..n | [amount] | [date] | [authority] |
| [Other filings the country skill requires] | | | |

The country skill provides the form names, portals, and deadline rules.

### Output 4 — Reviewer brief

```markdown
# [Country] Income Tax — Reviewer Brief
**Taxpayer:** [reference]
**Tax year:** [YYYY]    **Basis period:** [dates]
**Generated:** [date]

## Summary
- Total income: [amount] [currency]
- Taxable income: [amount]
- Tax liability: [amount]
- Balance due / (refundable): [amount]
- Effective rate on taxable income: [x.x%]
- Tier 1 (confident): [count of decisions]
- Tier 2 (assumed, flagged): [count]
- Tier 3 (user-answered): [count]

## High-priority items (review first)
[Numbered list: largest cash impact or highest uncertainty first.
Each: one sentence what, one sentence why it matters, one sentence
what the reviewer should do.]

## Assumptions made (Tier 2 defaults)
[For each: the item, the default applied, the alternative, and the
cash impact of the alternative.]

## Questions asked and user answers (Tier 3)
[For each: the question, the answer or "don't know — default applied",
and the resulting treatment.]

## Decisions for the taxpayer or reviewer
[Elections, basis choices, regime options: each option and its cash
impact this year and next.]

## Items the reviewer should verify
[Specific: certificates to obtain, invoices to sight, residency
evidence, prior-year figures to confirm. Not generic "check everything."]
```

### Output 5 — Action list for the taxpayer

What to do, when, and how much: file, pay, register, retain records, obtain missing certificates, and make the decisions listed in the reviewer brief. Every payment and filing in Output 3 appears here with its date and amount.

---

## Section 4 — Computation rules

This section defines the universal mechanics. The country skill provides every figure; this section provides the way figures are applied.

### Progressive rate schedules

Apply rates to **slices**. Each band taxes only the portion of taxable income that falls between its lower and upper limits; the sum of the slices is taxable income. Never apply a band's rate to the whole amount. Where the country skill states bands per filing unit (single, joint, household), use the unit confirmed in Step 2. Where a schedular item has its own flat rate, tax it outside the progressive schedule and do not count it in the slices.

### Allowances, deductions, and credits

An **allowance or deduction** reduces taxable income; its value is the taxpayer's marginal rate. A **credit** reduces tax; its value is its face amount. Apply phase-outs and tapers on the base the country skill defines (total income, adjusted income, taxable income), computed before the item they reduce. Unless the country skill says otherwise, the order is: source expenses, then loss relief, then deductions, then allowances, then rates, then credits.

### Presumptive and flat-rate regimes

Where the taxpayer qualifies for a simplified regime (turnover-based, presumptive expenses, flat rate on receipts), compute under the regime **and** under the general rules only when the regime is elective and the country skill calls for the comparison. Present the result as a decision in Output 4. Never elect on the taxpayer's behalf.

### Withholding, prepayments, and instalments

Withholding suffered and prepayments made are credited at face value, and only when evidenced by a certificate, a receipt, or an authority statement. Where the country skill derives next year's instalments from this year's liability, compute them on the confirmed liability and show the rule.

### Accounting basis and timing

Use the basis the country skill assigns or the taxpayer elected: cash (receipts and payments in the year) or accrual (invoices raised and costs incurred in the year). Receipts and payments that straddle the year end, prepayments covering more than one year, and deposits are timing items — flag them and apply the basis rule, do not average.

### Losses

Loss relief is per source, per period, and per cap exactly as the country skill states. Losses used, losses restricted, and losses carried forward are three separate figures in the loss memorandum.

### Interaction with contributions and other taxes

Social contributions are deductible, creditable, or neither, per the country skill; take the figure from the social contributions or payroll skill's output where one is loaded. Local and municipal income taxes, solidarity surcharges, and health levies are separate rungs on the ladder, not adjustments to the rate. Wealth, property transfer, and inheritance taxes are outside this base.

### Foreign items

Every foreign-source receipt, foreign account, and foreign tax paid is flagged. Foreign tax is credited or deducted only as the country skill and `cross-border-workflow-base` permit; it is never silently netted against income.

### Currency and rounding

Compute in the filing currency. Convert foreign amounts at the rate and date the country skill specifies. Round as the country skill instructs; if it is silent, carry full precision through the ladder and round only the final tax figures to the currency's smallest unit.

### Mid-year changes

Where a rate or threshold changed during the tax year, the country skill states the effective date and whether the year is time-apportioned. Apply exactly that; do not blend rates.

---

## Section 5 — Self-checks (run before delivering output)

Run these twelve checks against all outputs. If any fails, fix and re-run all twelve. Do not deliver until all pass.

### Arithmetic integrity

**Check 1 — Register reconciles to the statements.** Classified credits plus classified debits plus exclusions equal the total movement on every bank statement and every invoice list. No line is missing.

**Check 2 — Every subtotal recomputes.** Net income by source, total income, taxable income, gross tax, tax liability, and the balance each equal the sum of the lines above them. Not approximately — exactly.

**Check 3 — Band slices sum.** The slices in section C of the working paper sum to the amount subject to the progressive schedule. No slice exceeds its band's width.

**Check 4 — Effective rate within bounds.** Tax liability divided by taxable income lies between zero and the top marginal rate (plus surcharges the country skill adds). A 0% effective rate is valid only if taxable income is below the first threshold.

**Check 5 — Credits do not go negative.** Non-refundable credits reduce gross tax to no less than zero. Only credits the country skill marks refundable can produce a refund.

**Check 6 — Settlement reconciles.** Tax liability less withholding, prepayments, and refundable credits equals the balance. Withholding claimed equals the sum of the certificates sighted.

### Cross-output consistency

**Check 7 — Working paper totals match the register.** Each income and expense category in the working paper equals the register total for that category.

**Check 8 — Calendar amounts match the working paper.** The balance due and each instalment in Output 3 equal the figures in section D of Output 2.

**Check 9 — Action list is complete.** Every filing and payment in Output 3 and every decision in Output 4 appears in Output 5.

### Disclosure and completeness

**Check 10 — Every figure is cited and current.** Every rate, threshold, allowance, and credit carries a citation from the country skill, and the country skill's tax year matches the profile's tax year.

**Check 11 — Tier 2 and Tier 3 disclosure complete.** Every decision marked Tier 2 or Tier 3 in the register has an entry in the reviewer brief. Counts on both sides match.

**Check 12 — Nothing counted twice or dropped.** No amount is both expensed and capitalised; no receipt appears in two income categories; no exclusion carries business character; every foreign item is flagged in the brief.

### Failure handling

If any check fails, fix the output and re-run all twelve. If a check fails twice in a row on the same item, stop and report the failure to the user rather than silently working around it.

---

## Section 6 — Country skill contract

Every country-specific income tax skill loaded alongside this workflow base MUST provide the following. The country skill is incomplete without all mandatory slots.

### Mandatory slots

1. **Tax year and basis period** — the year's dates, how business accounting periods map onto it, the filing unit, and a summary of the residency test with the refusal or hand-off for anyone who fails it.
2. **Income categories and their treatment** — the categories, whether the system is schedular or global, and where each common receipt type goes.
3. **Rate schedule** — bands and rates per filing unit, flat or schedular rates, surcharges and levies with their base, and effective dates.
4. **Allowances, deductions, and credits** — amounts, eligibility, tapers and phase-outs, ordering, and whether each credit is refundable.
5. **Expense rules** — what is deductible, what is apportioned and how, what is capital (with the allowance or depreciation method and rates), and what is disallowed.
6. **Loss relief rules** — per source, carry-forward and carry-back periods, caps, and ordering.
7. **Withholding and prepayment mechanics** — which receipts arrive net, how withholding is evidenced, and how next year's instalments are computed and dated.
8. **Interaction with social contributions** — whether contributions are deductible or creditable, and which skill computes them.
9. **Filing mechanics** — forms, portals, deadlines, payment methods, and penalties for late filing and late payment.
10. **Transaction pattern library** — income patterns, expense patterns by category, exclusions, and how the country's banks present statements.
11. **Refusal catalogue and country-specific conservative defaults** — the situations the skill must not compute, and the defaults that extend Section 2.
12. **Currency, conversion, and rounding rules.**
13. **Worked examples** — at least one employee, one self-employed taxpayer, and one mixed case, each walking the full ladder to the balance due.

### Optional slots

14. **Special regimes** — presumptive, flat-rate, or simplified-expense regimes with their thresholds and the comparison rule.
15. **Capital gains interplay** — where gains sit inside or beside the income tax computation.
16. **Local and municipal taxes** — rates by locality and how the locality is determined.
17. **Integration notes** — how the skill consumes the payroll, bookkeeping, social contributions, crypto, and cross-border skills in the same pack.

---

## Section 7 — Reference material

### Validation status

This file is v1.0 of `income-tax-workflow-base`, drafted in September 2026 as part of the Open Accountants skill architecture. It follows the structural pattern established by `payroll-workflow-base` v1.0 and `bookkeeping-workflow-base` v1.0. It was written to back the `depends_on: income-tax-workflow-base` declaration that 174 country content skills already carried while no file of that name existed; the shape those skills share — quick reference, refusal catalogue, transaction pattern library, worked examples, Tier 1 rules, Tier 2 catalogue — is what the country skill contract in Section 6 formalises.

### Design decisions

1. **Individuals only.** Corporate profit computations have different inputs (audited accounts, group relief, deferred tax) and their own base. Keeping them apart keeps each contract short.
2. **A computation ladder, not a form map.** Form line numbers differ by country and change yearly; the nine rungs in Step 7 do not. The country skill maps rungs to lines.
3. **Withholding and prepayments are Tier 2 until evidenced.** Crediting an unevidenced amount understates the balance due — the error the reviewer cannot recover from after filing.
4. **Regime elections are decisions, never defaults.** The skill computes the options and their cash impact; the taxpayer and reviewer choose.

### Known gaps

1. Partnership returns are not covered; a partner's share of profit is handled as that partner's income only.
2. Trusts and estates are not covered.
3. Non-residents, split-year residents, and dual residents are refused or handed to `cross-border-workflow-base`.
4. Amended returns and voluntary disclosures are not covered.
5. Capital gains mechanics are a country slot; this base only positions the resulting figure on the ladder.

### Change log

- **v1.0 (September 2026):** Initial release. Establishes the universal income tax workflow, three-tier classification system, five-output specification, twelve self-checks, and country skill contract.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
