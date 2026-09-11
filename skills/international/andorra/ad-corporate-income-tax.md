---
name: ad-corporate-income-tax
description: "Source-cited draft: corporate income tax for Andorra (tax year 2025) — rates, thresholds and rules with primary-source citations. Unverified; pending local-accountant review."
jurisdiction: AD
tax_year: 2025
last_updated: 2026-09-11
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Andorra Corporate Income Tax

## Corporate income tax (Impost sobre Societats)

- **Standard corporate income tax rate** — 10% on taxable profit %  _(Llei 95/2010 IS)_
- **Reduced rate for newly created companies** — Historically 5% on the first EUR 50,000 of taxable base in the first years of activity % (approx — confirm this incentive is still in force for 2025)  _(Llei 95/2010 IS)_
- **Holding-company (ETVPESE) regime** — Qualifying foreign-shareholding income (dividends and capital gains) may be exempt, giving an effective rate near 0% (approx — confirm current qualifying conditions)  _(Llei 95/2010 IS (regim de societats de tinenca de participacions))_
- **Intangible-exploitation / IP regime** — Qualifying income from exploitation of certain intangibles may benefit from a reduced effective rate (around 2%) % (approx — confirm; subject to OECD nexus / substance rules)  _(Llei 95/2010 IS)_
- **Tax base** — Accounting profit per Andorran GAAP (Pla General de Comptabilitat), adjusted for tax-specific items  _(Llei 95/2010 IS)_
- **Corporate residence** — A company is resident if incorporated under Andorran law, has its registered office in Andorra, or has its effective management in Andorra  _(Llei 95/2010 IS)_
- **Withholding tax on dividends to non-residents** — 0% — no withholding tax on dividends paid by Andorran companies to non-residents %  _(Llei 94/2010 IRNR)_
- **Withholding tax on interest to non-residents** — 0% — no withholding tax on interest paid to non-residents %  _(Llei 94/2010 IRNR)_
- **Withholding tax on royalties to non-residents** — **5%**. This is a reduced rate: the general IRNR rate on Andorran-source income of a non-resident without a permanent establishment is **10%**, so a payment that is not a royalty does not get the 5%. The domestic 5% is settled; what varies is treaty relief, and Andorra's treaty network is small enough that the counterparty's country should be checked for a treaty rather than assumed to have one %  _(Llei 94/2010 IRNR)_
- **⚠ IS filing deadline — settled: it is July, and *"within 6 months"* is the wrong half** — This row stated the rule as ***within 6 months*** of the close of the financial year and then glossed it as *"commonly filed in July for calendar-year companies"*. Six months after 31 December is 30 June, so the two halves could not both be right. **The regulation resolves it in favour of July.** Article 35(1) of the ***Reglament de l'impost sobre societats***, as replaced by **Decret 207/2021 art. 2**, requires the return to be filed ***"el mes següent als sis mesos posteriors a la conclusió del període impositiu"*** — **in the month *following* the six months after the close of the tax period**. For a 31 December year-end the six months run to 30 June and the return is filed **during July**: a whole month's window, not a 30 June deadline and not a seven-month rule of thumb. The form, place and manner are left to the ministry  _([Reglament de l'impost sobre societats, art. 35(1)](https://bopadocuments.blob.core.windows.net/bopa-documents/031045/html/GR20190516_14_47_10.html); [Decret 207/2021, del 23-6-2021, art. 2](https://bopadocuments.blob.core.windows.net/bopa-documents/033073/html/GD20210623_14_30_00.html))_
- **⚠ The deadline is not in Llei 95/2010 at all, so citing the Llei for it is citing the wrong instrument** — **Article 57** of the consolidated Law says only that taxpayers must file *"en el lloc, **el termini** i la forma que **es determini reglamentàriament**"* — the place, **the time limit** and the form are all **delegated to regulation**. Article 58 does the same for self-assessment and payment. The Law fixes no date and no window, so the question this guide's deadline rows pose has **no answer in the statute they cite**; it lives in the Reglament above. A reader who checks the Llei and finds nothing has not missed it  _([Llei 95/2010 IS, text refós (Decret legislatiu del 5-6-2019), arts. 57–58](https://bopadocuments.blob.core.windows.net/bopa-documents/031055/html/GD20190617_08_43_02.html))_
- **Advance payment — 50% confirmed, the month is a formula, and the first year is exempt** — **Article 45 of the Law** and **article 33 of the Reglament** agree: the payment on account is **50 per cent of the assessed liability of the immediately preceding year**, made ***"durant el novè mes posterior a l'inici del període impositiu"*** — **during the ninth month after the start of the tax period**, against the period in course on the first day of that month. The *"around 50%"* is exact. The *"typically in September"* holds only for a **calendar-year** company: the rule is keyed to the taxpayer's own period, so a company with any other year-end pays in a different month. **Article 33(3) adds a carve-out this guide never had — no payment on account is due in the first year of activity.** Where a short prior period is involved, article 45(2) prorates the prior liability up to twelve months. **"Model 202" is not sourced**: neither the Law, the Reglament nor Decret 207/2021 names any numbered form — Decret 207/2021 art. 1 leaves the payment-on-account declaration to *"els formularis, en el lloc i de la forma que estableixi el ministeri"* — and 202 is the number of the **Spanish** *pago fraccionado* form, so check it before quoting it  _([Llei 95/2010 IS, art. 45](https://bopadocuments.blob.core.windows.net/bopa-documents/031055/html/GD20190617_08_43_02.html); [Reglament IS, art. 33](https://bopadocuments.blob.core.windows.net/bopa-documents/031045/html/GR20190516_14_47_10.html))_

> **How the Andorran material was reached, for whoever checks it next.** `www.impostos.ad`
> answers but serves an identical JavaScript shell for every path and yields no article
> text. **BOPA's *Legislació* portal is the same shape** — `bopa.ad/Legislacio` ignores query
> strings and renders client-side — so the earlier note pointing a reviewer at that URL was
> pointing at a page that cannot be read the way it was meant to be. What works is BOPA's
> own search API, which the portal's bundle calls and which is unauthenticated, and the
> documents it returns, which sit on public blob storage and are **UTF-16 encoded** — decoded
> as UTF-8 they read as mojibake and a naive text extraction finds nothing, which is the
> trap to avoid. The consolidated Law is the **Decret legislatiu del 5-6-2019**; the
> Reglament is the **Decret del 14-5-2019**, amended by **Decret 207/2021**, **Decret
> 464/2024** and **Decret 99/2025**. Only the 2021 decree touches article 35, and its
> transitional provision shows the window **has** been moved before — the return for periods
> ending in December 2020 was pushed to **31 August 2021** — so July is the standing rule,
> not an immovable one.

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
