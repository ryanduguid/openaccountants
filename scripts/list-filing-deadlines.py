"""List each jurisdiction's stated annual return deadline, so it can be checked.

The companion to `list-vat-rates.py`, for the field that costs a penalty rather
than a wrong number. `check-filing-deadlines.py` finds a form a jurisdiction
dates two ways; it cannot find a deadline every guide agrees on and that is
simply wrong. This dumps the claim so a human can compare it against the outside
world.

Anchored on the label rather than the form number. `check-filing-deadlines.py`
requires a form name and a date on one line, which reaches 70 of 241
jurisdiction folders. Most guides write the deadline against a label instead --
"**Annual personal income tax return deadline** -- Before 31 March" -- so that
is what this reads.

Personal and corporate deadlines differ in most jurisdictions and are kept
apart. A deadline stated as a rule rather than a date ("15th day of the 6th
month after year-end") is reported as written, because normalising it would
throw away the part a reader needs.

CAUTION, and it is specific to this field. Many of these lines already cite
PwC's *Tax administration* page as their source. Comparing them back to PwC
confirms the drafting, not the law, and will report clean whether or not the
deadline has since moved. Prefer the tax authority's own filing-season page for
any jurisdiction whose provenance names an aggregator.

It also cannot tell an assertion from a warning about one. A guide that says
"30 June is not the filing deadline" reads here as a guide claiming 30 June,
and the Italy correction produced exactly that until the sentence was reworded.
A row that disagrees with itself may be a guide arguing with a date rather than
stating one, so read the line before you act on it.

Usage: python3 scripts/list-filing-deadlines.py [--selftest]
"""
import os, re, sys, collections

MONTH = ('January|February|March|April|May|June|July|August|September|'
         'October|November|December')

# The label. A bare "return" was tried first and had to go: it matched sales,
# payroll and withholding returns, which put Australia's BAS and PAYG dates in
# the same column as its individual return and made seven benign rows look like
# a disagreement. The return must be named as annual or as an income tax return.
LABEL = re.compile(
    r'\b(?:annual\s+(?:income\s+)?(?:tax\s+)?return|'
    r'(?:income|profits?)\s+tax\s+return)\b'
    r'[^|\n]{0,40}?\b(deadline|due date|due|filing date|filed by|lodge by)\b', re.I)

DATE = re.compile(r'\b(\d{1,2})\s+(%s)\b|\b(%s)\s+(\d{1,2})\b' % (MONTH, MONTH))

# A deadline expressed as a rule off the year-end rather than a calendar date.
RULE = re.compile(r'\b(\d{1,2})(?:st|nd|rd|th)?\s+(day|month|days|months)\b'
                  r'[^|\n]{0,60}?\b(year[- ]end|following|after|close)\b', re.I)

# A bare deadline label, accepted only inside a file whose slug already says
# which return it is. Australia writes "| Filing deadline | 31 October 2025
# (self-lodged) |" in au-individual-return.md and never repeats the word
# "return" on the line; requiring it on the line lost Australia, the UK,
# Ireland and Canada altogether.
BARE = re.compile(r'\b(filing deadline|lodgment deadline|lodgement deadline|'
                  r'filing due date|self-lodge deadline|return deadline)\b', re.I)
SLUG = re.compile(r'(individual|personal|income-tax|corporate-tax|company-tax|'
                  r'corporate-income-tax|tax-return|return)', re.I)

# A parenthetical naming the year-end, which qualifies the label rather than
# giving the deadline. Madagascar files "(30 June year-end) -- 15 November" and
# was reported as filing on 30 June.
YEAREND = re.compile(r'\([^()]*year[- ]end[^()]*\)', re.I)

# A trailing source citation in the house _( ... )_ form.
CITE = re.compile(r'_\([^)]*\)_\s*$')

# "between 1 March and 30 June", "1 April - 30 June", "15 March to 15 July".
_D = r'(?:\d{1,2}\s+(?:%s)|(?:%s)\s+\d{1,2})' % (MONTH, MONTH)
WINDOW = re.compile(r'\b(?:between\s+)?(%s)\s*(?:and|to|[-\u2013\u2014])\s*(%s)\b' % (_D, _D), re.I)

PERSONAL = re.compile(r'\b(individual|personal|employee|self[- ]employed)\b', re.I)
CORPORATE = re.compile(r'\b(corporate|company|companies|corporation|CIT|profits tax)\b', re.I)


def kind(line, slug=''):
    """Which tax the deadline belongs to, from the line, then from the filename."""
    for text in (line, slug.replace('-', ' ')):
        if CORPORATE.search(text):
            return 'corporate'
        if PERSONAL.search(text):
            return 'personal'
    return 'unspecified'


def _spell(match):
    """Render a DATE match day-first, whichever way the guide wrote it."""
    g = match.groups()
    return '%s %s' % (g[0], g[1]) if g[0] else '%s %s' % (g[3], g[2])


def deadline_in(line, slug=''):
    """Return (kind, stated deadline) for a line that states one, else None.

    The date wins over the rule when a line carries both, because
    "15th day of the 6th month after year-end (15 June for calendar-year
    companies)" is more useful read as 15 June.
    """
    # The house style ends a bullet with its source in _( ... )_, and those
    # carry dates. Monaco cites "Sovereign Ordinance no. 3.152 of 19 March
    # 1964" and was reported as filing on 19 March.
    line = YEAREND.sub(' ', CITE.sub(' ', line))
    m = LABEL.search(line)
    if not m and slug and SLUG.search(slug):
        m = BARE.search(line)
    if not m:
        return None
    tail = line[m.end():]
    text = tail if DATE.search(tail) else line
    # A window names its opening first. Bulgaria files "between 1 March and
    # 30 June" and only the second date is the deadline.
    w = WINDOW.search(text)
    if w:
        return kind(line, slug), _spell(DATE.match(w.group(2)) or DATE.search(w.group(2)))
    d = DATE.search(text)
    if d:
        return kind(line, slug), _spell(d)
    r = RULE.search(tail)
    if r:
        return kind(line, slug), r.group(0).strip()[:48]
    return None


def selftest():
    """Assert the reader still finds the deadline shapes it was built from.

    Every case below is a real line from the corpus. The last two are the ones
    that matter: a line that states a rule rather than a date, and a line that
    states both, where reading the rule instead of the date loses the answer a
    filer needs.
    """
    cases = [
        ('- **Annual personal income tax return deadline** - Before 31 March of the '
         'year following the fiscal year', 'personal', '31 March'),
        ('| Annual return deadline (self-lodged) | 28 February of the following year |',
         'unspecified', '28 February'),
        ('| FBiH/RS annual return deadline | 31 March | PwC, *Tax administration* |',
         'unspecified', '31 March'),
        # US guides write "May 15"; every date comes back day-first so the
        # column can be compared without minding which house style wrote it.
        ("- **Filing deadline** - Louisiana's individual income tax return deadline "
         'is May 15 (not April 15).', 'personal', '15 May'),
        ('- **Annual return filing deadline** - 31 May of the year following the tax year',
         'unspecified', '31 May'),
        ('| Annual corporate income tax return deadline | By the 25th day of the third '
         'month following the tax period |', 'corporate', None),
        ('- **Annual corporate income tax return deadline** - 15th day of the 6th month '
         'after year-end (15 June for calendar-year companies)', 'corporate', '15 June'),
    ]
    for line, want_kind, want in cases:
        got = deadline_in(line)
        assert got is not None, 'read no deadline from: %s' % line
        k, stated = got
        assert k == want_kind, 'wrong tax for %r: got %r, want %r' % (line, k, want_kind)
        if want is not None:
            assert stated == want, 'wrong deadline for %r: got %r, want %r' % (
                line, stated, want)
        else:
            assert not DATE.search(stated), (
                'expected a rule, got a calendar date %r from: %s' % (stated, line))
    # a year-end inside the label is not the deadline
    assert deadline_in('- **CIT return filing deadline (30 June year-end)** - 15 November',
                       'mg-corporate-income-tax') == ('corporate', '15 November')
    # a window names its opening first; the deadline is the far end
    # "Annual CIT return deadline" reaches the reader through the bare label,
    # since LABEL spells out income/tax and not every acronym in between.
    assert deadline_in('- **Annual CIT return deadline** - Between 1 March and 30 June of the '
                       'year following the tax year',
                       'bg-corporate-income-tax') == ('corporate', '30 June')
    # a date inside the trailing source citation is not a deadline
    mc = ('- **ISB return filing deadline** - Annual return due within 3 months of the financial '
          'year-end  _(Sovereign Ordinance no. 3.152 of 19 March 1964)_')
    got = deadline_in(mc, 'mc-corporate-income-tax')
    assert got and '19 March' not in got[1], 'read the citation date as a deadline: %r' % (got,)
    # a bare label counts only inside a file whose slug names the return
    au = '| Filing deadline | 31 October 2025 (self-lodged); May 2026 (tax agent) |'
    assert deadline_in(au, 'au-individual-return') == ('personal', '31 October')
    assert deadline_in(au) is None, 'a bare label must not count without file context'
    # an instalment line is not an annual return deadline
    assert deadline_in('Each instalment equals one-quarter of the lesser amount, '
                       'due 15 June.') is None
    print('selftest: %d cases pass' % len(cases))


def main():
    out = collections.defaultdict(lambda: collections.defaultdict(collections.Counter))
    for dp, _, fns in os.walk('skills'):
        for fn in sorted(fns):
            if not fn.endswith('.md'):
                continue
            p = os.path.join(dp, fn)
            parts = p.split(os.sep)
            if len(parts) < 3:
                continue
            # skills/international/<jur>/x.md is a jurisdiction; skills/federal/x.md
            # is one too, and taking parts[2] blindly filed it under its own
            # filename. `us-pte-state-matrix.md` appeared as a country.
            jur = parts[2] if len(parts) >= 4 else parts[1]
            for line in open(p, encoding='utf-8', errors='replace'):
                got = deadline_in(line, fn[:-3])
                if got:
                    out[jur][got[0]][got[1]] += 1

    for juris in sorted(out):
        for k in ('personal', 'corporate', 'unspecified'):
            counts = out[juris].get(k)
            if not counts:
                continue
            flag = '  <-- guides disagree' if len(counts) > 1 else ''
            print('%-26s %-12s %s%s' % (
                juris, k, ', '.join('%s (%d)' % (d, n) for d, n in counts.most_common()),
                flag))
    print('jurisdictions stating an annual return deadline:', len(out))


if __name__ == '__main__':
    if '--selftest' in sys.argv:
        selftest()
    else:
        main()
