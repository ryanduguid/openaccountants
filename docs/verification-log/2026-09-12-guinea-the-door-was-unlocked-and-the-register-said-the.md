# Guinea: the door was unlocked, and the register said the building was empty

> Entry of 2026-09-12 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

`dgi.gov.gn` was on the single-source queue as *"reaching the authority and finding it
does not publish the law"*. Retried 11 September 2026 through a real browser, the site
returned **6,336 characters of text** where an earlier attempt had returned zero. It is a
full WordPress publication library.

**The note this file's Guinea guide carried was wrong, and it was mine.** It said:

> The library contains no Code Général des Impôts — its "Loi et règlements" section holds
> finance laws for 2016–2021 and 2025, arrêtés, décisions and reports, and nothing else.

The *Bibliothèque de documents* page was read. **The home page was not**, and that is where
the authority's tax publications hang — off the front page, not the library. They include:

- ***Système Fiscal Guinéen au 31 mars 2021*** — the Direction Nationale des Impôts' own
  32-row table of every Guinean tax, each with its rate **and its CGI article**.
- **Full chapter reproductions of the CGI**: Impôt sur les Sociétés (11 pages, clean text
  layer), Taxes sur les Salaires, Contribution Foncière Unique, patentes et licences, TUV.
- **Loi de finances initiale 2025** — *loi ordinaire L/2024/023/CNT*, 22 pages, scanned.

The lesson is narrow and worth keeping: **"the library has nothing" is a claim about a
page, not about a site.** A negative finding about an authority needs the same breadth of
search as a positive one, and mine had been one click wide.

## What the authority's own table changed

| Guide | Was | Authority says |
|---|---|---|
| `gn-corporate-income-tax` | one "standard" rate, 25% | **three** rates — **35%** telecoms/banks/insurance/petroleum, **30%** mining, **25%** others, all art. 229 CGI (LF 2018) |
| `gn-corporate-income-tax` | mining 30%, sourced to the Mining Code via an IMF staff report | 30% confirmed, but referred to **art. 229 CGI** |
| `gn-corporate-income-tax` | IMF "3% of annual turnover" | 3% of **prior-year** turnover, floored and capped — GNF 15m/45m medium, **75m/100m** large (art. 244) |
| `gn-corporate-income-tax` | capital gains "around 15%" | **no such rate**; share gains sit in IRCM at **10%** (art. 170) |
| `gn-tax-overview` | annual return 31 March | **30 April** (art. 142.I, LF 2025 art. 24) — and it already said 30 April in `gn-corporate-income-tax` |
| `gn-tax-overview`, `gn-vat-gst` | VAT return "within 15 days after month-end" | **the 10th of each month** (art. 373 sexies I, LF 2025 art. 13) |
| `gn-payroll-social` | remittance "generally by the 15th" | **ten days** of the following month (art. 72.I, LF 2025 art. 13) |
| `gn-payroll-social` | CNSS only | **+6% versement forfaitaire** (art. 201) and **+3% apprenticeship tax** (art. 204) — 9% of payroll in taxes alone, both absent |

The overview's 31 March is the one to dwell on: **the repository already held the right
answer.** `gn-corporate-income-tax` said 30 April and the overview said 31 March, in the
same jurisdiction folder, and no checker noticed because the two rows carry different
labels. Internal contradiction is only detectable where two guides happen to phrase a
thing the same way.

## A fabricated defect, caught by the rule that exists to catch it

Drafting the VAT guide, a row was written asserting that art. 1186 CGI states its fine as
*"quatre millions"* in words against **(4 000 000 000)** in digits — a four-million /
four-billion mismatch, reported as a drafting defect in a real statute.

**There is no such defect.** The page reads ***"quatre milliards (4 000 000 000)"***.
Words and digits agree exactly. The mismatch came from reading a **contact sheet** —
twelve pages tiled at 0.52 scale to locate sections — and treating it as text.

The same sheet had already rendered *"Les assujettis qui **ne bénéficient** pas"* as
*"qui ont bénéficié pas"*, inverting a provision's scope. Both were caught the same way,
by the standing rule: **accept a figure from a scanned instrument only where the statute
gives it in words and digits together — read off the page itself, at full resolution.**
The contact sheet locates; it never quotes.

This is the fifth time in this branch a correction has itself been a defect — after
Kuwait's carried-along clause, North Macedonia's "eight withholding heads" against the
statute's ten, and the SARS URL. It is the first one caught **before** it was committed,
which is the only difference worth anything.

## The summary table nearly broke a correct row too

The DNI table describes art. 198's 15% withholding as applying to *"prestations
matériellement fournies ou effectivement utilisées en Guinée"* — services. On that basis
the guide's row **"withholding tax on royalties (to non-residents) — 15%"** looked
mislabelled and was about to be rewritten.

Reading the article itself stopped it. Art. 198 has **three** limbs, and the table
paraphrases only the third: (a) liberal-profession fees, **(b) sums received by inventors,
copyright and similar rights, and all products of industrial or commercial property**, and
(c) services. **Royalties are limb (b). The row was right.** A tax authority's own summary
table is a primary publication and still only a summary; where it and the provision both
exist, the provision governs.

## Two publications from one authority, and the later one wins on rates

The DGI's CGI chapter reproductions are headed *"Source : Code Général des Impôts, Edition
2015"* and carry the DGI's own warning that *"certaines dispositions des articles ont fait
l'objet de modification"*, directing readers to the 2018 and 2019 finance laws. The IS
chapter accordingly still shows a **flat 35%** — the pre-LF-2018 rate.

So the authority publishes 35% in one document and 35/30/25 in another. They are not in
conflict: one is the 2015 text, the other the 2021 position after LF 2018 split the rate
by sector. **Reading only the CGI chapter would have replaced a correct 25% with a stale
35%** — a "primary source" correction that made the guide worse. The chapter's own
warning label is what resolves it, and a source that dates and caveats itself is worth
more than one that does not.

**Loi de finances 2025 amends neither art. 229 nor art. 244**, so the 2021 rate table is
not displaced. That negative finding took reading all 22 pages, and it is the reason the
rates above can be stated for tax year 2025 at all.

## Left alone on purpose

The DNI table gives the **RTS** salary scale (art. 63, LF 2019) as five bands topping at
**20%** over GNF 20,000,000, starting to bite at GNF 1,000,000. `gn-income-tax` carries
five bands topping at **35%**, tax-free to GNF 5,000,000. **No row matches**, and the
shared boundaries (5m/10m/20m) are what a garbled reconstruction of one tariff looks like.

The bands were **not** overwritten. RTS is a withholding on employment income and the
guide's rows are labelled IRPP; the table's figures read as **monthly** and the guide's as
annual. Replacing a possibly-annual IRPP scale with a possibly-monthly RTS one trades an
unsourced error for a sourced one, which is worse, because the citation makes it credible.
Both guides now carry the conflict and a research gap, and `gn-payroll-social` states the
art. 63 scale for the payroll withholding, where it certainly does apply.

## e-invoicing, found while inside the jurisdiction

Loi de finances 2025 art. 27 rewrites **art. 383.V CGI**: *"La facture est saisie
manuellement sur le portail e-Tax, soit transmise automatiquement via l'API e-TVA de la
plateforme SAFIG."* Guinea runs invoice-level reporting with a manual portal route and an
API route. This is one of the fourteen jurisdictions whose e-invoicing pointer was still
an unsourced statement; it is now sourced to the enacting article. Picking it up cost
nothing because the law was already open — which is the case for reading statutes over
chasing link rot.

---
