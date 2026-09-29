---
name: us-il-sales-tax
description: "Illinois Sales Tax return (Form ST-1) for self-employed individuals. Covers all four Illinois occupation and use taxes (ROT, UT, SOT, SUT), state and local rates, hybrid sourcing (origin for sales from Illinois inventory, destination for remote retailers and marketplace facilitators over the nexus threshold), vendor discount, and filing frequencies. Primary source: 35 ILCS 120/ (ROT), 35 ILCS 105/ (UT), 35 ILCS 115/ (SOT), 35 ILCS 110/ (SUT)."
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

# IL Sales Tax

## Illinois Sales Tax (Form ST-1) v1.0

> **Accountant-reviewed.** Rates and thresholds reviewed against the cited authorities by **a licensed accountant (name withheld at their request)** on 2026-06-03; the sign-off is recorded in the frontmatter (`reviewed_by`) and on the roster in `PARTNERS.md`. The verified figures are stated in the sections below with their sources (the separate "Verified rates & thresholds" list that carried them was folded into the body on 2026-09-29). Items the review flagged for clarification are excluded from that sign-off and remain marked in the text.

## What this file is

**Obligation category:** CT (Consumption Tax)
**Functional role:** Return preparation
**Status:** Complete

This is a Tier 2 content skill for preparing the Illinois Form ST-1 (Sales and Use Tax and E911 Surcharge Return). Illinois has a unique four-tax structure for sales/use taxes, and this skill covers all four taxes as they appear on the combined ST-1 return.

## Section 1 -- Scope statement

**In scope:**

- Form ST-1 (Sales and Use Tax and E911 Surcharge Return)
- All four Illinois occupation/use taxes:
  - Retailers' Occupation Tax (ROT) -- on sellers of tangible personal property
  - Use Tax (UT) -- on out-of-state purchases by Illinois consumers
  - Service Occupation Tax (SOT) -- on servicepersons transferring tangible personal property incident to a service
  - Service Use Tax (SUT) -- on consumers of property transferred incident to a service
- State and local rate components
- Vendor discount (1.75%)
- Filing frequency determination

**Out of scope (refused):**

- Automobile Renting Occupation and Use Tax
- Hotel Operators' Occupation Tax
- Telecommunications taxes
- Cannabis taxes
- Chicago Home Rule Municipal Soft Drink Tax and other Chicago-specific levies
- Marketplace facilitator obligations
- Multi-state nexus determinations

## Section 2 -- Filing requirements

### Who must register

- **Registration requirement** — Any person engaged in the business of selling tangible personal property at retail in Illinois must register with the Illinois Department of Revenue (IDOR) and collect and remit ROT. Servicepersons who transfer tangible personal property incident to a service must also register.  _(35 ILCS 120/2.)_

### Filing frequency

**Filing frequency**  _(86 Ill. Admin. Code 130.601)_

| Monthly tax liability | Filing frequency | Source |
| --- | --- | --- |
| $200 or more/month (average) | Monthly (due 20th of following month) | 86 Ill. Admin. Code 130.601 |
| Less than $200/month (average) | Quarterly (due 20th after quarter end) | 86 Ill. Admin. Code 130.601 |
| Less than $50/month (average) | Annual (due January 20) | 86 Ill. Admin. Code 130.601 |

- **Electronic filing** — Illinois generally mandates electronic filing of Form ST-1 for retailers; a waiver is requested on Form IL-900-EW. The $200 average-monthly-liability figure sets monthly versus quarterly filing frequency; it is not an e-file trigger.  _(ST-1 instr.; 86 Ill. Admin. Code 130; 35 ILCS 120/3.)_

## Section 3 -- Rates and thresholds

### The four-tax structure

**The four-tax structure**  _(35 ILCS 120/2; 35 ILCS 105/3; 35 ILCS 115/3; 35 ILCS 110/3)_

| Tax | Who pays | Rate (general merchandise) | Rate (qualifying food/drugs/medical) | Source |
| --- | --- | --- | --- | --- |
| Retailers' Occupation Tax (ROT) | Seller | 6.25% state | 1.0% state | 35 ILCS 120/2 |
| Use Tax (UT) | Buyer (out-of-state) | 6.25% state | 1.0% state | 35 ILCS 105/3 |
| Service Occupation Tax (SOT) | Serviceperson | 6.25% state | 1.0% state | 35 ILCS 115/3 |
| Service Use Tax (SUT) | Consumer of service | 6.25% state | 1.0% state | 35 ILCS 110/3 |

**Note:** In practice, sellers collect all four taxes as a combined "sales tax" and remit on Form ST-1. The buyer sees a single tax rate.

### State rate components

**State rate components**  _(35 ILCS 120/2; 35 ILCS 120/2-10)_

| Component | Rate | Source |
| --- | --- | --- |
| State (general merchandise) | 6.25% | 35 ILCS 120/2 |
| State (qualifying food, drugs, medical appliances) | 1.00% (2025); the statewide 1% grocery tax is eliminated effective January 1, 2026, and municipalities may impose a local 1% grocery tax in its place; drugs and medical appliances stay at 1% | 35 ILCS 120/2-10; PA 103-0781; IDOR PIO-115 |

### Local rate add-ons (examples, 2025)

Sourcing is hybrid (see E-1). A sale from Illinois inventory takes the rate at the seller's Illinois location; a remote retailer or marketplace facilitator over the nexus threshold takes the rate at the purchaser's location.

**Local rate add-ons (examples, 2025)**  _(IDOR MyTax Illinois Tax Rate Finder)_

| Location | Combined rate (general) | Combined rate (food/drugs) | Source |
| --- | --- | --- | --- |
| Chicago | 10.25% (6.25% state + county, RTA and city) | 2.25% | IDOR MyTax Illinois Tax Rate Finder |
| Cook County (outside Chicago) | ~9.00-10.25% | varies | IDOR MyTax Illinois Tax Rate Finder |
| Springfield (Sangamon Co.) | 9.75% (6.25% state + 1.00% county + 2.50% home-rule city); 8.75% is an outdated figure | 2.00% | IDOR MyTax Illinois Tax Rate Finder |
| Champaign | 9.00% (6.25% state + 1.25% county + 1.50% city); some third-party sources show 9.25% after local changes, so confirm | 2.00% | IDOR MyTax Illinois Tax Rate Finder |

**Important:** Local rates vary by municipality and county and change during the year. Always verify the exact combined rate for the relevant location using the MyTax Illinois Tax Rate Finder (tax.illinois.gov) before filing.

### Vendor discount

**Vendor discount**  _(35 ILCS 120/3; PA 103-0592; ST-1 instr. (R-01/26), Step 4)_

| Item | Amount | Source |
| --- | --- | --- |
| Vendor discount | 1.75% of the total tax due on the ST-1 (Line 9, state and locally imposed ROT alike) when the return is filed and the tax paid on time; minimum $5 per year; capped at $1,000 per month effective January 1, 2025 | 35 ILCS 120/3; PA 103-0592; ST-1 instr. Step 4 |

The vendor discount compensates the retailer for collecting and remitting tax. ST-1 Step 4 applies the 1.75% to Line 9, the total tax due including the locally imposed taxes, subject to the $1,000 monthly cap; it is forfeited if the return is filed or the tax paid late.

## Section 4 -- Computation rules (Step format)

### Step 1: Determine the applicable tax

0. **Step 1** — Selling tangible personal property at retail? --> ROT Providing a service that involves transferring tangible personal property? --> SOT Purchasing from out-of-state for own use in Illinois? --> UT/SUT Most small retailers will report primarily under ROT.

### Step 2: Classify all sales

0. **Step 2** — For each sale, determine: 1. **Taxable or exempt?** (See Section 5 for exemptions.) 2. **General merchandise or qualifying food/drugs/medical?** (Determines rate.) 3. **Sourcing location.** (For a sale from Illinois inventory the rate depends on WHERE YOU SELL FROM; for a remote retailer or marketplace facilitator over the nexus threshold it depends on WHERE THE GOODS GO. See E-1.)

### Step 3: Compute gross receipts (ST-1 Line 1)

0. **Step 3** — Sum all receipts from taxable and exempt sales.

### Step 4: Subtract exempt receipts (ST-1 Lines 2-4)

0. **Step 4** — Deduct sales for resale, sales to exempt organizations, and other exempt transactions.

### Step 5: Compute taxable receipts by rate category

0. **Step 5** — General merchandise taxable receipts x applicable combined rate (state + local). Qualifying food/drug/medical taxable receipts x applicable combined rate (state + local at reduced rate).

### Step 6: Compute total tax (ST-1 Line 12)

0. **Step 6** — Sum of all tax amounts by rate category.

### Step 7: Apply vendor discount (ST-1 Line 14)

0. **Step 7** — If filing on time: - Total tax due (Line 9, state and local) x 1.75% = vendor discount. - Cap the discount at $1,000 for the month (from January 1, 2025).

### Step 8: Add use tax if applicable (ST-1 Line 18)

0. **Step 8** — For items purchased from out-of-state vendors without IL tax collected, report use tax at the applicable rate.

### Step 9: Compute net tax due (ST-1 Line 20)

0. **Step 9** — Total tax - vendor discount + use tax = net tax due.

## Section 5 -- Edge cases and special rules

### E-1: Hybrid sourcing

- **Hybrid sourcing** — Illinois sourcing is hybrid, not purely origin-based. An in-state retailer selling from Illinois inventory (in store, or shipped from an Illinois location) uses origin sourcing: the rate at the seller's Illinois location. Remote retailers and marketplace facilitators that meet the $100,000-in-sales or 200-transaction nexus threshold source to the destination, the purchaser's Illinois location, under the Leveling the Playing Field for Illinois Retail Act; and effective January 1, 2026 Illinois expands destination-based ROT to in-state sellers shipping from outside the state. Sales by Illinois retailers to out-of-state buyers may be exempt (see E-3).  _(IDOR Publication 113; IDOR Informational Bulletin FY 2026-12; Leveling the Playing Field for Illinois Retail Act; 86 Ill. Admin. Code 130.410.)_

### E-2: Qualifying food, drugs, and medical appliances

- **Qualifying food, drugs, medical appliances** — These items are taxed at the reduced 1% state rate (plus reduced local rates). Qualifying food includes most grocery items but NOT prepared food, soft drinks, candy, or alcoholic beverages, which take the general rate. The statewide 1% tax on qualifying groceries is eliminated effective January 1, 2026 (PA 103-0781); municipalities may impose a local 1% grocery tax in its place, and drugs and medical appliances stay at the 1% state rate.  _(35 ILCS 120/2-10; 86 Ill. Admin. Code 130.310; IDOR PIO-115; PA 103-0781.)_

### E-3: Interstate sales

- **Interstate sales** — Sales shipped to buyers outside Illinois are generally exempt from Illinois ROT if the seller ships the goods via common carrier or U.S. mail. The seller must retain proof of out-of-state delivery.  _(35 ILCS 120/1.)_

### E-4: Service vs. sale distinction

- **Service vs. sale distinction** — If a serviceperson transfers tangible personal property incident to a service, SOT applies to the property transferred, not to the full service charge. The general SOT base is the selling price of the property if it is separately stated on the bill, or 50% of the entire bill if it is not, and never less than the serviceperson's cost. The "cost price" base applies only to de minimis servicepersons (annual cost of property transferred below 35% of total receipts, or below 75% for pharmacists and graphic arts), who may pay use tax on cost price instead. For example, a plumber who installs a faucet and states it separately pays SOT on the faucet's selling price, not on the labor charge.  _(35 ILCS 115/3; 86 Ill. Admin. Code 140.106; IDOR Publication 113.)_

### E-5: Exempt organizations

- **Exempt organizations** — Sales to organizations holding a valid Illinois exemption identification number (E-number) are exempt. The seller must retain a copy of the exemption certificate.  _(35 ILCS 120/2-5(11).)_

### E-6: Zero returns

- **Zero returns** — Retailers with no activity must still file a return showing zero tax. Failure to file results in penalties and potential revocation of the certificate of registration.

### E-7: Prepaid phone cards and calling arrangements

- **Prepaid calling arrangements** — Prepaid calling arrangements are taxable as general merchandise at the point of sale.  _(35 ILCS 120/2-25.)_

## Section 6 -- Test suite

### Test 1: Standard retailer, general merchandise

**Input:** Chicago seller. Gross sales: $20,000, all general merchandise, all in-store. No exempt sales.
**Expected:** Combined rate: 10.25%. Tax: $20,000 x 10.25% = $2,050. Vendor discount on the total tax (under the $1,000 monthly cap): $2,050 x 1.75% = $35.88. Net tax: $2,050 - $35.88 = $2,014.12.

### Test 2: Mixed rate sales (food and general, 2025)

**Input:** Springfield seller. General merchandise: $10,000. Qualifying food: $5,000. Month in 2025.
**Expected:** General: $10,000 x 9.75% = $975. Food: $5,000 x 2.00% = $100. Total: $1,075. Vendor discount on the total tax: $1,075 x 1.75% = $18.81. Net: $1,056.19. (From January 1, 2026 the 1% state grocery tax no longer applies; use the local grocery tax, if any, for the food line.)

### Test 3: Service with property transfer

**Input:** HVAC contractor in Champaign. Service charge: $3,000. Parts transferred, separately stated on the bill at a selling price of $1,200 (cost $800).
**Expected:** SOT applies to the $1,200 selling price of the parts (separately stated, and above cost). Tax: $1,200 x 9.00% = $108. Had the parts not been separately stated, the base would be 50% of the $4,200 bill, $2,100.

### Test 4: Use tax on out-of-state purchase

**Input:** Chicago business purchases $5,000 of equipment from out-of-state vendor, no tax collected.
**Expected:** Use tax: $5,000 x 10.25% = $512.50.

### Test 5: Late filing (no vendor discount)

**Input:** Same as Test 1 but filed 10 days late.
**Expected:** No vendor discount. Net tax: $2,050 plus penalties and interest.

## Section 7 -- Prohibitions

- **P-1:** Do NOT source every sale by the seller's location. Sales from Illinois inventory are origin-sourced; remote retailers and marketplace facilitators over the nexus threshold source to the destination (E-1).
- **P-2:** Do NOT charge the general merchandise rate on qualifying food, drugs, or medical appliances.
- **P-3:** Do NOT limit the vendor discount to the state portion. It is 1.75% of the total ST-1 tax due (Line 9), capped at $1,000 per month.
- **P-4:** Do NOT apply SOT to the full service charge -- the base is the selling price of the transferred property (or 50% of the bill when not separately stated), never less than cost; cost price is only for de minimis servicepersons.
- **P-5:** Do NOT claim vendor discount on a late-filed return.
- **P-6:** Do NOT assume all food is taxed at the reduced rate. Prepared food, candy, and soft drinks are taxed at the general rate.

## Section 8 -- Self-checks

Before delivering output, verify:

- [ ] Correct combined rate used for seller's location (verified via IDOR tax rate database)
- [ ] Sales properly categorized as general merchandise vs. qualifying food/drugs/medical
- [ ] Sourcing applied per E-1 (origin for sales from Illinois inventory; destination for remote retailers and marketplace facilitators over the threshold)
- [ ] Vendor discount at 1.75% of the total ST-1 tax, capped at $1,000 per month, only for timely returns
- [ ] SOT applied to the selling price of the transferred property (or 50% of the bill if not separately stated), not to the service charge
- [ ] Use tax reported for out-of-state purchases
- [ ] Zero return filed if no activity
- [ ] Interstate sales properly excluded with documentation

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
