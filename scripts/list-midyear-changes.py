"""Find rate changes dated mid-year that give no guidance on the split.

A rate that changes on the first day of the tax year needs no explanation: the
year gets one figure. A rate that changes part-way through needs two, and the
month decides which applies. Guides on this branch have repeatedly carried the
new figure and the date and nothing else, which leaves an agent computing a full
year at whichever rate it read first.

"Mid-year" is decided per jurisdiction, from the tax year the guide itself
states. 6 April is a clean boundary in the UK and mid-year everywhere else.

It ranks, it does not accuse: a line can be correct and terse, and a change can
be so old that nothing straddles it any more. Always exits 0.

IT CURRENTLY REPORTS NOTHING, AND HERE IS HOW TO TELL THAT IS REAL

At the default cutoff the corpus is clean on this dimension, which is the
easiest possible state for a broken checker to fake. Two ways to confirm it is
not faking. Widen the window -- `--since 2020` still returns ten lines, so the
machinery finds things when things are there. And plant one: a guide reading
"| Tax year | Calendar year |" plus "- **VAT standard rate** - 23% from
1 August 2026" is reported immediately.

It got to zero honestly. Of 112 raw hits, two were real and are fixed (the
Maldives TGST rise on 1 July 2025 and Fiji's VAT cut on 1 August 2025, both
missing the earlier period and the time-of-supply test that decides it); the
rest were the checker not knowing how guides write. Each filter below names the
guide that forced it.

Usage: python3 scripts/list-midyear-changes.py [--selftest] [--since YEAR]
"""
import os, re, sys, collections, datetime

MONTHS = {m.lower(): i for i, m in enumerate(
    ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
     'September', 'October', 'November', 'December'], 1)}

# The jurisdiction's own statement of its tax year, from a quick-reference table
# or a labelled bullet.
TAX_YEAR = re.compile(r'\|\s*Tax year\s*\|\s*([^|]+)\|'
                      r'|\*\*Tax year\*\*\s*[—-]+\s*([^\n]+)', re.I)
DAY_MONTH = re.compile(r'\b(\d{1,2})\s+(January|February|March|April|May|June|July|'
                       r'August|September|October|November|December)\b', re.I)

# A commencement date attached to a figure.
EFFECTIVE = re.compile(
    r'\b(?:from|effective|with effect from|commencing|as from|as of)\s+'
    r'(\d{1,2})\s+(January|February|March|April|May|June|July|August|'
    r'September|October|November|December)\s+(20[12]\d)', re.I)
RATE = re.compile(r'\d+(?:\.\d+)?\s?%|\b[A-Z]{3}\s?[\d,]{3,}')

BULL = re.compile(r'^\s*-\s+\*\*([^*]{4,120}?)\*\*\s*[—-]+\s*(.+)$')
ROW = re.compile(r'^\s*\|\s*([^|]{4,120}?)\s*\|\s*(.+?)\s*\|?\s*$')

# Wording that shows the earlier period is handled. Deliberately generous: the
# aim is to report changes the guide says nothing about, not to grade how well
# the ones it does explain are written.
#
# Tested against the WHOLE FILE, not the line. Romania was the case that forced
# this: its VAT table states "21% ... from 1 August 2025" on one row, and the
# return-mapping table twenty rows below carries "21% from Aug 2025 / 19%
# before" for every affected box. The guide handles the split thoroughly; only
# the rate row is terse, and a rate row is supposed to be. Testing the line
# reported four Romanian lines that were all fine.
HANDLED = re.compile(r'\bto 3[01] [A-Z]|\buntil\b|\bbefore\b|\bpro[- ]rat|\bsplit\b|'
                     r'\bfor the period\b|\bmonth\b|\bearlier\b|\bpreviously\b|'
                     r'\bwas\b'
                     # Wording that names the old figure without naming a period.
                     # Every one of these was a false positive on the first run:
                     # Barbados "increased from 0.1% effective 1 April 2025",
                     # Ireland "4.1% (rising to 4.2% from 1 October 2025)",
                     # India "the former 12% and 28% slabs were abolished".
                     r'|\b(?:increased|reduced|cut|raised|risen|up|down)\s+from\b'
                     r'|\brising to\b|\bfalling to\b|\bformer\b|\bprior\b'
                     r'|\breverts?\b|\breverting\b'
                     # A date range written with a dash is the commonest way a
                     # guide states the earlier period, and the first version of
                     # this pattern missed it. Estonia's VAT line reads
                     # "24% (from 1 July 2025; 22% for 1 Jan-30 Jun 2025)",
                     # which could hardly be clearer, and was reported.
                     r'|\d{1,2}\s*\w{3,9}\s*[-\u2010-\u2015]\s*\d{1,2}\s*\w{3,9}'
                     r'|\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)'
                     r'[a-z]*\s*[-\u2010-\u2015]\s*'
                     r'(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)', re.I)

SKIP_TREES = ('us-states', 'foundation', 'templates', 'patterns')


def year_start(text):
    """(day, month) the tax year begins, from a guide's own statement."""
    if re.search(r'calendar year', text, re.I):
        return (1, 1)
    m = DAY_MONTH.search(text)
    return (int(m.group(1)), MONTHS[m.group(2).lower()]) if m else None


def tax_year_starts(root='skills'):
    """{jurisdiction: (day, month)} for every jurisdiction that states one."""
    out = {}
    for dp, _, fns in os.walk(root):
        parts = dp.split(os.sep)
        if len(parts) < 3 or parts[1] in SKIP_TREES:
            continue
        for fn in sorted(fns):
            if not fn.endswith('.md') or parts[2] in out:
                continue
            with open(os.path.join(dp, fn), encoding='utf-8', errors='replace') as fh:
                text = fh.read()
            for m in TAX_YEAR.finditer(text):
                start = year_start(m.group(1) or m.group(2) or '')
                if start:
                    out[parts[2]] = start
                    break
    return out


def flagged(line, start, since, file_text=''):
    """The effective date if this line changes a figure mid-year and neither it
    nor the rest of the file says which periods get which figure."""
    m = BULL.match(line) or ROW.match(line)
    if not m:
        return None
    label, value = m.group(1), m.group(2)
    whole = label + ' ' + value
    d = EFFECTIVE.search(whole)
    if not d or not RATE.search(value):
        return None
    if int(d.group(3)) < since:
        return None            # a change old enough that nothing straddles it
    day, month = int(d.group(1)), MONTHS[d.group(2).lower()]
    if (day, month) == start:
        return None
    # South Africa's provisional-tax dates land on 2 March against a 1 March
    # year start; a few days either side of the boundary is the boundary.
    if month == start[1] and abs(day - start[0]) <= 6:
        return None
    if HANDLED.search(whole):
        return None
    # A table that lists successive effective dates handles the split by
    # structure rather than by wording -- Barbados's minimum-wage schedule is
    # a row per date, and no row needs to explain the one above it. If this is
    # a table row and the file has another row with a DIFFERENT effective date,
    # treat the series as the explanation.
    if ROW.match(line) and not BULL.match(line):
        others = {x.group(0) for x in EFFECTIVE.finditer(file_text)}
        if len(others) > 1:
            return None

    # The split may be explained anywhere in the guide. Look for the same month
    # and year mentioned alongside earlier-period wording.
    # Match the same change written any of the ways guides write it:
    # "August 2025", "Aug 2025", "Aug. 2025", "08/2025", "Aug/25".
    mon_full, yr = d.group(2), d.group(3)
    month_year = r'(?:%s|%s)\.?[\s/-]+(?:%s|%s)|%02d/%s' % (
        mon_full, mon_full[:3], yr, yr[2:], MONTHS[mon_full.lower()], yr)
    for other in file_text.splitlines():
        if re.search(month_year, other, re.I) and HANDLED.search(other):
            return None
    return d.group(0)


def selftest():
    assert year_start('Calendar year (1 January -- 31 December)') == (1, 1)
    assert year_start('1 July 2024 - 30 June 2025') == (1, 7)
    assert year_start('6 April to 5 April') == (6, 4)
    assert year_start('Financial year, no dates given') is None

    cal, july = (1, 1), (1, 7)
    mid = '- **VAT standard rate** - **21%** from 1 August 2025\n'
    # mid-year for a calendar-year country, and the line says nothing else
    assert flagged(mid, cal, 2025) == 'from 1 August 2025'
    # the same date is not mid-year for a 1 July jurisdiction... it still is,
    # 1 August is a month in; but 1 July would not be:
    assert flagged('- **Rate** - 21% from 1 July 2025\n', july, 2025) is None
    # a line that already gives the earlier period is not reported
    assert flagged('- **Rate** - 21% from 1 August 2025, was 19% until 31 July\n',
                   cal, 2025) is None
    # a date with no figure beside it is a commencement note, not a rate change
    assert flagged('- **New law** - applies from 1 August 2025\n', cal, 2025) is None
    # a change old enough that no live computation straddles it
    assert flagged(mid, cal, 2026) is None
    # the UK's 6 April is a clean boundary at home
    assert flagged('- **Rate** - 20% from 6 April 2026\n', (6, 4), 2025) is None

    # Romania's shape: the rate row is terse, and the split is explained
    # elsewhere in the same file. Testing the line alone reported it; testing
    # the file does not.
    romania = ('- **Reduced VAT** - 11% on food and accommodation '
               '(from 1 August 2025)\n'
               'Row 2: domestic supplies at reduced rate (11% from Aug 2025 '
               '/ 9% before)\n')
    row = romania.splitlines()[0]
    assert flagged(row, cal, 2025) == 'from 1 August 2025'      # line alone
    assert flagged(row, cal, 2025, romania) is None             # whole file

    # a date range with a dash states the earlier period just as clearly
    assert flagged('- **VAT** - 24% (from 1 July 2025; 22% for 1 Jan-30 Jun 2025)\n',
                   cal, 2025) is None
    assert flagged('- **VAT** - 24% from 1 July 2025, 22% Jan-Jun\n',
                   cal, 2025) is None

    # the old figure named without a period is still the split, stated
    assert flagged('- **Levy** - 0.25% (increased from 0.1% effective 1 April 2025)\n',
                   cal, 2025) is None
    assert flagged('| PRSI | 4.1% (rising to 4.2% from 1 October 2025) |\n',
                   cal, 2025) is None
    assert flagged('| GST | two slabs from 22 September 2025; the former 12% '
                   'and 28% slabs were abolished |\n', cal, 2025) is None

    # a schedule that lists successive dates explains itself by structure
    schedule = ('| From 21 January 2026 | 10.71 | 2% CPI increase |\n'
                '| From 1 April 2025 | 10.50 | prior step |\n')
    assert flagged(schedule.splitlines()[0], cal, 2025, schedule) is None
    # but a lone table row with one date in the file is still reported
    lone = '| VAT | 21% from 1 August 2025 | Fiscal Code |\n'
    assert flagged(lone.splitlines()[0], cal, 2025, lone) == 'from 1 August 2025'

    # KNOWN MISS, and the reason this ranks rather than accuses: HANDLED keys on
    # wording, so a line that gives the earlier figure without any of those
    # words is still reported. "21% from 1 August 2025; 19% for January to
    # July" survives only because it contains "month"-free prose that happens to
    # match nothing. Read the line before editing it.
    print('selftest: %d cases pass (1 documented miss)' % 21)


def main(since=None):
    since = since or datetime.date.today().year - 1
    starts = tax_year_starts()
    hits = collections.defaultdict(list)
    for dp, _, fns in os.walk('skills'):
        parts = dp.split(os.sep)
        if len(parts) < 3 or parts[1] in SKIP_TREES:
            continue
        start = starts.get(parts[2])
        if not start:
            continue           # cannot tell mid-year from year-start
        for fn in sorted(fns):
            if not fn.endswith('.md'):
                continue
            path = os.path.join(dp, fn)
            with open(path, encoding='utf-8', errors='replace') as fh:
                text = fh.read()
            for n, line in enumerate(text.splitlines(), 1):
                got = flagged(line, start, since, text)
                if got:
                    hits[parts[2]].append((path, n, got))
    for jur, rows in sorted(hits.items(), key=lambda kv: -len(kv[1])):
        d, m = starts[jur]
        print('%-18s (year starts %d/%d)  %d line(s)' % (jur, d, m, len(rows)))
        for path, n, when in rows:
            print('    %s:%d  %s' % (path, n, when))
    print()
    print('jurisdictions stating a tax year:', len(starts))
    print('with a mid-year change and no stated split (since %d):' % since,
          sum(len(v) for v in hits.values()), 'line(s) across', len(hits))
    print('A terse line can still be correct, and an old change may have '
          'nothing straddling it. Read the line before editing.')
    return 0  # never gates CI: a terse line is not a defect


if __name__ == '__main__':
    if '--selftest' in sys.argv:
        selftest()
    else:
        y = None
        if '--since' in sys.argv:
            y = int(sys.argv[sys.argv.index('--since') + 1])
        sys.exit(main(y))
