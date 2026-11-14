---
name: cayman-tax
description: Use this skill whenever asked about Cayman Islands taxation or the absence of direct taxes. Trigger on phrases like "Cayman tax", "Cayman Islands VAT", "Cayman Islands income tax", "Cayman corporate tax", or any request involving Cayman Islands tax compliance. The Cayman Islands does NOT have income tax, capital gains tax, VAT, payroll tax, or any direct taxes. Revenue is raised through import duties, work permit fees, and financial services fees. ALWAYS read this skill before handling any Cayman Islands tax work.
version: 3.0
jurisdiction: KY
tax_year: 2026
last_updated: 2026-11-14
review_status: pending_review
category: international
tier: 2
depends_on:
  - workflow-base
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Cayman Tax

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Territory | Grand Cayman, Cayman Brac and Little Cayman. [2026 tax-system scope](ky-tax-overview.md#tax-system-scope-in-2026) |
| Tax | Import duties (primary), work permit fees, financial services fees, stamp duty, landholding share transfer tax, tourism tax |
| Currency | Cayman dollar (KYD or CI$). Check the conversion rule for the payment. [Monetary Authority Act, ss 22–25](https://www.cima.ky/upimages/lawsregulations/MonetaryAuthorityLaw2020Revision_1579789069_1599483258.pdf) |
| Assessment period | No general domestic income tax assessment period. Check the period for the particular duty, licence or reporting obligation. [2026 tax-system scope](ky-tax-overview.md#tax-system-scope-in-2026) |
| Primary legislation | Tax Concessions Act (Revised); Customs Tariff Act (Revised) |
| Supporting legislation | Companies Act (2026 Revision), Economic Substance Act (2026 Revision) |
| Responsible authorities | Use the authority for the duty, fee or reporting regime. [2026 tax-system scope](ky-tax-overview.md#tax-system-scope-in-2026) |
| Property filings | Lands and Survey Department for land transfer stamp duty. The landholding corporation files its equity transfer return with the Minister responsible for Finance. See Section 5.2. |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires sign-off by a licensed Cayman practitioner |
| Skill version | 3.0 |

### Tax Landscape

**Tax Landscape**

| Tax Type | Status |
| --- | --- |
| Income Tax (personal/corporate) | None |
| Capital Gains Tax | None |
| VAT / Sales Tax | None |
| Payroll Tax | None |
| Withholding Tax | None |
| Property Tax (annual) | None |
| Estate / Inheritance Tax | None |
| Import Duties | Yes -- primary revenue source |
| Work Permit Fees | Yes |
| Financial Services Fees | Yes |
| Stamp Duty | Yes, including transfers, leases and mortgages of Cayman land |
| Landholding Share Transfer Tax | Yes, on taxable transfers of equity in landholding corporations |
| Tourist accommodation | Generally 13% on covered stays. Qualifying timeshare stays have a separate charge. [2026 guide](ky-vat-gst.md#tourist-accommodation-and-timeshares) |

- **Tax Undertaking Certificate duration** — Up to 30 years from approval for an exempted company (Tax Concessions Act s 6(5)); up to 50 years for an exempted limited partnership (ELP Act s 38(3)), a limited liability company (LLC Act s 58(3)) or an exempted trust (Trusts Act s 81(2)). Undertakings are given to entities, not to individuals  _(Tax Concessions Act (2018 Revision), s 6(5) — https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/1964/1964-0164/1964-0164_2018%20Revision.pdf ; Exempted Limited Partnership Act (2025 Revision), s 38(3) — https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/2001/2001-0005/2001-0005_2025%20Revision.pdf ; Limited Liability Companies Act (2025 Revision), s 58(3) — https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/2016/2016-0002/2016-0002_2025%20Revision.pdf ; Trusts Act (2021 Revision), s 81(2) — https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/1967/1967-0006/1967-0006_2021%20Revision.pdf)_

### Import duty

Use the [2026 customs guide](ky-vat-gst.md#customs-duty) to classify each
product, value the entry and identify any exemptions and separate charges.

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown duty rate | Get the tariff code, entry date and evidence of any relief before calculating |
| Unknown economic substance | Identify the entity and activity before applying the test |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

- **Minimum viable** — nature of inquiry (employment, imports, entity registration, property).
- **Recommended** — entity type, number of employees, import values, property details.
- **Ideal** — complete registration documents, prior customs filings, economic substance reports.

### Refusal Catalogue

- **R-KY-1 -- Income tax** — Cayman Islands has no income tax.
- **R-KY-2 -- VAT/sales tax** — Cayman Islands has no VAT or sales tax.
- **R-KY-3 -- ES work outside the selected Section 6.1 reference classifications and manual controls.** Trigger for a request to resolve the held partnership filing limb, unsupported historical application, other detailed ES branches, current portal procedures or a filing. Verbatim output: `R-KY-3: This ES request exceeds the selected verified classification scope. Obtain the applicable primary authority and a qualified Cayman specialist's review before proceeding.` Supported Section 6.1 reference classifications may proceed through the workflow; an unknown fact within that scope is Needs Input, with the affected conclusion held.
- **R-KY-4 -- CRS/FATCA reporting** — Escalate to specialist.
- **R-KY-ES-REVIEW -- No qualified reviewer.** Trigger when the requester will not obtain qualified review and asks to rely on the result as final. Verbatim output: `R-KY-ES-REVIEW: A qualified Cayman reviewer must check this work before reliance or filing. I cannot provide final assurance without that review.`

## Section 3 -- Compliance Pattern Library

### 3.1 Employer Obligations

**Employer Obligations**  _(National Pensions Act)_

| Obligation | Amount/Rate | Notes |
| --- | --- | --- |
| Pension (defined contribution) | Required total 10%; employer at least 5% | Subject to coverage, earnings cap and member-consent rules; see §5.3 |
| Health insurance | Employer must provide | Minimum coverage prescribed |
| Work permit fees | Varies by category | Non-Caymanian workers |
| Payroll tax | None |  |

### 3.2 Import Duty Categories

Use Schedule 1 for the code and rate and Schedule 6 for classification.
Check Schedule 2 relief and Schedules 3–5 for package tax, handling,
storage and other charges. [Customs Tariff Act (2026 Revision), ss 2–5](https://gov.ky/w/customs-tariff-act-2026-revision-lg5-s3)

### 3.3 Entity Registration Fees

The [formation and reporting guide](ky-company-formation.md) gives the current statutory fee bands, the changes from 1 January 2027 and the separate requirements for licences and regulated funds.

## Section 4 -- Worked Examples

### Example 1 -- Import Duty

Wooden office furniture under code 9403.30.00 enters for home use in 2026.
At a customs value of CI$10,000, import duty is CI$2,200 before any
other border charges or relief. [2026 customs guide](ky-vat-gst.md#customs-duty)

### Example 2 -- Employment Obligations

**Input:** Employee at KYD 60,000/year, non-Caymanian, age 30, employed continuously in Cayman for two years, not a household domestic. Assume a defined-contribution plan with a 5% employer share.

**Classification:** No Cayman wage income tax withholding. The employer and employee each contribute KYD 3,000 to the pension plan. The employer arranges health cover and, if a work permit is required, pays the applicable permit fees. See [payroll and social contributions](ky-payroll-social.md) for the 2026 rules.

### Example 3 -- Tourist accommodation

In 2026 a hotel charges a tourist CI$500 for a room. At 13%, the
accommodation tax is CI$65. For a qualifying owner-occupied timeshare,
1 occupied room across parts of 2 days instead attracts the equivalent
of US$20. [Tourist Accommodation Act, ss 2–3](https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/1964/1964-0168/1964-0168.pdf) · [2026 reporting and payment rules](ky-vat-gst.md#tourist-accommodation-and-timeshares)

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 No Direct Taxes

- **No direct taxes** — No income tax of any kind. No capital gains tax. No VAT/sales tax. No withholding tax. No payroll tax. No annual property tax. No estate tax. Tax undertakings are available for up to 30 years for exempted companies and 50 years for exempted limited partnerships, LLCs and exempted trusts. See Section 5.2 for duties on property transactions and probate instruments. [Government overview](https://cigarchives.gov.ky/economy) · [Tax Concessions Act (2018 Revision), s 6](https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/1964/1964-0164/1964-0164_2018%20Revision.pdf) · [Exempted Limited Partnership Act (2025 Revision), s 38](https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/2001/2001-0005/2001-0005_2025%20Revision.pdf)

### 5.2 Property and Transfer Duties

#### Land transfers from 1 January 2026

For an ordinary transfer of developed or undeveloped land, take the higher of the price in the instrument and the property's market value. Use the full value before deducting any mortgage or other encumbrance. Stamp duty is **7.5% of the full base below CI$2 million** and **10% of the full base at or above CI$2 million**. The earlier rates apply to a qualifying instrument executed before 1 January 2026. [Stamp Duty Act (2019 Revision), Schedule, conveyance paras 2–4](https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/1973/1973-0005/1973-0005.pdf) · [SL 63 of 2025, regs 1–3](https://legislation.gov.ky/cms/images/LEGISLATION/SUBORDINATE/2025/2025-0063/2025-0063_SL%2063%20of%202025.pdf) · [Government explanation, 2 January 2026](https://gov.ky/w/legislation-passed-to-increase-stamp-duty-on-properties-worth-2m-and-over)

For a 2026 price of CI$1.9 million, duty is CI$142,500 when market value is also CI$1.9 million and CI$200,000 when market value is CI$2 million.

```oa-check
name: KY ordinary land transfer below and at the 2026 threshold
inputs:
  price: 1900000
  lower_value: 1900000
  higher_value: 2000000
  lower_rate: 7.5
  higher_rate: 10
steps:
  - below_threshold: pct(max(price, lower_value), lower_rate)
  - at_threshold: pct(max(price, higher_value), higher_rate)
expected:
  below_threshold: 142500
  at_threshold: 200000
```

A purchase agreement that confers possession attracts ad valorem duty. Where the agreement expressly prevents possession, the purchaser can choose the CI$100 duty or ad valorem duty. Possession includes collecting rents. On a later conveyance that conforms to the agreement, including one with only minor discrepancies in the property description, deduct the ad valorem duty actually paid on the agreement from the duty otherwise due on the conveyance, down to nil. Present both instruments and the earlier payment evidence to Lands and Survey for endorsement. [Stamp Duty Act, ss 19 and 20(5) and Schedule, agreement paras 1–4](https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/1973/1973-0005/1973-0005.pdf) · [Lands and Survey transfer checklist](https://www.caymanlandinfo.ky/forms-and-guidelines)

For instruments executed on opposite sides of 1 January 2026, calculate each charge using the rate applicable to that instrument, then deduct the earlier payment if the credit conditions are met. For example, if a qualifying 2025 agreement was stamped at 7.5% on CI$2 million and the conforming 2026 conveyance is chargeable at 10% on the same base, the statutory calculation leaves CI$50,000 after credit. Confirm the assessment with Lands and Survey for the specific instruments. [SL 63 of 2025, regs 2–3](https://legislation.gov.ky/cms/images/LEGISLATION/SUBORDINATE/2025/2025-0063/2025-0063_SL%2063%20of%202025.pdf) · [Stamp Duty Act, s 19 and Schedule, agreement para 2](https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/1973/1973-0005/1973-0005.pdf)

```oa-check
name: KY conforming transfer across the 2026 stamp duty rate change
inputs:
  duty_base: 2000000
  agreement_rate: 7.5
  transfer_rate: 10
steps:
  - agreement_paid: pct(duty_base, agreement_rate)
  - transfer_duty: pct(duty_base, transfer_rate)
  - balance: max(0, transfer_duty - agreement_paid)
expected:
  agreement_paid: 150000
  transfer_duty: 200000
  balance: 50000
```

A statutory linked property transaction can combine a bare land purchase in a development scheme with construction. For transfers from 1 January 2026, the rate on the total linked value is 3% through CI$300,000, 7.5% above CI$300,000 and below CI$2 million and 10% from CI$2 million. Where the linked value exceeds CI$300,000 and the agreement for bare land and later conveyance are separately chargeable under paras 3 and 4, each instrument bears 3.75% of the linked value below CI$2 million or 5% from CI$2 million. For those 2 instruments, each 45-day period runs from the buyer's first signature on that instrument. [Stamp Duty Act, s 2 and Schedule, linked property transactions para 1](https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/1973/1973-0005/1973-0005.pdf) · [SL 63 of 2025, regs 1–3](https://legislation.gov.ky/cms/images/LEGISLATION/SUBORDINATE/2025/2025-0063/2025-0063_SL%2063%20of%202025.pdf)

#### Caymanian buyer concessions

For 2026 transactions, the concession limits apply to the total duty base in CI$. Joint limits require 2–10 Caymanian purchasers and the stated purchase number must apply to each buyer. Earlier purchases in the Islands count even if the buyer had yet to acquire Caymanian status. A first purchase as a Caymanian may qualify for the second-property concession if it is the buyer's second purchase overall. Above the applicable upper limit, ordinary rates apply to the full base. Check the evidence of eligibility and any conditions imposed by the Minister. [SL 3 of 2025, reg 2, conveyance paras 10–12](https://legislation.gov.ky/cms/images/LEGISLATION/SUBORDINATE/2025/2025-0003/2025-0003_SL%203%20of%202025.pdf) · [SL 63 of 2025, reg 2](https://legislation.gov.ky/cms/images/LEGISLATION/SUBORDINATE/2025/2025-0063/2025-0063_SL%2063%20of%202025.pdf) · [Stamp Duty Act, Schedule, conveyance para 13](https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/1973/1973-0005/1973-0005.pdf)

| Qualifying purchase | Land with a building | Bare land |
| --- | --- | --- |
| First, sole | Nil through CI$550,000. Above that and through CI$650,000, 3.75% on the excess over CI$550,000. | Nil through CI$250,000. Above that and through CI$350,000, 3.75% on the excess over CI$250,000. |
| First, joint | Nil through CI$600,000. Above that and through CI$700,000, 3.75% on the excess over CI$600,000. | Nil through CI$450,000. Above that and through CI$550,000, 3.75% on the excess over CI$450,000. |
| Second, sole | 3.75% on the full base through CI$600,000. | 3.75% on the full base through CI$300,000. |
| Second, joint | 3.75% on the full base through CI$700,000. | 3.75% on the full base through CI$550,000. |

At a CI$600,000 duty base for developed land in 2026, a sole Caymanian buyer pays CI$1,875 on a qualifying first purchase or CI$22,500 on a qualifying second purchase.

```oa-check
name: KY sole Caymanian buyer first and second developed land concessions
inputs:
  base: 600000
  first_nil_limit: 550000
  concession_rate: 3.75
steps:
  - first_purchase: pct(base - first_nil_limit, concession_rate)
  - second_purchase: pct(base, concession_rate)
expected:
  first_purchase: 1875
  second_purchase: 22500
```

For first or second purchases, send a separate application and sworn affidavit for each buyer to the Ministry of Finance and Economic Development. The April 2026 form asks for certified evidence of Caymanian status where applicable, a certified or notarised offer or purchase agreement and valuation evidence. It also asks about ownership through landholding companies. Approved concessions carry a 5-year title restriction from registration. A transfer during that period needs the Minister's permission and attracts a prorated amount of the ordinary duty that would have applied when the concession was granted. [Ministry application and document checklist, 16 April 2026](https://www.caymanlandinfo.ky/docs/default-source/laws-and-regulations/stamp-duty/application-concession-form-for-caymanian-property-buyers.pdf?sfvrsn=a01a6f6d_1)

Cabinet extended Cayman Brac concessions through 31 December 2030. Qualifying developed property below CI$2 million has a 3% rate. For the full waiver on qualifying undeveloped land below CI$2 million, submit the Ministry's Cayman Brac application with the certified transfer, development dates and a notarised declaration of intent. Present the approval letter and certificate to the Registrar at registration. A title restriction prevents transfer before the conditions are met, and the building requires planning approval and a Certificate of Occupancy. The Cabinet announcement measures the 2-year development period from the waiver grant, whilst the application refers to purchase. Confirm the date in the approval. The Minister may grant up to 2 more years. Missing the applicable deadline makes the waived duty payable with a 10% penalty. Confirm which concession applies if more than one could cover the transaction. [Cabinet announcement, 14 January 2026](https://gov.ky/w/cayman-brac-duty-concessions-extended) · [Ministry Cayman Brac application and procedure](https://www.caymanlandinfo.ky/docs/default-source/laws-and-regulations/stamp-duty/cayman-brac-stamp-duty-concessions.pdf?sfvrsn=ea25d4ad_1)

#### Land transfer filing and other instruments

- **File or seek adjudication.** For a transfer under the Registered Land Rules, the transferee must have the completed instrument stamped or present it for adjudication within 45 days of the transferor's signature. For other conveyances of land or strata title, the 45 days run from the disposition or first disposition. A chargeable assignment of purchase rights has a separate 45-day period from the assignor's signature. An agreement on which the purchaser elected ad valorem duty uses the first day an obligation was discharged. Other ad valorem instruments have a general 45-day rule, with specific triggers for signing abroad or escrow. [Stamp Duty Act, s 20](https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/1973/1973-0005/1973-0005.pdf)
- **Submit the instruments.** Use the RL1 checklist and lodge the transfer and supporting agreement or declaration, relief approval and corporate permissions where applicable with Lands and Survey. Include an itemised inventory at current market values for any removable chattels claimed. Fixtures form part of the immovable property. Section 33 requires a printed copy for stamping where the instrument is electronic. Retain the lodgement and payment evidence. [Lands and Survey forms and guidelines](https://www.caymanlandinfo.ky/forms-and-guidelines) · [Valuation and Estates chattels policy](https://www.caymanlandinfo.ky/docs/default-source/forms/document-preparation/20220801-cig-policy-on-sd-on-chattels.pdf?sfvrsn=802da7e7_1) · [Stamp Duty Act, ss 4–6, 16 and 33](https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/1973/1973-0005/1973-0005.pdf)
- **Review a valuation.** If the Valuation and Estates Office assesses market value above the consideration, it issues an assessment. Submit evidence, such as the date the price was agreed, property damage or related purchases, in the review window on the assessment. If the dispute remains, present the instrument for adjudication by the Commissioner of Stamp Duty, who is the Minister of Finance. The statutory fee is 1% of the sum adjudicated, with a CI$1 minimum and CI$1,000 maximum. The Act gives the Commissioner 15 days after presentation to adjudicate, subject to payment of the fee. [Lands and Survey transfer guidance](https://www.caymanlandinfo.ky/services/valuation/stamp-duty/mortgages/transfer-sale-of-land) · [Lands and Survey purchase agreement guidance](https://www.caymanlandinfo.ky/services/valuation/stamp-duty/mortgages/contracts-for-sale---purchase-agreements) · [Stamp Duty Act, ss 4 and 8–9 and Schedule, adjudication](https://judicial.ky/wp-content/uploads/stamp-duty-act-2019-revision.pdf)
- **Pay and, if needed, appeal.** Stamp an unstamped or partly stamped instrument within 7 days after adjudication and cover the adjudication fee. After paying the adjudicated duty, file a notice of motion in the Grand Court within 30 days of the adjudication and serve a copy on the Commissioner. The appeal rules call for grounds, a supporting affidavit and relevant documents with certified copies. The court can uphold, reduce, eliminate or increase the duty. Late stamping can attract interest at 10% per annum for the first month or part of it and 20% per annum thereafter on the unpaid balance. The Commissioner can waive interest for good cause. [Stamp Duty Act, ss 10–13 and 21–22](https://judicial.ky/wp-content/uploads/stamp-duty-act-2019-revision.pdf) · [Stamp Duty (Appeal) Rules, rr 3–6](https://legislation.gov.ky/cms/images/LEGISLATION/SUBORDINATE/1976/1976-0020/1976-0020_SL%2020%20of%201976.pdf)
- **Leases and mortgages.** A lease longer than 30 years uses conveyance duty on the full value of the property or interest. For a term of 30 years or less, charge conveyance duty on any premium and apply the rent rate to average annual rent. Where the instrument specifies a rent away from market value, use market rent having regard to the premium. The rent rate is 5% through 5 years, 10% above 5 through 10 years and 20% above 10 through 30 years. For a lease under one year, use 5% of aggregate rent. Count extension options and check later rent adjustments. The ordinary mortgage duty on Cayman immovable property is 1% of the secured sum through CI$300,000 and 1.5% above it. Further advances and qualifying instruments can have separate treatment. [Stamp Duty Act, Schedule, lease and mortgage](https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/1973/1973-0005/1973-0005.pdf)
- **Gifts and succession.** There is no general gift or inheritance tax. Qualifying transfers for natural love and affection attract CI$50 in stamp duty, subject to the statutory relationship and certification rules. A personal representative's assent vesting land carries nil stamp duty. A grant of probate or letters of administration carries CI$10 in instrument duty. The Land Registry has separate registration requirements and fees. [Government overview](https://cigarchives.gov.ky/economy) · [Stamp Duty Act, Schedule, conveyance para 9, assent and probate](https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/1973/1973-0005/1973-0005.pdf) · [Lands and Survey forms and guidelines](https://www.caymanlandinfo.ky/forms-and-guidelines)

#### Equity transfers in landholding corporations from 1 January 2026

Check the share transfer tax when a corporation holds Cayman land directly or through equity in another landholding corporation. An interest under a lease originally longer than 30 years can qualify. The statutory definitions reach qualifying partnerships and equity dealings that change beneficial ownership, ownership proportions or entitlements to profits or capital. Apply the nominal proportion of equity transferred to the total market value of the corporation's landed property at the transfer date to determine the statutory taxable value. The ordinary tax is **7.5% of the higher of the price and taxable value below CI$2 million**, or **10% of that full amount if either value reaches CI$2 million**. [Land Holding Companies Share Transfer Tax Act (2022 Revision), ss 2 and 3](https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/1976/1976-0020/1976-0020_2022%20Revision.pdf) · [Act 16 of 2025, ss 1–3](https://gov.ky/w/land-holding-companies-share-transfer-tax-amendment-act-2025-lg54-s3) · [Government explanation, 2 January 2026](https://gov.ky/w/legislation-passed-to-increase-stamp-duty-on-properties-worth-2m-and-over)

The corporation delivers the transfer instrument if there is one, the prescribed return and the payment to the Minister responsible for Finance within 31 days of transfer. The return records the parties and date, the nominal equity issued and transferred, the parcel identifiers and market value at transfer and the signer's capacity and declaration. Use the Schedule form as amended from 1 January 2026. Line 8 applies 7.5% or 10% to taxable value in its wording, whilst the Act charges the higher of consideration and taxable value. Retain both values and the statutory calculation. Confirm the Ministry's filing and payment channel and how it wants line 8 completed when the consideration is higher. For a transfer completed before 1 January 2026, the earlier calculation applies under the express transition if the transfer was still unsubmitted and the 31 days had yet to expire at commencement. [Principal Act, s 3](https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/1976/1976-0020/1976-0020_2022%20Revision.pdf) · [Act 16 of 2025, ss 2–3](https://gov.ky/w/land-holding-companies-share-transfer-tax-amendment-act-2025-lg54-s3) · [1997 Regulations, reg 2 and Schedule](https://legislation.gov.ky/cms/images/LEGISLATION/SUBORDINATE/1997/1997-0016/1997-0016_1997%20Revision.pdf) · [SL 57 of 2025, regs 1–2](https://gov.ky/documents/43485/45951/LandHoldingCompaniesShareTransferTax%28Amendment%29Regulations%2C2025_MADE.pdf/130ce07d-f910-c6e9-0f84-29dac826841c?t=1766076380599)

For a 2026 transfer of 25% by nominal value of the issued equity in a corporation with Cayman landed property worth CI$7.6 million, taxable value is CI$1.9 million. If the price is CI$2 million, the statutory tax is CI$200,000 before any relief.

```oa-check
name: KY landholding share transfer where only consideration reaches the 2026 threshold
inputs:
  landed_property_value: 7600000
  nominal_equity_percentage: 25
  consideration: 2000000
  higher_rate: 10
steps:
  - taxable_value: pct(landed_property_value, nominal_equity_percentage)
  - tax: pct(max(consideration, taxable_value), higher_rate)
expected:
  taxable_value: 1900000
  tax: 200000
```

Check the statutory exclusions for distributions by personal representatives, bankruptcy estates, certain transfers with unchanged beneficial ownership, qualifying family gifts, court orders and approved landholding corporations. An approved corporation files a compliance declaration signed by 2 directors with the Minister on the anniversary of the original grant, with a CI$5,000 annual fee. Separate discretionary relief under s 3(4) can apply where the specified owners hold at least 45% and transfer land to or from the corporation. Late payment accrues interest at 10% per annum for the first month or part of it and 20% per annum thereafter on the unpaid balance. Section 9 applies the stamp duty adjudication and appeal route to market valuation disputes. [Principal Act, ss 3(4), 4–5 and 7–9 and Schedule](https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/1976/1976-0020/1976-0020_2022%20Revision.pdf)

### 5.3 Pension and Health Insurance

- The [2026 Cayman payroll guide](ky-payroll-social.md) covers enrolment, wages, permitted deductions, provider payments, work permit fees and reconciliation. Private pension contributions are generally based on earnings up to CI$87,000. Standard employee health premiums are paid to the insurer by the employer, with up to 50% recoverable from the employee. High-risk and dependant premiums have separate rules. [National Pensions Act, ss 3, 25 and 47–48](https://www.procure.gov.ky/upimages/commonfiles/1751266504NationalPensionsAct2024Revision_1751266507.pdf) · [Health Insurance Act, ss 5 and 7–8](https://hsa-cayman.imgix.net/images/HealthInsuranceAct_2021-Revision.pdf)

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Economic Substance

Establish the entity's legal form, exclusions, each relevant activity and its
gross relevant income for the financial year before choosing the economic
substance (ES) test. The selected holding-company cases below use the
Economic Substance Act (2026 Revision), revised as at 31 December 2025, and
DITC Guidance v3.2 (July 2022), including its partnership appendix, checked
against the official resources listing on 14 November 2026. Confirm the law
and guidance applicable to a different period. [Act, s 4 and
Schedule][ky-es-act] · [DITC resources][ky-es-resources]

Relevant activities include banking, distribution and service centre,
financing and leasing, fund management, headquarters, holding company,
insurance, intellectual property and shipping business. Investment fund
business is excluded from that activity definition. Check the separate
relevant-entity exclusions for domestic companies, local partnerships,
investment funds and entities tax resident outside Cayman. Domestic and
local status require their statutory conditions; ownership alone does not
establish an exclusion. Check the investment-fund definition for an
intermediary structure before treating an operating investment as excluded.
[Act, Schedule, pp 22–25][ky-es-act]

#### Holding-company classification and evidence

The statutory pure equity holding definition requires an entity to hold
only equity participations in other entities and earn only dividends and
capital gains. Apply the guidance's incidental-activity treatment on its
stated facts. Equity participation includes a right to share in an entity's
profits; debt and other non-equity investments do not qualify. A trust,
general partner or service provider holding assets for another person must
be assessed on its own assets, income and activities. [Act, Schedule,
pp 23–25][ky-es-act] · [Guidance, Schedule F.1 and F.3, pp 67–68][ky-es-guidance]

The current relevant-entity and pure equity definitions include qualifying
partnership classes. Read the main guidance's company terminology subject
to its partnership appendix. Check legal form, registration and all
exclusions before applying the reduced test. [Act, Schedule,
pp 24–25 and paragraph (2), p 27][ky-es-act] · [Guidance, Appendix A.3(b)
and (e), pp 87–88][ky-es-guidance]

Keep the following in the ES working paper, alongside the universal
workflow's intake, source records and review trail:

- Legal form, registration, group structure, financial year and evidence for
  each claimed exclusion, including any foreign tax residence claim.
- Asset and ownership records, equity rights, lending arrangements and
  brokerage or custody contracts showing what the entity itself owns.
- All activities and income streams, with gross relevant income reconciled
  to the books under the applicable accounting standards. A loss or absence
  of cash receipts does not establish absence of gross relevant income.
- Applicable company filings and their completion evidence, Cayman service
  agreements, the functions actually performed, human resources and
  premises available for the level and complexity of the holding business.

Missing ownership, activity, income or adequacy evidence makes the affected
classification or test conclusion **Needs Input**. Identify the missing
record; do not treat an unsubstantiated reduced-test claim as compliance.
[Act, ss 4(5), 7 and Schedule definition of relevant income][ky-es-act] ·
[Guidance, II.D, III.A.3 and Schedule F.2][ky-es-guidance]

#### Which test applies

The ordinary test requires the relevant core income-generating activities,
appropriate direction and management in Cayman, and adequate Cayman
expenditure, physical presence and qualified personnel having regard to
the relevant income. Where more than one relevant activity is carried on,
assess each activity. High-risk intellectual property business has a
separate presumption and evidence requirements. [Act, s 4(1)–(4), (7)–(8)
and Schedule][ky-es-act]

For a relevant entity whose only relevant activity is pure equity holding
business, s 4(5) instead requires confirmation of both:

1. Compliance with all applicable filing requirements under the Companies
   Act (2026 Revision).
2. Adequate Cayman human resources and premises for holding and managing
   the equity participations.

DITC says this reduced test does not require direction and management in
Cayman. An engaged registered-office provider may provide adequate
resources, depending on how the business operates and its complexity.
A registered address or service invoice alone does not establish that
adequacy. Record the services and resources actually available; the cited
holding-company guidance gives no fixed employee or premises safe harbour.
[Act, s 4(5)][ky-es-act] · [Guidance, Schedule F.2, p 67][ky-es-guidance]

**Partnership filing hold:** the appendix confirms that qualifying
partnerships can access the reduced test, whilst s 4(5)(a) still refers to
applicable Companies Act filings. The sources reviewed here do not
establish a substituted Partnership Act filing limb. Record the supported
classification and available evidence, but mark the final reduced-test
compliance conclusion **Needs Input** until that filing-limb application is
resolved for the legal form. Do not invent an equivalent filing rule or
exclude partnerships merely because the main guidance uses company
terminology. Historical commencement questions for pre-existing
partnerships also require separate period-specific verification.
[Act, s 4(5) and Schedule][ky-es-act] · [Guidance, partnership appendix,
pp 86–88][ky-es-guidance]

#### Five manual classification checks

These hypothetical controls state expected classifications and remaining
evidence requirements. They are manual checks, not executed filing or
compliance tests. Establish the relevant-entity gates and all activities
for each case before using its result.

| Facts | Expected classification and test | Evidence and surviving duties |
| --- | --- | --- |
| A relevant company directly holds subsidiary equity, receives dividends into an interest-bearing bank account and uses that account only for those receipts and its expenses. It has no other activity. | On the guidance's stated facts, incidental bank interest preserves pure equity holding classification. Apply the reduced test. | Establish ownership and the limited bank-account use, applicable filings and adequate Cayman resources. ES notification and an ES return remain required. [Guidance F.3(a), pp 67–68][ky-es-guidance] |
| An entity holds equity together with an interest-bearing bond, debt investment, government security or property interest. | These additional investments take it outside the guidance's pure equity holding definition. Establish whether another relevant activity applies before selecting the ordinary test. | Check every activity separately. The financing and leasing definition requires a business providing credit for consideration and excludes financial leasing of land or interests in land. Preserve notification duties; determine return and test duties from the established activities. [Act, s 4 and Schedule][ky-es-act] · [Guidance F.1, p 67][ky-es-guidance] |
| A relevant entity's only asset is a contractual claim against a broker; the broker holds the account's underlying equities. | On those precise ownership facts, the guidance says it is not carrying on holding company business. The reduced holding-company test does not apply. | Keep the brokerage and ownership documents. This result does not classify every nominee or custody arrangement. ES notification remains required; check other activities before concluding on an ES return or another test. [Guidance F.3(b), p 68][ky-es-guidance] |
| A relevant entity directly holds equity for its own account and receives dividends or capital gains, with passive collection or more active management of those holdings. | Passive collection can be relevant activity. Active holding management alone does not create a separate statutory holding-company test. Recheck the actual assets, income and any additional activity. | Assess adequacy against the operations and complexity. Do not assume passive status removes the reduced test or that a service provider guarantees compliance. Keep notification and applicable reporting duties separate. [Act, s 4(5), (8)][ky-es-act] · [Guidance II.C.1, III.A.3 and F.1–2][ky-es-guidance] |
| A relevant entity continues its holding activity but the accounting records establish no gross relevant income for the financial year. | DITC Guidance III.A.1 says a relevant entity with no relevant income need not meet the ES test for that period. Attribute that treatment to the guidance. | Notification and reporting survive; the guidance describes a return akin to a nil return. Verify the gross-income reconciliation. Zero profit or zero cash receipts alone is insufficient, and no current portal selection is established here. [Act, Schedule definition of relevant income][ky-es-act] · [Guidance II.D and III.A.1, pp 15 and 17][ky-es-guidance] |

#### Notification, reporting and output holds

Section 7 requires an entity's annual notification, with supporting evidence
reasonably required by the Authority, at the time and in the form and
manner it specifies. A relevant entity required to satisfy the test reports
within 12 months after its financial year end. DITC's no-relevant-income
treatment retains notification and reporting, so do not infer a reporting
exemption from that test treatment. [Act, s 7(1)–(4)][ky-es-act] ·
[Guidance III.A.1 and IV.A–B][ky-es-guidance]

Output the entity/exclusion decision, activity classification, gross
relevant-income reconciliation, applicable test, evidence for each limb and
the separate notification/return obligations. Mark each unresolved item
**Needs Input**. Current ES notification and return screens, submission
fields, general-partner return non-duplication procedures and historic
commencement disputes are outside this section's verified scope. Confirm
the Authority's current instructions before submission; the guidance's
prospective portal wording does not establish a present filing procedure.
[Guidance, partnership appendix, p 86][ky-es-guidance]

See the [formation and reporting guide](ky-company-formation.md#accounts-audits-and-tax-cooperation)
for the wider filing context and the [cross-border guide](ky-corporate-income-tax.md#economic-substance-and-financial-account-information)
for evidence of foreign tax residence.

#### ES workflow controls

For the selected classification task, retain the universal workflow's
profile confirmation, refusal checks, source conditions and all 4 outputs:
working paper, reviewer brief, action list and review checklist. Check
R-KY-3 and R-KY-ES-REVIEW before substantive work. If a refusal fires,
follow the base's refusal trace and stop that engagement. Section 6.1
supplies a selected classification path; the other country sections do not
establish a complete return or engagement workflow on their own. Load the
relevant topical guides and verify their scope before operational use.

Use the evidence groups above as the ES additions to the structured intake.
Also confirm the requested output, the financial year and the reviewer's
credentials and engagement scope. Combine overlapping questions with the
base intake. Do not ask for real taxpayer data to demonstrate the manual
cases.

| Unresolved input | Treatment within the selected scope |
| --- | --- |
| Legal form, exclusion or ownership | Hold the affected entity or holding-company classification as Needs Input; obtain registration, rights and ownership evidence. |
| Other assets, activities or income | Hold the test selection until the full asset/activity and gross-income reconciliation is available. |
| Claimed absence of relevant income | Keep the no-income test treatment unresolved until the books support it; retain notification/reporting work. |
| Filing-limb or resource adequacy evidence | Hold the compliance conclusion; a supported classification does not establish test satisfaction. |

**Reviewer attention policy:** flag every ES classification, exclusion,
test-selection and compliance conclusion for review, including a case with
no identified cash impact. There is no monetary threshold below which this
review is waived. This is a workflow policy, not a statutory threshold.
Record any uncalculated cash impact as uncalculated; do not turn it into
zero tax or a penalty estimate.

Add an ES decision row for each activity to the working paper. Record the
financial year, legal form, exclusion evidence, ownership facts, gross
relevant income, classification, selected test, each limb's evidence,
primary provision and period, notification/return obligations, unresolved
items and reviewer decision. Carry each held item and required document
into the action list. Add the 5 manual case results, T2 judgements and
Needs Input items to the reviewer brief, with a source and reason for each.
Use the ES items in the Review Checklist Items section below for both
self-check and reviewer delivery. Do not replace the base's checks or
sign-off with these additions.

[ky-es-act]: https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/2018/2018-0045/2018-0045_2026%20Revision.pdf
[ky-es-guidance]: https://www.ditc.ky/wp-content/uploads/Economic-Substance-Guidance.pdf
[ky-es-resources]: https://www.ditc.ky/es/es-legislation-resources/

### 6.2 Duty Concessions

Check a development's specific relief approval, its conditions and the instrument or import declaration it covers. Section 5.2 covers stamp duty and the [2026 imports guide](ky-vat-gst.md#relief-and-additional-charges) covers Cabinet's related customs concessions. [Stamp Duty Act, s 20(6)](https://judicial.ky/wp-content/uploads/stamp-duty-act-2019-revision.pdf) · [Cabinet announcement, 14 January 2026](https://gov.ky/w/cayman-brac-duty-concessions-extended)

### 6.3 Real Estate (Non-Caymanian)

- The government describes no general restriction on foreign ownership of land. The RL1 checklist separately requires exempted companies to provide permission to hold property from the Minister of Finance. Apply the valuation and rate rules in Section 5.2 and check the purchaser's legal form and relief eligibility before filing. [Government overview](https://cigarchives.gov.ky/economy) · [Lands and Survey RL1 checklist](https://www.caymanlandinfo.ky/forms-and-guidelines)

## Section 7 -- Excel Working Paper Template

```
CAYMAN ISLANDS -- Working Paper

A. IMPORT DUTIES
  A1. Import value                                 ___________
  A2. Category / duty rate                         ___________
  A3. Total duty                                   ___________

B. EMPLOYMENT OBLIGATIONS
  B1. Total payroll                                ___________
  B2. Pension contributions (10%)                  ___________
  B3. Health insurance cost                        ___________
  B4. Work permit fees                             ___________

C. ENTITY FEES
  C1. Annual registration fee                      ___________

REVIEWER FLAGS:
  [ ] Economic substance filing required?
  [ ] Work permits current?
  [ ] Pension contributions current?
```

## Section 8 -- Bank Statement Reading Guide

**Bank Statement Reading Guide**

| Bank | Format | Key Fields |
| --- | --- | --- |
| Cayman National, Butterfield | PDF, CSV | Date, Description, Debit, Credit, Balance |
| CIBC FirstCaribbean | CSV | Date, Narrative, Amount |

## Section 9 -- Onboarding Fallback

```
ONBOARDING QUESTIONS -- CAYMAN ISLANDS
1. Nature of inquiry (employment, imports, entity, property)?
2. Entity type (exempted company, LP, fund)?
3. Employees in Cayman? How many?
4. Non-Caymanian employees (work permits)?
5. Import goods into Cayman?
6. Own property in Cayman?
7. Relevant activities for economic substance?
8. Hotel/tourism operations?
9. Annual registration fee current?
10. Prior customs/duty filings available?
```

## Section 10 -- Reference Material

**Reference Material**

| Topic | Reference |
| --- | --- |
| Tax concessions | Tax Concessions Act (Revised) |
| Customs duties | Customs Tariff Act (Revised) |
| Companies | Companies Act (Revised) |
| Economic substance | [Economic Substance Act (2026 Revision)][ky-es-act] and [DITC Guidance v3.2 (July 2022), including partnership appendix][ky-es-guidance]; selected holding-company scope in Section 6.1 |
| Pensions | National Pensions Act |
| Health insurance | Health Insurance Act |
| Stamp duty | Stamp Duty Act |
| Tourism tax | Tourism Accommodation Tax |

## Review Checklist Items

For the selected Section 6.1 ES path, add these to the base's self-checks
and reviewer checklist:

- Confirm the period, legal form, all relevant activities and evidence for
  each exclusion. Match direct ownership or broker-claim facts to the
  selected classification; do not generalise the examples.
- Reconcile gross relevant income to the books, separately from profit and
  cash receipts. Preserve the guidance attribution and continuing
  notification/reporting duties in a no-income case.
- Check the selected test and each limb's evidence, including actual Cayman
  resources. Retain the partnership filing-limb hold and all other Needs
  Input items; no final compliance conclusion may bypass them.
- Manually compare all 5 hypothetical cases with their expected results and
  cited provisions. Record any departure and its cause. These controls do
  not establish an executed taxpayer workflow.
- Confirm that all 4 universal outputs, refusal traces where applicable,
  review flags and action items are present and internally consistent.
  Obtain qualified review before reliance; current submission procedures
  remain outside this verified path.

## Change log

- **3.0, 14 November 2026:** expand selected ES holding-company
  classifications using the 2026 Act and DITC Guidance v3.2 with its
  partnership appendix; add 5 manual controls, source holds and universal
  workflow additions. Update the ES reference and remove the obsolete
  upstream verified-version claim. Other country figures were not
  re-verified by this ES pass.

## PROHIBITIONS

- NEVER state Cayman Islands has income tax -- it does not
- NEVER state Cayman Islands has VAT or sales tax -- it does not
- NEVER state Cayman Islands has payroll tax -- it does not
- NEVER apply direct tax calculations to Cayman entities
- NEVER ignore import duty obligations
- NEVER ignore economic substance requirements
- NEVER ignore CRS/FATCA reporting for financial institutions
- NEVER present calculations as definitive

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

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
