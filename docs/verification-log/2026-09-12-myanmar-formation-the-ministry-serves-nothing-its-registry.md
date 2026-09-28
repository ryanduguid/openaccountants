# Myanmar formation: the ministry serves nothing, its registry serves the statute

> Entry of 2026-09-12 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

`mm-company-formation.md` was the last tractable entry on the single-source list — **8 of
10 numeric facts on a law firm's blog**. Earlier passes had recorded Myanmar formation as
unreachable, and **`www.dica.gov.mm` does give the 39-byte empty document** (fetched alone,
so not the fetcher-contamination artefact).

**The registry subdomain is a different machine and it is alive.** `myco.dica.gov.mm`
(20.188.98.74, Azure — the ministry sits on 103.89.50.27) answers 200 as *Myanmar Companies
Online* and publishes the ***Myanmar Companies Law 2017 in English***: 188 pages, clean text
layer, alongside the Regulations 2018 and DICA Notifications 56–60/2018.

**One organisation, two hosts, opposite results.** A jurisdiction is not unreachable because
its ministry is; the registry, the gazette or the court service may serve what the ministry
does not. Guinea's answer was one page over on the same host; Myanmar's was one subdomain
over.

## The blog was mostly right, and wrong in the direction that matters

| Row | Blog said | Companies Law 2017 says |
|---|---|---|
| foreign company | *"a foreign person **owns more than 35% of its shares**"* | s. 1(xiv) — *"owns **or controls**, **directly or indirectly**, an **ownership interest**"*, and **combinations aggregate** |
| directors | *"**a private company limited by shares** requires at least one director ordinarily resident"* | s. 4(a)(v) — **every company**. And s. 4(a)(vi), absent from the guide: **a public company needs three directors, one a Myanmar citizen ordinarily resident** |
| share capital | *"no statutory minimum … (approx — confirm)"* | confirmed — and **s. 60(b): *"A share will not have a nominal or par value"*** |
| annual return | two months, then one month after the anniversary | **s. 97(a), exactly** |

**The 35% was right and the sentence around it was not.** A guide that says "owns more than
35% of its shares" tells a reader to count shares; the statute tells them to look through
indirect holdings, aggregate unrelated foreign persons, and count **control** as well as
ownership. The number survives; the test a reader would apply does not. That is the
characteristic defect of this corpus, and the reason a rate-level check finds nothing.

The **no-par-value** point is the same shape in reverse. "No minimum share capital" is
technically true and structurally misleading: under s. 60(b) a Myanmar share has **no
nominal value at all**, so a minimum is not unset but absent by design.

## What reading the whole Law added

- **s. 1(xix)** defines *"ordinarily resident"*: permanent resident, **or resident at least
  183 days in each 12-month period**. The guide used the phrase with no test behind it.
- **s. 53** puts an **overseas corporation** on a different clock entirely — annual return
  **within 28 days of its financial year end**, plus accounts at least yearly and at
  **intervals of no more than 15 months**. The guide listed "branch/overseas corporation"
  as an entity type and gave it no filing rule at all.
- **ss. 86–87**: a share transfer must be notified within **21 days**, and **the notice must
  state whether the transfer made the company become or cease to be a foreign company**,
  on pain of a **750,000 kyat** fine on every director knowingly involved. With the 35%
  test reaching indirect and aggregated interests, an ordinary share sale can flip that
  status and start the clock — a consequence no part of the guide previously joined up.

---
