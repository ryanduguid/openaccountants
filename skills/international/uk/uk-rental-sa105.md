---
name: uk-rental-sa105
description: >
  Use this skill whenever asked about UK property income or rental income for individuals. Trigger on phrases like "SA105", "rental income UK", "property income", "buy-to-let", "letting income", "landlord tax UK", "rent-a-room", "mortgage interest relief", "Section 24", "property allowance", "non-resident landlord scheme", "NRLS", "furnished holiday let", "FHL abolished", "repairs deduction", "letting agent fees", "property expenses", "UK property pages", or any question about computing, filing, or reporting UK property income on a Self Assessment tax return. Covers SA105 form structure, allowable expenses, mortgage interest restriction, Rent-a-Room relief, property income allowance, non-resident landlord scheme, and the abolition of FHL rules. ALWAYS read this skill before touching any UK rental income work.
version: 1.0
jurisdiction: GB
tax_year: 2025
category: international
depends_on:
  - uk-income-tax-sa100
verified_by: pending
---

# UK Property Income (SA105) Skill v1.0

---

## Section 1 -- Quick Reference

| Field | Value |
|---|---|
| Country | United Kingdom |
| Tax | Income Tax on Property Income |
| Currency | GBP only |
| Tax year | 6 April to 5 April (2024-25: 6 April 2024 -- 5 April 2025) |
| Primary legislation | Income Tax (Trading and Other Income) Act 2005 (ITTOIA), Part 3 |
| Supporting legislation | Income Tax Act 2007, ss. 274A-274D (mortgage interest restriction); ITTOIA ss. 784-802 (Rent-a-Room); Finance Act 2025 (FHL abolition) |
| Tax authority | HM Revenue and Customs (HMRC) |
| Filing portal | HMRC Self Assessment Online |
| Filing deadline (online) | 31 January following the tax year |
| Filing deadline (paper) | 31 October following the tax year |
| SA105 form | UK Property supplementary pages to SA100 |
| Validated by | Pending — requires sign-off by a UK chartered accountant or licensed tax adviser |
| Skill version | 1.0 |

### SA105 Key Boxes (2024-25)

| Box | Description | Section |
|---|---|---|
| Box 3 | Joint property income indicator | Header |
| Box 4 | Rent-a-Room relief (rents ≤£7,500) | Rent-a-Room |
| Box 5 | Total rents and income from property (FHL section) | FHL — abolished from 2025-26 |
| Box 20 | Total rents and other income from property | Property income |
| Box 20.1 | Property income allowance (£1,000) | Allowance |
| Box 24 | Rent, rates, insurance and ground rents | Expenses |
| Box 25 | Property repairs and maintenance | Expenses |
| Box 26 | Loan interest and other financial costs | Expenses |
| Box 27 | Legal, management and other professional fees | Expenses |
| Box 28 | Costs of services provided, including wages | Expenses |
| Box 29 | Other allowable property expenses | Expenses |
| Box 30 | Private use adjustment | Expenses |
| Box 36 | Replacement of domestic items relief | Expenses |
| Box 37 | Rent-a-Room exempt amount | Relief |
| Box 38 | Adjusted profit for the year | Computed |
| Box 39 | Loss brought forward from earlier years | Losses |
| Box 40 | Taxable profit (Box 38 minus Box 39) | Final |

### Income Tax Rates (2024-25)

| Band | Taxable income | Rate |
|---|---|---|
| Personal allowance | Up to £12,570 | 0% |
| Basic rate | £12,571 -- £50,270 | 20% |
| Higher rate | £50,271 -- £125,140 | 40% |
| Additional rate | Over £125,140 | 45% |

Property income is added to all other income and taxed at the marginal rate.

### Conservative Defaults

| Ambiguity | Default |
|---|---|
| Unknown property use (residential vs commercial) | Treat as residential (mortgage interest restriction applies) |
| Unknown whether jointly owned | STOP — affects share of income/expenses |
| Unknown residency status | STOP — NRLS rules differ |
| Unknown repair vs improvement | Treat as improvement (not deductible) |
| Unknown private use percentage | 100% private (no deduction) |

---

## Section 2 -- Allowable Expenses

### 2.1 Fully Deductible Revenue Expenses

| Expense | SA105 Box | Notes |
|---|---|---|
| Letting agent fees / management charges | Box 27 | Percentage of rent or fixed fee |
| Insurance (buildings, landlord liability, rent guarantee) | Box 24 | Property-specific insurance only |
| Council tax (if paid by landlord) | Box 24 | Only when landlord contractually pays |
| Ground rent / service charges | Box 24 | Leasehold obligations |
| Water rates (if paid by landlord) | Box 24 | Metered or unmetered |
| Accountancy fees (property accounts) | Box 27 | Attributable to property business |
| Legal fees (tenancy agreements, debt recovery) | Box 27 | Revenue legal costs only |
| Advertising for tenants | Box 29 | Online listings, newspaper ads |
| Travel to property (inspections, repairs) | Box 29 | Mileage at 45p/mile (first 10,000) then 25p |
| Stationery and postage | Box 29 | Property business related |
| Telephone costs (property business calls) | Box 29 | Apportioned if personal phone |

### 2.2 Repairs vs Improvements

| Deductible (Repairs) | NOT Deductible (Improvements) |
|---|---|
| Replacing broken boiler with equivalent | Installing central heating where none existed |
| Repainting after tenant departure | Adding an extension or conservatory |
| Fixing leaking roof (like-for-like) | Converting loft into habitable room |
| Replacing rotten window frames (like-for-like) | Upgrading single glazing to double glazing |
| Re-plastering damaged walls | Rewiring entire property (if improvement) |

HMRC applies the principle: does it restore the asset to its original condition (repair) or improve/enhance it (capital)?

### 2.3 Replacement of Domestic Items Relief (Box 36)

From April 2016, for residential lets:
- Claim the cost of replacing a domestic item (furniture, furnishings, appliances, kitchenware)
- The ORIGINAL purchase cost is NOT deductible — only replacements
- If the replacement is an improvement, only the cost of an equivalent replacement is deductible
- Domestic items include: beds, sofas, carpets, curtains, white goods, televisions, crockery

### 2.4 Mortgage Interest Restriction (Section 24)

From 2020-21, finance costs for residential property are **fully restricted**:

| Component | Treatment |
|---|---|
| Mortgage interest | NOT deductible as an expense |
| Arrangement fees (revenue portion) | NOT deductible as an expense |
| Tax credit | 20% of the lower of: (a) finance costs, (b) property profits, (c) adjusted total income |

The restriction applies to:
- Individual landlords (not companies)
- Residential property lettings only
- Partnerships of individuals

The restriction does NOT apply to:
- Companies (corporate landlords can still deduct interest)
- Commercial property lettings
- Previously: Furnished Holiday Lets — but FHL regime is abolished from April 2025

**Box 26** on SA105 still captures finance costs, but HMRC computes the 20% basic rate reduction separately on the tax computation.

### 2.5 Property Income Allowance (£1,000)

- If gross property income is £1,000 or less: no need to report or register for Self Assessment
- If gross property income exceeds £1,000: choose between claiming the £1,000 allowance (no expenses deducted) or deducting actual expenses
- Cannot claim both the allowance and expenses
- Cannot claim if income is from a connected person (employer, family company)

---

## Section 3 -- Rent-a-Room Relief

| Feature | Detail |
|---|---|
| Threshold | £7,500 per year (£3,750 if letting jointly) |
| Requirement | Must let furnished accommodation in your only or main home |
| If income ≤ threshold | Put 'X' in Box 4; no further property pages needed |
| If income > threshold | Option 1: Tax on excess (income minus £7,500 in Box 37, no expenses); Option 2: Normal profit calculation (ignore Box 37) |
| Cannot combine with | Property income allowance (choose one or the other) |
| Does NOT apply to | Unfurnished rooms, separate self-contained flats, non-main-residence |

---

## Section 4 -- Furnished Holiday Lets (FHL) -- Abolished

### Pre-April 2025 (2024-25 and Earlier)

FHL status required meeting ALL of:
- Available for letting ≥210 days per year
- Actually let ≥105 days per year
- Not let to the same person for >31 consecutive days (total such lets <155 days)

FHL benefits included: full mortgage interest deduction, capital allowances on furniture, CGT reliefs (Entrepreneurs'/BADR, rollover), pension-relevant earnings.

### From April 2025 (2025-26 Onwards)

The FHL regime is **abolished** by Finance Act 2025:
- All former FHLs are treated as standard residential property
- Mortgage interest restriction (Section 24) applies
- No capital allowances on furniture (replacement of domestic items relief instead)
- CGT: no BADR, no rollover relief (standard residential CGT rates apply)
- Not pension-relevant earnings

**Transitional:** Overlap relief and brought-forward losses from FHL remain available in 2025-26 under transitional provisions.

---

## Section 5 -- Non-Resident Landlord Scheme (NRLS)

| Feature | Detail |
|---|---|
| Applies to | Landlords whose "usual place of abode" is outside the UK |
| Withholding | Letting agent or tenant must withhold basic rate tax (20%) from rent and pay to HMRC quarterly |
| HMRC approval | Non-resident can apply to receive rent gross (form NRL1) if tax affairs are up to date |
| Annual return | Non-resident must still file SA100 + SA105 (or SA700 for companies) |
| Expenses | Same rules apply — agent may deduct allowable expenses before withholding |

---

## Section 6 -- Transaction Pattern Library

### 6.1 Income Patterns (Credits)

| Pattern | Treatment | Notes |
|---|---|---|
| TENANT RENT, STANDING ORDER [tenant name] | Box 20 -- rental income | Monthly rent receipts |
| LETTING AGENT DEPOSIT, FOXTONS, OPENRENT | Box 20 -- rental income | Agent-collected rent (gross up if agent deducts fees) |
| AIRBNB PAYOUT, BOOKING.COM | Box 20 -- rental income | Short-term platform income; may also be Rent-a-Room eligible |
| TENANT DEPOSIT (via DPS, TDS, mydeposits) | EXCLUDE | Refundable deposit — not income unless forfeited |
| DEPOSIT RETENTION, DAMAGE DEDUCTION | Box 20 -- rental income | Retained deposit = income in the year retained |
| HMRC REFUND, TAX REFUND | EXCLUDE | Not rental income |

### 6.2 Expense Patterns (Debits)

| Pattern | SA105 Box | Notes |
|---|---|---|
| MORTGAGE, NATIONWIDE, BARCLAYS MORTGAGE | Box 26 (finance costs) | Subject to Section 24 restriction — 20% credit only |
| BUILDINGS INSURANCE, LANDLORD INSURANCE | Box 24 | Fully deductible |
| LETTING AGENT FEE, MANAGEMENT FEE | Box 27 | Fully deductible |
| PLUMBER, ELECTRICIAN, BUILDER [repair] | Box 25 | Deductible if repair; capital if improvement |
| GAS SAFETY, ELECTRICAL CERTIFICATE, EPC | Box 29 | Regulatory compliance — fully deductible |
| COUNCIL TAX (landlord-paid void period) | Box 24 | Deductible during void periods between tenants |
| GROUND RENT, SERVICE CHARGE | Box 24 | Leasehold costs |
| CLEANING, END OF TENANCY CLEAN | Box 29 | Between-tenant cleaning |
| JOHN LEWIS, CURRY'S [replacement appliance] | Box 36 | Replacement of domestic items relief |
| ACCOUNTANT, TAX RETURN FEE | Box 27 | Property portion only |
| FURNITURE, BED, SOFA [replacement] | Box 36 | Replacement only — not first purchase |

### 6.3 Exclusions

| Pattern | Treatment |
|---|---|
| MORTGAGE CAPITAL REPAYMENT | EXCLUDE — not an expense |
| PROPERTY PURCHASE, STAMP DUTY, SOLICITOR (acquisition) | EXCLUDE — capital cost (relevant to CGT on disposal) |
| PERSONAL USE EXPENSES | EXCLUDE — private use |
| INTERNAL TRANSFER, OWN ACCOUNT | EXCLUDE |

---

## Section 7 -- Worked Examples

### Example 1 -- Basic Buy-to-Let (2024-25)

**Input:** Annual rent £12,000. Mortgage interest £4,000. Agent fees £1,200. Insurance £300. Repairs £800. No other property income. Basic rate taxpayer.

**Computation:**
```
Box 20: £12,000
Box 24: £300 (insurance)
Box 25: £800 (repairs)
Box 26: £4,000 (finance costs — restricted)
Box 27: £1,200 (agent fees)

Profit before finance costs: £12,000 - £300 - £800 - £1,200 = £9,700
Finance cost deduction: £0 (fully restricted for residential)
Property profit: £9,700
Tax at 20% (basic rate): £1,940
Finance cost tax credit: 20% × £4,000 = £800
Net tax on property income: £1,940 - £800 = £1,140
```

### Example 2 -- Rent-a-Room (Under Threshold)

**Input:** Rents out furnished spare bedroom in main home. Annual income £6,000.

**Computation:** Income £6,000 < £7,500 threshold. Put 'X' in Box 4. No further SA105 needed. Tax = £0 on this income.

### Example 3 -- Rent-a-Room (Over Threshold)

**Input:** Spare room income £10,000.

**Option A (Rent-a-Room exemption method):**
```
Taxable = £10,000 - £7,500 = £2,500
No expenses can be deducted alongside
```

**Option B (Normal calculation):**
```
If actual expenses are £4,000: profit = £10,000 - £4,000 = £6,000
```
Option A (£2,500 taxable) is better than Option B (£6,000 taxable).

### Example 4 -- Higher Rate Taxpayer with Section 24 Restriction

**Input:** Total income £80,000 (employment) + £15,000 rent. Mortgage interest £8,000. Other expenses £3,000.

**Computation:**
```
Property profit: £15,000 - £3,000 = £12,000
Taxed at 40% (higher rate): £4,800
Finance cost tax credit: 20% × £8,000 = £1,600
Net tax on property: £4,800 - £1,600 = £3,200

Effective tax rate on rent: £3,200 / £15,000 = 21.3%
Without Section 24: tax would be (£15,000 - £3,000 - £8,000) × 40% = £1,600
Section 24 cost to this taxpayer: £1,600 extra
```

---

## Section 8 -- Losses

| Rule | Detail |
|---|---|
| Property losses | Can only be carried forward against future property profits |
| Cannot be set against | Employment income, trading income, or other non-property income |
| Carry forward | Indefinite — no time limit |
| Capital allowances creating loss | Can create or increase a property loss |
| Multiple properties | All UK properties pooled into one property business |
| Box 39 | Losses brought forward from earlier years |

---

## Section 9 -- Edge Cases

### 9.1 Void Periods
Expenses incurred between tenants (council tax, insurance, marketing) remain deductible provided the property is available for letting and the landlord is actively seeking a new tenant.

### 9.2 Mixed-Use Property
If the landlord lives in part of the property and lets another part, apportion expenses by floor area or rooms. Only the letting portion is deductible.

### 9.3 Cash Basis vs Traditional Accounting
- Default for property income from 2017-18: cash basis (income when received, expenses when paid)
- Can elect traditional (accruals) accounting by ticking Box 20.2
- Threshold for mandatory cash basis: gross receipts up to £150,000

### 9.4 Property Income Allowance vs Expenses
If gross rental income is low (near £1,000), compare: claiming £1,000 allowance (no expenses) vs deducting actual expenses. Choose whichever gives the lower taxable amount.

---

## PROHIBITIONS

- NEVER deduct mortgage interest as an expense for residential property — it is a 20% basic rate tax credit only (Section 24)
- NEVER allow the initial purchase cost of domestic items — only replacements qualify under Box 36
- NEVER combine Rent-a-Room relief with the property income allowance
- NEVER allow improvement costs as revenue deductions — these are capital
- NEVER ignore the non-resident landlord scheme for overseas landlords
- NEVER pool UK and overseas property into one computation — they are separate property businesses
- NEVER apply FHL rules for 2025-26 onwards — the regime is abolished
- NEVER present property income computations as definitive — always label as estimated

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
