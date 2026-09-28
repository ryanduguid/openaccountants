# The queue read 1, and that was the strongest evidence it was broken

> Entry of 2026-09-10 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

This section used to end by saying "the queue is now empty", after 260
conversions cleared it — with the caveat that this was no claim that every
citation in the corpus points somewhere good, since 66% of them still point at
commentary. The caveat was true and far too weak. The queue was empty because
the checker was looking at a shape the corpus mostly does not use.

There are two citation shapes here. The markdown link:

```
[Code Général des Impôts (Bénin)](https://www.rivermate.com/guides/benin)
```

and the trailer the generated fact blocks end almost every bullet with:

```
_(Code Général des Impôts (Madagascar) — TVA — https://manao.mg/fr/tva)_
```

Same claim, same harm, no markdown link in the second. Scanning only `[…](…)`
made **528 citations across 78 jurisdictions invisible** — under exactly the
test the markdown scan applies, that the destination is neither a tax authority
nor a recognised tax publisher. Madagascar names the Code Général des Impôts
sixty-five times, links to an authority zero times, and not one of those was in
the queue. The count is now **529**.

Two things about how that was found are worth keeping.

**It was found by disbelieving a clean result, not by a failure.** Nothing was
wrong with the output. The queue said 1, the selftest passed, the suite passed.
The prompt to look was a jurisdiction returning to the *other* queue — Madagascar,
after the `manao.mg` removal — and noticing that its citations all named the tax
code while none of them had ever appeared here.

**The first measurement of the blind spot was itself wrong, in the same
direction.** It returned **982**, because it exempted recognised publishers and
forgot to exempt authorities. `dgii.gov.do`, `gra.gm`, `src.gov.sc`, `ura.go.ug`
— the Dominican, Gambian, Seychellois and Ugandan revenue authorities — are
where a statute citation is *supposed* to land, and 454 of them did. Applying
the checker's real test gives 528. A measurement of a checker's blind spot is
itself a checker and needs the same scepticism.

Clearing the queue is a worklist of 529, not part of this change; the conversion
form is the one already used for the markdown shape, `Instrument name (as
described at [host](url))`, which keeps the instrument name — the true half of
the citation — and stops it claiming to be the destination.
