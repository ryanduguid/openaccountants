# Thailand — the authority's own account, and three different ways a source fails

> Entry of 2026-09-12 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

`th-corporate-income-tax.md` was silent; `th-tax-overview.md` had a one-liner marked
*(approx — confirm)* whose citation was a **malformed nested markdown link** —
`[[Emergency Decree…](pwc-url)](pwc-url)` — naming the decree and linking only to a
commercial summary.

The Thai Revenue Department publishes its own English news releases, and two of them
carry the facts:

- **News No. 6/2025, 27 December 2024.** Cabinet approved the draft on 11 December
  2024; the *Emergency Decree on Top-up Tax, B.E. 2567 (2024)* was **promulgated in
  the Royal Gazette on 26 December 2024**; it applies to MNE groups with consolidated
  financial statement revenues of **at least EUR 750 million**, for **accounting
  periods commencing on or after 1 January 2025**; filing is fully electronic.
- **News No. 5/2026, 30 December 2025.** The Cabinet approved **in principle** four
  draft instruments of secondary legislation prescribing *which* MNE groups are
  subject to the charge and how income, expenses and covered taxes are adjusted in
  computing it.

**That second release is the one worth having.** It means the charge has applied since
1 January 2025 while the instruments fixing its precise scope and computation were
still in draft a year later. No rate-and-date summary conveys that, and a reader who
takes the scope as settled is reading a year-old snapshot of a moving target.

**Three sources, three different failure modes, none of them "unreachable":**

| Host | What happened | What it means |
|---|---|---|
| `www.rd.go.th` | 200, serves PDFs over plain `curl` with a referer | Usable, and authoritative |
| `ratchakitcha.soc.go.th` | Cloudflare *"Just a moment…"* — and it **stayed** 403 after the challenge-waiting driver ran | A challenge that does **not** clear. Distinct from Iraq's outright WAF deny and from a challenge that does clear |
| `krisdika.go.th` | `curl: (60) self-signed certificate` | Not a missing intermediate, so `--cacert` does not help. Verification stays on; not fetched |

The middle row is a category this register did not have. Until now the browser either
cleared a challenge or the host refused browsers too. Here the challenge is real, the
driver waited it out, and the answer was still 403.

**What was deliberately not asserted.** Oman art. 2, Kuwait and the Netherlands art.
2.1(1) all state the EUR 750m threshold as *at least two of the four immediately
preceding* periods. The Revenue Department's release states Thailand's threshold
**without** that qualification, and the decree itself could not be read. So the
two-of-four wording is **not** in the Thai guide. Four instances of a pattern is a
strong prior and still not a reading.
