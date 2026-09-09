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

Precision is low by design: it flags roughly 100 lines to surface a handful. The
dominant false positive is provenance — "current as of April 2026",
"research-verified ... as of May 2026" — which is excluded here, but anything
that legitimately discusses a past year's anticipated change will still appear.
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

FUTURE = re.compile(
    r'\b(will\s+(?:be|commence|apply|take\s+effect|rise|increase|change|start|come\s+into)'
    r'|commences?\b|is\s+expected|are\s+expected|expected\s+to|upcoming\b|forthcoming\b'
    r'|pending\b|not\s+yet\b|awaiting\b|once\s+enacted|when\s+enacted|until\s+Royal\s+Assent'
    r'|to\s+be\s+confirmed|TBC\b|due\s+to\s+(?:commence|start|take\s+effect))', re.I)

# provenance and currency statements are not predictions
PROVENANCE = re.compile(r'(current(?:ity)?\s+as\s+of|as\s+of\s+(?:this|the)\s+skill|'
                        r'research-verified|verified\s+against|currency\s+date|'
                        r'last\s+(?:updated|reviewed)|sources?\s+(?:current|as\s+of)|'
                        r'^\s*[-*]?\s*\*\*v\d)', re.I)


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
                for m in DATE.finditer(line):
                    d = parse(m)
                    if d and d < today:
                        print('%s:%d  (says %s, which was %d days ago)\n    %s'
                              % (p, ln, d.isoformat(), (today - d).days, line.strip()[:170]))
                        hits += 1
                        break
    print('anticipatory statements about a date now past:', hits)


main()
