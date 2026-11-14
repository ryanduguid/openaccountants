---
name: ad-payroll-social
description: Use this skill whenever asked about Andorra payroll processing for employed persons. Trigger on phrases like "Andorra payroll", "CASS contributions", "IRPF withholding Andorra", "employee CASS", "employer CASS", "retencions Andorra", "CASS-0031", "salari Andorra", "net salary Andorra", "gross to net Andorra", "withholding tax Andorra", "Andorra social security", "retenidor Andorra", "DTF withholding", "IRNR Andorra", "non-resident tax Andorra", "minimum wage Andorra", "salari mínim Andorra", or any question about computing employee pay, withholding tax, or social security contributions for Andorra-based employees. This skill covers IRPF employment income withholding, CASS contributions (employee and employer), non-resident income tax (IRNR), minimum wage, mandatory registration obligations, payslip requirements, and filing obligations. ALWAYS read this skill before processing any Andorra payroll.
jurisdiction: AD
category: payroll
tax_year: 2025
tax_year_notes: "2025 examples; selected withholding regulations applicable from 2024, primary 2025/2026 minimum-wage periods and separately labelled July 2026 CASS information. Actual-period amendments and special-regime eligibility remain to be reconciled."
last_updated: 2026-11-12
version: 0.3
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# andorra-payroll

## Section 1 -- Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Principality of Andorra (Principat d'Andorra) |
| Currency | EUR only |
| Standard pay frequency | Monthly (most common) |
| Tax year | Calendar year (1 January -- 31 December) |
| Income tax system | IRPF (Impost sobre la Renda de les Persones Físiques); use the applicable notified/calculated withholding percentage |
| Tax authority | Departament de Tributs i de Fronteres (DTF) |
| Social security authority | CASS (Caixa Andorrana de Seguretat Social) |
| Key legislation | Llei 5/2014 (IRPF); Decret 596/2023 (IRPF regulation); Llei 17/2008 (CASS framework); Decrets 4/2025, 8/2026 and 253/2026 (minimum-wage periods); Decret 16/2025 (average salary 2025) |
| Filing portal | e-tramits.ad (IRPF); cass.ad (CASS) |
| Official language | Catalan |
| Validated by | Pending -- requires sign-off by a qualified Andorran tax adviser (assessor fiscal) |
| Skill version | 0.3 |

## Section 2 -- Income Tax Withholding (IRPF)

Employment withholding is a payment on account of annual IRPF. Correct withholding does not itself exempt an employee from an annual return: the government FAQ includes residents with gross employment/property income of at least €24,000 amongst those required to file. See Section 9.4. [Government IRPF FAQ](https://www.e-tramits.ad/tramits/impostos/irpf).

**Source and period boundary, checked 12 November 2026:** the selected IRPF provisions below are from Decret 596/2023, published on 2 January 2024, effective on publication and applicable to tax periods starting from 1 January 2024. The selected IRNR provisions are from Decret 594/2023 in the same issue. These captures do not establish that all later amendments have been reconciled. The guide remains a tier 2 draft pending professional review. Annual tax, deduction, savings, capital-gains and treaty material still needs actual-period primary-law checks; do not use it to infer a current payroll rate. Section 5 separately reconciles the selected 2025/2026 minimum-wage decrees.

### 2.1 Statutory IRPF Rate Structure (Annual General Base)

- **Statutory rate structure overview** — The statutory structure has a 0% band up to €24,000 and a 10% marginal rate above €40,000. A bonification (tax relief) of up to €800 reduces the effective rate on the €24,001--€40,000 slice to approximately 5%.  _(Llei 5/2014; e-tramits.ad IRPF portal)_

**Statutory IRPF Rate Table**  _(Llei 5/2014; Assessors Associats)_

| Annual Taxable Income | Marginal Rate | Note |
| --- | --- | --- |
| €0 -- €24,000 | 0% | General personal minimum exemption |
| €24,001 -- €40,000 | ~5% effective | 10% statutory rate with bonification up to €800 reducing effective rate |
| Above €40,000 | 10% | *(Source: Llei 5/2014; Assessors Associats)* |

**Important:** The 5% effective rate is not a literal bracket -- it results from a bonification mechanism. The statutory marginal rate is 10% throughout the taxable base; the bonification creates the stepped effective rate in practice.

### 2.2 Employer Withholding Procedure (Retencions)

Do not select a withholding percentage from a generic salary-band table or impose a blanket 7% cap. Decret 596/2023 provides the following procedure:

| Income or circumstance | Procedure |
| --- | --- |
| Ordinary employment income subject to CASS contributions | The ministry determines the percentage separately for each payer and communicates it to CASS and the payer. Use the notified rate from the month in which it is communicated. Until the annual notice arrives, continue the rate for the last month of the preceding year |
| Ordinary employment income outside CASS contribution obligations | The payer calculates the rate under articles 24 and 25 using projected fixed/variable remuneration, deductible expenses, reductions and relief. Article 27 governs this payer calculation |
| Courses, conferences and similar specified teaching income, unless economic-activity income; specified notice/dismissal compensation | Article 24(2) specifies a fixed 10% rate. Classify the payment and any mandatory-compensation exemption before applying it |
| Ministry lacks the remuneration data needed to calculate the rate | Article 24(3) specifies 10% |
| Employee requests a higher percentage | Article 24(5) permits this; retain the request and applicable communication |
| Circumstances change | Article 25 requires regularisation where the change exceeds 1 percentage point. Its recalculated rate is expressed to 2 decimals and may not exceed 10%; this is not a general 7% cap. CASS regularisation is quarterly |

For ordinary cash pay, withholding = actual gross employment income for the payment × applicable percentage. Annual gross ÷ 12 is a monthly amount only under an equal-pay assumption. A projection used to determine a rate does not replace actual taxable pay. In-kind income and payments on account require their own valuation and treatment.

The annual tax summary in Section 2.1 is not a substitute for this procedure. Obtain the notified rate or evidence of a valid payer calculation, its effective month and the relevant employee declarations before processing. [Decret 596/2023, articles 24–27](https://www.bopa.ad/Documents/Detall?doc=GD_2023_12_29_12_41_49).

### 2.3 IRPF Deductions Affecting Tax Base

**IRPF Deductions Table**  _(aaa.ad 2025 tax return guide; Bloomberg Tax IRPF 2025 filing announcement)_

| Deduction | Annual Amount |
| --- | --- |
| General personal minimum (exemption) | €24,000 |
| Per qualifying dependent child (<25 yrs, living with taxpayer, income ≤ minimum wage) | €1,000 |
| Supplemental for dependent child in higher education | €300 additional |
| Per qualifying ascendant (>65 yrs, living with taxpayer, income <€12,000) or descendant <25 | €750 |
| Primary residence mortgage: 50% of annual mortgage payments, capped | €5,000/taxpayer/year |
| Affordable rental housing investment: 50%, capped | €5,000/taxpayer/year |

### 2.4 Savings / Investment Income (Base de l'Estalvi)

**Savings/Investment Income Table**  _(Elysium Consulting / Invicoandorra)_

| Income Type | Rate |
| --- | --- |
| First €3,000 savings/investment income per year | 0% (exempt) |
| Savings/investment income above €3,000 | 10% flat |
| Dividends from Andorran entities (corporate tax already paid) | Fully exempt |
| Foreign dividends | 10% (unless treaty relief applies) |

### 2.5 Capital Gains -- Special Exemptions

- Shares with ≤25% stake: exempt
- Any asset held ≥10 years: exempt
- Real estate capital gains: generally exempt if held ≥10 years

## Section 3 -- Non-Resident Income Tax (IRNR)

Determine non-residence, Andorran-source employment, exemptions, any treaty treatment and any elected frontier/seasonal-worker regime before choosing a rate. A blanket 10% rule for every non-resident employee is insufficient: articles 30–32 of Decret 594/2023 address elections and distinct withholding treatment for qualifying seasonal/frontier workers. The examples below assume a separately confirmed 10% rate; they do not establish eligibility or a general rate schedule.

| Withholding category | Filing and payment under article 24 |
| --- | --- |
| Employment income paid by CASS or subject to CASS contributions | Monthly declaration and payment to the finance ministry on days 1–15 of the following month; a joint CASS declaration may be used |
| Other income subject to IRNR withholding | During the month after each calendar quarter, using the approved model. Article 24(1) also permits amounts relating to income accrued in the quarter's last month to be declared in the following quarter's liquidation period |

Article 29(2) requires a withholding certificate when the invoice, receipt or equivalent document does not show the withholding, or when the recipient requests one. Article 29(3) separately requires payers to communicate the preceding quarter's withholding/payments on account to recipients during the first 30 calendar days of April, July, October and January. Article 24(4) allows the ministry to request an annual summary at the fourth-quarter payment deadline; do not substitute IRPF's annual certificate rule for these IRNR obligations.

Article 27 preserves specified withholding exemptions, including applicable treaty relief, without necessarily removing declaration obligations. Do not treat a bank description or the employee's nationality as proof of tax treatment. Actual-period law, underlying statutory rates, treaty eligibility and the current approved forms still need confirmation. [Decret 594/2023, articles 24, 27 and 29–32](https://www.bopa.ad/Documents/Detall?doc=GD_2023_12_29_13_31_02).

## Section 4 -- CASS Social Security Contributions

### 4.1 Governing Framework

CASS is the social security body under Llei 17/2008. Its salaried-worker guidance sets out the rates, contribution base, declaration obligations and surcharges selected below. Self-employed reference salaries and percentage tiers must not be imported into the ordinary employee contribution base. [CASS contributions, surcharges and sanctions](https://www.cass.ad/cotitzacions-recarrecs-sancions).

### 4.2 Contribution Rates -- Standard Salaried Employees

**Standard contribution rates**, as displayed in the [CASS salaried-worker guidance checked 12 November 2026](https://www.cass.ad/cotitzacions-recarrecs-sancions). Verify the requested period and any special regime before use.

| Branch | Employee | Employer | Total |
| --- | --- | --- | --- |
| General Branch (health, maternity/paternity, temporary disability, death/orphan benefits) | 3.0% | 7.0% | 10.0% |
| Retirement Branch (retirement, widow/widower, survivor pensions) | 3.5% | 8.5% | 12.0% |
| **TOTAL** | **6.5%** | **15.5%** | **22.0%** |

**Special case: employee already receiving a retirement pension.** The same CASS guidance provides for General Branch contributions only.

| Branch | Employee | Employer | Total |
| --- | --- | --- | --- |
| General Branch only | 3.0% | 7.0% | 10.0% |
| Retirement Branch | Not applicable | Not applicable | -- |
| **TOTAL** | **3.0%** | **7.0%** | **10.0%** |

### 4.3 Occupational Accident Coverage

- **Occupational accident coverage** — There is no separate employer occupational risk premium. Occupational accidents and diseases are covered within the General Branch. The standard 15.5% employer contribution subsumes this coverage.  _(Elysium Consulting CASS 2025 guide)_

### 4.4 Contribution Base

The salaried contribution base is qualifying global remuneration, rather than necessarily the cash paid into the employee's account.

- Included items in the CASS guidance include salary supplements, bonuses, gratuities, monetary/non-monetary incentives, advantageous loans, private insurance, specified accommodation/meals/travel benefits, indemnities, settlements and other remuneration.
- Exclusions include customer tips, employer liberalities, qualifying travel/subsistence/transport/accommodation expense reimbursements and financing/benefits of supplementary employer pension plans. A payment's label alone does not establish an exclusion.
- Apply the relevant CASS rules to classify and value benefits and termination payments. Do not assume every reimbursement is excluded.
- The selected sources do not establish an ordinary salaried contribution ceiling. They also do not prove that no special limit can exist. Do not apply the former self-employed €3,520.36/137.5% figure to employees; require authority for any proposed cap or special base.

[CASS salaried contribution guidance](https://www.cass.ad/cotitzacions-recarrecs-sancions).

### 4.5 Separate Article 99 Employee Supplement

For General Branch benefit rights, Article 99 of Llei 17/2008 requires the global monthly contribution base to reach the official minimum, subject to the specified special regimes and regulatory conditions. The replacement text is in [Llei 18/2014, article 25](https://portaljuridicandorra.ad/L2014018). Under [the contribution/collection regulation, article 19](https://portaljuridicandorra.ad/DR20150527A), the employee declares and pays a separate supplement at **10% of the shortfall**, for the General Branch only. Aggregate all salaried jobs. A person entitled to General Branch benefits for a reason other than their salary contributions is not required to supplement under article 19(3). Confirm that entitlement before applying the exception.

This supplement does not automatically increase the employer's ordinary payroll base, is not a 22% charge and is not automatically deducted through the cash-pay worksheet. Confirm the employee's actual eligibility, affiliation and relevant month's threshold first.

**Period-specific CASS instructions:** the [9 July 2026 informational factsheet, pages 1–2](https://www.cass.ad/sites/default/files/arxius/CASS_COMPLEMENT%20ART99%20ASS%20fitxa%2009-07-2026.pdf) uses **€1,568.67 from 1 July 2026**. Section 5 gives €1,525.33 for January–June 2026; do not use either amount for the whole year. The factsheet says:

- Register using CASS-0087, effective from presentation until cancellation. Declare/pay online with a digital certificate on days 1–15 of the following month.
- Make a zero declaration when salary reaches the minimum or temporary incapacity lasts the entire month. Aggregate all salaried jobs.
- Ask CASS for the actual amount for partial-month registration, partial-month incapacity or benefits in kind rather than applying the simple shortfall formula.

The factsheet expressly has **no legal validity**; published BOPA law controls. It identifies exceptions for people affiliated to the specified regimes, including qualifying students/high-performance athletes aged 25–30 and qualifying indirectly insured low-paid employees. Age or low pay alone does not establish eligibility.

**Eligibility/source conflict:** [Llei 4/2022, final provision 6(15)](https://www.portaljuridicandorra.ad/L2022004_0) requires voluntary admission to the 25–30 regime, inability to register as indirectly insured, recognised studies or recognised high-performance-athlete status, no regular work and no self-employed activity. For article 224, [Llei 1/2024, final provision 4(10)](https://www.portaljuridicandorra.ad/L2024001_0) specifies part-time employment, indirect-insurance status and no concurrent economic/professional self-employed activity under article 19. Its reproduced eligibility paragraph omits the below-minimum wording present in its title. The [CASS web page](https://www.cass.ad/complement-de-salari) instead says these low-paid workers are **not** indirectly insured, contrary to the July factsheet. Do not resolve those discrepancies by silently changing a negation or granting an exemption. Obtain the applicable BOPA text and CASS confirmation of the person's regime before relying on article 224.

The legal copies above establish selected provisions, not a complete amendment chain. Llei 18/2014's final provision 3 commences it on the first day of the month after 6 months from publication; Llei 4/2022 and Llei 1/2024 generally commence the day after publication, with specified exceptions. Their BOPA publication identities/dates and any relevant later corrections remain to be reconciled before determining an individual's actual-period entitlement.

## Section 5 -- Minimum Wage (Salari Mínim Interprofessional)

The published decrees fix the following hourly amounts and monthly equivalents for a 40-hour week (hourly rate × 40 × 52 ÷ 12, rounded to cents). Financial effect can precede publication and legal commencement.

| Financial effect period | Hourly minimum | Monthly equivalent | Published BOPA instrument | Publication / commencement |
| --- | --- | --- | --- | --- |
| From 1 January 2025, for 2025 | €8.35 | €1,447.33 | [Decret 4/2025, sole article](https://www.bopa.ad/Documents/Detall?doc=GD_2025_01_15_12_19_56) | 16 January 2025 / 17 January 2025 |
| 1 January–30 June 2026 | €8.80 | €1,525.33 | [Decret 8/2026, sole article](https://www.bopa.ad/Documents/Detall?doc=GD_2026_01_14_12_20_08) | 15 January 2026 / 16 January 2026 |
| From 1 July 2026 | €9.05 | €1,568.67 | [Decret 253/2026, articles 1–3](https://www.bopa.ad/Documents/Detall?doc=GD_2026_07_02_14_45_22) | 8 July 2026 / 8 July 2026 |

Decret 253/2026 gives financial effect from 1 July, requires employers to adjust salaries below the new minimum and repeals the conflicting Decret 8/2026 amount from that effect date. Use its fixed €9.05 amount; do not substitute an unrounded percentage calculation. These are the selected instruments checked on 12 November 2026, not a guarantee against a later change.

The 2025 example's €17,367.96 is 12 payments of the rounded €1,447.33 monthly equivalent. It is an arithmetic illustration, not a separately prescribed annual minimum. Confirm hours, the actual period and any other applicable labour rules before declaring compliance; a social-contribution supplement does not itself cure underpayment of wages.

## Section 6 -- Processing Inputs and Defaults

| Parameter | Required treatment |
| --- | --- |
| IRPF withholding percentage | Obtain the applicable notified rate or evidenced payer calculation and its effective month; do not derive it from the retired salary bands |
| Employee/employer CASS | Standard 6.5%/15.5% of the qualifying contribution base; 3%/7% General Branch only for the confirmed retirement-pension case |
| Proposed CASS cap or special base | Require actual-period authority; do not use self-employed reference tiers |
| Tax residence and special regime | Confirm before choosing IRPF/IRNR treatment; no default residence assumption |
| Personal deductions | Use the declarations and prescribed procedure; do not replace a notified rate with a guessed adjustment |
| Pay frequency and currency | Confirm the actual payment period; the cash examples use monthly EUR pay |
| Low-paid employee supplement | Assess separately under the applicable month's Article 99 rules, aggregate salaries, other benefit entitlement and confirmed special-regime conditions |

Sources: [IRPF regulation, articles 24–27](https://www.bopa.ad/Documents/Detall?doc=GD_2023_12_29_12_41_49), [CASS salaried guidance](https://www.cass.ad/cotitzacions-recarrecs-sancions) and the legal/factsheet sources and their limits in Sections 4.5 and 5.

## Section 7 -- Required Inputs

Before computing Andorra payroll, you MUST have:

1. **Employee tax residency status** -- resident (IRPF) or non-resident (IRNR)
2. **Applicable year and remuneration projection** -- fixed/variable annual remuneration and declarations required by the prescribed rate-setting procedure
3. **Actual period pay and qualifying bases** -- distinguish cash gross, taxable employment income, CASS contribution base, benefits and excluded reimbursements; obtain the applicable withholding percentage and its effective month
4. **CASS registration status** -- confirm both employer and employee are registered
5. **Personal deduction declarations** -- children, ascendants, mortgage if applicable (affects DTF-determined withholding rate)
6. **Pension-drawing status** -- if employee is already receiving a retirement pension, different CASS rates apply
7. **Employment start date** -- for pro-rating partial months

### Refusal Catalogue

- **Unknown residency status** — Cannot determine whether IRPF or IRNR applies
- **Salary in non-EUR currency** — Andorra uses EUR exclusively; flag if any other currency is mentioned
- **Double-taxation treaty claim** — Treaty benefit cannot be applied without knowing employee's country of tax residence and the specific treaty provisions -- direct to qualified adviser
- **Unsupported cap or special-base claim** — Do not apply a proposed CASS limit without its actual-period authority; self-employed tiers are not an employee cap
- **Benefits-in-kind valuation** — Housing, vehicles, and meal benefits require valuation -- do not guess
- **Termination payments** — Indemnification amounts under Andorran labour law require legal advice before payroll treatment can be determined

## Section 8 -- Transaction and Payment Pattern Library

This section enables recognition and classification of Andorra-specific payroll entries on bank statements and in accounting records.

### 8.1 Employee Bank Statement Patterns (Salary Credits)

**Employee Bank Statement Patterns Table**

| Pattern Observed | Classification |
| --- | --- |
| NOMINA, SALARI, SUELDO | Net salary payment (credit to employee) |
| PAGAMENT NOMINA [employer name] | Net salary payment |
| TRANSFERENCIA NOMINA | Net salary payment |
| BONUS, PRIMA, GRATIFICACIÓ | Discretionary bonus or one-off payment |
| LIQUIDACIÓ, INDEMNITZACIÓ | Termination payment -- requires separate tax/CASS analysis |
| PAGA EXTRA | Extra salary payment (if contractual 13th/14th month exists) |
| DIETES, DESPLAÇAMENT | Per diems / travel reimbursement -- generally not subject to CASS/IRPF if genuine expense reimbursement |

### 8.2 Employer Bank Statement Patterns (Payroll Debits)

**Employer Bank Statement Patterns Table**

| Pattern Observed | Classification |
| --- | --- |
| CASS-0031, COTITZACIO CASS | Monthly CASS contribution payment (employer + employee shares) |
| CASS [employer number] | CASS remittance |
| DTF IRPF, RETENCIO IRPF, TRIBUTS | IRPF withholding remittance to DTF |
| DTF IRNR, RETENCIO IRNR | IRNR withholding remittance (non-resident employees) |
| PAGAMENT NOMINES, TRANSFERENCIES NOMINA | Bulk salary disbursement to employees |
| SEGURETAT SOCIAL, COTITZACIONS | Social security contributions (CASS) |

### 8.3 CASS-0031 Form Classification

The published blank CASS-0031 combines CASS contributions and IRPF/IRNR withholding in one declaration, with separate tax and social-contribution columns and totals. Page 2 assigns tax withholding to DTF and contributions to CASS. Do not combine them into one undifferentiated contribution total or assume that filing alone proves both payments. IRPF article 33 provides for the same payment method as CASS and, by default, the same direct-debit account, whilst allowing another account or method. The current authenticated online fields and actual payment instructions still need practitioner confirmation. [Published CASS-0031, pages 1–2](https://www.cass.ad/sites/default/files/tramits/cass-0031.pdf), [IRPF regulation, article 33](https://www.bopa.ad/Documents/Detall?doc=GD_2023_12_29_12_41_49).

### 9.1 CASS Monthly Declaration (CASS-0031)

| Item | Detail |
| --- | --- |
| Published form | CASS-0031, Full de declaració de cotitzacions i retencions IRPF/IRNR |
| Frequency/window | Monthly declaration and payment on days 1–15 of the following month |
| Contributions | Employer remits employee and employer shares of the qualifying base; apply the retirement-pension exception where appropriate |
| Separate tax totals | Distinguish IRPF/IRNR withholding from CASS contributions and reconcile both obligations |
| Submission | CASS guidance requires employers, including domestic employers, to use online services with a digital certificate. The published paper form is a reference, not proof of current online fields |

[CASS guidance](https://www.cass.ad/cotitzacions-recarrecs-sancions), [CASS-0031, pages 1–2](https://www.cass.ad/sites/default/files/tramits/cass-0031.pdf).

### 9.2 Approved DTF Models and Communications

Use the approved model for the actual income category and procedure. This reconciliation confirms CASS-0031's published content, but does not authenticate the former guide's mappings of DTF forms 310/312/312-A/315/316/317/311/311-A/340/341. Do not rely on those numbers as operational directions without checking the current official model.

For IRPF employment income subject to CASS contributions, articles 29 and 31 require payer communications including new-employment remuneration information; article 31 sets a 10-day period from the start of a new employment relationship. Article 29(3) excludes non-CASS employment income from that payer-communication obligation; its separate payer-calculation route remains in Section 2.2. This DTF communication is distinct from CASS affiliation/registration. [Decret 596/2023, articles 29 and 31](https://www.bopa.ad/Documents/Detall?doc=GD_2023_12_29_12_41_49).

### 9.3 IRPF Withholding, Annual Summary and Certificate

| Obligation | Period/window in Decret 596/2023 |
| --- | --- |
| CASS-covered employment withholding, article 33(1) | Monthly declaration and payment to the ministry on days 1–15 of the following month; the declaration may be joint with CASS |
| Other employment withholding, article 33(2) | Quarterly declaration/payment during April, July, October and January for the preceding quarter. This selected provision does not prescribe the former guide's 20-day deadline |
| Annual employment withholding summary, article 34 | For non-CASS income: 1–31 January of the following year. A separate summary is not required for CASS-covered income, for which the ministry obtains the monthly data |
| Withholding certificate, article 35 | 1 January–31 March of the following year. For CASS-covered income, issuing it is mandatory only if expressly requested |

The monthly/quarterly distinction follows the income's CASS obligation, not employer size or withholding volume. IRNR has its own article 24 procedure in Section 3. [Decret 596/2023, articles 33–35](https://www.bopa.ad/Documents/Detall?doc=GD_2023_12_29_12_41_49).

### 9.4 Annual IRPF Return (Employee Level)

The government FAQ lists residents required to file as those with economic-activity income, gross employment/property income of at least €24,000, unwithheld movable-capital income exceeding €3,000 or capital gains/losses. Exempt income is excluded when assessing these conditions. Correct employment withholding does not remove these tests.

The published filing window is 1 April–30 September of the year following the income year, so the stated window for 2025 income is 1 April–30 September 2026. Check the actual campaign, approved model and access method before filing; this source review does not authenticate every former Form 300 annex mapping. [Government IRPF FAQ](https://www.e-tramits.ad/tramits/impostos/irpf).

### 9.5 Registration and New Hires

CASS guidance requires employees to be insured from the start of employment. Missing registration does not remove the employer's contribution obligation. Confirm employer/employee affiliation and the current CASS registration procedure before processing. The former guide's specific 5-day new-hire deadline is not established by the sources selected here.

Keep CASS registration separate from the DTF's withholding-agent and remuneration-communication requirements. The 10-day DTF new-employment payer communication in articles 29 and 31 applies to the CASS-covered income described in Section 9.2; it is not a substitute CASS registration deadline. [CASS guidance](https://www.cass.ad/cotitzacions-recarrecs-sancions), [IRPF regulation, articles 29 and 31](https://www.bopa.ad/Documents/Detall?doc=GD_2023_12_29_12_41_49).

### 10.1 CASS Late Payment Surcharges

**CASS Late Payment Surcharges Table**  _(Effective from 1 July 2022 reform; CASS official contributions page)_

| Lateness | Surcharge |
| --- | --- |
| Up to 1 month late | 5% of unpaid amount |
| From 1 month and 1 day through 6 months late | 10% of unpaid amount |
| More than 6 months late | 20% of unpaid amount |

The CASS page labels the 501–20,000 retirement-point range **very serious**; the serious range is 51–500 points and minor infractions carry a warning or 25–50 points. Do not convert points into euros without the applicable valuation or infer a sanction from lateness alone. Use the source's classification for the actual conduct. The surcharge table above is the regime labelled effective from 1 July 2022, not the older daily-rate text also present on the page. [CASS surcharges and sanctions](https://www.cass.ad/cotitzacions-recarrecs-sancions).

### 10.2 IRPF Penalties

Specific penalty percentages for IRPF late filing or late withholding remittance are **[RESEARCH GAP -- not confirmed in reviewed sources; consult DTF directly for the sanction schedule under Llei 5/2014 and Decret 596/2023]**.

### 10.3 Minimum Wage Violation Fines

- **Minimum wage violation fines** — Fines: €500 -- €10,000 per violation.  _(Playroll EOR guide)_

## Section 11 -- Worked Examples

These are cash-only arithmetic illustrations using equal monthly pay, separately assumed withholding percentages and a CASS contribution base equal to the stated gross. They do not derive a rate from salary, establish an actual DTF notice or cover in-kind benefits, treaty elections or an Article 99 supplement. The 2025 wage illustration does not establish a current minimum wage. Round each deduction/contribution to cents, then reconcile net pay.

### Example 1 -- 2025 Minimum Wage Employee (Resident, No Personal Deductions)

**Example 1 table**  _(Decret 4/2025)_

| Item | Calculation | Monthly Amount |
| --- | --- | --- |
| Gross salary | Per Decret 4/2025 | €1,447.33 |
| Employee CASS (6.5%) | 1,447.33 × 6.5% | −€94.08 |
| IRPF withholding (0%) | Assumed applicable rate 0%; not inferred from annual salary | €0.00 |
| **Net pay to employee** | 1,447.33 − 94.08 | **€1,353.25** |
| Employer CASS (15.5%) | 1,447.33 × 15.5% | €224.34 |
| **Total employer cost** | 1,447.33 + 224.34 | **€1,671.67** |

**Profile:** Resident employee, single, no dependants, illustrative annual cash gross = 12 × €1,447.33 = €17,367.96, using the rounded 2025 monthly equivalent in Section 5. This is not the 2026 minimum.

### Example 2 -- Mid-Range Salary (Resident, No Personal Deductions)

**Example 2 table**

| Item | Calculation | Monthly Amount |
| --- | --- | --- |
| Gross salary | 50,000 ÷ 12 | €4,166.67 |
| Employee CASS (6.5%) | 4,166.67 × 6.5% | −€270.83 |
| IRPF withholding (2%) | Assumed applicable rate 2%; 4,166.67 × 2% | −€83.33 |
| **Net pay to employee** | 4,166.67 − 270.83 − 83.33 | **€3,812.51** |
| Employer CASS (15.5%) | 4,166.67 × 15.5% | €645.83 |
| **Total employer cost** | 4,166.67 + 645.83 | **€4,812.50** |

**Profile:** Resident employee, annual gross = €50,000. Monthly gross = €4,166.67.

### Example 3 -- Higher Salary (Resident, No Personal Deductions)

**Example 3 table**

| Item | Calculation | Monthly Amount |
| --- | --- | --- |
| Gross salary | 80,000 ÷ 12 | €6,666.67 |
| Employee CASS (6.5%) | 6,666.67 × 6.5% | −€433.33 |
| IRPF withholding (4.5%) | Assumed applicable rate 4.5%; 6,666.67 × 4.5% | −€300.00 |
| **Net pay to employee** | 6,666.67 − 433.33 − 300.00 | **€5,933.34** |
| Employer CASS (15.5%) | 6,666.67 × 15.5% | €1,033.33 |
| **Total employer cost** | 6,666.67 + 1,033.33 | **€7,700.00** |

**Profile:** Resident employee, annual gross = €80,000. Monthly gross = €6,666.67.

### Example 4 -- Lower-Mid Salary (Resident, Assumed Withholding)

**Example 4 table**

| Item | Calculation | Monthly Amount |
| --- | --- | --- |
| Gross salary | 30,000 ÷ 12 | €2,500.00 |
| Employee CASS (6.5%) | 2,500.00 × 6.5% | −€162.50 |
| IRPF withholding (0.5%) | Assumed applicable rate 0.5%; 2,500.00 × 0.5% | −€12.50 |
| **Net pay to employee** | 2,500.00 − 162.50 − 12.50 | **€2,325.00** |
| Employer CASS (15.5%) | 2,500.00 × 15.5% | €387.50 |
| **Total employer cost** | 2,500.00 + 387.50 | **€2,887.50** |

**Profile:** Resident employee, annual gross = €30,000. Monthly gross = €2,500.00.

### Example 5 -- Non-Resident Employee

**Example 5 table**

| Item | Calculation | Monthly Amount |
| --- | --- | --- |
| Gross salary | 36,000 ÷ 12 | €3,000.00 |
| Employee CASS (6.5%) | 3,000.00 × 6.5% | −€195.00 |
| IRNR withholding (assumed applicable 10%) | 3,000.00 × 10% | −€300.00 |
| **Net pay to employee** | 3,000.00 − 195.00 − 300.00 | **€2,505.00** |
| Employer CASS (15.5%) | 3,000.00 × 15.5% | €465.00 |
| **Total employer cost** | 3,000.00 + 465.00 | **€3,465.00** |

**Profile:** Non-resident employee, annual gross from Andorran employment = €36,000. Monthly gross = €3,000.00. Assume the classification, 10% withholding and absence of applicable relief have been separately confirmed; lack of treaty evidence alone does not establish no relief.

**Filing note:** this assumed CASS-covered employment falls within the monthly 1–15 window in IRNR article 24(2), not the other-income quarterly route.

### Example 6 -- Employee Already Drawing Retirement Pension (Resident)

**Example 6 table**

| Item | Calculation | Monthly Amount |
| --- | --- | --- |
| Gross salary | 24,000 ÷ 12 | €2,000.00 |
| Employee CASS -- General Branch only (3.0%) | 2,000.00 × 3.0% | −€60.00 |
| IRPF withholding (0%) | Assumed applicable rate 0%; not inferred from annual salary | €0.00 |
| **Net pay to employee** | 2,000.00 − 60.00 | **€1,940.00** |
| Employer CASS -- General Branch only (7.0%) | 2,000.00 × 7.0% | €140.00 |
| **Total employer cost** | 2,000.00 + 140.00 | **€2,140.00** |

**Profile:** Resident employee who is also receiving a CASS retirement pension, annual gross = €24,000. Monthly gross = €2,000.00.

## Section 12 -- Mandatory Processing Checks

These processing checks do not promote the guide to accountant-reviewed tier 1.

- Confirm the actual period, residence, income category and any special-regime election before choosing IRPF/IRNR treatment.
- Obtain the applicable withholding percentage and effective month using Section 2.2 or the separately confirmed IRNR procedure. Do not substitute the retired salary bands or a blanket 7% cap.
- Confirm CASS registration and the qualifying contribution base. Standard employee/employer rates are 6.5%/15.5%; the confirmed retirement-pension case uses 3%/7% General Branch only.
- Distinguish actual cash pay, taxable employment income and the CASS base. Assess any employee-funded Article 99 supplement separately for its month, confirmed eligibility and other General Branch benefit entitlement.
- Declare and pay CASS-covered employment contributions and withholding in the monthly 1–15 window, retaining separate contribution/tax totals and payment evidence.
- Check the actual-period minimum wage, benefits, termination treatment and any claimed special limit before approving the payroll.

Primary sources and their period limits are in Sections 2.2, 3, 4 and 9.

## Section 13 -- Tier 2 Catalogue (Reviewer Judgement Required)

These items involve judgement, incomplete research data, or complexity that requires a qualified Andorran adviser to resolve before finalising payroll.

**Tier 2 Catalogue Table**

| Situation | Remaining check before reliance |
| --- | --- |
| Withholding notice, declarations or changed circumstances | Obtain the actual percentage, effective month and regularisation evidence; reconcile the requested period's amendments |
| Proposed CASS ceiling or special base | Require the specific salaried-worker authority; no self-employed reference tier |
| Low-paid or multiple-job employee | Reconcile actual-month Article 99 law/threshold, aggregate salaries, other General Branch entitlement, affiliation and the unresolved article 224 source wording before any exemption or separate supplement |
| Treaty or frontier/seasonal-worker claim | Verify residence, actual-period treaty/statute, election and withholding conditions; no general country list proves relief |
| Benefits in kind or termination compensation | Reconcile tax and CASS classification/valuation separately with the relevant law |
| Self-employed or mixed status | Keep employment payroll distinct from economic-activity obligations; no employee-rate inference from self-employed tiers |
| Registration and online submission | Confirm current CASS affiliation steps, authenticated fields, approved DTF models and payment evidence; the published blank form is not an online walkthrough |
| Annual close and recipient reporting | For IRPF apply Section 9.3's summary/certificate distinctions. For IRNR apply Section 3's quarterly recipient notices, certificate conditions and any ministry-requested annual summary; confirm actual campaign instructions |
| Other guide material | Reconcile annual deductions, savings/capital gains, later amendments, occupational coverage and IRPF/minimum-wage penalty provisions with primary law |

The selected sources resolve several former gaps but do not complete actual-period law or practitioner sign-off.

## Section 14 -- Excel Working Paper Template

Use this structure only for cash-only monthly payroll where taxable cash pay equals cash gross. Record benefits, excluded reimbursements, other deductions and separate supplements outside this simplified worksheet, with their own reconciliations.

```
ANDORRA PAYROLL WORKING PAPER
Period / Year: [MONTH YYYY]
Employer CASS / DTF registration: [confirmed evidence]

A  Employee identifier
B  Residence, tax category, pension/special-regime classification
C  Actual cash gross this period (EUR)
D  Remuneration projection / rate notice reference and effective month
E  Applicable IRPF/IRNR percentage (confirmed under the relevant procedure)
F  Period tax withholding (=C×E, rounded to cents)
G  Employee CASS rate (6.5% standard; 3% confirmed retirement-pension case)
H  Employee CASS (=N×G, rounded to cents)
I  Net cash pay (=C−F−H; no other deductions in this simplified case)
J  Employer CASS rate (15.5% standard; 7% confirmed retirement-pension case)
K  Employer CASS (=N×J, rounded to cents)
L  Cash payroll plus employer CASS (=C+K; other costs excluded)
M  Source, classification, valuation and payment evidence
N  Qualifying CASS contribution base (not automatically equal to C)

RECONCILIATION:
Sum C = Sum I + Sum H + Sum F
CASS contribution total = Sum H + Sum K
Tax withholding total = Sum F
Retain distinct CASS and DTF totals and evidence of both obligations.
The published CASS-0031 contains separate tax/social totals.
IRPF article 33 allows the same payment method/account as CASS by default;
confirm the actual payment arrangement rather than assuming one transfer.

FILING:
[ ] CASS contributions and CASS-covered IRPF/IRNR: days 1–15 next month
[ ] Other withholding: apply the relevant quarterly procedure, not employer size
[ ] IRPF annual summary/certificate: apply Section 9.3 and its CASS distinctions
[ ] IRNR recipient notice: first 30 calendar days Apr/Jul/Oct/Jan for prior quarter
[ ] IRNR certificate conditions and any requested annual summary: apply Section 3
[ ] Any Article 99 supplement: separate actual-month eligibility/threshold/return/payment
```

Check: cash gross/CASS base €3,000, standard employee CASS €195 and employer CASS €465 give a CASS total of €660. With an assumed €40 tax deduction, net cash pay is €2,765 and the separate tax total is €40. The two obligations total €700; €700 is not the CASS contribution total.

## Section 15 -- Bank Statement / Terminology Reading Guide

### Andorran Payroll Terms (Catalan)

**Andorran Payroll Terms Table**

| Catalan Term | English Equivalent |
| --- | --- |
| Impost sobre la Renda de les Persones Físiques (IRPF) | Personal income tax |
| Impost sobre la Renda dels No-Residents (IRNR) | Non-resident income tax |
| Caixa Andorrana de Seguretat Social (CASS) | Andorran Social Security Fund |
| Departament de Tributs i de Fronteres (DTF) | Department of Taxes and Borders (tax authority) |
| Retenidor | Withholding agent (employer in payroll context) |
| Retencions | Withholdings (tax withheld from salary) |
| Cotitzacions | Contributions (social security contributions to CASS) |
| Salari brut | Gross salary |
| Salari net | Net salary |
| Nòmina | Payslip / payroll |
| Branca general | General branch (CASS health/disability coverage) |
| Branca de jubilació | Retirement branch (CASS pension coverage) |
| Base de cotització | Contribution base; do not infer a salaried cap from terminology |
| Salari mínim interprofessional | National minimum wage |
| Declaració de cotitzacions | Contributions declaration (CASS-0031) |
| Bonificació | Bonification / tax relief |
| Base imposable | Taxable base |
| Base de l'estalvi | Savings income base |

### Typical Payslip Line Items (Andorra)

**Typical Payslip Line Items Table**

| Payslip Line | Meaning |
| --- | --- |
| Salari base / Sou base | Base salary |
| Complements salarials | Salary supplements (seniority, technical, etc.) |
| Cotització CASS (treballador) | Employee CASS contribution deducted |
| Retenció IRPF / Retenció IRNR | Income tax withholding deducted |
| Total percepcions | Total gross earnings |
| Total deduccions | Total deductions |
| Líquid a percebre | Net pay (take-home amount) |

## Section 16 -- Onboarding Fallback

Return Needs Input before calculating if the actual period, residence/tax category, applicable withholding rate and effective month, actual pay, qualifying CASS base or registration evidence is missing. Confirm pension receipt rather than inferring it from age; the selected exception changes standard rates to 3% employee and 7% employer, not simply half the standard total.

Obtain separate evidence for personal declarations, treaty/special-regime claims, benefits in kind, compensation and low-paid/multiple-job supplements. Identify the missing item and the applicable source condition; do not manufacture a salary-band rate or assume residence.

**Response template:** 'I need [specific missing evidence] for [period] before calculating this payroll. Please provide it or obtain confirmation from a qualified Andorran assessor fiscal.'

## Section 17 -- Reference Material

### Key Legislation

**Key Legislation Table**

| Instrument | Subject |
| --- | --- |
| Llei 5/2014 | Personal income tax (IRPF) -- principal act |
| [Decret 596/2023](https://www.bopa.ad/Documents/Detall?doc=GD_2023_12_29_12_41_49) | Selected IRPF rules published 2 January 2024, applicable to periods starting from 1 January 2024; later amendments not fully reconciled |
| [Decret 594/2023](https://www.bopa.ad/Documents/Detall?doc=GD_2023_12_29_13_31_02) | Selected IRNR withholding/declaration rules; same publication issue; actual-period reconciliation remains |
| Llei 17/2008, 3 October | Social security (CASS framework) |
| Decret 16/2025 (29 January 2025) | Sets average global monthly salary at €2,560.99/month |
| Decrets 4/2025, 8/2026 and 253/2026 | Primary minimum-wage amounts, effect dates and commencement in Section 5 |
| Llei 18/2014 article 25 and contribution/collection regulation article 19 | Article 99 supplement framework and employee formalities, subject to Section 4.5 limits |
| Llei 4/2022 final provision 6(15); Llei 1/2024 final provision 4(10) | Selected special-regime qualification changes; article 224 wording conflict unresolved |

### Official Sources

**Official Sources Table**

| Source | URL |
| --- | --- |
| CASS contributions and surcharges | cass.ad/cotitzacions-recarrecs-sancions |
| CASS-0031 combined declaration form | cass.ad/tramits/cass-0031 |
| e-tramits IRPF portal | e-tramits.ad/tramits/ca/declaracio-de-limpost-sobre-la-renda-de-les-persones-fisiques-irpf/p/tr-irpf |
| e-tramits IRPF forms | e-tramits.ad/tramits/ca/impostos/irpf/formularis |
| Govern.ad IRPF FAQs | govern.ad/ca/l/4194272 |
| Govern.ad IRNR | govern.ad/ca/tematiques/impostos-taxes-i-duana/impostos-en-andorra/impost-sobre-la-renda-dels-no-residents-fiscals-a-andorra |
| Primary minimum-wage decrees | [Government instrument index](https://www.govern.ad/fr/tematiques/ocupacio-i-treball/relacions-laborals-i-seguretat/salaris-i-festius); direct BOPA links in Section 5 |
| Elysium Consulting -- CASS 2025 | elysiumconsultingfirm.com/en/publications/the-cass-in-andorra-contributions-coverage-and-key-facts-for-2025 |
| Primary IRPF withholding procedure | [Decret 596/2023, articles 24–27](https://www.bopa.ad/Documents/Detall?doc=GD_2023_12_29_12_41_49) |
| Bloomberg Tax -- IRPF 2025 filing | news.bloombergtax.com/daily-tax-report-international/andorra-tax-agency-announces-2025-individual-income-tax-return-filing-deadline-releases-filing-guidance |
| WIT Andorra -- IRPF 2025 guide | wit.ad/en/irpf-andorra-2025-guide-deadlines-and-how-to-file-it/ |

### Treaty Boundary

The former secondary-source country list is not an actual-period treaty check. Verify the applicable treaty, entry into force, income article and employee eligibility before relief; this selected payroll reconciliation does not establish a current treaty inventory.

## Section 18 -- Test Suite

Tests 1–6 use the cash-only assumptions in Section 11 and an explicitly assumed applicable withholding rate. They test calculations after classification and rate confirmation, not legal eligibility or rate derivation. Their amounts do not establish minimum-wage compliance or include any separate Article 99 supplement; Test 7 separately illustrates that conditional charge.

**Test 1:** Employee, annual gross €20,000, resident, no deductions.
- Assumed applicable withholding rate: 0%; not derived from annual salary
- Monthly gross: 20,000 ÷ 12 = €1,666.67
- Monthly IRPF: €0.00
- Employee CASS: 1,666.67 × 6.5% = €108.33
- Net pay: 1,666.67 − 0.00 − 108.33 = **€1,558.34**
- Employer CASS: 1,666.67 × 15.5% = €258.33
- Total employer cost: 1,666.67 + 258.33 = **€1,925.00**

**Test 2:** Employee, annual gross €35,000, resident, no deductions.
- Assumed applicable withholding rate: 1%; not derived from annual salary
- Monthly gross: 35,000 ÷ 12 = €2,916.67
- Monthly IRPF: (35,000 × 1%) ÷ 12 = 350.00 ÷ 12 = **€29.17**
- Employee CASS: 2,916.67 × 6.5% = **€189.58**
- Net pay: 2,916.67 − 29.17 − 189.58 = **€2,697.92**
- Employer CASS: 2,916.67 × 15.5% = **€452.08**
- Total employer cost: 2,916.67 + 452.08 = **€3,368.75**
- Reconciliation: 2,697.92 + 29.17 + 189.58 = 2,916.67 ✓

**Test 3:** Employee, annual gross €60,000, resident, no deductions.
- Assumed applicable withholding rate: 3%; not derived from annual salary
- Monthly gross: 60,000 ÷ 12 = €5,000.00
- Monthly IRPF: (60,000 × 3%) ÷ 12 = 1,800 ÷ 12 = **€150.00**
- Employee CASS: 5,000.00 × 6.5% = **€325.00**
- Net pay: 5,000.00 − 150.00 − 325.00 = **€4,525.00**
- Employer CASS: 5,000.00 × 15.5% = **€775.00**
- Total employer cost: 5,000.00 + 775.00 = **€5,775.00**
- Reconciliation: 4,525.00 + 150.00 + 325.00 = 5,000.00 ✓

**Test 4:** Non-resident employee, annual gross €48,000.
- Monthly gross: 48,000 ÷ 12 = €4,000.00
- Assumed applicable IRNR rate 10%: 4,000.00 × 10% = **€400.00**
- Employee CASS: 4,000.00 × 6.5% = **€260.00**
- Net pay: 4,000.00 − 400.00 − 260.00 = **€3,340.00**
- Employer CASS: 4,000.00 × 15.5% = **€620.00**
- Total employer cost: 4,000.00 + 620.00 = **€4,620.00**
- Reconciliation: 3,340.00 + 400.00 + 260.00 = 4,000.00 ✓

**Test 5:** Pension-drawing employee, annual gross €18,000, resident.
- Monthly gross: 18,000 ÷ 12 = €1,500.00
- Assumed applicable withholding rate: 0%; not derived from annual salary
- Employee CASS (general branch only, 3.0%): 1,500.00 × 3.0% = **€45.00**
- Net pay: 1,500.00 − 0.00 − 45.00 = **€1,455.00**
- Employer CASS (general branch only, 7.0%): 1,500.00 × 7.0% = **€105.00**
- Total employer cost: 1,500.00 + 105.00 = **€1,605.00**
- Reconciliation: 1,455.00 + 0.00 + 45.00 = 1,500.00 ✓

**Test 6:** Employee, annual gross €160,000, resident, assumed applicable withholding rate 7%.
- The assumed 7% is an input, not a statutory maximum or salary-band result
- Monthly gross: 160,000 ÷ 12 = €13,333.33
- Monthly IRPF: (160,000 × 7%) ÷ 12 = 11,200 ÷ 12 = **€933.33**
- Employee CASS: 13,333.33 × 6.5% = **€866.67**
- Net pay: 13,333.33 − 933.33 − 866.67 = **€11,533.33**
- Employer CASS: 13,333.33 × 15.5% = **€2,066.67**
- Total employer cost: 13,333.33 + 2,066.67 = **€15,400.00**
- Reconciliation: 11,533.33 + 933.33 + 866.67 = 13,333.33 ✓

**Test 7: Article 99 period boundary, conditional arithmetic only.** Assume CASS has confirmed an eligible full-month employee case, aggregate salaried contribution base of €1,000, no other General Branch entitlement, no special-regime exemption, no incapacity, no benefits in kind and no partial month. This does not establish wage-law compliance or an actual person's eligibility.

| Month | Confirmed monthly threshold | Separate employee supplement at 10% |
| --- | --- | --- |
| June 2026 | €1,525.33 | (1,525.33 − 1,000.00) × 10% = **€52.53** |
| July 2026 | €1,568.67 | (1,568.67 − 1,000.00) × 10% = **€56.87** |

Use Sections 4.5 and 5. Do not carry the June threshold into July, add employer contributions to this separate charge or treat it as an automatic payslip deduction. Missing eligibility evidence requires confirmation before calculation.

## PROHIBITIONS

- Do not calculate without confirmed actual-period tax classification, applicable withholding rate/effective month and qualifying CASS base.
- Do not impose a blanket 7% IRPF cap, revive the retired salary bands or default an unknown employee to resident treatment.
- Do not omit standard employee/employer CASS or ignore the confirmed retirement-pension exception.
- Do not apply self-employed tiers as salaried caps or automatically uplift the employer base for the separate Article 99 supplement.
- Do not use an annual projection in place of actual period pay, or use the cash-only worksheet for unvalued benefits and reimbursements.
- Do not treat a joint declaration as proof that separate tax/contribution amounts were correctly paid, or use a blanket quarterly/20-day rule for CASS-covered payroll.
- Do not infer treaty relief, personal deductions, special-regime eligibility or minimum-wage compliance without the necessary evidence.
- Do not present this tier 2 draft or its calculations as professionally signed off.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a qualified Andorran assessor fiscal) before implementation.

This source-cited draft is maintained in the ryanduguid/openaccountants fork. Its editing date and selected-source checks do not establish complete actual-period verification or professional sign-off.

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
