# And the checker called the revenue authority a commercial host

> Entry of 2026-09-10 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

Rewriting the five guides moved every citation onto `www.otr.tg`. The
single-source queue then reported all five under its own heading: *"one host
carries the numbers, and it is neither an authority nor a recognised
publisher."* The host was the **Office Togolais des Recettes** — the body that
assesses and collects the taxes and publishes the code.

`otr.tg` is a bare ccTLD with no `gov` label, so the government-domain pattern
cannot see it, and the allowlist had never been asked about Togo. This is the
same error as `u.ae`, `belastingdienst.sr` and `andoz.tj` before it, and it
keeps recurring for the same structural reason: **the allowlist only learns
about an authority when somebody cites it**, so improving a jurisdiction's
sourcing is what exposes the gap, and the gap always reads as though the new
sourcing were worse.

Fixed by adding `otr.tg` with the test it satisfies, and by pinning three of
these bare-ccTLD authorities in the selftest so the class stops being
re-discovered one jurisdiction at a time. Secondary share **65% → 64%**
(2,697 authority against 4,768 secondary); hedged figures **845 → 837**.

The asymmetry recorded earlier in this document holds here in its sharpest
form. A missing allowlist entry over-reports risk, and the artefact it leaves —
a jurisdiction sitting on a queue somebody reads — is what eventually gets it
fixed. This one took a rewrite of five guides to surface. The entries that are
wrong in the other direction leave no artefact at all.
