# Armenia — the authority was one form submission away

> Entry of 2026-09-11 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

`am-company-formation.md` sat at **5 of 5** on `armenian-lawyer.com`. The queue had
carried a note that `arlis.am` "returns 200", which is the weakest possible reason
to leave a jurisdiction on commercial sources: a 200 says the server answered, not
that anything was read.

Opened in a browser, `arlis.am` is the Ministry of Justice's legal information
system and it publishes **the consolidated Tax Code and the LLC Law in full text**
— 1.45 million characters for the Tax Code alone, current consolidation, status
*Գործում է*. Nothing about it was hard except finding the search box.

**The search is a POST form whose text input has no `name` attribute.** A GET with
a query string silently returns the home page — same byte length, HTTP 200, no
error — so the obvious first attempt looks like a working request that finds
nothing. The field had to be addressed by its placeholder text and the form
submitted in the page. **A site is not "unsearchable" until you have looked at how
its search actually posts**, and the failure mode here was a 200 with plausible
content, the same trap the DR Congo leaflet set.

## What the Tax Code said

Two of the guide's numbers were right and thinly sourced, and now carry the
statute: **profit tax 18%** (art. 125(1)) and **VAT 20%** (art. 63(1)). Three were
approximations that the statute states exactly, and three whole mechanisms were
missing:

- **"Within about 20 days of incorporation"** is, precisely, *by the 20th day
  following the day of state registration, inclusive* — arts. 254(1)(2) and
  267(1)(2). An existing company elects by **20 February**.
- **"Turnover tax" is not a rate.** Article 258(1) prints a ten-row schedule from
  **1%** (Government-listed high technology) to **20%**, under an **AMD
  115,000,000** previous-year ceiling (art. 254(2)). Eligibility also depends on the activity, related-party and contractual exclusions in article 254(3). The guide now includes the expense reductions and floors in article 258(2)–(7): trading 9.5% of qualifying expenses with a 1% turnover floor; production 5% with a 3% floor; catering 9% with a 3.5% floor; other activity 6% with a 4.5% floor. Unused reductions carry forward by activity. [Tax Code, arts. 258 and 260](https://www.arlis.am/en/acts/230455/latest).
- **Micro-business** has an **AMD 24,000,000** ceiling (art. 267(3)) and an
  exemption whose exceptions are the operative part: a micro-business is still
  liable for import taxes, excise, environmental and road tax, and **still
  withholds income tax on employees** (art. 269). The article 267(5) exclusions must be checked before electing; accounting and advisory activities are excluded even below the ceiling.
- **The 16.67% embedded-VAT rate** (art. 63(2)) applies in four invoicing-failure
  cases and appears nowhere in the corpus.
- **Charter capital**: art. 28(1) sets no minimum — and its *next sentence* lets
  other laws set minimums by sector, which the flat "no statutory minimum" claim
  concealed.
- **Approving annual results** must happen *"ոչ շուտ, քան 2 ամիս և ոչ ուշ, քան 6
  ամիս"* after year end — **not earlier than two months** and not later than six.
  The guide gave the ceiling and dropped the floor. **A one-sided window reads as
  complete**, which is why the omission survives review.

## One check paid for four files

The flat **20% personal income tax** appears across `armenia-payroll.md`,
`armenia-social-contributions.md` and their triggers, cited to PwC throughout.
Article 150(1) confirms it and shows the phase-down that produced it — 23% from
2020, 22%, 21%, then 20% from 1 January 2023. `armenia-payroll.md` said the rate
"reached 20% from **1 July 2023**"; the statute says **1 January**.

Article 150(1.1) sets a 10% rate for qualifying R&D salary, subject to the Government-listed occupation, qualifying work, commission opinion and residence conditions. Those conditions now feed the required inputs, calculation rules and templates in both payroll guides. A verified AMD 600,000 R&D salary produces AMD 60,000 PIT; the general rate produces AMD 120,000. Unresolved eligibility stops the final calculation. If the commission opinion is revoked, the general rules govern recalculation. [Tax Code, art. 150](https://www.arlis.am/en/acts/230455/latest).

Corpus effect: authority citations 3,010 → measured after commit; Armenia moves off
zero authority citations. The registration fee, incorporation timeline and
e-invoicing mandate stay on commercial sources and are marked as such — the Law on
State Registration of Legal Entities and the Law on State Duty are both on
`arlis.am` and would settle them.
