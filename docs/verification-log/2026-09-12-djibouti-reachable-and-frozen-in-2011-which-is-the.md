# Djibouti — reachable, and frozen in 2011, which is the Mauritania result got right first time

> Entry of 2026-09-12 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

The same hostname sweep that opened the Central African Republic opened Djibouti:
`ministere-finances.dj` resolves and answers 200 where the register had `impots.dj` and
`impots.gouv.dj` under "no DNS at all". `dj-payroll-social.md` sat on the single-source
queue at **6 of 7 on an HR platform**.

**The site is frozen.** Newest news item 9 September 2012; fuel-price table covering
11 June to 11 July 2013; a budget link headed "Loi de Finances 2008"; and several `href`
values still pointing at `file:///C:/Mes Sites Web/…` on whoever built it. It serves a
*Code Général des Impôts* at `TVA/CGI 2010.pdf` whose title page reads **"DJIBOUTI — CODE
GENERAL DES IMPOTS 2011, à jour des dispositions de la loi de finance pour 2011"** and
whose own index footer says 2010. 200 pages, clean text.

**Mauritania is the precedent, and this time the claim was framed correctly from the
start.** There, "the authority works" was reported first and corrected in the same sitting
once the content turned out to stop in 2020. Here the guide's banner leads with the age:
*"The authority is reachable, and everything it publishes stops in 2011."* Every ITS figure
is stated as read from the authority's own text **and fifteen years old**, against a guide
marked `tax_year: 2025`, with an explicit instruction to treat each one as possibly
superseded by any loi de finances from 2012 onward — none of which this ministry publishes.

**Within that limit it was worth reading.** The guide said "ITS (progressive 2% to 30%)"
and nothing else. The Code gives:

- **Five bands** (art. 15): 2% below FDJ 30,000; 15% to 50,000; 18% to 150,000; 20% to
  600,000; 30% above. The endpoints the guide had are confirmed; the four interior
  boundaries it never had are now there.
- **No zero band** — the bottom slice is taxed at 2%, with a rounding rule instead: any
  fraction of income below FDJ 5,000 is disregarded (art. 14).
- **A seven-fold trap.** Article 16 taxes anyone employed for **less than one calendar
  month** at a **minimum flat 15%** on the *whole* month's remuneration. A short engagement
  under FDJ 30,000 goes from 2% to 15% — and short engagements are exactly what a payroll
  run treats casually.
- **Employees are jointly and severally liable with the employer** for ITS up to the tax
  on their own salaries (art. 286). That is the **opposite** of Burundi's article 113,
  read earlier in this same branch, where the employer alone bears unwithheld tax. Two
  francophone payroll regimes, opposite default answers to "who pays if the employer gets
  it wrong" — precisely the kind of thing a reader carries across by assumption.
- **A quarterly payment option** the guide omitted: ITS is due before the 15th of the
  following month, but an employer whose total ITS does not exceed FDJ 50,000 may pay
  before the 15th of the month after each quarter (art. 287).
- Plus the benefits-in-kind valuation rules including a flat **FDJ 40,000 per month per
  company vehicle** (art. 17), the ten-year record-keeping rule (art. 286), the
  collective-agreement pay-grid substitution where the administration doubts the employer
  (art. 13), and immediate payment on cessation or death (art. 288).

**The six CNSS rows are untouched and still unverified**, and the guide says why:
contribution rates are CNSS regulations, not the Code, which only makes CNSS deductions
deductible from the ITS base (art. 6). Reading a tax code does not verify a social
security schedule, and a banner that implied otherwise would be the Mauritania error in a
new place.

**One small thing the sweep also showed.** The guide already cited
`www.ministere-finances.dj/ITS%20IMPOTS%20DIRECT.html` in one row — so the working host
was **already in the corpus** while the source-availability register recorded the
jurisdiction as having no DNS. The register and the guides were never reconciled against
each other. That is worth more than the individual fix: a register of what is reachable is
only as good as its last check, and the corpus itself was holding evidence that
contradicted it.
