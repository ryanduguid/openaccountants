# Most of the corpus's citations are secondary, and it shows

> Entry of 2026-09-10 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

`scripts/list-source-mix.py` classifies every external link by whether it points
at a tax authority or at a secondary source, ignoring the CTA block each guide
ends with. The measurement:

Run it rather than trusting the numbers below:

```
python3 scripts/list-source-mix.py
```

**As at 10 September 2026: 65% of citations were secondary — 4,804 against 2,608
authority links, with 14 of 189 jurisdictions citing no authority domain at
all.** One publisher, PwC's Worldwide Tax Summaries, carries about a third of
all external citations on its own; the next largest is the IRS at 140, then
Estonia's tax board at 82.

That last figure moved from 18 to 14 in a single afternoon, and none of the four
gained a verified rate. Iraq, DR Congo, Suriname and Libya each had a live,
reachable revenue authority the corpus had simply never linked to: Iraq cited
PwC 55 times and an incorporation firm 14 times while `tax.mof.gov.iq` published
guides to income, property, corporate and withholding tax. Three of the four
needed no allowlist entry at all — their domains already matched the government
pattern. The only thing missing was a link.

Which is worth stating plainly, because the queue is easy to misread: leaving
the zero-authority list means *a citation now points at the authority*, not that
anything it says has been checked against it.

Those counts are a dated snapshot and are quoted for the argument, not as a
current figure. They drifted **eleven times** while this section was being
written — adding `lex.uz` to the classifier moved the zero-authority count by
one, correcting Uzbekistan moved the citation totals, auditing the statute-link
queue found nine more revenue authorities and statutory funds the classifier
had been calling marketing sites, then a code review found four domains on
the allowlist that were not authorities at all, then reading the statute-link
queue's *destinations* found four more (`u.ae`, `nssfug.org`, EswatiniLII,
NamibLII), then `belastingdienst.sr`, and then four jurisdictions were linked to
authorities that had been reachable the whole time. That is the same defect
`scripts/check-coverage-claims.py` exists to catch in `COVERAGE.md`: a derived
number copied into prose is stale the moment the thing it describes changes.
The command is the durable statement; the numbers are an illustration of it.
The heading above used to say "three quarters", which was true of the first
measurement and of no measurement since; a fraction in a heading is prose that
nobody re-runs.

> **The first version of this measurement was wrong, and the way it was wrong is
> the point.** It reported 76% secondary and 41 zero-authority jurisdictions,
> because its authority test was a government-domain pattern and a great many
> revenue authorities are not on government domains. Botswana headed the
> zero-authority list while citing `burs.org.bw`, its own revenue service.
> Estonia's tax board, the corpus's most-cited authority after the IRS, scored
> as secondary. The allowlist is now built from measurement — every entry is a
> domain the corpus actually cites — and `--unclassified` prints the remaining
> authority-shaped candidates so the omission stays visible rather than silent.
> Read the authority count as a **floor**, never a ceiling — with the caveat in
> the next section, which is that an allowlist can also be wrong upwards.

The list still earns its place. **Slovakia, Laos and Libya** are on it, and all
three produced defects on this branch: Slovakia's minimum-tax band (the
Financial Administration says EUR 960 on taxable *revenues*, not EUR 940 on
taxable income), Laos naming three of six withholding heads, Libya's three
hedged near-denials where its source states plainly that the country levies no
withholding at all.

**Iceland and Mauritius were on the list and are no longer**, which is the
measurement working as intended: Iceland's guide now cites Skatturinn because
correcting its interest rate meant going there (12%, against a 13% that was a
2024-only figure), and Mauritius's now cites the MRA because that is where the
missing eight withholding heads were found. Fixing a jurisdiction by reading its
authority takes it off this list.

Two distinct failure modes sit behind this, both found on this branch:

- **The summary's scope becomes the corpus's scope.** PwC's withholding page for
  Turkey, Thailand and Austria is three-headed, so guides built from it are
  three-headed, however faithfully they cite it. Austria's entire §99 EStG
  charge — consultancy, hiring-out of labour, supervisory fees, performers, all
  at 20% — is absent from the page.
- **The summary's prose is not the collection agent's table.** Pakistan's
  securities CGT is computed and deducted by NCCPL, whose TY 2026 notification
  gives non-ATL rates as exactly double the ATL rates below 1 July 2025 and
  equal to them above it. PwC describes a "not less than 15%" floor and KPMG a
  normal-slab/29% treatment. Both describe the statute; neither is what gets
  deducted. Three successive versions of that table in this repo were wrong,
  two of them written during this very pass.

The rule that follows is narrow enough to apply: **for a tax collected at
source, read the collection agent's own notification before any summary of it.**
NCCPL, ZIMRA's REV 5 remittance return and Trinidad's Board of Inland Revenue
guide all publish the table they actually operate, and in each case it carried
something no summary did.

The checker ranks and never gates CI, because citing a summary is not a defect
and an authority link does not prove the figures came from it. It measures
exposure, not diligence.
