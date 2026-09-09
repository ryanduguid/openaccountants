"""Flag a deadline rule that disagrees with the date beside it.

Guides state a deadline twice in one sentence: the rule, and what the rule
works out to for a calendar-year taxpayer. When the two disagree, one of them
is wrong and a reader cannot tell which.

    Greece   "Last working day of the sixth month after the tax year-end
              (15 July 2026 for FY2025 calendar-year companies)"
              Six months after 31 December is 30 June, not 15 July. AADE sets
              the date by annual decision, so the rule was the wrong half.

    Andorra  "Within 6 months of the close of the financial year (commonly
              filed in July for calendar-year companies)"
              Still open. Andorran sources repeat the same slippage, saying six
              months and then naming the end of July.

Both were found by reading. This finds them by arithmetic. The check assumes a
31 December year-end, which is the case the parenthetical is almost always
written for, and reports the rule, the date the rule implies, and the date the
guide gives.

It cannot tell which half is wrong. Greece's rule was wrong and its date right;
a jurisdiction that moved its deadline and updated only the prose would be the
other way round. Read the guide.

Usage: python3 scripts/check-deadline-rules.py [--selftest]
"""
import os, re, sys, calendar

MONTH_NAMES = ('January February March April May June July August September '
               'October November December').split()
MONTH = '|'.join(MONTH_NAMES)

WORDS = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6,
         'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12,
         'first': 1, 'second': 2, 'third': 3, 'fourth': 4, 'fifth': 5, 'sixth': 6,
         'seventh': 7, 'eighth': 8, 'ninth': 9, 'tenth': 10, 'eleventh': 11,
         'twelfth': 12}
NUM = r'(\d{1,2}|' + '|'.join(WORDS) + r')'

# "within 6 months of the close", "within four months after the year-end"
WITHIN = re.compile(r'\bwithin\s+%s\s+months?\s+(?:of|after|following|from)\b' % NUM, re.I)
# "last working day of the sixth month after the tax year-end"
LASTDAY = re.compile(r'\blast\s+(?:working\s+|business\s+)?day\s+of\s+the\s+%s'
                     r'(?:st|nd|rd|th)?\s+month\b' % NUM, re.I)
# "15th day of the 6th month after year-end", "25th day of the third month"
NTHDAY = re.compile(r'\b(\d{1,2})(?:st|nd|rd|th)\s+day\s+of\s+the\s+%s'
                    r'(?:st|nd|rd|th)?\s+month\b' % NUM, re.I)

DATE = re.compile(r'\b(\d{1,2})\s+(%s)\b|\b(%s)\s+(\d{1,2})\b' % (MONTH, MONTH))

# The arithmetic below assumes a 31 December year-end, so the line has to say
# it uses one. Without this the first run returned 43 hits and roughly 40 were
# a different year-end stated in the same sentence: Ethiopia counts four months
# from 7 July, Australian trusts two months from 30 June, and Hong Kong's
# BIR60 is due a month after ISSUE rather than after any year-end.
CALENDAR = re.compile(r'(?<!non-)calendar[- ]year|31 December year[- ]end', re.I)

# What the count runs from. Hong Kong's BIR60 is due "within 1 month of issue",
# which is a month after a piece of post arrives and not a month after anything
# this script can compute. The rule has to name a year-end to be checkable.
ANCHOR = re.compile(r'year[- ]?end|end of the (?:tax|financial|fiscal|accounting|income) year|'
                    r'close of|tax period|financial year|fiscal year|accounting year|'
                    r'year of (?:income|assessment)', re.I)


def _n(tok):
    """A count written as a numeral or a word."""
    tok = tok.lower()
    return int(tok) if tok.isdigit() else WORDS[tok]


def expected(line):
    """The (day, month) a rule implies for a 31 December year-end, or None.

    `day` is None where the rule says "within N months" or "last day", which
    both land on the end of the month rather than a stated day.
    """
    for pat, day_group in ((NTHDAY, 1), (LASTDAY, None), (WITHIN, None)):
        m = pat.search(line)
        if not m:
            continue
        if not ANCHOR.search(line[m.end():m.end() + 50]):
            continue            # the count runs from something else entirely
        months = _n(m.group(2 if day_group else 1))
        return (int(m.group(1)) if day_group else None), months
    return None


def stated(line):
    """The first calendar date in the line, as (day, month), or None."""
    m = DATE.search(line)
    if not m:
        return None
    g = m.groups()
    if g[0]:
        return int(g[0]), MONTH_NAMES.index(g[1].title()) + 1
    return int(g[3]), MONTH_NAMES.index(g[2].title()) + 1


def disagrees(line):
    """Return (rule, implied, given) where a rule and its own date differ."""
    if not CALENDAR.search(line):
        return None
    exp = expected(line)
    got = stated(line)
    if not exp or not got:
        return None
    day, month = exp
    if month != got[1]:
        pass                      # different month, always a disagreement
    elif day is None:
        # "within N months" and "last day" mean the end of that month
        if got[0] >= calendar.monthrange(2026, month)[1]:
            return None
        # a date early in the right month still disagrees with "last day"
    elif day == got[0]:
        return None
    implied = '%s %s' % ('end of' if day is None else day, MONTH_NAMES[month - 1])
    given = '%d %s' % (got[0], MONTH_NAMES[got[1] - 1])
    return implied, given


def selftest():
    """The two rules that were read by eye, and the two that are correct."""
    bad = [
        ('- **Corporate income tax return deadline** - Last working day of the sixth month '
         'after the tax year-end (15 July 2026 for FY2025 calendar-year companies, per AADE)',
         'end of June', '15 July'),
        ('- **IS filing deadline** - Within 6 months of the close of the financial year '
         '(commonly filed by 31 July for calendar-year companies via Model 200)',
         'end of June', '31 July'),
    ]
    for line, implied, given in bad:
        got = disagrees(line)
        assert got == (implied, given), 'missed %r: got %r' % (line[:50], got)
    ok = [
        # 15th day of the 6th month is 15 June, and the guide says 15 June
        '- **Annual corporate income tax return deadline** - 15th day of the 6th month after '
        'year-end (15 June for calendar-year companies)',
        # 25th day of the third month is 25 March, and the guide says 25 March
        '- **Annual corporate income tax return deadline** - By the 25th day of the third '
        'month following the tax period (i.e. 25 March for calendar-year taxpayers)',
        # "within 4 months" lands on the end of April, and 30 April is the end of April
        '| **Filing deadline** | **30 April** of the year following the tax year (or 4 months '
        'after fiscal year-end if non-calendar) |',
        # a rule with no date beside it is nothing to check
        '- **Final self-assessment return deadline** - Within 6 months after the end of the '
        'accounting year',
        # a non-calendar year-end stated in the line: four months from 7 July
        '- **Annual income tax return deadline (companies)** - Within 4 months of the end of '
        'the tax year (i.e. by 7 November for an 8 July-7 July year)',
        # "within 1 month of ISSUE" is not counted from a year-end at all
        '- **Salaries Tax filing** - BIR60 due within 1 month of issue (typically by 2 May for '
        'standard calendar-year cases)',
    ]
    for line in ok:
        assert disagrees(line) is None, 'false positive on: %s' % line[:60]
    print('selftest: %d disagreements, %d clean' % (len(bad), len(ok)))


def main():
    hits = 0
    for dp, _, fns in os.walk('skills'):
        for fn in sorted(fns):
            if not fn.endswith('.md'):
                continue
            p = os.path.join(dp, fn)
            for i, line in enumerate(open(p, encoding='utf-8', errors='replace'), 1):
                d = disagrees(line)
                if d:
                    print('%s:%d\n    rule implies %s, guide says %s\n    %s'
                          % (p, i, d[0], d[1], line.strip()[:150]))
                    hits += 1
    print('rules disagreeing with the date beside them:', hits)
    return hits


if __name__ == '__main__':
    if '--selftest' in sys.argv:
        selftest()
    else:
        main()
