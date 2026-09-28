# The reader that said a document was empty when it had not read it

> Entry of 2026-09-10 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

Chasing the same single-source queue into Cote d'Ivoire, `scripts/read-tax-pdf.py`
was pointed at the *annexe fiscale* to the 2025 budget law. It printed one blank
line and exited 0.

That is not "the document contains no text". Every page in that file declares
its content as `/Contents [672 0 R]` -- a one-element **array** -- and the
reader's regex matched only the bare `/Contents 672 0 R` form. It found 150
pages, extracted none of them, and reported the result as though it had looked.
An hour later the same output would have read as evidence that Cote d'Ivoire
publishes nothing useful.

Three fixes, and the second matters more than the first:

1. Accept the array form, joining the parts before tokenising (a split
   `/Contents` is one stream cut at an arbitrary byte, so the pieces cannot be
   tokenised separately).
2. **Exit non-zero with a diagnostic when no page yields content**, naming how
   many objects were seen and how many were marked `/Type /Page`, and saying in
   terms that the document was not read. A tool that cannot read something must
   say so rather than return nothing.
3. Report the observed `/MediaBox` width when it disagrees with the
   `PAGE_WIDTH` argument. Passing the wrong width silently drops everything
   past the first column band -- another way to get a confident empty answer.

The Togo extraction is byte-identical after the change, which is the only
evidence that the fix is a fix and not a rewrite.

Two limits stay, and both are now visible rather than silent. Pages come out in
object order, not reading order, so the 2025 annexe interleaves pages 33-39;
the page footers make the true order recoverable. And the annexe's subset fonts
carry no usable `/ToUnicode`, so accented Latin letters map wrongly
(`p`->`e-acute`, `j`->`a-grave`, `r`->`e-circumflex`). **Digits, punctuation and
article numbers come through intact**, which is what made the figures below
quotable; the French prose around them had to be read through the substitution.
