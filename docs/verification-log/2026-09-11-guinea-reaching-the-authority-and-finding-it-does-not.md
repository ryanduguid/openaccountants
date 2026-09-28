# Guinea — reaching the authority and finding it does not publish the law

> Entry of 2026-09-11 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

`gn-income-tax.md` was **6 of 6** on `taxatlas.io`, every row marked "(approx —
confirm)". The outcome here is not a correction: it is a **negative result,
established rather than assumed**, and it is worth recording because "we used a
commercial source" and "the authority does not publish this" are very different
statements to leave in front of a reviewer.

## Clearing a bot challenge, and why the obvious fix fails

`dgi.gov.gn` answers a plain HTTP client with **202 and a 169-byte body** — an
interstitial challenge, not a page. In a browser the home page renders normally.

The trap is one layer down. A browser automation library gives you two ways to
fetch: navigate a **page**, which runs JavaScript, or call the context's
**request** API, which does not. Binary downloads naturally reach for the request
API — and it **cannot clear a JavaScript challenge**, so it returns the same
248-byte interstitial while the browser sitting next to it loads the site fine.
Two download strategies failed this way before the shape of the problem was clear.

What works is to **warm the context with a real page navigation first**, let the
challenge resolve, and only then call the request API — the clearance cookie is
set on the context, so the subsequent fetch inherits it. One further detail
mattered: the warm-up must **wait for the network to settle** before its title is
checked. Checking at `domcontentloaded` read an empty title, concluded the page had
not rendered, and skipped the wait, so no cookie was ever obtained. With a
`networkidle` wait and a short settle, the same code returned **5,214,544 bytes of
`application/pdf`**.

**A challenge is cleared per browsing context, not per request**, and the fix is
ordering rather than cleverness.

## And then the document was the wrong kind of document

The DGI's *Bibliothèque de documents* was read in full. Its "Loi et règlements"
section lists finance laws for 2016–2021 and 2025, arrêtés, décisions, taxpayer
charter and mission reports. **There is no Code Général des Impôts on the site at
all.**

The newest instrument, **Loi ordinaire L/2024/023/CNT portant loi de finances pour
l'année 2025**, is a 22-page scan with no text layer. OCR shows what it is: a
**budget appropriation law** — total revenue estimated at GNF 35,176,145,730,740,
split between the general budget and special-allocation budgets, then allocations,
closing at article 37 with the standard repeal-and-publication clause. **No IRPP
scale appears in it**, so it cannot confirm or contradict any row of the guide.

**A finance law is not always a tax law.** In several jurisdictions already worked
here — Burundi, Sierra Leone — the annual finance act is where the operative rates
and thresholds live, and that pattern invites the assumption that reaching a
finance act means reaching the rates. Guinea's is a pure appropriation act. The
guide's bands stay marked, the research gap now names the exact missing document,
and the reviewer is told where the search already went so they do not repeat it.
