#!/usr/bin/env python3
"""Find guides that still describe as forthcoming something that has already happened.

A tax corpus ages in a particular way. A rate written before it took effect is
phrased in the future — "commences 1 July 2026", "TBC pending Royal Assent",
"expected to rise" — and once that date passes the sentence becomes false while
every number in it stays right. No rate check sees this, because there is no
wrong rate: the defect is the tense.

Two real errors were found this way:

  * au-super-guarantee (agent-skills) said payday super "commences 1 July 2026"
    and gave quarterly deadlines and an 11.5% SG rate. We are past that date:
    payday super is in force, the rate is 12%, and the ATO Small Business Super
    Clearing House it pointed at has closed.
  * uk-income-tax-sa100 held the 2026-27 savings and property rates open as "TBC
    pending Finance Bill enactment" in four places while its own rate table two
    sections earlier already carried the settled answer — the file contradicted
    itself. The agent-skills copy also had the additional rate as 45%, not 47%.

**Two gaps that let a real error through, found by hitting it by hand.** Taiwan
called its 15% alternative minimum tax for large multinational groups "proposed
... from 2025" in two guides. It was announced in August 2024, took effect on
1 January 2025 and first appeared in returns filed in 2026, so the rate and the
date were both right and the word "proposed" was the error. This checker could
not see it twice over:

  * "proposed" was not anticipatory language here. Nor were "proposal",
    "planned", "slated" or "scheduled to". All are now.
  * The date pattern required a month name, so "from 2025" was invisible while
    "from January 2025" was not. A bare year after from/effective/as of/starting
    is now read as 1 January of that year.

Both are in the selftest, because a vocabulary gap is silent and this one hid a
rate a reader would decline to apply.

Precision is low by design: it flags roughly 100 lines to surface a handful.
Two false-positive classes are excluded. Provenance is one — "current as of
April 2026", "v2.0, rewritten April 2026. Awaiting validation" — and it is the
larger. The other was introduced by the bare-year change and had to be closed
straight away: a line naming a past enactment and a future commencement, like
"Royal Assent 26 June 2026 is LAW: from 1 July 2027 the CGT discount is
reduced". That line is anticipating 2027, and flagging the assent date says it
is stale when it is exactly current. Any line carrying a date still ahead is
skipped for that reason.

Together those took the corpus from 79 hits to 107: 24 of the original 79 were
provenance or prospective statements now correctly suppressed, and 52 new
candidates appeared. Every one of the 24 was read before being suppressed and
none was an error.
Read each hit; a date in the past is not by itself an error.

Set the comparison date with --today YYYY-MM-DD (default: today).

Usage: python3 scripts/check-stale-futures.py [--today YYYY-MM-DD] [dir ...]
Exit status is always 0: this is a review aid, not a gate.
"""
import datetime, glob, os, re, signal, sys

try:
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
except (AttributeError, ValueError):
    pass

MONTHS = ('january february march april may june july august september october '
          'november december').split()
MRE = '|'.join(MONTHS)
DATE = re.compile(r'\b(\d{1,2})\s+(%s)\s+(\d{4})\b|\b(%s)\s+(\d{4})\b' % (MRE, MRE), re.I)

# A commencement can name a year and no month. Taiwan's alternative minimum tax
# read "a 15% rate is proposed for in-scope MNE groups ... from 2025", a
# prediction about a year that has since arrived, and the month-only pattern
# above could not see it. Read as 1 January of the year named.
BAREYEAR = re.compile(r'\b(?:from|effective|as\s+of|starting|commencing|'
                      r'with\s+effect\s+from)\s+(20\d\d)\b', re.I)

FUTURE = re.compile(
    r'\b(will\s+(?:be|commence|apply|take\s+effect|rise|increase|change|start|come\s+into)'
    r'|commences?\b|is\s+expected|are\s+expected|expected\s+to|upcoming\b|forthcoming\b'
    r'|pending\b|not\s+yet\b|awaiting\b|once\s+enacted|when\s+enacted|until\s+Royal\s+Assent'
    r'|to\s+be\s+confirmed|TBC\b|due\s+to\s+(?:commence|start|take\s+effect)'
    # A rate called "proposed" after it took effect is the same defect with no
    # number wrong. Taiwan's 15% MNE rate was law from 1 January 2025 and two
    # guides still called it a proposal; a reader does not apply a proposed rate.
    r'|proposed\b|proposal\b|planned\b|slated\b|scheduled\s+to'
    r'|set\s+to\s+(?:rise|increase|change|apply|take))', re.I)

# provenance and currency statements are not predictions
PROVENANCE = re.compile(r'(current(?:ity)?\s+as\s+of|as\s+of\s+(?:this|the)\s+skill|'
                        r'research-verified|verified\s+against|currency\s+date|'
                        r'last\s+(?:updated|reviewed)|sources?\s+(?:current|as\s+of)|'
                        r'^\s*[-*]?\s*\*\*v\d|status\s+as\s+of|validation\s+date|'
                        r'awaiting\s+validation|drafted\s+\w+\s+20\d\d|'
                        r'rewritten\s+in\s+\w+\s+20\d\d|this\s+(?:file|skill)\s+is\s+v\d)', re.I)


def parse(m):
    if m.group(3):
        d, mo, y = int(m.group(1)), m.group(2), int(m.group(3))
    else:
        d, mo, y = 28, m.group(4), int(m.group(5))
    try:
        return datetime.date(y, MONTHS.index(mo.lower()) + 1, d)
    except ValueError:
        return None


def main():
    argv = sys.argv[1:]
    today = datetime.date.today()
    if '--today' in argv:
        i = argv.index('--today')
        today = datetime.date(*map(int, argv[i + 1].split('-')))
        del argv[i:i + 2]
    roots = argv or ['skills']

    hits = 0
    for root in roots:
        for p in sorted(glob.glob(os.path.join(root, '**', '*.md'), recursive=True)):
            for ln, line in enumerate(open(p, encoding='utf-8', errors='replace'), 1):
                if not FUTURE.search(line) or PROVENANCE.search(line):
                    continue
                dates = [parse(m) for m in DATE.finditer(line)]
                dates += [datetime.date(int(y), 1, 1) for y in BAREYEAR.findall(line)]
                dates = [d for d in dates if d]
                # A line carrying a future date is anticipating that one. Royal
                # Assent on 26 June 2026 for a change effective 1 July 2027 is
                # not stale, and flagging the enactment date says it is.
                if any(d >= today for d in dates):
                    continue
                for d in dates:
                    if d < today:
                        print('%s:%d  (says %s, which was %d days ago)\n    %s'
                              % (p, ln, d.isoformat(), (today - d).days, line.strip()[:170]))
                        hits += 1
                        break
    print('anticipatory statements about a date now past:', hits)



def selftest():
    """The two gaps that hid Taiwan, and two lines that must not fire."""
    today = datetime.date(2026, 9, 9)
    tw = ('- **Corporate Income Basic Tax (AMT)** - 12% standard rate (a 15% rate is proposed '
          'for in-scope MNE groups under the OECD global minimum tax from 2025 - confirm)')
    assert FUTURE.search(tw), '"proposed" is anticipatory language'
    assert [int(y) for y in BAREYEAR.findall(tw)] == [2025], \
        'a commencement can name a year and no month'
    prov = '- **Provenance** - research-verified against PwC as of May 2026'
    assert PROVENANCE.search(prov), 'provenance is not a prediction'
    mixed = ('Treasury Laws Amendment Act 2026 (Royal Assent 26 June 2026) is LAW: from '
             '1 July 2027 the 50% CGT discount is reduced')
    ds = [parse(m) for m in DATE.finditer(mixed)]
    ds += [datetime.date(int(y), 1, 1) for y in BAREYEAR.findall(mixed)]
    assert any(d and d >= today for d in ds), \
        'a line with a future date is anticipating that one, not the enactment date'
    ahead = '- **MTD ITSA** - becomes mandatory from 2028 for the lowest band'
    assert not [y for y in BAREYEAR.findall(ahead) if datetime.date(int(y), 1, 1) < today], \
        'a date still ahead is not stale'
    print('selftest: 4 cases pass')


if '--selftest' in sys.argv:
    selftest()
else:
    main()
