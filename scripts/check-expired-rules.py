"""Flag guidance that was conditioned on something which has since happened.

A stale figure at least carries its year and a careful reader discounts it. An
expired *rule* does not: it reads as current policy however old it is, and an
agent will follow it. This finds the second kind.

The shape is a conservative default, a refusal trigger or a research gap that
says, in substance, "hold the old value until the new one is published". Every
one of them was right on the day it was written. Each becomes the error it was
written to prevent on the morning the thing it waited for arrives, and nothing
in the file knows.

What the first run found, from a grep before this existed:

  * Uruguay   Both BPS guides carried "pay period in 2026 or later: apply the
              FY2025 values and flag; do not invent 2026 figures", and
              uruguay-payroll's prohibitions ended with "NEVER apply unconfirmed
              2026 figures". The 2026 BPC was decreed on 20 January 2026. From
              that morning the rule held every 2026 payroll 4.38% below the
              correct thresholds, which is what it existed to prevent.
  * Paraguay  "The next adjustment is expected July 2026 (under tripartite
              negotiation as of April 2026; not yet officially confirmed). Use
              PYG 2,899,048; do not apply an unconfirmed 2026 figure." Decreto
              6225 of 17 June 2026 raised it 5% to PYG 3,044,000 from 1 July.
              The minimum wage is the IPS contribution floor, so the rule
              understated every contribution on a wage at or near the floor.
  * UK        A tier 1, accountant-reviewed guide carried "TBC -- HMRC publishes
              annually" in all five cells of its 2026-27 threshold column, plus
              a refusal code for the case. The 2026-27 year began on 6 April
              2026 and GOV.UK publishes the thresholds. Worth noting that the
              recorded review is dated 3 June 2026, two months into that year:
              a human sign-off passed over it too, which is the argument for
              checking this by date rather than by reading.
  * US-CA     "Where the FTB has not yet published final figures, the skill uses
              projected amounts and flags them with (verify 2025)."

Two kinds of hit this deliberately does NOT report.

A rule that names no date cannot be judged. "Do not invent depreciation rates"
is a permanent instruction and correct forever; Iceland, Moldova and Georgia all
carry one and none is a defect. Only a rule tied to a date this script can read
is reportable.

A statement of law that happens to contain "until" is not a rule about the
corpus's own maintenance. Bermuda's tax assurance runs "until 2035", Albania's
0% band "until 2029", North Carolina's graduated penalty takes effect in 2027.
Those are the facts, correctly dated, and a future date suppresses the hit.

MEASURED AGAINST ITSELF, SEPTEMBER 2026

The queue reached 51, then 46 as leads were worked. Before working more of it,
it was worth asking how many were real -- the same question that removed 40% of
the withholding-scope queue as tool artefacts. Here it removed 13 of 46.

Every lead dated before 2024 was a STATUTE YEAR read as a deadline: Part 4A TCA
1997, amendments to ITO 2001, the Federal Excise Act 2005, PMK 136/2023,
Perpres 49/2021. A rule citing a 1997 Act appeared 29 years overdue. Cited
years older than last year are now suppressed, and the cutoff is by age rather
than blanket, because "Finance Act 2025 ... TBC, confirm gazetted text" waits
on a year that also sits in a statute name.

Two false-positive classes survive and are documented rather than patched,
because every phrasing that would suppress them also suppresses real hits:

  * A HISTORICAL EFFECTIVE DATE inside a waiting line. "Since 1 July 2024 (PMK
    136/2023) the NIK functions as the NPWP ... TBC" reports on the 2024, which
    is when the rule started rather than a deadline it missed.
  * A WAITING PHRASE ABOUT THE CLIENT'S OWN PAPERWORK. Saudi RETT's
    "inheritance certificate not yet issued -- STOP, wait for the Sharia court
    certificate" is an instruction about one estate's documents, and the US
    estate pack's "refer to state-specific Tier 2 skill (not yet released)" is
    about this repo's roadmap. Neither waits on a publication.

A THIRD BLIND SPOT, AND THIS ONE THE CHECK CREATED ITSELF

Working the queue produced corrections that say, in substance, "this used to
wait on X, and X has happened". Each necessarily names the instrument and its
date, so each came straight back as a fresh lead: "NTA 2025 commenced on 1
January 2026 and is in force", "Finance Act 2026 abolished the surcharge",
"that TBC has been overtaken twice". Three of thirty-seven hits were this check
reporting its own fixes, and the share would have grown with every fix made --
a queue refilling with its own annotations faster than it drains.

A resolution is recognisable because it is past tense about the event, which a
rule still waiting cannot be. RESOLVED now suppresses the line where it says
the instrument commenced, was enacted or gazetted, has been abolished or
overtaken, is in force, or that a deadline has passed or a window closed.

WHAT THE REMAINING QUEUE IS MADE OF

Classified by hand at 34 lines, because a count is not a work estimate:

  * About eight are GENUINE open TBCs on specific technical points -- Nigeria's
    MET top-up mechanics and Development Levy allocation formula, Pakistan's
    late-filer tier and ACT characterisation. These need someone to read a
    gazette.
  * About seven are PERMANENT INSTRUCTIONS that happen to name a year: "where a
    threshold is uncertain, mark TBC and verify against the current Finance Act
    text". Those are correct forever and are not defects. They are reported
    because the year sits inside the instruction, and no phrasing separates them
    from a real wait without losing real waits.
  * The rest are the documented false-positive classes: a historical effective
    date, a waiting phrase about a client's own paperwork, and a worked
    example's fact pattern ("ZATCA has not yet published a standard price for
    this exact SKU" is a premise of a scenario, not a rule).

So the working figure is closer to eight than to thirty-four, and anyone
draining this queue should expect to close most of it by reading rather than by
editing.

What a full run returns after all of that: 34 lines, and they are leads rather
than defects. Most are genuinely pending -- Nigeria waiting on the
NTA 2025 implementing regulations, Morocco on the e-invoicing decree, Pakistan
on several 2026 items -- and each needs someone to go and look rather than a
recompute. Two UK guides are waiting on a Scottish Budget and on Finance Bill
enactment, which are the same shape and worth taking next.

The check earned its keep before it was finished. Run against the UK student
loan guide immediately after that guide was fixed, it found a second copy of the
same threshold table two hundred lines further down, still reading TBC in all
five cells, plus a refusal code and a sensitivity test built on the same
placeholder. The first fix had been to the table a reader sees first.

A code review on PR #16 found two more gaps and both are fixed here. A named
month was treated as expiring on its first day, so a rule waiting on "September
2026" read as expired from 2 September. And a cell reading "TBC -- verify
Finance Bill 2026" was not matched at all, because the TBC alternative required
a publication verb and "verify" was not in the list; adding it took the queue
from 37 to 51 and surfaced the UK savings-allowance cells this branch then
resolved.

Exit status is 1 when anything is reported, so this can gate CI once the
standing queue is worked down.

Usage: python3 scripts/check-expired-rules.py [--selftest] [path ...]
"""
import os, re, sys, datetime, calendar

TODAY = datetime.date.today()

# A rule that waits for a publication.
#
# This pattern has been tightened twice. The first version returned 286 hits and
# the second 63, and in both cases the count said more about the pattern than
# about the corpus. What came out, and why:
#
#   * A bare "TBC". In the Australian pack TBC is the Transfer Balance Cap, used
#     a dozen times as a noun. TBC now has to sit beside a publication verb.
#   * A bare "as of <Month> <Year>". That is the corpus dating a research
#     position honestly -- Morocco's crypto pack says "no published binding
#     guidance as of May 2026" and means it. Dating a statement is the behaviour
#     this repo wants, and on its own it says nothing about whether the thing has
#     since been published.
#   * A bare "until <year>". Russia's "Until 2024, USN payers were not VAT
#     payers" is a statement of history, and Bermuda's "until 2035" and Albania's
#     "until 2029" are statements of law. Only "until ... published" counts.
#   * "do not use the <year> figure". Latvia's payroll guide says "Rises to
#     EUR 780 from 1 January 2026 -- do NOT use the 2026 figure for a 2025
#     computation", which is a correct instruction not to mix years and the
#     opposite of the defect.
#   * A bare "expected <year>". A worked example's "Expected 2025 NTO = $25,000"
#     is an answer key, not a forecast.
#
# The cost of that is recall, and it is worth naming. Uruguay's conservative
# default read "apply FY2025 values and flag; do not invent 2026 figures" and no
# pattern here catches it, because every phrasing that would also catches Latvia.
# The file still surfaces, because its prohibitions list said "use FY2025 values
# until 2026 values are published" two hundred lines below and that does match.
# Treat a hit as pointing at a FILE worth reading rather than at the only bad
# line in it.
WAITING = re.compile(
    r'not yet (?:been |\w+ )?(?:published|announced|confirmed|released|set|issued)|'
    r'\bTBC\b[^.|\n]{0,40}?\b(?:publish|announce|confirm|pending|await|verify)|'
    r'\b(?:publish|announce|confirm|pending|await|verify)\w*[^.|\n]{0,40}?\bTBC\b|'
    r'until\b[^.|\n]{0,60}?\b(?:published|announced|available|released|issued)\b|'
    r'pending (?:HMRC|IRS|FTB|SLC|MTESS|BPS|DGI|SIN|ATO|publication|announcement|confirmation)|'
    r'(?:expected|anticipated)\b[^.|\n]{0,50}?'
    r'\b(?:adjustment|publication|decree|regulation|announcement|revision|update|uprating)\b|'
    r'\b(?:adjustment|publication|decree|regulation|announcement|revision|update|uprating)\b'
    r'[^.|\n]{0,50}?\b(?:is |are )?(?:expected|anticipated)\b',
    re.I)

# How far from the waiting phrase a date has to be to be about it.
WINDOW = 60

# A line that RESOLVES a wait is not a line that is waiting.
#
# This check created its own noise. Working its queue produced corrections that
# say, in substance, "this used to wait on X, and X has happened" -- "NTA 2025
# commenced on 1 January 2026 and is in force", "Finance Act 2026 abolished the
# surcharge", "that TBC has been overtaken twice". Each of those sentences
# necessarily names the thing waited on and its date, so each came straight back
# as a fresh lead. Three of thirty-seven hits were the check reporting its own
# fixes, and the share would grow with every fix made.
#
# A resolution is recognisable because it is in the past tense about the event:
# the instrument commenced, was enacted, was gazetted, has been abolished, is in
# force, has fired, is now confirmed, has been overtaken, is RESOLVED. A rule
# still waiting cannot say any of those about the thing it waits for.
#
# This suppresses the whole LINE rather than the date, deliberately. A line that
# both records a resolution and raises a genuinely new wait is rare, and the
# cost of missing one is smaller than the cost of a queue that refills with its
# own annotations faster than it drains.
RESOLVED = re.compile(
    r'\b(?:commenced|entered into force|came into force|took effect|'
    r'was (?:enacted|gazetted|published|issued|passed|signed)|'
    r'(?:has|have) (?:been )?(?:abolished|repealed|overtaken|fired|resolved|'
    r'superseded|since been|now been)|'
    r'is (?:now )?in force|is now confirmed|now confirmed|'
    r'RESOLVED|RESOLVIDO|no longer (?:pending|open)|'
    r'that (?:TBC|hedge|rule) has|deadline has passed|window has closed)\b',
    re.I)

# The date the rule is waiting on.
YEAR = re.compile(r'\b((?:19|20)\d{2})\b')
# A year inside a statute's NAME is usually not a date anything is waiting for.
# Nine of the 46 leads this check produced were of that shape: "Part 4A TCA
# 1997", "amendments to ITO 2001", "Federal Excise Act 2005", "PMK 136/2023",
# "Perpres 49/2021". Reading those as deadlines made a rule citing a 1997 Act
# look 29 years overdue, which costs a reader the same attention as a real
# finding. Two ways a year can sit in a citation:
#   * it follows an instrument word within a short span -- Act 2005, TCA 1997;
#   * it sits in a reference number -- 136/2023, 49/2021, 56/2025.
#
# But a citation year is NOT always inert, and the first version of this fix got
# that wrong. "Finance Act 2025 -- annual amendments to ITO 2001 ... (TBC,
# confirm gazetted text)" is a rule waiting on the Finance Act 2025, and that
# year sits in a statute name too. Suppressing every cited year lost the hit.
#
# The distinguisher is age. A rule written now cannot be waiting on an Act from
# 1997 or 2005, and can plausibly be waiting on one from last year. So a cited
# year is suppressed only when it is older than LAST year. That is a heuristic
# and it has a cost worth naming: a rule genuinely waiting on a long-overdue
# instrument from 2023 or earlier will be missed. That trade is deliberate --
# 13 false positives removed against a class of miss that has not yet appeared
# in this corpus -- and it is the reason the cutoff is stated here rather than
# buried in the regex.
CITATION_YEAR = re.compile(
    r'(?:\b(?:act|ordinance|law|decree|regulation|code|rules?|'
    r'tca|ito|sta|pmk|perpres|pp|uu|rd|cap|schedule|s|art|article|no)\b'
    r'[^\w\n]{0,12}(?:\d{1,4}[^\w\n]{0,3})?|/)'
    r'((?:19|20)\d{2})\b', re.I)
MONTHS = ('January February March April May June July August September October '
          'November December').split()
MONTH_YEAR = re.compile(r'\b(%s)\s+((?:19|20)\d{2})\b' % '|'.join(MONTHS), re.I)
# A span like "2026-27" is judged by the year it STARTS in, which the bare-year
# pattern already picks up. Treating it as running to 2027 was the first version
# and it suppressed the case the check exists for: the UK 2026-27 tax year began
# on 6 April 2026, so a cell still reading TBC in September 2026 is expired.

# Frontmatter description lines restate trigger phrases and are not guidance.
SKIP_PREFIX = ('description:', 'name:', 'tax_year_notes:')


def _dates(line):
    """Every date the line commits to, as the last day it is still waiting.

    The two precisions are treated differently, deliberately.

    A **named month** runs to its last day. "The adjustment is expected July
    2026" is not expired on 2 July. Returning the first of the month was the
    original bug and it made every month-precise rule look expired from the
    second day of the month it was waiting for.

    A **bare year** is taken as 1 January of that year, not 31 December. In
    these rules a bare year names the year the awaited thing arrives in -- "use
    FY2025 values until 2026 values are published", and the 2026 BPC decree
    landed on 20 January. Reading it as year-end would mean the check could
    never report anything during the current year, which is exactly when a rule
    like that is doing damage. The cost is the opposite error: a rule waiting on
    something genuinely due late in the current year reads as expired early.
    That is the safer direction for a lead-generator a human reads.
    """
    out = []
    for m in MONTH_YEAR.finditer(line):
        y, mo = int(m.group(2)), MONTHS.index(m.group(1).title()) + 1
        out.append(datetime.date(y, mo, calendar.monthrange(y, mo)[1]))
    stale_citation = {m.start(1) for m in CITATION_YEAR.finditer(line)
                      if int(m.group(1)) < TODAY.year - 1}
    for m in YEAR.finditer(line):
        if m.start(1) in stale_citation:
            continue  # an old statute's name, not a date being waited on
        out.append(datetime.date(int(m.group(1)), 1, 1))
    return out


def _horizon(text):
    """Every date `text` commits to, each as the last day it is still waiting."""
    return _dates(text)


def expired(line, today=None, context=None):
    """Return the year a waiting rule has outlived, or None.

    A rule is expired when every date it names has passed. If it names any
    future date it is still waiting for that one, which is the whole point of
    Bermuda's "until 2035" and North Carolina's 2027 penalty change.

    `context` covers the case that motivated the check and that a per-line pass
    cannot see. The UK guide's stale cells read "TBC -- HMRC publishes annually"
    with no year on them at all; the year is in the table header three rows up.
    Pass that header as context and its dates are used when the line has none.
    """
    today = today or TODAY
    if line.strip().startswith(SKIP_PREFIX):
        return None
    m = WAITING.search(line)
    if not m:
        return None
    if RESOLVED.search(line):
        return None              # a correction recording that the wait ended
    near = line[max(0, m.start() - WINDOW):m.end() + WINDOW]
    horizon = _horizon(near) or (_horizon(context) if context else [])
    if not horizon:
        return None              # no date to judge it by
    if any(d > today for d in horizon):
        return None              # still waiting for something that has not come
    return max(horizon).year


def selftest():
    """Four real expired rules, and the lines that must not be reported (one a known miss)."""
    today = datetime.date(2026, 9, 9)
    hits = [
        ('- **Never apply unconfirmed 2026 figures** - NEVER apply unconfirmed 2026 figures '
         '(BPC, MNIG, minimum wage, retirement ceiling) - use FY2025 values until 2026 values '
         'are published.', 2026),
        ('> **[RESEARCH GAP]** The next adjustment is expected July 2026 (under tripartite '
         'negotiation as of April 2026; not yet officially confirmed). Use the **PYG 2,899,048** '
         'figure as the current authoritative minimum; do not apply an unconfirmed 2026 figure.',
         2026),
        # no year on the cell itself; the header supplies it (see `context`)
        ('| Plan 1 | 9% | 24,990 | 26,065 | TBC -- HMRC publishes annually |', 2026),
        ('- **R-UK-SL-4 -- 2026-27 thresholds not yet published** - Trigger: a 2026-27 '
         'computation requires a threshold HMRC has not yet announced.', 2026),
    ]
    # month precision: the named month is not over, so it is still waiting
    assert expired('The next adjustment is expected September 2026; not yet published.',
                   today) is None, 'a named month is not expired until it ends'
    assert expired('The next adjustment was expected August 2026; not yet published.',
                   today) == 2026, 'the month before is expired'
    # a TBC cell that says "verify" rather than "publishes" is still a waiting rule
    assert expired('| Dividend allowance | GBP 500 | GBP 500 (TBC -- verify Finance Bill 2026) |',
                   today) == 2026
    header = '| Plan | Rate | 2024-25 Threshold | 2025-26 Threshold | 2026-27 Threshold |'
    for line, year in hits:
        got = expired(line, today, context=header)
        assert got == year, 'read %r, wanted %r, from: %s' % (got, year, line[:60])
    # the same cell with no header to lean on is unjudgeable, not a hit
    assert expired('| Plan 1 | 9% | 24,990 | 26,065 | TBC -- HMRC publishes annually |',
                   today) is None
    # a correction recording that the wait ended is not itself a waiting rule
    assert expired('> **Status as at September 2026:** NTA 2025 **commenced on 1 January 2026** '
                   'and is in force. Every "TBC -- verify under NTA 2025 implementing '
                   'regulations" marker in this pack predates commencement.', today) is None, \
        'a status note recording commencement is not a pending rule'
    assert expired('- **Surcharge on high income** - Finance Act 2026 abolished the surcharge '
                   'from 1 July 2026. This entry previously stated the 9%/10% split as the live '
                   'position, pending confirmation.', today) is None, \
        'a correction recording an abolition is not a pending rule'
    # but the uncorrected form of the same rule still reports
    assert expired('- **Surcharge on high income** - 9% salaried / 10% non-salaried; TBC, '
                   'confirm retention under Finance Act 2025.', today) == 2025, \
        'the rule before correction still reports'

    # a year inside a statute's name is not a date anything waits for
    assert expired('- **Pillar Two rules** - QDMTT, IIR and UTPR under Part 4A TCA 1997 '
                   '(Finance (No. 2) Act 2023) - filing requirements per Revenue guidance, '
                   'TBC; verify on revenue.ie before filing.', today) is None, \
        'TCA 1997 is a statute name, not a 1997 deadline'
    # A KNOWN MISS, kept as a test so it stays known. This line waits on the
    # Finance Act 2025 being gazetted, which happened in June 2025, so it is a
    # genuine expired rule. It is not reported: the only years within WINDOW of
    # the "TBC - confirm" phrase are 2001 and 2005, both suppressed as old
    # statute names, and the 2025 sits about ninety characters away at the head
    # of the line. Widening WINDOW to reach it would pull in unrelated years
    # from the same row, so the recall cost is accepted here and written down.
    assert expired('- **Finance Act 2025** - annual amendments to ITO 2001, STA 1990 and the '
                   'Federal Excise Act 2005 (TBC - confirm gazetted text).', today) is None, \
        'known miss: the year waited on is outside WINDOW'
    # the same rule with the Act next to the waiting phrase IS reported
    assert expired('- Annual amendments under ITO 2001 - TBC, confirm the Finance Act 2025 '
                   'gazetted text.', today) == 2025, \
        'a recent Act beside the waiting phrase is the thing waited on'
    assert expired('Verify against the current BKPM regulation and the Perpres 49/2021 annex; '
                   'mark as TBC where uncertain.', today) is None, \
        'a reference number like 49/2021 is not a deadline'
    # This one IS reported, and not because of the 2023 in the regulation
    # number -- that is suppressed. It is reported because "1 July 2024" is a
    # real month-year inside the window. That is a separate false-positive
    # class this check does not solve: a HISTORICAL EFFECTIVE DATE read as a
    # deadline. The docstring notes the same shape for "until". Left standing
    # rather than patched, because the phrasings that would suppress it also
    # suppress genuine "expected July 2026" hits.
    assert expired('Since 1 July 2024 (PMK 136/2023) the NIK functions as the NPWP; confirm '
                   'the kode billing position - TBC.', today) == 2024, \
        'reported on the 2024 effective date, not on the regulation number'

    clean = [
        # a future date means the rule is still doing its job
        '| Pay period in 2027 or later | Apply the 2026 constants and flag that they are last '
        "year's until the 2027 BPC decree is published; do not invent them. |",
        # statements of law that merely contain "until"
        'Tax Assurance Certificate guarantees this until 2035.',
        '- Band 0 - 14,000,000: 0% (until 2029)',
        # a permanent instruction with no date is not judgeable and not a defect
        'Do NOT invent rates -- flag every capital item for reviewer to apply the correct rate.',
        # trigger phrases restated in frontmatter are not guidance
        'description: Trigger on phrases like "April 2026 student loan threshold", "TBC".',
        # a correct instruction not to mix years, which is the opposite of the defect
        '- **2026 minimum wage warning** - Rises to EUR 780/month from 1 January 2026 - do NOT '
        'use the 2026 figure for a 2025 computation.',
        # "until confirmed" about the facts of a case, not about a pending publication
        '| Royalty cost-deduction class unknown | Use the lowest standard deduction (34%) until '
        'type confirmed | PwC income-determination |',
        # a worked example's answer key, not a forecast
        '**Input:** 2023 NTO = $500. 2024 NTO = $800. Expected 2025 NTO = $25,000.',
        # KNOWN MISS, kept here so the gap is not mistaken for coverage: this row
        # IS an expired rule and no pattern above catches it, because every
        # phrasing that would also catches the Latvia line two entries up.
        '| Pay period in 2026 or later | Apply **FY2025** values (BPC 6,576; ceiling 272,564) '
        'and flag; do not invent 2026 figures |',
    ]
    for line in clean:
        assert expired(line, today, context=header) is None, 'false positive on: %s' % line[:70]
    print('selftest: %d expired, %d not reported (1 of them a known miss)' % (len(hits), len(clean)))


HEADER = re.compile(r'^\s*\|.*\|\s*$')


def main(roots):
    hits = 0
    for root in roots:
        for dp, _, fns in os.walk(root):
            for fn in sorted(fns):
                if not fn.endswith('.md'):
                    continue
                p = os.path.join(dp, fn)
                context = None
                for i, line in enumerate(open(p, encoding='utf-8', errors='replace'), 1):
                    # Remember the last table row carrying a year: it is the
                    # header a dateless cell below it is speaking about.
                    if HEADER.match(line) and _horizon(line):
                        context = line
                    elif not line.strip().startswith('|'):
                        context = None
                    year = expired(line, context=context)
                    if year:
                        print('%s:%d  (waited on %d)\n    %s' % (p, i, year, line.strip()[:190]))
                        hits += 1
    print('\nrules that have outlived what they were waiting for:', hits)
    return hits


if __name__ == '__main__':
    if '--selftest' in sys.argv:
        selftest()
    else:
        sys.exit(1 if main([a for a in sys.argv[1:] if not a.startswith('-')] or ['skills']) else 0)
