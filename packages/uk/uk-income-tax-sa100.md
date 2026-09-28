---
name: uk-income-tax-sa100
description: Use this skill whenever asked about UK income tax for individuals filing SA100 Self Assessment. Trigger on phrases like "income tax UK", "SA100", "personal allowance", "tax bands", "tax computation", "marriage allowance", "savings allowance", "dividend allowance", "Scottish tax rates", "payments on account", "tax reducers", "tax relief", "April 2026", "2026-27", "Autumn Budget 2025", "income tax bands frozen 2027-28", or any question about computing a UK individual's income tax liability. Covers personal allowance (including taper), income tax bands for rUK and Scotland, marriage allowance, savings and dividend allowances, tax reducers, the final tax computation, payments on account, and the Autumn Budget 2025 changes from April 2026. ALWAYS read this skill before touching any UK income tax return work.
version: 2.2
jurisdiction: GB
tax_year: 2025
tax_year_notes: "2024-25, 2025-26 and 2026-27; 2026-27 reconciled to Finance Act 2026 (c. 11)"
last_updated: 2026-09-12
reviewed_by: James Power
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

> This revision includes changes made after the recorded accountant review and awaits a new review.

# UK Income Tax Sa100

## UK Income Tax (SA100) -- Individual Tax Computation Skill v2.2

This skill covers **three tax years in parallel**:

- **Prior year:** 2024-25 (6 April 2024 -- 5 April 2025) -- filed by 31 January 2026
- **Current year:** 2025-26 (6 April 2025 -- 5 April 2026) -- filed by 31 January 2027
- **From 6 April 2026:** 2026-27 (6 April 2026 -- 5 April 2027) -- filed by 31 January 2028

All headline income tax rates and thresholds are **frozen through 2027-28**. The Autumn Budget 2025 announced targeted rate increases on investment income, but they do **not** all start together: **dividends** rise from 6 April 2026, while **savings** and **property** income rise from 6 April **2027** -- see Section 1.5.

## Rates and thresholds: review pending

> Reviewed against the cited tax authorities by **James Power** on 2026-06-03.
> Items flagged for further clarification are tracked separately and excluded here.
> This block is generated from verified `skill_facts` — edit the facts, not the prose.

### Income Tax SA100

- **Personal allowance** — £0 – £12,570 at 0%  _(ITA 2007)_
- **Basic rate (rUK)** — £12,571 – £50,270 at 20%  _(ITA 2007)_
- **Higher rate (rUK)** — £50,271 – £125,140 at 40%  _(ITA 2007)_
- **Additional rate (rUK)** — Over £125,140 at 45%  _(ITA 2007)_
- **Starter rate (Scotland)** — £12,571 – £14,876 at 19%  _(Scotland Act 2016)_
- **Basic rate (Scotland)** — £14,877 – £26,561 at 20%  _(Scotland Act 2016)_
- **Intermediate rate (Scotland)** — £26,562 – £43,662 at 21%  _(Scotland Act 2016)_
- **Higher rate (Scotland)** — £43,663 – £75,000 at 42%  _(Scotland Act 2016)_
- **Advanced rate (Scotland)** — £75,001 – £125,140 at 45%  _(Scotland Act 2016)_
- **Top rate (Scotland)** — Over £125,140 at 48%  _(Scotland Act 2016)_
- **Personal allowance** — £12,570  _(ITA 2007)_
- **PA taper starts** — £100,000 adjusted net income  _(ITA 2007)_
- **PA fully withdrawn** — £125,140  _(ITA 2007)_
- **Basic rate band** — £37,700  _(ITA 2007)_
- **PSA (basic rate)** — £1,000  _(ITA 2007)_
- **PSA (higher rate)** — £500  _(ITA 2007)_
- **Dividend allowance** — £500  _(ITA 2007 s.13A)_
- **Marriage allowance transfer** — £1,260 (reducer £252)  _(ITA 2007)_
- **Pension annual allowance** — £60,000  _(Finance Act)_
- **Basic rate** — 8.75%  _(ITA 2007)_
- **Higher rate (£50,271--£125,140)** — 33.75%  _(https://www.gov.uk/government/publications/rates-and-allowances-income-tax/income-tax-rates-and-allowances-current-and-past)_
- **Additional rate** — 39.35%  _(ITA 2007)_
- **Online SA return deadline** — 31 January following tax year  _(TMA 1970)_
- **Paper SA return deadline** — 31 October following tax year  _(TMA 1970)_

## Section 1 -- Quick Reference

**Section 1 -- Quick Reference**

| Field | Value |
| --- | --- |
| Country | United Kingdom |
| Tax | Income Tax (rUK rates or Scottish rates) |
| Currency | GBP only |
| Tax years in scope | 2024-25 (prior), 2025-26 (current), 2026-27 (from 6 April 2026) |
| Primary legislation | Income Tax Act 2007 (ITA 2007); ITEPA 2003; ITTOIA 2005 |
| Supporting legislation | Finance Act 2024; Finance Act 2025; Finance (No. 2) Bill 2024-26 / Finance Bill 2026 (pending Royal Assent); Scotland Act 2016; TMA 1970 |
| Tax authority | HM Revenue & Customs (HMRC) |
| Filing portal | HMRC Self Assessment Online |
| Filing deadline (online) 2024-25 | 31 January 2026 |
| Filing deadline (online) 2025-26 | 31 January 2027 |
| Filing deadline (online) 2026-27 | 31 January 2028 |
| Contributor | Open Accountants Community |
| Validated by | Verified by James Power on 2026-06-03 |
| Skill version | 2.2 |

### 1.0 Three-Year Comparison -- Headline rUK Bands (FROZEN through 2027-28) [T1]

**1.0 Three-Year Comparison -- Headline rUK Bands (FROZEN through 2027-28) [T1]**

| Item | 2024-25 | 2025-26 | 2026-27 |
| --- | --- | --- | --- |
| Personal allowance | GBP 12,570 | GBP 12,570 | GBP 12,570 (frozen) |
| Basic rate band (20%) | up to GBP 50,270 | up to GBP 50,270 | up to GBP 50,270 (frozen) |
| Higher rate band (40%) | GBP 50,271 -- 125,140 | GBP 50,271 -- 125,140 | GBP 50,271 -- 125,140 (frozen) |
| Additional rate (45%) | over GBP 125,140 | over GBP 125,140 | over GBP 125,140 (frozen) |
| PA taper threshold | GBP 100,000 | GBP 100,000 | GBP 100,000 (frozen) |
| PA fully withdrawn at | GBP 125,140 | GBP 125,140 | GBP 125,140 (frozen) |

**Source:** Personal allowance and higher rate threshold freeze extended to 5 April 2028 (Finance (No. 2) Act 2023 s.5; Autumn Budget 2025 confirmed no further extension at this stage, but the freeze through 2027-28 remains in force).

### 1.1 Income Tax Bands -- England, Wales, Northern Ireland (rUK) -- 2024-25 [T1]

**1.1 Income Tax Bands -- England, Wales, Northern Ireland (rUK) -- 2024-25 [T1]**

| Band | Taxable Income | Rate |
| --- | --- | --- |
| Personal allowance | GBP 0 -- 12,570 | 0% |
| Basic rate | GBP 12,571 -- 50,270 | 20% |
| Higher rate | GBP 50,271 -- 125,140 | 40% |
| Additional rate | Over GBP 125,140 | 45% |

### 1.2 Income Tax Bands -- rUK -- 2025-26 [T1]

**1.2 Income Tax Bands -- rUK -- 2025-26 [T1]**

| Band | Taxable Income | Rate |
| --- | --- | --- |
| Personal allowance | GBP 0 -- 12,570 | 0% |
| Basic rate | GBP 12,571 -- 50,270 | 20% |
| Higher rate | GBP 50,271 -- 125,140 | 40% |
| Additional rate | Over GBP 125,140 | 45% |

### 1.3 Income Tax Bands -- rUK -- 2026-27 (from 6 April 2026) [T1]

**1.3 Income Tax Bands -- rUK -- 2026-27 (from 6 April 2026) [T1]**

| Band | Taxable Income | Rate |
| --- | --- | --- |
| Personal allowance | GBP 0 -- 12,570 | 0% |
| Basic rate | GBP 12,571 -- 50,270 | 20% |
| Higher rate | GBP 50,271 -- 125,140 | 40% |
| Additional rate | Over GBP 125,140 | 45% |

Headline rates and thresholds are **unchanged** from 2025-26 -- the freeze continues through 2027-28. Autumn Budget 2025 changes are confined to investment income (see Section 1.5).

### 1.4 Scottish Income Tax Bands [T1]

- **Scope of Scottish bands** — Scottish bands are set annually by the Scottish Parliament (Scotland Act 2016) and are independent of the rUK schedule. They apply ONLY to non-savings, non-dividend income. Savings and dividends always use UK-wide rates.  _(Scotland Act 2016)_

#### Scottish Bands 2024-25

**Scottish Bands 2024-25**

| Band | Taxable Income | Rate |
| --- | --- | --- |
| Personal allowance | GBP 0 -- 12,570 | 0% |
| Starter rate | GBP 12,571 -- 14,876 | 19% |
| Basic rate | GBP 14,877 -- 26,561 | 20% |
| Intermediate rate | GBP 26,562 -- 43,662 | 21% |
| Higher rate | GBP 43,663 -- 75,000 | 42% |
| Advanced rate | GBP 75,001 -- 125,140 | 45% |
| Top rate | Over GBP 125,140 | 48% |

#### Scottish Bands 2025-26

**Scottish Bands 2025-26**

| Band | Taxable Income | Rate |
| --- | --- | --- |
| Personal allowance | GBP 0 -- 12,570 | 0% |
| Starter rate | GBP 12,571 -- 15,397 | 19% |
| Basic rate | GBP 15,398 -- 27,491 | 20% |
| Intermediate rate | GBP 27,492 -- 43,662 | 21% |
| Higher rate | GBP 43,663 -- 75,000 | 42% |
| Advanced rate | GBP 75,001 -- 125,140 | 45% |
| Top rate | Over GBP 125,140 | 48% |

#### Scottish Bands 2026-27

Set at the Scottish Budget delivered on 13 January 2026. The six rates are
unchanged; the starter and basic band limits rose 7.4% and the higher, advanced
and top thresholds are frozen.

| Band | Income with the standard GBP 12,570 personal allowance | Rate |
| --- | --- | --- |
| Starter rate | GBP 12,571 -- 16,537 | 19% |
| Basic rate | GBP 16,538 -- 29,526 | 20% |
| Intermediate rate | GBP 29,527 -- 43,662 | 21% |
| Higher rate | GBP 43,663 -- 75,000 | 42% |
| Advanced rate | GBP 75,001 -- 125,140 | 45% |
| Top rate | Over GBP 125,140 | 48% |

The combination is worth stating because it is counter-intuitive: widening the
two lowest bands while freezing the higher-rate threshold **reduces** tax for a
Scottish taxpayer at GBP 50,000 by GBP 31.75 against 2025-26, even though no
rate fell. Section 4's worked example carries that through.

This block previously read "TBC -- Scottish Budget 2025-26 not yet enacted at
time of writing ... apply 2025-26 bands as a working estimate". The Budget was
delivered on 13 January 2026 and the placeholder outlived it, while the worked
example further down had already been updated to the real thresholds. Reference
table stale, example current -- the reverse of the usual direction, and a
reminder to fix both halves.  _(gov.scot, "Scottish Income Tax 2026 to 2027: technical factsheet"; Scottish Rate Resolution)_

### 1.5 Changes from April 2026 -- Autumn Budget 2025 [T1]

The Autumn Budget 2025 changes take effect in two stages. **Dividends** rise from **6 April 2026**; **savings and property income** rise from **6 April 2027**. Do not synchronise them:

**Autumn Budget 2025 Changes**

| Item | 2025-26 | 2026-27 |
| --- | --- | --- |
| Dividend ordinary rate | 8.75% | **10.75%** |
| Dividend upper rate | 33.75% | **35.75%** |
| Dividend additional rate | 39.35% | 39.35% (unchanged) |
| Savings income basic / higher / additional | 20% / 40% / 45% | **20% / 40% / 45% — unchanged for 2026-27.** The Autumn Budget 2025 rates of **22% / 42% / 47%** apply **from April 2027**, a year after the dividend change above |
| Property income basic / higher / additional | 20% / 40% / 45% | **20% / 40% / 45% — unchanged for 2026-27.** The Autumn Budget 2025 rates of **22% / 42% / 47%** apply **from April 2027**. Note the additional rate goes to 47%, not 45% as an earlier draft of this table had it |
| All other headline bands and PA | frozen | frozen (no change) |
| HICBC tapered threshold | GBP 60,000 / GBP 80,000 | GBP 60,000 / GBP 80,000 (unchanged from 2024-25 reform) |

- **Dividend rates** -- confirmed 2pp uplift on ordinary and upper rates from 6 April 2026. See companion skill `uk-dividends` for the detailed dividend computation, the GBP 500 allowance interaction, and worked examples.
- **Savings income and property income** -- the Autumn Budget 2025 rates are **22% / 42% / 47%**, and they apply **from 6 April 2027**, a year after the dividend change. They are specific, not "expected", and the additional rate does move (to 47%). For **2026-27** savings and property income is taxed at the ordinary **20% / 40% / 45%**: compute it, do not hold it open. Applying 22/42/47 to a 2026-27 return overstates the liability at every band.
- **HICBC** -- the GBP 60,000 starting / GBP 80,000 full claw-back tapered threshold introduced from 2024-25 remains in force for 2026-27 (no further reform announced).
- **All other bands frozen** -- Personal Allowance (GBP 12,570), basic rate threshold (GBP 50,270), additional rate threshold (GBP 125,140), and PA taper threshold (GBP 100,000) are all frozen through 2027-28.

### Key Allowances and Thresholds [T1]

**Key Allowances and Thresholds [T1]**

| Item | 2024-25 | 2025-26 | 2026-27 |
| --- | --- | --- | --- |
| Personal allowance | GBP 12,570 | GBP 12,570 | GBP 12,570 |
| PA taper threshold | GBP 100,000 | GBP 100,000 | GBP 100,000 |
| PA fully withdrawn | GBP 125,140 | GBP 125,140 | GBP 125,140 |
| Basic rate band | GBP 37,700 | GBP 37,700 | GBP 37,700 |
| Personal savings allowance (basic rate) | GBP 1,000 | GBP 1,000 | GBP 1,000 |
| Personal savings allowance (higher rate) | GBP 500 | GBP 500 | GBP 500 |
| Personal savings allowance (additional rate) | GBP 0 | GBP 0 | GBP 0 |
| Starting rate for savings band | GBP 5,000 | GBP 5,000 | GBP 5,000 |
| Dividend allowance | GBP 500 | GBP 500 | GBP 500 |
| Marriage allowance transfer | GBP 1,260 (reducer GBP 252) | GBP 1,260 (reducer GBP 252) | GBP 1,260 (reducer GBP 252) |
| Annual pension allowance | GBP 60,000 | GBP 60,000 | GBP 60,000 |
| HICBC tapered threshold (start / full claw-back) | GBP 60,000 / 80,000 | GBP 60,000 / 80,000 | GBP 60,000 / 80,000 |

### Dividend Rates [T1]

**Dividend Rates [T1]**

| Band | 2024-25 | 2025-26 | 2026-27 |
| --- | --- | --- | --- |
| Within basic rate band | 8.75% | 8.75% | **10.75%** |
| Within higher rate band | 33.75% | 33.75% | **35.75%** |
| Within additional rate band | 39.35% | 39.35% | 39.35% |

See companion skill `uk-dividends` for full dividend-specific guidance, including the GBP 500 allowance, scrip dividends, and overseas dividend treatment.

### Conservative Defaults [T1]

**Conservative Defaults [T1]**

| Ambiguity | Default |
| --- | --- |
| Unknown tax year | Current year (2025-26) |
| Unknown residency | UK resident (but STOP if genuinely unclear) |
| Unknown Scottish status | rUK rates |
| Unknown income category | Non-savings income |
| Unknown pension contribution method | Relief at source |
| Unknown marriage allowance eligibility | Do not apply |
| 2026-27 savings/property rate | 20% / 40% / 45% -- unchanged. The 22/42/47 rates begin in 2027-28 |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

- **Minimum viable** — P60 (employment income), self-employment profit from SA103, and confirmation of residency status and Scottish taxpayer status.
- **Recommended** — P11D (benefits in kind), bank interest certificates, dividend vouchers, pension contribution statements, Gift Aid records, prior year SA302 (tax calculation).
- **Ideal** — all supplementary pages (SA103, SA105, SA106), complete records of all income sources, prior year payments on account made.

### Refusal Catalogue

- **R-UK-IT-1** — Non-resident and split-year cases have different rules and may involve the remittance basis. Out of scope. Escalate. (Non-resident or split-year treatment)
- **R-UK-IT-2** — The remittance basis for non-doms requires specialist advice. Out of scope. (Note: the remittance basis is abolished from 6 April 2025 and replaced by a residence-based regime -- escalate any post-April-2025 non-dom queries.) (Non-domiciled individuals)
- **R-UK-IT-3** — Income from trusts (SA107) has specific rules. Out of scope. (Trust income)
- **R-UK-IT-4** — Tapered annual allowance, money purchase annual allowance, and carry-forward calculations beyond basic require specialist review. Escalate. (Complex pension annual allowance)
- **R-UK-IT-5** — Capital gains are computed separately on SA108. This skill covers income tax only. (Capital gains)
- **R-UK-IT-6** — Savings and property income for **2027-28 onward**, where the return spans the 22 / 42 / 47 rates that begin 6 April 2027 and their interaction with the residential finance-cost reducer, which rises to the property basic rate of 22% from 2027–28. Flag for reviewer. A **2026-27** return needs no such flag: those rates are unchanged at 20 / 40 / 45.

## Section 3 -- Transaction Pattern Library

For SA100, the "transactions" are not bank statement lines but rather income items from various sources flowing into the tax computation. This pattern library maps income types to the correct SA100 section and tax treatment.

### 3.1 Employment Income Patterns

**3.1 Employment Income Patterns**

| Source Document | SA100 Section | Treatment | Notes |
| --- | --- | --- | --- |
| P60 (annual certificate) | TR3 (Employment) | Gross pay before PAYE deducted | PAYE tax goes to "tax deducted" |
| P45 (leaver certificate) | TR3 | Gross pay for period employed | May need to combine with P60 from new employer |
| P11D (benefits in kind) | TR3 | Add to employment income | Car benefit, medical insurance, etc. |
| Tips, bonuses (not on P60) | TR3 | Add to employment income | Must be declared even if not on P60 |
| Redundancy payment | TR3 | First GBP 30,000 exempt. Excess taxable. | [T2] Confirm composition of payment |
| Employer pension contribution | EXCLUDE | Not taxable income to employee | Employer contribution does not appear on SA100 |

### 3.2 Self-Employment Income Patterns

**3.2 Self-Employment Income Patterns**

| Source | SA100 Section | Treatment | Notes |
| --- | --- | --- | --- |
| SA103 taxable trading profit | TR4 (Self-employment) | Attach SA103 | Computed per uk-self-employment-sa103 skill |
| Multiple self-employments | TR4 | Separate SA103 for each trade | Combined for Class 4 NIC |

### 3.3 Savings Income Patterns

**3.3 Savings Income Patterns**

| Source | SA100 Section | Treatment | Notes |
| --- | --- | --- | --- |
| Bank interest (UK) | TR5 (Savings) | Gross amount | Most banks pay interest gross since 2016 |
| Building society interest | TR5 | Gross amount | Same |
| Government bond interest (gilts) | TR5 | Gross amount | Savings income |
| NS&I interest (non-ISA) | TR5 | Gross amount | Premium Bond prizes are tax-free |
| ISA interest | EXCLUDE | Tax-free | Do not include |
| P2P lending interest | TR5 | Gross amount | Savings income |

### 3.4 Dividend Income Patterns

**3.4 Dividend Income Patterns**

| Source | SA100 Section | Treatment | Notes |
| --- | --- | --- | --- |
| UK company dividends | TR6 (Dividends) | Gross dividend | No tax credit since 2016 |
| Overseas dividends | TR6 or SA106 | Gross amount in GBP | May have foreign tax credit |
| Investment fund dividends | TR6 | As per tax voucher | Some funds pay interest distributions |
| Scrip dividends | TR6 | Cash equivalent | Taxable as dividend |

### 3.5 Pension Income Patterns

**3.5 Pension Income Patterns**

| Source | SA100 Section | Treatment | Notes |
| --- | --- | --- | --- |
| State pension | TR5 (Pensions) | Full amount taxable | No tax deducted at source |
| Private/occupational pension | TR5 | Gross amount | PAYE usually deducted |
| Pension lump sum (25% tax-free) | Partly TR5 | Only 75% taxable | First 25% is tax-free |
| Drawdown income | TR5 | Full amount taxable | No tax-free element (25% already taken) |

### 3.6 Pension Contribution Patterns (Deductions)

**3.6 Pension Contribution Patterns (Deductions)**

| Source | Treatment | Notes |
| --- | --- | --- |
| Personal pension (relief at source) | Gross up: contribution x 100/80. Extends basic rate band. Higher/additional relief via SA100. | Net contribution already includes 20% basic rate relief claimed by pension provider. |
| Workplace pension (net pay) | Already deducted from gross pay. No further claim. | Already reflected in P60 gross figure. |
| SIPP contribution | Same as relief at source | Gross up for higher rate relief. |

### 3.7 Other Income Patterns

**3.7 Other Income Patterns**

| Source | SA100 Section | Treatment | Notes |
| --- | --- | --- | --- |
| Rental income (net) | TR6 (Property) | Attach SA105 | Separate computation |
| Foreign income | SA106 | Separate computation | May involve double tax relief |
| Miscellaneous income | SA101 | Various | Catch-all |

## Section 4 -- Worked Examples

Each scenario is repeated across all three years so reviewers can see the year-on-year effect of the rate freeze and the April 2026 changes.

### Example 1 -- Basic Rate Taxpayer (Employment Only)

- **Basic rate taxpayer computation** — Input: Employment GBP 35,000. PAYE deducted GBP 4,486. No other income. Computation (identical for 2024-25, 2025-26, and 2026-27 -- bands frozen): Personal allowance: GBP 12,570. Taxable income: 35,000 - 12,570 = GBP 22,430. Tax: 22,430 x 20% = GBP 4,486. Less PAYE: GBP 4,486. Balance: GBP 0. Note: Because no investment income is involved and headline bands are frozen, the computation is identical across all three years.

### Example 2 -- Employment + Self-Employment + Dividends

Input: Employment GBP 40,000 (PAYE GBP 5,486). Self-employment profit GBP 20,000. Dividends GBP 5,000.

#### 2024-25 computation

- **2024-25 computation** — Total income: GBP 65,000. Personal allowance: GBP 12,570. Taxable: GBP 52,430. Non-savings (GBP 60,000 - 12,570 = GBP 47,430): 37,700 x 20% = GBP 7,540. Remaining 9,730 x 40% = GBP 3,892. Dividends (GBP 5,000 -- all in higher rate band): 500 at 0% (dividend allowance) + 4,500 x 33.75% = GBP 1,518.75. Total tax: 7,540 + 3,892 + 1,518.75 = GBP 12,950.75. Less PAYE: GBP 5,486. Balance via SA: GBP 7,464.75

#### 2025-26 computation

- **2025-26 computation** — Identical to 2024-25 (no rate or threshold changes). Total tax GBP 12,950.75.

#### 2026-27 computation

- **2026-27 computation** — Non-savings tax unchanged: 7,540 + 3,892 = GBP 11,432. Dividends at new rates: 500 at 0% + 4,500 x 35.75% = GBP 1,608.75. Total tax: 11,432 + 1,608.75 = GBP 13,040.75. Increase vs 2025-26: GBP 90.00 (entirely from the 2pp dividend uplift on the GBP 4,500 chargeable above the allowance). (Class 4 NIC on self-employment is computed in the SA103 skill -- see uk-self-employment-sa103.)

### Example 3 -- Personal Allowance Taper

- **PA taper example** — Input: Total income GBP 115,000. GBP 10,000 gross pension contribution (relief at source). Computation (identical for 2024-25, 2025-26, and 2026-27 -- PA taper threshold frozen at GBP 100,000): Adjusted net income: 115,000 - 10,000 = GBP 105,000. PA reduction: (105,000 - 100,000) / 2 = GBP 2,500. Personal allowance: 12,570 - 2,500 = GBP 10,070. Basic rate band extended by pension: 37,700 + 10,000 = GBP 47,700. Higher rate threshold: 10,070 + 47,700 = GBP 57,770

### Example 4 -- Scottish Taxpayer with Savings

Input: Scottish taxpayer. Employment GBP 50,000. Bank interest GBP 3,000.

#### 2024-25 computation

- **2024-25 computation** — Non-savings (Scottish 2024-25 rates): 50,000 - 12,570 = GBP 37,430 taxable. Starter (2,306): 19% = GBP 438.14. Basic (11,685): 20% = GBP 2,337.00. Intermediate (17,101 -- up to 43,662-12,570=31,092): 21% = GBP 3,591.21. Higher (37,430 - 31,092 = 6,338): 42% = GBP 2,661.96. Savings (UK rates): GBP 3,000 -- taxpayer is higher rate. PSA: GBP 500 at 0%. Remaining: GBP 2,500 at 40% = GBP 1,000. Total: 9,028.31 + 1,000 = GBP 10,028.31

#### 2025-26 computation

- **2025-26 computation** — Non-savings (Scottish 2025-26 rates -- starter and basic bands slightly wider): 50,000 - 12,570 = GBP 37,430 taxable. Starter (2,827): 19% = GBP 537.13. Basic (12,094): 20% = GBP 2,418.80. Intermediate (16,171 -- up to 43,662-12,570=31,092): 21% = GBP 3,395.91. Higher (37,430 - 31,092 = 6,338): 42% = GBP 2,661.96. Savings (UK rates): GBP 3,000 -- taxpayer is higher rate. PSA: GBP 500 at 0%. Remaining: GBP 2,500 at 40% = GBP 1,000. Total: 9,013.80 + 1,000 = GBP 10,013.80

#### 2026-27 computation

- **2026-27 computation** — Non-savings (Scottish 2026-27 rates, set at the Scottish Budget: starter band to GBP 16,537, basic to GBP 29,526, intermediate to GBP 43,662 frozen): 50,000 - 12,570 = GBP 37,430 taxable. Starter (3,967): 19% = GBP 753.73. Basic (12,989): 20% = GBP 2,597.80. Intermediate (14,136 -- up to 43,662-12,570=31,092): 21% = GBP 2,968.56. Higher (37,430 - 31,092 = 6,338): 42% = GBP 2,661.96. Non-savings subtotal GBP 8,982.05, which is GBP 31.75 *less* than 2025-26 because the starter and basic bands widened 7.4% while the higher-rate threshold stayed frozen. Savings (UK rates): GBP 3,000 -- taxpayer is higher rate. PSA: GBP 500 at 0%. Remaining: GBP 2,500 at **40%** = GBP 1,000. Total: 8,982.05 + 1,000 = GBP 9,982.05

> **Why the savings slice is 40% and not 42%.** The Autumn Budget 2025 raised
> the savings rates by two percentage points to 22% / 42% / 47%, and Finance Act
> 2026 s.5 commences that **from 6 April 2027** — the 2027-28 tax year, not
> 2026-27. In 2026-27 savings income is still taxed at the ordinary 20/40/45.
> The 42% appearing twice in this example is a coincidence and a trap: the
> Scottish higher rate is 42% on **non-savings** income by residence, and
> Scottish rates never apply to savings at all (see the prohibitions). Reading
> the announced savings uplift a year early is the error to avoid, and it
> overstates this return by GBP 50. `uk-rental-sa105` carries the same warning
> for property income, which commences on the same date under s.7.

### Example 5 -- Marriage Allowance

- **Marriage allowance example** — Input: Spouse A income GBP 10,000. Spouse B income GBP 28,000 (basic rate). Election made. Computation (identical for 2024-25, 2025-26, and 2026-27 -- marriage allowance frozen at GBP 1,260 / reducer GBP 252): Spouse A: PA reduced to GBP 11,310. Income GBP 10,000 < GBP 11,310. Tax = GBP 0. Spouse B: Tax = (28,000 - 12,570) x 20% = GBP 3,086. Less marriage allowance reducer GBP 252. Tax = GBP 2,834.

### Example 6 -- HICBC (2024-25 reform onwards, applies in 2025-26 and 2026-27)

- **HICBC example** — Input: Higher earner adjusted net income GBP 70,000. Child benefit received GBP 2,212.60 (one child, full year). Computation (identical for 2024-25, 2025-26, and 2026-27 -- HICBC threshold frozen at GBP 60,000 / GBP 80,000): ANI in taper zone: GBP 70,000 (between GBP 60,000 and GBP 80,000). Excess over GBP 60,000: GBP 10,000. Charge percentage: 10,000 / 200 = 50%. HICBC: 2,212.60 x 50% = GBP 1,106.30. Added to tax due via SA100

### 5.1 Income Ordering [T1]

- **Income ordering** — Mandatory order: (1) Non-savings income fills bands first. (2) Savings income next. (3) Dividends on top. This ordering is required by law and affects which rates apply. The ordering rule is unchanged in 2026-27, and so are the savings rates: **only the dividend rates change in 2026-27**. Savings and property rates change a year later, in 2027-28.  _(ITA 2007, ss 6-22; Finance Act 2026 ss 4, 5, 7)_

### 5.2 Personal Allowance [T1]

- **Personal allowance** — GBP 12,570 across all three years (2024-25, 2025-26, 2026-27 -- frozen through 2027-28). Tapers at GBP 1 for every GBP 2 above GBP 100,000 adjusted net income. Fully withdrawn at GBP 125,140. Effective 60% marginal rate in taper zone. Adjusted net income = Total income - gross pension contributions - grossed-up Gift Aid.  _(ITA 2007, s35)_

### 5.3 Savings Allowance and Starting Rate [T1]

- **Personal savings allowance and starting rate for savings** — Personal savings allowance: GBP 1,000 (basic rate), GBP 500 (higher rate), GBP 0 (additional rate). Starting rate for savings: GBP 5,000 at 0%, reduced by GBP 1 for each GBP 1 of non-savings income above PA. **2026-27: unchanged — savings income above the allowance is taxed at the ordinary 20% / 40% / 45%.** The announced 2pp uplift to 22% / 42% / 47% is enacted by Finance Act 2026 s.5 but commences **6 April 2027**, so it applies from 2027-28 and not before. The starting rate limit stays at GBP 5,000 for 2026-27 through 2030-31 under the same Act. Applying 22/42/47 to a 2026-27 return overstates the liability at every band.  _(ITA 2007, ss 12A-12B; Finance Act 2026 s.5)_

### 5.4 Dividend Allowance [T1]

- **Dividend allowance and dividend rates** — GBP 500 at 0% rate (unchanged across all three years). Uses up the basic rate band -- it is NOT a deduction from income. Dividend rates above the allowance: 2024-25 and 2025-26: 8.75% / 33.75% / 39.35%. 2026-27: 10.75% / 35.75% / 39.35%. See uk-dividends for the full dividend treatment.  _(ITTOIA 2005, s13A)_

### 5.5 Marriage Allowance [T1]

- **Marriage allowance** — Transfer GBP 1,260 from spouse with income below PA to basic-rate spouse. Reducer = GBP 252 (always at 20%, even for Scottish taxpayers). Recipient must NOT be higher/additional rate. Unchanged across all three years.  _(ITA 2007, s55B)_

### 5.6 Basic Rate Band Extension [T1]

- **Basic rate band extension** — Extended by: gross pension contributions (relief at source) + grossed-up Gift Aid donations. Example: GBP 4,000 gross pension = basic rate band becomes GBP 41,700. Unchanged across all three years.  _(ITA 2007, s10)_

### 5.7 Payments on Account [T1]

- **Payments on account** — Required if prior year SA liability > GBP 1,000 AND less than 80% deducted at source. POA1: 31 January (50% of prior year). POA2: 31 July (50%). Balance: 31 January following year. Mechanism unchanged across all three years.  _(TMA 1970, ss 59A-59B)_

### 5.8 Filing and Penalties [T1]

- **Filing deadlines and penalties** — Online deadlines: 2024-25 return: 31 January 2026; 2025-26 return: 31 January 2027; 2026-27 return: 31 January 2028. Late filing: GBP 100 immediate, then GBP 10/day after 3 months, then 5% of tax at 6 and 12 months. Late payment: 5% at 30 days, 6 months, 12 months.  _(TMA 1970, ss 8-12, 93, 97)_

### 5.9 High Income Child Benefit Charge (HICBC) [T1]

- **HICBC rule** — Applies from 2024-25 onwards with a tapered range of GBP 60,000 to GBP 80,000 adjusted net income (reform enacted by Finance Act 2024). Charge = 1% of child benefit for every GBP 200 of income between GBP 60,000 and GBP 80,000. At GBP 80,000+: 100% claw-back. Thresholds unchanged in 2025-26 and 2026-27.  _(ITEPA 2003, ss 681B-681H (as amended by FA 2024))_

### 6.1 Personal Allowance Taper Planning [T2]

Pension contributions and Gift Aid can reduce adjusted net income below GBP 100,000 to restore the PA. Legitimate planning strategy. Flag for reviewer to confirm contribution amounts are within annual allowance.

### 6.2 High Income Child Benefit Charge -- Cross-Year Planning [T2]

For taxpayers in the GBP 60,000-80,000 taper zone, the effective marginal rate including HICBC can exceed 60%. Cross-year planning (timing of bonus income, pension contributions to reduce ANI) is materially valuable. Flag for reviewer.

### 6.3 Reducing Payments on Account [T2]

Client can apply (SA303) to reduce POAs if they expect lower liability. If estimate is too low, HMRC charges interest from original due date. Flag before reducing. For the 2025-26 -> 2026-27 transition, POAs for 2026-27 will be based on 2025-26 liability -- consider whether the 2026-27 dividend/savings rate increases will materially raise the actual liability above POA estimates.

### 6.4 Pension Annual Allowance [T2]

- **Pension annual allowance** — GBP 60,000 standard. Tapers to GBP 10,000 for adjusted income over GBP 260,000. 3-year carry forward of unused allowance available. Excess triggers annual allowance charge at marginal rate. Flag for specialist review if near limits.  _(FA 2004, ss 188-195)_

### 6.5 Multiple Income Sources Band Allocation [T2]

When savings and dividends push income across rate band boundaries, the interaction of PSA, dividend allowance, and band extensions can be complex. Flag for reviewer to verify computation. Especially important for 2026-27 given the divergence of dividend, savings, and non-savings rates.

### 6.6 2026-27 Savings and Property Income Rate Confirmation [T2]

The Autumn Budget 2025 rates for savings and property income are **22% / 42% / 47%** and they apply **from 6 April 2027**, not 6 April 2026 — a year after the dividend change. For **2026-27** both streams stay at the ordinary **20% / 40% / 45%**, so a 2026-27 return can be finalised: there is nothing to hold open. Note the additional rate does move, to 47%. The residential finance-cost reducer remains 20% through 2026–27 and rises to the property basic rate of 22% from 2027–28. See [Finance Act 2026 sections 6(8) and 7, Schedule 1 paragraph 40](https://www.legislation.gov.uk/ukpga/2026/11/pdfs/ukpga_20260011_en.pdf).

## Section 7 -- Excel Working Paper Template

SA100 TAX COMPUTATION -- Tax Year [SELECT: 2024-25 / 2025-26 / 2026-27]

A. INCOME
  A1. Employment income (P60 gross)                ___________
  A2. Benefits in kind (P11D)                      ___________
  A3. Self-employment profit (from SA103)          ___________
  A4. Savings income (bank interest)               ___________
  A5. Dividend income                              ___________
  A6. Pension income                               ___________
  A7. Property income (from SA105)                 ___________
  A8. Other income                                 ___________
  A9. TOTAL INCOME                                 ___________

B. DEDUCTIONS FROM TOTAL INCOME
  B1. Trading losses (sideways relief)             ___________
  B2. Gross pension contributions (for ANI)        ___________
  B3. Gift Aid (grossed up, for ANI)               ___________
  B4. Adjusted net income                          ___________

C. PERSONAL ALLOWANCE
  C1. Standard PA                                  12,570
  C2. Taper reduction (if ANI > 100,000)           ___________
  C3. Available PA                                 ___________

D. TAXABLE INCOME
  D1. Non-savings taxable                          ___________
  D2. Savings taxable                              ___________
  D3. Dividend taxable                             ___________
  D4. Total taxable                                ___________

E. TAX COMPUTATION
  E1. Tax on non-savings (rUK or Scottish)         ___________
  E2. Tax on savings (with PSA + starting rate)    ___________
       Rates: 2024-25 & 2025-26 = 20/40/45
              2026-27 = TBC (expected 22/42/45)    [FLAG]
  E3. Tax on dividends (with allowance)            ___________
       Rates: 2024-25 & 2025-26 = 8.75/33.75/39.35
              2026-27 = 10.75/35.75/39.35
  E4. Total income tax                             ___________
  E5. Less: tax reducers (MA, EIS, etc.)           ___________
  E6. Income tax charged                           ___________
  E7. Plus: HICBC (if ANI > 60,000)                ___________
  E8. Less: PAYE deducted                          ___________
  E9. Less: tax on savings at source                ___________
  E10. Less: payments on account                    ___________
  E11. TAX DUE / (REFUND)                          ___________

F. CLASS 4 NIC (from SA103)                        ___________

G. TOTAL DUE (E11 + F)                             ___________

REVIEWER FLAGS:
  [ ] Tax year selected and applied consistently?
  [ ] Scottish or rUK rates confirmed?
  [ ] PA taper checked?
  [ ] Income ordering correct (non-savings > savings > dividends)?
  [ ] Marriage allowance eligibility verified?
  [ ] HICBC computed if ANI > 60,000?
  [ ] For 2026-27: dividend rates updated to 10.75/35.75/39.35?
  [ ] For 2026-27: savings/property rates confirmed against enacted Finance Bill 2026?
  [ ] All T2 items flagged?

## Section 8 -- Bank Statement Reading Guide

**Bank statement reading guide**

| Item | What to Look For |
| --- | --- |
| Undeclared bank interest | INTEREST PAID lines on personal account |
| Dividends received | DIVIDEND lines, share platform payouts |
| Rental income | Regular credits from tenants |
| Pension income | Monthly credits from pension providers |
| Gift Aid payments | Debits to charities |
| Pension contributions | Debits to SIPP providers |
| Student loan repayments | SLC deductions (informational only -- collected via PAYE) |

## Section 8 -- Bank Statement Reading Guide

SA100 is primarily compiled from official documents (P60, P11D, interest certificates, dividend vouchers) rather than raw bank statements. However, bank statements may be needed to identify:

## Section 9 -- Onboarding Fallback

If the client cannot provide all documents immediately:

1. Confirm which tax year(s) the engagement covers (2024-25, 2025-26, and/or 2026-27)
2. Start with P60 and any SA103 computation
3. Ask for bank statements to identify savings interest and dividends
4. Apply conservative defaults
5. Generate working paper with flags
6. Present questions:

```
ONBOARDING QUESTIONS -- UK INCOME TAX (SA100)
0. Which tax year? (2024-25 prior / 2025-26 current / 2026-27 from April 2026)
1. Are you a Scottish taxpayer? (main residence in Scotland)
2. Employment income -- do you have your P60 and P11D?
3. Self-employment -- have you completed your SA103?
4. Bank interest received in the year?
5. Dividends received in the year?
6. Pension income (state and/or private)?
7. Rental income?
8. Pension contributions made (personal, not workplace)?
9. Gift Aid donations made?
10. Married/civil partner -- is marriage allowance being claimed?
11. Payments on account already made for the year?
12. PAYE tax deducted (from P60)?
13. Child benefit received? (HICBC if ANI > GBP 60,000)
```

### Key Legislation

**Key Legislation table**

| Topic | Reference |
| --- | --- |
| Income categorisation | ITA 2007, ss 6-22 |
| Personal allowance | ITA 2007, s35 |
| PA taper | ITA 2007, s35(4) |
| Basic rate band | ITA 2007, s10 |
| Savings allowance | ITA 2007, ss 12A-12B |
| Dividend allowance | ITTOIA 2005, s13A |
| Dividend rates, 2026-27 onwards (10.75% / 35.75% / 39.35%) | Finance Act 2026, s.4 — Royal Assent 18 March 2026, in force from 6 April 2026 |
| Savings rates, **2027-28** onwards (22% / 42% / 47%) | Finance Act 2026, s.5 — enacted, but commencing 6 April 2027. Not a 2026-27 change |
| Separate property income rates, **2027-28** onwards (22% / 42% / 47%) | Finance Act 2026, ss.6-7 — enacted, commencing 6 April 2027. See uk-rental-sa105 |
| Threshold freeze through 2027-28 | Finance (No. 2) Act 2023, s.5 |
| Marriage allowance | ITA 2007, s55B |
| Scottish rates | Scotland Act 2016 |
| Pension relief | FA 2004, ss 188-195 |
| Gift Aid | ITA 2007, s414 |
| HICBC | ITEPA 2003, ss 681B-681H (as amended by FA 2024) |
| Payments on account | TMA 1970, ss 59A-59B |
| Filing/penalties | TMA 1970, ss 8-12, 93, 97 |

## Section 10 -- Reference Material

## PROHIBITIONS

- **Prohibitions list** — NEVER compute tax without first confirming the tax year (2024-25, 2025-26, or 2026-27) NEVER apply 2025-26 dividend rates to a 2026-27 computation (the ordinary and upper rates change to 10.75% and 35.75%) NEVER apply the 22% / 42% / 47% savings or property rates to a 2026-27 return -- Finance Act 2026 commences both from 6 April 2027, so 2026-27 savings and property income is still taxed at 20% / 40% / 45% NEVER compute tax without categorising income as non-savings, savings, or dividends NEVER apply Scottish rates to savings or dividend income NEVER apply marriage allowance if recipient is higher/additional rate NEVER ignore PA taper for adjusted net income above GBP 100,000 NEVER apply PSA to additional rate taxpayers (it is GBP 0) NEVER treat dividend allowance as a deduction -- it is a 0% rate band NEVER apply starting rate for savings if non-savings income exceeds GBP 17,570 NEVER compute POAs based on current year -- always prior year SA liability NEVER advise on non-domiciled or remittance basis -- escalate NEVER present tax calculations as definitive -- always label as estimated

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The 2026-27 figures in this skill are as enacted. The Finance Bill following the Autumn Budget of 26 November 2025 received Royal Assent on 18 March 2026 as **Finance Act 2026 (c. 11)**, and the figures here have been reconciled to it. Read the commencement dates rather than the announcement: the dividend uplift runs from 6 April 2026 (s.4), while the savings and property uplifts run from 6 April 2027 (ss.5, 7) and do not touch a 2026-27 return. Scottish rates and bands for 2026-27 are as set at the Scottish Budget.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — no liability on either side until you and the accountant sign
a formal engagement letter — book a free 30-minute call:

→ [Book a call](https://calendly.com/openaccountants-info/30min)

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).

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
