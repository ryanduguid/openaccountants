---
name: ca-fed-t1135
description: >
  Use this skill whenever asked about Canada Form T1135, Foreign Income Verification
  Statement, specified foreign property, foreign asset reporting, the $100,000 cost amount
  threshold, the $250,000 simplified-versus-detailed reporting boundary, or how to classify
  foreign accounts, foreign securities, foreign real estate, foreign trusts, and other
  foreign property for a Canadian resident taxpayer. Trigger on phrases like "T1135",
  "foreign income verification statement", "specified foreign property", "foreign assets over
  100000", "do I need to file T1135", "foreign bank account reporting Canada", "US brokerage
  T1135", "foreign rental property T1135", "simplified T1135", "Part A Part B T1135", or any
  question about whether a Canadian resident individual, corporation, trust, or partnership
  must disclose foreign property. ALWAYS read this skill before touching any Canada
  T1135-related work.
version: 2.2
jurisdiction: CA-FED
tax_year: 2025
category: international
---

# Canada T1135 Foreign Income Verification Statement Skill v2.2

---

## Section 1 -- Quick reference

Read this whole section before classifying anything.

| Field | Value |
|---|---|
| Country | Canada -- Federal |
| Jurisdiction Code | CA-FED |
| Tax | Foreign reporting -- specified foreign property |
| Currency | CAD, unless a valid functional currency election applies |
| Tax year | Calendar year for individuals; taxation year / fiscal period as applicable for other filers |
| Primary legislation | Income Tax Act (Canada), section 233.3 |
| Tax authority | Canada Revenue Agency (CRA) |
| Form | T1135 -- Foreign Income Verification Statement |
| Filing deadline | Same due date as the related income tax return or partnership information return |
| Contributor | Open Accountants Community |
| Validated by | Pending -- Canadian CPA sign-off required |
| Validation date | Pending |
| Skill version | 2.2 |
| Confidence coverage | Tier 1: threshold testing, Part A / Part B decision, category mapping, common exclusions, form-field capture. Tier 2: mixed-use property, joint ownership, Category 7 aggregation, late filings. Tier 3: foreign affiliate issues, beneficial ownership chains, digital-asset situs. |

### Core thresholds (2025 form usage)

| Item | Rule |
|---|---|
| Basic filing threshold | File T1135 if total cost amount of specified foreign property exceeded $100,000 CAD at any time in the year |
| Threshold basis | Cost amount, NOT fair market value |
| Simplified boundary | If total cost exceeded $100,000 CAD but stayed below $250,000 CAD throughout the year, complete either Part A or Part B |
| Detailed boundary | If total cost reached $250,000 CAD or more at any time in the year, complete Part B |

### T1135 categories

| Category | Description |
|---|---|
| 1 | Funds held outside Canada |
| 2 | Shares of non-resident corporations (other than foreign affiliates) |
| 3 | Indebtedness owed by non-residents |
| 4 | Interests in non-resident trusts |
| 5 | Real property outside Canada (other than personal-use property and real estate used in an active business) |
| 6 | Other property outside Canada |
| 7 | Property held in an account with a Canadian registered securities dealer or a Canadian trust company |

### Common exclusions

| Item | Treatment |
|---|---|
| Personal-use property | Excluded |
| Property used or held exclusively in an active business | Excluded |
| Property inside registered plans (RRSP, RRIF, TFSA, RESP, DPSP) | Excluded |
| First year of Canadian tax residence for an individual | Generally excluded from T1135 filing obligation for that first resident year |

### Conservative defaults

| Ambiguity | Default |
|---|---|
| Unknown residency status | STOP -- residency required |
| Unknown cost basis | STOP -- do not use market value as final threshold test |
| Unknown first-year resident status | Ask one targeted question |
| Unknown account type | Do NOT assume registered-plan exclusion |
| Unknown property use | Do NOT assume personal-use or active-business exclusion |
| Unknown country code | Use provisional country and flag reviewer confirmation |
| Unknown ownership chain | Flag reviewer escalation |
| Unknown functional currency election | Assume CAD unless clearly documented otherwise |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

Before reaching any conclusion, gather:

1. Taxpayer type -- individual, corporation, trust, or partnership
2. Canadian tax residency status for the year
3. First-year resident status if the filer is an individual
4. Taxation year / fiscal period from and to dates
5. Whether the filing is amended
6. Whether a functional currency election applies
7. Complete list of all foreign assets or accounts held at any time in the year
8. Cost amount in CAD for each reportable or potentially reportable property
9. Maximum cost amount during the year where available
10. Cost amount at year-end or fair market value at year-end where the form requires it
11. Gross income / income received and gain (loss) on disposition
12. Country code and institution / issuer / counterparty / property description
13. Whether any property was inside a registered plan
14. Whether any property was personal-use property or used exclusively in an active business
15. Whether any property was jointly owned, held through a nominee, trust, partnership, or Canadian registered securities dealer / Canadian trust company

If cost amount is unavailable, STOP. Do not convert a market-value-only answer into a final filing conclusion.

### Refusal catalogue

**R-CA-T1135-1 -- Non-resident taxpayer.** Trigger: taxpayer was not resident in Canada for the relevant year. Message: "T1135 is a Canadian-resident foreign reporting regime. Non-resident treatment is outside this skill. Escalate to a Canadian cross-border tax practitioner."

**R-CA-T1135-2 -- Residency timing unclear.** Trigger: immigration / emigration timing is unclear. Message: "Residency timing changes the T1135 analysis. Do not guess. Escalate to a licensed Canadian CPA."

**R-CA-T1135-3 -- Beneficial ownership / nominee / trust chain unclear.** Trigger: legal ownership and reporting attribution are uncertain. Message: "Legal ownership and reporting attribution are unclear. Do not guess. Escalate to a Canadian CPA with international reporting experience."

**R-CA-T1135-4 -- Cost basis unavailable.** Trigger: only market value is available. Message: "T1135 threshold testing uses cost amount, not market value. A final conclusion cannot be made without cost basis support."

**R-CA-T1135-5 -- Digital asset situs uncertain.** Trigger: crypto, offshore wallet, exchange, or token arrangement with unclear situs or characterization. Message: "Digital asset reporting classification is fact-specific and outside routine scope. Escalate before concluding."

**R-CA-T1135-6 -- Foreign affiliate issue.** Trigger: possible foreign affiliate identified. Message: "Possible foreign affiliate reporting issue identified. Do not handle within routine T1135 workflow. Escalate."

---

## Section 3 -- Foreign property pattern library

This is the deterministic pre-classifier for T1135 assets. Each asset gets exactly one of three outcomes: **REPORTABLE**, **EXCLUDED**, or **REVIEWER FLAG**.

### 3.1 Commonly reportable property

| Pattern | Treatment | Category |
|---|---|---|
| Foreign bank account | REPORTABLE | 1 |
| Shares of non-resident corporations held directly | REPORTABLE | 2 |
| Shares of non-resident corporations held with foreign broker | REPORTABLE | 2 |
| Foreign bonds, notes, loans receivable, indebtedness | REPORTABLE | 3 |
| Interests in non-resident trusts / foreign mutual fund trusts | REPORTABLE | 4 |
| Foreign rental / investment real estate | REPORTABLE | 5 |
| Other foreign investment property | REPORTABLE | 6 |
| Property held in an account with a Canadian registered securities dealer or a Canadian trust company | REPORTABLE | 7 |

### 3.2 Commonly excluded property

| Pattern | Treatment | Reason |
|---|---|---|
| Foreign property inside RRSP / RRIF / TFSA / RESP / DPSP | EXCLUDED | Registered-plan exclusion |
| Foreign vacation property used as personal-use property | EXCLUDED | Personal-use property exclusion |
| Property used or held exclusively in an active business | EXCLUDED | Active-business exclusion |
| Canadian mutual fund trust / Canadian mutual fund corporation | EXCLUDED | Investor holds Canadian property, not underlying foreign property |

### 3.3 Always flag for reviewer

| Pattern | Treatment | Reason |
|---|---|---|
| Mixed-use foreign real estate | REVIEWER FLAG | Personal-use exclusion depends on facts |
| Joint ownership with unclear contributions | REVIEWER FLAG | Threshold depends on beneficial ownership share |
| Bare trust / nominee / beneficial ownership mismatch | REVIEWER FLAG | Attribution issue |
| Partnership interest with foreign property underneath | REVIEWER FLAG | Partner-level vs entity-level analysis |
| Possible foreign affiliate | REVIEWER FLAG | Foreign affiliate rules may displace routine T1135 handling |
| Crypto / offshore wallet / exchange arrangement | REVIEWER FLAG | Situs / property characterization issue |
| Pre-construction foreign real estate deposits | REVIEWER FLAG | Determine whether reportable property exists yet |

---

## Section 4 -- Threshold and filing path rules

### 4.1 Residency screen

| Condition | Result |
|---|---|
| Non-resident for the relevant year | STOP -- fire R-CA-T1135-1 |
| Individual in first year of Canadian tax residence | Generally no T1135 filing obligation for that first resident year |
| Canadian-resident individual, corporation, trust, or partnership | Continue to threshold test |

### 4.2 Threshold test (Tier 1)

Aggregate the **cost amount** of all reportable specified foreign property held at any time in the year.

| Condition | Result |
|---|---|
| Total never exceeded $100,000 CAD | T1135 generally not required |
| Total exceeded $100,000 CAD at any time | T1135 generally required |
| Cost amount missing | STOP -- fire R-CA-T1135-4 |

Do NOT ignore property sold before year-end. If the threshold was met during the year, those assets still matter.

### 4.3 Part A vs Part B

| Condition | Filing path |
|---|---|
| Total cost exceeded $100,000 CAD but stayed below $250,000 CAD throughout the year | Part A or Part B |
| Total cost reached $250,000 CAD or more at any time | Part B |

### 4.4 Part A -- Simplified reporting method

Part A requires:
- type-of-property boxes
- top three country codes based on maximum cost amount during the year
- gross income from all specified foreign property
- gain (loss) from disposition of all specified foreign property

Even if Part A is used, still build the underlying asset inventory for reviewer support.

### 4.5 Part B -- Detailed reporting method

Part B requires category-by-category detail for each specified foreign property held at any time in the year, unless valid Category 7 aggregation is used.

Always gather:
- country code
- institution / issuer / trust / property description
- maximum cost amount during the year or other category-specific maximum field
- cost amount at year-end where the form calls for it
- gross income or income received
- gain (loss) on disposition

---

## Section 5 -- Category classification rules

### 5.1 Category 1 -- Funds held outside Canada

Capture:
- country code
- name of bank / other entity holding the funds
- maximum funds held during the year
- funds held at year-end
- income received

### 5.2 Category 2 -- Shares of non-resident corporations

Capture:
- country code
- name of corporation
- maximum cost amount during the year
- cost amount at year-end
- gross income
- gain (loss) on disposition

### 5.3 Category 3 -- Indebtedness owed by non-residents

Capture:
- country code
- description of indebtedness
- maximum cost amount during the year
- cost amount at year-end
- gross income
- gain (loss) on disposition

### 5.4 Category 4 -- Interests in non-resident trusts

Capture:
- name of trust
- country code
- maximum cost amount during the year
- income received
- capital received
- gain (loss) on disposition

### 5.5 Category 5 -- Real property outside Canada

Capture:
- description of property
- country code
- maximum cost amount during the year
- cost amount at year-end
- gross income
- gain (loss) on disposition

### 5.6 Category 6 -- Other property outside Canada

Capture:
- description of property
- country code
- maximum cost amount during the year
- cost amount at year-end
- gross income
- gain (loss) on disposition

### 5.7 Category 7 -- Property held with Canadian registered securities dealer or Canadian trust company

Capture:
- dealer / trust company name
- country code
- maximum fair market value during the year
- fair market value at year-end
- gross income
- gain (loss) on disposition

Category 7 is a special aggregation rule. Do not force Categories 2 to 6 line-by-line reporting if valid Category 7 aggregation is available and chosen.

### 5.8 Country code rules

- Capture country code in form-ready format wherever the form requires it.
- For Part A, identify the top three countries based on maximum cost amount during the year.
- For shares of non-resident corporations, generally use the country of residence of the corporation.
- For interests in non-resident trusts, generally use the country of residence of the trust.
- If country coding is uncertain, flag reviewer confirmation.

### 5.9 Income and gain rules

- Use **gross income** where the form calls for gross income.
- Use **gain (loss)** as the form label, not taxable capital gain / allowable capital loss.
- Do NOT net unrelated gains and losses across assets unless the form presentation explicitly aggregates them.

---

## Section 6 -- Exclusions and special cases

### 6.1 Registered plans

Foreign property inside RRSP, RRIF, TFSA, RESP, and DPSP is excluded from T1135. Do not include those assets in the threshold calculation.

### 6.2 Personal-use property

Personal-use property is excluded. Do NOT assume foreign real estate qualifies if it also has rental or investment use.

### 6.3 Active-business property

Property used or held exclusively in an active business is excluded. Do NOT assume a day trader or active investor automatically qualifies.

### 6.4 Joint ownership

If foreign property is jointly owned, determine beneficial ownership and contribution proportions before reaching the threshold conclusion. Do not assume 50/50 without support.

### 6.5 Mixed-use foreign real estate

Vacation use plus rental activity is fact-sensitive. Ask for personal-use days, rental days, and business purpose. Flag for reviewer.

### 6.6 Late or missed filings

If prior-year T1135 filings were missed:
- flag possible penalties and extended reassessment exposure
- build the asset inventory year by year
- discuss voluntary disclosure only as a reviewer issue
- do NOT promise relief

---

## Section 7 -- Reviewer escalation protocol

Escalate before finalizing if any of the following are present:

1. immigration / emigration timing issues
2. beneficial ownership or nominee issues
3. possible foreign affiliate exposure
4. partnership or trust attribution uncertainty
5. digital-asset situs or characterization issues
6. mixed-use foreign real estate with weak factual support
7. pre-construction foreign property deposits with unclear property rights
8. unclear functional currency election or prior-year amended filing issues

When escalating, provide:
- taxpayer type
- residency facts
- threshold computation to date
- asset inventory
- missing facts
- proposed category mapping
- reason for escalation

---

## Section 8 -- Form assembly protocol

Use this section only after classification is complete.

### 8.1 Header fields

Capture exactly:
- amended return status
- functional currency code, if any
- filer type
- identification number
- reporting entity name
- address
- taxation year from date
- taxation year to date

### 8.2 Part A output block

Capture exactly:
- applicable type-of-property boxes
- top three country codes
- gross income from all specified foreign property
- gain (loss) from disposition of all specified foreign property

### 8.3 Part B output block

For each category used, capture the exact form fields listed in Section 5.

### 8.4 Working paper template

```text
CANADA T1135 -- WORKING PAPER (2025)

A. HEADER
  A1. Amended return?                                        YES / NO
  A2. Functional currency election?                          YES / NO
  A3. Functional currency code                               ___________
  A4. Filer type                                             ___________
  A5. Identification number                                  ___________
  A6. Taxation year from                                     ___________
  A7. Taxation year to                                       ___________

B. THRESHOLD SUMMARY
  B1. Aggregate cost amount of reportable specified foreign property   ___________
  B2. Exceeded $100,000 CAD at any time?                              YES / NO
  B3. Reached $250,000 CAD at any time?                               YES / NO
  B4. Filing path                                                     NONE / PART A / PART B

C. ASSET INVENTORY
| # | Asset description | Category | Country code | Max cost / FMV | Year-end cost / FMV | Income / capital received | Gain (loss) | Outcome | Notes |
|---|---|---|---|---:|---:|---:|---:|---|---|
| 1 | | | | | | | | REPORTABLE / EXCLUDED / REVIEWER FLAG | |

D. EXCLUSIONS APPLIED
| Asset | Exclusion reason | Support |
|---|---|---|

E. REVIEWER FLAGS
| Issue | Reason | Action |
|---|---|---|
```

### 8.5 Certification and preparer fields

Do not finalize the form package without:
- certification statement
- signer name
- position or title where applicable
- signature block
- date
- paid preparer name, address, postal code, and telephone if applicable

---

## Section 9 -- Test suite

Use these as minimum validation scenarios.

### Test 1 -- Below threshold

Input: Canadian-resident individual with foreign bank account cost amount $42,000 and U.S. shares cost amount $31,000. No other specified foreign property.

Expected result:
- Aggregate cost amount = $73,000
- T1135 not required

### Test 2 -- Over threshold, below detailed boundary

Input: Canadian-resident individual with foreign bank account cost amount $18,000 and U.S. shares cost amount $108,000, later sold before year-end.

Expected result:
- Threshold exceeded during year
- T1135 required
- Part A or Part B available if total stayed below $250,000 throughout the year

### Test 3 -- Detailed reporting required

Input: Canadian-resident corporation with foreign securities cost amount $310,000 at peak during the year.

Expected result:
- T1135 required
- Part B required

### Test 4 -- Registered-plan exclusion

Input: RRSP with U.S. ETF cost amount $150,000 and TFSA with foreign stock cost amount $35,000; no non-registered foreign property.

Expected result:
- Excluded property only
- T1135 not required

### Test 5 -- Mixed-use condo

Input: Foreign condo used personally for 6 weeks and rented for the rest of the year.

Expected result:
- Do not auto-exclude
- Reviewer flag required

### Test 6 -- Category 7

Input: Foreign securities held in an account with a Canadian registered securities dealer.

Expected result:
- T1135 may be reportable through Category 7 aggregation if the facts support that method

---

## Section 10 -- Prohibitions and disclaimer

### Prohibitions

- NEVER use fair market value as the threshold test when cost amount is required.
- NEVER assume a Canadian broker removes T1135 exposure.
- NEVER assume no filing because the year-end balance fell below $100,000 CAD.
- NEVER ignore sold-before-year-end assets if the threshold was met during the year.
- NEVER assume personal-use or active-business exclusion without facts.
- NEVER ignore the first-year resident exception.
- NEVER skip amended-return, functional-currency, certification, or paid-preparer fields when assembling the form.
- NEVER present a speculative answer as definitive.

### Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon them. The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).
