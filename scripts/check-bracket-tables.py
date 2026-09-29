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

The second check recomputes the fixed amount in tables written as
"R44,118 + 26% above R245,100" (or "$20 + 3.00% of excess over $1,000",
"3,600 + 20% of excess over 50,000"): each band's fixed amount must equal the
previous band's fixed amount plus the previous band's rate applied to the
width between the two bases, to within a rounding allowance of 1.5 units or
0.05%. A row that fails was transcribed or re-indexed without its neighbour,
which the rate-repeat check cannot see. Any table with two consecutive rows in
that layout is checked, whatever its header; rows with another kind of band
between them (a flat "5.5% of the whole value") are not compared across it.

Statutes do carry genuine steps, and the baseline keeps them once read: Ohio's
2025 table sets $342.00 at $26,050 but $2,394.32 at $100,000 (R.C. 5747.02
(A)(3)(b) as amended by HB 96; the middle band reaches $2,375.63), and El
Salvador's 2025 withholding tables kept the $17.67 and $212.12 quotas of the
old second band when the exempt band grew to $550 and $6,600 (Decreto
Ejecutivo No. 10/2025). Each guide says so beside its table.

Usage: python3 scripts/check-bracket-tables.py [dir ...]   (default: skills)

Gate: exits 1 on any repeated pair or cumulative mismatch not listed in
scripts/baselines/bracket-tables.txt and on any baseline entry that no longer
reproduces. --json, --baseline PATH, --no-baseline and --update-baseline are
described in scripts/oa_tools/findings.py. The fingerprint is the file plus
the two rows (or, for a cumulative mismatch, the file plus the failing row),
so the legitimate repeats above stay accepted until one of their rows
changes.
"""
import os, re, sys, glob

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from oa_tools import findings  # noqa: E402

PCT = re.compile(r'(\d{1,2}(?:[.,]\d+)?)\s*%')
NUM = re.compile(r'\d[\d,. ]*\d|\d')
HDR = re.compile(r'(income|revenu|reddito|renta|rendimento|einkommen|band|bracket|'
                 r'tranche|slab|salary|wage|profit|turnover|chargeable|taxable)', re.I)
# "R44,118 + 26% above R245,100", "$20 + 3.00% of excess over $1,000",
# "USD 17.67 + 10% on excess over 550.00", "AZN 350 + 25% of the amount exceeding 2,500"
MONEY = r'(?:[A-Z]{1,3}\$?|[$€£R₹])?\s?\d[\d,. ]*'
CUM = re.compile(
    r'(?P<fixed>' + MONEY + r')\s*(?:\+|plus)\s*'
    r'(?P<rate>\d{1,2}(?:[.,]\d+)?)\s*%\s*'
    r'(?:of|on|above|over)?\s*(?:the\s+)?'
    r'(?:amount|excess|income|value|taxable income|taxable amount|net income|chargeable income)?\s*'
    r'(?:over|above|exceeding|in excess of)?\s*'
    r'(?P<base>' + MONEY + r'\d|\d)')


def cells(row):
    r = row.strip().strip('|')
    return [c.strip() for c in r.split('|')]


def amount(s):
    """A money string to a float: thousands separators dropped, a decimal
    comma honoured, currency letters and symbols ignored."""
    s = re.sub(r'[^\d,.]', '', s)
    if not s:
        return None
    if ',' in s and '.' in s:
        if s.rfind(',') > s.rfind('.'):          # 1.234,56
            s = s.replace('.', '').replace(',', '.')
        else:                                    # 1,234.56
            s = s.replace(',', '')
    elif ',' in s:
        parts = s.split(',')
        if all(len(p) == 3 for p in parts[1:]):  # 1,234,567
            s = s.replace(',', '')
        else:                                    # 12,5
            s = s.replace(',', '.')
    elif s.count('.') > 1:                       # 1.234.567
        s = s.replace('.', '')
    try:
        return float(s)
    except ValueError:
        return None


def cumulative(block):
    """Rows whose fixed amount does not follow from the band directly above.

    Only rows on consecutive lines are compared: a band written another way
    between them (Victoria's "5.5% of the whole dutiable value") means the two
    parsed rows are not neighbours, and a comparison across it would only
    report the gap."""
    rows = []
    for i, r in enumerate(block):
        m = CUM.search(r)
        if not m:
            continue
        fixed, base = amount(m.group('fixed')), amount(m.group('base'))
        if fixed is None or base is None:
            continue
        rows.append((i, fixed, float(m.group('rate').replace(',', '.')), base, r.strip()))
    hits = []
    for (i0, f0, r0, b0, t0), (i1, f1, _, b1, t1) in zip(rows, rows[1:]):
        if i1 != i0 + 1 or b1 <= b0:
            continue
        expected = f0 + r0 / 100.0 * (b1 - b0)
        if abs(f1 - expected) > max(1.5, 0.0005 * abs(expected)):
            hits.append((t0, t1, f1, round(expected, 2)))
    return hits


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
        for prev, row, stated, expected in cumulative(block):
            hits.append(('cumulative', prev[:96], row[:96], stated, expected))
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
                hits.append(('repeat', hdr[0][:44], a[2][:96], b[2][:96]))
    return hits


def main(argv=None):
    parser = findings.argument_parser('bracket-tables', __doc__.split('\n\n')[0])
    args = parser.parse_args(argv)
    report = findings.Report('bracket-tables', args)
    repeats = mismatches = 0
    for root in args.roots:
        for path in sorted(glob.glob(os.path.join(root, '**', '*.md'), recursive=True)):
            for hit in scan(path):
                if hit[0] == 'repeat':
                    _, hdr, a, b = hit
                    repeats += 1
                    report.add(findings.Finding(
                        path, '%s / %s' % (a, b), 'adjacent bands at one rate under "%s"' % hdr,
                        detail={'header': hdr, 'rows': [a, b]},
                        text='%s\n    under: %s\n    %s\n    %s' % (path, hdr, a, b)))
                else:
                    _, prev, row, stated, expected = hit
                    mismatches += 1
                    report.add(findings.Finding(
                        path, 'cumulative: %s' % row,
                        'fixed amount %s, but the previous band gives %s' % (
                            ('%.2f' % stated).rstrip('0').rstrip('.'),
                            ('%.2f' % expected).rstrip('0').rstrip('.')),
                        detail={'rows': [prev, row], 'stated': stated, 'expected': expected},
                        text='%s\n    stated %s, expected %s from the previous band\n    %s\n    %s' % (
                            path, ('%.2f' % stated).rstrip('0').rstrip('.'),
                            ('%.2f' % expected).rstrip('0').rstrip('.'), prev, row)))
    report.note('\nadjacent same-rate band pairs: %d; cumulative amount mismatches: %d'
                % (repeats, mismatches))
    return report.finish()


if __name__ == '__main__':
    sys.exit(main())
