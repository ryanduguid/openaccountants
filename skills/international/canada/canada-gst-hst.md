---
name: canada-gst-hst
description: Use this skill whenever asked to prepare, review, or classify transactions for a Canadian GST/HST return (Form GST34) for a self-employed individual or small business in Canada. Trigger on phrases like "prepare GST return", "file HST", "Canadian sales tax", "GST/HST return", "Form GST34", "input tax credits", "ITC claim", or any request involving Canadian GST/HST filing. Also trigger when classifying transactions for GST/HST purposes from bank statements, invoices, or other source data. This skill covers federal GST and harmonized HST provinces only under the regular method. Quebec QST, Saskatchewan PST, Manitoba RST, British Columbia PST, Quick Method, and simplified method for charities are in the refusal catalogue. MUST be loaded alongside vat-workflow-base v0.1 or later (for workflow architecture). ALWAYS read this skill before touching any Canadian GST/HST work.
version: 2.2
jurisdiction: CA
category: international
tax_year: 2026
tax_year_notes: "Selected regular-method reporting, imported-services and input-tax-credit rules checked in November 2026. The worked purchases occur in April 2026."
last_updated: 2026-11-21
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Canada GST HST

## Canada GST/HST Return Skill (Form GST34) v2.2

## Section 1 — Quick reference

**Read this whole section before classifying anything. The workflow runbook is in `vat-workflow-base` Section 1 — follow that runbook with this skill providing the country-specific content.**

**Quick reference field table**

**Quick reference field table**

| Field | Value |
| --- | --- |
| Country | Canada |
| Federal GST rate | 5% |
| HST rates by province | ON 13%, NS 14% (effective Apr 1 2025), NB 15%, NL 15%, PE 15% |
| GST-only provinces | AB, BC, SK, MB, QC, NT, NU, YT (5% GST; BC/SK/MB/QC have separate provincial sales taxes) |
| Zero rate | 0% (basic groceries, prescription drugs, medical devices, exports) |
| Exempt | Financial services, residential rent, most health/dental/legal aid, childcare |
| Return form | GST34 (GST/HST Return for Registrants) |
| Filing portal | CRA My Business Account (canada.ca) |
| Authority | Canada Revenue Agency (CRA) |
| Currency | CAD only |
| Filing frequencies | Annual (taxable supplies <= $1.5M), Quarterly ($1.5M–$6M), Monthly (> $6M or voluntary election) |
| Deadline | Monthly/quarterly: 1 month after period end; Annual: 3 months after fiscal year end (individuals: June 15 but payment due April 30) |
| Small supplier threshold | $30,000 in any single calendar quarter or in the last four consecutive calendar quarters (ETA s.148) |
| Companion skill (Tier 1, workflow) | **vat-workflow-base v0.1 or later — MUST be loaded** |
| Contributor | Open Accounting Skills Community |
| Validation date | April 2026 baseline. Selected return-line, imported services, export consulting and input tax credit rules checked in November 2026. |

**Key GST34 lines**

| Line | Meaning |
| --- | --- |
| 101 | Total sales and other revenue (before GST/HST) |
| 103 | GST/HST collected or collectible |
| 104 | Adjustments to GST/HST (e.g., bad debt recovery, change-in-use) |
| 105 | Total GST/HST and adjustments (= 103 + 104) |
| 106 | Input tax credits (ITCs) |
| 107 | Adjustments to ITCs (e.g., recapture of ITCs on large business inputs — expired 2018) |
| 108 | Total ITCs and adjustments (= 106 + 107) |
| 109 | Net tax (= 105 − 108; positive = owing, negative = refund) |
| 110 | Instalments paid |
| 111 | Rebates claimed |
| 112 | Total other credits (= 110 + 111) |
| 113 | Balance (= 109 − 112; positive = amount owing) |
| 114 | Refund claimed |
| 115 | Amount owing |

**GST/HST rates by province (complete)**

| Province/Territory | Rate | Components | Effective |
| --- | --- | --- | --- |
| Alberta (AB) | 5% | GST only | — |
| British Columbia (BC) | 5% GST + 7% PST | Separate PST (not on GST34) | — |
| Manitoba (MB) | 5% GST + 7% RST | Separate RST (not on GST34) | — |
| New Brunswick (NB) | 15% HST | Harmonized | — |
| Newfoundland & Labrador (NL) | 15% HST | Harmonized | — |
| Northwest Territories (NT) | 5% | GST only | — |
| Nova Scotia (NS) | 14% HST | Harmonized | Apr 1, 2025 |
| Nunavut (NU) | 5% | GST only | — |
| Ontario (ON) | 13% HST | Harmonized | — |
| Prince Edward Island (PE) | 15% HST | Harmonized | — |
| Quebec (QC) | 5% GST + 9.975% QST | Separate QST (filed with Revenu Quebec) | — |
| Saskatchewan (SK) | 5% GST + 6% PST | Separate PST (not on GST34) | — |
| Yukon (YT) | 5% | GST only | — |

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown rate on a sale | HST at rate of province of supply (default ON 13% if province unknown) |
| Unknown GST/HST status of a purchase | Not eligible for ITC |
| Unknown province of supply | Province of registration |
| Unknown business-use proportion (vehicle, phone, home office) | 0% ITC |
| Unknown whether personal or business expense | Personal (no ITC) |
| Unknown blocked-input status (club dues, personal) | Blocked |
| Unknown whether transaction is in scope | In scope |

**Red flag thresholds**

| Threshold | Value |
| --- | --- |
| HIGH single-transaction size | CAD 5,000 |
| HIGH tax-delta on a single conservative default | CAD 400 |
| MEDIUM counterparty concentration | >40% of output OR input |
| MEDIUM conservative-default count | >4 across the return |
| LOW absolute net tax position | CAD 10,000 |

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the period in CSV, PDF, or pasted text. Must cover the full period. Acceptable from any Canadian or international business bank: RBC, TD, Scotiabank, BMO, CIBC, National Bank, Desjardins, Tangerine, Simplii, EQ Bank, Revolut Business, Wise Business, or any other.

**Recommended** — sales invoices for the period (especially for zero-rated exports and interprovincial supplies), purchase invoices for any ITC claim above CAD 400, the client's GST/HST Business Number (BN format: 123456789RT0001).

**Ideal** — complete sales journal, purchase journal, prior period GST34, Quick Method election (if applicable — but then R-CA-3 fires).

**Refusal policy if minimum is missing — SOFT WARN.** If no bank statement is available at all, hard stop. If bank statement only without invoices, proceed but record in reviewer brief: "This GST34 was produced from bank statement alone. The reviewer must verify that ITC claims above CAD 400 are supported by compliant invoices containing the supplier's BN and that place-of-supply determinations are correct."

### Canada-specific refusal catalogue

- **R-CA-1 — Quebec QST** — Quebec Sales Tax (QST) is administered by Revenu Quebec and filed separately from the federal GST return. This skill covers federal GST/HST (Form GST34) only. For QST, please use a CPA familiar with Quebec tax administration. (Trigger: client is in Quebec or asks about QST filing.)
- **R-CA-2 — Provincial sales tax (BC PST, SK PST, MB RST)** — Provincial sales taxes (BC PST, SK PST, MB RST) are separate from GST/HST and filed with the respective provincial authority. This skill covers the federal GST/HST return only. (Trigger: client asks about BC PST, Saskatchewan PST, or Manitoba RST filing.)
- **R-CA-3 — Quick Method** — The Quick Method calculates GST/HST remittance as a percentage of GST/HST-included revenue rather than tracking actual ITCs. This skill covers the regular method only. For Quick Method returns, apply the prescribed remittance rate for your sector and province. (Trigger: client has elected the Quick Method of accounting (GST74).)
- **R-CA-4 — Simplified method for charities/NPOs** — Charities, NPOs, and public service bodies have special GST/HST rules including the net tax calculation and public service body rebates. Out of scope. (Trigger: client is a registered charity, NPO, or public service body using the simplified method or net tax calculation.)
- **R-CA-5 — First Nations exemptions** — First Nations tax exemptions under the Indian Act (section 87) have specific rules that are outside the scope of this skill. Please consult a tax professional experienced in Indigenous tax matters. (Trigger: client asks about tax exemptions under the Indian Act or supplies on reserve.)
- **R-CA-6 — GST/HST groups (closely related corporations)** — Closely related group elections under s.156 involve intercompany supply rules that are out of scope. Please use a CPA. (Trigger: client is part of a GST/HST group election under ETA s.156.)
- **R-CA-7 — Non-resident simplified registration** — The simplified registration framework for non-resident digital economy businesses has different rules. Out of scope. (Trigger: non-resident registrant under the simplified registration framework.)
- **R-CA-8 — Real property transactions** — Real property transactions involve self-supply rules (s.191), change-of-use rules, and rebate calculations that are too fact-sensitive for this skill. Please use a CPA. (Trigger: client is buying/selling real property (land, buildings) with self-supply or change-of-use implications.)

## Section 3 — Supplier pattern library (the lookup table)

This is the deterministic pre-classifier. When a transaction's counterparty matches a pattern in this table, apply the treatment directly. If none match, fall through to Tier 1 rules in Section 5.

**How to read this table.** Match by case-insensitive substring on the counterparty name. If multiple patterns match, use the most specific.

### 3.1 Canadian banks (fees exempt — exclude)

**Canadian banks table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| RBC, ROYAL BANK OF CANADA | EXCLUDE for bank charges/fees | ETA Schedule V, Part VII: financial service, exempt |
| TD, TORONTO-DOMINION, TD CANADA TRUST | EXCLUDE for bank charges/fees | Same |
| SCOTIABANK, BANK OF NOVA SCOTIA | EXCLUDE for bank charges/fees | Same |
| BMO, BANK OF MONTREAL | EXCLUDE for bank charges/fees | Same |
| CIBC, CANADIAN IMPERIAL | EXCLUDE for bank charges/fees | Same |
| NATIONAL BANK, BNC, BANQUE NATIONALE | EXCLUDE for bank charges/fees | Same |
| DESJARDINS, CAISSE POPULAIRE | EXCLUDE for bank charges/fees | Same |
| TANGERINE, SIMPLII, EQ BANK | EXCLUDE for bank charges/fees | Same |
| REVOLUT, WISE, N26 (fee lines) | EXCLUDE for transaction/maintenance fees | Check for separate taxable subscription invoices |
| INTEREST, INTERET | EXCLUDE | Interest income/expense, exempt |
| MORTGAGE, HYPOTHEQUE, LOAN | EXCLUDE | Loan principal movement, out of scope |

### 3.2 Canadian government and statutory bodies (exclude entirely)

**Government bodies table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| CRA, CANADA REVENUE AGENCY, RECEIVER GENERAL | EXCLUDE | Tax payment (GST remittance, income tax instalment) |
| REVENU QUEBEC | EXCLUDE | QST or income tax payment |
| CPP, CANADA PENSION PLAN | EXCLUDE | Pension contribution, not a supply |
| EI, EMPLOYMENT INSURANCE | EXCLUDE | Employment insurance premium |
| WSIB, WCB, CNESST | EXCLUDE | Workers compensation |
| SERVICE CANADA, SERVICE ONTARIO | EXCLUDE | Government fees, sovereign act |
| CITY OF, VILLE DE, MUNICIPAL | EXCLUDE | Municipal tax/fee |

### 3.3 Canadian utilities

**Canadian utilities table**

| Pattern | Treatment | Rate | Notes |
| --- | --- | --- | --- |
| HYDRO ONE, TORONTO HYDRO, BC HYDRO, HYDRO-QUEBEC | Taxable | GST/HST at provincial rate | Electricity — overhead |
| ENBRIDGE, FORTISBC, ATCO GAS | Taxable | GST/HST at provincial rate | Gas — overhead |
| TELUS | Taxable | GST/HST at provincial rate | Telecoms — overhead |
| ROGERS, ROGERS COMMUNICATIONS | Taxable | GST/HST at provincial rate | Telecoms — overhead |
| BELL, BELL CANADA, BELL MOBILITY | Taxable | GST/HST at provincial rate | Telecoms — overhead |
| SHAW, COGECO, VIDEOTRON | Taxable | GST/HST at provincial rate | Telecoms — overhead |
| FIDO, KOODO, VIRGIN PLUS, FREEDOM MOBILE | Taxable | GST/HST at provincial rate | Telecoms — overhead |

### 3.4 Insurance (exempt — exclude)

**Insurance table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| MANULIFE, SUN LIFE, GREAT-WEST LIFE, CANADA LIFE | EXCLUDE | Insurance, exempt (ETA Schedule V, Part VII) |
| INTACT, AVIVA, DESJARDINS ASSURANCE | EXCLUDE | Same |
| CO-OPERATORS, WAWANESA, ECONOMICAL | EXCLUDE | Same |
| INSURANCE, ASSURANCE | EXCLUDE | All exempt |

### 3.5 Post and logistics

**Post and logistics table**

| Pattern | Treatment | Rate | Notes |
| --- | --- | --- | --- |
| CANADA POST, POSTES CANADA | EXCLUDE for standard letter mail |  | Exempt (ETA Schedule V, Part VII.1) |
| CANADA POST (courier, Xpresspost, Priority) | Taxable | GST/HST | Non-universal services are taxable |
| PUROLATOR | Taxable | GST/HST | Express courier |
| FEDEX CANADA, UPS CANADA, DHL CANADA | Taxable | GST/HST | Courier services |
| CANPAR, DICOM, LOOMIS | Taxable | GST/HST | Courier services |

### 3.6 Transport

**Transport table**

| Pattern | Treatment | Rate | Notes |
| --- | --- | --- | --- |
| VIA RAIL | Taxable | GST/HST | Domestic passenger rail |
| GO TRANSIT, TTC, STM, TRANSLINK, OC TRANSPO | EXCLUDE or zero-rated |  | Municipal transit — zero-rated per ETA Schedule VI, Part VII |
| UBER CANADA | Taxable | GST/HST | Ride-sharing; platform is GST-registered |
| LYFT | Taxable | GST/HST | Same |
| AIR CANADA (international) | Zero-rated | 0% | International transport — Schedule VI, Part VII |
| AIR CANADA (domestic) | Taxable | GST/HST | Domestic air |
| WESTJET (international) | Zero-rated | 0% | International |
| WESTJET (domestic) | Taxable | GST/HST | Domestic air |
| ENTERPRISE, HERTZ, AVIS, BUDGET (car rental) | Taxable | GST/HST at location rate | Car rental — ITC restricted if personal use |

### 3.7 Food retail (generally zero-rated basic groceries — but personal)

**Food retail table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TIM HORTONS, TIMS | Default BLOCK ITC | Restaurant/prepared food is taxable at GST/HST, but personal unless hospitality business |
| STARBUCKS, MCDONALDS, SUBWAY, A&W | Default BLOCK ITC | Same — prepared food/beverages are taxable but likely personal |
| LOBLAWS, NO FRILLS, REAL CANADIAN, SUPERSTORE | Default BLOCK ITC | Grocery — mix of zero-rated and taxable items; personal provisioning default |
| METRO, SOBEYS, SAFEWAY, IGA, SAVE-ON-FOODS | Default BLOCK ITC | Same |
| COSTCO, WALMART (grocery) | Default BLOCK ITC | Mixed supply — personal default |
| CANADIAN TIRE (non-food) | Taxable | GST/HST — ITC eligible if business purpose confirmed |

### 3.8 Services and intangible property bought from non-residents

Use the invoice, the contracting supplier or platform and its registration status. For a taxable supply under normal GST/HST registration, verify the tax charged, commercial use and supporting records before assigning an input tax credit (ITC). For a supply under the simplified digital economy regime, a normal registrant provides its registration evidence to the supplier or platform. The CRA says tax charged under the simplified regime when that evidence is missing does not qualify for an ITC or a rebate for tax paid in error. [CRA cross-border digital supplies](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/digital-economy-gsthst/charge-collect/cross-border.html)

For a service or intangible personal property supplied outside Canada to a Canadian resident, test the imported-taxable-supply definition and its exclusions. For an ordinary business other than a financial institution, the commercial-use exclusion generally applies where 90% or more of the acquisition is for commercial activities. Check the nature and place of supply, use and tax separately when the invoice shows no GST/HST. See section 5.7 for cases in which tax is payable. [Excise Tax Act s 217](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-217.html) · [Excise Tax Act s 141](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-141.html) · [CRA line 405 instructions](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/instructions-preparing-return.html)

### 3.9 Canadian SaaS / domestic suppliers (ITC-eligible)

**Canadian SaaS table**

| Pattern | Treatment | Rate | Notes |
| --- | --- | --- | --- |
| SHOPIFY | Taxable domestic | GST/HST (ON entity, 13% HST) | Platform subscription — ITC eligible |
| STRIPE PAYMENTS CANADA | Taxable domestic or exempt | Check invoice | Transaction fees may be exempt financial service; subscription taxable |
| WEALTHSIMPLE | EXCLUDE (exempt) | — | Financial service |
| FRESHBOOKS | Taxable domestic | GST/HST | Accounting software |
| WAVE FINANCIAL | Taxable domestic | GST/HST | Accounting software (now owned by H&R Block) |
| HOOTSUITE | Taxable domestic | GST/HST | Social media management |

### 3.10 Payment processors

**Payment processors table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| STRIPE (transaction fees) | EXCLUDE (exempt) | Payment processing fees are exempt financial services |
| PAYPAL (transaction fees) | EXCLUDE (exempt) | Same |
| SQUARE, MONERIS, GLOBAL PAYMENTS | Check invoice | Transaction fees exempt; hardware/subscription taxable |
| INTERAC | EXCLUDE (exempt) | Interac fees are financial services |

### 3.11 CRA payments and refunds

**CRA payments table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| CRA GST PAYMENT, RECEIVER GENERAL GST | EXCLUDE | GST remittance — not a supply |
| CRA INCOME TAX, INSTALMENT PAYMENT | EXCLUDE | Income tax — not a supply |
| CRA REFUND, GST REFUND | EXCLUDE | Government refund — not a supply |
| CRA CEBA, CEWS, CERS | EXCLUDE | Government subsidy — not a supply (but may have GST implications on repayment) |

### 3.12 Professional services (Canada)

**Professional services table**

| Pattern | Treatment | Rate | Notes |
| --- | --- | --- | --- |
| CPA, CHARTERED PROFESSIONAL ACCOUNTANT | Taxable | GST/HST | Always ITC-eligible |
| LAWYER, LAW OFFICE, BARRISTERS | Taxable | GST/HST | ITC-eligible if business purpose |
| NOTARY, NOTAIRE | Taxable | GST/HST | ITC-eligible if business purpose |
| CONSULTANT, CONSULTING | Taxable | GST/HST | ITC-eligible if business purpose |

### 3.13 Payroll (exclude entirely)

**Payroll table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| PAYROLL, SALARY, WAGES | EXCLUDE | Wages — outside GST/HST scope |
| CPP CONTRIBUTION | EXCLUDE | Pension contribution |
| EI PREMIUM | EXCLUDE | Employment insurance |
| CERIDIAN, ADP, PAYWORKS | EXCLUDE for payroll runs | Payroll processing fee itself may be taxable |

### 3.14 Property and rent

**Property and rent table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| RENT, LOYER (commercial) | Taxable | Commercial lease — GST/HST on rent, ITC eligible |
| RENT, LOYER (residential) | EXCLUDE | Residential lease exempt (ETA Schedule V, Part I) |
| CONDO FEES, STRATA FEES | EXCLUDE if residential | Residential condo fees exempt |
| PROPERTY TAX, MUNICIPAL TAX | EXCLUDE | Government levy, not a supply |

### 3.15 Internal transfers and exclusions

**Internal transfers table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TRANSFER, E-TRANSFER (own accounts) | EXCLUDE | Internal movement |
| INTERAC E-TRANSFER (to self) | EXCLUDE | Internal movement |
| DIVIDEND | EXCLUDE | Dividend payment, out of scope |
| LOAN REPAYMENT | EXCLUDE | Loan principal, out of scope |
| ATM WITHDRAWAL | TIER 2 — ask | Default exclude; ask what cash was spent on |
| OWNER DRAW, SHAREHOLDER LOAN | EXCLUDE | Owner withdrawal |

## Section 4 — Worked examples

These are six fully worked classifications drawn from a hypothetical bank statement of an Ontario-based self-employed software consultant.

### Example 1 — Imported service with mixed use

An ordinary Ontario-based GST/HST registrant acquires a remote database support service in April 2026. Assume the CAD 1,000 taxable service is supplied outside Canada to the registrant, the supplier charges no GST/HST, the full consideration is due in April and none of the section 217 exclusions applies. The service is acquired for use wholly in Ontario and 60% in commercial activities. The registrant self-assesses CAD 50 of federal GST and CAD 80 of the Ontario component on line 405, for a total of CAD 130. The ITC is CAD 78 on line 106 when the general conditions and documentation are met. The remaining CAD 52 is the net increase after the ITC. [Excise Tax Act ss 217–219](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-217.html) · [Provincial component, s 218.1](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-218.1.html) · [HST Regulations No. 2 s 7](https://laws-lois.justice.gc.ca/eng/regulations/SOR-2010-151/section-7.html) · [Excise Tax Act s 169](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-169.html) · [CRA return instructions](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/instructions-preparing-return.html)

If the same service is instead acquired entirely for the registrant’s commercial activities, the section 217 exclusion applies on these facts. There is no line 405 amount or ITC for self-assessed tax in that case. Determine the allocation from the underlying use and keep the supporting records. [Excise Tax Act s 217](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-217.html) · [CRA return instructions](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/instructions-preparing-return.html)

```oa-check
name: Ontario imported service with 60% commercial use
inputs:
  value: 1000
  federal_rate: 0.05
  ontario_rate: 0.08
  ontario_fraction: 1
  commercial_fraction: 0.6
steps:
  - federal_tax: value * federal_rate
  - ontario_tax: value * ontario_rate * ontario_fraction
  - line_405: federal_tax + ontario_tax
  - line_106: line_405 * commercial_fraction
  - net_increase: line_405 - line_106
expected:
  federal_tax: 50
  ontario_tax: 80
  line_405: 130
  line_106: 78
  net_increase: 52
```

### Example 2 — Domestic purchase with HST (Shopify)

`2026-04-10 ; SHOPIFY COMMERCE INC ; DEBIT ; Monthly plan ; -49.00 ; CAD`

Shopify is an Ontario-headquartered Canadian company. They charge 13% HST. The CAD 49.00 is the HST-inclusive price. Net = 49.00 / 1.13 = 43.36. HST = 5.64. Full ITC eligible on Line 106 for business software.

**Output table**

| Date | Counterparty | Gross | Net | GST/HST | Rate | Line | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-04-10 | SHOPIFY | -49.00 | -43.36 | -5.64 | 13% HST | 106 | N | — | — |

### Example 3 — Entertainment, restricted ITC

`2026-04-15 ; THE KEG STEAKHOUSE ; DEBIT ; Client dinner ; -285.00 ; CAD`

Hold the credit until the invoice and business purpose are confirmed. When the confirmed meal is reasonable, relates to commercial activities and is subject to the ordinary 50% income tax limit, apply the 50% GST/HST rule in section 5.10. [Excise Tax Act s 236](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-236.html) · [Income Tax Act s 67.1](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-67.1.html) · [CRA meal and entertainment expenses](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4022/general-information-gst-hst-registrants.html)

**Output table**

| Date | Counterparty | Gross | Net | GST/HST | Rate | Line | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-04-15 | THE KEG STEAKHOUSE | -285.00 | -285.00 | 0 | — | — | Y | Q1 | "Meals/entertainment: blocked (conservative)" |

### Example 4 — Capital equipment

`2026-04-18 ; APPLE STORE YORKDALE ; DEBIT ; MacBook Pro 16 ; -3,729.00 ; CAD`

The Ontario purchase invoice shows CAD 3,729 including 13% HST. Assume the registrant acquires the computer for use wholly in commercial activities and holds the required records. CAD 3,729 divided by 1.13 gives CAD 3,300 for the equipment and CAD 429 of HST, claimed on line 106. [Excise Tax Act s 169](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-169.html) · [Excise Tax Act s 199](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-199.html) · [CRA ITC eligibility for capital personal property](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/input-tax-credit/calculate-eligibility-percentage.html)

**Output table**

| Date | Counterparty | Gross | Net | GST/HST | Rate | Line | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-04-18 | APPLE STORE | -3,729.00 | -3,300.00 | -429.00 | 13% HST | 106 | N | — | — |

```oa-check
name: Ontario capital equipment bought wholly for commercial use
inputs:
  gross: 3729
  hst_rate: 0.13
steps:
  - before_tax: round(gross / (1 + hst_rate), 2)
  - line_106: round(gross - before_tax, 2)
expected:
  before_tax: 3300
  line_106: 429
```

### Example 5 — Export sale (zero-rated)

`2026-04-22 ; ACME CORP USA ; CREDIT ; Invoice CA-2026-018 IT consulting March ; +5,500.00 ; CAD`

A Canadian registrant earns CAD 5,500 for advisory IT work. Its contract and work records establish that the advisory service was supplied to the US company as a non-resident, without any of the exclusions in paragraphs 23(a) to (d). Confirm the contracting recipient and service scope before applying the zero rate. The $5,500 is regular-method revenue on line 101, with $0 tax on line 103. If reporting separately online, include the zero-rated export on line 91. Apply the ordinary input tax credit eligibility and documentary rules. [Excise Tax Act, Schedule VI, Part V, s 23](https://laws-lois.justice.gc.ca/eng/acts/e-15/page-121.html) [CRA export services memorandum](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/4-5-3/exports-services-intangible-personal-property.html) [CRA return instructions](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4022/general-information-gst-hst-registrants.html)

**Output table**

| Date | Counterparty | Gross | Net | GST/HST | Rate | Line | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-04-22 | ACME CORP USA | +5,500.00 | +5,500.00 | 0 | 0% | 101 (91 if separated online) | N | Q2 (HIGH) | Verify the recipient and section 23 exclusions |

### Example 6 — Vehicle costs, restricted ITC

`2026-04-28 ; PETRO-CANADA ; DEBIT ; Fuel ; -92.00 ; CAD`

Fuel purchase. In Canada, there is no blanket block on vehicle expenses (unlike Malta). ITCs are claimable to the extent of business use. For a passenger vehicle, the taxpayer must track business vs personal kilometers. Conservative default: 0% ITC (personal use assumed). If the taxpayer maintains a logbook showing, say, 60% business use, 60% of the GST/HST is claimable.

**Output table**

| Date | Counterparty | Gross | Net | GST/HST | Rate | Line | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-04-28 | PETRO-CANADA | -92.00 | -92.00 | 0 | — | — | Y | Q3 | "Vehicle fuel: 0% ITC (no logbook). Provide km logbook for partial ITC." |

### 5.1 GST at 5% (ETA s.165(1))

- **GST rate** — 5%  _(ETA s.165(1))_
- **GST applicability** — Federal component of all taxable supplies. Applies in GST-only provinces (AB, BC, SK, MB, NT, NU, YT). In these provinces, only 5% GST applies on the GST34. Provincial taxes (BC PST, SK PST, MB RST) are separate filings.  _(ETA s.165(1))_

### 5.2 HST at harmonized rates (ETA s.165(2))

- **HST harmonized rule** — In harmonized provinces (ON 13%, NS 14%, NB 15%, NL 15%, PE 15%), the HST replaces GST. The full HST amount is reported on the GST34. There is no separate provincial filing for HST provinces.  _(ETA s.165(2))_

### 5.3 Place of supply (SOR/2010-117)

- **Place of supply rule** — The rate depends on where the supply is made. For tangible personal property: province where delivery occurs. For services: generally the province of the recipient's business address. For intangible personal property: province where the property may be used. Interprovincial supplies require transaction-level place-of-supply determination.  _(SOR/2010-117)_

### 5.4 Zero-rated supplies (ETA Schedule VI)

- **Zero-rated supplies** — Basic groceries (Part III), prescription drugs (Part I), medical devices (Part II), exports of goods and qualifying services (Part V), international transport (Part VII), agricultural products (Part IV), financial services to non-residents (Part IX). Zero-rated means 0% tax but full ITC eligibility on related inputs.  _(ETA Schedule VI)_

### 5.5 Exempt supplies (ETA Schedule V)

- **Exempt supplies** — Financial services (Part VII), residential rent (Part I), health care services (Part II — but only listed services), educational services (Part III), childcare (Part IV), legal aid (Part V), public sector (Part VI). Exempt means no GST/HST charged and NO ITC on related inputs. If exempt supplies are significant → mixed-use apportionment required.  _(ETA Schedule V)_

### 5.6 Input tax credits (ETA s 169)

For ordinary supplier documentation, use the total amount paid or payable for the supplies shown on the document. The thresholds are CAD 100 and CAD 500, deemed effective from 20 April 2021. The CRA lists exceptions with different evidence requirements. [Input Tax Credit Information Regulations s 3](https://laws-lois.justice.gc.ca/eng/regulations/SOR-91-45/section-3.html) · [CRA records for an ITC claim](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/input-tax-credit.html)

- **Below CAD 100**. Keep the supplier or intermediary name, invoice date or tax paid or payable date if there is no invoice, and total amount paid or payable.
- **CAD 100 to below CAD 500**. Keep the preceding details plus the applicable GST/HST registration number, evidence of tax or tax-included amounts and the required taxable-supply designations if supplies have different tax statuses.
- **CAD 500 or more**. Also keep the recipient or authorised representative’s name, payment terms and a description that identifies each supply.

### 5.7 Self-assessment on imported taxable supplies (ETA ss 217–219)

For a qualifying imported taxable service or intangible supply, section 218 imposes 5% federal GST on the value of the consideration. Check the additional provincial component under section 218.1 separately. For ordinary residents of participating provinces, test the prescribed threshold of at least 10% use in participating provinces and compute each component using the extent of use in that province. A billing address alone is insufficient. [Excise Tax Act s 218](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-218.html) · [Excise Tax Act s 218.1](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-218.1.html) · [HST Regulations No. 2 s 7](https://laws-lois.justice.gc.ca/eng/regulations/SOR-2010-151/section-7.html)

An ordinary registrant reports applicable self-assessed tax on line 405 of the return for the reporting period in which it became payable. Calculate the ITC separately using eligible commercial use and sufficient records before filing. The general rule in section 169 applies subject to its conditions and other restrictions. For non-registrants and qualifying taxpayers, check the separate return and payment rules. This section covers ordinary services and intangible property from outside Canada. Verify imported goods, interprovincial transfers and special financial institution rules separately. [Excise Tax Act s 219](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-219.html) · [Excise Tax Act s 169](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-169.html) · [CRA return instructions](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/instructions-preparing-return.html)

### 5.8 Capital personal property and passenger vehicles (ETA ss 199, 201–202)

- **Ordinary capital equipment**. For most capital personal property, a registrant other than a financial institution generally tests whether the commercial use exceeds 50%. Identify passenger vehicles, aircraft and other special cases before applying the ordinary rule. [Excise Tax Act s 199](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-199.html) · [CRA ITC eligibility for capital personal property](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/input-tax-credit/calculate-eligibility-percentage.html)
- **Passenger vehicles acquired as capital property**. Section 201 limits the tax used for the ITC calculation by reference to the applicable income tax capital-cost ceiling. Section 202 has separate rules for improvements and for individuals or partnerships with mixed-use vehicles. For Class 10.1, the 2025 ceiling was CAD 38,000 before tax. The Department of Finance and CRA give CAD 39,000 before tax for 2026 acquisitions. The consolidated regulation still shows CAD 38,000 for acquisitions after 2024. Confirm the operative provision before calculating a 2026 vehicle ITC. [Excise Tax Act s 201](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-201.html) · [Excise Tax Act s 202](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-202.html) · [Income Tax Regulations s 7307](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-7307.html) · [Finance Canada 2026 limits](https://www.canada.ca/en/department-finance/news/2026/01/government-announces-the-2026-automobile-deduction-limits-and-expense-benefit-rates-for-businesses.html) · [CRA Class 10.1 guidance](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4012/t2-corporation-income-tax-guide-chapter-3-page-3-t2-return.html)

### 5.9 Blocked ITCs (ETA s.170)

- **Blocked ITCs** — - Club memberships (golf, fitness, social clubs) — ETA s.170(1)(a) — fully blocked - Personal expenses — ETA s.170(1)(b) — fully blocked - Gifts over $50 (except food/drink) — limited - Passenger vehicles: not blocked per se but limited to business-use proportion and CCA ceiling  _(ETA s.170)_

### 5.10 Meals and entertainment — 50% rule

When reasonable commercial meals and entertainment are subject to the 50% income tax limit, CRA guidance allows claiming 50% of the eligible GST/HST in each period, or claiming it in full and making the required adjustment. Test any exception against the statute. Check special rules for long-haul truck drivers, charities and public institutions separately. [Excise Tax Act s 236](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-236.html) · [Income Tax Act s 67.1](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-67.1.html) · [CRA meal and entertainment expenses](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4022/general-information-gst-hst-registrants.html)

### 5.11 Change in use of capital personal property (ETA s 199)

For ordinary capital personal property, a change across the more-than-50% commercial-use threshold may trigger a deemed acquisition or sale. For a deemed sale when commercial use falls to 50% or less, the CRA’s calculation uses basic tax content. Obtain the purchase, improvement, rebate and current valuation details before calculating the amount. Check the rules for vehicles, aircraft, real property and financial institutions separately. [Excise Tax Act s 199](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-199.html) · [CRA capital personal property change-in-use guidance](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4022/general-information-gst-hst-registrants.html)

### 5.12 Small supplier threshold (ETA s.148)

- **Standard small supplier test** — In the ordinary business case, test qualifying worldwide taxable supplies for a single calendar quarter and the preceding 4 calendar quarters, including applicable associate amounts and the statutory exclusions. The standard limit is $30,000. Voluntary registration and special registration rules are separate. [Excise Tax Act s 148](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-148.html)
- **Registration and collection** — For a single-quarter excess, the taxable domestic supply crossing the threshold triggers collection. If the threshold is exceeded over 4 or fewer consecutive quarters without a single-quarter excess, small supplier status normally ends at the end of the month following the quarter of excess. Start charging from the first taxable supply in Canada after that month. Apply to register within 29 days of the supply that triggers registration in these ordinary cases. [Excise Tax Act s 240](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-240.html) [CRA registration timing](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/when-register-charge.html)

### 5.13 Bad debts (ETA s.231)

- **Bad debt recovery rule** — If a registrant has previously reported GST/HST on a sale and the receivable becomes uncollectable, the GST/HST can be recovered via Line 107 (adjustment). Must be written off in the registrant's books. Recovery if the debt is later collected.  _(ETA s.231)_

### 5.14 Reporting sales on Line 101

- **Line 101, regular method** — Report the period's relevant revenue from taxable, zero-rated and exempt supplies and other reportable revenues. Exclude GST, HST, provincial sales tax and amounts previously reported. For the paper return, round to the nearest dollar. Line 103 separately shows GST/HST collected or collectible. [CRA regular-method return instructions](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4022/general-information-gst-hst-registrants.html)
- **Optional electronic breakdown** — When the regular-method filing interface offers the breakdown and you choose it, line 90 is for taxable supplies in Canada including domestic zero-rated supplies, and line 91 is for exempt supplies, zero-rated exports and other sales and revenues. The return populates line 101 from lines 90 and 91. Follow the separate line 102 instructions for associates where applicable. [CRA electronic return instructions](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4022/general-information-gst-hst-registrants.html)
- **Quick Method** — Use the separate CRA rules if this election applies. The regular-method worksheet here excludes taxes. [CRA Quick Method instructions](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4058/quick-method-accounting-gst-hst.html)

**Regular-method return example.** A fictional Ontario registrant has a $1,130 receipt for a standard-rated domestic sale that includes $130 HST, $300 of exempt supplies and the $5,500 zero-rated export in example 5. Its reportable revenue is $6,800, and it reports $130 separately as tax collected or collectible. In the optional electronic breakdown, line 90 is $1,000 and line 91 is $5,800. This example has no adjustments or associates. [CRA return instructions](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4022/general-information-gst-hst-registrants.html)

```oa-check
name: Regular-method line 101 excludes HST
inputs:
  domestic_receipt: 1130
  exempt_supplies: 300
  zero_rated_exports: 5500
  provincial_hst_rate: 0.13
steps:
  - line_90: round(domestic_receipt / (1 + provincial_hst_rate), 2)
  - line_91: exempt_supplies + zero_rated_exports
  - line_101: line_90 + line_91
  - line_103: domestic_receipt - line_90
expected:
  line_90: 1000
  line_91: 5800
  line_101: 6800
  line_103: 130
```

**Export calculation.** When example 5 qualifies for zero-rating under section 23, the $5,500 is revenue at 0%. The calculation assumes the legal classification has already been confirmed.

```oa-check
name: Qualified consulting export is revenue at the zero rate
inputs:
  fee: 5500
  export_rate: 0
steps:
  - reportable_revenue: fee
  - tax_on_export: round(fee * export_rate, 2)
expected:
  reportable_revenue: 5500
  tax_on_export: 0
```

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Vehicle costs

*Pattern:* Petro-Canada, Shell, Esso, Canadian Tire (auto), car payments. *Default:* 0% ITC (no logbook). *Question:* "Do you have a vehicle logbook showing business vs personal kilometers?"

### 6.2 Meals and entertainment

*Pattern:* restaurants, Tim Hortons, Starbucks, The Keg. *Default:* block. *Question:* "What was the commercial purpose and what tax does the receipt show?" Apply section 5.10 once confirmed.

### 6.3 Home office expenses

*Pattern:* utility bills, internet at home. *Default:* 0% ITC. *Question:* "Do you work from home? What percentage of your home is used exclusively for business?"

### 6.4 Round-number incoming transfers

*Pattern:* large round credit from owner name. *Default:* exclude as owner injection. *Question:* "Is this a customer payment, owner contribution, or loan?"

### 6.5 Incoming from individuals

*Pattern:* incoming from private names. *Default:* taxable sale at provincial HST rate, Line 101/103. *Question:* "Was it a sale? What was supplied?"

### 6.6 Interprovincial sales

*Pattern:* incoming from counterparty in different province. *Default:* rate of recipient's province. *Question:* "Confirm the province of the customer for place-of-supply determination."

### 6.7 Large purchases (potential capital asset)

*Pattern:* single purchase > CAD 1,000. *Default:* current expense on Line 106. *Question:* "Is this a capital asset with useful life > 1 year?"

### 6.8 Mixed-use phone, internet

*Pattern:* Rogers, Bell, Telus personal lines. *Default:* 0% if mixed. *Question:* "Is this a dedicated business line or mixed-use?"

### 6.9 Outgoing to individuals

*Pattern:* outgoing to private names. *Default:* exclude as draws. *Question:* "Was this a contractor payment, salary, refund, or personal transfer?"

### 6.10 Cash withdrawals

*Pattern:* ATM, cash withdrawal. *Default:* exclude. *Question:* "What was the cash used for?"

### 6.11 Rent payments

*Pattern:* monthly rent to landlord. *Default:* commercial (taxable, ITC eligible). *Question:* "Is this a commercial or residential lease?"

### 6.12 Amazon.ca purchases

*Pattern:* Amazon.ca, AMZN. *Default:* taxable domestic at HST rate. *Question:* "Was this a business purchase? Check invoice for GST/HST breakdown."

### 6.13 Stripe/PayPal incoming

*Pattern:* Stripe payouts, PayPal transfers. *Default:* sales revenue at provincial rate, Line 101/103. *Question:* "Are these customer payments? What province are your customers in?"

### 6.14 Tips and gratuities

*Pattern:* restaurant charges with tip component. *Default:* GST/HST only on pre-tip amount. *Question:* "Confirm pre-tip amount for ITC calculation."

### 6.15 US dollar transactions

*Pattern:* USD amounts on bank statement. *Default:* convert to CAD at Bank of Canada daily rate. *Question:* "Confirm the CAD equivalent shown on the bank statement."

## Section 7 — Excel working paper template (Canada-specific)

The base specification is in `vat-workflow-base` Section 3. This section provides the Canada-specific overlay.

### Sheet "Transactions"

Columns A–L per the base. Column H ("Line code") accepts GST34 line references (101, 103, 106, 405, etc.). Column I adds the GST/HST rate used (5%, 13%, 14%, 15%). For self-assessed imports, enter "405" in column H.

### Sheet "Line Summary"

- **Line Summary sheet formulas** — One row per GST34 line. Column A is the line number, column B is the description, column C is the value. ``` | 101 | Total sales and revenue | =SUM of all credit transactions (sales, zero-rated, exempt) | | 103 | GST/HST collected | =SUMIFS(Transactions!F:F, Transactions!G:G, "SALE") | | 105 | Total GST/HST and adjustments | =C[103]+C[104] | | 106 | Input tax credits | =SUMIFS(Transactions!F:F, Transactions!G:G, "ITC") | | 108 | Total ITCs and adjustments | =C[106]+C[107] | | 109 | Net tax | =C[105]-C[108] | | 405 | Tax self-assessed on imported supplies | =SUMIFS(Transactions!F:F, Transactions!H:H, "405") | ```

### Sheet "Return Form"

- **Return Form final figures** — Final GST34-ready figures: ``` Line 105 = Total GST/HST collected + adjustments Line 108 = Total ITCs + adjustments Line 109 = Line 105 - Line 108   [net tax] Line 113 = Line 109 - Line 112   [balance] Positive Line 113 → amount owing to CRA Negative Line 113 → refund claimed ```

### Mandatory recalc step

After building the workbook, run:

```bash
python /mnt/skills/public/xlsx/scripts/recalc.py /mnt/user-data/outputs/canada-gst-hst-<period>-working-paper.xlsx
```

## Section 8 — Canadian bank statement reading guide

Follow the universal exclusion rules in `vat-workflow-base` Step 6, plus these Canada-specific patterns.

**RBC Royal Bank online export format.** CSV export from RBC Online Banking. Columns: Account Type, Account Number, Transaction Date, Cheque Number, Description 1, Description 2, CAD$, USD$. Date format: MM/DD/YYYY. Amounts are positive for credits, negative for debits. Description 1 contains the transaction type (e.g., "POS Purchase", "Online Banking Transfer", "Direct Deposit"). Description 2 contains the counterparty/payee name.

**TD Canada Trust online export format.** CSV from EasyWeb. Columns: Date, Transaction Description, Debit, Credit, Balance. Date format: MM/DD/YYYY. The Transaction Description field combines type and payee (e.g., "POS W/D SHOPIFY COMMERCE INC", "INTERAC E-TRANSFER FROM JOHN SMITH"). "POS W/D" = point-of-sale withdrawal (debit). "PREAUTH PYMT" = pre-authorized payment.

**Scotiabank export format.** CSV from Scotia OnLine. Columns: Date, Description, Withdrawals, Deposits, Balance. Date format: DD/MM/YYYY (different from RBC/TD).

**BMO export format.** CSV from BMO Online Banking. Columns: Transaction Date, Description, Amount. Single amount column (negative for debits).

**CIBC export format.** CSV or QFX from CIBC Online. Columns: Date, Description, Debit, Credit. Date format: YYYY-MM-DD.

**Common Canadian bank statement patterns**

| Term | Meaning |
| --- | --- |
| POS, POS W/D, POS PURCHASE | Point-of-sale debit card purchase |
| PREAUTH, PREAUTH PYMT, PAP | Pre-authorized payment (direct debit) |
| INTERAC E-TRANSFER | Interac e-Transfer (incoming or outgoing) |
| ONLINE BANKING TRANSFER, TFR | Online transfer |
| DIRECT DEPOSIT, DIR DEP | Direct deposit (incoming) |
| CRA FED, RECEIVER GENERAL | CRA tax payment |
| NSF, NSF FEE | Non-sufficient funds fee (bank charge — exempt) |
| MONTHLY FEE, SERVICE CHARGE | Bank account fees (exempt) |
| INTL PURCHASE, FX FEE | International purchase and foreign exchange fee |
| ABM W/D, ATM | Cash withdrawal |

**Internal transfers.** Own-account transfers between client's RBC, TD, savings accounts. Labelled "online banking transfer", "TFR", or matching account numbers. Always exclude.

**Self-employed draws.** Transfers from business account to personal account labelled with the owner's name. Exclude.

**HST on bank statement lines.** Canadian invoices are GST/HST-inclusive on the bank statement. To extract the GST/HST component: Tax = Gross * Rate / (1 + Rate). Example: CAD 113.00 at 13% HST → Tax = 113 * 0.13 / 1.13 = 13.00.

**Interac e-Transfers.** Very common in Canada for B2B and B2C. The description shows "INTERAC E-TRANSFER FROM [name]" for incoming and "INTERAC E-TRANSFER TO [name]" for outgoing. Default treatment: incoming = potential sale (ask), outgoing = potential contractor payment or personal (ask).

**Foreign currency.** Convert to CAD using the Bank of Canada daily exchange rate. Note the rate in column L.

## Section 9 — Onboarding fallback (only when inference fails)

### 9.1 Entity type

*Inference rule:* "Inc", "Corp", "Ltd" = corporation; personal name = sole proprietor. *Fallback:* "Are you a sole proprietor, partnership, or corporation?"

### 9.2 GST/HST registration

*Inference rule:* if asking for a GST34, they are registered. *Fallback:* "Are you registered for GST/HST? What is your Business Number (BN)?"

### 9.3 Province

*Inference rule:* bank branch, counterparty mix, area codes in descriptions. *Fallback:* "What province is your principal place of business?"

### 9.4 Filing period

*Inference rule:* transaction date range. *Fallback:* "Is this for a monthly, quarterly, or annual period? What are the period dates?"

### 9.5 Accounting method

*Inference rule:* if no mention of Quick Method, assume regular. *Fallback:* "Are you using the regular method or the Quick Method (election GST74)?"

### 9.6 Industry

*Inference rule:* counterparty mix. *Fallback:* "In one sentence, what does the business do?"

### 9.7 Employees

*Inference rule:* CPP/EI/payroll outgoing. *Fallback:* "Do you have employees?"

### 9.8 Exempt supplies

*Inference rule:* financial/medical/educational/residential rental income patterns. *Fallback:* "Do you make any GST/HST-exempt supplies?"

### 9.9 Interprovincial sales

*Inference rule:* counterparties in multiple provinces. *Fallback:* "Do you sell to customers in provinces other than your own?"

### 9.10 Prior period balance

*Not inferable. Always ask.* "Do you have any GST/HST balance owing or credit from the previous period?"

## Section 10 — Reference material

### Validation status

Version 2.0 was rewritten in April 2026 to align with the three-tier OpenAccountants architecture. Canada-specific content (rates, line mappings, ITC rules, place of supply) is based on the Excise Tax Act as of April 2026 including the Nova Scotia HST rate change to 14% effective April 1, 2025.

### Sources

**Primary legislation:**
1. Excise Tax Act (R.S.C., 1985, c. E-15), Part IX — s.123 (definitions), s.148 (small supplier), s.165 (imposition), s.169 (ITCs), s.170 (restrictions), s.218 (self-assessment), Schedule V (exempt), Schedule VI (zero-rated)
2. Input Tax Credit Information (GST/HST) Regulations — documentation thresholds
3. Place of Supply (GST/HST) Regulations (SOR/2010-117)
4. New Harmonized Value-added Tax System Regulations

**CRA guidance:**
5. GST34 form and guide (RC4022) — canada.ca
6. Quick Method guide (RC4058)
7. GST/HST Memoranda Series — various technical interpretations
8. GST/HST Info Sheets — place of supply, ITCs, specific industries

**Other:**
9. Bank of Canada daily exchange rates — bankofcanada.ca
10. CRA My Business Account — business registration verification

### Known gaps

1. Quebec QST is entirely refused — a separate skill is needed.
2. BC PST, SK PST, MB RST are refused — separate provincial skills needed.
3. Quick Method remains outside this guide.
4. First Nations exemptions are refused — specialized knowledge required.
5. Real property self-supply rules (s.191) are refused — too fact-sensitive.
6. The NS HST rate changed to 14% on April 1, 2025 — verify no further rate changes.
7. Interprovincial place-of-supply for digital services is evolving — flag for reviewer if significant.
8. Confirm actual billing, supplier registration and the commercial-use allocation before applying the imported-supply or ITC rules.

### Change log

- **v2.1 (November 2026):** Correct selected GST/HST registration timing, return lines and the export consulting example against CRA guidance and the Excise Tax Act.
- **v2.0 (April 2026):** Full rewrite to align with three-tier OpenAccountants architecture. 10-section Malta v2.0 structure adopted. Supplier pattern library added (Section 3). Six worked examples added (Section 4). Tier 1 rules compressed (Section 5). Tier 2 catalogue added (Section 6). Excel template added (Section 7). Bank statement guide with RBC/TD/BMO/CIBC formats added (Section 8). Onboarding moved to fallback (Section 9).
- **v2.0 (prior, April 2026):** Previous version with inline tier tags. Superseded.

### Self-check (v2.0)

1. Quick reference at top with rate table and conservative defaults: yes (Section 1).
2. Supplier library as literal lookup tables: yes (Section 3, 15 sub-tables).
3. Worked examples (hypothetical ON IT consultant): yes (Section 4, 6 examples).
4. Tier 1 rules compressed: yes (Section 5, 14 rules).
5. Tier 2 catalogue compressed: yes (Section 6, 15 items).
6. Excel template with mandatory recalc: yes (Section 7).
7. Onboarding as fallback only: yes (Section 9, 10 items).
8. All 8 Canada-specific refusals present: yes (Section 2, R-CA-1 through R-CA-8).
9. Reference material at bottom: yes (Section 10).
10. Confirm the imported taxable supply definition, applicable self-assessed tax and any eligible ITC in sections 3.8 and 5.7 and example 1.
11. Meals 50% rule explicit: yes (Section 5.10 + Example 3).
12. Vehicle logbook requirement explicit: yes (Example 6).
13. Place of supply rules documented: yes (Section 5.3).
14. HST rate table complete with NS 14%: yes (Section 1).
15. Zero-rated vs exempt distinction explicit: yes (Section 5.4–5.5).

## End of Canada GST/HST Return Skill v2.1

This skill is incomplete without the companion workflow file loaded alongside it: `vat-workflow-base` v0.1 or later (Tier 1, workflow architecture). Do not attempt to produce a GST34 without it loaded.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
