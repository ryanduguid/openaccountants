---
name: bi-income-tax
description: "Source-cited draft: personal income tax for Burundi, tax year 2026-27. The progressive 0/20/30 scale applies to employment and rental income only; business income of a natural person is taxed at a flat 30% subject to a 1% minimum tax on turnover, and for 2026/2027 natural persons with turnover up to BIF 25,000,000 instead file quarterly at a flat 1% of quarterly turnover. Covers the annual bands, the non-resident scale, the minimum tax and the free-zone exception. Trigger on \"Burundi income tax\", \"impot sur les revenus Burundi\", \"OBR PAYE\", \"Burundi tax bands\", \"impot minimal Burundi\". Read from OBR-published law; unverified, pending local-accountant review."
jurisdiction: BI
category: international
tax_year: 2026
tax_year_notes: "The scale in §1 is article 21 of loi n° 1/02 du 24 janvier 2013 as amended by loi n° 1/14 du 24 décembre 2020. The small-trader regime in §2 is article 190 of the Loi de Finances 2026/2027 (loi n° 1/10 du 30 juin 2026), expressed to apply 'au titre de la gestion budgétaire 2026/2027' — it is year-specific and must be re-checked against each Finance Act. Burundi's budget year runs 1 July to 30 June."
last_updated: 2026-09-10
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Burundi Personal Income Tax

> **The bands were right and what they apply to was wrong.** The previous version
> said Burundi "applies a progressive scale to individual income (**employment,
> business and rental income**)". Article 21 applies the scale to **employment and
> rental income**. A natural person's **business income is taxed at a flat 30%** —
> and for 2026/2027, a natural person with turnover up to **BIF 25,000,000** is
> outside both, filing **quarterly at 1% of turnover**.
>
> The previous version also carried an explicit warning that none of its figures
> had been put in front of a primary source, because `obr.bi` answered with a fatal
> PHP error. **That warning can now be retired**: the OBR site returns normally in
> a browser, and its legislation register carries the income tax law, its 2020
> amendment and the current Finance Act. The bands it stated are confirmed.

## 1. The scale — article 21, and it is annual

For **residents**, taxable income falling within **employment income and rental
income** is rounded to the nearest thousand Burundian francs and taxed in bands:

| Annual net taxable income (BIF) | Rate |
| --- | --- |
| 0 – 1,800,000 | **0%** |
| 1,800,001 – 3,600,000 | **20% of the part exceeding 1,800,000** |
| 3,600,001 and above | **30% of the part exceeding 3,600,000** |

_(Loi n° 1/02 du 24 janvier 2013 relative aux impôts sur les revenus, art. 21, as amended by loi n° 1/14 du 24 décembre 2020 — https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf)_

- **The statute states these annually; the previous version stated them monthly** —
  BIF 1,800,000 and 3,600,000 a year are BIF 150,000 and 300,000 a month, so the
  monthly figures the guide gave were arithmetically right. They were presented as
  the rule, though, where they are a **derivation from it**, and the derivation only
  holds for someone paid evenly across twelve months  _(art. 21 — https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf)_
- **Rounding is part of the rule** — taxable income is rounded to the **nearest
  thousand BIF** before the bands are applied  _(art. 21 — https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf)_
- **These are marginal bands, not slab rates** — the statute says *"20% de la part
  qui dépasse 1.800.000"* and *"30% de la part qui dépasse 3.600.000"*. Only the
  excess over each threshold is taxed at the higher rate  _(art. 21 — https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf)_
- **Non-residents use the same scale, on a narrower base** — the same *barème*
  applies to non-residents for first-schedule income, but **only two categories
  count**: Burundi-source employment income within arts. 6 and 7, and **rental
  income**. The previous version said nothing about non-residents  _(art. 21 — https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf)_

## 2. Business income of a natural person is not on that scale

- **Flat 30%** — *"les personnes physiques exerçant des activités d'affaires sont
  imposées au taux unique de trente pour cent (30%)"*. The progressive scale does not
  reach business income  _(art. 21 — https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf)_
- **A 1% minimum tax on turnover applies whatever the result** — any natural person
  carrying on business in Burundi, **whether of Burundian or foreign law**, is subject
  to the minimum tax *"quels qu'en soient ses résultats"*, **including beneficiaries
  of the investment code**  _(art. 21 — https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf)_
- **Free-zone businesses are excepted for ten years** — the exception is for *"les
  bénéficiaires des avantages de la zone franche pendant les dix (10) premières
  années de son existence"*  _(art. 21 — https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf)_
- **The minimum tax has a precise trigger** — it is **1% of turnover**, and it bites
  when net taxable income is **less than turnover divided by 30**. The two figures fit
  together exactly: at a 30% rate, tax on turnover ÷ 30 is 30% × turnover ÷ 30 = **1%
  of turnover**, so the minimum tax is the tax that would be due at precisely the
  trigger point, and above that point the ordinary computation always gives more  _(art. 21 — https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf)_

### The small-trader regime for 2026/2027

Article 190 of the Finance Act displaces the above for smaller traders, **by express
derogation from art. 41 of the 2020 amending law**:

| Natural person's annual turnover | Obligation for 2026/2027 |
| --- | --- |
| **Up to BIF 25,000,000** | **Quarterly** return; tax at a **single rate of 1% of quarterly turnover** |
| **Above BIF 25,000,000** | **Annual** income tax return, and the taxpayer is **directly obliged to keep simplified or full accounts** as the case requires |

_(Loi de Finances 2026/2027 (loi n° 1/10 du 30 juin 2026), art. 190 — https://www.obr.bi/images/LOI_DE_FINANCES_2026-2027_PROMULGUEE_compressed.pdf)_

- **BIF 25,000,000 is the same figure that triggers compulsory VAT registration** for
  2026/2027, so a natural person crossing it moves from quarterly 1%-of-turnover
  filing to annual filing with books **and** into the VAT net at the same time. See
  `bi-vat-gst`  _(Loi de Finances 2026/2027, arts. 190 and 271 — https://www.obr.bi/images/LOI_DE_FINANCES_2026-2027_PROMULGUEE_compressed.pdf)_

## 3. What this replaces

| The previous version said | The law says |
| --- | --- |
| "a progressive scale to individual income (employment, **business** and rental income)" | The scale reaches **employment and rental income**. Business income of a natural person is a **flat 30%** — art. 21 |
| Monthly bands: 0% to 150,000; 20% to 300,000; 30% above | **Arithmetically right, structurally derived.** The statute sets **annual** bands at 1,800,000 and 3,600,000, and rounds income to the nearest thousand BIF first |
| Bands stated without saying whether they are marginal | *"20% de la part qui dépasse 1.800.000"* — **marginal** |
| *nothing* | The **same scale applies to non-residents**, but only on Burundi-source employment income and rental income |
| *nothing* | A **1% minimum tax on turnover** for natural persons in business, applying whatever the result and even to investment-code beneficiaries, with a **ten-year free-zone exception** |
| *nothing* | For 2026/2027, natural persons with turnover **up to BIF 25,000,000** file **quarterly at 1% of turnover**; above it, **annually, with books** — Finance Act art. 190 |
| An explicit warning that no figure had been checked against a primary source, because `obr.bi` served a fatal PHP error | **The site works in a browser.** Every figure above is cited to the law or the Finance Act as published by the OBR |

> **How these documents were read.** The OBR publishes its legislation as **scanned
> images with no text layer**, so the text here was recovered by OCR. **OCR output
> is not the same evidential quality as a text layer.** Every figure above was
> accepted only where the statute states it in **words and digits together** —
> *"trente pour cent (30%)"*, *"vingt-cinq millions de francs burundais (25 000 000
> BIF)"* — and the minimum-tax arithmetic in §2 provides an independent check on
> both the 30% and the 1%. Article 190 was re-read at higher resolution because the
> first pass dropped the line naming its subject; without that re-read the regime
> would have been described without knowing it applies to **natural persons**. A
> reviewer with the paper text should confirm every number regardless.

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
