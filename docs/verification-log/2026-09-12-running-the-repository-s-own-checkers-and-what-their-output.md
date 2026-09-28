# Running the repository's own checkers, and what their output is now worth

> Entry of 2026-09-12 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

`scripts/` holds 59 maintenance and checking scripts. Three that had not been run in this
work were run corpus-wide: `check-effective-dates.py`, `check-superseded-rates.py` and
`check-amount-conflicts.py`. Between them they raised a handful of leads. **Every one was
read. Every one was a false positive**, and the reasons are worth recording because they
are the same three classes this document has already had to name.

| Lead | Why it is not a defect |
|---|---|
| Albania: `tax_year=2025` but "head works in 2029" | Every 2029 mention is the **sunset** of a time-limited 0% PIT regime — *"in force until 31 Dec 2029"*. The guide is correctly dated 2025 and correctly describes a regime that runs to 2029 |
| Uzbekistan: 1% dated "1 January 2026" and "1 May 2025" | **Two different levies.** One is a 1% PIT in designated enclaves and a low-income relief; the other is a 1% *employer social tax* incentive for textile clusters and similar. The checker matched the number, not the tax |
| Morocco: turnover ceiling 2,000,000 vs 500,000 | **Two different regimes** — the Contribution Professionnelle Unique and the auto-entrepreneur regime — each with its own ceiling |
| Botswana: 14% stated as current against a 14% → 15% change | Both guides already carry the explanation: the rise proposed for 1 April 2025 appears never to have taken effect, and both say so |

**This is the homonym problem again, at figure level rather than word level.** A checker
that compares numbers sharing a label across a jurisdiction will match a *rate* to a
*different tax at the same rate*, and a *ceiling* to a *different regime's ceiling*. It
is the same failure as `Pillar II` matching a pension pillar, and it is not a reason to
stop running the checkers — it is a reason to treat their output as **triage prompts,
never as findings**. The count these scripts print is the number of things to read.

That the corpus now yields mostly false positives from its own conflict checkers is,
cautiously, a decent sign. It is emphatically **not** evidence that the corpus is
correct: these scripts compare guides against **each other**, so they are silent wherever
every guide is consistently wrong. Everything of substance found in this work — Oman's
misnamed charging limb, North Macedonia's year-wrong date, Spain's unread statute — was
found by reading a **primary source**, not by any internal consistency check.
