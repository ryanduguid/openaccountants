# Correction: the "39-byte empty document" was two different numbers, and I merged them

> Entry of 2026-09-12 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

Earlier entries in this file record a recognised dead-host signature — *"resolves but
never serves, returning a **39-byte empty document**"* — and one of them goes further:
*"the proxy log confirms the 39 bytes come from the server."*

**That last claim is wrong, and the diagnosis built on it was over-specified.**

There are two 39s and they are unrelated:

1. **`html=39` from the fetcher** is the length of an **empty DOM**.
   `<html><head></head><body></body></html>` is **exactly 39 characters**. It means the
   browser holds a blank document — the navigation never committed. The accompanying
   title, `Loading <url>`, says the same thing.
2. **`39 B received` in the proxy log** is a count of **bytes on the TLS tunnel**.

Reading them as one number turned "the page did not load" into "the server answered and
served nothing", which is a claim about the far end that the evidence does not support.

## What the proxy log actually shows

Fetching `www.minjus.gob.cu` and `www.parlamento.st` produced six identical failures each:

> `ws_closed_mid_exchange | tunnel closed (code 1006, Connection ended) after 12s;
> 517 B sent, 39 B received, client reading`

517 bytes out is a TLS **client hello**. Thirty-nine bytes back, then the tunnel closes
about twelve seconds later. **The TLS exchange does not complete.** That is consistent
with the host being down, with filtering in the path, or with geo-blocking — and the log
does not distinguish them.

So the corrected reading is narrow: **`html=39` + `Loading <url>` means the navigation
failed, and nothing more.** It is still a useful signature — it reliably separates "did
not load" from "loaded something" — but it diagnoses the *fetch*, not the *server*.

## It is also not country-specific, which is how the error surfaced

The signature had been recorded against Eritrea, two Cuban hosts and Kuwait's ministry,
which made a per-country story easy to believe. Extending the Myanmar move — *when the
ministry is dead, try the registry or gazette* — produced two more: **`www.minjus.gob.cu`**
(Cuba's Ministry of Justice, publisher of the *Gaceta Oficial*) and
**`www.parlamento.st`** (São Tomé's National Assembly). Two countries, same failure. That
killed the "Cuba is blocked" reading and prompted opening the proxy log instead of
inferring from the fetcher alone.

**Six hosts now share it, across four countries.** Each affected note has been narrowed
from *"serves a 39-byte empty document"* to *"does not complete a TLS handshake from
here"*, with the cause left open.

## The Myanmar move still works, and both new attempts failed

`myco.dica.gov.mm` succeeded where `www.dica.gov.mm` fails, so a ministry's silence is not
a jurisdiction's. But applying that to Cuba and São Tomé returned nothing: their justice
ministry and parliament fail exactly as their finance ministries do. **A heuristic that
pays once is not a method** — it is worth trying and worth reporting when it does not.

## Myanmar, second pass: what the other 180 pages held

The first Myanmar pass took the foreign-company test, the director rules and the annual
return. A second pass through the same 188 pages took the rest of what the guide had on a
blog.

**The entity-types row was wrong in both directions at once.** It listed *"Private company
limited by shares; public company limited by shares; branch/overseas corporation; **sole
proprietorship; partnership**"*. Section 2 provides for a company limited by shares
(private or public), a **company limited by guarantee**, and an **unlimited company**;
section 3 adds business associations and overseas corporations. So the guide **omits two
statutory forms** and **lists two things that are not companies under this Law at all**.
It also misses the hard cap in section 2: a **private company is limited to 50 members**,
employees excluded.

**The audit row was unqualified and is wrong for most companies.** It read *"Companies must
prepare annual financial statements; audited accounts are filed…"*. **Section 257(c):**

> *"Sections 260 to 268 (inclusive) and 279(b) do not apply to a small company"*

— the core of Division 24 (Financial Reports and Audit) — unless the constitution applies
them, the members pass an ordinary resolution, or the Registrar so determines. **Section
146** (the AGM provisions and the auditor's attendance) is switched off on the same three
conditions. And a *"small company"* under **s. 1(xxxviii)** is one with **≤30 employees**
and **<50,000,000 kyats** aggregate prior-year revenue, neither a public company nor a
subsidiary of one. That is a large share of Myanmar companies, and the guide told every one
of them the opposite.

**Section 257(b) adds a conflict rule the guide could not have inferred:** where Division 24
and the **Myanmar Accountancy Council Law** conflict, the Accountancy Council Law prevails.
A reader working only from the Companies Law can reach the wrong answer on reporting and
never know it.

## The single-source list is now exhausted of tractable entries

`list-single-source-blocks.py` reports **7** guides where one host that is neither an
authority nor a recognised publisher carries ≥75% of the numbers — down from 8, and from
14 when this branch began. What remains is:

| Guide | Why it stays |
|---|---|
| `iq-company-formation` | Iraq's Cloudflare WAF deny — a control the site owner chose, left alone |
| `er-income-tax` | Eritrea — no host completes a TLS handshake from here |
| `cu-vat-gst`, `cu-payroll-social` | Cuba — four hosts tried across finance, tax, gazette and justice |
| `st-corporate-income-tax`, `st-vat-gst`, `st-income-tax` | São Tomé — finance ministry hosting account disabled; parliament does not complete a handshake |

**Every one is blocked by reachability, not by effort.** That is the honest end state for
this queue: not "all jurisdictions are now sourced", but "the ones that can be opened from
here have been, and here is precisely how each of the rest fails".

## Laos, second pass: reading the replacing Law's rate articles

The first Laos pass established the repeal and deliberately **did not** rewrite the rates,
on the ground that hastily-read figures from a 34-page Lao-script scan would be worse than
carefully-sourced stale ones. That hold was right to make and right to lift once the work
could be done properly: a contact sheet located the rate provisions, and **articles 15 and
16 were then rendered at 200 dpi and read**.

Every figure appears in the Lao text in **words and digits together** — *ຊາວສ່ວນຮ້ອຍ (20%)*,
*ສິບຫ້າສ່ວນຮ້ອຍ (15%)*, *ຊາວສອງສ່ວນຮ້ອຍ (22%)*, *ສາມສິບສ່ວນຮ້ອຍ (30%)*, *ສາມສິບຫ້າສ່ວນຮ້ອຍ
(35%)*, *ຫ້າສ່ວນຮ້ອຍ (5%)*, *ເຈັດສ່ວນຮ້ອຍ (7%)* — clearing the digits-and-words rule.

**Most of the guide's rates survived the repeal.** That is worth stating plainly, because
the repeal banner alone implies the opposite:

| Guide row | Verdict against the replacing Law |
|---|---|
| standard 20% | **confirmed** (art. 15) |
| tobacco 22% incl. 2% to the control fund | **confirmed** (art. 16(1.1)) |
| mining 35% *(approx — confirm)* | **confirmed**, and wider — it reaches **mineral exporters**, not only concessions (art. 16(1.4)) |
| green tech 7% *(approx — confirm)* | **confirmed**, but **time-limited** to the investment-promotion incentive period (art. 16(2.2)) |
| "education / training & research centres 5%" | **too narrow** — art. 16(2.1) covers innovation, modern schools **and hospitals**, production factories, education equipment, and urban production and greening, **and is time-limited** |
| listed companies 13% for 4 years | **not in article 16 at all** — flagged, not deleted |

**Two rates were missing outright**: **22% on alcoholic beverages** (art. 16(1.2), with 2%
to the health-promotion fund) and **30% on casino business** (art. 16(1.3)).

## The finding that was not being looked for

**Article 15's second paragraph is a domestic minimum top-up tax.** Where a legal entity in
a group that is a member of a **multinational company** has an **effective rate actually
paid below fifteen percent (15%)** under international rules, it must pay additional
domestic minimum profit tax to make up the shortfall.

This branch ran a deliberate **Pillar Two sweep** across Oman, the Netherlands, Spain,
Thailand, North Macedonia, Croatia and Kuwait. **Laos was never a candidate** — it came up
only because a repeal check sent someone to read the rate article. The detector built for
the purpose found Laos not at all; an unrelated errand did.

The guide states the charge and **states what it does not know**: scope, any revenue
threshold, commencement and safe harbours are in *"separate regulations"* which the Law
names and which were not read. Naming a mechanism is a factual claim — the Oman lesson —
so the row says a top-up tax exists and stops there.

## What the time limits cost a reader

The 5% and 7% rates both run *"until the end of the profit-tax incentive period fixed by
the Law on Investment Promotion"*. The guide gave both as standing sector rates. A reader
told "green technology companies pay 7%" and not told it expires has the right number
attached to the wrong duration — the same defect shape as a right rate on the wrong base,
and equally invisible to a rate-level check.
