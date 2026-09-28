# Oman payroll: five branches, three carried, and a 9% charge nobody mentioned

> Entry of 2026-09-12 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

Running the figure-grep from the previous section across the Oman pack turned up a second
jurisdiction-internal contradiction: `oman-vat` carried *"Social insurance (**PASI**): employer
11.5%, employee 7%"* while `om-payroll-social` said, correctly, that the **Social Protection
Fund replaced PASI** under RD 52/2023. One file named an abolished authority with pre-reform
rates; its sibling had the reform.

Checking which of the two was right meant reading the Law, and the Law made the payroll guide
wrong as well — in a way worth naming precisely.

## The scope error that looks like an arithmetic error and is not

`om-payroll-social` gave the individual branch rates and then a combined line:

> *"Approximate combined SPF rates (Omani nationals) — Employer ~12.5% + employee ~8% (**sum of
> the old-age, work-injury and employment-security branches**)"*

Every rate it carried was right. The sum of the three branches it named was right. **The
Law has five contributory branches**, and the pack was missing two of them:

| Branch | Employee | Employer | Law article |
|---|---|---|---|
| Old age, disability and death | 7.5% | 11% | art. 70 |
| Work injuries and occupational diseases | 0% | 1% | art. 90 |
| Employment security | 0.5% | 0.5% | art. 116 |
| **Sick leave and extraordinary leave** | **0%** | **1%** | **art. 123** |
| **Maternity leave** | **0%** | **1%** | **art. 128** |
| Total | 8% | **14.5%** | |

The employer side was understated by **two full points**. And the row is the reason it
survived: **it stated its own scope**. *"Sum of the old-age, work-injury and
employment-security branches"* is a true sentence, internally consistent, and it reads like a
row that has shown its working. A reviewer checking the arithmetic would tick it. The defect
is not in the sum but in the **enumeration behind it**, and nothing in the row invites you to
ask whether the list is complete.

**A total that names its components is not thereby verified.** It has only moved the claim
from "this number is right" to "this list is exhaustive" — which is the harder claim and the
one nobody checks.

## The ceiling that covers two branches out of five

The old row hedged *"subject to a contribution ceiling (approx — confirm exact wage definition
and ceiling)"*. **Article 52** answers it and then complicates it: the ceiling is **RO 3,000
per month**, and it applies to **old age/disability/death and work injuries only**. The same
article says employment security, sick leave and maternity *"are calculated on the basis of the
wage"* — uncapped.

So above RO 3,000 the employer pays 12% on RO 3,000 **plus 2.5% on the whole wage**, and there
is **no single combined percentage** that describes the charge. The corrected 14.5% is itself
true only at or below the ceiling, and the guide now says so on the same row rather than
leaving a clean-looking number to be misapplied. **Correcting a wrong total into a right total
would have been the wrong fix** — the shape of the answer, not just its value, was wrong.

## The largest omission was not an insurance branch

**Part Four (arts. 135–143)** creates a **savings system** financed by **9% of the monthly
basic wage of the insured non-Omani** (art. 139(1)), compulsory for non-Omani workers (art.
136), payable by the **employer** (Regulation art. 101) — and **art. 137** provides that it
*"replaces the end-of-service grant or gratuity disbursed by the employer to non-Omanis"*.

For an employer of expatriates in Oman this is the biggest single line in payroll, and the pack
did not mention it in any file. It was missed because it is **not in the contributions part of
the Law and not on the SPF's contribution-rate table** — it sits in its own Part, under its own
name, and the FAQ page that answers "what are the contribution rates" does not list it. **A
rate table is a list of things the publisher classified as rates**, which is not the same as a
list of what an employer pays.

The same reading corrected the expatriate row, which said non-Omanis were *"covered only for
work-injury insurance"*. Sick leave (art. 121) and maternity (art. 127) each apply
***compulsorily*** to board-designated non-Omani categories — and under art. VI(2) of the
decree, work injuries for non-Omanis commences **three years** after issuance, making the one
branch the row named **the last one to start**.

## Two hedges that were answerable and one that was not

- *"Confirm exact day"* for remittance → **art. 58**: within the **first 15 days** of the
  following month. The same article makes the **employer liable for the employee's share**,
  with deduction a right rather than a precondition.
- *"Confirm exact ceiling"* → art. 52, above.
- The savings system's commencement is **genuinely open**: art. VI(5) leaves the date to the
  board, capped at three years from 19 July 2023. The SPF's Provident Scheme page repeats the
  three-year limit and does not publish the board's date. That is recorded as a research gap
  with the outer limit stated, rather than dated by inference.

## A flat rate that is a floor

**Article 90** sets work injuries at 1% and, in the same article, has the Regulation set
*"the principles for **increasing** the percentage of contributions"* by sector or entity on
observed claims and safety compliance. The guide said 1%. **An experience-rated contribution
stated as a flat rate is wrong for exactly the employers who most need it to be right.**

## A date left unreconciled on purpose

RD 52/2023 art. VI computes the phase-in from issuance on **19 July 2023**: maternity at one
year, sick leave at two, non-Omani work injuries at three. The SPF's FAQ table instead gives
**1/7/2024** and **1/7/2025** — about eighteen days earlier than the decree's computation under
a day/month/year reading, and impossible under month/day/year. A Hijri computation from 1
Muharram 1445 lands closer to the FAQ's dates, which is suggestive and not evidence. Both dates
are now past, so nothing in the guide turns on it; **the guide says the decree's trigger, names
the discrepancy, and asserts neither**.

## And the narration matcher nobody would have caught

`oman-vat` and `agent-skills/oman-vat` are return-preparation skills: they classify bank lines
by narration. Both matched `PASI, PUBLIC AUTHORITY FOR SOCIAL INSURANCE` and **nothing else** —
so a 2025 statement showing a payment to the **Social Protection Fund** matches no rule at all.
This is a failure mode specific to pattern-matching skills: **a superseded institution is not
merely a stale fact in them, it is a hole in the matcher**. Both files now carry the SPF
narration (with Arabic) as the current payee and keep the PASI row explicitly labelled as
legacy, because historical statements still say PASI.
