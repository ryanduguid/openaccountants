# The same checker, tried a second time, discarded a second time

> Entry of 2026-09-10 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

An outside review of PR #16 returned fourteen bugs, and **five were one defect**:
a figure corrected in one place and left standing in another. Paraguay's decreed
minimum wage against a prohibitions section still calling it unconfirmed; the
UK's enacted Scottish bands against a section still saying to use last year's;
Uruguay's 14% deduction credit against a working paper still offering 10%;
Liechtenstein's 2026 rates in a 2025 guide; Nigeria's education tax charged
beside the levy that replaced it.

This is the defect class the section above records a discarded checker for. The
review is independent evidence that the class is real, common, and not caught by
anything here.

## Reviewing for the defect, and committing it

Six of the seven were already fixed. The seventh, Nigeria, was recorded in a
pull-request comment as **"Fixed. 'There is no medium-company 20% band from 1
January 2026'"** — and it was not. That quotation is real and the rate bullet
was correct. What the check missed is that the correction's *consequences* were
still standing three sections away:

- a `CIT — large company` band at turnover > NGN 50B, in the bullet **directly
  after** the one saying NTA 2025 has two bands and no third;
- Plc obligations and the mandatory-filings list both charging tertiary
  education tax beside the 4% development levy that replaced it under s.59 —
  ten lines below a bullet already saying "do not add 3% tertiary education
  tax";
- a comparison table offering small companies an "education tax exempt" that is
  not a separate exemption to claim.

The check asked *did someone write the correction* and answered yes. The defect
is *did the correction reach everything it contradicts*. **Reviewing for this
class while committing it** is the most direct evidence available that it is
hard for a person, which is what makes automating it attractive — and the rest
of this section is why that remains unearned.

NGN 50 billion is real, and belongs to a different charge: the domestic turnover
limb of the 15% Minimum Effective Tax Rate in s.57(2)(b), which tops an
effective rate up rather than setting a CIT rate. Togo's XOF 60,000,000 again —
a real number filed under the wrong tax survives a spot-check, because anyone
searching for the number finds it.

## The second attempt, and what was new about it

The first attempt seeded from **denial sentences**. This one seeded from
**authorial retirement notes** — "previously stated 10%", "the earlier figure of
about 10.6%", "the old EGP 500,000 figure is superseded" — a narrower class,
because a denial is something a guide writes constantly and a retirement note is
something an author writes deliberately.

It also had a discriminator the first attempt lacked, and this one is worth
keeping even though the script is not:

> **A line carrying both the retired value and its replacement is a before/after
> statement, not a stale copy.** "The pension rate doubled from 6% to 12%",
> "EUR 550.66/month to 31 Jul; EUR 620.20 from 1 Aug". A genuinely stale copy
> carries the old value **alone** — that is what makes it stale.

That single rule removed Rwanda, Bulgaria and the US 1099-K guide from the top
of the output, where all three had filled it with lines that state their change
correctly.

## It found two real defects

**Sri Lanka's capital gains guide** — Tier 1, accountant-reviewed, marked
current — put its headline rate at 10% when no taxpayer it names pays 10%. Act
No. 11 of 2026, enacted 3 June 2026, is recorded three bullets below:
individuals and partnerships 15%, trusts and unit trusts and mutual funds and
NGOs 30%, companies 30% at the CIT rate. Every class covered, none left at 10%.
Reading the first rate bullet understates an individual by a third and a trust
by two thirds. The same file called the CSE withholding 10% in one bullet and
"now 15% post-amendment" in another — not settleable from the file, since a
withholding rate need not track the final rate it collects against, so it is
recorded as a gap naming both readings.

And Nigeria, above. Both fixes stand on their own evidence — the statute, and
the file's own other bullets — not on the script.

## And it was discarded anyway

Three tokeniser and regex defects, each found only by reading the output:

| defect | what it did |
| --- | --- |
| `band` matched inside the compound *four-band* | retired 0%, 8% and 10% from Kosovo's **current** schedule — 25 false hits, ranked first |
| the adjective-to-noun gap crossed a comma | bound "the **prior** year, the **floor**" and retired $1,000 and 50%, California's correct prepayment rule |
| any three-letter uppercase prefix read as a currency | **`ASC 805` became an amount**, and the US GAAP business-combinations guide arrived at the top with 53 false hits, because the standard's own number is on every line of it |

And three mutually incompatible rankings in one sitting, volume swinging
**60 → 29 → 94** files as each replaced the last. The middle one halved the
output and killed a true positive. Each new ranking broke a selftest written to
pin the previous one — which is the honest signal that the design was being
changed faster than it was being understood.

**Precision was never measured on a random sample.** Under every ranking that
was sampled, the top of the corpus-wide output was dominated by false positives
of a new kind. That is the bar the first attempt was discarded against —
*each tightening cut the volume and none of them improved precision* — and
applying a softer bar to the second attempt because it is newer would be the
double standard the rest of this document exists to avoid.

## Two lessons that cost more than they should have

**The sub-lesson recorded above was rediscovered, not remembered.** This
document already said, in the first attempt's write-up, that *a denial
sentence's figures split by which side of the marker they sit on*. The second
attempt assumed the retired value always **follows** the trigger, failed two
real cases, and relearned the rule from a failing selftest. It was written down,
in prose, in the right file — and prose in a methodology document did not stop
it being re-derived the hard way. A lesson lives where it executes: in a
selftest, not in a paragraph.

**A claim was published from a case that had already been fixed.** The second
attempt replaced distance-based ranking with subject-based ranking, and the
change was written up — in this document and in a pull-request description — as
a measured lesson: *"a stale copy is missed BECAUSE it is far from the note, so
proximity cannot be the evidence."* It is not supported. The Uruguay guide it
was measured against had already been repaired at the commit examined, so the
"false positives" it was tuned away from were the only thing left in the file.
Distance ranking is what surfaced Sri Lanka's stale headline; subject ranking
demoted it and promoted the two **correct** bullets in its place, because they
share "amendment" and "enactment" with the note and the stale line shares
nothing. **A stale copy is stale precisely because nobody rewrote it to match
the note, so requiring it to echo the note's wording selects against the thing
being looked for.**

Both errors have the same root as the defect class itself: something was
established in one place and its consequences were not carried to the others.

## What is actually left

The human control, unchanged and now twice-earned: **when a correction
contradicts something the guide already says, search the file for the number
before writing the new row, and again after** — and then check what the
corrected figure *implies* elsewhere, not merely whether the correction is
present. The Nigeria review above failed the second half of that sentence, which
is why it is now in it.

The replacement-value rule in the box above is the one mechanical piece worth
carrying into any third attempt. It is not enough on its own.

---
