# `category` — the spec requires it, CI does not check it, and the docs already say so

> Entry of 2026-09-12 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

Reviewing a Bangladesh guide, an automated reviewer reported a missing `category`
key as a violation of a rule requiring it. `CLAUDE.md` and `docs/skill-template.md`
do both list `category` as required, and `CLAUDE.md` says *"CI enforces the spec
via `scripts/validate-guides.py`"*.

Measured: **1,188 of 1,926 guides carry no `category` key**, and
`scripts/validate-guides.py` does not contain the string `category` at all.

But `docs/skill-template.md` line 21 already records this, in terms:
*"**Not checked by CI at all**, and absent from roughly two-thirds of the corpus
(1,210 of 1,926 guides as at 2026-09-10) … The count drifts as guides are edited —
nothing keeps it honest, so re-measure before quoting it."*

So this is **not a new finding** — it is a known, documented gap, and the fresh
measurement (1,188, against 1,210 a day earlier) is just the drift the note
predicted. Two conclusions worth keeping:

1. **The reviewer's framing was the wrong one.** Reported as a per-file rule
   violation, it invites 1,188 single-file patches. The actual decision — enforce
   the key in CI and backfill, or relax the spec — is one decision about the
   corpus, and it belongs to the maintainer.
2. **A documented known gap must be checked for before it is reported as a
   discovery.** The measurement was worth running; presenting it as new would not
   have been.
