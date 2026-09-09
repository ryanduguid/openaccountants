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

What a full run returns now that those four are fixed: 37 lines, and they are
leads rather than defects. Most are genuinely pending -- Nigeria waiting on the
NTA 2025 implementing regulations, Morocco on the e-invoicing decree, Pakistan
on several 2026 items -- and each needs someone to go and look rather than a
recompute. Two UK guides are waiting on a Scottish Budget and on Finance Bill
enactment, which are the same shape and worth taking next.

The check earned its keep before it was finished. Run against the UK student
loan guide immediately after that guide was fixed, it found a second copy of the
same threshold table two hundred lines further down, still reading TBC in all
five cells, plus a refusal code and a sensitivity test built on the same
placeholder. The first fix had been to the table a reader sees first.

Exit status is 1 when anything is reported, so this can gate CI once the
standing queue is worked down.

Usage: python3 scripts/check-expired-rules.py [--selftest] [path ...]
"""
import os, re, sys, datetime

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
    r'\bTBC\b[^.|\n]{0,40}?\b(?:publish|announce|confirm|pending|await)|'
    r'\b(?:publish|announce|confirm|pending|await)\w*[^.|\n]{0,40}?\bTBC\b|'
    r'until\b[^.|\n]{0,60}?\b(?:published|announced|available|released|issued)\b|'
    r'pending (?:HMRC|IRS|FTB|SLC|MTESS|BPS|DGI|SIN|ATO|publication|announcement|confirmation)|'
    r'(?:expected|anticipated)\b[^.|\n]{0,50}?'
    r'\b(?:adjustment|publication|decree|regulation|announcement|revision|update|uprating)\b|'
    r'\b(?:adjustment|publication|decree|regulation|announcement|revision|update|uprating)\b'
    r'[^.|\n]{0,50}?\b(?:is |are )?(?:expected|anticipated)\b',
    re.I)

# How far from the waiting phrase a date has to be to be about it.
WINDOW = 60

# The date the rule is waiting on.
YEAR = re.compile(r'\b((?:19|20)\d{2})\b')
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
    """Every date the line commits to, as (date, is_month_precise)."""
    out = []
    for m in MONTH_YEAR.finditer(line):
        out.append((datetime.date(int(m.group(2)), MONTHS.index(m.group(1).title()) + 1, 1), True))
    for m in YEAR.finditer(line):
        out.append((datetime.date(int(m.group(1)), 1, 1), False))
    return out


def _horizon(text):
    """Every date `text` commits to."""
    return [d for d, _ in _dates(text)]


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
    header = '| Plan | Rate | 2024-25 Threshold | 2025-26 Threshold | 2026-27 Threshold |'
    for line, year in hits:
        got = expired(line, today, context=header)
        assert got == year, 'read %r, wanted %r, from: %s' % (got, year, line[:60])
    # the same cell with no header to lean on is unjudgeable, not a hit
    assert expired('| Plan 1 | 9% | 24,990 | 26,065 | TBC -- HMRC publishes annually |',
                   today) is None
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
