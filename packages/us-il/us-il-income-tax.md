---
name: us-il-income-tax
description: "Illinois Individual Income Tax Return (Form IL-1040) for sole proprietors and single-member LLCs. Covers the flat 4.95% rate, Illinois base income computation from federal AGI, Schedule M addition and subtraction modifications, property tax credit (Schedule ICR), earned income credit, and the full return assembly. Primary source: 35 ILCS 5/."
version: 1.0
jurisdiction: US-IL
tax_year: 2025
last_updated: 2026-09-29
reviewed_by: A licensed accountant (name withheld at their request)
review_status: current
depends_on:
  - us-tax-workflow-base
category: state
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# IL Income Tax

## Illinois IL-1040 Individual Return v1.0

> **Accountant-reviewed.** Rates and thresholds reviewed against the cited authorities by **a licensed accountant (name withheld at their request)** on 2026-06-03; the sign-off is recorded in the frontmatter (`reviewed_by`) and on the roster in `PARTNERS.md`. The verified figures are stated in the sections below with their sources (the separate "Verified rates & thresholds" list that carried them was folded into the body on 2026-09-29). Items the review flagged for clarification are excluded from that sign-off and remain marked in the text.

## What this file is

**Obligation category:** IT (Income Tax)
**Functional role:** Return assembly
**Status:** Complete

This is a Tier 2 content skill for preparing the Illinois Form IL-1040 for a full-year Illinois resident who is a sole proprietor or single-member LLC owner. Illinois imposes a flat 4.95% income tax rate, starting from federal adjusted gross income (AGI) and applying Illinois-specific modifications.

## Section 1 -- Scope statement

**In scope:**

- Form IL-1040 (Individual Income Tax Return)
- Schedule M (Other Additions and Subtractions)
- Schedule ICR (Illinois Credits, including property tax credit and K-12 education expense credit)
- Schedule IL-E/EIC (Illinois Earned Income Credit)
- Full-year Illinois residents
- Filing status: single, MFJ, MFS, head of household, qualifying surviving spouse
- Self-employment income from Schedule C flowing through federal AGI

**Out of scope (refused):**

- Part-year and non-resident returns (Schedule NR)
- Business income apportionment for multi-state operations
- Partnership and S-corp pass-through (Schedule K-1-P)
- Illinois estate/trust income tax (Form IL-1041)
- Amended returns (Form IL-1040-X)
- Net loss carryforward computations beyond simple tracking
- Illinois corporate income tax (Form IL-1120)

## Section 2 -- Filing requirements

### Who must file

- **Filing requirement** — An Illinois resident must file Form IL-1040 if: 1. They are required to file a federal income tax return, OR 2. They want to claim a refund of Illinois income tax withheld, OR 3. They have Illinois base income exceeding the personal exemption amount.  _(35 ILCS 5/502(a).)_

### Due date

**Due date table**  _(35 ILCS 5/505)_

| Item | Date | Source |
| --- | --- | --- |
| Filing deadline | April 15, 2026 (for tax year 2025) | 35 ILCS 5/505 |
| Extension deadline | October 15, 2026 (automatic 6-month extension for every filer; no Illinois form) | 35 ILCS 5/505(b); 2025 IL-1040 instr. |

- **Automatic extension detail** — Illinois grants an automatic 6-month extension to every filer, whether or not a federal extension was requested, and there is no Illinois extension form to file. A federal extension matters only when more than 6 months is needed. The extension is to file, not to pay: tax must be paid by April 15 (Form IL-505-I carries an extension payment), and estimated tax payments remain due on their dates.  _(35 ILCS 5/505(b); 2025 IL-1040 instr., "When is my return due / Automatic extension")_

## Section 3 -- Rates and thresholds

**Rates and thresholds table**  _(see rows)_

| Item | Amount | Source |
| --- | --- | --- |
| Illinois flat income tax rate | 4.95% | 35 ILCS 5/201(b)(5.4) |
| Personal exemption -- single (2025) | $2,850 | 35 ILCS 5/204; IDOR Informational Bulletin FY 2025-16; 2025 IL-1040 instr. |
| Personal exemption -- MFJ (2025) | $5,700 (2 x $2,850) | IDOR FY 2025-16 |
| Personal exemption -- each dependent (2025) | $2,850 | IDOR FY 2025-16 |
| Additional exemption -- age 65+ or legally blind | $1,000 per qualifying condition (taxpayer and spouse each) | 35 ILCS 5/204; IL-1040 instr. |
| Exemption phase-out (cliff, not a taper) | Exemptions fully disallowed when federal AGI exceeds $250,000 (single, HoH, MFS) or $500,000 (MFJ) | 35 ILCS 5/204(d); IL-1040 instr. |
| Property tax credit rate | 5% of property taxes paid on principal residence (nonrefundable) | 35 ILCS 5/208 |
| Property tax credit -- AGI cap | Disallowed when federal AGI exceeds $250,000 (single, HoH, MFS) or $500,000 (MFJ) | 35 ILCS 5/208; Schedule ICR instr. |
| Earned income credit | 20% of federal EIC (refundable); not subject to the AGI cliff | 35 ILCS 5/212 (2025) |
| K-12 education expense credit | 25% of qualified expenses over $250, max credit $750 (nonrefundable); disallowed above the same $250,000 / $500,000 AGI cap | 35 ILCS 5/201(m); Schedule ICR instr. |

- **Note on personal exemption** — Illinois does NOT have a standard deduction or itemized deductions at the state level. The personal exemption is the only below-the-line deduction.  _(35 ILCS 5/204; 86 Ill. Admin. Code 100.2410)_
- **The 2025 exemption is $2,850.** The amount is indexed annually; $2,775 was the 2024 amount and $2,625 an older one. The same $2,850 applies to the IL-1040, to estimated tax (IL-1040-ES) and to withholding (Booklet IL-700-T).  _(IDOR FY 2025-16)_

## Section 4 -- Computation rules (Step format)

### Step 1: Start with federal AGI (Line 1)

- **Federal AGI starting point** — Enter federal adjusted gross income from federal Form 1040, Line 11. This is the starting point for Illinois.  _(35 ILCS 5/203(a))_

### Step 2: Add Illinois addition modifications (Line 3, Schedule M)

Common additions for self-employed individuals:

**Addition modifications table**  _(see rows)_

| Addition | Description | Source |
| --- | --- | --- |
| A-1 | Interest and dividends from state/local bonds of other states | 35 ILCS 5/203(a)(2)(F) |
| A-5 | Bonus depreciation add-back (IL decouples from IRC §168(k); the addition and the replacement subtraction are computed on Form IL-4562) | 35 ILCS 5/203(a)(2)(D-25); IL-4562 instr. |
| A-18 | Net loss add-back (if federal AGI includes IL net loss deduction from prior years that IL has not allowed) | 35 ILCS 5/203(e) |
| A-24 | SALT deduction add-back -- Illinois requires add-back of any state income tax deducted federally (this is automatic since IL starts from AGI, not taxable income) | N/A -- structural |

- **Key structural point** — Because Illinois starts from federal AGI (not federal taxable income), the federal standard deduction, itemized deductions, and QBI deduction do NOT flow into the Illinois computation. This means there is no SALT add-back issue -- it is handled structurally.  _(N/A -- structural)_

### Step 3: Subtract Illinois subtraction modifications (Line 7, Schedule M)

Common subtractions:

**Subtraction modifications table**  _(see rows)_

| Subtraction | Description | Source |
| --- | --- | --- |
| S-1 | U.S. government interest (Treasury bonds, savings bonds) | 35 ILCS 5/203(a)(2)(N) |
| S-2 | Illinois income tax refund included in federal AGI | Structural (IL tax is not deductible for IL) |
| S-7 | Social Security and railroad retirement income included in federal AGI | 35 ILCS 5/203(a)(2)(F) |
| S-8 | IL retirement income subtraction (contributions to qualified IL plans) | 35 ILCS 5/203(a)(2)(F) |
| S-19 | Illinois special depreciation (replace federal bonus with IL straight-line MACRS) | 35 ILCS 5/203(a)(2)(D-25) |

### Step 4: Compute Illinois base income (Line 9)

- **Illinois base income formula** — Federal AGI + additions - subtractions = Illinois base income.  _(35 ILCS 5/203)_

### Step 5: Subtract personal exemptions (Line 10)

- **Personal exemptions (2025)** — $2,850 per taxpayer (single: $2,850; MFJ: $5,700); $2,850 per dependent claimed on the federal return; plus $1,000 for each of age 65+ and legal blindness, for the taxpayer and for the spouse. The exemptions are disallowed in full, not tapered, once federal AGI exceeds $250,000 (single, HoH, MFS) or $500,000 (MFJ).  _(35 ILCS 5/204; 35 ILCS 5/204(d); IDOR FY 2025-16)_

### Step 6: Compute Illinois net income (Line 11)

- **Illinois net income formula** — Illinois base income - exemptions = Illinois net income. If negative, enter zero.  _(35 ILCS 5/204)_

### Step 7: Compute Illinois tax (Line 12)

- **Illinois tax formula** — Illinois net income x 4.95% = Illinois income tax.  _(35 ILCS 5/201(b)(5.4))_

### Step 8: Apply tax credits (Lines 14-23)

- **Credit order** — Apply credits in this order: 1. Property tax credit (Schedule ICR): 5% of property taxes paid on the principal residence. Non-refundable; disallowed when federal AGI exceeds $250,000 (single, HoH, MFS) or $500,000 (MFJ). 2. K-12 education expense credit (Schedule ICR): 25% of qualifying expenses exceeding $250, max credit $750. Non-refundable; subject to the same AGI cap. 3. Credit for taxes paid to other states: If the taxpayer earned income in another state that was taxed by that state, Illinois allows a credit to prevent double taxation. Non-refundable. 4. Illinois Earned Income Credit (Schedule IL-E/EIC): 20% of federal EIC. Refundable, and not subject to the AGI cliff.  _(35 ILCS 5/208; 35 ILCS 5/201(m); 35 ILCS 5/212; Schedule ICR instr.)_

### Step 9: Subtract withholding and estimated payments (Lines 24-27)

- **Withholding and payments** — Illinois withholding from W-2s and 1099s. Estimated tax payments made (Form IL-1040-ES). Overpayment from prior year applied.  _(35 ILCS 5/803)_

### Step 10: Compute balance due or refund (Line 34/36)

- **Balance due/refund formula** — Tax after credits - withholding - estimated payments = balance due (if positive) or refund (if negative).  _(IL-1040 instr.)_

## Section 5 -- Edge cases and special rules

### E-1: Bonus depreciation add-back and replacement

- **Bonus depreciation add-back and replacement** — Illinois requires taxpayers to add back federal bonus depreciation (IRC §168(k)) and instead claim the standard MACRS depreciation that would have been allowable without bonus depreciation. Both the addition and the replacement subtraction are computed on Form IL-4562 and carried to Schedule M. This creates a timing difference, not a permanent one. Track the depreciation schedules carefully.  _(35 ILCS 5/203(a)(2)(D-25); IL-4562 instr.)_

### E-2: Net loss limitation is a corporate rule

- **No individual net loss cap** — The Illinois net loss deduction cap (35 ILCS 5/207) applies to corporations filing Form IL-1120: $500,000 per year for tax years ending on or after December 31, 2024 and before December 31, 2027, and $100,000 per year for tax years ending before December 31, 2024. It does not apply to individuals. An individual's federal net operating loss deduction reaches the IL-1040 through federal AGI and is not capped by Illinois.  _(35 ILCS 5/207; 2025 IL-1120 instr. (R-12/25); PA 103-0592)_

### E-3: No standard deduction

- **No standard deduction** — Illinois has NO standard deduction and NO itemized deductions at the state level. The only below-the-line deduction is the personal exemption. This catches taxpayers who expect a state deduction mirroring the federal one.  _(86 Ill. Admin. Code 100.2410)_

### E-4: Social Security subtraction

- **Social Security subtraction** — All Social Security benefits included in federal AGI are subtracted for Illinois purposes. Illinois does not tax Social Security income.  _(35 ILCS 5/203(a)(2)(F).)_

### E-5: Illinois residency determination

- **Residency determination** — An Illinois resident is an individual who is in Illinois for other than a temporary or transitory purpose, or who is domiciled in Illinois but absent for a temporary or transitory purpose. The test is domicile and purpose of presence; Illinois has no "place of abode plus day count" statutory-residency test of the New York or California kind, so keeping a home in Illinois does not by itself make a person domiciled elsewhere a resident.  _(35 ILCS 5/1501(a)(20); 86 Ill. Admin. Code 100.3020)_

### E-6: Gambling winnings

- **Gambling winnings** — Illinois does not allow a subtraction for gambling losses. If federal AGI includes net gambling winnings (after losses are deducted as federal itemized deductions), the Illinois computation starts from AGI which includes gross gambling winnings. The losses deducted federally as itemized deductions do not reduce IL base income.  _(unsure)_

## Section 6 -- Test suite

### Test 1: Standard freelancer, single

**Input:** Federal AGI: $100,000 (all Schedule C). No additions. Social Security subtraction: $0. No property tax. Single, no dependents. Tax year 2025.
**Expected:** Base income: $100,000. Exemption: $2,850. Net income: $97,150. Tax: $97,150 x 4.95% = $4,808.93.

### Test 2: MFJ with property tax credit

**Input:** Federal AGI: $150,000. No modifications. MFJ, 2 dependents. Property taxes paid: $8,000. Tax year 2025.
**Expected:** Exemptions: $5,700 + (2 x $2,850) = $11,400. Net income: $138,600. Tax: $138,600 x 4.95% = $6,860.70. Property tax credit: $8,000 x 5% = $400 (federal AGI is under the $500,000 MFJ cap). Net tax: $6,460.70.

### Test 2a: Exemption cliff

**Input:** Federal AGI: $260,000. No modifications. Single, no dependents. Property taxes paid: $9,000. Tax year 2025.
**Expected:** Federal AGI exceeds $250,000, so the personal exemption is $0 (not reduced, disallowed) and the property tax credit is disallowed. Net income: $260,000. Tax: $260,000 x 4.95% = $12,870.00.

### Test 3: Bonus depreciation add-back

**Input:** Federal AGI includes $50,000 of bonus depreciation on a $50,000 asset (5-year MACRS). Year 1.
**Expected:** Addition: $50,000. Subtraction: $10,000 (year 1 standard MACRS on 5-year property). Net addition: $40,000. Track remaining $40,000 as future IL subtractions.

### Test 4: Social Security subtraction

**Input:** Federal AGI: $60,000 including $12,000 of Social Security benefits taxed federally.
**Expected:** Subtraction: $12,000. IL base income: $48,000.

### Test 5: Earned income credit

**Input:** Federal EIC: $2,000. Single, 1 child.
**Expected:** IL EIC: $2,000 x 20% = $400 (refundable).

## Section 7 -- Prohibitions

- **P-1:** Do NOT apply a standard deduction or itemized deductions to Illinois income. Only the personal exemption applies.
- **P-2:** Do NOT apply the corporate net loss deduction cap ($500,000; 35 ILCS 5/207) to an individual. It belongs to Form IL-1120.
- **P-3:** Do NOT assume bonus depreciation flows through. Illinois requires the add-back.
- **P-4:** Do NOT tax Social Security benefits for Illinois purposes.
- **P-5:** Do NOT file an Illinois extension form. The 6-month extension is automatic for every filer, with or without a federal extension; only the payment is due on April 15.
- **P-7:** Do NOT taper the exemptions or the property-tax and K-12 credits near the AGI cap. They are disallowed in full once federal AGI exceeds $250,000 (single, HoH, MFS) or $500,000 (MFJ).
- **P-6:** Do NOT use graduated brackets. Illinois has a flat 4.95% rate.

## Section 8 -- Self-checks

Before delivering output, verify:

- [ ] Federal AGI correctly transcribed from Form 1040, Line 11
- [ ] All Schedule M additions identified (especially bonus depreciation)
- [ ] All Schedule M subtractions identified (especially Social Security, gov't bond interest)
- [ ] Personal exemptions correctly computed ($2,850 x number of exemptions for 2025, plus $1,000 per age-65/blind condition), and set to zero above the $250,000 / $500,000 AGI cliff
- [ ] Flat rate of 4.95% applied
- [ ] Property tax credit at 5% (non-refundable; disallowed above the AGI cap)
- [ ] EIC at 20% of federal EIC (refundable)
- [ ] No standard deduction applied
- [ ] No corporate net loss cap applied to the individual
- [ ] Reviewer brief includes all positions and flags

## Section 9 -- Disclaimer

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
