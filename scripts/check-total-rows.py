# -*- coding: utf-8 -*-
"""Check a table's Total row against the component rows above it.

A contribution table that lists its parts and then totals them is asserting the
sum twice. When the two disagree, one of them is wrong, and no external source
is needed to know that much -- only to decide which.

Found two real errors:

  * sweden-payroll listed allman loneavgift at 12.62%, making the seven
    arbetsgivaravgifter components sum to 32.42% against the table's own stated
    total of 31.42%. Skatteverket gives 11.62%. Worth noting how this one went:
    a web search asserted 12.62%, and the table's internal arithmetic is what
    showed the search wrong before the primary source confirmed it.
  * mx-imss put IMSS Modalidad 40 at "approx. 10.075%" over components summing
    to 8.75%. Neither figure was right: the 2025 rate is about 13.347%, the
    table was missing Gastos Medicos para Pensionados (1.425%) entirely, and its
    CEAV line predated the 2020 pension reform's annual increases. The stated
    total understated the real cost of the scheme by a quarter, and two worked
    examples and a freelance-intake guide inherited it.

It cannot tell a component from a mutually exclusive alternative, and that is
the whole of its false-positive rate. All 16 flags remaining in skills/ and
agent-skills/ are of that kind:

  * spain-payroll lists indefinido 1.55% and temporal 1.60% unemployment as
    separate rows. They are alternatives, and each totals correctly on its own
    (6.50% and 6.55%).
  * sd-payroll-social lists employer 17%, employee 8%, self-employed 25% and
    voluntarily-insured 23%. Only the first two are components of the stated
    25% total; the others are different contributor categories.
  * jp-incorporation gives a total for under-40s and another for 40-and-over,
    because nursing care applies only from 40. Each is right for its own band.

Rows whose label names a cap, floor, threshold or base are skipped, and a
Total row resets the running sum so tables with intermediate subtotals check
each block separately.

Usage: python3 scripts/check-total-rows.py [dir ...]   (default: skills)
Exit status is always 0: this is a review aid, not a gate.
"""
import glob, os, re, sys

PCT = re.compile(r'(\d{1,3}(?:[.,]\d+)?)\s*%')
TOTAL = re.compile(r'^\W*\**\s*(total|combined|sub-?total|overall|aggregate)\b', re.I)
SKIP = re.compile(r'\b(cap|ceiling|floor|max|min|threshold|base|of which|note|n/?a|reduced|exempt)\b', re.I)

def cells(r): return [c.strip() for c in r.strip().strip('|').split('|')]

checked = bad = 0
for root in sys.argv[1:] or ['skills']:
    for p in sorted(glob.glob(os.path.join(root, '**', '*.md'), recursive=True)):
        lines = open(p, encoding='utf-8', errors='replace').read().split('\n')
        i = 0
        while i < len(lines):
            if not lines[i].strip().startswith('|'): i += 1; continue
            j = i
            while j < len(lines) and lines[j].strip().startswith('|'): j += 1
            block, i = lines[i:j], j
            if len(block) < 4: continue
            hdr = cells(block[0]); data = block[2:]
            if not any(TOTAL.match(cells(r)[0]) for r in data if cells(r)): continue
            for c in range(1, len(hdr)):
                # every row must give exactly one percentage in this column
                vals = []
                ok = True
                for r in data:
                    cc = cells(r)
                    if len(cc) <= c: ok = False; break
                    m = PCT.findall(cc[c])
                    if len(m) != 1: ok = False; break
                    vals.append((TOTAL.match(cc[0]) is not None, SKIP.search(cc[0]) is not None,
                                 float(m[0].replace(',', '.')), r.strip()))
                if not ok or not any(v[0] for v in vals): continue
                run, comps = 0.0, 0
                for is_tot, is_skip, v, raw in vals:
                    if is_tot:
                        if comps >= 2:
                            checked += 1
                            if abs(run - v) > 0.051:
                                bad += 1
                                print('%s\n    under: %s\n    %s\n    -> components since the last total sum to %.2f%%, row says %g%%'
                                      % (p, ' | '.join(hdr)[:96], raw[:96], run, v))
                        run, comps = v, 0
                    elif not is_skip:
                        run += v; comps += 1
                break
print('total rows checked: %d ; not equal to their components: %d' % (checked, bad))
