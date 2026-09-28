# Togo: five guides, one PDF, and eleven figures that did not survive it

> Entry of 2026-09-10 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

The single-source queue named `tg-income-tax.md` at 35/35 — every numeric fact
in the guide resting on one commercial summary site. Togo is a WAEMU state
sharing Benin's code structure, and unlike most of the queue its authority is
reachable: `www.otr.tg` serves the consolidated **Code Général des Impôts et
Livre des Procédures Fiscales, mis à jour 2025** as a 361-page PDF.

Read with `scripts/read-tax-pdf.py`, in both 1-column and 2-column modes so
that no figure was quoted unless the two passes agreed. Eleven figures across
five guides did not survive the reading:

| Guide said | The code says |
|---|---|
| IRPP band 1 taxed at 0.5% | **exonéré** (CGI art. 74) |
| band 2 at 7% | **3%** |
| band 3 at 15% to XOF 5,500,000 | **10%** to **6,000,000** |
| five bands, top rate from 15,000,000 | **eight** bands, 35% from **20,000,000** |
| "family quotient (parts)" | a fixed **XOF 10,000 per dependant per month**, capped at six, employment income only (arts. 72–73) |
| *(missing)* | a **28% standard deduction** on employment income up to XOF 10,000,000 (art. 26) |
| *(missing)* | business income is **off the scale at a flat 30%** (art. 78) |
| VAT reduced rate 10% | a **single rate of 18%**; the reduced-rate paragraph is *Abrogé* (art. 195) |
| VAT threshold XOF 60,000,000 | **XOF 100,000,000** (art. 177) |
| minimum tax "commonly cited XOF 3,000" | **MFP: 1% of turnover excl. VAT, floor XOF 20,000** (art. 120) |
| employer *taxe sur les salaires* 3% | **no such tax in the code**; only the vehicle tax and TETTIC are assimilated to direct taxes |
| registration duty on contributions 2% | formation and capital increases are **registered *gratis*** (art. 464(21)) |

Three of those deserve separate notes, because each is a different failure mode
and only one is "the summary was wrong".

**A real number, filed under the wrong tax.** XOF 60,000,000 is in the code —
art. 130, as the ceiling of the *taxe professionnelle unique* for individuals.
The VAT threshold is art. 177's 100,000,000. Same for the 2% registration duty:
art. 436 charges 2%, but on acts **extending a company's term**, and company
formation is on the *gratis* list. Both figures would survive a spot-check
against the statute by anyone who searched for the number rather than for the
rule — which is the search a reviewer under time pressure actually runs.

**Two books, one PDF, one article number.** The download binds the CGI and the
Livre des Procédures Fiscales together, each numbering its articles from 1. The
annual return deadline is **LPF art. 20**. CGI art. 20 is about benefits in
kind, and CGI art. 83 — which a search for the deadline surfaces — sits under
*Chapitre XIII : La Patente*, a different tax entirely. Every citation added
here names its book for that reason.

**The claim that was right, stated wrongly.** The guide gave the withholding
remittance deadline as "within 15 days of the end of the pay month". LPF art. 27
says *le 15 du mois suivant* — a fixed calendar date, not a rolling window. In
most months these coincide, which is exactly why the wrong form of the rule
survives: it is never visibly wrong. Two nearby articles use the same words for
other taxes (LPF art. 59 for TETTIC, art. 60 for VAT), and quoting either of
those would have "confirmed" the salary rule from a provision that has nothing
to do with salaries.

Also worth stating: the non-resident 20% withholding at LPF art. 98 is credited
against the year's tax and **is not refundable**. The guide called it a final
withholding. A non-refundable credit and a *libératoire* final tax behave the
same way in the common case and differently whenever there is other income —
the kind of distinction a summary flattens.
