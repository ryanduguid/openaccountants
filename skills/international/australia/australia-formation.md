---
name: australia-formation
description: Use this skill whenever asked about forming, incorporating, or registering a company in Australia. Trigger on phrases like "set up a company in Australia", "Pty Ltd", "ASIC registration", "Australian company formation", "register a business Australia", "ABN", "ACN", "proprietary limited", "sole trader Australia", "partnership Australia", or any question about starting a business entity in Australia. Covers entity types (Pty Ltd, Ltd, sole trader, partnership, trust), registration process, costs, post-formation compliance, and bank account opening. ALWAYS read this skill before advising on Australian company formation.
version: 1.7
jurisdiction: AU
tax_year: 2026
last_updated: 2026-11-18
review_status: pending_review
depends_on:
  - company-formation-workflow-base
category: formation
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Australia Formation v1.7

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

### Australia Company Formation Skill v1.7

## Ask the client first

- What taxpayer or entity, jurisdiction and reporting capacity are in scope?
- Which income year or transaction period applies?
- What records support the amounts, dates and classifications?
- Which residence, election, exception or eligibility conditions in this guide affect the answer?
- What facts or source conditions remain unresolved?
- For a company change: what is the event date, does a constitution or the replaceable rules govern, and who is the authorised officeholder?

## The method, step by step

### Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Australia (Commonwealth of Australia) |
| Currency | AUD |
| Company registrar | Australian Securities and Investments Commission (ASIC) -- asic.gov.au |
| Key legislation | Corporations Act 2001 (Cth) |
| Typical formation time | 1--3 business days (online via BRS) |
| Corporate tax rate | 25% for base rate entities (aggregated turnover under $50m and base rate entity passive income no more than 80% of assessable income); 30% for all others |
| Skill version | 1.7 |

### Section 2 -- Entity Types Comparison

**Entity Types Comparison**

| Feature | Sole Trader | Partnership | Pty Ltd (Proprietary) | Public Company (Ltd) | Trust (with corporate trustee) |
| --- | --- | --- | --- | --- | --- |
| Legal personality | No | No | Yes | Yes | No (trustee is legal person) |
| Liability | Unlimited | Unlimited (joint and several) | Limited to share capital | Limited | Trustee liability (limited if Pty Ltd trustee) |
| Min. founders | 1 | 2 | 1 shareholder + 1 director | 1 shareholder + 3 directors + 1 secretary | 1 settlor + 1 trustee |
| Min. share capital | N/A | N/A | No minimum (commonly $1) | No minimum | N/A |
| Max. shareholders | 1 | N/A | 50 counted non-employee holders, excluding qualifying CSF holders as explained below | Unlimited | N/A |
| Tax treatment | Personal income tax | Partners taxed individually | Company tax rate | Company tax rate | Trust distributions taxed in beneficiaries' hands |
| Admin burden | Very low | Low | Medium | High | Medium--High |
| ASIC registration | No | No (ABN only) | Yes ($636) | Yes | Only if trustee is a company |
| Audit required | No | No | Usually if large; small-company foreign control, CSF proceeds and audit directions can also require an audit, subject to applicable relief | Yes | No (unless regulated) |

For the 50-holder limit, exclude holders issued shares under a crowd-sourced funding (CSF) offer. Also exclude purchasers of shares originally issued under a CSF offer while the company's shares have not started trading on a financial market in Australia or overseas. That secondary-holder exclusion ends when market trading starts; original CSF holders remain excluded for their qualifying shares (ASIC RG 261 paragraphs 305 to 308). Thus 50 counted holders plus 100 qualifying CSF holders do not breach the limit merely because there are 150 holders.

Check the preparation, lodgement and audit conditions in `australia-financial-statements.md`, including the cumulative CSF proceeds threshold of at least $3 million. Small size alone does not remove an audit obligation.

- **Recommended default** — Proprietary company limited by shares (Pty Ltd) for most commercial purposes.
- **Choose the structure before registering** — Compare ownership, funding, liability, profit distribution and ongoing administration; a company is not automatically the best structure for a small business. Shareholders' liability is generally limited to unpaid amounts on their shares, but directors can be personally liable through guarantees, breaches of duties, insolvent trading and tax obligations, and a corporate trustee does not remove every trustee or director risk.  _([ASIC, Becoming a company director](https://www.asic.gov.au/for-business-and-companies/small-business-director-essentials/becoming-a-company-director))_

### Section 3 -- Registration Process

#### Step 1: Choose Company Name

- **Choose Company Name** — Check availability on ASIC's company name check tool; Must include "Pty Ltd" or "Proprietary Limited"; Can reserve name for 2 months ($65 fee) or register directly; Identical or near-identical names will be rejected  _(ASIC)_

#### Step 2: Obtain Consent from Officeholders

- **Obtain Consent from Officeholders** — All proposed directors and secretaries must consent in writing before registration; At least 1 director must ordinarily reside in Australia (for Pty Ltd)
- **Director eligibility and director ID** — Directors must be at least 18 and not disqualified from managing companies, and each must apply personally for a director identification number before appointment. A person appointed only to lend their name carries the same duties. A proprietary company using the crowd-sourced funding regime needs at least two directors.  _([ASIC, Becoming a company director](https://www.asic.gov.au/for-business-and-companies/small-business-director-essentials/becoming-a-company-director); [ASIC, Crowd-sourced funding](https://www.asic.gov.au/crowd-sourced-funding))_

#### Step 3: Prepare Company Details

- **Prepare Company Details** — Registered office address (must be in Australia; can be accountant's or agent's office); Principal place of business; Share structure (number and class of shares, rights); Details of shareholders, directors, secretary (if any)
- **Governance rules and consents** — Decide whether the company runs on the replaceable rules, a constitution, or both where permitted. Record share classes, rights, numbers and amounts paid or unpaid, obtain members' written consents and the occupier's consent for a registered office the company does not occupy, and open the share register at registration. Registering a company name does not create trade mark rights.  _([ASIC, Register a company](https://www.asic.gov.au/for-business-and-companies/companies/register-a-company))_

#### Step 4: Register via Business Registration Service (BRS)

- **Register via BRS** — Go to register.business.gov.au; Can simultaneously apply for: company registration, ABN, TFN, GST, PAYG withholding; Fee: $636 (company with share capital, from 1 July 2026); ASIC processes and issues ACN (Australian Company Number) typically within 1--3 days  _(BRS / ASIC)_

#### Step 5: Receive Certificate of Registration

- **Receive Certificate of Registration** — Certificate confirms ACN, company name, date of registration, type; Company legally exists from date on certificate
- **After registration** — Retain the certificate and ACN, check the register against the approved details and record the actual registration date. Do not promise a fixed processing or bank-account opening time, and keep access credentials with the authorised officeholder.

#### Step 6: Apply for ABN (Australian Business Number)

- **Apply for ABN** — Free via Australian Business Register (ABR); Required for tax invoices, GST, and dealing with other businesses; Can be applied for during BRS registration  _(ABR)_

#### Step 7: Register for GST (if applicable)

- **GST registration threshold** — Registration is required when GST turnover is or will be $75,000 or more ($150,000 for non-profit bodies); voluntary registration is permitted below the threshold.
- **GST turnover, not bank receipts** — The threshold uses the GST turnover definition, which differs from every receipt in the bank account. Taxi and ride-sourcing activities must register regardless of turnover, and voluntary registration below the threshold brings reporting obligations.  _([ATO, Registering for GST](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/registering-for-gst))_

#### Step 8: Register for PAYG Withholding (if employing)

- **Register for PAYG Withholding** — Required before paying employees or directors; Register via BRS or ATO  _(BRS / ATO)_
- **Payroll obligations from the first payment** — Before the first payment subject to withholding, set up payroll and check worker classification, Single Touch Payroll, awards, leave, workers compensation and state payroll tax. From 1 July 2026, Payday Super requires super guarantee contributions, at the general SG rate of 12% of qualifying earnings, to reach the fund within seven business days of payday, subject to specific exceptions.  _([ATO, About Payday Super](https://www.ato.gov.au/businesses-and-organisations/super-for-employers/about-payday-super))_

**Choose the SG schedule before applying a rate.** The rates and examples in this guide use the general SG schedule. Norfolk Island's transitional rate is 10% for 2025-26, 11% for 2026-27 and 12% from 1 July 2027. For a Norfolk Island arrangement, check the separate SG rules in `au-super-guarantee.md` before using a general rate or example. [ATO super guarantee rates](https://www.ato.gov.au/tax-rates-and-codes/key-superannuation-rates-and-thresholds/super-guarantee).

### Section 4 -- Capital Requirements

**Capital Requirements**

| Entity Type | Min. Share Capital | Min. Paid-Up | Payment Timing | In-Kind Contributions |
| --- | --- | --- | --- | --- |
| Pty Ltd | No statutory minimum ($1 common) | No minimum | As specified in share terms | Permitted (no independent valuation required for proprietary companies) |
| Public Ltd | No statutory minimum | No minimum | As specified | Permitted (expert's report required for non-cash consideration over threshold) |

- **No minimum capital requirement** — Australia has no minimum capital requirements for company formation.

### Section 5 -- Costs Breakdown

**Costs Breakdown**

| Cost Component | Amount (AUD) | Notes |
| --- | --- | --- |
| ASIC company registration | $636 | One-time (company with share capital, from 1 July 2026) |
| Name reservation (optional) | $65 | Valid 2 months |
| Business name registration (if different from company name) | $47/year or $108/3 years | Only if trading under a different name |
| ABN registration | Free | Via ABR |
| GST registration | Free | Via ATO |
| ASIC annual review fee | $342/year | Pty Ltd (from 1 July 2026; $1,591 for a public company) |
| **Total initial cost (government)** | **$636--$701** | Excluding professional fees |
| Legal / accountant setup fees | $500--$2,000 | Constitution, shareholder agreement, tax setup |
| **Total with professional help** | **$1,136--$2,701** |  |

ASIC fees are indexed each 1 July; the amounts above apply from 1 July 2026 ([ASIC, Fees for commonly lodged documents](https://www.asic.gov.au/for-business-and-companies/forms-and-fees/all-fees/fees-for-commonly-lodged-documents), checked 11 October 2026).

#### Annual Maintenance

**Annual Maintenance**

| Item | Cost (AUD) |
| --- | --- |
| ASIC annual review fee | $342 |
| Accountant / tax agent fees | $1,500--$5,000/year |
| Business name renewal (if applicable) | $47/year |
| Registered office service (if using) | $200--$600/year |
| ASIC late fees | $102 (≤1 month) / $428 (>1 month), running from the review fee's due date, 2 months after the review date |

### Section 7 -- Bank Account Opening

#### Documents Typically Required

- **Documents Typically Required** — Certificate of registration (ACN); Company constitution or replaceable rules; ABN confirmation; ID (passport / driver's licence) for all directors; Proof of address for directors and shareholders

#### Typical Timeline

- **Typical Timeline** — 1--3 days (Big 4 banks and digital banks for Australian residents); 1--3 weeks (non-resident directors, enhanced KYC)

#### Common Banks

Commonwealth Bank (CBA), Westpac, ANZ, NAB (Big 4); Macquarie, Bendigo (mid-tier); Airwallex, Wise Business (digital/international)

### Section 8 -- Foreign Founder Considerations

**Foreign Founder Considerations**

| Question | Answer |
| --- | --- |
| Non-resident directors allowed? | Yes, but at least 1 director must ordinarily reside in Australia |
| Resident director requirement | At least 1 (for Pty Ltd); at least 2 of 3 for public companies |
| Nominee directors | Permitted (ASIC register shows actual director names) |
| Physical presence required? | No (online registration); resident director must be genuinely resident |
| Foreign ownership restrictions | Foreign Investment Review Board (FIRB) approval may be required for certain sectors and thresholds |
| ABN for foreign entities | A foreign company carrying on business in Australia registers with ASIC ($636 from 1 July 2026), receives an ARBN and can apply for an ABN |
| Tax treaty benefits | Australia has extensive DTA network; check withholding rates |

- **Foreign founders** — Examine the resident director requirement, the founders' tax residency, foreign investment rules and the difference between incorporating an Australian company and registering an existing foreign company, and record the chosen structure and the reasons for it before applying.

### Section 10 -- Timeline

**Timeline**

| Step | Duration | Cumulative |
| --- | --- | --- |
| Prepare documents and officer consents | 1--2 days | Day 1--2 |
| Register via BRS (ABN + company + GST) | 1 day | Day 2--3 |
| ASIC issues ACN and certificate | 1--3 days | Day 3--6 |
| Open business bank account | 1--3 days (resident) / 1--3 weeks (non-resident) | Day 4--27 |
| ATO registrations confirmed | 1--28 days | Day 4--34 |
| **Ready to trade** |  | **As fast as 3--5 days (Australian-resident founders)** |

## Worked cases

Cases 1 and 2 are synthetic; they apply Section 6.5 and recompute with `python3 scripts/check-examples.py skills/international/australia/australia-formation.md`. Dates are day numbers in 2027, where day 1 is 1 January 2027. Each case assumes the replaceable rules govern notice, the constitution sets no longer period, and each last day is a business day where the act is done (s 105(3) otherwise moves it to the next business day). Days are counted under s 105 of the *Corporations Act 2001*: a period dating from a day or event excludes that day (s 105(1)), and in counting how many days one day is before or after another, the first is counted and the other is not (s 105(2)). That rule, not the clear-days reading of older cases, governs the Act's 21 days' notice. A constitution that requires clear days sets a longer period, which these cases assume away; under one, the latest notice and posting days in Case 1 each move 1 day earlier (posting by day 24).

### Case 1: Form 2560 and a posted notice for an equal reduction

A proprietary company with 3 members proposes an equal reduction at a general meeting on Thursday 18 February 2027 (day 49) and will post the notice. The notice must be given at least 21 days before the meeting (s 249H(1)), so it must be taken to be given by day 28 (Thursday 28 January). A posted notice is given 3 days after posting (s 249J(4)(a)), so the latest posting day is day 25 (Monday 25 January). Form 2560 must be lodged before the notice is sent (s 256C(5)), so by day 25 and before posting; ASIC's 22 days give day 27 (Wednesday 27 January). Diary day 25, the earlier.

```oa-check
name: AU formation equal reduction Form 2560 and posted notice 2027
inputs:
  meeting_day: 49
  notice_days: 21
  postal_deeming_days: 3
  asic_form_2560_days: 22
steps:
  - latest_notice_given_day: meeting_day - notice_days
  - latest_posting_day: latest_notice_given_day - postal_deeming_days
  - asic_latest_lodgement_day: meeting_day - asic_form_2560_days
  - diary_lodgement_day: min(latest_posting_day, asic_latest_lodgement_day)
expected:
  latest_notice_given_day: 28
  latest_posting_day: 25
  asic_latest_lodgement_day: 27
  diary_lodgement_day: 25
tolerance: 0.000001
```

### Case 2: a selective reduction that cancels shares

A proprietary company passes the special resolutions for a selective reduction that cancels one member's shares on Wednesday 3 February 2027 (day 34) and lodges Form 2205 on Friday 5 February (day 36). Form 2205 was due by day 48 (Wednesday 17 February). The 14 days after lodgement end on day 50 (Friday 19 February). The Act does not settle whether 'must not make the reduction until 14 days after lodgment' (s 256C(3)) allows the reduction on day 50 or only after it, so diary day 51 (Saturday 20 February) as the earliest day, which meets both readings. The s 178D item 4 period for the member register notice ends on day 48, 3 days before that day: record it for the authorised officeholder. The company makes the reduction and cancels the shares on Monday 22 February (day 53). ASIC's 28 days end on day 81 (Monday 22 March), the same day the s 254Y month ends. Diary 22 March 2027.

```oa-check
name: AU formation selective reduction Form 2205 and notices 2027
inputs:
  resolution_day: 34
  form_2205_period_days: 14
  lodgement_day: 36
  wait_after_lodgement_days: 14
  reduction_day: 53
  asic_change_period_days: 28
steps:
  - form_2205_last_day: resolution_day + form_2205_period_days
  - wait_last_day: lodgement_day + wait_after_lodgement_days
  - earliest_reduction_day: wait_last_day + 1
  - s178d_gap_days: earliest_reduction_day - form_2205_last_day
  - asic_change_last_day: reduction_day + asic_change_period_days
expected:
  form_2205_last_day: 48
  wait_last_day: 50
  earliest_reduction_day: 51
  s178d_gap_days: 3
  asic_change_last_day: 81
tolerance: 0.000001
```

## When to refuse or refer

### Section 9 -- Common Mistakes and Refusals

- **R-AU-F1 -- No Australian-resident director** — Every Pty Ltd must have at least one director who ordinarily resides in Australia. A company cannot be registered without this. Advise the client to appoint a local director or use a resident director service (with proper governance).  _(R-AU-F1)_
- **R-AU-F2 -- Failing to pay ASIC annual review fee** — ASIC charges $342/year for a proprietary company from 1 July 2026. If the annual review fee stays unpaid, ASIC can start deregistering the company. The fee is due within 2 months after the review date; late fees then apply: $102 within 1 month of that due date, $428 after 1 month.  _(R-AU-F2)_
- **R-AU-F3 -- GST threshold ignorance** — If annual turnover reaches $75,000, GST registration is mandatory. Failing to register when required results in penalties and backdated GST assessments.  _(R-AU-F3)_
- **R-AU-F4 -- Superannuation non-compliance** — The general SG rate is 12% (11.5% for 2024-25). From 1 July 2026, Payday Super applies it to each payment of qualifying earnings, and the contribution must reach the employee's fund within seven business days of payday; on $100,000 of qualifying earnings the minimum is $12,000. Late or short payment results in the Superannuation Guarantee Charge (SGC). SGC for periods from 1 July 2026 is tax-deductible; penalties and interest after the ATO assesses it, and SGC under the former quarterly regime, are not. See `au-super-guarantee.md`.  _(R-AU-F4; [ATO, About Payday Super](https://www.ato.gov.au/businesses-and-organisations/super-for-employers/about-payday-super))_
- **R-AU-F5 -- Shell company without substance** — This skill will not assist in forming a company with no genuine business activity in Australia. ASIC and the ATO actively pursue sham structures.  _(R-AU-F5)_
- **R-AU-F6 -- Deciding a directors' judgement** — Do not decide, or draft a finding on, whether a share capital reduction is fair and reasonable to the shareholders or materially prejudices the company's ability to pay its creditors, or whether the company is solvent. Record what the directors considered and leave the opinion to them (Sections 6.4 and 6.5).  _(R-AU-F6)_
- **R-AU-F7 -- Other capital reductions and the tax on a capital return** — Refer share buy-backs, redemptions of redeemable preference shares, reductions under ss 258A to 258F of the *Corporations Act 2001* and reductions by a listed company, and the income tax treatment of any payment to shareholders, to a reviewer (Section 6.5).  _(R-AU-F7)_


### Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute legal, tax, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before acting upon.

This guide is maintained in the [ryanduguid/openaccountants fork](https://github.com/ryanduguid/openaccountants). Check its quality tier, recorded review status and cited primary sources for the requested period. The upstream website does not publish or verify this fork's changes.

> Contributed by Ryan Duguid.



## Filing and payment

### Section 6 -- Post-Formation Compliance

**Post-Formation Compliance**

| Obligation | Deadline | Authority |
| --- | --- | --- |
| ASIC annual review | Annual (on registration anniversary); review fee due within 2 months after the review date | ASIC |
| Company tax return | Due date varies (usually by 15 May via tax agent for 30 June year-end) | ATO |
| BAS (Business Activity Statement) | Quarterly or monthly (GST, PAYG, instalment) | ATO |
| PAYG summaries / STP finalisation | 14 July following the financial year | ATO |
| Superannuation guarantee | Received by the fund within 7 business days of each payday (Payday Super, from 1 July 2026) | Super fund / ATO |
| Change notifications to ASIC | Mostly within 28 days of the change; some 7 or 14 days or 1 month (Section 6.1) | ASIC |
| Financial records | Maintain for 7 years | Internal |
| Directors' duties | Ongoing (s180--184 Corporations Act) | ASIC |

- **Keep the company separate and diarised** — Keep company money and transactions apart from personal finances, agree who maintains the share register, accounting records, tax calendar and ASIC correspondence, and diary the annual review, solvency resolution and change notifications. Retain financial records for seven years after the transactions they cover. Tax return and activity statement dates depend on the company's circumstances and lodgement arrangements; they are not all due on one date.  _([ASIC, What books and records should my company keep](https://asic.gov.au/for-business/running-a-company/company-officeholder-duties/what-books-and-records-should-my-company-keep/))_

#### 6.1 Change notices to ASIC

Each change has its own section of the *Corporations Act 2001*, form and period. The table follows compilation 149 of the Act (in force from 19 September 2026) and ASIC's pages and INFO 30 as read on 18 November 2026; reread them at use. Form 484 is the change of company details transaction in the company officeholder portal. 'No fee' is INFO 30's entry from 1 July 2026; 'Not listed' means INFO 30 gives no fee for that form.

| Change | Section | ASIC form | Lodge within | Fee (2026-27) |
| --- | --- | --- | --- | --- |
| Director or secretary appointed | s 205B(1); an alternate director's details and terms of appointment, s 205B(2) | 484 | 28 days after the appointment | Not listed |
| Officeholder's personal details change | s 205B(4) | 484 | 28 days after the change | Not listed |
| Director or secretary ceases | s 205B(5) | 484, or the officeholder's own Form 370 with a copy of the resignation letter, which replaces the company's notice (ss 205A and 205B(6)) | 28 days | Not listed |
| Registered office | s 142(2) | 484 | 28 days after the change | No fee |
| Principal place of business | s 146(1) | 484 | 28 days after the change | No fee |
| Share issue | s 254X(1); for a proprietary company also ss 178A, 178C and 178D item 3 | 484; Form 207Z stamp duty certificate for non-cash consideration under a contract (s 254X(2)); for a public company's non-cash issue, also Form 208 or a copy of the written contract (s 254X(1)(e)) | 28 days after the issue | No fee |
| Share transfer or other member register change (proprietary company) | ss 178A to 178C and 178D item 5 | 484 | 28 days after the register is altered | Not listed |
| Share cancellation | s 254Y(1) | 484 | 1 month after the cancellation; INFO 30 applies its late fee after 28 days | No fee |
| Proposed share capital reduction | s 256C(5) | 2560 | Before the notice of meeting is sent; ASIC says at least 22 days before the meeting (29 for a public listed company) | Not listed |
| Selective reduction resolution | s 256C(3) | 2205 | 14 days after it is passed | No fee |
| Negative solvency resolution, or none passed | s 347B | 485 | 7 days (Section 6.4) | Not listed |
| Correction to the annual statement | s 346C(3) | Change of company details, per ASIC's annual review page | 28 days after the statement's issue date | Not listed |

- **Late fees** — A notice lodged after its period attracts a late fee on top of any lodgement fee. From 1 July 2026 it is $102 if ASIC receives the document within 1 month after the prescribed time and $428 if later (Corporations (Fees) Regulations 2001 Schedule 2 item 14). A late annual review fee and late annual statement corrections attract the same amounts, each separately.  _([ASIC, Fees for commonly lodged documents (INFO 30)](https://www.asic.gov.au/for-business-and-companies/forms-and-fees/all-fees/fees-for-commonly-lodged-documents), reissued July 2026; [ASIC, Late fees](https://www.asic.gov.au/for-business-and-companies/forms-and-fees/late-fees))_
- **Counting days** — A period dating from a day or event excludes that day. In counting how many days one day is before or after another, the first is counted and the other is not. When a period for doing something ends on a day that is not a business day where it must be done, it may be done on the next business day; check that place's public holidays.  _([Corporations Act 2001 s 105](https://www.legislation.gov.au/C2004A00818/latest/text))_
- **A late notice moves the resignation date** — A director's resignation takes effect on the day they stopped only if ASIC is notified within 28 days (s 205A or s 205B(5)). Otherwise it takes effect on the day the notice is lodged, unless ASIC, on an application made within 56 days, or the Court fixes the earlier day (s 203AA). ASIC then records the date the change was made as the end date. Flag any notice near its 28th day for the authorised officeholder.  _([Corporations Act 2001 ss 203AA, 205A and 205B](https://www.legislation.gov.au/C2004A00818/latest/text); [ASIC, Add or remove a company officeholder](https://www.asic.gov.au/for-business-and-companies/companies/company-officeholder-rules-and-changes/add-or-remove-a-company-officeholder))_
- **Changes from 1 July 2027** — The Treasury Laws Amendment (Business Registries Stabilisation and Uplift) Act 2026 adds a director's or alternate director's director identification number to the personal details notified under s 205B, with 14 days after the Registrar issues the number where the director had none on appointment (new s 205B(3A)). It also adds electronic addresses: an officeholder's (s 205B(3)(d)) and the company's, whose change, once that address has been lodged with or given to ASIC, is notified within 28 days (new s 146B). Until then, record whether each director holds a director ID, not the number. The amending Acts that commence on 1 and 4 December 2026 and 8 April 2027 do not mention the sections cited in this Section 6.  _([Treasury Laws Amendment (Business Registries Stabilisation and Uplift) Act 2026, s 2 and Schedules 1 and 2](https://www.legislation.gov.au/C2026A00057/asmade/text))_

#### 6.2 Officeholder changes

- **Who may appoint or remove** — Identify the governing rules first. The constitution can displace or modify a replaceable rule (s 135(2)), and a replaceable rule does not apply while one person is both sole director and sole shareholder (s 135(1)); that person appoints another director by recording the appointment and signing the record (s 201F(1)). Under the replaceable rules, members appoint by resolution in general meeting (s 201G); directors appoint (s 201H(1)), and a proprietary company confirms that appointment by resolution within 2 months or the director ceases (s 201H(2)); members of a proprietary company remove a director by resolution (s 203C); and a director resigns by written notice to the company at its registered office (s 203A). A public company differs: the directors' appointee is confirmed at the next AGM (s 201H(3)), it needs at least 3 directors, not counting alternate directors, 2 of them ordinarily resident in Australia (s 201A(2)), and members remove a director under s 203D at a meeting that cannot be called on shorter notice (s 249H(3)); record a public company's change as a question for the authorised officeholder.  _([Corporations Act 2001](https://www.legislation.gov.au/C2004A00818/latest/text))_
- **Before appointment** — Hold the person's signed consent to act, given before appointment and kept by the company (s 201D), and confirm that they applied for a director ID before appointment, as ASIC requires. Record whether each condition is evidenced and leave eligibility to the authorised officeholder; the director eligibility bullet in Section 3, Step 2 applies.  _([Corporations Act 2001 s 201D](https://www.legislation.gov.au/C2004A00818/latest/text); [ASIC, Add or remove a company officeholder](https://www.asic.gov.au/for-business-and-companies/companies/company-officeholder-rules-and-changes/add-or-remove-a-company-officeholder))_
- **Minimum officeholders after every change** — A proprietary company needs at least 1 director who ordinarily resides in Australia (s 201A(1)), and at least 2 while it has CSF shareholders, of whom at least 1 (if there are 2) or a majority (if more) ordinarily reside in Australia (s 201A(1A)). A resignation does not take effect if no director would remain (s 203AB), but that rule does not stop a change that leaves fewer directors than s 201A requires. A members' resolution removing the last director is void (s 203CA); ASIC says a sole director cannot resign without a replacement. Keep a sole director's resignation conditional on a valid appointment. Route a departing or incoming director's exposure to director penalties to `au-director-penalties.md`.  _([Corporations Act 2001](https://www.legislation.gov.au/C2004A00818/latest/text); [ASIC, Add or remove a company officeholder](https://www.asic.gov.au/for-business-and-companies/companies/company-officeholder-rules-and-changes/add-or-remove-a-company-officeholder))_
- **Passing and recording resolutions** — Directors may pass a resolution without a meeting if all directors entitled to vote sign it (s 248A, a replaceable rule), and the sole director of a proprietary company by recording and signing it (s 248B). Members of a proprietary company may do so if all members entitled to vote sign (s 249A), and a one-member company by the member recording and signing it (s 249B). Record each resolution in the minute book within 1 month and have the minutes signed within a reasonable time (s 251A). Draft the documents with proposed dates for signing; never sign, lodge, pay or backdate, and record a request to date a document before it was signed as an exception.  _([Corporations Act 2001](https://www.legislation.gov.au/C2004A00818/latest/text))_
- **Address changes** — For a registered office the company does not occupy, the notice states that the occupier consented. The change takes effect from the later of the 7th day after the notice is lodged and a later day stated in it (s 142(3)). Notify a principal place of business change separately (s 146).  _([Corporations Act 2001 ss 142 and 146](https://www.legislation.gov.au/C2004A00818/latest/text); [ASIC, Change a company address](https://www.asic.gov.au/for-business-and-companies/companies/changes-to-company-details/change-a-company-address))_

#### 6.3 Share issues and transfers

- **Share issue** — Confirm the power and approval under the constitution or replaceable rules, and record the number, class and amounts paid and unpaid. Lodge the s 254X notice within 28 days after the issue, with a certificate that stamp duty on the contract is paid for an issue for non-cash consideration under a contract (s 254X(2)). A public company issuing for non-cash consideration also gives the prescribed particulars on Form 208 or lodges a copy of the written contract (s 254X(1)(e)). A proprietary company notifies member details and the share structure at the same time (ss 178A, 178C and 178D item 3). Route the duty question to `au-stamp-duty.md`.  _([Corporations Act 2001](https://www.legislation.gov.au/C2004A00818/latest/text); [ASIC, Company share issues](https://www.asic.gov.au/for-business-and-companies/companies/company-share-and-shareholder-rules-and-changes/company-share-issues))_
- **Transfers and other member register changes** — Record the signed transfer and the register entry, and lodge a proprietary company's notice within 28 days after the register is altered (s 178D item 5). A proprietary company with more than 20 members notifies only changes that affect a top 20 member of a class (s 178B). Route the tax consequences to `au-capital-gains.md` and loans or payments to shareholders to `au-div7a.md`.  _([Corporations Act 2001](https://www.legislation.gov.au/C2004A00818/latest/text); [ASIC, Transfer of shares or change to beneficial ownership status](https://www.asic.gov.au/for-business-and-companies/companies/company-share-and-shareholder-rules-and-changes/transfer-of-shares-or-change-to-beneficial-ownership-status); [ASIC, Members register requirements and changes](https://www.asic.gov.au/for-business-and-companies/companies/company-share-and-shareholder-rules-and-changes/members-register-requirements-and-changes))_

#### 6.4 Annual review and solvency resolution

- **Annual statement** — ASIC gives the extract of particulars within 2 weeks after each review date (s 346A). Correct any wrong particular within 28 days after its issue date (s 346C(3)); the correction does not remove late fees already incurred (s 346C(5)).  _([Corporations Act 2001](https://www.legislation.gov.au/C2004A00818/latest/text); [ASIC, Company annual review](https://www.asic.gov.au/for-business-and-companies/companies/company-annual-review))_
- **Solvency resolution** — The directors pass a solvency resolution within 2 months after each review date, unless the company lodged a financial report under Chapter 2M in the 12 months before that date (s 347A). Notify ASIC on Form 485 within 7 days after a negative resolution, or within 7 days after the 2 months if none was passed (s 347B). A positive resolution is kept, not lodged. If the review fee is paid, no s 347B notice is lodged and no financial report was lodged in the 12 months before the review date, the directors are taken to have represented that the company is solvent, unless they prove they passed a positive solvency resolution in time (s 347C). Draft the resolution and assemble the information the directors ask for; the solvency opinion is theirs alone.  _([Corporations Act 2001 ss 347A to 347C](https://www.legislation.gov.au/C2004A00818/latest/text); [ASIC, Company annual review](https://www.asic.gov.au/for-business-and-companies/companies/company-annual-review))_

#### 6.5 Share capital reductions

This covers a reduction under Division 1 of Part 2J.1 of the *Corporations Act 2001*. A share buy-back (Division 2), a redemption of redeemable preference shares (s 254K) and the reductions ss 258A to 258F authorise follow other rules: record each as a question for the authorised officeholder (R-AU-F7). The directors and members decide; this guide prepares the record.

- **Classify the reduction** — It is an equal reduction only if it relates only to ordinary shares, applies to each holder in proportion to the ordinary shares they hold and has the same terms for each; otherwise it is selective (s 256B(2)). Ignore differences due only to different accrued dividend entitlements, different amounts unpaid or rounding to whole shares (s 256B(3)). Record the evidence for each condition and keep the classification `UNVERIFIED` while any is missing. Record any restriction in the constitution, and whether the terms vary the rights of a class of shares, as questions for the authorised officeholder.  _([Corporations Act 2001 s 256B](https://www.legislation.gov.au/C2004A00818/latest/text))_
- **The directors' judgements** — The reduction must be fair and reasonable to the shareholders as a whole and must not materially prejudice the company's ability to pay its creditors (s 256B(1)). The creditor condition does not apply to cancelling a share for no consideration, and cancelling a partly-paid share is for consideration (s 256B(1A)). Record which directors considered each condition, when and on what information; do not decide either or draft a finding (R-AU-F6). A reduction made in breach stays valid, but anyone involved contravenes a civil penalty provision (s 256D), and the directors may have to compensate the company if it is or becomes insolvent when it reduces its capital (s 256E, pointing to ss 588G and 1317H).  _([Corporations Act 2001 ss 256B, 256D and 256E](https://www.legislation.gov.au/C2004A00818/latest/text))_
- **Approval** — An equal reduction needs a resolution passed at a general meeting (s 256C(1)); ASIC says an ordinary resolution, unless the constitution requires a special one. A selective reduction needs either a special resolution at a general meeting with no votes in favour cast by anyone who is to receive consideration or have their liability for unpaid amounts reduced, or by their associates, or a resolution agreed at a general meeting by all ordinary shareholders. If it cancels shares, it also needs a special resolution at a meeting of the holders whose shares are cancelled (s 256C(2)).  _([Corporations Act 2001 s 256C](https://www.legislation.gov.au/C2004A00818/latest/text); [ASIC, Reduction in share capital](https://www.asic.gov.au/for-business-and-companies/companies/company-share-and-shareholder-rules-and-changes/reduction-in-share-capital))_
- **Passing the resolution** — A one-member company passes it by the member recording and signing it, and a requirement to lodge information or a document about it is met by lodging that with the passed resolution (s 249B(2)); ASIC says such a company needs no notice, meeting or lodgement before the resolution is passed. A proprietary company may pass it without a meeting if every member entitled to vote signs, and lodging the document to be signed, and the information or documents given with it, meets the requirements to lodge the notice of meeting and its accompanying documents (s 249A(5)). A meeting needs at least 21 days' notice, or longer if the constitution says so (s 249H(1)). Shorter notice needs the prior agreement of members with at least 95% of the votes (s 249H(2)(b)), or of all members entitled to attend and vote for an AGM (s 249H(2)(a)): record each agreement and its date. Under the replaceable rule, a posted notice is given 3 days after posting (s 249J(4)(a)).  _([Corporations Act 2001 ss 249A, 249B, 249H and 249J](https://www.legislation.gov.au/C2004A00818/latest/text); [ASIC, Reduction in share capital](https://www.asic.gov.au/for-business-and-companies/companies/company-share-and-shareholder-rules-and-changes/reduction-in-share-capital))_
- **Before the notice is sent** — The notice must include a statement of all information known to the company that is material to the vote, except information already disclosed to shareholders where requiring it again would be unreasonable (s 256C(4)). Before it is sent, lodge the notice and any document about the reduction that goes with it (s 256C(5)) on Form 2560; ASIC says at least 22 days before the meeting, or 29 for a public listed company. Diary the earlier date (Case 1). Where members agree to shorter notice, ASIC's page does not say how its 22 days apply: refer it.  _([Corporations Act 2001 s 256C](https://www.legislation.gov.au/C2004A00818/latest/text); [ASIC, Reduction in share capital](https://www.asic.gov.au/for-business-and-companies/companies/company-share-and-shareholder-rules-and-changes/reduction-in-share-capital))_
- **After the resolution** — For a selective reduction only, lodge the resolution on Form 2205 within 14 days after it is passed, and do not make the reduction until 14 days after lodgement (s 256C(3)); diary the day after the 14th day as the earliest, because the Act does not settle whether the 14th day itself is allowed (Case 2). For a proprietary company, s 178D item 4 times the member register notice for a reduction by the s 256C(3) period. For a selective reduction that period can end before the reduction may be made (Case 2), and an equal reduction has no s 256C(3) period; record either as a question for the authorised officeholder.  _([Corporations Act 2001 ss 178D and 256C](https://www.legislation.gov.au/C2004A00818/latest/text); [ASIC, Reduction in share capital](https://www.asic.gov.au/for-business-and-companies/companies/company-share-and-shareholder-rules-and-changes/reduction-in-share-capital))_
- **After the reduction** — Notify any share cancellation within 1 month after it (s 254Y(1)); INFO 30 applies the late fee after 28 days. ASIC's reduction page says to report the share structure changes and, for a proprietary company, top 20 member changes through the change of company details transaction within 28 days after reducing the capital. Diary the earliest date that applies.  _([Corporations Act 2001 s 254Y](https://www.legislation.gov.au/C2004A00818/latest/text); [ASIC, Reduction in share capital](https://www.asic.gov.au/for-business-and-companies/companies/company-share-and-shareholder-rules-and-changes/reduction-in-share-capital); [ASIC, Cancel company shares](https://www.asic.gov.au/for-business-and-companies/companies/company-share-and-shareholder-rules-and-changes/cancel-company-shares))_
- **Tax is referred** — Route the shareholders' CGT records to `au-capital-gains.md`, which lists CGT event G1. Whether any part of the payment is a dividend for income tax, or frankable, is for a tax reviewer; this guide does not decide it. Do not make the reduction, pay any amount, sign, lodge or decide a condition.

## Sources

| Source | URL | Read on |
|---|---|---|
| Retained citation | <https://www.asic.gov.au/for-business-and-companies/small-business-director-essentials/becoming-a-company-director> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.asic.gov.au/crowd-sourced-funding> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.asic.gov.au/for-business-and-companies/companies/register-a-company> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/registering-for-gst> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.ato.gov.au/businesses-and-organisations/super-for-employers/about-payday-super> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.ato.gov.au/tax-rates-and-codes/key-superannuation-rates-and-thresholds/super-guarantee> | Not re-read for this format update; see retained provenance |
| ASIC, Fees for commonly lodged documents (INFO 30), reissued July 2026 | <https://www.asic.gov.au/for-business-and-companies/forms-and-fees/all-fees/fees-for-commonly-lodged-documents> | 2026-11-18; Section 6.1 forms, fees and late fees from 1 July 2026, and the $636, $65, $342 and $1,591 fees |
| Retained citation | <https://asic.gov.au/for-business/running-a-company/company-officeholder-duties/what-books-and-records-should-my-company-keep/> | Not re-read for this format update; see retained provenance |
| Corporations Act 2001, compilation 149 (C2026C00432, in force from 19 September 2026), volume 1: ss 105, 135, 142, 146, 178A to 178D, 201A to 201H, 203A to 203D, 205A, 205B, 248A to 249B, 249H, 249J, 251A, 254X, 254Y and 256B to 256E | <https://www.legislation.gov.au/C2004A00818/2026-09-19/2026-09-19/text/original/epub/OEBPS/document_1/document_1.html> | 2026-11-18; Section 6 and Cases 1 and 2 |
| Corporations Act 2001, compilation 149, volume 2: ss 346A, 346C and 347A to 347C | <https://www.legislation.gov.au/C2004A00818/2026-09-19/2026-09-19/text/original/epub/OEBPS/document_2/document_2.html> | 2026-11-18; Section 6.4 |
| Federal Register, Corporations Act 2001 versions | <https://www.legislation.gov.au/C2004A00818/latest/versions> | 2026-11-18; compilation 149 current, next versions from 1 and 4 December 2026, 8 April 2027 and 1 July 2027 |
| Treasury Laws Amendment (Business Registries Stabilisation and Uplift) Act 2026, s 2 and Schedule 1 items 3 to 5, Schedule 2 items 48 and 49 | <https://www.legislation.gov.au/C2026A00057/asmade/text> | 2026-11-18; Section 6.1, changes from 1 July 2027 |
| ASIC, Reduction in share capital | <https://www.asic.gov.au/for-business-and-companies/companies/company-share-and-shareholder-rules-and-changes/reduction-in-share-capital> | 2026-11-18; Forms 2560 and 2205, 22 and 29 days, 28 days after reducing, single-member companies |
| ASIC, Cancel company shares | <https://www.asic.gov.au/for-business-and-companies/companies/company-share-and-shareholder-rules-and-changes/cancel-company-shares> | 2026-11-18; notice within one month |
| ASIC, Add or remove a company officeholder | <https://www.asic.gov.au/for-business-and-companies/companies/company-officeholder-rules-and-changes/add-or-remove-a-company-officeholder> | 2026-11-18; Form 484, 28 days, director ID before appointment, Form 370, sole director |
| ASIC, Change a company address | <https://www.asic.gov.au/for-business-and-companies/companies/changes-to-company-details/change-a-company-address> | 2026-11-18; 28 days, occupier consent |
| ASIC, Company share issues | <https://www.asic.gov.au/for-business-and-companies/companies/company-share-and-shareholder-rules-and-changes/company-share-issues> | 2026-11-18; 28 days after the issue, Forms 207Z and 208 |
| ASIC, Transfer of shares or change to beneficial ownership status | <https://www.asic.gov.au/for-business-and-companies/companies/company-share-and-shareholder-rules-and-changes/transfer-of-shares-or-change-to-beneficial-ownership-status> | 2026-11-18; Form 484 within 28 days |
| ASIC, Members register requirements and changes | <https://www.asic.gov.au/for-business-and-companies/companies/company-share-and-shareholder-rules-and-changes/members-register-requirements-and-changes> | 2026-11-18; top 20 members |
| ASIC, Company annual review | <https://www.asic.gov.au/for-business-and-companies/companies/company-annual-review> | 2026-11-18; solvency resolution, Form 485, 7 days |
| ASIC, Late fees | <https://www.asic.gov.au/for-business-and-companies/forms-and-fees/late-fees> | 2026-11-18; $102 and $428 |

Not yet confirmed: A complete page-level source/read-date audit and independent legal review have not been performed for this structural update. Existing dates and qualifications retain their original scope. Cases 1 and 2 recompute with `check-examples` but have had no human review, and Section 6 has had no legal review.

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
