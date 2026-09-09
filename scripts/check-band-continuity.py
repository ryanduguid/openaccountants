#!/usr/bin/env python3
"""Bracket tables whose bands leave a gap or overlap.

Every band in a progressive schedule must begin where the previous one ended.
A gap leaves income taxed by no band; an overlap leaves it taxed by two. Either
way the table cannot be applied, and neither is visible to a check that tests
rate *values* -- every rate in a broken table can be individually correct.

The failure mode this catches is a **half-completed annual update**. When a
maintainer refreshes a table by editing the band ends and stops, the ends carry
the new year and the starts carry the old, and the seam shows as a gap or an
overlap of exactly the indexation step. Four of the five findings were this:

  * fr-income-tax -- ends moved to the 2025 bareme (29,315 / 83,823 / 180,294),
    starts left at an older scale (26,232 / 74,546). Income between 26,232 and
    29,315 fell in two bands at once.
  * be-income-tax -- ends moved to income year 2025 (28,800 / 49,840), starts
    left at income year 2026 (16,721 / 29,511), leaving a 400 and a 710 gap.
  * belgium-payroll and its agent-skills copies -- self-consistent, but the
    2026 thresholds under a heading with no year in a tax_year: 2025 guide.
    Both years are now tabulated side by side.
  * bf-payroll -- every band began 100 above the previous end rather than 1,
    so six 99-franc slices of monthly income were taxed by nothing.
  * malta-payroll (M0) -- a 0% band ending at 15,500 against a 15% band
    starting at 15,001. The table's own "Subtract" column settles it without
    an external source: the bands must agree where they meet, so the boundary
    is (2,250 - 0) / (0.15 - 0) = 15,000. The other 20 boundaries across
    Malta's seven status tables all check out by the same identity.

Only tables whose first column parses as an ascending run of numeric ranges are
considered, and a difference of 0 or 1 between one band's end and the next one's
start counts as contiguous, as does the 0.01 convention used for cent-precision
tables. Differences beyond a quarter of the band value are ignored as unlikely
to be the same scale.

Usage: python3 scripts/check-band-continuity.py [dir ...]   (default: skills)
Exit status is always 0: this is a review aid, not a gate.
"""
import glob, os, re, signal, sys

try:
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
except (AttributeError, ValueError):
    pass

RANGE = re.compile(r'^\D*?([\d][\d,. ]*\d|\d)\s*(?:--|–|—|-|to|through)\s*([\d][\d,. ]*\d|\d)\s*$')
HDR = re.compile(r'(income|revenu|reddito|renta|rendimento|einkommen|band|bracket|tranche|'
                 r'slab|salary|wage|profit|turnover|chargeable|taxable|earnings)', re.I)
PCT = re.compile(r'\d{1,2}(?:[.,]\d+)?\s*%')


def cells(row):
    return [c.strip() for c in row.strip().strip('|').split('|')]


def num(s):
    t = s.replace(' ', '').replace(' ', '').replace(',', '')
    if t.count('.') > 1 or (t.count('.') == 1 and len(t.split('.')[-1]) == 3):
        t = t.replace('.', '')
    try:
        return float(t)
    except ValueError:
        return None


def scan(path):
    lines = open(path, encoding='utf-8', errors='replace').read().split('\n')
    out, i = [], 0
    while i < len(lines):
        if not lines[i].strip().startswith('|'):
            i += 1
            continue
        j = i
        while j < len(lines) and lines[j].strip().startswith('|'):
            j += 1
        block, i = lines[i:j], j
        if len(block) < 5:
            continue
        hdr = cells(block[0])
        if not hdr or not HDR.search(hdr[0]):
            continue
        data = block[2:]
        if sum(1 for r in data if PCT.search(r)) < len(data) - 1:
            continue
        parsed = []
        for r in data:
            c = cells(r)
            m = RANGE.match(re.sub(r'\*+', '', c[0])) if c else None
            if m:
                lo, hi = num(m.group(1)), num(m.group(2))
                if lo is not None and hi is not None and hi > lo:
                    parsed.append((lo, hi, r.strip()))
                    continue
            parsed.append(None)
        run, best = [], []
        for b in parsed:
            if b:
                run.append(b)
            else:
                if len(run) > len(best):
                    best = run
                run = []
        if len(run) > len(best):
            best = run
        if len(best) < 3:
            continue
        for a, b in zip(best, best[1:]):
            gap = b[0] - a[1]
            if 0 <= gap <= 1:
                continue
            limit = max(a[1], 1) * 0.25
            if 1 < gap <= limit:
                out.append((hdr[0][:44], a[2], b[2], 'GAP of %s' % format(gap - 1, ',g')))
            elif -limit <= gap < 0:
                out.append((hdr[0][:44], a[2], b[2], 'OVERLAP of %s' % format(-gap, ',g')))
    return out


total = 0
for root in sys.argv[1:] or ['skills']:
    for p in sorted(glob.glob(os.path.join(root, '**', '*.md'), recursive=True)):
        for hdr, a, b, kind in scan(p):
            print('%s\n    under: %s\n    %s\n    %s\n    -> %s' % (p, hdr, a[:96], b[:96], kind))
            total += 1
print('bracket tables with a gap or overlap:', total)
