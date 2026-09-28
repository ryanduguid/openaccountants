# Chasing the eleven dead hosts, and declining to fix nine of them the fast way

> Entry of 2026-09-12 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

The eleven surviving hard-dead hosts were each given a replacement hunt: probe the
plausible correct names, then **HTTP-verify what the candidate actually serves** before
changing a citation. That second step is the whole discipline — it is what the South
African correction skipped.

**Fixed, because the replacement was verified to serve the exact body cited:**

| Was | Now | Evidence |
|---|---|---|
| `sessi.gos.pk` | **`sessi.gov.pk`** | 200, titled *"SESSI - Sindh Employees' Social Security Institution"*. `gos` for `gov` — a one-letter typo |
| `www.e-govern.ad` | **`www.impostos.ad`** | 200, redirects to `govern.ad/ca/tematiques/impostos-taxes-i-duana`, titled *"Impostos, taxes i duana - Govern d'Andorra"* |
| `www.tax.gov.bm` | **`www.gov.bm`** | 200, *"Government of Bermuda - Official Website"*. No `taxcommissioner.gov.bm` resolves either, so the row says the exact filing path has **not** been re-established rather than inventing one |

**Not fixed, and the reasons are the point.**

**Armenia is why the HTTP step exists.** `www.petakner.am` is dead, and the obvious
correction — the tax authority is *petekamutner*, not *petakner* — looks like the same
one-letter win as Pakistan. But `petekamutner.am` resolves to **10.3.17.39**, an RFC 1918
private address. Whatever that zone is serving, it is not a public site reachable from
here. Swapping the citation to it would have replaced a dead host with a **worse** one
that looks right, and DNS alone would have called it a success.

**Kazakhstan is why a mass replace was declined.** `cabinet.salyk.kz` does not resolve —
no variant, no parent. It is also named **twenty-six times across twelve files** as the
Taxpayer Cabinet (Кабинет налогоплательщика). `kgd.gov.kz` resolves and answers 200 as the
State Revenue Committee, and `cabinet.kgd.gov.kz` resolves but fails certificate
verification here. A portal unreachable from this container may be entirely correct for a
taxpayer inside Kazakhstan. So **two rows now carry the finding and the other
twenty-four references stand unchanged** — replacing twenty-six citations on DNS evidence
alone is precisely how a citation gets moved to a worse address. Three of the remaining
hard-dead hosts are Chinese, where the same caveat is strongest.

**The general rule this pass earned.** A dead citation has three possible fixes and only
one is safe: find the replacement and *verify it serves the named body*; flag the death
and leave the reference; or guess. The middle option is not a failure — for Kazakhstan,
Armenia, Montenegro and the three Chinese hosts it is the correct answer, and it is the
one a checker that only counts dead links will never suggest.
