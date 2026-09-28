# A scan that would have produced five findings, all of them wrong

> Entry of 2026-09-12 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

With the e-invoicing pointers in place, the twenty-three `*-einvoice.md` guides were
scanned for citation density, to pick which jurisdiction to take to primary source next
after Germany. The scan counted statute-shaped references and flagged **five guides with
zero**: Bangladesh, China, Greece, Kazakhstan and Pakistan.

**All five were false positives, and they failed in four different ways.** Reading them:

| Guide | What the scan missed |
|---|---|
| China | It cites **《刑法》第 201 条**, **第 205 条** and **第 205 条之一** — the Criminal Law articles on invoice fraud. The scan's pattern was Latin-alphabet and could not see a Chinese citation at all |
| Greece | It cites *"Law 5073/2023, updated by Law 5222/2025"*. The pattern wanted `Law No`, so a bare `Law 5073/2023` did not match |
| Italy (1 ref, nearly flagged) | Names **D.Lgs. 127/2015**, Ministerial Decree 55/2013, **D.Lgs. 471/1997** for penalties and **D.Lgs. 82/2005** for archiving, with *Art. 6, D.Lgs. 471/1997* inline on the penalty row. They sit in a "Key legislation" table row rather than in the repository's `_(source)_` wrapper |
| Bangladesh, Kazakhstan, Pakistan | **The premise was wrong.** These are 50–61-line stubs that deliberately decline to state what has not been verified. Pakistan: *"FBR e-invoicing scope and dates change by SRO — verify with the FBR."* Kazakhstan carries it as a prohibition: *"NEVER state ЭСФ deadlines or scope without verifying current КГД rules."* Both name the authority and stop |

Four distinct failure modes: **wrong alphabet, wrong phrasing, wrong container, wrong
premise.** The scan measured conformance to one citation *format* and was read as though
it measured whether a guide is *sourced*. Those are different properties, and only the
second matters.

The fourth is the one worth dwelling on. A short guide that names the authority and
refuses to state a deadline it has not checked is **behaving better than a long confident
one**, not worse. Any metric that rewards citation count would have ranked those three
guides as the corpus's weakest, when what they are actually doing is the thing this whole
document argues for. **A guide that says "I do not know, ask the FBR" is not an
unsourced guide. It is a correct one.**

**Outcome: no changes.** The scan produced five leads and zero defects, and the right
result was to edit nothing. Recording that, because a session that only ever reports what
it changed will quietly select for changing things.
