"""Two date checks. A correct rate on the wrong date reads as fact and checks clean.

Every numeric checker in this repo compares *amounts*. None of them looks at when
a rule is said to start, or at whether the year a guide declares matches the year
it actually works in. Both are ways a guide can be entirely right about its
figures and still give the wrong answer.

**A. Rates a jurisdiction dates two different ways.** Within one folder, collect
sentences that assert a rate taking effect -- one rate, one date, an effect verb
("from", "effective", "rose to", "commenced") -- and report a rate attached to
two different dates.

Run over `skills/` this returns 8 rows and, read in context, all 8 are one rate
shared by two unrelated taxes or regimes:

  * Singapore -- "From 1 January 2020 ... self-assess output tax at 9%". The
    2020 date starts the reverse-charge regime; the 9% is today's rate. Both
    quick-reference tables correctly say "9% (from 1 January 2024)".
  * Ireland -- 33% CGT under s.28 TCA beside 33% CAT on Finance Act 2024
    thresholds effective 2 October 2024. Two taxes, one rate.
  * Uzbekistan -- a 1% social-tax incentive from 1 May 2025 beside a 1% turnover
    tax from 1 January 2026.
  * Nigeria -- 7.5% VAT from 1 February 2020, retained by the NTA from
    1 January 2026.
  * Australia and Saudi Arabia -- 15%, 30%, 50% each span several regimes.

A clean result, recorded so the next person need not re-derive it. One rate
serving two taxes is the standing false-positive class; there is no way to
separate them without reading the sentence.

**B. Guides working in a year later than the one they declare.** Compare
`tax_year` against the modal year in the guide's own quick-reference block. Two
rows, one real:

  * `au-fbt` declared `tax_year: 2025` while its body worked the FBT year
    1 April 2026 - 31 March 2027 throughout, updated 2026-08-02. Its sibling
    `au-fbt-year` already carried `tax_year: 2026` plus the fiscal-year note the
    spec asks for, so the convention was settled and this file had drifted off
    it. Fixed.
  * `albania-tax-optimization` matches 2029 five times: the sunset of a
    temporary 0% regime, not a working year. That is the false-positive class --
    a guide whose headline rule has a long-dated expiry.

Only a clear majority of a guide's head counts as its working year, and only a
gap of two years or more is reported, so an ordinary filing-year reference does
not trip it.

Usage: python3 scripts/check-effective-dates.py [skills]
"""
import os, re, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from frontmatter_yaml import load_frontmatter

MONTHS = 'January|February|March|April|May|June|July|August|September|October|November|December'
DATE = re.compile(r'\b(\d{1,2}\s+(?:%s)\s+20\d{2})\b' % MONTHS)
PCT = re.compile(r'(\d{1,2}(?:\.\d{1,3})?)\s?%')
EFFECT = re.compile(r'\b(from|effective|with effect from|as from|commenc\w+|introduced|'
                    r'increased to|reduced to|rose to|fell to|raised to|cut to|applies from)\b', re.I)
FM = re.compile(r'\A---\n(.*?)\n---\n', re.S)
YR = re.compile(r'\b(20[2-3]\d)\b')


def walk(root):
    for dp, _, fns in os.walk(root):
        for fn in sorted(fns):
            if fn.endswith('.md'):
                p = os.path.join(dp, fn)
                parts = p.split(os.sep)
                if len(parts) >= 3:
                    yield p, parts[2]


def rate_dates(root):
    pairs = collections.defaultdict(lambda: collections.defaultdict(set))
    for p, jur in walk(root):
        text = open(p, encoding='utf-8', errors='replace').read()
        for s in re.split(r'(?<=[.!?])\s+|\n|\|', text):
            if not EFFECT.search(s):
                continue
            ds, ps = DATE.findall(s), PCT.findall(s)
            if len(ds) == 1 and len(ps) == 1:      # one rate, one date, no ambiguity
                pairs[jur][ps[0]].add((ds[0], p))
    hits = 0
    for jur in sorted(pairs):
        for pct, obs in sorted(pairs[jur].items()):
            if len({d for d, _ in obs}) > 1 and len(obs) > 1:
                print('%-22s %6s%%  ' % (jur, pct) + ' | '.join(
                    '%s (%s)' % (d, os.path.basename(f)) for d, f in sorted(obs)))
                hits += 1
    print('rates a jurisdiction dates two different ways:', hits)
    return hits


def declared_vs_worked(root):
    rows = []
    for p, _ in walk(root):
        txt = open(p, encoding='utf-8', errors='replace').read()
        m = FM.match(txt)
        if not m:
            continue
        try:
            fmd = load_frontmatter(m.group(1))
        except Exception:
            continue
        ty = str(fmd.get('tax_year', '')).strip()
        if not re.fullmatch(r'20\d{2}', ty):
            continue
        head = txt[m.end():][:4000]           # the quick-reference block
        c = collections.Counter(YR.findall(head))
        if not c:
            continue
        modal, n = c.most_common(1)[0]
        if n < 3 or n < sum(c.values()) * 0.4:   # no clear working year
            continue
        if int(modal) - int(ty) >= 2:
            rows.append((p, ty, modal, n, sum(c.values())))
    for p, ty, modal, n, tot in sorted(rows):
        print('%-62s tax_year=%s  head works in %s (%d of %d year mentions)'
              % (p, ty, modal, n, tot))
    print('guides whose quick-reference works two or more years past their tax_year:', len(rows))
    return len(rows)


if __name__ == '__main__':
    root = sys.argv[1] if len(sys.argv) > 1 else 'skills'
    print('== A. rates dated two ways within one jurisdiction')
    a = rate_dates(root)
    print('\n== B. declared tax_year vs the year the guide works in')
    b = declared_vs_worked(root)
