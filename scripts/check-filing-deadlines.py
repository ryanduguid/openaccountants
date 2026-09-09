"""Flag a form a jurisdiction gives two different calendar deadlines.

A wrong deadline is a penalty, and no checker here looked at one. Within a
folder, collect lines that name exactly one form and one calendar date and
carry a deadline word ("due", "deadline", "file by", "lodge by"), then report a
form with two different dates against it.

Run over `skills/` this returns 9 rows. Seven are correct as written and are
the standing false-positive classes:

  * an extension form legitimately has two dates -- `Form D-410` and
    `Form 4868` are filed by 15 April and extend to 15 October;
  * a form with several filing frequencies has one date per frequency --
    `MO-941` is due the 15th monthly, the last day of the month after quarter
    end quarterly, and 31 January annually;
  * a form whose deadline depends on who lodges -- New Zealand's `IR3` is due
    7 July self-filed and 31 March through a tax agent;
  * a date inside a worked example -- California's `Form 568` is due 15 March
    everywhere, and the "1 December" is a short accounting period running
    1-31 December;
  * `FY2025` is not a form; the form pattern matches it anyway.

The eighth was a table headed "Form 5080 due date" whose last row is Form 5081.
The ninth was real, and it was much bigger than a date.

**Malta.** `malta-income-tax` and `mt-rental-income` put TA24 at 30 April;
`mt-estimated-tax` and `malta-tax-optimization` put it at 30 June. Reading them
showed why: TA24 is the optional 15% final tax on gross rental income
(ITA Art. 31D), and five guides in the pack were using its name for something
else entirely -- the self-employed Personal Income Tax Return, which is due
30 June and carries Box 2, Box 20 and Box 36. `mt-estimated-tax`, a provisional
tax guide, named TA24 24 times, including a HARD STOP refusing to compute
without "the prior year TA24" -- a rental form a self-employed client would
never have filed. 37 references across five guides were corrected, and
`malta-income-tax` now carries a note saying which form is which, because TA24
is a real form and the wrong usage reads like a synonym.

That is the shape of what this check is for: the deadline conflict was the
symptom, and the defect underneath it was a form name.

Usage: python3 scripts/check-filing-deadlines.py [skills]
"""
import os, re, collections, sys

MONTH = ('January|February|March|April|May|June|July|August|September|'
         'October|November|December')
DAY = re.compile(r'\b(\d{1,2})\s+(%s)\b|\b(%s)\s+(\d{1,2})\b' % (MONTH, MONTH))
FORM = re.compile(r'\b((?:Form|Formulario|Formulaire|Modelo|Schedule|Return)\s+'
                  r'[A-Z0-9][A-Za-z0-9\-/\.]{1,12}|[A-Z]{2,6}-?\d{1,4}[A-Z]?|'
                  r'\b\d{3,4}-?[A-Z]{1,4}\b)')
DUE = re.compile(r'\b(due|deadline|file by|lodge by|filed by|submit by)\b', re.I)


def main(root):
    pairs = collections.defaultdict(lambda: collections.defaultdict(set))
    for dp, _, fns in os.walk(root):
        for fn in sorted(fns):
            if not fn.endswith('.md'):
                continue
            p = os.path.join(dp, fn)
            parts = p.split(os.sep)
            if len(parts) < 3:
                continue
            for line in open(p, encoding='utf-8', errors='replace'):
                if not DUE.search(line):
                    continue
                ds, fs = DAY.findall(line), set(FORM.findall(line))
                if len(ds) != 1 or len(fs) != 1:   # one form, one date, no ambiguity
                    continue
                d = ds[0]
                date = '%s %s' % (d[0], d[1]) if d[0] else '%s %s' % (d[3], d[2])
                pairs[parts[2]][fs.pop()].add((date, p))

    hits = 0
    for jur in sorted(pairs):
        for form, obs in sorted(pairs[jur].items()):
            if len({d for d, _ in obs}) > 1 and len(obs) > 1:
                print('%-20s %-14s ' % (jur, form) + ' | '.join(
                    '%s (%s)' % (d, os.path.basename(f)) for d, f in sorted(obs)))
                hits += 1
    print('forms a jurisdiction gives two different calendar deadlines:', hits)
    return hits


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'skills')
