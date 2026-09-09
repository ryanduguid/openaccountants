---
name: pe-individual-return
description: "> Use this skill whenever asked about Prince Edward Island provincial individual income tax. Trigger on phrases like \"PEI tax\", \"Prince Edward Island tax\", \"PE provincial tax\", \"PEI T1\", \"PEI brackets\", \"HST PEI\", \"PEI credits\", or any question about computing PEI provincial tax for an individual return. This skill covers PEI's five-bracket tax system (the surtax was abolished for 2024), HST at 15%, provincial credits, and filing requirements. ALWAYS read this skill before touching any PEI individual tax return work."
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
metadata:
  source: openaccountants
  jurisdiction: CA
  category: international
  quality: source-cited draft
  openaccountants_url: "https://openaccountants.com/skills/pe-individual-return"
  tax_year: 2025
  obligation: IT
---

# Prince Edward Island Individual Tax Return -- Provincial T1 Skill v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

---

## Section 1 -- Quick Reference

| Field | Value |
|---|---|
| Province | Prince Edward Island (Canada) |
| Tax | Provincial Personal Income Tax |
| Currency | CAD only |
| Tax year | 1 January -- 31 December 2025 |
| Primary legislation | Income Tax Act (Prince Edward Island) |
| Tax authority | Canada Revenue Agency (administers on behalf of PEI) |
| Filing portal | CRA My Account / NETFILE / paper T1 |
| Filing deadline | 30 April 2026 (15 June 2026 if self-employed; balance due 30 April) |
| Skill version | 1.0 |

### PEI Provincial Tax Rates (2025)

| Taxable Income (CAD) | Rate |
|---|---|
| 0 -- 33,328 | 9.5% |
| 33,329 -- 64,656 | 13.47% |
| 64,657 -- 105,000 | 16.6% |
| 105,001 -- 140,000 | 17.62% |
| 140,001+ | 19% |

### Key PEI Features

| Feature | Detail |
|---|---|
| Harmonized sales tax (HST) | 15% (5% federal + 10% provincial) |
| Basic personal amount (2025) | $14,650 |
| Spousal/equivalent amount | $14,650 |
| Age amount | $4,959 |
| PEI Low-Income Tax Reduction | Reduces/eliminates tax for low-income residents |
| PEI Sales Tax Credit | $110/adult; income-tested |
| PEI Volunteer Firefighter Credit | $500 |

### Combined Federal + PEI Marginal Rates (2025)

| Taxable Income (CAD) | Combined Rate |
|---|---|
| 0 -- 33,328 | 24% |
| 33,329 -- 57,375 | 27.97% |
| 57,376 -- 64,656 | 33.97% |
| 64,657 -- 105,000 | 37.1% |
| 105,001 -- 114,750 | 38.12% |
| 114,751 -- 140,000 | 43.62% |
| 140,001 -- 177,882 | 45% |
| 177,883 -- 253,414 | 48% |
| 253,415+ | 52% |

### Conservative Defaults

| Ambiguity | Default |
|---|---|
| Unknown residency province on Dec 31 | Do not compute -- confirm province |
| Unknown marital/family status | Single, no dependants |

---

## Section 2 -- Classification and Filing

### 2.1 T1 Structure

| Schedule | Purpose |
|---|---|
| T1 General | Federal return |
| Form PE428 | PEI Tax and Credits |
| Form PE479 | PEI Credits (refundable) |

### 2.2 Provincial Non-Refundable Credits (Form PE428)

| Credit | Amount (2025) | Rate |
|---|---|---|
| Basic personal amount | $13,500 | 9.5% |
| Spousal / common-law partner | $13,500 | 9.5% |
| CPP/EI contributions | Actual | 9.5% |
| Age amount | $4,959 | 9.5% |
| Pension income | Up to $1,000 | 9.5% |
| Disability | $8,777 | 9.5% |
| Tuition | Actual | 9.5% |
| Medical expenses | Excess over 3% of net income | 9.5% |
| Donations | First $200 at 9.5%; excess at 19% | Non-refundable |
| Volunteer firefighter | $500 | 9.5% |

### 2.4 PEI Refundable Credits (Form PE479)

| Credit | Detail |
|---|---|
| PEI Sales Tax Credit | $110/adult; income-tested; phases out above $30,000 (single) |
| Low-Income Tax Reduction | Eliminates/reduces tax for incomes below ~$20,000 |
| Seniors Independence Initiative | Home care/modification assistance (not a tax credit per se) |
| Community Development Equity Tax Credit | 35% of eligible investment |

---

## Section 3 -- Computation Method

### Step 1: Calculate Taxable Income
Same as federal taxable income (Line 26000).

### Step 2: Apply PEI Bracket Rates
- First $33,328 × 9.5%
- $33,329 to $64,656 × 13.47%
- $64,657 to $105,000 × 16.6%
- $105,001 to $140,000 × 17.62%
- Above $140,000 × 19%

### Step 3: Subtract Non-Refundable Tax Credits
Total credit amounts × 9.5% (lowest bracket rate).

### Step 4: Apply Low-Income Tax Reduction
Reduces or eliminates tax for low-income earners.

### Step 5: Net Provincial Tax
After credit reductions. There is no surtax step: PEI abolished its surtax for 2024 and later years.

### Step 6: Apply Refundable Credits
Subtract Sales Tax Credit and other refundable amounts.

---

## Section 4 -- HST Considerations

| Item | Detail |
|---|---|
| HST rate | 15% (5% federal + 10% provincial) |
| HST registrant | Full ITC available for business purchases |
| Small supplier threshold | $30,000 in 4 consecutive quarters |
| Real property (new residential) | Provincial new housing rebate available |

---

## Section 5 -- Income Types and Dividend Tax Credits

### 5.1 PEI Dividend Tax Credit

| Dividend Type | Federal Gross-Up | PE Credit Rate |
|---|---|---|
| Eligible dividends (public corps) | 38% gross-up | 10.5% of taxable amount |
| Non-eligible dividends (CCPCs) | 15% gross-up | 1.8% of taxable amount |

### 5.2 Capital Gains

- 50% inclusion rate for first $250,000 (individuals)
- 66.67% above $250,000 (effective June 2024)
- Lifetime Capital Gains Exemption: $1,250,000 on qualifying small business shares
- Combined top rate on capital gains (50% inclusion): ~25.5%

### 5.3 Filing Deadlines and Instalments

| Item | Detail |
|---|---|
| Filing deadline | 30 April 2026 (self-employed: 15 June 2026) |
| Balance due | 30 April 2026 regardless of filing deadline |
| Instalment threshold | Net tax owing > $3,000 in current year AND either of prior 2 years |
| Instalment schedule | Quarterly: March 15, June 15, September 15, December 15 |
| Interest on late balance | Prescribed rate (compounded daily) |

---

## Section 6 -- Edge Cases

### 6.1 Returns for 2023 and Earlier -- the Repealed Surtax
PEI levied a 10% surtax on basic provincial tax over $12,500 up to and including the **2023** tax year. It was repealed as part of the 2023-24 budget, which replaced the three-bracket-plus-surtax structure with the current five-bracket scale from 2024 onward.

Apply the surtax **only** when preparing or amending a return for 2023 or an earlier year, using that year's brackets. For 2024 and later, there is no surtax.  _(EY Tax Alert 2023 no. 22, *Prince Edward Island budget 2023-24*)_

### 6.2 Seasonal Workers
PEI has significant seasonal employment (fishing, tourism, agriculture). Workers may have:
- EI benefits during off-season (taxable)
- Intermittent T4s from multiple employers
- Provincial tax applies to total income regardless of seasonal pattern

### 6.3 Small Province Considerations
PEI has a small population (~170,000) -- fewer provincial-specific programs compared to larger provinces. Federal credits (GST/HST credit, Canada Workers Benefit) are particularly important for low-income PEI residents.

### 6.4 Inter-Provincial Commuters
Workers commuting to Nova Scotia or New Brunswick for employment are taxed as PEI residents if resident on Dec 31 in PEI. No provincial tax allocation for employment income earned in other provinces.

### 6.5 Community Development Equity Tax Credit

| Element | Detail |
|---|---|
| Credit rate | 35% of eligible investment |
| Maximum investment | $20,000/year |
| Maximum credit | $7,000/year |
| Eligible businesses | PEI-based community development corporations |
| Hold period | 5 years minimum |
| Carry-forward | 4 years |

### 6.6 PEI Property Transfer Tax
When acquiring property in PEI, a Real Property Transfer Tax of 1% of the greater of purchase price or assessed value applies. This is not an income tax but relevant context for property investors -- it adds to cost base for CGT purposes.

---

## Section 6 -- Prohibitions

- NEVER apply other provincial rates to a PEI resident
- NEVER separate HST into components for filing -- PEI uses harmonized HST
- NEVER claim PEI credits without confirming PEI residency on December 31
- NEVER add a PEI surtax to a 2024-or-later computation; it was repealed. It applies only to 2023 and earlier returns.
- NEVER present tax calculations as definitive -- always label as estimated

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CGA, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

---

_Source: [OpenAccountants](https://openaccountants.com/skills/pe-individual-return) — open tax Guides for AI, reviewed by named CPAs/CAs/EAs. Quality: **source-cited draft**. For always-current figures and named-accountant backing, connect the OpenAccountants MCP server (`openaccountants-mcp`)._
