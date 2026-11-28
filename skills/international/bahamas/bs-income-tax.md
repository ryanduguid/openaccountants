---
name: bs-income-tax
description: "Bahamas domestic personal income tax scope through 10 November 2026, with National Insurance, 2025 payroll examples and property rules from July 2026."
jurisdiction: BS
category: international
tax_year: 2025
tax_year_notes: "Personal income tax scope and the July 2026 National Insurance ceiling checked through 10 November 2026. Payroll examples use the 2025 schedule. Property examples apply rules effective from 1 July 2026."
last_updated: 2026-11-28
version: 0.5
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
| Client asks about a property sale | Check property transfer VAT, the relevant instrument and the date of supply under Section 5.7 |

### Required Inputs

**Minimum viable** -- client's employment status (employed / self-employed / both), approximate annual earnings or turnover, and confirmation they are resident in or operating from the Bahamas.

**Recommended** -- NIB registration number (nine-digit), whether a Business Licence has been obtained, VAT registration status and number if applicable, property ownership details for RPT, any recent real estate transfers, including the parties, instrument, consideration, fair market value and relevant dates.

**Ideal** -- NIB Smart Card, Business Licence certificate, VAT registration certificate, DIR taxpayer file number, complete annual turnover figure, payroll records (for employers), bank statements for the full year.

**Refusal if minimum is missing -- SOFT WARN.** If employment status is unknown, issue a hard stop: "Employment and self-employment status is required to determine NIB contribution rates and obligations. Please confirm before proceeding."

### Refusal Catalogue

- **R-BS-1** — For a domestic personal income tax computation, record the tax and its return as inapplicable for the checked period. Assess separate obligations for the person's circumstances.
- **R-BS-2** — "The Bahamas has no general personal capital gains tax. For a property transfer, check VAT and stamp duty under Section 5.7. For securities, check the entity and its assets before concluding whether a transfer tax applies." (Capital gains computation requested.) [Bahamas Government investment guide][bs-investment-guide]
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
| VAT STAMP, PROPERTY VAT PAYMENT | Review with the conveyance, assessment and payment receipt | Identify the property transaction and confirm the accounting treatment and any VAT recovery separately |
| STAMP DUTY PAYMENT | Review the instrument and payment receipt | Identify the chargeable instrument, including the non-land portion of a business sale under section 23. See Section 5.7. |

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

### Example 5 -- VAT on a Property Purchase

Nicole, a Bahamian citizen, buys her second home in Nassau in August 2026. The consideration and fair market value are both BSD 250,000. Assume a direct sale with no special relief.

The ordinary Bahamian individual rate is 4% on the full BSD 250,000. Estimated transfer VAT is **BSD 10,000**. The conveyance deed qualifies for the stamp duty exemption. The parties are jointly and severally liable for VAT. Use the agreement to establish who bears the cost between them. [VAT Act, Third Schedule item 2][bs-vat-act] · [Property VAT Rules, rules 4 and 10][bs-property-vat-rules] · [Stamp Act, Second Schedule item 21][bs-stamp-act]

Obtain the provisional VAT invoice before execution. If execution is the first event establishing supply, the ordinary payment window runs for 180 calendar days from execution. Check payment exceptions and the separate deed registration clock under Section 5.7. [Conveyancing Acts 54 of 2025][bs-conveyance-2025] and [29 of 2026][bs-conveyance-2026] · [Property VAT Rules, rules 3–4][bs-property-vat-rules]

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

### 5.6 Real Property Tax (RPT)

Use the Department of Inland Revenue assessment, the applicable year, the ownership and the use of each unit. The following classifications and rates reflect the law from 1 July 2026. Confirm how the July amendments affect an assessment issued under earlier rules. [Real Property Tax Act, ss 2–3 and 7][bs-rpt-act] · [Act 22 of 2022, ss 3 and 10][bs-rpt-2022] · [Act 21 of 2026, ss 1–4][bs-rpt-2026]

| Class | Annual tax |
| --- | --- |
| Owner-occupied | First BSD 300,000 exempt, 0.625% on the part above BSD 300,000 up to BSD 500,000 and 1% on the excess. Annual cap BSD 150,000. |
| Foreign owner-occupied | 0.625% on the first BSD 1 million and 1% on the excess. Annual cap BSD 200,000. |
| Residential | BSD 300 if value is at most BSD 75,000. Above BSD 75,000, 0.625% on the whole value. [Act 16 of 2020, s 2][bs-rpt-2020] |
| Commercial | 0.75% on the first BSD 500,000, 1% on the part above BSD 500,000 up to BSD 2 million and 1.5% on the excess. |
| Taxable unimproved property | BSD 100 on the first BSD 7,000 and 2% on the excess. [Real Property Tax Act, s 3(2)(b)][bs-rpt-act] · [Act 13 of 2018, s 3][bs-rpt-2018] |

For owner-occupied treatment, verify the qualifying Bahamian or permanent residence status with the right to work and the ownership and exclusive permanent or seasonal dwelling use conditions. The separate foreign owner-occupied class applies to a qualifying non-Bahamian with a residence permit, annual work permit or Home Owner Resident Permit who owns in fee simple or is a mortgagor in possession and occupies the property exclusively as a permanent or seasonal dwelling. For property held through a company, check section 3(8), including exclusive dwelling use and the declaration by the beneficial owner of more than 50% of the shares. Apply the single-residence restriction in section 3(8A) when a person or spouses have separate residences. [Act 22 of 2022, s 3][bs-rpt-2022] · [Act 21 of 2026, s 2][bs-rpt-2026]

The residential class covers up to 4 units, excluding outbuildings, used solely as dwellings outside either owner-occupied class. The beneficial owner must be a Bahamian citizen or registered for VAT to operate the property as a commercial rental establishment. Check the rule that treats each dwelling as commercial where a person owns more than 4 non-owner-occupied dwellings. [Act 22 of 2022, s 2][bs-rpt-2022] · [Act 21 of 2026, s 2][bs-rpt-2026]

For a Crown-Leased Cay, verify the separate assessment and rate under section 3(2)(d). [Real Property Tax Act, ss 2–3][bs-rpt-act]

The new proviso in section 3(2)(bb) applies owner-occupied rates to a unit classified under section 3(8B) and caps the aggregate annual tax for the other units at BSD 300,000. The proviso refers to duplexes, triplexes and fourplexes. Confirm whether a fourplex qualifies because section 3(8B) refers to qualifying duplexes and triplexes. Where co-owners fall into different statutory categories, rates or exemptions, section 3A allocates the assessed value in equal shares and applies the appropriate treatment separately to each share. [Act 14 of 2023, s 2][bs-rpt-2023] · [Act 21 of 2026, ss 3–4][bs-rpt-2026]

- **Unimproved land.** Check the exemption for unimproved property owned by Bahamians and the conditions in section 42. Property under construction can fall in the unimproved class before occupancy or issue of the occupancy certificate. Property used for business activity falls outside the unimproved class. [Real Property Tax Act, s 42][bs-rpt-act] · [Act 22 of 2022, ss 2 and 10][bs-rpt-2022]
- **Annual payment.** The section 18 due date is 31 March for the tax year starting 1 January, subject to the statutory qualifications. Section 20B deducts 10% of the tax due when the tax and any related surcharge are paid in full by 31 March. Section 18(2) protects amounts paid by 31 December of the same tax year from surcharge. Confirm the due date and any written extension against the assessment. [Real Property Tax Act, s 20B][bs-rpt-act] · [Act 22 of 2022, s 7][bs-rpt-2022]
- **Change of use.** An owner must file a return within 14 days if property classified as owner-occupied changes from sole use as the owner's dwelling. Give the date and details of the change. [Act 17 of 2021, s 3][bs-rpt-2021]
- **Evidence to confirm before applying special treatment.** Check relevant exemptions, nonstandard assessments, property declarations and current filing procedures. For pensioner relief, section 20A provides a 50% reduction of eligible tax after the owner-occupied exemption, limited to tax on the first BSD 1 million of assessed value. Check citizenship, retirement benefit or age 65, beneficial ownership, occupation, proof and the prescribed declaration. Confirm the interaction with other relief before calculating. [Real Property Tax Act, ss 5, 10, 20A and 42][bs-rpt-act] · [DIR forms][bs-rpt-forms]

### 5.7 VAT and Stamp Duty on Property Transfers

A deed conveying or otherwise transferring realty within item 21 of the Stamp Act Second Schedule is exempt from stamp duty from 1 July 2024. Check any presentation requirements under section 3. A taxable real property transfer generally attracts VAT. For an ordinary purchase, use the higher of consideration and fair market value under rule 10(1). Select the applicable Third Schedule item using the transaction and transferee details. [Stamp Act, ss 1 and 3 and Second Schedule item 21][bs-stamp-act] · [VAT Act, Third Schedule][bs-vat-act] · [Property VAT Rules, rule 10][bs-property-vat-rules]

**Ordinary purchase by a Bahamian individual under Third Schedule item 2.** Apply the rate to the whole taxable value.

| Taxable value (BSD) | VAT rate |
| --- | --- |
| Up to 100,000 | 2.5% |
| Over 100,000 to 300,000 | 4% |
| Over 300,000 to 500,000 | 6% |
| Over 500,000 to 700,000 | 8% |
| Over 700,000 to 1 million | 9% |
| Over 1 million | 10% |

Item 2 extends to specified holding companies. Check its conditions before using those rates for a company. Item 1 generally provides 2.5% up to BSD 100,000 and 10% above that for a Bahamian company or other qualifying Bahamian entity within that item. Item 3A specifies 10% for a foreign person. [VAT Act, s 2 and Third Schedule items 1, 2 and 3A][bs-vat-act]

**First home.** An eligible Bahamian citizen can obtain zero-rating on the acquisition of a first dwelling valued at up to BSD 300,000, subject to the Rules and Comptroller approval. The separate zero-rating for qualifying financing uses a BSD 500,000 ceiling. From 1 July 2026, a qualifying first-home acquisition over BSD 300,000 and up to BSD 600,000 attracts 4% on the whole taxable value under Third Schedule item 3. Check the transaction type and approval before applying any relief. [VAT Act, First Schedule item 9(d) and Third Schedule item 3][bs-vat-act] · [Act 19 of 2026, ss 1 and 5][bs-vat-2026] · [Property VAT Rules, rule 9][bs-property-vat-rules]

**Invoice, payment and registration.** From 1 July 2026, section 40 requires a provisional invoice from the VAT Comptroller before executing a conveyance. Under rules 3 and 4, VAT is due on the earliest of execution, completion and substantial performance. Ordinarily pay in full within 180 calendar days of supply, subject to VAT Act section 32(16) and the rule 4(3) reporting treatment for a registrant making a supply in its taxable activity. Parties are jointly and severally liable under rule 4(8). Section 40(4) separately requires submission of the deed for registration within 180 calendar days of execution. Confirm the current invoice and registration procedures with DIR and the conveyancer. [Conveyancing Acts 54 of 2025][bs-conveyance-2025] and [29 of 2026][bs-conveyance-2026] · [Property VAT Rules, rules 3–4][bs-property-vat-rules] · [DIR provisional invoice guidance][bs-dir-invoice] · [DIR VAT Stamp portal][bs-dir-property]

The DIR VAT forms index links to the VAT Invoice for Conveyance Request Form listed in July 2025. An individual or agent can start the request with the property, parties and purchase terms. Confirm the currency before entering the price because the label and currency indicator differ. Obtain the provisional invoice before execution. Use it to estimate VAT. Pay the VAT that DIR assesses after reviewing the conveyance documents. The assessed amount can differ from the estimate. [DIR VAT forms][bs-dir-vat-forms] · [DIR provisional invoice guidance][bs-dir-invoice]

The invoice request form excludes applicants requiring a First Home VAT concession or another exemption and directs them to the First Home Exemption Portal. Its buyer checkbox records an existing first-home approval. Confirm the current acquisition approval process and the route for other exemptions with DIR. [DIR VAT forms][bs-dir-vat-forms]

Under section 40(3), the parties and their attorneys, real estate agents and brokers are jointly and severally responsible for ensuring payment and must report any known non-compliance immediately in writing to the VAT Comptroller. Sections 40(5)–(6) require verification that the Comptroller issued the provisional invoice before disbursing or completing a loan, mortgage or refinancing to facilitate the purchase or development. Contravention is an offence and carries a penalty equal to the unpaid VAT on the conveyance. [Conveyancing Act 54 of 2025, s 3][bs-conveyance-2025] · [Act 29 of 2026, ss 1 and 3][bs-conveyance-2026]

**Payment priority.** From 1 July 2025, conveyance VAT ranks equally with RPT levied on the same property and ahead of security interests, proprietary rights and other claims affecting it. The Comptroller may assess VAT on a supply of real property at any time. Assessed VAT takes priority over fees, commissions and other amounts payable in respect of the supply. If those amounts are paid first, each recipient is jointly and severally liable up to the lesser of the payment received and the unpaid VAT assessed on that supply. Check both priority rules before releasing funds. [Conveyancing Act 54 of 2025, ss 1 and 3][bs-conveyance-2025] · [VAT Act 45 of 2025, ss 1 and 17][bs-vat-2025]

**Property declarations.** From 1 July 2025, section 47C requires the transferor of a direct or indirect beneficial interest in real property to file a prescribed declaration with the Comptroller within 30 days after execution of the instrument or arrangement. If the transferor engages a real estate agent for the conveyance, that agent must file on the transferor's behalf. If the agent fails to file on time, the agent and transferor are jointly and severally liable for a penalty of 3% of the consideration paid or payable. Indirect transfers can include a change of control or enjoyment through a trust, nominee or company. [VAT Act 45 of 2025, ss 1 and 11][bs-vat-2025]

Use the Prescribed Declaration Form 47C linked in the DIR VAT forms index. The form asks whether the filer is the transferor or the real estate agent filing on the transferor's behalf. Prepare the party and property details, consideration and the description of how the beneficial interest moved. Calculate the deadline from execution of the instrument or arrangement under the Act. Retain evidence of lodgement. [DIR VAT forms][bs-dir-vat-forms]

Under section 47B a company covered by that section must notify its registered agent, or the Registrar General if it has no registered agent, within 15 days of acquiring or disposing of an interest in real property. For companies registered under the Companies Act or International Business Companies Act, the registered agent or Registrar General, as applicable, files the annual declaration with the Comptroller by 31 January for the prior year under the amendment effective 1 July 2025. Check the required property interests and share ownership changes under section 47B(3). DIR links to a registered-agent online form for the 2025 reporting year. Confirm the form for the applicable year and the Registrar General's process where the company has no agent. [VAT Act, s 47B][bs-vat-act] · [VAT Act 45 of 2025, ss 1 and 10][bs-vat-2025] · [DIR VAT forms][bs-dir-vat-forms]

**Other instruments and transfers.** Check the VAT and Stamp Act treatment separately for share sales involving entities with Bahamian property or business interests, business sales, mortgages, leases and transactions involving gifts or trusts. Section 23 of the Stamp Act addresses sales of businesses. The July 2026 amendment changes the stamp duty treatment of the portion involving property other than land. Confirm the relevant rates, exemptions and filing procedures before estimating these cases. [VAT Act, Third Schedule][bs-vat-act] · [Stamp Act, ss 23–27 and Second Schedule item 26][bs-stamp-act] · [Act 18 of 2026, s 3][bs-stamp-2026]

**Acquisitions by non-Bahamians.** Check whether sections 2–4 require registration with the Investments Board or a permit before acquisition. Record the required certificate or permit with the acquisition documents. Section 10A can cause a permit to expire 180 days from grant if the holder fails to submit the acquisition instrument for VAT, pay that VAT, make the requisite property return and pay RPT as assessed. Section 10B provides an extension subject to notice, fee and timing conditions. Check the permit clock separately from the VAT clock. Confirm the procedure for any exception, registration, expiry or extension with the conveyancer. [International Persons Landholding Act, ss 2–4][bs-landholding-act] · [Acts 24 of 2024, ss 2–3][bs-landholding-2024] and [50 of 2025, ss 2–3][bs-landholding-2025]

From 1 July 2026, a qualifying certificate holder can apply to the Director of Immigration for the annual Home Owner Resident Permit. The permit is distinct from the acquisition permit and the RPT classification. [Act 27 of 2026, ss 1–3][bs-landholding-2026]

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

From 1 July 2026, lodge an objection with the Chief Valuation Officer within 30 calendar days after service of the assessment notice. Use the prescribed written form and state the grounds in detail. For an objection to the assessment of tax, pay the full assessed tax or provide acceptable security when lodging. The Chief Valuation Officer can relieve that requirement for good cause, subject to conditions. The statute allows late objections in specified circumstances. [Act 21 of 2026, s 7][bs-rpt-2026]

An appeal against a served objection decision ordinarily has a 30-calendar-day deadline after service. For an objection on which the officer has yet to serve a decision after 180 days from lodging, section 12(3) provides a separate route to the Tax Appeal Commission. Confirm the applicable filing deadline for that case. The Commission Act prescribes a notice of appeal and conditions for the Commission to hear and determine assessment appeals. Check the current filing process, certification, payment or security arrangements and the waiver route for an eligible individual. [Act 21 of 2026, s 8][bs-rpt-2026] · [Tax Appeal Commission Act, ss 5–8 and 11][bs-commission-act] · [Act 24 of 2026, s 2][bs-commission-2026]

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
   E1. Property class and assessment year:    ___________
   E2. Assessed value:    BSD ___________
   E3. RPT computed per applicable rate:    BSD ___________
   E4. Verified relief or s 20B reduction:    BSD ___________
   E5. Net RPT payable:    BSD ___________
   E6. Payment and declaration dates checked:    [ ]

F. PROPERTY TRANSFER VAT (Real Estate Transactions Only)
   F1. Consideration and fair market value:    BSD ___________ / BSD ___________
   F2. Applicable transferee class, rate and relief:    ___________
   F3. Estimated VAT and contractual allocation:    BSD ___________ / ___________
   F4. Provisional VAT invoice obtained before execution?    [ ]
       Invoice verified before any loan, mortgage or refinancing disbursement or completion?    [ ]
   F5. Date of supply and VAT payment deadline:    ___________ / ___________
   F6. Deed execution and registration deadline:    ___________ / ___________
   F7. VAT and RPT priority checked before paying claims, fees or commissions?    [ ]
   F8. 30-day beneficial interest declaration due date and filer:    ___________ / ___________
   F9. Company 15-day notice and annual declaration dates and filers:    ___________

REVIEWER FLAGS:
   [ ] NIB registration confirmed and contributions current?
   [ ] Employment / self-employment status confirmed?
   [ ] Business Licence obtained before operations commenced?
   [ ] VAT registration status confirmed (above/below BSD 100k threshold)?
   [ ] RPT assessed value verified?
   [ ] Property transfer VAT assessed, provisional invoice checked and deadlines documented?
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
| VAT STAMP | DIR property transaction VAT assessment or payment reference | Match to the relevant instrument and receipt |
| STAMP DUTY PAYMENT | Instrument-specific stamp duty payment | Check the instrument, statutory charge and receipt |
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
   What year does the assessment cover, and has it been paid?
7. Did you buy or sell real estate in the period?
   If yes, collect the invoice, payment evidence and the execution and supply dates.
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
| Annual property tax | [Real Property Tax Act][bs-rpt-act] · [Acts 13 of 2018][bs-rpt-2018], [15 of 2019][bs-rpt-2019], [16 of 2020][bs-rpt-2020], [17 of 2021][bs-rpt-2021], [22 of 2022][bs-rpt-2022], [14 of 2023][bs-rpt-2023], [16 of 2024][bs-rpt-2024] and [21 of 2026][bs-rpt-2026] |
| Property transfer VAT and conveyancing | [VAT Act][bs-vat-act] · [Act 19 of 2026][bs-vat-2026] · [Property VAT Rules][bs-property-vat-rules] · [Conveyancing Acts 54 of 2025][bs-conveyance-2025] and [29 of 2026][bs-conveyance-2026] |
| Stamp duty on instruments | [Stamp Act 22 of 2024][bs-stamp-act] · [Act 18 of 2026][bs-stamp-2026] |
| Customs duties (general) | Bahamas Customs -- bahamascustoms.gov.bs |
| Minimum wage (BSD 6.50/hr from Jan 2023) | WageIndicator; Playroll Bahamas minimum wage guide |
| Procedural obligations overview | Higgs & Johnson -- higgsjohnson.com/principal-procedural-obligations-of-a-taxpayer-in-the-bahamas/ |

### Penalties Summary Table

**Penalties Summary Table**

| Obligation | Penalty |
| --- | --- |
| NIB arrears | Annual compound interest at the prime rate, subject to regulations and any other prescribed rate and date. Verify any waiver and the Board's calculation. [National Insurance Act, s 55](https://laws.bahamas.gov.bs/cms/images/LEGISLATION/PRINCIPAL/1972/1972-0021/1972-0021.pdf) · [Act 27 of 2024, s 6](https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2024/2024-0027A/2024-0027A.pdf) |
| VAT late filing | BSD 100 fixed + 10% of unpaid tax (Source: Inland Revenue VAT Fines) |
| VAT late interest | From 1 July 2025, section 47A(4) applies prime plus 1% to outstanding tax after its due date. For real property, section 47A(4A) starts interest liability 21 days after the tax becomes due and payable. Verify the applicable prime rate and calculation. [Act 45 of 2025, ss 1 and 9][bs-vat-2025] · [S.I. 37 of 2025, rule 2][bs-property-vat-2025] |
| VAT late registration | Retroactive back-tax + penalties imposed by DIR |
| Business Licence late application | BSD 100 (Source: inlandrevenue.finance.gov.bs/business-licence/fees-fines-and-penalties-bl/) |
| Business Licence late tax payment | 10% of tax liability |
| Business Licence interest (30+ days) | 5% per annum |
| RPT surcharge, from 1 July 2024 | Subject to section 18, 5% per year for most property. For unimproved property owned by a non-Bahamian, 5% in the first year outstanding, 7.5% in the second and 12% in the third and later years. [Act 16 of 2024, s 3][bs-rpt-2024] · [Act 22 of 2022, s 7][bs-rpt-2022] |
| Property transfer VAT, late submission or payment | Under section 38D as amended from 1 December 2024, the recipient is liable to a fine. For property valued at BSD 300,000 or less, the fine is 10% of tax owed. Above BSD 300,000 the fine is 10% if the instrument is submitted and VAT is paid within 6 months after their respective prescribed deadlines, and 15% if either exceeds that window. Verify late interest separately. [VAT Act, s 38D][bs-vat-act] · [Act 18 of 2024, ss 1 and 7][bs-vat-2024] |

Refer potential false statements on property transfers to the reviewer for separate consideration under section 38K. [VAT Act 45 of 2025, ss 1 and 8][bs-vat-2025]
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

**Test 6 -- Transfer VAT, qualifying first-home buyer.**
Input: Bahamian citizen buys a first dwelling in August 2026, with consideration and fair market value both BSD 400,000. The purchase qualifies for the first-home rate.
Expected: BSD 400,000 × 4% = BSD 16,000 estimated acquisition VAT. Assess any financing relief separately.

Boundary checks under Section 5.7. An approved first-home acquisition at BSD 300,000 is zero-rated. A qualifying acquisition at BSD 600,000 attracts BSD 600,000 × 4% = BSD 24,000. Each amount is the higher of consideration and fair market value.

**Test 7 -- Transfer VAT, second home.**
Input: Bahamian citizen purchases a second dwelling in August 2026, with consideration and fair market value both BSD 75,000. No special relief applies.
Expected: BSD 75,000 × 2.5% = BSD 1,875 estimated transfer VAT. The parties are jointly and severally liable.

Late fine boundaries under section 38D. For property valued at BSD 300,000, the fine is 10% of tax owed even if a deadline is missed by more than 6 months. At BSD 300,001, the fine is 10% if both submission and payment take place within 6 months of their respective deadlines, and 15% if either occurs after its 6-month window. Check interest separately.

**Test 8 -- No income tax return.**
Input: Any individual (employed or self-employed) asks if they need to file an income tax return in the Bahamas.
Expected: The Bahamian personal income tax return is inapplicable for the checked period. Verify separate obligations for the person's circumstances.

**Test 9 -- Employer NIB (C10 Form).**
Input: Employer with 2 ordinary weekly paid employees in 2025, each on BSD 700 in insurable basic wages per week.
Expected: Per employee per week, the employee share is BSD 32.55 and the employer share is BSD 46.55. Combined C10 total is BSD 632.80 for a 4-Monday month and BSD 791.00 for a 5-Monday month.

**Test 10 -- RPT, owner-occupied property.**
Input: Qualifying owner-occupied property under the rules from 1 July 2026, assessed value BSD 450,000. Assume no additional relief or surcharge.
Expected: First BSD 300,000 exempt. BSD 150,000 × 0.625% = BSD 937.50 estimated RPT. If the conditions in section 20B are met, the BSD 93.75 reduction gives BSD 843.75 payable.

Residential boundary under Section 5.6. A separate qualifying residential property assessed at BSD 75,000 incurs BSD 300 before any relief. At BSD 75,200 the tax is BSD 75,200 × 0.625% = BSD 470 before any relief.

## PROHIBITIONS

- NEVER compute, estimate, or imply that the Bahamas levies personal income tax on individuals
- NEVER generate a Bahamian personal income tax return
- NEVER confuse NIB contributions (social insurance) with income tax -- they are separate systems with separate authorities
- NEVER skip NIB compliance guidance -- it is the primary individual tax obligation and penalties accumulate rapidly
- NEVER advise a self-employed client to start business without first addressing Business Licence and NIB registration
- NEVER allow entertainment expenses as deductible without reviewer confirmation
- NEVER use the deed registration clock to determine the VAT payment deadline
- NEVER present these computations as definitive without reviewer sign-off -- always label as estimated
- NEVER confuse BSD (Bahamian Dollar) with a different currency -- it is pegged 1:1 to USD
- NEVER use the first-home financing ceiling to determine the acquisition rate

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

[bs-rpt-act]: https://laws.bahamas.gov.bs/cms/images/LEGISLATION/PRINCIPAL/1969/1969-0023/1969-0023_2.pdf
[bs-rpt-2018]: https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2018/2018-0013/2018-0013.pdf
[bs-rpt-2019]: https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2019/2019-0015/2019-0015.pdf
[bs-rpt-2020]: https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2020/2020-0016/2020-0016.pdf
[bs-rpt-2021]: https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2021/2021-0017/2021-0017.pdf
[bs-rpt-2022]: https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2022/2022-0022/2022-0022.pdf
[bs-rpt-2023]: https://inlandrevenue.finance.gov.bs/wp-content/uploads/2023/07/Real-Property-Tax-Amendment-Act-2023.pdf
[bs-rpt-2024]: https://inlandrevenue.finance.gov.bs/wp-content/uploads/2024/08/Real-Property-Tax-Amendment-Act-2024.pdf
[bs-rpt-2026]: https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2026/2026-0021A/2026-0021A.pdf
[bs-rpt-forms]: https://inlandrevenue.finance.gov.bs/real-property-tax/forms-rpt/
[bs-vat-act]: https://inlandrevenue.finance.gov.bs/wp-content/uploads/2024/11/Value-Added-Tax-Act.pdf
[bs-vat-2024]: https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2024/2024-0018A/2024-0018A.pdf
[bs-vat-2025]: https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2025/2025-0045A/2025-0045A.pdf
[bs-vat-2026]: https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2026/2026-0019A/2026-0019A.pdf
[bs-property-vat-rules]: https://inlandrevenue.finance.gov.bs/wp-content/uploads/2023/06/Extraordinary_Gazette_17th_March_2023.pdf#page=5
[bs-property-vat-2025]: https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2025/2025-0037S/2025-0037S.pdf
[bs-conveyance-2025]: https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2025/2025-0054A/2025-0054A.pdf
[bs-conveyance-2026]: https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2026/2026-0029A/2026-0029A.pdf
[bs-dir-invoice]: https://inlandrevenue.finance.gov.bs/guidance-note-20-requirement-for-provisional-vat-invoice-now-available/
[bs-dir-property]: https://inlandrevenue.finance.gov.bs/other/vat-stamp/
[bs-dir-vat-forms]: https://inlandrevenue.finance.gov.bs/value-added-tax/forms/
[bs-stamp-act]: https://laws.bahamas.gov.bs/cms/images/LEGISLATION/PRINCIPAL/2024/2024-0022/2024-0022_1.pdf
[bs-landholding-act]: https://laws.bahamas.gov.bs/cms/images/LEGISLATION/PRINCIPAL/1993/1993-0041/1993-0041.pdf
[bs-landholding-2024]: https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2024/2024-0024A/2024-0024A.pdf
[bs-landholding-2025]: https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2025/2025-0050A/2025-0050A.pdf
[bs-landholding-2026]: https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2026/2026-0027A/2026-0027A.pdf
[bs-commission-act]: https://laws.bahamas.gov.bs/cms/images/LEGISLATION/PRINCIPAL/2020/2020-0003/2020-0003.pdf
[bs-commission-2026]: https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2026/2026-0024A/2026-0024A.pdf
[bs-stamp-2026]: https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2026/2026-0018A/2026-0018A.pdf
[bs-investment-guide]: https://cdn.bahamas.gov.bs/tenant/tenanttgotb/documents/All%20Documents/1302BahamasbookletFINAL11zon-20240209160028.pdf

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
