---
name: bs-income-tax
description: "Bahamas domestic personal income tax scope through 10 November 2026, with National Insurance references and 2025 examples for individuals and sole traders."
jurisdiction: BS
category: international
tax_year: 2025
tax_year_notes: "Personal income tax scope and the July 2026 National Insurance ceiling checked through 10 November 2026. Worked examples use the 2025 schedule."
last_updated: 2026-11-10
version: 0.3
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# bahamas-income-tax

## Section 1 -- Quick Reference

**Section 1 -- Quick Reference**

| Field | Value |
| --- | --- |
| Country | Commonwealth of The Bahamas |
| Domestic personal income tax | None in the period checked through 10 November 2026 |
| Currency | Bahamian Dollar (BSD), pegged 1:1 to USD |
| Personal income tax year | Inapplicable |
| Primary individual obligation | National Insurance Board (NIB) contributions |
| Revenue authority (VAT, Business Licence, RPT) | Department of Inland Revenue (DIR) |
| NIB authority | National Insurance Board (nib-bahamas.com) |
| Filing portal (VAT) | https://vat.revenue.gov.bs/ |
| Bahamian personal income tax return | Inapplicable |
| Validated by | Pending -- requires sign-off by a qualified Bahamian practitioner |
| Validation date | Pending |
| Skill version | 0.3 |

### There Is No Personal Income Tax

The Ministry of Finance's June 2024 competent authority guidance records the absence of a domestic personal income tax. This position was checked through 10 November 2026 against the 2026-27 Budget Communication and the current legislation index. For resident and non-resident individuals, a Bahamian personal income tax base, bands, deductions, allowances and return are inapplicable. Check foreign tax and separate Bahamian reporting and contribution obligations for the facts and period concerned. [Ministry of Finance, Bahamas–Japan MAP guidance, ‘Scope of the MAP “Limitations”’](https://cdn.bahamas.gov.bs/tenant/tenantministryoffinance/documents/All%20Documents/BAHAMAS-JAPANMAPGUIDANCEDOCUMENT-20240718120503.pdf) · [2026-27 Budget Communication](https://bahamasbudget.gov.bs/media/filer_public/81/9d/819d8c82-6e4c-471e-bf84-2e0965620327/final_budget_communication_fiscal_year_20262027-_a_budget_that_build_on_progress_.pdf) · [Legislation index](https://laws.bahamas.gov.bs/cms/legislation/index/by-alphabetical.html)

The examples use the 2025 NIB schedule. See `bs-payroll-social` for the July 2026 ceiling and weekly transition, worker classes and filing requirements.

### NIB Contribution Rates (Effective 1 July 2024)

The ordinary contribution rates changed on 1 July 2024. Check the separate contribution classes before applying these rates to pensioners, people aged 65 or older, summer workers or qualifying gratuities. [S.I. 37 of 2024, regs 1, 4–7 and 9](https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2024/2024-0037S/2024-0037S.pdf) · [NIB rates sheet](https://www.nib-bahamas.com/UserFiles/HTMLEditor/Contribution-Rates-and-Insurable-Ceilings-2024.pdf)

| Category | Rate from 1 Jul 2024 | Previous rate |
| --- | --- | --- |
| Employee | **4.65%** | 3.9% |
| Employer | **6.65%** | 5.9% |
| Combined (employee + employer) | **11.30%** | 9.8% |
| Ordinary self-employed, under 65 and without retirement benefit | **10.30%** | 8.8% |
| Voluntarily insured | **6.50%** | 5.0% |

### NIB Insurable Wage Ceiling

| Period | Weekly ceiling | Monthly ceiling |
| --- | --- | --- |
| Previous (to 30 Jun 2024) | BSD 740 | BSD 3,207 |
| July 2024 schedule through June 2026 | BSD 810 | BSD 3,510 |
| From 1 July 2026 | BSD 830 | BSD 3,597 |

For weekly payroll the BSD 810 ceiling applies to the week beginning 29 June 2026. Use BSD 830 from the week beginning 6 July. Regulation 52 provides for the biennial ceiling adjustment. [NIB July 2026 notice](https://www.nib-bahamas.com/uploads/2026_biennial_adjustments_f9ad1d917d.pdf) · [Contributions Regulations, reg 52](https://laws.bahamas.gov.bs/cms/images/LEGISLATION/SUBORDINATE/1984/1984-0068/1984-0068_2.pdf)

### Maximum Weekly and Annual NIB Contributions at the 2025 Ceiling (BSD 810/week)

These figures show unrounded weekly rate products and illustrative totals over 52 equal contribution weeks. Confirm the NIB rounding and reporting method for a payment.

| Party | Rate | Unrounded weekly amount | 52-week illustration |
| --- | --- | --- | --- |
| Employee | 4.65% | BSD 37.665 | BSD 1,958.58 |
| Employer | 6.65% | BSD 53.865 | BSD 2,800.98 |
| Combined (employee + employer) | 11.30% | BSD 91.53 | BSD 4,759.56 |
| Ordinary self-employed | 10.30% | BSD 83.43 | BSD 4,338.36 |

```oa-check
name: BS unrounded 2025 ordinary contributions at the weekly ceiling
inputs:
  ceiling: 810
  employee_rate: 4.65
  employer_rate: 6.65
  self_employed_rate: 10.3
  weeks: 52
steps:
  - employee_weekly: pct(ceiling, employee_rate)
  - employer_weekly: pct(ceiling, employer_rate)
  - combined_annual: (employee_weekly + employer_weekly) * weeks
  - self_employed_annual: pct(ceiling, self_employed_rate) * weeks
expected:
  employee_weekly: 37.665
  employer_weekly: 53.865
  combined_annual: 4759.56
  self_employed_annual: 4338.36
```

### VAT Rates (as of 1 September 2025)

(Source: Inland Revenue VAT -- inlandrevenue.finance.gov.bs/value-added-tax/; Higgs & Johnson 2025 Tax Legislative Updates)

**VAT rates**  _(inlandrevenue.finance.gov.bs/value-added-tax/; Higgs & Johnson 2025 Tax Legislative Updates)_

| Category | Rate | Applies to |
| --- | --- | --- |
| Standard | **10%** | Most goods and services |
| Reduced | **5%** | Unprepared groceries, medications, medical supplies, baby/adult diapers, feminine hygiene products (effective 1 Sep 2025) |
| Zero | **0%** | Exports; certain financial services |
| Exempt | Exempt | Residential rent; certain education; certain financial products |

- **Sweets/gum/sodas rate change** — From 1 Sep 2025, sweets, chewing gum, and sodas were moved back to 10% (from prior reduced-rate treatment).  _(PM Davis announcement -- bahamas.gov.bs)_

### Business Licence Fee Schedule

(Source: Inland Revenue -- inlandrevenue.finance.gov.bs/tax-incentives/business-licence-new-rates-1/)

**Business Licence Fee Schedule**  _(inlandrevenue.finance.gov.bs/tax-incentives/business-licence-new-rates-1/)_

| Annual turnover | Licence tax |
| --- | --- |
| ≤ BSD 50,000 | BSD 100 flat fee |
| BSD 50,001 -- BSD 500,000 | 0.50% of turnover |
| BSD 500,001 -- BSD 5,000,000 | 0.75% of turnover |
| > BSD 5,000,000 | 1.25% of turnover |

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Client asks about domestic personal income tax | Record the tax and its return as inapplicable for the checked period |
| Unknown NIB registration status | STOP -- instruct client to register with NIB if self-employed and not yet registered |
| Unknown business turnover (VAT threshold) | Assume VAT registration required; escalate to confirm |
| Unknown property ownership | Skip RPT section; note it for reviewer |
| Unknown business-use % (vehicle, phone, home) | 0% deduction for Business Licence cost purposes |
| Unknown expense category (Business Licence deductibility) | Not deductible until confirmed |
| Client asks about capital gains on property | No CGT in Bahamas; stamp duty applies on conveyance |

### Required Inputs

**Minimum viable** -- client's employment status (employed / self-employed / both), approximate annual earnings or turnover, and confirmation they are resident in or operating from the Bahamas.

**Recommended** -- NIB registration number (nine-digit), whether a Business Licence has been obtained, VAT registration status and number if applicable, property ownership details for RPT, any recent real estate transactions for stamp duty.

**Ideal** -- NIB Smart Card, Business Licence certificate, VAT registration certificate, DIR taxpayer file number, complete annual turnover figure, payroll records (for employers), bank statements for the full year.

**Refusal if minimum is missing -- SOFT WARN.** If employment status is unknown, issue a hard stop: "Employment and self-employment status is required to determine NIB contribution rates and obligations. Please confirm before proceeding."

### Refusal Catalogue

- **R-BS-1** — For a domestic personal income tax computation, record the tax and its return as inapplicable for the checked period. Assess separate obligations for the person's circumstances.
- **R-BS-2** — "The Bahamas has no capital gains tax. If you are selling real estate, stamp duty applies on the conveyance -- see Section 6. If you are selling securities, no transfer taxes apply." (Capital gains computation requested.)
- **R-BS-3** — "There is no inheritance, estate, or gift tax in the Bahamas. Estate planning and probate costs are legal/probate fees, not taxes. Escalate to a Bahamian attorney for estate planning." (Inheritance or estate planning.)
- **R-BS-4** — For company tax, check whether the Domestic Minimum Top-Up Tax applies under ss 1, 4 and 5 of the Act. Check Business Licence, VAT and NIB separately. [Domestic Minimum Top-Up Tax Act, 2024](https://laws.bahamas.gov.bs/cms/images/LEGISLATION/PRINCIPAL/2024/2024-0058/2024-0058_1.pdf)
- **R-BS-5** — For a non-resident or expatriate, apply the domestic personal income tax position for the checked period and verify any foreign tax, separate reporting, social insurance and work permit obligations.
- **R-BS-6** — For NIB arrears or enforcement, obtain the Board's statement and refer the case for qualified review. See `bs-payroll-social` for the statutory interest and waiver provisions.
- **R-BS-7** — "From July 2025, businesses with less than 50% zero or reduced-rated supplies cannot claim VAT refunds. Escalate to a DIR-registered VAT practitioner." (VAT refund claims.)  _(Higgs & Johnson 2025 Tax Legislative Updates)_

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier for bank statement lines. When a transaction matches a pattern below, apply the treatment directly. If none match, fall through to Tier 1 rules in Section 5.

**How to read this table.** Match by case-insensitive substring on the counterparty name or description. If multiple patterns match, use the most specific. NIB obligations are the primary personal tax cost in the Bahamas; VAT is relevant only if the client is VAT-registered.

### 3.1 NIB-Related Transactions

**NIB-Related Transactions**

| Pattern | Classification | Treatment | Notes |
| --- | --- | --- | --- |
| NIB CONTRIBUTION, NIB PAYMENT, NATIONAL INSURANCE | NIB contribution | Self-employed: deductible cost of doing business | Employee share is not a tax -- it funds social benefits |
| NIB C10, C10 FORM | NIB employer payment | Employer's NIB liability | C10 = monthly employer contribution form |
| NIB SURCHARGE, NIB PENALTY, NIB INTEREST | NIB penalty | NOT deductible | Penalties are not a business expense |
| NIB BENEFIT, NIB SICKNESS, NIB MATERNITY | NIB benefit received | Exclude from income analysis | These are social benefit receipts, not business income |

### 3.2 Business Licence Transactions

**Business Licence Transactions**

| Pattern | Classification | Treatment | Notes |
| --- | --- | --- | --- |
| BUSINESS LICENCE, BL RENEWAL, INLAND REVENUE BL | Business Licence fee | Deductible operating expense | Annual compliance cost |
| BUSINESS LICENCE PENALTY, LATE BL FEE | Business Licence penalty | NOT deductible |  |
| DIR PAYMENT, INLAND REVENUE PAYMENT | Regulatory payment | Verify type: BL tax, VAT, or RPT | Classify by supporting reference |

### 3.3 VAT-Related Transactions (VAT-Registered Clients)

**VAT-Related Transactions**

| Pattern | Classification | Treatment | Notes |
| --- | --- | --- | --- |
| VAT PAYMENT, DIR VAT, VAT RETURN PAYMENT | VAT liability payment | EXCLUDE | VAT liability payment, not an expense |
| VAT REFUND, DIR VAT REFUND | VAT refund received | EXCLUDE | VAT asset recovery, not income |
| [Invoice line] + 10% VAT | Sales invoice | Extract net (excl. VAT) as revenue | VAT collected is not income |
| [Invoice line] + 5% VAT | Reduced-rate sale | Extract net (excl. VAT) as revenue | Essentials category at 5% |

### 3.4 Income Patterns (Credits)

**Income Patterns (Credits)**

| Pattern | Classification | Treatment | Notes |
| --- | --- | --- | --- |
| CLIENT PAYMENT, INVOICE PAYMENT, TRANSFER IN [client name] | Business revenue | Self-employment income | If VAT-registered, extract net |
| ZELLE, PAYPAL TRANSFER, STRIPE PAYOUT, WIRE TRANSFER | Business revenue | Self-employment income | Confirm invoices match |
| SALARY, PAYROLL [employer name], WAGES | Employment income | Bahamian personal income tax inapplicable | Check employer NIB |
| RENTAL INCOME, RENT RECEIVED | Rental income | Bahamian personal income tax inapplicable | Check Real Property Tax and Business Licence separately |
| BANK INTEREST, INTEREST EARNED | Investment income | Bahamian personal income tax inapplicable | Check foreign tax and reporting where relevant |
| GOVERNMENT GRANT, BAHAMAS INVEST GRANT | Check nature | Capital grants: exclude; revenue grants: include in Business Licence turnover |  |
| NIB BENEFIT, MATERNITY BENEFIT, RETIREMENT PENSION | Benefit payment | Exclude from business analysis | Social benefit, not taxable income |

### 3.5 Business Operating Expense Patterns (Debits) -- Deductible for Business Licence Purposes

**Business Operating Expense Patterns (Debits)**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| OFFICE RENT, COMMERCIAL RENT [address] | Office rent | Deductible | Dedicated business premises |
| ACCOUNTANT FEES, CPA FEES, BOOKKEEPING | Professional fees | Deductible |  |
| ATTORNEY, LAWYER, LEGAL FEES (business) | Legal fees | Deductible | Must be business-related |
| OFFICE SUPPLIES, STATIONERY, PAPER, PRINTER INK | Office supplies | Deductible |  |
| MARKETING, GOOGLE ADS, META ADS, FACEBOOK ADS | Marketing | Deductible |  |
| BUSINESS INSURANCE, PROFESSIONAL LIABILITY | Insurance | Deductible | Business-related only |
| DOMAIN, HOSTING, AWS, DIGITALOCEAN, CLOUDFLARE | IT infrastructure | Deductible (operating) | Recurring subscription = expense |
| GOOGLE WORKSPACE, MICROSOFT 365, QUICKBOOKS | Software subscription | Deductible | Recurring = expense |
| BANK FEE, SERVICE CHARGE, WIRE FEE (business account) | Bank charges | Deductible | Business account only |
| TRAINING, CPD, COURSE, SEMINAR | Training | Deductible | Must relate to current business |

### 3.6 Expense Patterns -- NOT Deductible

**Expense Patterns -- NOT Deductible**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| RESTAURANT, DINING, CLIENT MEAL, ENTERTAINMENT | Entertainment | NOT deductible | Personal/entertainment |
| PERSONAL WITHDRAWAL, DRAWINGS, ATM (personal) | Drawings | NOT deductible | Owner drawings |
| GROCERIES, SUPERMARKET, PERSONAL SHOPPING | Personal | NOT deductible |  |
| FINE, COURT FINE, TRAFFIC VIOLATION | Fines | NOT deductible | Public policy |
| INCOME TAX PAYMENT | Verify | Bahamian personal income tax is inapplicable | Confirm the tax, taxpayer and jurisdiction |

### 3.7 Exclusions (Neither Income nor Expense)

**Exclusions (Neither Income nor Expense)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| INTERNAL TRANSFER, OWN ACCOUNT | EXCLUDE | Between own accounts |
| LOAN REPAYMENT, MORTGAGE PRINCIPAL | EXCLUDE | Loan principal is not an expense |
| VAT PAYMENT, DIR VAT | EXCLUDE | VAT liability settlement |
| PROVISIONAL TAX, ADVANCE TAX | Verify | Confirm the tax, taxpayer and jurisdiction |
| STAMP DUTY PAYMENT | EXCLUDE from operating expenses | One-time property transaction cost, not recurring |

### 3.8 Bahamian Banks -- Statement Format Reference

**Bahamian Banks -- Statement Format Reference**

| Bank | Common Patterns | Notes |
| --- | --- | --- |
| Commonwealth Bank | TRANSFER, DD, PAYMENT, DEBIT CARD | Most common retail bank; PDF and online export |
| Bank of The Bahamas | TRANSFER, DIRECT DEBIT, DRAFT | Government-linked; PDF statements |
| Scotiabank Bahamas | PAYMENT, TFR, DD, CARD | Canadian bank; CSV available |
| FirstCaribbean (CIBC) | TRANSFER, PAYMENT, CHARGE | PDF; limited CSV |
| Fidelity Bank Bahamas | TRANSFER, WIRE, DEBIT | Business accounts common |
| Wise / Revolut Business | TRANSFER, CONVERSION, CARD PAYMENT | Clean CSV; multi-currency -- use BSD or USD amounts (1:1 peg) |

### Example 1 -- Employed Individual, Annual Salary BSD 45,000

**Scenario:** Maria is an ordinary employee paid weekly for 52 weeks in 2025. Annual basic salary BSD 45,000.

**Step 1 -- Personal income tax:** BSD 0. No personal income tax exists in the Bahamas.

**Step 2 -- NIB contributions:**
- Weekly salary: 45,000 ÷ 52 = BSD 865.38 -- ABOVE the weekly ceiling of BSD 810
- Insurable wage = ceiling: BSD 810/week
- Employee NIB before per-payroll rounding: 4.65% × BSD 810 × 52 = **BSD 1,958.58**
- Employer NIB before per-payroll rounding: 6.65% × BSD 810 × 52 = **BSD 2,800.98**
- Pay after the illustrated employee contribution: BSD 45,000 − BSD 1,958.58 = **BSD 43,041.42**

**Step 3 -- Filing scope:** The example concerns employment only. The Bahamian personal income tax return is inapplicable.

**Summary:**
```
Annual salary:            BSD 45,000
Less: Employee NIB:       BSD (1,958.58)
Pay after employee NIB:   BSD 43,041.42
Income tax:               BSD 0
```

### Example 2 -- Self-Employed Freelancer, Annual Revenue BSD 30,000

**Scenario:** James is a continuing self-employed web developer under 65 without retirement benefit in 2025. Current annual revenue is BSD 30,000. Assume qualifying prior-year self-employment income of BSD 30,000 and 52 equal contribution weeks for the NIB illustration.

**Step 1 -- Personal income tax:** BSD 0.

**Step 2 -- NIB contributions (self-employed rate 10.30%):**
- Illustrative weekly income is about BSD 576.92, below the BSD 810 ceiling.
- Annual NIB: 10.30% × BSD 30,000 = **BSD 3,090/year**
- For payment, reconcile the applicable contribution weeks and amount with NIB.

**Step 3 -- Business Licence:**
- Turnover ≤ BSD 50,000: flat fee **BSD 100**
- Renewal filing by 31 January; payment by 31 March

**Step 4 -- VAT:** BSD 30,000 < BSD 100,000 threshold. **No VAT registration required** (voluntary registration available).

**Step 5 -- No RPT** (renting; does not own property).

**Summary:**
```
Annual revenue:           BSD 30,000
NIB (10.30%):             BSD (3,090)
Business Licence fee:     BSD (100)
Income tax:               BSD 0
Balance before expenses:  BSD 26,810
```

### Example 3 -- Self-Employed at NIB Ceiling, BSD 60,000 Revenue

**Scenario:** Sandra is a continuing self-employed accountant under 65 without retirement benefit in 2025. Current annual revenue is BSD 60,000. Assume qualifying prior-year self-employment income of BSD 52,000 and 52 equal contribution weeks.

**Step 1 -- Personal income tax:** BSD 0.

**Step 2 -- NIB contributions:**
- Illustrative weekly income of BSD 1,000 exceeds the BSD 810 ceiling.
- Annual NIB: 10.30% × BSD 810 × 52 = **BSD 4,338.36**.

**Step 3 -- Business Licence:**
- Turnover BSD 60,000 (in band BSD 50,001 -- BSD 500,000): 0.50% × BSD 60,000 = **BSD 300**

**Step 4 -- VAT:** BSD 60,000 < BSD 100,000 threshold. Not required; may register voluntarily.

**Summary:**
```
Annual revenue:           BSD 60,000
NIB (at ceiling):         BSD (4,338.36)
Business Licence fee:     BSD (300)
Income tax:               BSD 0
Balance before expenses:  BSD 55,361.64
```

### Example 4 -- VAT-Registered Consultant, BSD 180,000 Revenue

**Scenario:** David is a continuing self-employed management consultant in 2025, with revenue BSD 180,000/year including VAT charged at 10%. VAT registered.

**Step 1 -- Revenue (net of VAT):**
- BSD 180,000 includes 10% VAT. Net revenue = BSD 180,000 ÷ 1.10 = **BSD 163,636**
- VAT collected = BSD 163,636 × 10% = BSD 16,364 (liability to DIR, not income)

**Step 2 -- Personal income tax:** BSD 0.

**Step 3 -- NIB:**
- Assume David is under 65 without retirement benefit and his qualifying prior-year income exceeds the weekly ceiling throughout 52 illustrative contribution weeks.
- NIB = 10.30% × BSD 810 × 52 = **BSD 4,338.36**.

**Step 4 -- Business Licence:**
- Turnover BSD 163,636 (band BSD 50,001 -- BSD 500,000): 0.50% × BSD 163,636 = **BSD 818**
- Certified turnover statement by accountant required (>BSD 100,000)

**Step 5 -- VAT obligations:**
- Quarterly VAT return (turnover ≤ BSD 5M)
- Due within 21 days of end of each quarter
- Pay net VAT (output VAT collected minus input VAT on business purchases)

**Summary:**
```
Gross revenue invoiced:   BSD 180,000
Less: VAT collected:      BSD (16,364)
Net business revenue:     BSD 163,636
NIB (at ceiling):         BSD (4,338.36)
Business Licence fee:     BSD (818)
Income tax:               BSD 0
```

### Example 5 -- Property Purchase, Stamp Duty Calculation

**Scenario:** Nicole purchases a residential property in Nassau for BSD 250,000.

**Step 1 -- Personal income tax on transaction:** BSD 0.

**Step 2 -- Stamp duty (graduated, shared 50/50 buyer/seller by default):**
- First BSD 20,000 at 4%: BSD 20,000 × 4% = BSD 800
- Next BSD 30,000 (BSD 20,001 -- BSD 50,000) at 6%: BSD 30,000 × 6% = BSD 1,800
- Next BSD 50,000 (BSD 50,001 -- BSD 100,000) at 8%: BSD 50,000 × 8% = BSD 4,000
- Remaining BSD 150,000 (above BSD 100,000) at 10%: BSD 150,000 × 10% = BSD 15,000
- **Total stamp duty: BSD 21,600**
- Nicole's share (buyer, 50%): **BSD 10,800**
- Seller's share (50%): **BSD 10,800**

*Arithmetic check: 800 + 1,800 + 4,000 + 15,000 = BSD 21,600 ✓*

**Step 3 -- First-time buyer exemption:** If Nicole is a first-time buyer purchasing a dwelling up to BSD 500,000, she is **exempt** from stamp duty. (Source: Churchill & Jones Realty stamp duty guide)

**Step 4 -- VAT provisional invoice (from July 2025):** Before executing conveyance, parties must obtain a provisional VAT invoice from DIR. (Source: Higgs & Johnson 2025 Tax Legislative Updates)

**Step 5 -- Payment deadline:** Stamp duty due **within 6 months** of transaction closing.

### Example 6 -- Employer Payroll NIB (3 Employees)

**Scenario:** Small business with 3 ordinary employees in 2025, each paid BSD 600 in insurable basic wages per week.

**NIB per employee per week:**
- Employee share: 4.65% × BSD 600 = BSD 27.90
- Employer share: 6.65% × BSD 600 = BSD 39.90
- Combined per employee: BSD 67.80/week

**C10 totals for all 3 employees**

| Mondays in month | Employee shares | Employer shares | Combined |
| --- | ---: | ---: | ---: |
| 4 | BSD 334.80 | BSD 478.80 | BSD 813.60 |
| 5 | BSD 418.50 | BSD 598.50 | BSD 1,017.00 |

The monthly statement counts the actual contribution weeks. The usual payment deadline is the 15th of the following month. [NIB C10(A) instructions, point 6](https://www.nib-bahamas.com/wp-content/uploads/2025/05/C10-A-INSTRUCTIONS-FOR-COMPLETING-C10-A-FORM-Revised-August-2015.pdf) · [Contributions Regulations, reg 26](https://laws.bahamas.gov.bs/cms/images/LEGISLATION/SUBORDINATE/1984/1984-0068/1984-0068_2.pdf)

```oa-check
name: BS C10 ordinary weekly payroll with four and five contribution weeks
inputs:
  insurable_wages: 600
  employees: 3
  employee_rate: 4.65
  employer_rate: 6.65
steps:
  - employee_weekly: pct(insurable_wages, employee_rate) * employees
  - employer_weekly: pct(insurable_wages, employer_rate) * employees
  - four_mondays_total: (employee_weekly + employer_weekly) * 4
  - five_mondays_total: (employee_weekly + employer_weekly) * 5
expected:
  employee_weekly: 83.70
  employer_weekly: 119.70
  four_mondays_total: 813.60
  five_mondays_total: 1017.00
```

### 5.1 The Fundamental Rule -- No Personal Income Tax

- **Domestic filing.** For the checked period, there is no Bahamian personal income tax return for employment or self-employment income. Apply the separate reporting rules for any business activity or foreign jurisdiction involved. [Ministry of Finance, Bahamas–Japan MAP guidance, ‘Scope of the MAP “Limitations”’](https://cdn.bahamas.gov.bs/tenant/tenantministryoffinance/documents/All%20Documents/BAHAMAS-JAPANMAPGUIDANCEDOCUMENT-20240718120503.pdf)

### 5.2 NIB Contribution Calculation Rules

Use `bs-payroll-social` to confirm the class, insurable wage or income, contribution period, ceiling and remittance. For ordinary continuing self-employment, use qualifying prior-year profit under reg 30 and the First Schedule. Gross turnover and current-period cash receipts belong to separate calculations. [Contributions Regulations, regs 2 and 30 and First Schedule](https://laws.bahamas.gov.bs/cms/images/LEGISLATION/SUBORDINATE/1984/1984-0068/1984-0068_2.pdf)

### 5.3 NIB Benefits Funded by Contributions

(Source: nib-bahamas.com/about-nib/benefits-and-assistance/)

Ten cash benefits are funded: Sickness, Maternity, Funeral, Retirement (Pensions), Invalidity, Survivorship, Unemployment, Industrial Injury, Disablement, and Death.

**NIB Benefits (2025)**  _(nib-bahamas.com/about-nib/benefits-and-assistance/)_

| Benefit (2025) | Amount |
| --- | --- |
| Minimum retirement pension | ~BSD 364/month |
| Maternity grant (from Jul 2025) | BSD 570 |
| Funeral benefit | BSD 2,060 (rising to BSD 2,100 from Jul 2026) |

- **Qualification for benefits** — To qualify for most benefits, the claimant must have accumulated sufficient contribution weeks. Contributions must be current (no arrears).

### 5.4 VAT: When It Applies to Individuals

- **VAT applicability** — VAT is relevant to individuals only if they are carrying on a business (self-employed, sole trader). Pure employees have no VAT obligation.
- **VAT registration threshold** — BSD 100,000 in annual taxable supplies. Must register within 14 days of becoming liable.  _(inlandrevenue.finance.gov.bs/value-added-tax/faqs/)_
- **Filing and payment** — General (turnover ≤ BSD 5M): quarterly return, due 21 days after end of quarter. Large taxpayer (turnover > BSD 5M): monthly return, due 14 days after end of month. E-commerce businesses, hotels, and vacation rental services: must register regardless of turnover.
- **Record-keeping** — Maintain accounting records for at least 5 years.  _(Inland Revenue VAT FAQs)_

### 5.5 Business Licence: Who Needs One

- **Who needs a licence** — Every person carrying on business in the Bahamas must hold a Business Licence -- including self-employed individuals and sole traders.  _(Inland Revenue Business Licence)_
- **Key deadlines** — New business: obtain licence before commencing operations. Annual renewal application: 31 January (for the current year). Licence tax payment: 31 March. Business cessation notification to DIR: within 14 days, no later than 31 December.
- **Financial statement requirements by turnover threshold** — > BSD 100,000: certified turnover statement by qualified accountant. BSD 250,000 -- BSD 5,000,000: review engagement report. > BSD 5,000,000: audited financial statements.  _(Inland Revenue Business Licence rates)_

### 5.6 Real Property Tax (RPT): Rules

- **RPT applicability** — RPT applies to owners of real property. Rates depend on classification.  _(inlandrevenue.finance.gov.bs/real-property-tax/faqs-rpt/)_

**Owner-Occupied Residential**  _(inlandrevenue.finance.gov.bs/real-property-tax/faqs-rpt/)_

| Assessed value | Rate |
| --- | --- |
| First BSD 300,000 | Exempt |
| BSD 300,001 -- BSD 500,000 | 0.625% |
| Above BSD 500,000 | 1.0% |
| Annual cap | BSD 150,000 |

**Residential (4 units or fewer, not owner-occupied)**  _(inlandrevenue.finance.gov.bs/real-property-tax/faqs-rpt/)_

| Assessed value | Rate |
| --- | --- |
| Up to BSD 75,000 | BSD 300 flat |
| Above BSD 75,000 | 0.625% |

**Commercial / 5+ units / Foreign-Owned Rentals**  _(inlandrevenue.finance.gov.bs/real-property-tax/faqs-rpt/)_

| Assessed value | Rate |
| --- | --- |
| First BSD 500,000 | 0.75% |
| BSD 500,001 -- BSD 2,000,000 | 1.0% |
| Above BSD 2,000,000 | 1.5% |
| Annual cap (from 2025 amendment) | BSD 150,000 |

**Vacant Land -- Foreign-Owned Only**  _(inlandrevenue.finance.gov.bs/real-property-tax/faqs-rpt/)_

| Assessed value | Rate |
| --- | --- |
| First BSD 7,000 | BSD 100 flat |
| Above BSD 7,000 | 2.0% |

- **RPT deadlines and discounts** — Annual payment deadline: 31 March. Early payment discount: 10% if paid by 31 March. Pensioner discount (Bahamian citizen, 65+): 50% off balance. Annual surcharge if unpaid by 31 December: 5% surcharge, plus 5% interest on outstanding amounts. Property declaration to DIR: by 31 December each year.

### 5.7 Stamp Duty on Real Estate Conveyances

**Stamp Duty on Real Estate Conveyances**  _(Churchill & Jones Realty stamp duty guide; Higgs & Johnson 2025 Tax Legislative Updates)_

| Consideration | Stamp duty rate |
| --- | --- |
| Up to BSD 20,000 | 4% |
| BSD 20,001 -- BSD 50,000 | 6% |
| BSD 50,001 -- BSD 100,000 | 8% |
| Above BSD 100,000 | 10% |

- **Split, exemption, and deadlines** — Normally split equally (50/50) between buyer and seller unless otherwise agreed. First-time buyer exemption: Exempt on a dwelling house or vacant land for a dwelling up to BSD 500,000. Stamp duty on mortgage instruments: approximately 1% of mortgage amount [RESEARCH GAP -- reviewer to confirm exact current rate]. Leases < 5 years: 2.5% of annual rent. Payment deadline: within 6 months of transaction closing. From 1 July 2025: Parties must obtain a provisional VAT invoice from DIR before executing conveyance instruments. Failure: 3% of consideration penalty (joint and several: transferor + agent).  _(Higgs & Johnson 2025 Tax Legislative Updates)_

### 5.8 Non-Deductible Items

**Non-Deductible Items**

| Item | Reason |
| --- | --- |
| Entertainment, client meals | Personal/entertainment; not wholly for business |
| Owner drawings | Not an expense |
| NIB surcharges and penalties | Penalties are not operating costs |
| Business Licence late penalties | Penalties |
| Personal living expenses | Not business-related |
| Court fines, traffic violations | Public policy |
| Income tax payments | Confirm the tax, taxpayer and jurisdiction before classifying |

### 6.1 Home Office Deduction (Business Licence Cost Basis)

There is no Bahamian personal income tax deduction for home-office costs. For the turnover-based Business Licence calculation in this guide, use the applicable turnover rules and track home-office costs separately for profitability.

For VAT-registered clients, the business-use proportion of home utilities may affect which input VAT is creditable.

**Flag for reviewer:** Confirm whether client's business address is home or commercial, and confirm what proportion of home expenses are genuinely attributable to the business. The Bahamas has no statutory guidance on this proportion -- reviewer must apply judgment.

**Conservative default:** 0% home office allocation until reviewer confirms.

### 6.2 Vehicle Business Use

Relevant for VAT input tax recovery (if VAT-registered) and for understanding true business costs.

- Client must document approximate business vs personal mileage
- No statutory mileage rate exists in the Bahamas [RESEARCH GAP -- reviewer to confirm any DIR guidance]

**Conservative default:** 0% business use until confirmed.

### 6.3 NIB Contribution Status Verification

Before advising a client, confirm:
- Are they registered with NIB? (nine-digit NIB number assigned on registration)
- Are contributions current? (check with NIB directly)
- Is the client voluntarily insured (if not employed or self-employed in the traditional sense)?

For arrears, verify the Board's statement and the applicable interest rate, dates and waiver with a qualified practitioner. [National Insurance Act, s 55](https://laws.bahamas.gov.bs/cms/images/LEGISLATION/PRINCIPAL/1972/1972-0021/1972-0021.pdf) · [Act 27 of 2024, s 6](https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2024/2024-0027A/2024-0027A.pdf)

### 6.4 VAT Input Tax Apportionment (Mixed-Use Businesses)

If a VAT-registered business makes both taxable and exempt supplies, input VAT must be apportioned. Partial exemption calculation:

- Standard method: proportion of taxable to total supplies (by value)
- From July 2025: businesses with < 50% zero/reduced-rated supplies cannot claim VAT refunds (Source: Higgs & Johnson 2025)

**Flag for reviewer:** Confirm supply mix and apportionment method for VAT-registered clients with exempt supplies.

### 6.5 Real Property Tax Assessment Disputes

The assessed value (used for RPT rate bands) is set by DIR and may differ from market value. A property owner may dispute the assessment.

**Flag for reviewer:** If client believes assessed value is overstated, escalate to a Bahamian real property attorney or appraiser before filing.

### 6.6 Business Licence Turnover Definition

The turnover figure used for Business Licence purposes is gross revenue (not net profit, not value-added). For VAT-registered businesses, confirm whether turnover is inclusive or exclusive of VAT for Business Licence computation purposes. [RESEARCH GAP -- reviewer to confirm whether DIR uses gross or VAT-exclusive turnover for Business Licence rate band computation]

## Section 7 -- Working Paper Template

```
BAHAMAS TAX COMPLIANCE -- WORKING PAPER
Tax Year: 2025
Client: ___________________________
Employment Status: Employed / Self-Employed / Both
NIB Number: ___________________________
VAT Registration Number (if applicable): ___________________________
Business Licence Number (if applicable): ___________________________

A. PERSONAL INCOME TAX
   A1. PIT due:    BSD 0 (no PIT in the Bahamas)
   A2. PIT return to file:    NONE

B. NIB CONTRIBUTIONS
   B1. Employment type:    Employed / Self-Employed / Voluntary
   B2. Class and insurable wage or self-employment income basis: ___________
   B3. Contribution weeks or months and applicable ceiling:    ___________
   B4. Insurable wages or income by period:    BSD ___________
   B5. Applicable rate by period and class:    ___%
   B6. Contribution for periods covered:    BSD ___________
   B7. Monthly statement total based on actual periods:    BSD ___________
   B8. Payment deadline and any exception:    ___________
   B9. Employer contributions for periods covered:    BSD ___________

C. BUSINESS LICENCE (Self-Employed / Sole Traders Only)
   C1. Annual gross turnover:    BSD ___________
   C2. Licence tax rate (from rate schedule):    ___%  or  BSD 100 flat
   C3. Annual licence tax:    BSD ___________
   C4. Renewal application filed by 31 January:    [ ]
   C5. Licence tax paid by 31 March:    [ ]
   C6. Financial statement requirement:
       [ ] > BSD 100k: certified turnover statement
       [ ] BSD 250k -- BSD 5M: review engagement report
       [ ] > BSD 5M: audited financial statements

D. VAT (VAT-Registered Clients Only)
   D1. VAT registration number:    ___________
   D2. Annual taxable supplies:    BSD ___________
   D3. Filing frequency: Quarterly (≤ BSD 5M) / Monthly (> BSD 5M):    ___________
   D4. Output VAT collected (period):    BSD ___________
   D5. Input VAT creditable (period):    BSD ___________
   D6. Net VAT due (D4 - D5):    BSD ___________
   D7. Return and payment due (21 days / 14 days after period end):    ___________

E. REAL PROPERTY TAX (Property Owners Only)
   E1. Property classification:    Owner-Occupied / Non-Owner-Occupied / Commercial / Vacant
   E2. Assessed value:    BSD ___________
   E3. RPT computed per rate table:    BSD ___________
   E4. Early payment discount (10% if paid by 31 March):    BSD ___________
   E5. Net RPT payable:    BSD ___________
   E6. Payment due: 31 March    [ ]
   E7. Property declaration to DIR by 31 December:    [ ]

F. STAMP DUTY (Real Estate Transactions Only)
   F1. Consideration (property value):    BSD ___________
   F2. Stamp duty (graduated per rate table):    BSD ___________
   F3. Client's share (typically 50%):    BSD ___________
   F4. First-time buyer exemption applies?    Yes / No
   F5. Provisional VAT invoice obtained from DIR?    [ ] (required from Jul 2025)
   F6. Payment due within 6 months of closing:    [ ]

REVIEWER FLAGS:
   [ ] NIB registration confirmed and contributions current?
   [ ] Employment / self-employment status confirmed?
   [ ] Business Licence obtained before operations commenced?
   [ ] VAT registration status confirmed (above/below BSD 100k threshold)?
   [ ] RPT assessed value verified?
   [ ] Any stamp duty transaction in period -- provisional VAT invoice obtained?
   [ ] No PIT return required -- confirmed with client?
   [ ] All T2 items flagged for reviewer?
```

### Bahamian Bank Statement Formats

**Bahamian Bank Statement Formats**

| Bank | Format | Key Fields | Notes |
| --- | --- | --- | --- |
| Commonwealth Bank (Bahamas) | PDF, online export | Date, Description, Debit, Credit, Balance | Most common retail bank; description contains counterparty |
| Bank of The Bahamas | PDF | Date, Particulars, Withdrawals, Deposits | Government-linked bank; less structured descriptions |
| Scotiabank Bahamas | PDF, CSV | Value Date, Description, Amount, Balance | Canadian multinational; clean CSV export |
| FirstCaribbean (CIBC) | PDF | Date, Description, Debit, Credit | Caribbean regional bank |
| Fidelity Bank Bahamas | PDF, CSV | Date, Description, Amount, Balance | Common for business accounts |
| Wise / Revolut Business | CSV | Date, Counterparty, Amount, Currency, Reference | Clean data; multi-currency; note BSD = USD (1:1 peg) |

### Key Bahamian Banking and Tax Terms

**Key Bahamian Banking and Tax Terms**

| Term | Meaning | Classification Hint |
| --- | --- | --- |
| C10 FORM | Monthly NIB employer contribution form | NIB payment -- business expense |
| R1 FORM | NIB self-employed / voluntary registration form | Registration, not a payment |
| DIR | Department of Inland Revenue | VAT / BL / RPT authority |
| NIB | National Insurance Board | Social contributions authority |
| BL | Business Licence | Annual licence fee |
| RPT | Real Property Tax | Annual property tax |
| STAMP DUTY | Conveyance tax | Property transaction tax |
| BSD / B$ | Bahamian Dollar | Pegged 1:1 to USD; treat as USD equivalent |
| WIRE / TT | Telegraphic Transfer / Wire | International payment -- check invoices |
| CONCH, WALK-IN PAYMENT | In-person DIR/NIB payment | Often for BL or RPT |
| NASSAU, FREEPORT | City references | No tax difference by island for NIB/BL/VAT |

### USD vs BSD Amounts

- **USD vs BSD equivalence** — The Bahamian Dollar is pegged 1:1 to the US Dollar and freely exchangeable. Bank statements may show USD amounts interchangeably. For all tax computations, treat BSD and USD as equivalent. Do not apply any currency conversion.

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3)
2. Mark all Tier 2 items as "PENDING -- reviewer must confirm"
3. Apply conservative defaults (Section 1)
4. Generate the working paper (Section 7) with clear flags
5. Confirm that Bahamian personal income tax and its return are inapplicable for the checked period. Identify any separate filing requirements.
6. Present the following questions to the client:

```
ONBOARDING QUESTIONS -- BAHAMAS TAX COMPLIANCE
1. Are you an employee, self-employed, or both?
2. What is your approximate annual gross income (or annual turnover if self-employed)?
3. Are you registered with the National Insurance Board (NIB)?
   If yes, what is your NIB number?
   If self-employed, do you pay your monthly NIB contributions by the 15th?
4. Do you hold a Business Licence?
   If yes, when is your renewal due and have you filed/paid for 2025?
5. Are you registered for VAT with the Department of Inland Revenue?
   If yes, what is your annual turnover?
6. Do you own any real property in the Bahamas?
   If yes, what classification (owner-occupied / rental / commercial)?
   Have you paid your 2025 Real Property Tax?
7. Did you buy or sell any real estate in 2025?
   If yes, has stamp duty been paid within 6 months of closing?
8. Do you employ any staff?
   If yes, are you filing C10 forms and paying NIB by the 15th monthly?
```

### Key Legislation and Authority References

**Key Legislation and Authority References**

| Topic | Reference / Authority |
| --- | --- |
| Domestic personal income tax scope | [Ministry of Finance, Bahamas–Japan MAP guidance, ‘Scope of the MAP “Limitations”’](https://cdn.bahamas.gov.bs/tenant/tenantministryoffinance/documents/All%20Documents/BAHAMAS-JAPANMAPGUIDANCEDOCUMENT-20240718120503.pdf) |
| NIB rates and worker classes | [S.I. 37 of 2024](https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2024/2024-0037S/2024-0037S.pdf) · [NIB rates sheet](https://www.nib-bahamas.com/UserFiles/HTMLEditor/Contribution-Rates-and-Insurable-Ceilings-2024.pdf) |
| NIB wage ceiling and review mechanism | [NIB July 2026 notice](https://www.nib-bahamas.com/uploads/2026_biennial_adjustments_f9ad1d917d.pdf) · [Contributions Regulations, reg 52](https://laws.bahamas.gov.bs/cms/images/LEGISLATION/SUBORDINATE/1984/1984-0068/1984-0068_2.pdf) |
| NIB registration (Form R1) | [NIB employer guidance](https://www.nib-bahamas.com/_m1758/Employers) |
| NIB employer statements | [C10(A) instructions](https://www.nib-bahamas.com/wp-content/uploads/2025/05/C10-A-INSTRUCTIONS-FOR-COMPLETING-C10-A-FORM-Revised-August-2015.pdf) · [NIB portals](https://www.nib-bahamas.com/portals) |
| VAT rates and administration | Inland Revenue -- inlandrevenue.finance.gov.bs/value-added-tax/about-vat/ |
| VAT reduced rate (5%, from Sep 2025) | PM Davis announcement -- bahamas.gov.bs; Higgs & Johnson 2025 |
| VAT registration thresholds | inlandrevenue.finance.gov.bs/value-added-tax/faqs/ |
| VAT penalties | inlandrevenue.finance.gov.bs/value-added-tax/fees-fines-and-penalties/ |
| Business Licence rates | inlandrevenue.finance.gov.bs/tax-incentives/business-licence-new-rates-1/ |
| Business Licence penalties | inlandrevenue.finance.gov.bs/business-licence/fees-fines-and-penalties-bl/ |
| Real Property Tax rates | inlandrevenue.finance.gov.bs/real-property-tax/faqs-rpt/ |
| RPT 2025 amendments (BSD 150k cap) | Real Property Tax Amendment Bill 2025 -- laws.bahamas.gov.bs |
| Stamp duty rates | Churchill & Jones Realty -- churchilljonesrealty.com/stamp-duties-taxes/ |
| Stamp duty + VAT invoice rule (Jul 2025) | Higgs & Johnson 2025 Tax Legislative Updates |
| Customs duties (general) | Bahamas Customs -- bahamascustoms.gov.bs |
| Minimum wage (BSD 6.50/hr from Jan 2023) | WageIndicator; Playroll Bahamas minimum wage guide |
| Procedural obligations overview | Higgs & Johnson -- higgsjohnson.com/principal-procedural-obligations-of-a-taxpayer-in-the-bahamas/ |

### Penalties Summary Table

**Penalties Summary Table**

| Obligation | Penalty |
| --- | --- |
| NIB arrears | Annual compound interest at the prime rate, subject to regulations and any other prescribed rate and date. Verify any waiver and the Board's calculation. [National Insurance Act, s 55](https://laws.bahamas.gov.bs/cms/images/LEGISLATION/PRINCIPAL/1972/1972-0021/1972-0021.pdf) · [Act 27 of 2024, s 6](https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2024/2024-0027A/2024-0027A.pdf) |
| VAT late filing | BSD 100 fixed + 10% of unpaid tax (Source: Inland Revenue VAT Fines) |
| VAT monthly interest | 1.5% per month on outstanding balance |
| VAT late registration | Retroactive back-tax + penalties imposed by DIR |
| Business Licence late application | BSD 100 (Source: inlandrevenue.finance.gov.bs/business-licence/fees-fines-and-penalties-bl/) |
| Business Licence late tax payment | 10% of tax liability |
| Business Licence interest (30+ days) | 5% per annum |
| RPT annual surcharge (unpaid by 31 Dec) | 5% surcharge + 5% interest |
| Stamp duty -- no provisional VAT invoice | 3% of consideration (joint/several: transferor + agent) (Source: Higgs & Johnson 2025) |
| Operating without Business Licence | Prosecution |

### Test Suite

**Test 1 -- Employee, salary at ceiling.**
Input: Ordinary employee paid BSD 950 weekly for 52 weeks in 2025.
Expected: BSD 810 weekly ceiling. Before per-payroll rounding, employee NIB is 4.65% × BSD 810 × 52 = BSD 1,958.58. Pay after this contribution is BSD 49,400 − BSD 1,958.58 = BSD 47,441.42.

**Test 2 -- Employee, salary below ceiling.**
Input: Ordinary employee paid BSD 500 in insurable basic wages weekly for 52 weeks in 2025.
Expected: Insurable wage = BSD 500/week. Employee NIB = 4.65% × BSD 500 = BSD 23.25/week = BSD 1,209/year. Employer NIB = 6.65% × BSD 500 = BSD 33.25/week = BSD 1,729/year. No income tax.

**Test 3 -- Self-employed, below ceiling.**
Input: Continuing self-employed person under 65 without retirement benefit, with BSD 25,000 in qualifying prior-year income, split evenly across 52 illustrative contribution weeks in 2025.
Expected: About BSD 480.77 per week, below the BSD 810 ceiling. The illustrative annual NIB total before payment rounding is 10.30% × BSD 25,000 = BSD 2,575.

**Test 4 -- Self-employed, above ceiling.**
Input: Continuing self-employed person under 65 without retirement benefit, with qualifying prior-year income above the weekly ceiling for all 52 illustrative contribution weeks in 2025.
Expected: Annual NIB = 10.30% × BSD 810 × 52 = BSD 4,338.36.

**Test 5 -- VAT registration threshold.**
Input: Self-employed, annual taxable supplies BSD 95,000.
Expected: Below BSD 100,000 threshold. VAT registration NOT required (but voluntary registration available). No VAT return to file.

**Test 6 -- Stamp duty, first-time buyer.**
Input: First-time buyer, purchasing a dwelling for BSD 400,000.
Expected: Normally stamp duty would be: BSD 800 (first BSD 20k) + BSD 1,800 (next BSD 30k) + BSD 4,000 (next BSD 50k) + BSD 30,000 (remaining BSD 300k at 10%) = BSD 36,600 total. BUT first-time buyer exemption applies (dwelling ≤ BSD 500k). Stamp duty = BSD 0.

**Test 7 -- Stamp duty, non-exempt buyer.**
Input: Second-property buyer, purchasing for BSD 75,000.
Expected: BSD 800 (4% × 20k) + BSD 1,800 (6% × 30k) + BSD 2,000 (8% × 25k) = BSD 4,600 total. Split equally: each party pays BSD 2,300.
*Arithmetic check: 20,000 × 4% = 800; 30,000 × 6% = 1,800; 25,000 × 8% = 2,000. Sum = BSD 4,600. Each party BSD 2,300 ✓*

**Test 8 -- No income tax return.**
Input: Any individual (employed or self-employed) asks if they need to file an income tax return in the Bahamas.
Expected: The Bahamian personal income tax return is inapplicable for the checked period. Verify separate obligations for the person's circumstances.

**Test 9 -- Employer NIB (C10 Form).**
Input: Employer with 2 ordinary weekly paid employees in 2025, each on BSD 700 in insurable basic wages per week.
Expected: Per employee per week, the employee share is BSD 32.55 and the employer share is BSD 46.55. Combined C10 total is BSD 632.80 for a 4-Monday month and BSD 791.00 for a 5-Monday month.

**Test 10 -- RPT, owner-occupied property.**
Input: Owner-occupied residential property, assessed value BSD 450,000.
Expected: First BSD 300,000 exempt. Next BSD 150,000 at 0.625%: BSD 150,000 × 0.625% = BSD 937.50. Total RPT = BSD 937.50. If paid by 31 March: 10% early-payment discount = BSD 93.75 saving; net BSD 843.75.

## PROHIBITIONS

- NEVER compute, estimate, or imply that the Bahamas levies personal income tax on individuals
- NEVER generate a Bahamian personal income tax return
- NEVER confuse NIB contributions (social insurance) with income tax -- they are separate systems with separate authorities
- NEVER skip NIB compliance guidance -- it is the primary individual tax obligation and penalties accumulate rapidly
- NEVER advise a self-employed client to start business without first addressing Business Licence and NIB registration
- NEVER allow entertainment expenses as deductible without reviewer confirmation
- NEVER omit the provisional VAT invoice warning for real estate transactions (required from July 2025)
- NEVER present these computations as definitive without reviewer sign-off -- always label as estimated
- NEVER confuse BSD (Bahamian Dollar) with a different currency -- it is pegged 1:1 to USD
- NEVER apply a stamp duty first-time buyer exemption without confirming it is a dwelling (not commercial) and consideration ≤ BSD 500,000

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
