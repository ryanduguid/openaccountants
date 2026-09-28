---
name: am-company-formation
description: "Source-cited draft covering Armenian company formation and tax-regime elections from 2025. Explains LLC charter capital, the annual-results meeting window, election deadlines and the general, turnover-tax and micro-business systems. Includes activity and related-party exclusions, turnover ceilings, expense deductions, minimum payable tax and deduction carry-forwards. Use for registering a company in Armenia, choosing an entity, LLC capital, Armenian tax regimes, turnover tax calculations or micro-business eligibility. The statutory rules cite the Tax Code and LLC Law on ARLIS. Registration fees, processing times and some administrative requirements still need primary-source confirmation. Pending local-accountant review."
jurisdiction: AM
category: formation
tax_year: 2025
tax_year_notes: "Rates and thresholds are read from the consolidated Tax Code (ՀՕ-165-Ն) as published on arlis.am and current at the date below. The turnover-tax schedule in §3 and the AMD 115,000,000 and 24,000,000 thresholds are amended frequently by Finance-type acts and must be re-checked each year."
last_updated: 2026-09-11
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Armenia Company Formation & Entity Choice

Sections 1–3 cite the consolidated Tax Code and LLC Law on ARLIS. Check the version applicable to the transaction date, including commencement provisions, before applying these rules to an earlier period. Section 4 retains administrative claims that need further primary-source verification.

## 1. Limited liability companies

- The LLC Law sets no general minimum charter capital. Other laws and legal acts may prescribe a minimum for particular sectors. Charter capital and participants' contributions are denominated in dram. [LLC Law, art. 28](https://www.arlis.am/en/acts/218832/latest).
- The ordinary general meeting is held at least annually. The meeting approving annual results must take place **between two and six months after the financial year ends**. [LLC Law, art. 37](https://www.arlis.am/en/acts/218832/latest).

## 2. Regime eligibility and election deadlines

First check the activity, ownership, related-party and contractual exclusions in Section 3. An election filed on time cannot make an excluded business eligible.

- An eligible business registered during the tax year must submit its turnover-tax or micro-business declaration **by the 20th day following state registration, inclusive**, to enter that regime from registration through year end.
- An eligible existing business elects **by 20 February, inclusive**, for the regime to apply from 1 January.
- The general system applies where no valid special-regime election is made.

[Tax Code, arts. 254(1) and 267(1)](https://www.arlis.am/en/acts/230455/latest).

## 3. The three systems

### General system

- Resident companies and non-residents operating through a permanent establishment pay **18% profit tax** on the relevant taxable base. Investment funds other than pension and guarantee funds, and securitisation funds, pay **0.01%**. [Tax Code, art. 125(1)–(2)](https://www.arlis.am/en/acts/230455/latest).
- A sole trader in the turnover-tax system pays **AMD 5,000 per month** as final profit tax on those activities. This is separate from turnover tax. [Tax Code, art. 125(3)](https://www.arlis.am/en/acts/230455/latest).
- VAT is **20%** on taxable transactions under article 60, subject to the exemptions and zero-rating rules in articles 64 and 65. [Tax Code, art. 63(1) and (3)](https://www.arlis.am/en/acts/230455/latest).
- Article 63(2) uses **16.67%** to extract VAT from consideration in four specified cases: failure to recognise VAT-payer status, failure to show VAT separately in the settlement document, no settlement document, or issue of only a cash-register receipt. Check the statutory conditions before using this computational rate. [Tax Code, art. 63(2)](https://www.arlis.am/en/acts/230455/latest).

### Turnover tax

The ordinary ceiling is **AMD 115,000,000 of previous-year sales turnover across all activities**, including micro-business turnover. Apply the reorganisation aggregation rules where relevant. [Tax Code, art. 254(2)](https://www.arlis.am/en/acts/230455/latest).

Before electing, check **all exclusions in article 254(3)**. They include financial and insurance businesses, gambling operators, notaries and audit firms, legal and accounting activities, head-office and management consultancy activities, and the specified labour-supply activities. The related-party and contractual tests also matter:

- Article 30(1) related organisations and sole traders are excluded, subject to the exception where the related parties have declared cessation and actually stopped activity.
- For persons deemed related under article 30(2), aggregate previous- or current-year turnover exceeding AMD 115,000,000 disqualifies the group.
- Parties to joint-activity, commission-sale or specified agency agreements are excluded.

Confirm each activity code against the full article for the relevant period. Public catering has a special election under article 254(6)–(7) that can override the ordinary ceiling and some restrictions; the exclusions in paragraph 3(3) and 3(3.1) still apply. [Tax Code, art. 254(3)–(7)](https://www.arlis.am/en/acts/230455/latest).

The following are **gross rates before the expense reductions below**:

| Income type | Gross rate |
| --- | --- |
| Trading in goods, excluding listed secondary raw materials and disposal of other assets | 10% |
| Trading in secondary raw materials on the Government's list | 5% |
| Newspapers disposed of by editorial offices | 1.5% |
| Production activity | 7% |
| Rent, interest, royalty | 10% |
| Public catering | 12% |
| Other assets and other activity of a payer that declared for public catering | 20% |
| Activities on the Government's list of high-technology fields | 1% |
| Disposal of other assets, including immovable property | 10% |
| Other activity | 10% |

[Tax Code, art. 258(1)](https://www.arlis.am/en/acts/230455/latest). A payer that elects the public-catering regime uses only the catering and catering-payer other-activity rows, as article 258(8) requires.

#### Expense reductions and tax payable

For each activity below, let `T` be the quarter's taxable turnover, `E` its qualifying documented expenses, and `C` the unused tax reduction brought forward for that activity. Calculate:

`available_reduction = expense_rate × E + C`

`tax_payable = max(floor_rate × T, gross_rate × T − available_reduction)`

`carry_forward = available_reduction − (gross_rate × T − tax_payable)`

| Activity | Gross rate | Expense reduction rate | Minimum tax as a share of T |
| --- | --- | --- | --- |
| Trading under article 258(1), row 1 | 10% | 9.5% | 1% |
| Production | 7% | 5% | 3% |
| Public catering | 12% | 9% | 3.5% |
| Other activity under article 258(1), row 10 | 10% | 6% | 4.5% |

[Tax Code, art. 258(2)–(7) and art. 260](https://www.arlis.am/en/acts/230455/latest).

Qualifying expenses require the documents specified in article 55(2)(1–5), (12) or (13). They include the period's production and service costs, the original cost of goods acquired for resale, and administrative and selling expenses. Article 258(6) excludes fixed-asset and intangible-asset acquisition, construction, development, capital and current expenditure on those assets, depreciation and disposal costs, gratuitously received inputs, business travel and representation expenses, and the specified non-food asset costs for catering businesses.

Keep expenses and unused reductions separate by activity. Where administrative and selling expenses cannot be separately allocated, article 260(3) apportions them by turnover. Unused reductions carry into later quarters for the same activity, including when its current-quarter taxable base is zero. The floors still apply. On leaving the turnover-tax system, use article 264's transition rules rather than continuing this quarterly carry-forward unchanged.

The reporting period is a quarter. File and pay **by the 20th of the following month**. [Tax Code, arts. 259–262](https://www.arlis.am/en/acts/230455/latest).

### Micro-business

The ordinary ceiling is **AMD 24,000,000 of previous-year sales turnover across all activities**, including turnover-tax activities. Apply the reorganisation rules in article 267(3). [Tax Code, art. 267(3)](https://www.arlis.am/en/acts/230455/latest).

Check **all article 267(5) exclusions before electing**. They include trading businesses; financial, insurance, gambling and audit activities; consulting, legal, accounting, engineering, advertising, design, marketing, translation and other listed services; software development and other listed technical work; and specified catering and transport activities. The article also excludes recipients under specified rent, interest or royalty contracts, apart from the stated current-bank-account interest exception. Use the statutory activity definitions for the period concerned.

Article 267(5)(6)–(8) also excludes article 30(1) related persons unless the cessation exception applies; article 30(2) related groups whose aggregate turnover exceeds AMD 24,000,000; and parties to joint-activity, commission-sale or specified agency agreements. A business below the ceiling can still be ineligible. [Tax Code, art. 267(5)](https://www.arlis.am/en/acts/230455/latest).

Eligible micro-business activities are exempt from state taxes, tax-agent obligations and article 135 profit-tax advances, **except** import taxes (including EAEU imports), income tax on taxable payments to individuals who are not sole traders or notaries, and excise, environmental and road taxes. Salary withholding therefore continues at the applicable rate. [Tax Code, art. 269(1)–(2)](https://www.arlis.am/en/acts/230455/latest).

## 4. Registration mechanics — still on commercial sources

The following administrative claims retain their earlier sources. [RESEARCH GAP — the Law on State Registration of Legal Entities and the
Law on State Duty are both on `arlis.am` and would settle the fee and the timeline.]

- **Common entity types** — Limited liability company (LLC / ՍՊԸ), joint-stock company (JSC), and sole proprietor / individual entrepreneur  _(Civil Code of the Republic of Armenia (https://www.repatarmenia.org/repatriate/practical-information/business/starting-a-business-in-armenia))_
- **Foreign ownership** — 100% foreign ownership permitted; no local residency requirement for founders or directors  _(Law on Limited Liability Companies of the Republic of Armenia (https://armenian-lawyer.com/immigration/registering-an-llc-in-armenia-one%E2%80%91day-incorporation-tax-registration-and-first-compliance-steps/))_
- **Registration authority** — State Register of Legal Entities, Ministry of Justice of the Republic of Armenia (e-register)  _(Law on State Registration of Legal Entities (https://www.e-register.am/en/))_
- **Incorporation timeline** — Standard LLC registration in roughly 2–3 business days (online), with simple cases possible within hours ((approx — confirm) typical processing time)  _(Law on State Registration of Legal Entities (https://armenian-lawyer.com/immigration/company-registration-in-armenia-in-2-3-days-a-realistic-day-by-day-setup-checklist/))_
- **Government registration fee** — No state registration fee for standard LLC incorporation ((approx — confirm) current fee schedule)  _(Law on State Duty of the Republic of Armenia (https://armenian-lawyer.com/immigration/registering-an-llc-in-armenia-one%E2%80%91day-incorporation-tax-registration-and-first-compliance-steps/))_
- **E-invoicing / digital signature** — Electronic invoicing and digital signing are mandatory for all businesses  _(Tax Code of the Republic of Armenia (https://armenian-lawyer.com/immigration/registering-an-llc-in-armenia-one%E2%80%91day-incorporation-tax-registration-and-first-compliance-steps/))_

## 5. Worked checks

- An eligible trader has quarterly taxable sales of AMD 10,000,000, qualifying documented expenses of AMD 8,000,000 and no unused reduction. Gross tax is AMD 1,000,000; the reduction is AMD 760,000; the floor is AMD 100,000. **Tax payable is AMD 240,000**.
- With the same sales and AMD 10,000,000 of qualifying expenses, the available reduction is AMD 950,000. The floor limits the reduction used to AMD 900,000: **pay AMD 100,000 and carry forward AMD 50,000** for trading. [Tax Code, art. 258(2), (6) and (7)](https://www.arlis.am/en/acts/230455/latest).
- An accounting company with AMD 15,000,000 annual turnover cannot elect turnover tax or micro-business merely by meeting the ceilings and filing on time. Its activity is excluded under articles 254(3)(3.1) and 267(5)(2). [Tax Code](https://www.arlis.am/en/acts/230455/latest).

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
