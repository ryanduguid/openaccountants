#!/usr/bin/env python3
"""Recompute the derived columns a rate table carries, from the rest of the table.

Many bracket tables ship a column that is not independent data but a consequence
of the bands beside it: cumulative tax at the top of each band, or a cumulative
percentage of an instalment schedule. That redundancy is a gift — the table can
be checked against itself, with no external source and no judgement about which
year is current. It is the same argument that settled Malta's bad boundary in
check-band-continuity.py: adjacent bands must agree where they meet, so the
table's own subtract column fixed the threshold.

Two families are checked:

  cumulative tax   For each band, cumulative[i] must equal cumulative[i-1] plus
                   (upper - lower) x rate. Catches a band edited without its
                   cumulative column, which is what a half-finished annual
                   update leaves behind.

  cumulative %     An instalment schedule's cumulative column must be
                   non-decreasing, must agree with the running sum of any
                   per-instalment share column beside it, and must finish at
                   100% -- except under an annualised-income method, where 90%
                   is correct because the required annual payment is itself 90%
                   of current-year tax (federal Schedule AI, and the state
                   worksheets that mirror it). Those are not reported.

What it found. British Columbia's guide was `tax_year: 2025` carrying its 2024
brackets throughout — 47,937 / 95,875 / 110,076 / 133,664 / 181,232 / 252,752
against the 2025 values 49,279 / 98,560 / 113,158 / 137,407 / 186,306 / 259,829,
with a 2024 basic personal amount to match. BC was the one province with no
combined federal+provincial table, so it escaped the sweep that corrected the
other seven; the cumulative column is what gave it away. Ontario's cumulative
column was $1.40 light from its third band on.

Chasing BC's worked example then turned up a materially wrong credit that no
column check would have found: the B.C. tax reduction was written as
"$521 + $152 per dependant, reduced by 3.56% of net income". It is $562 for
2025, reduced by 3.56% of net income **in excess of $25,020**, eliminated at
$40,807, with no per-dependant amount. Reducing by 3.56% of the whole of net
income zeroes the credit at $14,635 instead, so the guide told a taxpayer on
$25,000 they got nothing when they were entitled to the full $562.
check-arithmetic.py had flagged that line and an earlier pass had triaged it as
a credit-sign artefact. It was not one.

One known residual, correctly reported: mozambique-income-tax. Its cumulative
column is built from the published "parcela a abater" rather than by
accumulating the bands, and those published figures do not produce continuous
brackets — strict continuity would need 35,700 rather than 37,500. The guide
already records this as a RESEARCH GAP and says which basis it used, so the
1,800 difference this reports is the discrepancy the guide is flagging, not a
new error.

Number parsing is locale-aware in the narrow way this corpus needs: a dot or a
space groups thousands only when a comma supplies the decimal (1.234,56 and
8 059), so Portugal's tables parse without breaking en-US ones. A cumulative
cell that shows its working ("20,000 + 48,000 = TZS 68,000") is read as the
value after the equals sign.

Usage: python3 scripts/check-derived-columns.py [dir ...]   (default: skills)
Exit status is always 0: this is a review aid, not a gate.
"""
import glob, os, re, signal, sys

try:
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
except (AttributeError, ValueError):
    pass

SEP = r'(?:--|–|—|-|to|through|a\b|até|ate)'
RANGE = re.compile(r'^\D*?([\d][\d,.  ]*\d|\d)\s*' + SEP + r'\s*([\d][\d,.  ]*\d|\d)\s*$', re.I)
FIRST = re.compile(r'^\W*(?:first|até|ate|up to|primeiros?|0\s*' + SEP + r')\s*([\d][\d,.  ]*\d|\d)\s*$', re.I)
PCT = re.compile(r'(\d{1,3}(?:[.,]\d+)?)\s*%')
MONEY = re.compile(r'(\d[\d,.  ]*\d|\d)')
# an annualised-income instalment schedule legitimately ends at 90%
ANNUALISED = re.compile(r'annuali[sz]', re.I)
# a cell showing arithmetic is a formula for an amount, not a cumulative share
# a tax-free band states no rate: 'Nil', 'Exempt', '0', '--'
NIL = re.compile(r'\b(nil|exempt|none|no tax|tax[- ]free|zero)\b|^\s*[-–—0]+\s*$', re.I)
FORMULA = re.compile(r'[×x*+\u2212]|\bof\b|\bexcess\b|[A-Z]{3}\s*\d', re.I)


def cells(row):
    return [c.strip() for c in row.strip().strip('|').split('|')]


def num(s):
    t = s.replace(' ', ' ').strip()
    if re.fullmatch(r'\d{1,3}(?:[. ]\d{3})+,\d+', t):
        return float(t.replace('.', '').replace(' ', '').replace(',', '.'))
    if re.fullmatch(r'\d{1,3}(?:[. ]\d{3})+', t):
        return float(t.replace('.', '').replace(' ', ''))
    if re.fullmatch(r'\d+,\d{1,2}', t):
        return float(t.replace(',', '.'))
    return float(t.replace(',', '').replace(' ', ''))


def money_result(cell):
    c = re.sub(r'[^\d,.  ]', ' ', cell.split('=')[-1])
    m = MONEY.findall(c)
    return num(m[-1]) if m else None


def blocks(path):
    lines = open(path, encoding='utf-8', errors='replace').read().split('\n')
    i = 0
    while i < len(lines):
        if not lines[i].strip().startswith('|'):
            i += 1
            continue
        j = i
        while j < len(lines) and lines[j].strip().startswith('|'):
            j += 1
        yield lines[i:j], '\n'.join(lines[max(0, i - 4):i])
        i = j


def check(path, verified):
    out = []
    for block, preamble in blocks(path):
        if len(block) < 5:
            continue
        hdr = cells(block[0])
        cum_c = next((k for k, h in enumerate(hdr)
                      if re.search(r'cumulat|imposto cumulativo|acumulad', h, re.I)), None)
        if not cum_c:
            continue
        rate_c = next((k for k, h in enumerate(hdr)
                       if k not in (0, cum_c) and re.search(r'rate|taxa normal|taxa\b|tax\b', h, re.I)), None)

        # --- family 1: cumulative tax at top of band ---
        rows = []
        for r in block[2:]:
            c = cells(r)
            if len(c) <= cum_c:
                rows.append(None)
                continue
            col0 = re.sub(r'\*+', '', c[0]).strip()
            lo = hi = None
            m = RANGE.match(col0)
            if m:
                lo, hi = num(m.group(1)), num(m.group(2))
            else:
                f = FIRST.match(col0)
                if f:
                    lo, hi = 0.0, num(f.group(1))
            if lo is None:
                rows.append(None)
                continue
            src = c[rate_c] if rate_c is not None and len(c) > rate_c else ' '.join(c[1:cum_c])
            mp = PCT.findall(src)
            if mp:
                rt = float(mp[0].replace(',', '.')) / 100
            elif NIL.search(src):
                rt = 0.0          # a tax-free first band carries no percentage
            else:
                rt = None
            cu = money_result(c[cum_c])
            rows.append((lo, hi, rt, cu, r.strip()) if None not in (lo, hi, rt, cu) else None)
        good = [x for x in rows if x]
        if len(good) >= 3 and rows and rows[0] is not None:
            verified.append(path)
            run, prev_hi = 0.0, None
            for lo, hi, rt, cu, raw in good:
                # a band written "30,001 -- 50,000" is 20,000 wide, not 19,999: measure
                # from the previous band's top so the off-by-one never has to be absorbed
                width = hi - (prev_hi if prev_hi is not None else lo)
                run += width * rt
                prev_hi = hi
                if abs(run - cu) > 1.0:
                    out.append((' | '.join(hdr)[:100], raw[:98],
                                'bands give %s, column says %s'
                                % (format(run, ',.2f'), format(cu, ',.2f'))))
            continue

        # --- family 2: cumulative percentage of an instalment schedule ---
        share_c = next((k for k, h in enumerate(hdr)
                        if k != cum_c and re.search(r'percent|%|share|portion|instal', h, re.I)), None)
        cum, share = [], []
        for r in block[2:]:
            c = cells(r)
            cell = c[cum_c] if len(c) > cum_c else ''
            # a cumulative *percentage* is a bare figure; a cell carrying arithmetic
            # is a formula for an amount (Azerbaijan's "14% x (income - 8,000)")
            if FORMULA.search(cell):
                cum.append(None); share.append(None); continue
            m = PCT.findall(cell)
            cum.append(float(m[0]) if len(m) == 1 else None)
            ms = PCT.findall(c[share_c]) if share_c is not None and len(c) > share_c else []
            share.append(float(ms[0]) if len(ms) == 1 else None)  # noqa: matched to cum above
        vals = [v for v in cum if v is not None]
        if len(vals) < 3 or any(v > 100.5 for v in vals):
            continue
        verified.append(path)
        if vals != sorted(vals):
            out.append((' | '.join(hdr)[:100], '', 'cumulative column is not non-decreasing: %s'
                        % ', '.join('%g%%' % v for v in vals)))
        elif abs(vals[-1] - 100) > 0.51 and not ANNUALISED.search(preamble + ' '.join(hdr)):
            out.append((' | '.join(hdr)[:100], '', 'final cumulative is %g%%, not 100%%' % vals[-1]))
        if share_c is not None and all(s is not None for s in share):
            run = 0.0
            for k, (s, c_) in enumerate(zip(share, cum)):
                if c_ is None:
                    continue
                run += s
                if abs(run - c_) > 0.51:
                    out.append((' | '.join(hdr)[:100], '',
                                'row %d: shares so far total %g%%, cumulative says %g%%' % (k + 1, run, c_)))
                    break
    return out


total, verified = 0, []
for root in sys.argv[1:] or ['skills']:
    for p in sorted(glob.glob(os.path.join(root, '**', '*.md'), recursive=True)):
        for hdr, raw, msg in check(p, verified):
            print('%s\n    under: %s' % (p, hdr))
            if raw:
                print('    %s' % raw)
            print('    -> %s' % msg)
            total += 1
print('derived columns verified: %d' % len(verified))
print('derived-column mismatches: %d' % total)
