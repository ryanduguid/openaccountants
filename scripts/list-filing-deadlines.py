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

Checked against an outside source so far (do not re-derive these from the
corpus). Eight jurisdictions, five wrong. Read that rate with care: these eight
were picked because their rows looked wrong, not at random, so it says the
leads were good, not that five in eight of the corpus is wrong.

  * Italy      WRONG on four counts. it-income-tax filed the Modello Redditi PF
               on 30 June, which is the payment date, and the Modello 730 on
               30 November, which is the second acconto. Filing is 31 October
               and 30 September. italy-formation dated the corporate Redditi SC
               to 30 November against a 9-month rule, italy-tax-optimization
               paid IRPEF on 16 June (that is IMU), and italy-crypto-tax
               deferred to 31 July where the surcharge date is 30 July.
               it-inps-contributions had 31 October right throughout.
  * Greece     WRONG. gr-income-tax filed individuals on 30 June; Greece files
               by 15 July on AADE's annual decision, extended to 24 July 2026
               for tax year 2025. The corporate guides stated a rule ("last
               working day of the sixth month") that yields 30 June and a
               worked date of 15 July in the same sentence.
  * Armenia    WRONG as a standing rule. am-tax-overview gave 1 November flat.
               That is the transitional window for tax year 2025; from tax year
               2026 it closes 1 July. armenia-income-tax had both.
  * Cyprus     WRONG, and not a date. cyprus-income-tax put the audited-accounts
               threshold at EUR 70,000 in one place and EUR 120,000 in another,
               both "from tax year 2026". Reform law N. 243(I)/2025 raised it to
               120,000. The 31 January deadline both places gave is right.
  * Finland    WRONG as a standing rule. fi-income-tax gave employees "mid-April
               (dates vary: 15, 22, or 29 April)", which is the previous
               season's set. The Tax Administration assigns one of four dates
               per taxpayer: 1, 14, 21 or 28 April 2026 for tax year 2025.
  * Bulgaria   CORRECT. "Between 1 March and 30 June" matches; the lister read
               the opening date until it was taught about windows.
  * Laos       CORRECT, and no longer hedged. 20 January for the profit tax
               return, 31 March for the financial statements, confirmed at PwC.
  * Monaco     CORRECT. "Within 3 months of the financial year-end". The
               19 March in its row came from the ordinance it cites, dated 1964.

Read but NOT checked outside the repo, and so not verified: Japan (15 March
income tax against 31 March consumption tax), the Netherlands (1 May, extending
to 1 September), India (31 July without an audit, 31 October with one), Saudi
Arabia (120 days), Madagascar, Nigeria, Kenya, Egypt, Macau, Lebanon, Papua New
Guinea, Namibia, Uganda, Kazakhstan, Ghana, Mongolia, Mexico, Vietnam, Qatar,
Mauritius, Cambodia, Argentina and Nicaragua. Each reads as a jurisdiction
stating two true things rather than contradicting itself, which is a reason not
to chase the row, not evidence the date is current.

Second tranche, drawn at random from the 149 international jurisdictions with a
row (seed 20260909), to get a rate the first eight could not give. Ten drawn,
ZERO errors:

  Afghanistan (3 months after a 20 March year-end), Bhutan 31 March, Burundi
  31 March, Costa Rica 15 March (16 March in 2026, the 15th being a Sunday),
  El Salvador 30 April, Indonesia 31 March for individuals and 30 April for
  companies, Lesotho 30 June against a 31 March year-end, Sierra Leone
  30 April on the 120-day rule, Tunisia 25 March for companies and 25 June for
  individuals, and Andorra's IRPF window of 1 April to 30 September.

So the field is in better shape than five in eight suggested, and the two
numbers together are the useful result: picking odd-looking rows found five
errors in eight, and drawing at random found none in ten. Chase the leads.

Open, and not counted against either tranche: Andorra's corporate deadline.
Both guides say "within 6 months of the close" and add "typically 31 July",
which cannot both hold for a calendar-year company, and both already hedge with
"(approx -- confirm exact statutory deadline)". Andorran sources repeat the same
slippage, saying six months and then naming the end of July. Settling it needs
Llei 95/2010 or the Departament de Tributs, so the hedge stays.

Third lead, and a different instrument. Grep the deadline lines for one that
names no year later than 2025, on the theory that Armenia and Finland had
frozen a season. 91 lines across 44 jurisdictions match and nearly all are
citation years or worked examples that state their own dates.

  * Australia  WRONG in au-return-assembly, which declares tax_year 2025, dates
               its BAS quarters correctly for the year ended 30 June 2026, and
               then gives the ITR deadline as 31 October 2025 and the tax agent
               window as March to May 2026. Both are a year early: 31 October
               2026 and 15 May 2027. au-individual-return declares tax_year 2024
               and its 31 October 2025 is right for that year, so it was given
               the rule instead of losing the date. Confirmed against the ATO
               lodgment program: 31 October self-lodged, 15 May by an agent
               engaged before 31 October.

Fourth lead, and the first one a script found rather than a reader.
scripts/check-deadline-rules.py does the arithmetic Greece and Andorra failed:
a guide states the rule and what the rule works out to for a calendar-year
taxpayer, so the two can be compared.

  * Norway     WRONG rule, right date, and it had said so. no-company-formation
               read "submitted to Regnskapsregisteret; deadline generally within
               6 months of year-end (31 July for calendar-year companies)
               ((confirm filing deadline))". Both dates are real and they belong
               to different steps: the general meeting approves the accounts
               within 6 months, so 30 June, and they must reach the register by
               31 July under Regnskapsloven section 8-2. The six-month rule was
               attached to the wrong step. Hedge resolved.

Fifth lead, borrowed from the threshold pass: look at the jurisdictions the
column does NOT contain. France, Portugal, Brazil and South Africa have no row
here, and all four had something to say.

  * Brazil        WRONG as a standing rule. br-income-tax leads with "Prazo da
                  DIRPF - 30 de maio do ano seguinte" while its own citation
                  says Receita Federal fixes the date each year by Instrucao
                  Normativa and names 30 May 2025 as that year's. The DIRPF 2026
                  window ran 23 March to 29 May 2026, shorter than the year
                  before. Third instance of a filing season frozen into a rule,
                  after Armenia and Finland.
  * South Africa  NOT WRONG, MISSING. za-income-tax names the return form as
                  ITR12 and never says when it is due, in a guide for filing it.
                  SARS sets the season annually: for the 2026 year of
                  assessment, auto-assessments 1 to 12 July 2026, manual filing
                  from 13 July, non-provisional deadline 23 October 2026, and
                  provisional taxpayers and trusts 22 January 2027. Added.
  * France        CORRECT. Declaration 2042 is due late May or early June,
                  staggered by departement, and the corporate declaration de
                  resultats within three months of year-end, four for a
                  31 December year-end.
  * Portugal      CORRECT. Modelo 22 by 31 May of the following year.

None of the four uses the wording this script looks for, so all four were
invisible to it before and two of them are invisible still. A jurisdiction
missing from the column is a question, not a pass.

Still open: 200 jurisdictions state a deadline and 24 have been checked.

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
# Which files may use a bare label. An allowlist of slugs was tried first and
# silently lost jurisdictions: mexico-crypto-tax and vietnam-pit both state
# "| Filing deadline | ... |" and matched none of individual/personal/income-tax,
# so Mexico and Vietnam had no deadline in the column at all. The list below
# names the guides that file a DIFFERENT return, and everything else is let
# through.
SLUG_BLOCK = re.compile(r'(vat|gst|sales-tax|payroll|withholding|paye|social|'
                        r'contribution|invoice|bookkeeping|estimated|instal|'
                        r'property|customs|excise|stamp|transfer-pricing|'
                        r'formation|financial-statement)', re.I)

# A parenthetical naming the year-end, which qualifies the label rather than
# giving the deadline. Madagascar files "(30 June year-end) -- 15 November" and
# was reported as filing on 30 June.
YEAREND = re.compile(r'\([^()]*year[- ]end[^()]*\)', re.I)

# A trailing source citation in the house _( ... )_ form.
CITE = re.compile(r'_\([^)]*\)_\s*$')

# "between 1 March and 30 June", "1 April - 30 June", "15 March to 15 July".
_D = r'(?:\d{1,2}\s+(?:%s)|(?:%s)\s+\d{1,2})' % (MONTH, MONTH)
# The dash may be doubled: the house style writes "1 April -- 30 September",
# and a single-character class read that as a bare "1 April" for Andorra.
WINDOW = re.compile(r'\b(?:between\s+)?(%s)\s*(?:and|to|[-\u2013\u2014]+)\s*(%s)\b' % (_D, _D), re.I)

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
    if not m and slug and not SLUG_BLOCK.search(slug):
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
    # the house style also writes the window with a doubled dash
    assert deadline_in('| Filing deadline | 1 April -- 30 September of the following year |',
                       'ad-income-tax') == ('unspecified', '30 September')
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
            # These folders carry many jurisdictions' dates on purpose, so they
            # always disagree with themselves and never mean anything by it.
            if jur in ('orchestrator', 'cross-border', 'verticals', 'integrations'):
                continue
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
