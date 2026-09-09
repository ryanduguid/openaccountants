#!/usr/bin/env python3
"""Find dated statements that may still describe a past event as forthcoming.

Matches anticipatory wording with named dates or bare commencement years.
Skips provenance and lines with future dates. A past proposed start date does
not establish enactment; every hit needs source review.

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
    # Proposals with past intended dates need review; they may remain proposals.
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
