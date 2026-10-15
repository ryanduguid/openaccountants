---
name: fi-income-tax
description: Use this draft for mainland Finland income tax questions about resident individuals, sole traders and freelancers for tax year 2025. Establish whether freelance receipts belong to business taxation or personal income taxation before applying business deductions. Covers the ordinary state scale, municipality and parish rates, capital income, work credit, basic deduction, insured health contributions and selected business deductions. Trigger on Finland income tax, Finnish tax return, Verohallinto, OmaVero, elinkeinotulo, pääomatulo, ansiotulo or ennakkovero. Unproved bases, elections, specialist rules, annual rounding and dependent totals remain held under the income-tax workflow base.
version: 1.3
jurisdiction: FI
tax_year: 2025
last_updated: 2026-10-16
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# FI Income Tax

This Tier 2 draft supplies selected mainland Finland rules for tax year 2025.
Version 1.3 corrects rates, deduction routes and component examples using the
period-specific sources below. It retains the earlier church-membership and
natural-person penalty corrections. A complete personal assessment still needs
the applicable law, deductions, credit allocation, annual rounding and taxpayer
records. Hold dependent amounts under the income-tax workflow base until these
are proved. This guide does not complete the base's country-companion contract.

Establish whether a freelancer's receipts are business income under EVL or
personal income under TVL. An occupation label does not establish eligibility
for business deductions. Åland has a separate municipal regime and a statutory
state-scale adjustment; use **ax-tax-scope** and period-specific Åland rules.
The Åland income guide's primary figures are for 2026 and cannot supply missing
2025 rules.

## Section 1 -- Quick Reference

**Section 1 -- Quick Reference**

| Field | Value |
| --- | --- |
| Country | Finland (Republic of Finland / Suomen tasavalta) |
| Tax | Income Tax (tulovero) |
| Currency | EUR only |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary legislation | Income Tax Act (tuloverolaki 1535/1992); Act on Tax Prepayments (ennakkoperintälaki 1118/1996) |
| Supporting legislation | Business Income Tax Act (laki elinkeinotulon verottamisesta 360/1968); annual state-scale, municipal/parish and health-contribution instruments cited below |
| Tax authority | Finnish Tax Administration (Verohallinto / Vero) |
| Filing portal | OmaVero (https://www.vero.fi/omavero) |
| Filing deadline | The cited 2025 business-return instructions give 1 April 2026. Establish the person's separate prefilled-return deadline from the authority record; do not extrapolate an annual calendar. |
| Validated by | Pending -- requires sign-off by a Finnish KHT/HT auditor or tax adviser |
| Validation date | Pending |
| Skill version | 1.3 |

### Earned Income -- State Tax Brackets (2025)

[Act 701/2024, section 1](https://www.finlex.fi/fi/lainsaadanto/2024/701)
fixes this ordinary scale for 2025 taxable earned income. The table is before
tax credits. It is not the adjusted Åland scale under Income Tax Act section 124(5).

| Taxable Earned Income (EUR) | Tax at Lower Limit | Rate on Excess |
| --- | --- | --- |
| 0 -- 21,200 | €0 | 12.64% |
| 21,200 -- 31,500 | €2,679.68 | 19.00% |
| 31,500 -- 52,100 | €4,636.68 | 30.25% |
| 52,100 -- 88,200 | €10,868.18 | 34.00% |
| 88,200 -- 150,000 | €23,142.18 | 41.75% |
| 150,000+ | €48,943.68 | 44.25% |

### Municipal Tax (kunnallisvero)

[The official 2025 schedule, 648/2024](https://www.finlex.fi/sv/lagstiftning/2024/648)
gives mainland municipal rates from **4.70% to 10.90%**. Helsinki is **5.30%**.
Select the taxpayer's applicable municipality and taxable earned-income base
after deductions. The schedule's 7.50% average is expressly for Act 627/1978
section 15(2); it is not a substitute for the taxpayer's rate.

### Church Tax (kirkollisvero)

The same [2025 schedule](https://www.finlex.fi/sv/lagstiftning/2024/648)
gives mainland municipality-linked Lutheran rates from **1.00% to 2.00%** and
Orthodox rates from **1.75% to 2.25%**. Helsinki's rates are **1.00% Lutheran**
and **1.80% Orthodox**. Special-parish notes require their own selection.

Establish the church, parish and legally effective membership at the end of
the preceding year before selecting a parish rate. [Act 1013/2012, section 1](https://www.finlex.fi/sv/lagstiftning/2012/1013)
provides the Lutheran membership test and municipal taxable-income base;
[Vero's general church-tax guidance](https://www.vero.fi/sv/skatteforvaltningen/nyhetsrummet/presentations_och_undervisningsmateria/kyrkoskat/)
uses the preceding-year-end test for Lutheran and Orthodox members. Special
parishes, foreign membership, estates and disputed effective dates need their
own checks. An unknown membership status does not establish zero church tax.

### Capital Income Tax (pääomatulovero)

**Capital Income Tax (pääomatulovero)**

[Income Tax Act, section 124(2)](https://www.finlex.fi/sv/lagstiftning/1992/1535)
sets the rates on taxable capital income. Classify receipts and apply their
taxable fractions, allowable costs and losses before using this table.

| Capital Income (EUR) | Rate |
| --- | --- |
| 0 -- 30,000 | 30% |
| 30,000+ | 34% |

### Health Insurance Contributions (2025)

[Act 694/2024, sections 1–4](https://www.finlex.fi/fi/lainsaadanto/saadoskokoelma/2024/694)
sets the 2025 rates. [Vero's historical guidance VH/1986/00.01.00/2024](https://www.vero.fi/syventavat-vero-ohjeet/ohje-hakusivu/338472/vakuutetun-sairausvakuutusmaksu/)
is expressly valid from 1 January to 31 December 2025. Do not import 2026 rates.

| Component | 2025 rate | Base and conditions |
| --- | --- | --- |
| Ordinary medical care | 1.06% | Generally municipal taxable earned income after the relevant deductions; the insured entrepreneur substitution below can change this base |
| Increased medical care | 1.45% combined | Qualifying income outside the daily-contribution base, including pension/benefit and age-related branches; Health Insurance Act chapter 18 section 20 supplies exceptions and the base comparison |
| Ordinary daily allowance | 0.84%, or zero below the threshold | Eligible wages plus confirmed YEL/MYEL income total at least EUR 16,862 annually; once reached, charge the entire eligible base |
| Additional YEL financing share | 0.20% | Confirmed YEL income only, including below the ordinary daily threshold; no equivalent MYEL supplement |

Confirm Finnish health-insurance coverage, date of birth, death-year status,
eligible wages, YEL/MYEL insurance and confirmed work income. Income-tax
residence alone does not establish coverage; Kela or, in relevant international
cases, ETK determines it. The death year has no insured contribution. EU or
treaty exclusions need their complete rules.

The daily-contribution age window starts on the first day of the month after
the 16th birthday and ends after the calendar month of the 68th birthday.
Medical care has no general age exemption. Being below the daily threshold
alone does not establish the increased medical rate. Sections 2.2.2 and 2.3.3
of the historical guidance state further exclusions, including specified
entrepreneur income; hold any unresolved increased-rate branch.

For insured entrepreneurs, confirmed YEL/MYEL work income replaces the specified
business-related earned receipts in the medical-care base. Add unrelated wages
and apply the relevant municipal-type deductions. Do not deduct YEL/MYEL
premiums in this substituted medical-care-base calculation. Without YEL/MYEL,
use the municipal taxable-income medical-care route; no confirmed entrepreneur
income supplies a daily base, but unrelated eligible wages can still do so.
Missing insurance does not excuse a separate compulsory-insurance obligation.

The daily contribution is deductible from net earned income; medical care is
not. Eligible residual tax credits can reduce medical care, but cannot reduce
the daily contribution. Keep their bases and credit allocation separate.

The historical guidance's table appears to reverse its final two headings.
Its section 3.2.3 and Act 694/2024 establish the **0.20% supplement** and the
**1.04% combined daily rate on YEL income** when the ordinary rate applies.
Do not apply that combined rate to unrelated wages or business profit.

### Self-Employed Business Income Split

[Income Tax Act sections 30, 30a, 38 and 41](https://www.finlex.fi/sv/lagstiftning/1992/1535)
require business tax adjustments and applicable prior losses before the **5%
entrepreneur deduction** and earned/capital allocation. The ordinary capital
share is up to a **20% annual return** on the prescribed business net assets
at the preceding calendar-year end; a start-up uses the tax-year-end assets.
Tax valuation is required, with **30% of qualifying withholding-subject wages
paid in the preceding 12 months** added to the allocation base.

A 10% request or an all-earned-income request must be made before assessment
ends. Section 38(2)'s compulsory capital treatment of qualifying fixed-asset
real-estate/securities gains still applies. Establish any request and the
valuation, accounting period, wage and gain facts before allocating income.
The complete asset-valuation chain, negative assets, period adjustments and
spouse allocation remain unverified here; hold dependent figures.

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown municipality | STOP -- municipal tax rate required |
| Unknown church membership | Needs Input; hold church tax and any dependent credit allocation or total until membership, parish and effective dates are established |
| Unknown capital-share request | Needs Input; establish the request record or its absence before using the ordinary 20% annual-return branch |
| Unknown business-use % (vehicle, phone, home) | Provisional zero deduction for the missing factual allocation; obtain evidence and keep the affected final position held |
| Unknown expense category or legal eligibility | Needs Input; hold the disputed deduction and dependent output |
| Unknown VAT registration or effective status | Needs Input; establish registration and the applicable VAT rule before selecting gross or net income/expense treatment |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** -- bank statement for the full tax year, municipality of residence, and confirmation of whether self-employed (elinkeinonharjoittaja) or freelancer (ammatinharjoittaja).

**Recommended** -- all sales invoices, purchase invoices/receipts, YEL pension insurance payment confirmations, prior year OmaVero tax decision, asset register for business.

**Ideal** -- complete bookkeeping (single-entry or double-entry), balance sheet if double-entry, prepayment tax (ennakkovero) payment confirmations, travel expense records.

For church tax, obtain the applicable church/parish, effective membership dates
and the relevant prefilled or authority record. Resolve conflicting information
before choosing a zero charge or parish rate.

Also obtain the EVL/TVL classification, accounting/tax adjustments, losses,
net-asset valuation and relevant wages, any capital-share request, insurance
coverage and confirmed work income. Separate premiums paid from confirmed YEL
income. Establish eligible work-credit income, net earned income, age at the
start of 2025 and qualifying child/guardian/spouse facts. These are required
when the corresponding calculation depends on them; the minimum document list
alone does not authorise a complete total.

### Refusal Catalogue

- **R-FI-1 -- Municipality unknown**: "The 2025 mainland municipal range is 4.70% to 10.90%. Establish the applicable municipality before computing municipal tax or a dependent total."
- **R-FI-2 -- Company or partnership** — "This skill covers sole traders (toiminimi) and freelancers (ammatinharjoittaja) only. Oy (osakeyhtiö), Ky (kommandiittiyhtiö), and Ay (avoin yhtiö) have different rules. Escalate to a Finnish tax adviser."
- **R-FI-3 -- Non-resident taxation** — "Non-resident and dual-resident taxation has separate rules (e.g., flat 35% withholding on employment income). Out of scope."
- **R-FI-4 -- International income / tax treaty** — "Cross-border income subject to Finland's extensive double tax treaty network requires specialist analysis. Escalate."
- **R-FI-CHURCH -- Membership or parish unresolved**: "I need the applicable church, parish and effective membership status at the end of the preceding year. Church tax and dependent credit allocations or totals remain held until these are established."

## Section 3 -- Deductions

### 3.1 Earned-income deductions and tax credits

[Act 702/2024, sections 106 and 125 and commencement](https://www.finlex.fi/fi/lainsaadanto/saadoskokoelma/2024/702)
first applies these figures for tax year 2025. Read unchanged conditions in
[Income Tax Act sections 96 and 125](https://www.finlex.fi/sv/lagstiftning/1992/1535)
and [Vero's 2025 calculation guidance](https://www.vero.fi/syventavat-vero-ohjeet/ohje-hakusivu/49038/verotettavan-tulon-laskeminen-henkiloverotuksessa8/).

| Item | 2025 treatment |
| --- | --- |
| Työtulovähennys, work-income tax credit | 18% of eligible work income, capped at the applicable maximum, then reduced using net earned income as described below; this reduces tax, not taxable income |
| Perusvähennys, basic income deduction | Up to EUR 4,115 in the mainland state and municipal earned-income bases, after preceding deductions; the Åland municipal deduction needs separate law |
| Compulsory YEL premiums paid | Choose the permitted business or personal own/spouse route, once only; this is distinct from confirmed YEL work income |

The ordinary work-credit maximum is **EUR 3,225**. Increase it by EUR 1,200
if the taxpayer had turned 65 before 2025 began. Add EUR 50 per qualifying
minor child for whom the taxpayer is guardian at year end. A qualifying minor
had not turned 17 before the tax year began. Double the child uplift only for
a child's sole guardian to whom the statutory spouse rules do not apply and
who has no spouse abroad. Establish those facts before claiming an uplift.

Reduce the capped credit by **2.22% of the net earned-income slice above
EUR 24,250 up to EUR 42,550**, and **3.44% of the slice above EUR 42,550**,
with a zero floor. Eligible work income and net earned income are different
inputs. Apply the credit first to state earned-income tax, then any excess to
municipal tax, church tax and medical care in their proportions, before other
income-tax credits. Never allocate it to daily contributions. Final allocation
precision and annual rounding remain unverified.

For the basic deduction, let B be non-negative net earned income after all
preceding deductions. If B is at most EUR 4,115, deduct B. Otherwise deduct
the larger of zero and EUR 4,115 less 18% of B's excess over EUR 4,115.
Consider all taxable earned income; capital income does not affect this deduction.

[Vero's YEL deduction guidance](https://www.vero.fi/yritykset-ja-yhteisot/verot-ja-maksut/liikkeen-tai-ammatinharjoittaja/vahennykset/yel-maksut/)
permits compulsory premiums in business taxation or personal earned-income
taxation of the taxpayer or spouse. The same insurance premiums cannot be
deducted in both routes. A personal/spouse claim is due before that assessment
ends; section 96 supplies the fallback if the requested spouse allocation
cannot be made. When premiums are booked as business costs but claimed
personally, make the corresponding non-deductible business adjustment.

### 3.2 Business Deductions (Self-Employed)

[Business Income Tax Act sections 7–8, 17, 22–24, 30–34 and 54–55](https://www.finlex.fi/fi/lainsaadanto/1968/360)
govern the selected EVL rules below. Prove the business purpose, private-use
allocation and income-source classification. Deductibility does not establish
immediate expensing: ordinary accrual timing, time-based costs, capitalisation
and any permitted accounting method need their own checks. A bank payment or
category label alone does not establish the deduction.

| Category | Treatment |
| --- | --- |
| Business premises rent | Business portion, with the applicable period allocation |
| Home workroom | 2025 standard amounts EUR 980, EUR 490 or EUR 245 under the use tests below; evidenced actual-cost route is separate |
| Literature, tools, telephone/internet, professional fees and bank charges | Establish income-earning purpose, private portion and expense/capital timing; the label alone does not prove eligibility |
| Business travel | Evidenced travel/accommodation costs and qualifying increased living costs; EVL 55 permits the additional deduction described below |
| Private-car business travel | 2025 basic benchmark EUR 0.59/km under EVL 55 eligibility, less relevant costs already deducted; not a payment to oneself |
| Training, memberships and legal costs | Needs Input for the relevant category rules; do not infer all courses, subscriptions or legal payments are deductible |
| Ordinary advertising | Establish the advertising classification and applicable timing under EVL 8 |
| Trade-receivable impairment | EVL 17 distinguishes trade impairment from definitively established losses on other financing receivables; prove type, prior recognition, impairment and timing |
| Representation | 50% of qualifying representation expenditure; establish the boundary with advertising and private costs |
| Ordinary movable depreciation | Pool qualifying machinery/equipment/comparable movables; up to 25% of the reducing tax balance, subject to bookkeeping limits |
| Buildings | Reducing unrelieved acquisition cost: generally 7% for the statutory shop/warehouse/factory/workshop categories and 4% for residences/offices; other categories need their own rules |

**Workroom.** [Vero's 2025 harmonisation guidance, section 2.1](https://www.vero.fi/syventavat-vero-ohjeet/ohje-hakusivu/48275/verohallinnon-yhtenaistamisohjeet-vuodelta-2025-toimitettavaa-verotusta-varten/)
allows EUR 980 for continuous full-time home income use or full-time remote
work on over 50% of annual working days; EUR 490 for continuous part-time use
or regular remote work on at most 50%; EUR 245 for the remaining occasional
income-use/remote-work cases. Assess each taxpayer separately. Combined standard
workroom deductions across income sources cannot exceed EUR 980 without proof
of higher actual costs. Actual costs require reliable evidence, allocation
between income sources and no duplicate deduction. Primary/secondary workplace
labels or floor area alone do not establish these conditions.

**Travel.** [Vero's business-travel guidance VH/721/00.01.00/2025](https://www.vero.fi/syventavat-vero-ohjeet/ohje-hakusivu/48192/liikkeen-ja-ammatinharjoittajien-seka-maataloudenharjoittajien-matkakustannusten-vahentaminen/)
explains EVL 55's additional deduction. For qualifying increased living costs,
use the positive difference between the applicable daily maximum and such
costs already deducted. Actual higher qualifying costs remain deductible
without another top-up. Travel and accommodation costs are separate from
these living-cost amounts. Claim the additional deduction on the tax return;
only actual costs belong in the books.

The [2025 travel decision, sections 11–12](https://www.vero.fi/syventavat-vero-ohjeet/paatokset/47405/verohallinnon-paatos-verovapaista-matkakustannusten-korvauksista-vuonna-2025/)
sets domestic benchmarks of **EUR 24 for over 6 hours** and **EUR 53 for over
10 hours**. Temporary business travel must leave the customary activity area,
reach over 15 km from its origin home/permanent business site, and have the
workplace over 5 km from both. Keep purpose, places, distances and start/end
times. One qualifying free/included meal halves the partial-day maximum;
two halve the full-day maximum. Multiple days, return-day extensions, foreign
travel and special cases need the complete decision. The displayed decision
is an old version; its domestic amounts agree with the 2025 business guidance,
but the complete version history was not certified.

For the **EUR 0.59/km** basic private-car benchmark, establish qualifying
ownership, at least 50% non-business use in the tax year, total and business
kilometres, and a driving log or reliable equivalent. Deduct costs already
claimed when calculating the additional amount; actual higher costs receive
no further top-up. The kilometre branch has no per-diem duration/distance test.
A business-asset car uses actual business costs and depreciation with private-use
adjustment, without this additional deduction. Unknown total kilometres do
not establish private-asset status. Special ownership, driver, estimate and
rate-uplift branches need their own proof.

**Assets.** EVL 33 permits requested immediate expensing of qualifying assets
with useful life at most 3 years, or small acquisitions costing at most
EUR 1,200 each with a EUR 3,600 annual small-acquisition limit. Treat an integrated
asset group as one acquisition. EVL 30 also permits writing off a remaining
pool at most EUR 1,200. Depreciation is limited by EVL 54's bookkeeping condition.
The temporary higher-depreciation amendment [1314/2022](https://www.finlex.fi/fi/lainsaadanto/saadoskokoelma/2022/1314)
extends a qualifying new-asset maximum of 50% through tax year 2025. The full
unchanged conditions of Act 1572/2019 were not obtained; hold that branch
until its eligibility, accounting and reporting requirements are verified.

### 3.3 Non-Deductible Expenses

**3.3 Non-Deductible Expenses**

| Expense | Reason |
| --- | --- |
| Personal living costs | Not business-related |
| Fines and penalties | Public policy |
| Income tax itself | Tax on income |
| Home to permanent business workplace | Private travel outside EVL business expenses; the sole trader may qualify for the separate personal TVL 93 commuting deduction |
| Clothing (unless protective/uniform) | Personal |
| Donations | No blanket business deduction; the limited qualifying business gift and separate personal donation routes below require their conditions |

[Vero's travel guidance, section 2.1](https://www.vero.fi/syventavat-vero-ohjeet/ohje-hakusivu/48192/liikkeen-ja-ammatinharjoittajien-seka-maataloudenharjoittajien-matkakustannusten-vahentaminen/)
places home-to-permanent-business-workplace travel on the prefilled personal
return under TVL 93. This route is not employee-only. It uses the cheapest
permitted method, own-risk amount, cap and other conditions. The [2025 commuting
valuation decision](https://www.vero.fi/sv/Detaljerade_skatteanvisningar/beslut/47204/)
gives EUR 0.27/km for an owned/held car only where the relevant own-car
commuting conditions are proved. It is distinct from the EVL 55 benchmark.

[Vero's 2025 harmonisation guidance, section 3.2](https://www.vero.fi/syventavat-vero-ohjeet/ohje-hakusivu/48275/verohallinnon-yhtenaistamisohjeet-vuodelta-2025-toimitettavaa-verotusta-varten/)
recognises small cash or in-kind gifts for public-benefit purposes connected
with the locality or business sector as relationship expenses, up to EUR 850
per recipient. Political gifts do not qualify. [TVL 98a](https://www.finlex.fi/sv/lagstiftning/1992/1535)
separately permits a personal net-earned-income deduction for qualifying
monetary science/art donations of EUR 850 to EUR 500,000 to publicly funded EEA
universities/higher-education institutions or linked university funds. Establish
the recipient, purpose, amount and route; do not merge these two rules.

## Section 4 -- Hypothetical component positions

These synthetic positions test selected 2025 components. They do not establish
a complete personal assessment, annual rounding or a settlement balance.

### Position 1 -- Helsinki trader with incomplete assessment inputs

Revenue EUR 65,000 less evidenced business expenses EUR 12,000 leaves
EUR 53,000 before any unprovided tax adjustments, losses or entrepreneur
deduction. Helsinki's municipal rate is 5.30%; confirmed ordinary Lutheran
membership would select its 1.00% parish rate. Net assets, wage addition,
capital-share request, YEL coverage/work income, deductions and credits are
unresolved. Business allocation, health contributions and total tax remain
Needs Input. Do not reproduce the former approximate total.

### Position 2 -- Ordinary work credit across both phase-out slices

Eligible work income and net earned income are each EUR 50,000. The taxpayer
was under 65 at the start of 2025 and has no qualifying children. The ordinary
cap applies. The lower phase-out slice is EUR 18,300; its reduction is
EUR 406.26. The upper slice is EUR 7,450; its reduction is EUR 256.28.
The component credit is EUR 2,562.46 before liability limits and allocation.

### Position 3 -- Basic deduction after earlier deductions

B is EUR 10,000 after all preceding deductions. The excess is EUR 5,885,
whose 18% reduction is EUR 1,059.30. The basic deduction is EUR 3,055.70
and the resulting base is EUR 6,944.30. This isolates one deduction; it does
not supply missing earlier deductions or the taxpayer's credit calculation.

### Position 4 -- YEL below the ordinary daily threshold

A covered 40-year-old has confirmed YEL work income EUR 11,000 and no other
daily-base income. The ordinary daily component is zero; the 0.20% YEL
supplement is EUR 22. Medical care needs its separately derived base and
deductions. Neither zero ordinary daily contribution nor EUR 22 is total health tax.

### Position 5 -- YEL and unrelated wages

A covered 40-year-old has confirmed YEL income EUR 20,000 and eligible
unrelated wages EUR 5,000. The combined daily base is EUR 25,000. Its 0.84%
ordinary component is EUR 210; the YEL-only 0.20% supplement is EUR 40.
The daily total is EUR 250. Medical care and the personal assessment remain
separate. Replacing YEL with MYEL removes this YEL-only supplement.

### Position 6 -- Taxable capital income after classification

Established taxable capital income is EUR 45,000 after the relevant taxable
fractions, costs, losses and other adjustments. The first EUR 30,000 gives
EUR 9,000 at 30%; the remaining EUR 15,000 gives EUR 5,100 at 34%.
The capital-tax component is EUR 14,100 before any applicable tax credits.
EUR 45,000 of gross dividends, rent and interest does not establish this input.

### Position 7 -- Additional travel deductions without double counting

An eligible EVL sole trader has a proved private-asset car and 100 business
kilometres. The basic benchmark is EUR 59. With EUR 25 of relevant actual costs
already deducted, the additional car deduction is EUR 34. A separate qualifying
11-hour domestic temporary trip meets all distance, purpose, evidence and
increased-living-cost conditions and includes no qualifying free meals. Its
EUR 53 maximum less EUR 20 of living costs already deducted leaves EUR 33
additional deduction. Keep travel/accommodation expenses separate. Neither
amount is a tax-free per-diem or kilometre payment to oneself.

## Section 5 -- Filing and Payment

### 5.1 Filing

**5.1 Filing**

| Item | Detail |
| --- | --- |
| 2025 business-return deadline | 1 April 2026 in [Vero's sole-trader return instructions](https://www.vero.fi/yritykset-ja-yhteisot/verot-ja-maksut/liikkeen-tai-ammatinharjoittaja/veroilmoituksen-t%C3%A4ytt%C3%B6ohje/); confirm any valid extension or case-specific notice |
| Personal prefilled-return deadline | Establish the assigned date from the person's authority record; this pass does not certify every 2026 calendar branch |
| Portal | OmaVero (omavero.fi) |
| Pre-populated return | Verohallinto pre-fills income from employers, banks, pension companies |
| Business return and attachments | Use the cited tax-2025 Form 5 instructions; determine attachments from the accounting method and facts |
| Record retention | Needs verification by record class, applicable law and starting date; no blanket six-year instruction is established here |

### 5.2 Prepayment Tax (Ennakkovero)

Self-employed persons must pay prepayment tax during the tax year. See the **fi-prepayments** skill for full details.

- Based on estimated income or prior year assessment
- The ordinary schedule has 2, 3, 6 or 12 instalments according to the assessed advance; see the source-linked bands in **fi-prepayments**
- Adjustable during the year through OmaVero
- Residual tax (jäännösvero) due if prepayments insufficient

### 5.3 Penalties

[Assessment Procedure Act 1558/1995, sections 32–33](https://www.finlex.fi/sv/lagstiftning/1995/1558),
introduced by [15/2018](https://www.finlex.fi/sv/lagstiftning/forfattningssamling/2018/15)
from tax year 2018, distinguishes a natural person's EUR 50 annual late-filing
fee from a tax increase. An individual sole trader uses this branch. A complete
required main return filed late before assessment ends comes within the fee
branch even after a request. A correction of an existing or deemed prefilled
return uses that substitution only on the taxpayer's own initiative before
completion. Separate errors can still attract an increase. The fee is once
per tax year, not EUR 50 plus a percentage of tax.

First establish the disclosure failure and any non-imposition ground. The
statute addresses minor failures, valid reasons and the applicable
unreasonableness test; the fee has additional outside-control and special-reason
grounds. A missing taxpayer-favourable item normally attracts neither charge,
subject to the repeated-failure/clear-indifference exception. That does not
excuse an entirely late required return or an unfounded deduction.

| Qualifying increase branch | Percentage of added income | Percentage of increased tax where section 32b applies |
|---|---|---|
| Ordinary | 2% | 10% |
| Repeated failure or clear indifference | 3% to 10% | 15% to 50% |
| Estimated assessment | 5% | 25% |
| Statutory interpretive uncertainty or qualifying unreasonableness | 1% | 5% |
| Foreign income satisfying section 32a(5), excluding the aggravated branch | 1% | 5% |
| Own-initiative correction after completion with the explanation duty fulfilled | 0.5% | 2% |

Added income is the primary base, including a qualifying reduction of an
assessed loss. Increased tax is the alternative base when the income base
cannot be used or income was placed in the wrong category. The natural-person
minimum is EUR 75 when an increase is imposed, after non-imposition grounds
have been considered. Do not apply an income percentage to additional tax or
classify a failure from an informal label such as 'negligent' alone.

[Vero's guidance dated 20 May 2026](https://www.vero.fi/sv/Detaljerade_skatteanvisningar/anvisningar/66816/pofoljdsavgifter-for-inkomstbeskattningen/)
contains apparent wording conflicts in sections 3.2.5 and 3.2.12: the former
uses added-income wording for the 15% to 50% increased-tax branch; the latter
states a EUR 150 minimum without qualifying the taxpayer category. Sections
32a–32b and the guidance's section 3.2.9 support the natural-person base and
EUR 75 minimum above. The 2026 guidance is interpretive material, not a change
of this guide's 2025 tax year. Disputed facts, special formal failures, foreign
credits, criminal-process safeguards and remedies need their complete rules.

Payment interest is separate. Use **fi-prepayments** for reduced settlement
interest and interest starting the day after an overdue amount's due date;
an honest shortfall in advances alone does not establish a disclosure penalty.

## Section 6 -- Interaction with Other Finnish Taxes

**Section 6 -- Interaction with Other Finnish Taxes**

| Tax | Interaction |
| --- | --- |
| VAT (ALV) | Separate system; see Finland VAT skill if applicable. VAT collected is not income; input VAT recovered is not expense. |
| YEL pension insurance | Establish the insurance obligation separately. Compulsory premiums permit the business or own/spouse personal deduction route, once only; see **fi-yel-social**. Confirmed work income supplies separate contribution bases. |
| Prepayment tax (ennakkovero) | Not an expense; credit against final liability. See **fi-prepayments** skill. |

## Section 7 -- Reference Material

### Key Legislation

**Key Legislation**

| Topic | Reference |
| --- | --- |
| Income tax rates | Income Tax Act (tuloverolaki) 1535/1992 |
| Business income | Business Income Tax Act (EVL) 360/1968 |
| Capital income split | Income Tax Act §38 |
| Deductions | Income Tax Act §29-§31, §93-§95; EVL §7-§18 |
| Prepayments | Prepayment Act (ennakkoperintälaki) 1118/1996 |
| Filing deadlines | Verohallinto annual announcement |

### Key Verohallinto Resources

**Key Verohallinto Resources**

| Resource | URL |
| --- | --- |
| OmaVero portal | https://www.vero.fi/omavero |
| Self-employed guide | https://www.vero.fi/en/businesses-and-corporations/about-corporate-taxes/sole-traders/ |
| Tax rates on pay | https://www.vero.fi/en/individuals/tax-cards-and-tax-returns/income/earned-income/tax-rates-on-pay-pensions-and-benefits/ |
| Per diem rates | https://www.vero.fi/en/individuals/tax-cards-and-tax-returns/income/earned-income/work-related-travel/ |

## Prohibitions

- NEVER compute total tax without knowing the client's municipality of residence
- NEVER ignore the earned income / capital income split for self-employed
- Establish EVL or TVL classification before using business deductions; assess personal commuting under its own rules
- Never deduct the same YEL insurance premiums in both business/agriculture and personal taxation
- NEVER treat prepayment tax (ennakkovero) as an expense -- it is a credit against final tax
- NEVER present calculations as definitive -- always label as estimated
- NEVER advise on non-resident, dual-resident, or cross-border tax situations

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
