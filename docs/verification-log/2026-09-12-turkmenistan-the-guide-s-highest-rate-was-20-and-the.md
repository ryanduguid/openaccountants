# Turkmenistan: the guide's highest rate was 20%, and the statute's is 50%

> Entry of 2026-09-12 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

Turkmenistan sat on the single-source queue with **no authority citation in any of its
six guides** — only chandrawatpartners.com, gsl.org, rivermate.com and
healyconsultants.com. Applying the Guinea lesson (a "publishes nothing" verdict can be
one click wide), `tax.gov.tm` was tried and is **live, HTTP 200**, titled
*"Türkmenistanyň maliýe we ykdysadyýet ministrliginiň Salgyt Müdiriýeti"*.

Its *Hukuknamalar* page serves the ***«Salgytlar hakynda» Türkmenistanyň bitewi Kanuny***
— the Unified Law "On Taxes", **125 pages with a clean text layer**.

## What the Code changed

| Guide | Was | Article 172 and neighbours say |
|---|---|---|
| `tm-corporate-income-tax` | 8% ordinary / 20% state-owned and foreign | **a third band of 50%** for state-owned credit institutions, state-owned insurers, and communications / standardisation / metrology / certification providers |
| `tm-corporate-income-tax` | "small/medium enterprises — 2 percent *(approx — confirm eligibility)*" | 2% confirmed (art. 172(4)), and the base is computed **without deducting expenses** (art. 171(6)) — a low rate on a near-gross base |
| `tm-corporate-income-tax` | "ship and aircraft lease income — 6 percent" | 6% only for leasing ***işgärsiz*** — **without crew**. A wet lease stays at 15% (art. 180(3)) |
| `tm-corporate-income-tax` | property tax 1% *(approx — confirm)* | 1% confirmed, plus a stepped accrual — 0.25% / 0.5% / 0.75% / 1% (art. 141) |
| `tm-income-tax` | flat 10% | confirmed (art. 192(1)) — but gambling income is **out** of the flat rate, charged by fixed daily amounts (art. 192(2) → 172(3)) |
| `tm-vat-gst` | 15%, exports zero-rated other than oil and gas | confirmed — **the commercial source was right** — and art. 105 adds eight further limbs |
| all | nothing on art. 170 | a long exemption list: science and education, agricultural enterprises, circus services, disabled-persons' enterprises at ≥70% of staff **and** ≥20 people, free economic zones **for ten years** |

**The 50% is the finding.** Every summary of Turkmenistan in this corpus described it as
a low-tax jurisdiction topping out at 20%. For state banks, state insurers and telecoms
the profit tax is **50%** — more than six times the 8% headline the overview led with.

## The extraordinary figure got read twice, on purpose

50% is a startling corporate rate, so it was not taken from the text layer alone. The
page was rendered at 180 dpi and read: *"50 göterim - karz edaralary (döwlet eýeçiligine
degişli bolmadyk karz. edaralary muňa degişli däldir) we döwlet eýeçiligindäki
ätiýaçlandyryş guramalary üçin…"*. Confirmed.

The first render attempt landed on the **wrong page** — a text search for `172-nji`
matched a page of cross-references (art. 170) rather than the article itself. Searching
for the distinctive string `50 göterim` instead found it. **Searching for the article
number finds everything that cites the article; searching for its content finds the
article.**

Reading the page also paid for itself: the parenthetical *"credit institutions not
belonging to state ownership are not included in this"* means the 50% band takes only
**state-owned** credit institutions, while the 8% band excludes credit institutions
outright — so **privately-owned banks fall into the residual 20%**. That routing is
invisible in any rate summary and could not have been reconstructed from the three
numbers alone.

## Two things the Code did not settle, recorded as gaps rather than guessed

- **The TMT 1,280 monthly personal deduction** is not in the Code. An amount of that
  kind is normally fixed by a separate annual instrument. It keeps its "(approx —
  confirm)".
- **The 20% / 3.5% / 2% pension contributions** are not in the Code either. The Tax
  Directorate also publishes the *Ilaty durmuş taýdan goramak hakynda kodeksi* (Social
  Protection Code, 2012), which was downloaded and read — it governs **pension
  entitlements and their computation, not contribution rates**. Those sit in the Law
  *"On State Pension Insurance"*, which the site does not carry. Downloading a plausible
  code and finding it answers a different question is a result worth writing down;
  the alternative is citing it anyway because it is official and nearby.

## The fetcher will hand you the previous page's content

Four authority homepages were fetched in one `fetchc.mjs` invocation. Turkmenistan came
back with 90,864 bytes of HTML and 2,781 characters of text. **Eritrea came back with
90,841 bytes and 2,781 characters** — and a title of `Loading https://mof.gov.er/`.

Extracting the text confirmed it: the Eritrea file contained **Turkmenistan's page**.
`fetchc.mjs` reuses one browser page across its url/outfile pairs, so a failed navigation
leaves the prior page's DOM in place and writes it under the next filename.

Two near-identical byte counts for two unrelated ministries is what exposed it. The
reliable tell is the **title reading `Loading <url>`** — that result must be discarded,
not read. Eritrea is therefore **still untested**, and is recorded that way rather than
as either alive or dead. A tool that silently returns the wrong document is worse than
one that errors, and this one is now on the list of things to check before believing.

## Closing out the single-source queue's dead ends

With Turkmenistan opened, the rest of the queue was re-tested the same way — through a
real browser, against the authority's own hostname rather than a guessed one, testing
both bare and `www.` forms. Each was fetched **alone**, after the contamination above.

| Jurisdiction | Host | Result |
|---|---|---|
| **Turkmenistan** | `tax.gov.tm` | **HTTP 200, the full Tax Code.** Corrected — see above |
| **Eritrea** | `mof.gov.er` | resolves (196.200.102.238), serves a **39-byte empty document** |
| **Cuba** | `www.onat.gob.cu` | resolves (181.225.233.215), **39-byte empty document** |
| **Cuba** | `www.gacetaoficial.gob.cu` | resolves (190.92.115.173), **39-byte empty document** |
| **São Tomé** | `www.mf.gov.st` | HTTP 202, *"Under construction — Awesome site in the making!"* |
| **São Tomé** | `minfinancas.gov.st` | **HTTP 403 — *"Account disabled by server administrator"***, from an ISPmanager control panel |
| **Iraq** | — | untouched; its Cloudflare WAF deny is a control the site owner chose to apply |

**The 39-byte empty document is now a recognised signature**, not a puzzle. It is the
same response Kuwait's `fatwa.gov.kw` and `mof.gov.kw` give, and it means the name
resolves and something answers on port 443 while no document is served. Reporting it as
"no DNS" would be wrong, and reporting it as "the authority is reachable" would be
worse.

São Tomé's is the most precise negative result on this branch: not a firewall, not a
redirect, not a timeout — **the hosting account has been switched off**, and the control
panel says so in as many words. There is nothing behind it to retry into.

**So one jurisdiction in the group had a live authority and five did not**, and the one
that did had been recorded as a dead end for the same reason Guinea was: nobody had
tried the right hostname through a browser. That is the argument for re-testing a
"dead" register periodically, and equally the argument against assuming the next retry
will open. Five of six stayed shut.

---
