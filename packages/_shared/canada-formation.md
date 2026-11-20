---
name: canada-formation
description: Use this skill whenever asked about forming, incorporating, or registering a company in Canada. Trigger on phrases like "set up a company in Canada", "Canadian incorporation", "Corporations Canada", "federal incorporation", "provincial incorporation", "CBCA", "Ontario corporation", "BC incorporation", "Inc. Canada", "Canadian company formation", "register a business Canada", or any question about starting a business entity in Canada. Covers federal vs provincial incorporation, entity types, registration process, costs, post-formation compliance, and bank account opening. ALWAYS read this skill before advising on Canadian company formation.
version: 1.2
jurisdiction: CA
tax_year: 2025
last_updated: 2026-11-21
reviewed_by: Edgar Lautsyus
review_status: pending_review
depends_on:
  - company-formation-workflow-base
category: formation
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Canada Formation

## Canada Company Formation Skill v1.2

> **Previous practitioner review.** Nathan Wiebe reviewed the earlier rates and thresholds on 2026-06-21, and Edgar Lautsyus signed off on the prior version, as recorded in the frontmatter and `PARTNERS.md`. The November 2026 director residency and registration corrections await renewed practitioner review. Items flagged for clarification remain marked in the text.

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Canada |
| Currency | CAD |
| Company registrar (federal) | Corporations Canada (ISED) -- corporationscanada.ic.gc.ca |
| Company registrar (provincial) | Varies by province (e.g., Ontario: ServiceOntario; BC: BC Registry Services; QC: Registraire des entreprises) |
| Key legislation | Canada Business Corporations Act (CBCA) -- federal; provincial equivalents (OBCA, BCBCA, etc.) |
| Typical formation time | 1 day (federal online); 1--5 days (most provinces online) |
| Corporate income tax | General federal rate 15%, plus provincial or territorial tax. Eligible Canadian-controlled private corporations (CCPCs) can qualify for the 9% federal small business rate. Ontario’s own lower rate fell from 3.2% to 2.2% on 1 July 2026. Prorate a year spanning that date and test federal and provincial eligibility separately. [CRA corporation tax rates](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/corporation-tax-rates.html) · [Ontario Taxation Act, 2007, s 31](https://www.ontario.ca/laws/statute/07t11) |
| Skill version | 1.2 |

## Section 2 -- Entity Types Comparison

**Entity Types Comparison**

| Feature | Sole Proprietorship | Partnership (GP/LP) | Federal Corporation (CBCA) | Provincial Corporation | Cooperative |
| --- | --- | --- | --- | --- | --- |
| Legal personality | No | No (GP) / LP has some | Yes | Yes | Yes |
| Liability | Unlimited | GP: Unlimited; LP: Limited for limited partners | Limited | Limited | Limited |
| Min. founders | 1 | 2 | 1 shareholder + 1 director | Varies by province | Per applicable Act |
| Min. share capital | N/A | N/A | No minimum | No minimum (most provinces) | Per applicable Act |
| Jurisdiction | Province of residence | Province | Canada-wide (right to carry on business nationally) | Province of incorporation (must extra-provincially register elsewhere) | Federal or provincial |
| Tax treatment | Personal | Partners taxed individually | Corporate | Corporate | Corporate (special rules) |
| Name protection | Province only | Province only | Canada-wide | Province only | Varies |

**Federal vs Provincial Incorporation -- Key Decision**

| Factor | Federal (CBCA) | Provincial |
| --- | --- | --- |
| Name protection | Canada-wide | Province only |
| Right to operate | All provinces (must extra-provincially register) | Province of incorporation (must extra-provincially register in others) |
| Annual filing | With Corporations Canada + each province of registration | With provincial registry only |
| Cost | $200 + extra-provincial fees | Province-specific (e.g., Ontario $300 online) |
| Director residency | Generally at least 25% resident Canadians, with at least 1 when there are fewer than 4 directors. Check the special rules in [CBCA s 105(3)–(4)](https://laws-lois.justice.gc.ca/eng/acts/C-44/section-105.html). | Ontario repealed its general residency requirement on 5 July 2021. Check the applicable law in other provinces. [Ontario Business Corporations Act s 118](https://www.ontario.ca/laws/statute/90b16#BK98) |

**Recommended default:** Federal incorporation for businesses operating in multiple provinces. Provincial for single-province operations.

## Section 3 -- Registration Process (Federal)

### Step 1: Choose Corporate Name or Number

- **Corporate name/number rules** — Numbered corporation: no name search required (e.g., "12345678 Canada Inc."). Named corporation: NUANS name search included in online filing process. Name must include a legal element: "Inc.", "Incorporated", "Corporation", "Corp.", "Ltd.", "Limited", "Ltée", "Limitée"

### Step 2: Prepare Articles of Incorporation

Share classes and rights
Restrictions on share transfers (if any)
Number of directors (fixed or min/max range)
Restrictions on business activities (if any)
Provisions for financial year-end

### Step 3: File Online with Corporations Canada

- **Filing process** — Use Online Filing Centre at corporationscanada.ic.gc.ca. Fee: $200 (online); $250 (email/mail); +$100 for express (4 business hours). Certificate of Incorporation issued typically within 1 business day (online)

### Step 4: Extra-Provincial Registration

- **Extra-provincial registration process** — Federal corporation must register in each province where it carries on business. E.g., Ontario: file Form 2 with ServiceOntario; BC: extra-provincial registration with BC Registry. Fees vary: typically $0--$520 per province

### Step 5: Confirm the business number and applicable accounts

Federal incorporation and incorporation in Ontario automatically assign a business number (BN) and a corporation income tax (RC) account. Confirm those identifiers before applying for additional accounts. Determine obligations for GST/HST, payroll and imports separately. [CRA corporation income tax account](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/business-registration/business-number-program-account/need-program-accounts/corporation-income-tax.html)

### Step 6: Municipal Business Licence (if required)

Some municipalities require a business licence
Check with local municipality

## Section 4 -- Capital Requirements

**Capital Requirements**

| Entity Type | Min. Share Capital | Min. Paid-Up | Payment Timing | In-Kind Contributions |
| --- | --- | --- | --- | --- |
| Federal Corporation (CBCA) | No minimum | No minimum | As per share terms | Permitted (no statutory valuation requirement, but directors have fiduciary duties) |
| Ontario Corporation (OBCA) | No minimum | No minimum | As per share terms | Permitted |
| BC Corporation (BCBCA) | No minimum | No minimum | As per share terms | Permitted |
| Quebec Corporation (QBCA) | No minimum | No minimum | As per share terms | Permitted |

Canada has no minimum capital requirements for private corporation formation at any level.

## Section 5 -- Costs Breakdown

### Federal Incorporation

**Federal Incorporation Costs**

| Cost Component | Amount (CAD) | Notes |
| --- | --- | --- |
| Corporations Canada (online) | $200 | Standard (1 business day) |
| Express service | +$100 | 4 business hours |
| Extra-provincial registration (per province) | $0--$520 | Varies; Ontario ~$0; BC ~$350; QC ~$400 |
| NUANS name search (if named) | Included online | Separate $25 if pre-ordered |
| **Total federal + 1 province** | **$280--$600** | Government fees only |

### Provincial Incorporation (Examples)

**Provincial Incorporation Fees**

| Province | Online Fee | Notes |
| --- | --- | --- |
| Ontario | $300 | ServiceOntario |
| British Columbia | $350 | BC Registry Services |
| Alberta | $283.25 | Alberta Corporate Registry |
| Quebec | $397 | Registraire des entreprises |

### Annual Maintenance

**Annual Maintenance Costs**

| Item | Cost (CAD) |
| --- | --- |
| Corporations Canada annual return | $12 (online) / $20 (paper) |
| Provincial annual return | $0--$50 per province |
| Accountant fees | $1,500--$5,000/year |
| Corporate tax return (T2) | Included in accountant fees |
| Extra-provincial renewal fees | Varies by province |

## Section 6 -- Post-Formation Compliance

**Post-Formation Compliance**

| Obligation | Deadline | Authority |
| --- | --- | --- |
| Annual return (federal) | Within 60 days of anniversary date | Corporations Canada |
| Annual return (provincial) | Varies by province | Provincial registry |
| T2 corporate tax return | 6 months after fiscal year-end | CRA |
| Corporate tax payment | 2 months after year-end (3 months for small CCPC) | CRA |
| GST/HST returns | Quarterly or annually | CRA |
| Payroll remittances | Monthly or as required | CRA |
| T4/T5 information slips | By last day of February | CRA |
| Directors' register and minutes | Maintain at registered office | Internal |
| Shareholder register | Maintain at registered office | Internal |

## Section 7 -- Bank Account Opening

### Documents Typically Required

- **Required documents** — Certificate of Incorporation (federal or provincial) Articles of Incorporation Directors' resolution authorising account opening Government-issued ID for all directors and signing authorities Business Number from CRA Proof of business address

### Typical Timeline

- **Bank account opening timeline** — 1--5 days (major Canadian banks for Canadian residents) 1--3 weeks (non-resident founders)

### Common Banks

Royal Bank of Canada (RBC), TD Bank, Scotiabank, BMO, CIBC (Big 5)
National Bank, Desjardins (QC) (large regional)
Wise Business, Airwallex (digital/international)

## Section 8 -- Foreign Founder Considerations

**Foreign Founder Considerations**

| Question | Answer |
| --- | --- |
| Non-resident directors allowed? | Federal corporations can appoint non-residents subject to the residency and other director qualifications in [CBCA s 105](https://laws-lois.justice.gc.ca/eng/acts/C-44/section-105.html). Ontario removed its general residency requirement from 5 July 2021. [Ontario Business Corporations Act s 118](https://www.ontario.ca/laws/statute/90b16#BK98) |
| Nominee directors | Permitted but must comply with CBCA fiduciary duties |
| Physical presence required? | No -- online filing accepted |
| Apostille requirements | Foreign documents may require authentication for banking |
| Foreign ownership restrictions | No general restrictions; Investment Canada Act review for large acquisitions or sensitive sectors |
| Social Insurance Number | Not required for incorporation; required for payroll if personally employed by the corporation |
| Non-resident tax implications | Non-resident corporations carrying on business in Canada are subject to Canadian tax on Canadian-source income |

## Section 9 -- Common Mistakes and Refusals

- **R-CA-F1 -- Director residency (federal)** — Check the board against CBCA s 105 before filing. For an ordinary federal corporation with 3 directors, 1 resident Canadian satisfies the general rule. Check subsections 105(3.1)–(4) for a prescribed business sector or applicable Canadian ownership or control rules. [CBCA s 105](https://laws-lois.justice.gc.ca/eng/acts/C-44/section-105.html)
- **R-CA-F2 -- Missing extra-provincial registration** — A federal corporation must register in each province where it carries on business. Operating without registration can result in the corporation being unable to maintain legal proceedings in that province.
- **R-CA-F3 -- GST/HST registration timing** — For an ordinary business under the standard $30,000 small supplier test, include qualifying worldwide taxable supplies, including zero-rated supplies, and applicable associates. Exclude financial services, sales of capital property and consideration attributable to goodwill under the statutory rule. A single-quarter excess normally requires charging GST/HST on the taxable domestic supply that crossed the threshold. Where the threshold is exceeded over 4 or fewer consecutive calendar quarters without a single-quarter excess, small supplier status normally ends at the end of the month following the quarter of excess. Charge from the first later taxable supply in Canada and generally apply for registration within 29 days of the date that triggers registration. Public service bodies, taxi businesses and other special cases have separate rules. [Excise Tax Act ss 148](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-148.html) [and 240](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-240.html) [CRA registration timing](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/when-register-charge.html)
- **R-CA-F4 -- Confusing incorporation with business registration** — Sole proprietors and partnerships register a business name; they do not incorporate. Incorporation creates a separate legal entity with limited liability. These are fundamentally different.
- **R-CA-F5 -- Shell company for non-resident tax avoidance** — A Canadian corporation is taxed on worldwide income. Using a Canadian corporation solely to hold passive investments or as a conduit without Canadian substance may attract CRA scrutiny and GAAR (General Anti-Avoidance Rule) application.

### Worked GST/HST registration examples

Both examples assume an ordinary domestic business using the regular method. The listed amounts are qualifying supplies before tax, with no associate amounts or exclusions.

**Single-quarter excess.** By 15 September 2026, an Ontario business has made $29,500 of qualifying supplies this quarter. Its next standard-rated Ontario sale that day is $1,000. That sale takes quarterly supplies to $30,500. Registration is effective no later than 15 September, and Ontario HST at 13% on the full $1,000 sale is $130. The application is due within 29 days, by 14 October. [CRA registration timing](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/when-register-charge.html) [CRA rates](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-which-rate.html)

```oa-check
name: Ontario single-quarter threshold crossing
inputs:
  prior_sales: 29500
  next_sale: 1000
  hst_rate: 0.13
steps:
  - quarter_sales: prior_sales + next_sale
  - hst_on_crossing_supply: round(next_sale * hst_rate, 2)
expected:
  quarter_sales: 30500
  hst_on_crossing_supply: 130
```

**Successive-quarter excess.** Another Ontario business with no prior qualifying supplies makes $7,000, $8,000, $9,000 and $7,500 in the 4 quarters of 2025. The total is $31,500. It remains a small supplier through 31 January 2026, assuming it has no single-quarter excess in that period. Its first later taxable domestic sale is $500 on 4 February, with $65 of Ontario HST at 13%. Registration is effective no later than 4 February and the application is due within 29 days, by 5 March. [CRA registration timing](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/when-register-charge.html) [CRA rates](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-which-rate.html)

```oa-check
name: Ontario successive-quarter threshold crossing
inputs:
  first_quarter: 7000
  second_quarter: 8000
  third_quarter: 9000
  fourth_quarter: 7500
  first_later_sale: 500
  hst_rate: 0.13
steps:
  - qualifying_supplies: first_quarter + second_quarter + third_quarter + fourth_quarter
  - hst_on_first_later_sale: round(first_later_sale * hst_rate, 2)
expected:
  qualifying_supplies: 31500
  hst_on_first_later_sale: 65
```

## Section 10 -- Timeline

**Timeline**

| Step | Duration | Cumulative |
| --- | --- | --- |
| Decide federal vs provincial | 1 day | Day 1 |
| Prepare articles of incorporation | 1--3 days | Day 2--4 |
| File online (federal or provincial) | 1 day | Day 3--5 |
| Certificate of Incorporation received | 1 day (federal online) | Day 3--6 |
| Extra-provincial registration(s) | 1--10 days per province | Day 4--16 |
| CRA Business Number and tax accounts | 1--5 days (online) | Day 4--11 |
| Open bank account | 1--5 days (resident) / 1--3 weeks (non-resident) | Day 5--32 |
| **Ready to trade** |  | **As fast as 3--5 days (Canadian-resident, federal online)** |

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute legal, tax, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

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
