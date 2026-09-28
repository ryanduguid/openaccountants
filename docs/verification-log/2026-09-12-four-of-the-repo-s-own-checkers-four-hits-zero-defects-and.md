# Four of the repo's own checkers, four hits, zero defects — and one of them defends a correct table

> Entry of 2026-09-12 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

Running the repo's existing consistency checkers again, now that the primary-source work
has moved a lot of figures:

| Checker | Result |
|---|---|
| `check-headline-cit` | 79 jurisdictions state an unqualified standard CIT rate; **0 disagree with themselves** |
| `check-band-continuity` | **0** gaps or overlaps across every bracket table |
| `check-derived-columns` | 83 verified, **1 mismatch** — a false positive, below |
| `check-amount-conflicts` | **3 conflicts** — all three false positives |

**The derived-column hit is the interesting one, because the checker is wrong and the
guide is right.** `mozambique-income-tax.md`'s 25% row states cumulative tax of MZN
**340,500**; the checker computes **342,300** and reports a mismatch. Both are correct
arithmetic for different formulas:

- Accumulating marginal bands: 4,200 + 18,900 + 67,200 + (1,008,000 × 25%) = **342,300**.
- The formula AT applies, stated in the guide: income × rate − *parcela a abater* =
  1,512,000 × 25% − 37,500 = **340,500**.

They agree only if the *parcela* is the continuity-preserving 35,700, and **Mozambique's
published parcela is 37,500**. The guide already documented that discontinuity in a
research-gap note; what it did not do was warn that a checker would flag the correct
figure. It does now, because the obvious response to a red check is to change the number —
which would introduce an error and silence the warning at the same time.

The AT citation also said the authority *"returned a TLS error to the fetcher"*. Retried
11 September 2026: `www.at.gov.mz` now **resets the connection**, root and rates page
alike. The failure mode changed, the result did not, and the note now says so.

**All three amount conflicts are homonyms, and one is worth fixing anyway.**

- **Canada** — a BC PST threshold of 10,000 against a Saskatchewan PST threshold of
  30,000. Different provinces, different taxes. Nothing to do.
- **South Korea** — "basic deduction" of KRW 1,500,000 in `kr-income-tax` against
  ₩2,500,000 in `south-korea-crypto-tax`. The first is the **personal** 기본공제 per
  dependant; the second is the **virtual-asset** annual deduction under Income Tax Act
  art. 21(1)(27). Two different deductions sharing an English label. **Reported and not
  edited**: both guides are `reviewed_by: Yeong Min Lee` with `review_status: current`, so
  the wording is a named professional's, and disambiguating it is theirs to do rather than
  mine.
- **Morocco** — MAD 2,000,000 in `ma-cpu` against MAD 500,000 in `ma-auto-entrepreneur`.
  Different regimes. **Both are tier 2, so this one got fixed properly**, because the
  overlap is a genuine trap:

  | | Commercial / industrial / artisanal | Services / liberal |
  |---|---|---|
  | CPU | MAD 2,000,000 | MAD **500,000** |
  | Auto-entrepreneur | MAD **500,000** | MAD 200,000 |

  **MAD 500,000 is the CPU services ceiling and the AE commercial ceiling** — the same
  number meaning two different things one guide apart. Breaching an AE ceiling routes the
  taxpayer *to* CPU, where the limit is higher, so reading it backwards ejects someone
  from a regime they are still inside. Both guides now carry the cross-reference table and
  say the checker's flag is a false positive.

**What four checkers and zero defects means.** The same thing the earlier internal-scan
passes found: these checkers have been run down. Everything they can see has been fixed,
and what is left is homonyms — the same label attached to different things. That is not a
reason to delete them; a homonym that costs nothing to dismiss is cheap insurance against
a real conflict appearing later. It is a reason not to expect them to find the next
defect. **Every substantive correction in this branch came from reading a primary source,
and none came from a consistency checker.**

---
