---
name: eg-ae-dtt
description: >
  Use this skill whenever asked about the Egypt-UAE Double Tax Treaty
  — for residents/companies with cross-border flows between the two jurisdictions.
  Trigger on "Egypt UAE tax treaty", "DTT Egypt UAE", "ضريبة الازدواج مصر الإمارات",
  "cross-border Egypt UAE", "Egypt United Arab Emirates withholding". ALWAYS read this
  skill before applying treaty rates.
jurisdiction: EG-AE
tax_year: 2025
tier: 2
last_updated: 2026-07-12
version: 0.1
depends_on:
  - eg-corporate-tax
  - eg-withholding-tax
verified_by: pending
---

# Egypt ↔ UAE Double Tax Treaty (DTT) Summary

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Quick Reference

| Field | Value |
|-------|-------|
| Treaty Name | Agreement between the Arab Republic of Egypt and the United Arab Emirates for the Avoidance of Double Taxation and the Prevention of Fiscal Evasion with Respect to Taxes on Income |
| Old Treaty Signed | 2002 (original agreement) |
| Old Treaty In Force | 2003 |
| New Treaty Signed | 7 November 2021 (replaced the 2002 treaty) |
| New Treaty In Force | 19 April 2021 (entered into force); applies from 1 January 2022 |
| Current Version | New TT (2021) replacing Old TT (2002) |
| MLI Status | Egypt ratified MLI (30 Sep 2020). UAE ratified MLI (29 May 2019). MLI applies to this treaty. |
| Jurisdictions Covered | Egypt (EG), United Arab Emirates (AE) |
| Last Verified | July 2026 |
| Key Note | New treaty fundamentally changes dividend treatment (0% → 5%/10%), capital gains (residence → source state), and adds PPT. Interest remains 10%. UAE has 0% domestic WHT — treaty rates bind Egypt as source state only. |

---

## Withholding Tax Rate Summary

| Income Type | Treaty Rate (New TT) | Treaty Rate (Old TT) | Domestic Rate (Egypt) | Domestic Rate (UAE) | Treaty Article | Notes |
|-------------|---------------------|-----------------------|----------------------|---------------------|----------------|-------|
| Dividends — portfolio | 10% | 0% (no WHT) | 10% (unlisted) / 5% (listed) | 0% | Art 10 | Source state may tax for the first time under new TT |
| Dividends — substantial (≥10% voting stock, 365-day holding) | 5% | 0% (no WHT) | 10% (unlisted) / 5% (listed) | 0% | Art 10 | 365-day holding period requirement (ending on dividend distribution date); branch profit tax ≤5% |
| Interest | 10% | 10% | 20% | 0% | Art 11 | Same rate under old and new treaty; government exemption removed from new TT |
| Royalties — copyright/know-how/patents | 10% | 10% | 20% | 0% | Art 12 | Same rate; varies by category |
| Royalties — film & TV | 15% | 10% | 20% | 0% | Art 12 | Increased from 10% to 15% under new TT |
| Technical services | Under Art 7 (business profits) | Under Art 7 | 20% | 0% | Art 7 | No separate FTS article; taxable only if PE in source state |
| Capital gains — immovable property | Source state | Source state | 22.5% | N/A | Art 13(1) | Source state may tax |
| Capital gains — PE assets | Source state | Source state | 22.5% | N/A | Art 13(2) | Source state may tax |
| Capital gains — shares | Source state | Residence state | 22.5% | N/A | Art 13 | **Major change:** source state may now tax gains from share transfers (unless immovable property exception) |
| Pensions — private | 0% (residence state only) | 0% (residence state only) | Progressive | N/A | Art 18 | Taxable only in residence state |
| Social security | 0% | 0% | N/A | N/A | Art 19 | Government benefits exempt |
| Directors' fees | Source state | Source state | Progressive | N/A | Art 16 | Source state (company's state) may tax |
| Employment income | Residence state (with 183-day exception) | Same | Progressive | 0% | Art 15 | Source state may tax if 183-day test met |

---

## Article-by-Article Summary

### Article 5: Permanent Establishment (PE)

The new treaty modernizes the PE definition with BEPS-aligned provisions:

- **Service PE:** Furnishing of services may give rise to a PE if certain conditions are met (specific provision added)
- **Dependent agent:** New definition tackles commissionaire arrangements and similar strategies (aligned with MLI Article 12)
- **Anti-avoidance for specific activity exemptions:** Anti-fragmentation rule prevents splitting activities to avoid PE status
- **Insurance companies:** Special PE provision for insurance enterprises

**Closely related enterprise:** An enterprise is closely related to another if one controls the other or both are under the same control. Control = owning directly/indirectly at least **50%** of beneficial interest. Protocol: states shall exchange information to identify closely related persons.

### Article 7: Business Profits

- No taxation in source country unless non-resident carries on business through PE
- New rules on profit attribution to PEs (aligned with OECD Authorized OECD Approach)

### Article 10: Dividends — Key Changes

**Old TT:** Exclusive taxing rights to residence state (0% WHT in source state; both states restricted on branch profit tax).

**New TT:** Shared taxing rights:
- **5% WHT** if beneficial owner is a company holding ≥10% of voting stock for **365 days** including the dividend distribution date
- **10% WHT** in all other cases
- Branch profit tax allowed at up to **5%**

**Practical impact:** UAE-resident companies receiving dividends from Egyptian subsidiaries now face Egyptian WHT (previously 0%). The only relief: ≥10% holding → reduced to 5%.

### Article 11: Interest — Minor Changes

- Rate remains **10%** WHT in source state
- Government exemption removed from new treaty
- Same rate functionally for most taxpayers, but government/government-owned entities lose the previous exemption

### Article 13: Capital Gains — Key Changes

**Old TT:** Residence state had exclusive taxing rights on capital gains from share transfers (unless shares derive value from immovable property in source state).

**New TT:** **Source state can tax** gains from transfer of shares — specifically, the country where the entity whose shares are being transferred is a resident may tax the gains.

- Exception: gains from immovable property (Art 13(1) — source state taxes)
- Ships/aircraft (Art 13(3) — management state taxes)

### Article 15: Dependent Personal Services (Employment)

- 183-day threshold: source state may tax if employment exercised in source state ≥183 days in any 12-month period
- UAE has 0% personal income tax — UAE residents working in Egypt may trigger Egyptian taxation if the 183-day threshold is met

### Article 16: Directors' Fees

Source state (where company is resident) may tax directors' fees.

### Article 18: Pensions

- Private pension distributions: **0%** — taxable only in country of residence
- Government social security benefits: **0%** — exempt from source-country withholding

### Article 19: Government Service

- Government salaries: taxable only by paying government
- Government pensions: taxable only by paying government

### Article 21: Other Income

- New clarification for immovable property effectively connected to PE

### Article 28: Savings Clause for Hydrocarbons

The new treaty narrows the savings clause to income/profits from the **extraction of hydrocarbons** only. National laws regarding hydrocarbon extraction taxes are unaffected by the treaty.

### Article 30: Principal Purpose Test (PPT) — NEW

The new treaty adds a **Principal Purpose Test (PPT)** (not in the old treaty):
- Treaty benefits are **denied** when obtaining benefits is the objective or one of the objectives of the arrangement or transaction
- This aligns with OECD BEPS Action 6 and MLI Article 7 standards
- Substance and beneficial ownership requirements must be met to pass the PPT

---

## Tax Residency Certificate (TRC) Requirements

### Egypt side
- **Format:** Original TRC issued by the Egyptian Tax Authority (ETA)
- **Authentication:** Legalisation (Egypt is not an Apostille Convention party)
- **Validity:** 1 year from date of issue
- **Process:** Egypt applies **pay-and-refund mechanism** under Ministerial Decree 771/2009
  - 20% domestic WHT rate withheld at source for interest and royalties
  - Non-resident recipient files refund claim with ETA for differential between domestic rate and treaty rate

### UAE side
- **Format:** Tax Residency Certificate issued by UAE Federal Tax Authority (FTA) or Ministry of Finance (MoF)
- **Validity:** Typically 1 year from date of issue
- **Process:** UAE residents apply to FTA/MoF for TRC; UAE does not withhold tax domestically (0% WHT)
- **Corporate tax:** UAE Corporate Tax Law (Federal Decree-Law No. 47 of 2022) introduced 9% CT from June 2023. TRC must confirm status under this regime. Free zone entities must confirm qualifying free zone person status.
- **Economic Substance Regulations (ESR):** UAE residents claiming treaty benefits must comply with ESR requirements; substance is increasingly linked to treaty access.

---

## Mutual Agreement Procedure (MAP)

| Field | Egypt | UAE |
|-------|-------|-----|
| Competent Authority | Ministry of Finance — Egyptian Tax Authority (ETA), Conflict Resolution Department | Ministry of Finance (MoF) — International Tax Relations |
| Time Limit | 3 years from first notification (if MLI MAP applies) | 3 years from first notification (if MLI MAP applies) |
| Arbitration | Not included (standard MAP only) | Not included (standard MAP only) |
| MLI MAP | MLI Article 16 — enhanced MAP (Egypt ratified 30 Sep 2020) | MLI Article 16 — enhanced MAP (UAE ratified 29 May 2019) |

### MAP Contact Points

- **Egypt:** Egyptian Tax Authority (ETA) — Conflict Resolution Department, Ministry of Finance, Cairo
- **UAE:** Ministry of Finance (MoF) — International Tax Relations / Tax Treaty Department

---

## Anti-Treaty-Shopping / PPT (Principal Purpose Test)

The new treaty includes a standalone **Principal Purpose Test (PPT)** (Article 30):
- Treaty benefits are **denied** when obtaining benefits is the objective or one of the objectives of the arrangement or transaction
- This is a **new provision** — the old 2002 treaty did not have a PPT
- **Substance requirements:** Both ETA and UAE FTA may examine whether the treaty claimant has genuine economic substance in the residence state
- **Free zone considerations:** UAE free zone entities must demonstrate real substance (offices, employees, genuine business activities) to pass PPT scrutiny. Letterbox companies in free zones risk benefit denial.
- **Economic Substance Regulations (ESR):** UAE ESR compliance is linked to treaty access — entities failing ESR tests may face scrutiny under PPT when claiming treaty benefits against Egypt
- **MLI application:** Both states adopted MLI Article 7 PPT, which may also apply to the treaty independently of Article 30

---

## Cross-References to Upstream Skills

- **eg-corporate-tax** — Egypt's corporate income tax (22.5%) applies to resident companies and PEs of non-residents; treaty rates reduce WHT on outbound payments
- **eg-withholding-tax** — Egypt's domestic WHT rates (dividends 5%/10%, interest 20%, royalties 20%, services 20%); treaty provides reduced rates but pay-and-refund mechanism applies
- **oecd-model-treaty-defaults** — Reference for articles not individually summarized in this corridor file
- **withholding-tax-matrix** — Cross-reference for domestic WHT rates across jurisdictions
- **cross-border-tax-router** — Entry point for multi-jurisdictional personal tax routing

---

## Pitfalls and Practical Notes

1. **New treaty dividend shock:** The new treaty fundamentally changes dividend treatment for UAE residents — from 0% to 5%/10%. UAE investors in Egyptian companies must now budget for Egyptian WHT on dividends. The 5% rate requires ≥10% voting stock held for 365 days including distribution date.

2. **Capital gains reversal:** The residence-state exemption for share gains is eliminated. Egyptian-source share disposals may now be taxed in Egypt at 22.5%. This is a major change for UAE residents holding shares in Egyptian companies. Plan share disposals carefully.

3. **Egypt pay-and-refund trap:** Egypt does NOT automatically apply reduced treaty rates for interest and royalties. Domestic 20% WHT is withheld; refund claim filed later with the ETA. Budget for cash flow timing impact of up to 12+ months for refund processing.

4. **Film & TV royalty increase:** Royalty rate for film and TV rights increased from 10% to 15% under the new treaty. Media companies should verify which royalty category applies to their specific income streams (know-how 10%, film/TV 15%).

5. **365-day holding period for 5% dividend:** The 365-day holding period must include the date of dividend distribution. If shares are acquired shortly before distribution, the 10% rate applies instead of 5%.

6. **Technical services — no FTS article:** There is no separate Fees for Technical Services (FTS) article. Non-IP technical services fall under business profits (Art 7), taxable only if PE exists in source state. This is a significant advantage over Egypt's 20% domestic WHT on service payments — but requires careful PE analysis.

7. **UAE corporate tax interaction:** UAE introduced Corporate Tax (9% from June 2023). Previously, UAE entities had no income tax, meaning treaty benefits were primarily about avoiding Egyptian WHT. Now, foreign tax credits (FTC) may be available in UAE for Egyptian tax suffered — verify UAE CT law provisions.

8. **Free zone substance:** UAE free zone entities must have genuine substance to claim treaty benefits. PPT + ESR scrutiny means that entities established in free zones for the sole purpose of obtaining treaty benefits risk denial. Verify that the free zone entity conducts core income-generating activities in the UAE.

9. **Government exemption removed:** The government/central bank exemption for interest has been removed from the new treaty. Government-owned entities that previously enjoyed 0% interest must now verify their position under the new treaty.

10. **MLI effective dates:** MLI provisions apply to WHT from dates on or after 1 January 2021 (Egypt) / dates per UAE MLI position. Check whether MLI PPT or treaty PPT applies first depending on effective dates.

---

## Sources

- **Deloitte Middle East — New UAE-Egypt Tax Treaty analysis:** https://www.deloitte.com/middle-east/en/services/tax/perspectives/update-on-the-new-uae-and-egypt-tax-treaty.html
- **PwC Egypt — Withholding taxes:** https://taxsummaries.pwc.com/egypt/corporate/withholding-taxes
- **TaxInPangea — UAE-Egypt treaty:** https://www.taxinpangea.com/treaties/united-arab-emirates-egypt
- **UAE Ministry of Finance — Tax Treaties:** https://www.mof.gov.ae/en/resourcesAndBudget/Pages/TaxTreaties.aspx
- **Egypt ETA — Bilateral agreements:** https://eta.gov.eg/en/content/bilateral-agreements

**Last verified:** July 2026
