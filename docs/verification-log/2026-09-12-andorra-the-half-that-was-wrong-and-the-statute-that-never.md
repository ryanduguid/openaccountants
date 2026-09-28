# Andorra: the half that was wrong, and the statute that never held the answer

> Entry of 2026-09-12 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

Two guides said the IS return is due ***"within 6 months"*** of the year end and then glossed
that as ***"31 July"*** / ***"July"***. Six months after 31 December is 30 June. An earlier pass
recorded the contradiction, **substituted neither date**, and wrote that *"reading the sentence
gives no way to tell which"* half was wrong. That hold was right, and it is now discharged.

## July is right; "within 6 months" is the misreading

**Article 35(1) of the *Reglament de l'impost sobre societats***, as replaced by **Decret
207/2021 art. 2**:

> *"Els obligats tributaris han de presentar i subscriure la declaració per aquest impost **el
> mes següent als sis mesos posteriors a la conclusió del període impositiu**…"*

The month **following** the six months. For a 31 December year-end the six months run to 30
June and the return is filed **during July**. So it is not a six-month rule, not a
seven-month rule of thumb, and not a deadline at all in the usual sense — it is a **one-month
window**, keyed to the taxpayer's own period rather than to a calendar month.

The two halves were never a coin flip. One was the rule and the other was a paraphrase that
dropped the word doing the work.

## The bigger finding: the Law does not contain the deadline

**Article 57** of the consolidated Llei 95/2010 says only that taxpayers file *"en el lloc, **el
termini** i la forma que **es determini reglamentàriament**"*. Article 58 does the same for
self-assessment and payment. **The statute fixes no date and no window.** Every deadline row in
these guides cited the Llei — an instrument that has never held the answer. This is the
Turkmenistan art. 95 shape again (no turnover threshold in the article the guide pointed at)
and the North Macedonia shape (the return deadline is not in the Profit Tax Law): the guide
poses a question the cited instrument does not answer, and a reviewer who checks the citation
and finds nothing concludes they have missed it rather than that it is absent.

## What else the reading bought

- **Article 45 of the Law and article 33 of the Reglament** confirm the payment on account at
  **50%** of the prior year's assessed liability, *"durant el novè mes posterior a l'inici del
  període impositiu"*. The guide's *"around 50%"* is exact; its *"typically in September"* is
  true only of a calendar-year company, because the rule is keyed to the period.
- **Reglament art. 33(3): no payment on account in the first year of activity** — a carve-out
  absent from the guide.
- **"Model 202" is unsourced.** Neither the Law, the Reglament nor Decret 207/2021 names any
  numbered form; the 2021 decree leaves it to *"els formularis … que estableixi el ministeri"*.
  202 is the number of the **Spanish** *pago fraccionado* form. Flagged, not asserted wrong —
  the point is that it does not come from the instruments, not that Andorra cannot use it.
- **Decret 207/2021's transitional provision** moved the return for periods ending in December
  2020 to **31 August 2021**. July is the standing rule, not an immovable one.

## The earlier note pointed a reviewer at a page that cannot be read

That note told a reviewer to settle the question at `bopa.ad/Legislacio`. **The portal is the
same shape as `impostos.ad`** — it renders client-side and ignores query strings, so it serves
an identical shell whatever you ask it for. The advice was not wrong about where the law lives;
it was wrong about that URL being usable, and it is corrected in the guide.

What works is the portal's own unauthenticated search API, and the documents it returns, which
sit on public blob storage. **Those documents are UTF-16.** Decoded as UTF-8 they come back as
mojibake and a naive tag-strip finds zero occurrences of `declaraci` in a 240 KB tax statute —
a result that reads exactly like "the site serves nothing useful". That is a new entry in the
same family as the 39-byte conflation: **an encoding artefact impersonating an absence of
content.** The guide now records the encoding so the next person does not re-derive it.

## Andorra, second pass: what one downloaded statute paid for

The consolidated Law was already on disk from the deadline question, so four more rows cost
nothing but reading:

| Row | Was | Article 41 / 23 / 38 |
|---|---|---|
| standard rate | 10% | 10% confirmed — **and art. 41(2) adds 0% for collective investment undertakings**, expressly *not* their management companies. A second headline rate, absent from the guide |
| 5% for new companies | *"historically … confirm still in force for 2025"* | **not in the Law.** Art. 41 has two rates and no others, no *bonificació* for new companies appears anywhere, and the **first transitional provision is marked *(derogada)*** |
| holding regime | *"qualifying **foreign**-shareholding income … near 0%"* | outcome right, **every gate missing** — SA/SL only, **exclusive object**, must **apply**, **nominative shares**, and a non-resident participated company must bear a similar tax at **≥40% of the Andorran general rate**. And it covers **resident** participations too, so "foreign" is wrong |
| IP regime | *"a reduced effective rate (around 2%)"* | an **80% base reduction**, not a rate — 2% is what 80% off 10% produces. Closed list (patents, utility models, copyright-protected software), an OECD nexus fraction with a 30% uplift and a 25% foreign-subcontracting cap, three cumulative conditions, per-asset computation and a loss-recapture rule |

**"Around 2%" is the instructive one.** The number is arithmetically correct and every reader
who acts on it is wrong in the same direction: they will treat it as a rate available to
qualifying income, when it is the *product* of a base reduction that the nexus fraction cuts
down for anyone with acquired IP or foreign related-party development. A right number attached
to the wrong mechanism — the Morocco and Oman shape again, and again invisible to any check
that compares figures.

**The 5% row also shows what a hedge cannot do.** It carried *"(approx — confirm this incentive
is still in force for 2025)"*, which reads as diligence. But the hedge asks the reader to
confirm a thing, and the thing is not in the instrument the row cites; confirming it would mean
proving a negative against a statute the reader has no reason to open. The row is now the
answer rather than the question, and it says plainly that relief may exist **elsewhere** —
because absence from Llei 95/2010 is what was established, not absence from Andorran law.

**One live risk recorded rather than resolved.** The IS base is the accounting result, and
**Decret 479/2025 of 23 December 2025 approved a new *Pla general de comptabilitat***,
superseding Decret 120/2022. Its commencement and transitional rules were not read. A change of
accounting framework moves the starting point of the tax computation, so this is flagged as a
gap in the guide rather than left for a reader to discover.

## Andorra, third pass: the IGI, and three commercial hosts that were right

`ad-income-tax`'s IGI rows carried **`loyalbusinessconsulting.com; andorra-solutions.com;
gestoriabonconsellandorra.com`** on every figure. Against Llei 11/2012 (consolidated by the
Decret legislatiu del 5-6-2019) and the Reglament (Decret del 2-7-2014):

**Everything numeric was right.** EUR 40,000 and EUR 150,000 (Reglament art. 1); EUR 250,000,
EUR 3,600,000 and the months July/January, April/July/October/January, monthly (Law art. 78);
EUR 100,000 for the simplified regime (art. 74); and all five rates — 0 / 1 / 2.5 / 4.5 / 9.5%
(arts. 57–60 bis). Three commercial hosts, twelve figures, no numeric error. That result is
worth recording precisely because this branch has spent so much of its length showing the
opposite: a commercial source is not evidence, but it is not a presumption of error either,
and a pass that only ever reports commercial sources as wrong is not measuring them.

**What was wrong was never a number.**

- The 0% row read *"Medical, education, **financial**, postal services"*. **Financial services
  are at 9.5%** (art. 60) — and the table's own last line said so. The file **contradicted
  itself two rows apart** and no checker saw it, because one row is prose and the other is a
  table cell.
- *"Postal services"* is not art. 59 either. Art. 59(12) zero-rates **stamps and stamped
  effects supplied at no more than face value** — the paper, not the delivery.
- The 0% row omitted **letting of dwellings** (art. 59(9)), which is the head a reader is
  likeliest to arrive asking about.
- *"Transport"* at 2.5% omits art. 60 bis(1)'s ***excepte el transport per cable***. In a
  country whose passenger transport is substantially ski lifts, that carve-out is not a detail.
- *"Food, books, newspapers"* at 1% omits that art. 58 **excludes alcoholic drinks** and applies
  to publications only where they are not mainly advertising — with a **75%-of-publisher-revenue**
  test the guide never mentions.

## The threshold that is a trap rather than a line

The guide treats IGI registration as a state: above EUR 40,000 you are registered, below it you
are not, and the IRPF basis follows. **Reglament art. 1(4)** makes crossing it **retroactive to
1 January**: in the liquidation period where the threshold is passed, the taxpayer regularises
**the whole calendar year**. And **art. 1(3)** makes the test **joint across every activity** —
exceed it on the non-farm side and you are a trader for all of them.

Because this guide defines the IRPF basis by reference to IGI collected, the retroactivity
reaches the income tax too: its rule *"not IGI-registered → full invoice amount = IRPF income"*
stops holding for a year that began under the threshold and ended over it. **A rule that is
correct at both ends and wrong in between** — and the guide had no way to express that, because
it had modelled a switch where the statute has a look-back.

## The same wrong figure, twice, hedged once

The 5% start-up rate that `ad-corporate-income-tax` carried as *"historically … confirm still in
force"* also sat in `ad-income-tax`'s summary table as a **flat assertion with no hedge at all**:
*"10% flat; 5% for new companies with net income ≤ EUR 50,000"*. Correcting the hedged instance
and leaving the confident one would have left the corpus stating the error more strongly than
before the pass. **Grep for the figure, not for the row you found it in** — the same discipline
the Guinea 31 March / 30 April split should have taught, arriving a second time in a different
jurisdiction.

## The agent-skill had 0% and "exempt" the wrong way round

`agent-skills/andorra-igi` is a **return-preparation** skill: it classifies transactions into
boxes. Its header table listed

> *"Exempt supplies | Medical, education, insurance, residential rental, social welfare, burial"*
> *"Zero rate | 0% (exports, international transport, gold to Andorran financial institutions)"*

Medical, education, social welfare and residential letting are **not exempt**. They are heads of
the **0% *superreduït* rate at article 59** — a rate band, so the supply is **taxable** and input
tax attributable to it is recoverable. Exports are not a 0% band either: they fall outside the
territorial scope, with recovery preserved by **article 63**, and the exemptions the Law actually
spells out (arts. 39–41) are **import** exemptions.

**The two rows were swapped, and the swap costs money in one direction only.** A preparer
following this skill treats a clinic's or a landlord's output as exempt and **denies the client
input recovery the Law allows**. Both rows contain true-sounding lists of the right subject
matter; nothing about them reads as wrong. This is the sharpest instance in the branch of the
branch's recurring shape — **right facts, wrong mechanism** — and it is the first one where the
mechanism is the entire point of the document.

Also in the same table: *"Return form | Declaracio de l'IGI (**quarterly**)"*, flatly, when
article 78 makes it **semi-annual, quarterly or monthly** on turnover; *"cultural events"* at 1%
when article 60 bis puts performances and exhibitions at 2.5%; and *"para-pharmaceutical,
optical products"* at 2.5%, which is not in article 60 bis at all.

**One thing was named rather than fixed.** The skill's box map runs A1–A8 for 4.5 / 1 / 2.5 /
9.5% and has **no box for a 0% supply** — so an article 59 supply has nowhere to go in its model.
Patching that would mean inventing a box number on a real return form. The hole is flagged with
a research gap instead, on the same principle as Guinea's unmerged RTS scale: **a fabricated
answer with a citation beside it is worse than a stated gap.**
