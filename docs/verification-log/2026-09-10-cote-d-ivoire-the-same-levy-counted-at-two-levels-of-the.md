# Cote d'Ivoire: the same levy, counted at two levels of the same tax

> Entry of 2026-09-10 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

`ivory-coast-payroll.md` is one of the better-built guides in this corpus. It
computes cumulative tax at each band, marks ten open research gaps by section,
and carries a step-by-step computation order. Its step 7 charges the employer
2.8% (local) or 12% (expatriate) of gross. Its step 8 then charges 1.6% for the
FDFP training levies -- 0.4% apprenticeship plus 1.2% continuing training.

Article 16 of the *annexe fiscale* to Loi de Finances n deg 2024-1109 du 18
decembre 2024 re-presents the table at CGI art. 146 as four components:

| Component | Local | Expatriate |
|---|---|---|
| Contribution employeur proprement dite | -- | 9.2% |
| Contribution nationale pour le developpement economique, culturel et social | 1.2% | 1.2% |
| Taxe d'apprentissage | 0.4% | 0.4% |
| Taxe additionnelle pour la formation professionnelle continue | 1.2% | 1.2% |
| **Total** | **2.8%** | **12%** |

1.2 + 0.4 + 1.2 = 2.8. 9.2 + 1.2 + 0.4 + 1.2 = 12.0. Both columns close
exactly, which is what settles it: there is no room inside 2.8% for a further
1.6%. The guide charged a local employer 4.4% where the statute charges 2.8% --
**a 57% overstatement**, carried into all six worked examples, the spreadsheet
template, and a Tier 1 rule that told the reader never to omit the second
charge.

The arithmetic mattered here for a second reason. The table extracted with its
columns scrambled: the header row read "Personnel expatrie | Budget
beneficiaire | Personnel local" while the data rows ran the other way. Rather
than trust the header, the assignment was settled by which column each set of
components sums to. That is the guard the reader's own docstring asks for,
applied to a case where the layout was actively misleading.

**Why the error was invisible.** Nothing in the guide contradicted anything else
in it, and no checker in this repo could see it: the two figures are correct
individually, sit in different sections, and cite different sources -- PwC for
the 2.8%/12%, the FDFP's own site for the 1.6%. Both sources are right about
their half. PwC describes the employer contribution and does not mention the
training levies; the FDFP says it *manages* the two levies and does not say who
collects them or inside what. Neither is wrong. The error lives in the join,
and only the statute shows the join.

That is the general shape: **a summary describes one level of a tax, and
another summary describes a component of it, and adding them double-counts.**
It survives cross-checking two sources against each other, because each is
faithful to what it covers.

**Three more findings from the same document**, all things the guide either
hedged or lacked:

- **The 20% professional abatement is abolished.** The guide assumed this from
  PwC and marked it an open research gap. Art. 16 says it in terms: Ordonnance
  n deg 2023-719 *supprime* it and the base is now gross taxable income. Gap
  closed against the statute -- and the same article explains why the employer
  totals did not move: the component rates were re-set so that 2.8% and 12%
  are maintained on the now-unabated base.
- **Dockers and transit dockers pay a flat 1.5%**, off the progressive scale
  entirely (new CGI art. 120 bis). Applying the barème to a docker overstates
  the tax.
- **CGI art. 263 is repealed** and the taxe d'apprentissage was cut from 0.50%
  to 0.40% (CGI art. 143). The guide's 0.4% was right, sourced to a portal.

And the classifier repeated its Togo trick one commit later: citing `dgbf.ci`,
the Ivorian Ministry of Finance directorate that publishes the enacted annexe,
moved Cote d'Ivoire off the single-source queue and the corpus's secondary
count **up** by seven. Bare ccTLD, no `gov` label, invisible to the pattern.
Twice in one session, both francophone African ministries: added, with the
comment saying so, because the next one will arrive the same way.

---
