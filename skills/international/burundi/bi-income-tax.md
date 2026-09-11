---
name: bi-income-tax
description: "Source-cited draft covering Burundi personal income tax and the small-trader rules for budget year 2026/2027. Explains the annual employment and rental-income bands, monthly payroll provisions, non-resident treatment, the 30% business-income rate, the 1% minimum tax and individual capital income. Covers quarterly turnover taxation for qualifying natural persons and explains why VAT registration needs a separate test. Use for questions about Burundi income tax, OBR PAYE, personal tax bands, rental income, minimum tax or small-trader returns. The cited OBR laws were checked as scanned documents. Pending local-accountant review."
jurisdiction: BI
category: international
tax_year: 2026
tax_year_notes: "The scale in §1 is article 21 of loi n° 1/02 du 24 janvier 2013 as amended by loi n° 1/14 du 24 décembre 2020. The small-trader regime in §2 is article 190 of the Loi de Finances 2026/2027 (loi n° 1/10 du 30 juin 2026), expressed to apply 'au titre de la gestion budgétaire 2026/2027': it is year-specific and must be re-checked against each Finance Act. Burundi's budget year runs 1 July to 30 June."
version: 0.3
last_updated: 2026-09-11
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Burundi Personal Income Tax

## 1. The scale: article 21, and it is annual

For **residents**, taxable income falling within **employment income and rental
income** is rounded to the nearest thousand Burundian francs and taxed in bands:

| Annual net taxable income (BIF) | Rate |
| --- | --- |
| 0 – 1,800,000 | **0%** |
| 1,800,001 – 3,600,000 | **20% of the part exceeding 1,800,000** |
| 3,600,001 and above | **BIF 360,000 plus 30% of the part exceeding 3,600,000** |

_(Loi n° 1/02 du 24 janvier 2013 relative aux impôts sur les revenus, art. 21, as amended by loi n° 1/14 du 24 décembre 2020: https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf)_

- **Monthly payroll withholding** has its own statutory scale in article 117:
  0% up to BIF 150,000; 20% on the next BIF 150,000; and 30% above BIF 300,000.
  It includes exceptional payments. Articles 118 and 119 set separate rules for
  non-principal and occasional employers. See `bi-payroll-social`.
  [Income tax law, arts. 117–119](https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf).
- **Rounding is part of the rule**: taxable income is rounded to the **nearest
  thousand BIF** before the bands are applied  _(art. 21: https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf)_
- **These are marginal bands, not slab rates**: the statute says *"20% de la part
  qui dépasse 1.800.000"* and *"30% de la part qui dépasse 3.600.000"*. Only the
  excess over each threshold is taxed at the higher rate  _(art. 21: https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf)_
- **The BIF 360,000 in the table is computed, not quoted.** The statute's own cell
  reads only *"30% de la part qui dépasse 3.600.000"*. The table above states the
  **total tax due**, so it carries forward the second band's tax — 20% × (3,600,000
  − 1,800,000) = **BIF 360,000** — which the statutory cell leaves implicit. Read
  the cells as rates for their own band and you must add it yourself  _(art. 21: https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf)_
- **Non-residents use the same scale, on a narrower base**: the same *barème*
  applies to non-residents for first-schedule income, but **only two categories
  count**: Burundi-source employment income within arts. 6 and 7, and **rental
  income**  _(art. 21: https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf)_
- **Final withholding is income-specific.** Under article 22, withholding under articles 119 and 120 is final for a non-resident's Burundi-source income that is not attributable to a permanent establishment in Burundi. Article 22 preserves articles 119–121 against article 21(2). Ordinary employment and rental income still follow the applicable rules in article 21; a person's lack of a permanent establishment does not remove those categories from the scale. Check the income type and withholding provision before treating tax as final. [Income tax law, arts. 21–22](https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf).

## 2. Business income of a natural person is not on that scale

- **Flat 30%**: *"les personnes physiques exerçant des activités d'affaires sont
  imposées au taux unique de trente pour cent (30%)"*. The progressive scale does not
  reach business income  _(art. 21: https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf)_
- **A 1% minimum tax on turnover applies whatever the result**: any natural person
  carrying on business in Burundi, **whether of Burundian or foreign law**, is subject
  to the minimum tax *"quels qu'en soient ses résultats"*, **including beneficiaries
  of the investment code**  _(art. 21: https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf)_
- **Free-zone businesses are excepted for ten years**: the exception is for *"les
  bénéficiaires des avantages de la zone franche pendant les dix (10) premières
  années de son existence"*  _(art. 21: https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf)_
- **The minimum tax has a precise trigger**: it is **1% of turnover**, and it bites
  when net taxable income is **less than turnover divided by 30**. The two figures fit
  together exactly: at a 30% rate, tax on turnover ÷ 30 is 30% × turnover ÷ 30 = **1%
  of turnover**, so the minimum tax is the tax that would be due at precisely the
  trigger point, and above that point the ordinary computation always gives more  _(art. 21: https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf)_

### The small-trader regime for 2026/2027

Article 190 of the Finance Act displaces the above for smaller traders, **by express
derogation from art. 41 of the 2020 amending law**:

| Natural person's annual turnover | Obligation for 2026/2027 |
| --- | --- |
| **Up to BIF 25,000,000** | **Quarterly** return; tax at a **single rate of 1% of quarterly turnover** |
| **Above BIF 25,000,000** | **Annual** income tax return, and the taxpayer is **directly obliged to keep simplified or full accounts** as the case requires |

_(Loi de Finances 2026/2027 (loi n° 1/10 du 30 juin 2026), art. 190: https://www.obr.bi/images/LOI_DE_FINANCES_2026-2027_PROMULGUEE_compressed.pdf)_

- **VAT registration is a separate test.** At exactly BIF 25,000,000 a natural
  person may remain in the quarterly income-tax regime while reaching the VAT
  threshold. VAT tests taxable turnover and also has independent purchases,
  imports and stock tests. See `bi-vat-gst`.
  [Finance Act 2026/2027, arts. 190 and 271](https://www.obr.bi/images/LOI_DE_FINANCES_2026-2027_PROMULGUEE_compressed.pdf).

## 3. Filing

- **Annual deadline:** where an annual individual return is required, article 24 sets the deadline at the last day of the third month after the accounting year closes. Apply the small-trader rules in Section 2 where relevant. [Income tax law, art. 24](https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf).
- **Exemption for income already withheld:** article 25 exempts a person receiving only employment income withheld under article 113, income withheld under articles 119 and 120, or both categories. Article 26 permits an exempt person to file voluntarily, including to claim an overpayment. A person with only correctly withheld salary therefore does not have a mandatory annual return under article 24. Other income requires a separate filing assessment. [Income tax law, arts. 25–26](https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf).
- **Employer annual recapitulative:** article 24 excludes this employer filing from the individual deadline. Article 115 requires it within 30 days after the accounting year ends. See `bi-payroll-social`. [Income tax law, arts. 24 and 115](https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf).
- **Employee monthly filing:** where the employer is not obliged to withhold, article 116 requires the employee to file and pay by the 15th of the month following payment. [Income tax law, art. 116](https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf).

- **Employment income tax is a monthly obligation, not an annual one.** The closing
  paragraphs of article 24 provide that for employment income the declaration and
  payment are made *"par période imposable qui est … fixée à un mois"*, without
  prejudice to the article 115 annual recapitulative, with the deadline *"au
  quinzième jour du mois qui suit celui de la réalisation du revenu d'emploi"* —
  the **15th of the month following** the month the income arose. [Income tax law, art. 24](https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf).
- **Use the 2026/2027 filing rule before the older threshold.** Article 24 of the
  2020 law mentions quarterly declarations and payments for natural persons with
  turnover up to BIF 100,000,000. Finance Act 2026/2027 article 190 expressly
  requires an annual income-tax return above BIF 25,000,000. A taxpayer between
  those amounts must therefore retain the annual-return obligation in Section 2.
  The cited texts do not establish here whether additional quarterly declarations
  remain due. Confirm that interaction with OBR before preparing a filing calendar;
  article 126 provisional instalments are a separate question.
  [Finance Act, art. 190](https://www.obr.bi/images/LOI_DE_FINANCES_2026-2027_PROMULGUEE_compressed.pdf);
  [Income tax law, arts. 24 and 126](https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf).
- **Medium and large taxpayers need their return certified.** Article 27 requires
  natural persons with business income taxed under article 21(1) to file an annual
  return, and provides that those classed as **medium and large taxpayers** must
  have the declaration **and each annex** certified by a professional approved by
  the **Ordre des Professionnels Comptables**. [Income tax law, art. 27](https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf).
- **What the annual liability is reduced by.** Article 28 computes the tax on the
  annual return and then deducts withholding under **articles 112 to 116**,
  withholding under **articles 119 and 120**, and the **quarterly provisional
  instalments** made during the year under article 126. [Income tax law, art. 28](https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf).

### Worked scope checks

- A non-resident employee without a business establishment receives ordinary Burundi-source salary from their principal employer. The employer applies article 117's monthly employment scale; the absence of an establishment does not make this salary an article 119 or 120 payment.
- A person receives only salary correctly withheld under article 113. Article 25 exempts the annual individual return; article 26 still allows a voluntary return to seek a refund.
- A non-resident receives income withheld under article 119 or 120 that is not attributable to a Burundi permanent establishment. Article 22 makes that withholding final. Check article 25 against the person's other income before concluding that no annual return is required.

[Income tax law, arts. 21–26 and 117–120](https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf).

## Sources and review limits

Article 23 taxes individual capital income and capital gains at 15%, including
the asset-sale proceeds specified in article 37(2). This provision belongs to
the individual-income chapter. [Income tax law, art. 23](https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf).

The OBR sources are scans. Articles 21, 24 to 28, 117 and Finance Act article 190 were checked against the
page images at 300 dpi rather than the OCR layer. Local-accountant review is pending.

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
