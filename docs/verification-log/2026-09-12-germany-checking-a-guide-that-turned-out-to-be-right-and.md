# Germany — checking a guide that turned out to be right, and the one thing it did not cite

> Entry of 2026-09-12 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

Of the fifteen jurisdictions given an e-invoicing pointer above, Germany is the one
with the sharpest live obligation, so it was the one taken to primary source.
`gesetze-im-internet.de` serves the consolidated federal statutes openly, over plain
`curl`, with no challenge.

**Every date and figure in `germany-einvoice.md` held.** Reception mandatory
1 January 2025; issuance from 1 January 2027, and 1 January 2028 for smaller issuers;
EUR 800,000 threshold; EUR 250 small-amount invoices; Kleinunternehmer EUR 25,000 /
EUR 100,000. Checked against §14, §19 and §27 UStG and §33 UStDV. The wider German
pack is consistent with it — five files carry the Kleinunternehmer figures and all five
have the post-2025 numbers, cited to §19(1) as amended.

**Recording that a guide is right is worth as much as recording that one is wrong**,
and this document has been much better at the second. A verification that confirms is
not a wasted check; it is the only thing that distinguishes a figure that has been
tested from one that merely has not been challenged yet.

**What the guide did not cite.** Its "Key legislation" row named §14 UStG, the ERechV,
the Wachstumschancengesetz and the GoBD — but **not §27 Abs. 38 UStG**, which is the
provision every phase date in the guide actually comes from. The dates were right and
the authority for them was absent. Now cited.

**And the asymmetry worth stating outright, because it is the most misread part of the
regime.** §27 Abs. 38 relieves only what may be **transmitted** — the issuer's side. It
gives a recipient no right to refuse, and §14 Abs. 1 removes the consent requirement
wherever the §14 Abs. 2 Satz 2 Nr. 1 obligation applies. **So a German business has had
to be able to receive a compliant e-invoice since 1 January 2025 even though its
counterparties may lawfully still send paper until the end of 2026.** A summary that
reports "Germany's mandate starts in 2027" is describing the issuing half and is wrong
about the half that binds today. Both German VAT-return guides now carry that, sourced,
in place of the generic pointer.

That is the intended pattern for the remaining fourteen: one jurisdiction, one primary
source, replacing a pointer with a sourced statement — not fifteen descriptions written
from one sitting.

One correction inside that verification, and it is the same shape as everything else
in this document. `germany-einvoice.md`'s Transitional Rules table read *"Businesses may
still issue paper invoices or non-EN 16931 EDI invoices **with buyer consent**"*.
§27 Abs. 38 Nr. 1 attaches the consent condition to the **non-compliant electronic
format only** — paper needs no consent at all. The table was wrong in a way that made
the rule sound *stricter* than it is, and the banner added above it was right, so
leaving both would have put a contradiction inside one file eleven lines apart: exactly
the Kuwait defect, introduced by the correction rather than found by it. Both rows now
carry the provision and the condition it actually attaches to.
