# Why so much of this corpus cites PwC: some authorities cannot be read

> Entry of 2026-09-10 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

The section above reports that 65% of the corpus's citations are secondary, and
treats that as exposure. Part of it is not a sourcing choice at all.

Trying to check three jurisdictions off the zero-authority list against their own
authorities, in one sitting:

| Jurisdiction | Authority | What a fetch gets |
|---|---|---|
| Madagascar | `impots.mg` | 503 on every attempt, two days apart; five other Malagasy government hosts refuse the connection outright |
| Myanmar | `ird.gov.mm` | Loads, and is entirely in Burmese; the rate tables sit behind further navigation |
| Azerbaijan | `taxes.gov.az` | Loads. The Tax Code page is 451 KB of HTML that yields 7.7 KB of text — the Code itself is rendered by a JavaScript viewer |
| Cape Verde | `mf.gov.cv` | Loads; the ministry portal does not link the tax content from its front page |
| Zambia | `napsa.co.zm` | Answers 200 with twelve characters of text |

Only Benin's DGI handed over a 269-page PDF that could be read end to end, and
that pass found five wrong band boundaries, a wrong minimum-tax floor, a rate
given as flat when it is split, and a tax system described as using a mechanism
it does not use.

So the honest reading of the 65% is two things at once. Some of it is a corpus
that reached for the easy summary. Some of it is a jurisdiction whose law is
genuinely not machine-readable from outside the country, where PwC is the best
available source and saying so is the accurate thing to do. The two look
identical in the citation count, and this document has been treating them as one
number.

What separates them is not guessable from the corpus: it takes trying to fetch
the authority. `scripts/list-citation-rot.py` now records which hosts answer,
which refuse a script, and which are gone, and that is the beginning of telling
the two apart.

Note in passing, from two of those authorities' own front pages. Myanmar's IRD
carries a standing warning that fraudsters clone its site and states its official
URL to guard against it; Azerbaijan's State Tax Service prints "Official websites
of the Republic of Azerbaijan end with .gov.az" beside a list of trusted sites.
Both are the Benin problem seen from the other side, by the institutions it
happens to.
