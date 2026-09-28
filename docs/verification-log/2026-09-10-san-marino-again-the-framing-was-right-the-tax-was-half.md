# San Marino again: the framing was right, the tax was half-described, and the citations pointed at a law that does not set the rates

> Entry of 2026-09-10 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

`sm-vat-gst.md` was the jurisdiction's second entry on the single-source queue,
**6 of 6** on one commercial blog. Its headline claim was correct — San Marino
has no VAT, it has the *imposta monofase*, a tax charged once on entry into the
territory — and neither Legge 157/2022 nor Legge 3 marzo 2025 n.30 legislates a
VAT, so the framing holds. That is the fourth guide in this branch whose numbers
and framing survived the statute. **Concentration is exposure, not error.**

What the statute added is the half of the tax the guide did not describe.

**The monofase is refunded on export.** The second sentence of art. 1 of Legge 22
dicembre 1972 n.40: *"È previsto il rimborso dell'imposta quando i beni, anche
dopo la loro trasformazione, vengono esportati."* This is the provision that lets
a San Marino manufacturer import inputs, process them and export without the tax
sticking. The guide said nothing about refunds at all — and a widely repeated
commercial description of the monofase calls it *"non detraibile e non
rimborsabile"*. The first half is right: it is not deducted up the chain, which
is what "single-stage" means. The second half is contradicted by the statute's
opening article, and the case it gets wrong is the one exporters are in. The
machinery is real and visible: the Ufficio Tributario publishes an annual refund
declaration that derives an **aliquota media** from the year's purchases, so an
exporter's recovery depends on the mix of rates on what it bought rather than on
any headline percentage.

**And every rate citation pointed at the wrong instrument.** The guide cited
"Imposta Monofase (single-phase import tax) legislation" beside each of its six
rates. Art. 26 of the same law: *"Le eventuali variazioni delle aliquote,
l'introduzione di esenzioni, la variazione dei beni soggetti alle diverse
aliquote… possono essere disposte con decreto della Reggenza."* Rate changes, new
exemptions **and the movement of goods between bands** are all decree matters.
The law demonstrates this against itself: as enacted its art. 4 ordinary rate is
**7%**, with annexed tables at 2, 3, 8, 9, 14 and 15 per cent, every one long
superseded. So a rate quoted against Legge 40/1972 is quoted against a document
that has not set it for fifty years, and the six figures stay marked with a
research gap naming what a reviewer has to find: the decree in force.

This is a different failure from a wrong number. The rates may well all be right.
**The citation was unfalsifiable** — pointing at a document that could never
confirm or deny it — and that is worth catching on its own, because a reader who
checks the cited source finds a real law, sees nothing contradicting the figure,
and concludes it is verified.

Three smaller things the statute gave that the guide had none of: the taxable
base is converted at the official rate **of the day the tax is paid**, not the
invoice date (art. 3); barter is taxed on the value of **all** goods imported
(art. 3); and art. 2 excludes money and money claims, foreign currency, postal
values and stamps, securities not representing goods, daily newspapers, and
**imports by State bodies** — the guide listed no exclusions whatsoever. From
Legge 30/2025: postal imports may now be settled **on collection of the goods**
through Poste San Marino (art. 33), and supplier credit notes issued within a
year are **refunded in full** on top of the export refund (art. 34).

## The leak grep earned its place again

Rewriting the VAT guide left `sm-tax-overview.md` asserting "standard rate 17%"
against the same "Imposta Monofase legislation" citation — the exact defect just
documented, one file away. Found by grepping the corpus for *monofase* before
committing, not after. That is now the fourth jurisdiction where a rewrite leaked
into a sibling, and the second where grepping first caught it in the same commit
rather than an hour later.

Corpus effect, re-measured: authority citations 2,797 → **2,811**, secondary
4,722 → **4,715**. San Marino ends the pass at **25 authority citations against
50 secondary**, having started at zero, and **both** its guides are off the
single-source queue — which is now at **28**.
