# Oman — the mechanism was named, and the name was the wrong one

> Entry of 2026-09-12 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

`om-tax-overview.md` said: *"Oman introduced a top-up tax (Income Inclusion Rule)
effective 1 January 2025 for in-scope multinational groups (approx — confirm
scope thresholds)"*, cited to `Top-up Tax (Royal Decree No. 70/2024)` with no
link. `om-corporate-income-tax.md` said nothing at all.

The decree turned out to be published by the Oman Tax Authority **on its own
site**, on the Income Tax Law & Regulations page, listed in English as
*"Royal Decree 70/2024 The Top-up Tax Law on Entities of Multinational Groups"*.
Finding it needed a browser: the portal is a JavaScript application and returns
107 KB of markup with no readable content to `curl`. The PDF itself then
downloaded over plain `curl` with a referer, no challenge involved.

Reading the gazette (issue 1578):

- **Article 5 imposes the tax on three classes of payer, and the guide named the
  wrong one.** Limb (1) is *the constituent entity located in Oman* — a domestic
  charge that turns on the entity's own location and owes nothing to where the
  parent sits. Limbs (2) and (3) are the Income Inclusion Rule, for an Omani
  ultimate or intermediate parent, and **article 8 confines them to a low-taxed
  constituent entity not located in Oman**. Article 6 stands limb (2) down where a
  qualified IIR applies elsewhere; article 7 charges a partially-owned Omani
  parent its allocable share.
- So the common case — an Omani subsidiary of a foreign-parented group — is caught
  by limb (1) and **is not reached by the IIR at all**. A reader told the mechanism
  is "the Income Inclusion Rule" goes looking for a parent that need not exist.
- **The threshold was not approximate.** Article 2: EUR 750,000,000 on the ultimate
  parent's consolidated statements in at least **two of the four** preceding
  financial years, prorated for a year that is not twelve months. The guide marked
  this *(approx — confirm)* while the statute gave it exactly.
- **Article 9 delegates the computation mechanism, the safe harbours and the
  permanent-establishment rules to an Executive Regulation.** That Regulation has
  not been read. The guide now says so rather than implying the Law is complete.

This is the **treatment-versus-rate** lesson from Kuwait in a second form. There,
three files agreed on 15% and disagreed about *who* was reached. Here, one file had
the rate, the date and the decree number all correct, and still pointed the reader
at the wrong charging provision. **Naming a mechanism is a factual claim, and it
fails silently: the rate is right, the date is right, the citation is well formed,
and the answer is still wrong for the taxpayer most likely to ask.**

A separate defect in the same file, found only by reading it: the standard
withholding-tax bullet appeared **four times, identically**. A generation fault,
harmless to the answer, invisible to every check that looks at figures.
