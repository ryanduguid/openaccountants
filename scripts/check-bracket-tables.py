#!/usr/bin/env python3
"""Flag progressive rate tables whose adjacent bands carry the same rate.

A genuine progressive schedule never has two neighbouring bands at one rate:
if it did, the two would collapse into a single band and the threshold between
them would do nothing. So an adjacent repeat is either a transcription slip or
a band whose rate was edited without its neighbour — both of which a rate-value
check cannot see, because each individual rate is plausible on its own.

Four errors were found this way:

  * Ethiopia's Schedule B and C both ended "120,001-168,000 | 30%" followed by
    "over 168,000 | 30%", the second annotated "reduced from 35%". The cut was
    not real; the source that reported it had confused the individual top rate
    with the flat 30% that applies to companies.
  * Manitoba's combined federal+provincial table repeated 25.8% across the
    $47,000 provincial threshold. The second band should have been 27.25%.
  * Saskatchewan's repeated 25.5% across its own threshold, and was stale as
    well: both the provincial and the federal breakpoints were a year old.
  * Fiji's payroll table subtracted the wrong band floor, which the repeat
    drew attention to even though the repeated 20% there is genuine.

Expect false positives and read before editing. Legitimate repeats are common:

  * a flat rate really can span thresholds that exist for another tax, which is
    why Fiji's income tax table is split at SRT boundaries;
  * a table listing income *types* rather than bands (Slovenia's schedular 25%)
    trips the header test;
  * a multi-column combined table can hold a constant column, so Norway's flat
    22% base rate repeats down every row;
  * a corporate rate phase-down by year (North Carolina) repeats while the rate
    is held flat between steps;
  * worked-example tables that tabulate a computation rather than a schedule.

Only tables whose first column is a strictly ascending set of thresholds are
considered, which removes most but not all of these.

Usage: python3 scripts/check-bracket-tables.py [dir ...]   (default: skills)
Exit status is always 0: this is a review aid, not a gate.
"""
import os, re, sys, glob

PCT = re.compile(r'(\d{1,2}(?:[.,]\d+)?)\s*%')
NUM = re.compile(r'\d[\d,. ]*\d|\d')
HDR = re.compile(r'(income|revenu|reddito|renta|rendimento|einkommen|band|bracket|'
                 r'tranche|slab|salary|wage|profit|turnover|chargeable|taxable)', re.I)


def cells(row):
    r = row.strip().strip('|')
    return [c.strip() for c in r.split('|')]


def first_num(s):
    m = NUM.search(s.replace('%', ''))
    if not m:
        return None
    t = m.group(0).replace(' ', '').replace(' ', '').replace(',', '')
    if t.count('.') > 1:
        t = t.replace('.', '')
    try:
        return float(t)
    except ValueError:
        return None


def scan(path):
    lines = open(path, encoding='utf-8', errors='replace').read().split('\n')
    hits, i = [], 0
    while i < len(lines):
        if not lines[i].strip().startswith('|'):
            i += 1
            continue
        j = i
        while j < len(lines) and lines[j].strip().startswith('|'):
            j += 1
        block, i = lines[i:j], j
        if len(block) < 5:                      # header + rule + >=3 data rows
            continue
        hdr = cells(block[0])
        if not hdr or not HDR.search(hdr[0]):
            continue
        data = block[2:]
        # the rate column is the one holding exactly one percentage per row
        best, best_n = None, 0
        for c in range(1, len(hdr)):
            n = sum(1 for r in data
                    if len(cells(r)) > c and len(PCT.findall(cells(r)[c])) == 1)
            if n > best_n:
                best, best_n = c, n
        if best is None or best_n < len(data) - 1 or best_n < 3:
            continue
        seq = []
        for r in data:
            cs = cells(r)
            ms = PCT.findall(cs[best]) if len(cs) > best else []
            seq.append((first_num(cs[0]) if cs else None,
                        float(ms[0].replace(',', '.')) if len(ms) == 1 else None,
                        r.strip()))
        ths = [t for t, _, _ in seq if t is not None]
        # a real schedule is ordered and has no repeated threshold
        if len(ths) < 3 or ths != sorted(ths) or len(set(ths)) != len(ths):
            continue
        for a, b in zip(seq, seq[1:]):
            if a[1] is not None and a[1] == b[1]:
                hits.append((hdr[0][:44], a[2][:96], b[2][:96]))
    return hits


roots = sys.argv[1:] or ['skills']
total = 0
for root in roots:
    for path in sorted(glob.glob(os.path.join(root, '**', '*.md'), recursive=True)):
        for hdr, a, b in scan(path):
            print('%s\n    under: %s\n    %s\n    %s' % (path, hdr, a, b))
            total += 1
print('adjacent same-rate band pairs:', total)
