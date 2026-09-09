#!/usr/bin/env python3
"""Find jurisdictions whose guides disagree on the CURRENT STANDARD corporate rate.

Written to replace a scratchpad rate dump that I misread. That dump grepped every
"corporate ... tax ... rate ... N%" line in a jurisdiction and counted the distinct
values; ten jurisdictions came back with two, and I reported ten internal
contradictions. There were none. Every one was a second rate that is correct and
sits in the same file as the first:

  * a SECTOR rate            -- Iraq 15% standard / 35% oil & gas; Qatar 10% / 35%
                                oil and gas; Turkey 25% / 30% financial sector;
                                Guinea 25% / 30% mining; Sri Lanka 30% / 40%
                                betting, gaming and liquor
  * a BAND                   -- Slovakia 10% to EUR 100k, 21% to EUR 5m, 24% above
  * a TAXPAYER CLASS         -- Philippines 25% regular / 20% qualifying MSMEs
  * a FUTURE rate            -- Bhutan 30% for 2025, 22% from 1 January 2026
  * a HISTORICAL rate        -- Rwanda 28%, cited as "reduced from 30% effective 2025"
  * a LEVY ON THE TAX        -- Zimbabwe 25% corporate, 3% AIDS levy on tax payable

So the check has to read the label and the qualifier, not just the number. A line
counts as stating the current standard rate only when the label says standard,
headline, regular or main WITHOUT a sector, size, band or year qualifier, and the
qualifier text does not scope it to a sector, a band, a class or another year.

Result when written: of 100 jurisdictions stating a standard-labelled corporate
rate, 82 state it unqualified, and **none** disagree with itself -- on the
unqualified rate or on the first rate stated in any standard-labelled line. The
ten "contradictions" were all mine.

Two bugs in this script had to be fixed before that number meant anything, and
both were the same error the script exists to catch -- reading a number without
its context:

  * the trailing `_( ... )_` source citation was tested as if it were a scope
    qualifier, so every rate whose statute has a year in its name ("Llei 95/2010",
    "Act No. 586/1992 Coll.") was skipped as year-scoped. 44 jurisdictions tested
    instead of 70.
  * the percentage regex matched `25%` but not `25 percent`, so on "25 percent
    (before 3% AIDS levy on tax)" it returned 3, on "28 percent (Reduced from
    30%...)" it returned 30, and on "25 percent (reduced to 20% for MSMEs)" it
    returned 20 -- Zimbabwe, Rwanda and the Philippines reported as disagreeing
    when all three agree exactly.

Everything it skips is listed under --show-skipped, because the skip list is where
a real contradiction would hide: a guide that states a wrong rate as its standard
one is caught, but a guide that states a wrong SECTOR rate is not, and this cannot
find a rate that every guide in the jurisdiction agrees on and that is wrong --
that needs an outside source, which is what list-vat-rates.py exists to feed.

Usage: python3 scripts/check-headline-cit.py [--show-skipped]
Exit status is always 0: this is a review aid, not a gate.
"""
import glob, io, os, re, sys, collections

# label must be the unqualified standard rate
LABEL_OK = re.compile(r'^(standard|headline|regular|main)\b.*\b(corporate income tax|corporate tax|CIT)\b.*\brate\b', re.I)
# any of these in the label or the qualifier scopes the rate to something narrower
NARROW = re.compile(r'\b(oil|gas|mining|petroleum|financial|bank|insurance|leasing|factoring|'
                    r'betting|gaming|liquor|tobacco|telecom|extractive|branch|'
                    r'small|SME|MSME|micro|reduced|top|large|minimum|listed|listing|'
                    r'turnover|lump.?sum|non.?resident|resident|free zone|special|'
                    r'band|bracket|range|threshold|exceed|above|up to|between|'
                    r'from 20\d\d|in 20\d\d|until|before|after|effective|prior|'
                    r'was|formerly|previously|reduced from|increased from)\b', re.I)
YEARY = re.compile(r'\b(19|20)\d\d\b')
LINE = re.compile(r'^\s*[-*]\s+\*\*(?P<label>[^*]{3,90})\*\*\s+[—-]\s+(?P<rest>.+)$')
# the trailing _( ... )_ is the SOURCE CITATION, not a scope qualifier. Leaving it in
# made every rate whose statute has a year in its name -- "Llei 95/2010", "Act No.
# 586/1992 Coll.", "Income Tax Act 2015" -- look like a year-scoped rate, and the
# check silently tested 44 jurisdictions when it could test far more.
CITE = re.compile(r'_\(.*?\)_\s*$')
# the corpus writes the rate both as `25%` and as `25 percent`. Matching only the
# sign form made "25 percent (before 3% AIDS levy on tax)" yield 3, "28 percent
# (Reduced from 30%...)" yield 30, and "25 percent (reduced to 20% for MSMEs)"
# yield 20 -- three jurisdictions that agree perfectly, reported as disagreeing.
# That is the same mistake, in the checker, that the docstring above describes.
PCT = re.compile(r'(?<![\d.])(\d{1,2}(?:\.\d+)?)\s?(?:%|percent\b)')

def main():
    show_skipped = '--show-skipped' in sys.argv
    stated = collections.defaultdict(list)      # juris -> [(rate, path, lineno)]
    skipped = collections.defaultdict(list)

    for p in sorted(glob.glob('skills/international/*/*.md')):
        juris = p.split(os.sep)[2]
        for n, line in enumerate(io.open(p, encoding='utf-8', errors='replace'), 1):
            m = LINE.match(line)
            if not m:
                continue
            label, rest = m.group('label'), m.group('rest')
            if not LABEL_OK.match(label.strip()):
                continue
            rest = CITE.sub('', rest).strip()
            # the qualifier is everything after the number, plus the label itself
            if NARROW.search(label) or NARROW.search(rest) or YEARY.search(rest):
                skipped[juris].append((label.strip(), rest.strip()[:90], p, n))
                continue
            pcts = PCT.findall(rest)
            # exactly one percentage, or the line is stating more than one rate
            if len(set(pcts)) != 1:
                skipped[juris].append((label.strip(), rest.strip()[:90], p, n))
                continue
            stated[juris].append((pcts[0], p, n))

    conflicts = 0
    for juris in sorted(stated):
        rates = {r for r, _, _ in stated[juris]}
        if len(rates) > 1:
            conflicts += 1
            print('CONFLICT  %-22s %s' % (juris, ', '.join(sorted(rates, key=float))))
            for r, p, n in sorted(stated[juris]):
                print('              %s%%  %s:%d' % (r, p, n))

    print('\njurisdictions stating an unqualified standard CIT rate: %d' % len(stated))
    print('of those, disagreeing with themselves:                  %d' % conflicts)
    print('jurisdictions with rate lines skipped as qualified:     %d' % len(skipped))

    if show_skipped:
        print('\n--- skipped (sector, band, class, year or multi-rate lines) ---')
        for juris in sorted(skipped):
            for label, rest, p, n in skipped[juris]:
                print('%-20s %-46s %s:%d' % (juris, label[:46], p, n))
                print('%-20s   %s' % ('', rest))

main()
