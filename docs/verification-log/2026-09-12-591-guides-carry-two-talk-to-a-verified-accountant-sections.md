# 591 guides carry two "Talk to a verified accountant" sections

> Entry of 2026-09-12 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

Found while reading the Dutch guide end to end, not by any check. `CLAUDE.md` says:
*"Every published skill ends with the `<!-- openaccountants-cta-block -->` marker
followed by a 'Talk to a verified accountant' CTA … The marker makes the stamp
idempotent — bulk re-stamps skip files that already have it."*

The marker does make the stamp idempotent **from the moment the marker exists**. It
cannot detect a CTA written before the marker was introduced. In `nl-corporate-tax.md`
the marker sits *between* the two CTAs, which is the shape of the fault: a hand-written
CTA, then the marker, then the stamped CTA.

Measured: **591 of 1,926 guides** — just under a third — have more than one CTA heading
or more than one marker.

Cosmetic, and deliberately **not fixed**: a 591-file mechanical edit is a maintainer's
decision about a generated stamp, not a fact correction, and it would bury the
substantive diffs in this branch. The point worth keeping is narrower and it is about
this document's own claims: **an idempotence guarantee is only as old as the token it
keys on.** The claim in `CLAUDE.md` is true and still let a third of the corpus end up
with two CTAs, because it silently assumes no file predates the marker.
