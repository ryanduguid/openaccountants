# A blind spot fixed, that turned out to be empty

> Entry of 2026-09-10 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

`list-statute-links.py` required `skills/<tree>/<jurisdiction>/file.md` and so
never opened the **168 files that sit directly in a tree** — every US federal
guide, every cross-border guide, all the orchestrators. Same shape as the
trailer bug: for those files the queue was not low, it was uncomputed.

Fixed, and the honest result is that it found **nothing**. Zero rows in all 168.
The federal guides cite `[§1202](law.cornell.edu/uscode/text/26/1202)`, which
lands the reader on 26 U.S.C. §1202 itself — a citation doing its job.

Recording a fix that found nothing, because the alternative is leaving an
impression that it found something. It did surface one real false positive:
`law.cornell.edu` was top of the single-source queue at 52/62. Cornell's LII is
a Cornell Law School programme, not the official publisher — the OLRC publishes
the US Code — so it is a republisher, in ZambiaLII's position. But it
republishes the *section* rather than a summary of it, so it belongs with the
recognised publishers in both checkers, and flagging it would have been the
error.
