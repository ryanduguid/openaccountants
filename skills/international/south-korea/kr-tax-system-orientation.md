---
name: kr-tax-system-orientation
description: >
  South Korea's ordinary 2025 tax system, covering income scope, individual and corporate residence, taxpayer type, currency, tax years and national and local return routing. Trigger on Korean tax residence, income source or annual return routing.
jurisdiction: KR
category: international
tax_year: 2025
tax_year_notes: "Ordinary 2025 income tax and the related 2026 filing season. Check the applicable law for later years."
tier: 2
review_status: pending_review
last_updated: 2026-11-28
version: 1.0
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
depends_on:
  - workflow-base
---

# South Korea tax system orientation

Load `workflow-base`. Identify the taxpayer, income category, source and tax period before applying a rate or choosing a return. Use the rules for the Republic of Korea and confirm any treaty or special regime separately.

## Individuals

For 2025, an individual is resident if domiciled in Korea or if they have a place of abode there for at least 183 days under the domestic rules. Apply the Enforcement Decree to determine domicile, count the period of abode and establish when residence starts or ends. Residents are generally taxed on their worldwide income within the Act. For a foreign resident whose combined period of Korean domicile or abode was 5 years or less in the 10 years ending at the close of the tax period, include foreign-source income only to the extent paid in or remitted to Korea. Non-residents are taxed on income from Korean sources specified in the Act. Establish treaty residence, the source of each item and actual payments separately. [Income Tax Act, arts 1-2, 3 and 119][income-act] · [Income Tax Act Enforcement Decree, arts 2–4][residence-decree]

An individual operating an unincorporated business generally routes business income through the individual return. Some income has a separate assessment or withholding route, and some employees settle their liability through year-end withholding. Check whether the individual still needs an annual return. [Income Tax Act, arts 4, 19, 70 and 73][income-act] · [2025 National Tax Service filing guidance][foreign-filing]

## Corporations

A corporation is domestic if its head office, principal office or place of effective business management is in Korea. A domestic commercial corporation's business-year income includes domestic and overseas income under the ordinary rules. For a foreign corporation, check the categories of Korean-source income and whether a domestic place of business, withholding or another rule governs the return. Non-profit bodies, trusts, groups and liquidation have separate rules. [Corporate Tax Act, arts 2–5, 57, 93–94, 97 and 98][corporate-act]

## Ordinary national rates for 2025

| Tax | Rate |
| --- | --- |
| Individual aggregate income tax | 6% on taxable income up to KRW 14 million, with progressive marginal rates up to 45% on the portion above KRW 1 billion. [National Tax Service 2023–2025 rates][personal-rates]. |
| Corporate income tax | For ordinary domestic corporations, 9% to KRW 200 million, 19% on the portion above that through KRW 20 billion, 21% on the portion above that through KRW 300 billion and 24% above KRW 300 billion. Use the separate scale if art 55(1)(2) applies. [Corporate Tax Act, art 55][corporate-rates]. |
| VAT | Standard rate 10%. Check the treatment of the supply and applicable registration regime. [VAT Act, art 30][vat-rates]. |

## Currency, periods and authorities

The currency is the Korean won (KRW). Confirm any required exchange-rate source and conversion date for the item. The ordinary individual tax year ran from 1 January to 31 December 2025. A corporation's business year is an accounting period prescribed by law or its governing documents and cannot exceed one year. Check the actual business year and any special opening or closing period. [Bank of Korea Act, art 47-2][currency] · [Income Tax Act, art 5][income-act] · [Corporate Tax Act, arts 6–8][corporate-act]

File ordinary national returns with the competent district office of the National Tax Service or through HomeTax. The ordinary filing deadline for 2025 aggregate individual income was 1 June 2026. For ordinary corporate taxpayers with a business year ending 31 December 2025, the national filing deadline was 31 March 2026. The relevant local authority handles separate individual or corporate local income tax returns. Check the local deadline and any extensions separately. [National Tax Service individual filing guidance][individual-deadline] · [Corporate Tax Act, art 60][corporate-act] · [2025 corporate return notice][corporate-deadline] · [Local Tax Act, arts 95 and 103-23][local-act]

See the [individual income tax guide](kr-income-tax.md), [VAT guide](south-korea-vat.md) and [social insurance guide](kr-social-insurance.md) for specialist topics. Confirm current rates, special regimes, eligibility, registration, payment and acceptance for the actual case.

[income-act]: https://www.law.go.kr/LSW/lsInfoP.do?efYd=20250101&lsiSeq=267581
[residence-decree]: https://www.law.go.kr/LSW/lsInfoP.do?efYd=20250630&lsiSeq=272559
[foreign-filing]: https://www.nts.go.kr/english/na/ntt/selectNttInfo.do?nttSn=1350825
[corporate-act]: https://www.law.go.kr/LSW/lsInfoP.do?efYd=20250314&lsiSeq=269881
[currency]: https://www.law.go.kr/LSW/lsInfoP.do?efYd=20240517&lsiSeq=251083
[individual-deadline]: https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?cntntsId=7665&mi=2223
[corporate-deadline]: https://www.nts.go.kr/nts/na/ntt/selectNttInfo.do?nttSn=1349142
[local-act]: https://www.law.go.kr/LSW/lsInfoP.do?eventGubun=060125&lsiSeq=276349
[personal-rates]: https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?cntntsId=7667&mi=2224
[corporate-rates]: https://www.law.go.kr/LSW/lsInfoP.do?efYd=20250314&lsiSeq=269881&joNo=005500&urlMode=lsInfoP
[vat-rates]: https://www.law.go.kr/LSW/lsInfoP.do?efYd=20250101&lsiSeq=267579&joNo=003000&urlMode=lsInfoP

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
