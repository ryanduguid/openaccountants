# Armenia, again: the second reviewer finding that was wrong

> Entry of 2026-09-10 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

An outside review of PR #18 raised ten findings. Eight were already fixed at
head. One was a real leak (below). One was **wrong, and its recommended fix
would have broken a correct rule** — the second time in this branch that has
happened, and on the very article the near-miss section above is about.

The finding said the micro-business regime charges **AMD 5,000 of income tax per
employee**, not ordinary withholding, citing a law firm's page that says exactly
that. The guide says the opposite. The guide is right:

- **Art. 269(2)(2)** — the micro exemption does not reach "the obligation to
  compute and pay income tax **in the manner established by the Code**
  (*Օրենսգրքով սահմանված կարգով*) on taxable amounts paid to individuals who are
  not individual entrepreneurs or notaries". *In the manner established by the
  Code* is the ordinary rule. It names no rate and no per-head amount.
- **Art. 125(3)** — where the AMD 5,000 actually lives — charges individual
  entrepreneurs **in the turnover-tax system** (Chapter 55, not the micro
  chapter) **profit tax** (*շահութահարկ*, not *եկամտային հարկ*) of "five
  thousand drams per month, **regardless of the number of activity types**",
  and makes it their **final** profit-tax liability. Per entrepreneur, per
  month, for their own profit tax. Not per employee, not income tax, not micro.
- **Art. 270(2)** has micro-business subjects file the ordinary art. 156(1)
  income-tax calculation monthly — which is what ordinary withholding requires.
- **Art. 271**, "Payment of taxes and fees by micro-business subjects", is
  **repealed** (ՀՕ-450-Ն, 24 November 2022). Searching the Code for any amount
  attached to the micro provisions returns nothing.

So the secondary source is describing a regime that was repealed at the end of
2022, and the two AMD 5,000 charges — one real, one abolished — are close enough
to swap without anyone noticing. That is the same shape as the art. 125(3.1)
near-miss recorded above, where 18% was right for the article's first part and
23% for a subparagraph three down. **Both times the guide was already correct and
the proposed fix would have broken it.** Both times what settled it was opening
the Code and reading the whole article, including which tax the article is about.

One further note on that finding's evidence. It also said the guide contradicted
itself — that §5.10 still carried the per-employee treatment. At the commit it
reviewed that may have held; at head it does not. §5.10, the rate table, the
reviewer checklist and the prohibitions list all say the same thing. **A review
runs against a commit, not against your branch**, and a finding whose evidence is
an in-file contradiction is the kind most likely to have been overtaken.

## And one that was right, where the reviewer named one file and three were wrong

The same review found that Pakistan's Finance Act correction — read every "verify
against FA 2025" marker as naming the Act in force for the year being computed —
had been written into four `skills/` guides and into `agent-skills/pk-income-tax`,
but not into `agent-skills/pk-freelance-intake`. It was right, and the source
guide **said so in its own text**: a trailing note recorded that the counterpart
"has not been updated here". Writing down that a correction has not propagated is
not the same as propagating it.

Grepping the tree for the stale markers rather than fixing the file named found
**three**, not one: `pk-freelance-intake`, `pk-formation` and `pk-return-assembly`
all still told a reader to verify a current-year computation against FA 2025. All
three now carry the block. `agent-skills/` inherits nothing from `skills/` — it is
hand-maintained — so every correction that touches a jurisdiction with an
`agent-skills/` counterpart has to be written twice, and the grep is the only
thing that catches the second one.
