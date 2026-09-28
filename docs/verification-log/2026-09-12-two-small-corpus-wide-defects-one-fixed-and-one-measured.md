# Two small corpus-wide defects, one fixed and one measured

> Entry of 2026-09-12 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

**Fixed: 14 malformed nested citations.** `[[text](url)](url)` renders as a broken
link. Across the corpus there were exactly 14, in 4 guides — Thailand's overview had
9 of them. In every case the inner and outer URLs were identical, so all 14 collapsed
mechanically with no judgement call; the script left any with differing URLs alone,
and there were none.

**Fixed: the source classifier could not see two of Western Europe's law publishers.**
`wetten.overheid.nl` and `boe.es` were both scoring `secondary` while serving the
consolidated statute itself. The suffix rules key on `.gov`/`.go`/`.gob` markers, and
neither the Netherlands nor Spain uses one for its law publisher — the same blind spot
that `incv.cv` and `ohada.org` were added for. Both are now in `NON_GOV_AUTHORITY`
with selftests, so the Dutch and Spanish citations added in this branch count as what
they are.

**And a third domain was deliberately left out, which is the part worth recording.**
The first draft of that selftest also asserted `zoek.officielebekendmakingen.nl` —
the Dutch Staatsblad platform — as an authority. **The selftest failed, because it is
a separate registrable domain that `overheid.nl` does not reach.** Checking properly:
one request to it 404'd and one returned 500. Its own page title says
*"Overheid.nl > Officiële bekendmakingen"*, so it plainly **is** the same government
platform — and it is still absent from the allowlist, with the reason written in
beside the assertion that it classifies as `secondary`.

The rule this keeps: **a domain that has not served a document is not recorded as an
authority on the strength of its name.** That is the same rule that produced the
`boe.cv` correction, and this time a test I had just written was the thing that caught
me reaching.
