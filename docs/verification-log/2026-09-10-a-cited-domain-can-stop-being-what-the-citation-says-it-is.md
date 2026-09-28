# A cited domain can stop being what the citation says it is

> Entry of 2026-09-10 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

Benin's tax overview cited its tax year to
`https://finances.bj/wp-content/uploads/2025/01/Benin-Code-General-des-Impots-2025.pdf`.
That was the Ministry of Finance. The domain is now an Indonesian online-casino
site. The Direction Générale des Impôts has moved to
`www.impots.finances.gouv.bj` and still lists `cdgi@finances.bj` as its own
contact address, which is how you can tell the domain was theirs and was lost
rather than never having been theirs.

**A status code would not have found it.** `finances.bj` answers HTTP 200. Not
down, not a 404, not a redirect. Every check that asks "does this link resolve"
passes it. The domain is alive and answering; it just is not the ministry any
more. So `scripts/list-citation-rot.py` reads the body, not only the code.

The harm is sharper than a misdescribed source. A citation that names a statute
and lands on tax commentary sends a reader to tax commentary. This sends a
reader who is following a government citation to a gambling site, from a file
that names a Ministry of Finance beside the link.

Two hosts across 1,256 checked:

| Host | Citations | Jurisdiction | What it serves now |
|---|---|---|---|
| `zambiaprice.com` | 7 | Zambia | Indonesian slot-gambling SEO |
| `finances.bj` | 1 | Benin | an online casino, or a 500 |
| `doingbusiness.co.bw` | 1 | Botswana | "Under Construction" and a shopping cart |
| `obr.bi` | 1 | Burundi | HTTP 200 and a Joomla fatal error |

Zambia's is the worse of the two by consequence: those seven citations are the
*entire* NAPSA and NHIMA contribution table — both rates, both splits and the
monthly ceiling. Every figure in that block rested on one page that no longer
exists.

There is a third case that is not link rot at all. `www.impots.finances.gouv.bj`
— Benin's real, live, correct tax authority — is itself serving injected casino
spam ("Melbet Jordan", "Mol Casino", "ronybet"), the signature of a compromised
WordPress install. The citation is right and the authority is right; the
authority's site is hacked. Nothing the corpus can fix, and worth knowing.

## The exemption that would have hidden it

The first draft of the checker **suppressed** a squatter match when the page
also read institutional — on the reasonable theory that a gaming regulator
cited for betting duty legitimately uses those words. That rule was replaced,
before the first real run, with a demotion: such a page goes to its own printed
bucket instead of disappearing. The reasoning was the one this document keeps
arriving at — *a wrong exemption is the error that never reports itself.*

On the first real run that decision paid for itself immediately. Benin's DGI is
institutional **and** compromised. The suppressing version would have shown
nothing.

## And the bucket that was not measured at all

The same run put **github.com at the top of the dead list, with 169 citations**,
and `canada.ca` just below it. Neither is dead.

The selftest covers `judge()`, which decides what a response *means*. It could
not cover `fetch()`, which decides what response you *get*. So the classifier
was measured and the fetcher was not, and one whole bucket of 186 hosts and 654
citations came back unvalidated — reported with the same confidence as the two
real findings.

**First diagnosis, wrong.** Under fourteen-way concurrency a busy host times out,
and a timeout is indistinguishable from a domain that no longer exists. So a
serial re-check was added: anything the concurrent pass would call dead is tried
again, minutes later, with no contention.

The next sweep put github.com at the top of the dead list again. **Three of 171
hosts cleared.** The fix had addressed a hypothesis that was never tested — which
is the same error as the bucket it was meant to repair, committed while repairing
it.

**Second diagnosis, and the actual one: the environment.** These sweeps run
behind a policy-enforcing egress proxy. It answers 400 for github.com over both
schemes while `curl` reaches it perfectly well, and its own status endpoint
reports `gateway answered 502 to CONNECT (policy denial or upstream failure)`
for host after host sitting in the dead list — `minfin.gov.tm`, `mof.gov.er`,
`finances.gov.td` among them.

From inside the sandbox, **a policy denial and a dead domain are the same
event.** 592 citations were reported dead on the strength of neither, twice.

The script now proves it can reach the network before it is allowed to call
anything unreachable: a handful of control hosts are fetched first, and if any
fails the dead bucket is not printed at all and the summary says why. The serial
re-check stays — contention is real and the check is cheap — but it is no longer
mistaken for a fix.

That the loudest false positive was github.com, **both times**, is luck. A false
positive that obvious gets fixed within the hour. Had the same flaw produced a
plausible-looking list of small foreign tax authorities, it would have been
believed on both occasions, and a batch of working citations would have been
"fixed" away from sources that were fine.

There is a general form of this worth keeping: **a checker that depends on the
network cannot tell you the network is broken.** It will report the shape of its
own environment as a property of the thing it is measuring, and it will do so
with a plausible number attached.

## What it cannot see

Hosts, not documents. A ministry whose site is healthy but whose 2019 PDF has
been reorganised away passes here, and that is the commoner kind of link rot by
a wide margin. Host-level is what catches the class above — and that is the
class that misleads rather than merely disappoints.

It also does not judge WAF rejections. A live authority behind a firewall
answers a script with 403 or 406 — `impots.finances.gouv.bj` itself does, and so
do `onrc.ro` and `registrucentras.lt` — and calling those dead would bury two
real findings under 364 citations to sites that are perfectly fine.
