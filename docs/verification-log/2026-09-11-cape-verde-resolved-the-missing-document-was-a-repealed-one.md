# Cape Verde, resolved — the missing document was a repealed one

> Entry of 2026-09-11 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

The Cape Verde entry above recorded a four-layer dead end and left the
implausible CVE 1 minimum capital flagged rather than fixed. Both halves were
wrong, and the way they were wrong is the transferable part.

**The gazette was never missing.** The register bullet said there is "no `boe.cv`
or `bo.cv`". Those were guesses at a hostname. The Cape Verdean electronic gazette
is **`boe.incv.cv`** — open, free, no login, with a full-text search over every
Boletim Oficial and a `/Bulletins/Download/<id>` endpoint that returns the
complete signed PDF. **A hostname guess that fails is not evidence that a service
does not exist**, and writing one into a register turns a failed guess into a
recorded fact. The rule the register already had — *resolves-but-refuses is not
the same as no DNS* — needs a third case in front of it: **never-asked**.

**The code was not unreachable; it was repealed.** Every search was for the
*Código das Empresas Comerciais*, because that is what the guide cited. That code
— Decreto-Legislativo n.º 3/99, de 29 de março — had its Books II and III revoked
in 2019. The current instrument is the **Código das Sociedades Comerciais**,
Decreto-Legislativo n.º 2/2019, in Boletim Oficial n.º 80, I Série, de 23 de julho
de 2019, alongside a new Código Comercial in the same bulletin. Searching for the
*subject* found it immediately; searching for the *code by name* could only ever
have found a dead document.

This is a check the corpus was not making at all. Every figure-level checker asks
*is this number right?*; none asks *is the instrument this number is attributed to
still in force?* A repealed code fails silently, because the citation stays
well-formed and the figures stay plausible.

**And the flag was right for the wrong reason.** "CVE 1 statutory minimum" for a
Sociedade Anónima was suspicious because a public company should not share a
private one's floor. The real answer is that **neither has a statutory floor**:
article 172(2) and article 237(1) both fix capital freely in the articles, and the
same enacting decree that approved the code expressly revoked **Portaria n.º
17/2013, "que fixa os montantes mínimos do capital social"** — the instrument that
set minimum amounts. The floors that do exist are indirect and were absent from
the guide entirely: a quota may not have a nominal value below CVE 100, a share
below CVE 1,000, an SA formed by public subscription needs CVE 2,500,000 fully
paid, and an SA may not distribute a single escudo of profit until its legal
reserve reaches CVE 2,500,000. **The guide's one suspicious number was less
misleading than the four real constraints it omitted.**

The pay-up split it could not verify — 50% for an Lda, 30% for an SA — turned out
to be right, from articles 176(2) and 238(2). A commercial source being unverified
is not a reason to expect it to be wrong.
