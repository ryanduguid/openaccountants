# -*- coding: utf-8 -*-
"""Verify the deduction column of a quick-formula table against the bands beside it.

Many jurisdictions publish their schedule as `tax = rate x income - deduction`
rather than as a set of band widths -- Malta's "Subtract", Mozambique's
"parcela a abater", Ethiopia's "Deduction". That constant is not free
information: adjacent bands must produce the same tax where they meet, so

    deduction[i] = deduction[i-1] + (rate[i] - rate[i-1]) x boundary

Any table carrying the column can therefore be checked against itself, with no
external source. It is the same argument that settled Malta's bad 0% boundary
in check-band-continuity.py.

43 tables check out. The eight boundaries this reports are all Mozambique, and
they are **correct as published**: PwC and the AT both print 37,500 for the 25%
band and 141,540 for the 32% band, where strict continuity would need 35,700
and 143,340. Mozambique's published schedule is very slightly discontinuous at
those two boundaries, so the figures must not be "corrected" to make the
arithmetic close. All three Mozambican guides carrying the table now say so;
before this check, only two of the three did, and mozambique-social-contributions
reproduced the discontinuous figures with no warning at all.

That is the useful residue of a check that finds nothing wrong: it tells you
which of several copies of a table is missing the caveat the others carry.

Usage: python3 scripts/check-quick-formula.py [dir ...]   (default: skills)
Exit status is always 0: this is a review aid, not a gate.
"""
import glob, os, re, sys

SEP = r'(?:--|–|—|-|to|through|a\b|até|ate)'
RANGE = re.compile(r'^\D*?([\d][\d,.  ]*\d|\d)\s*' + SEP + r'\s*([\d][\d,.  ]*\d|\d)\s*$', re.I)
FIRST = re.compile(r'^\W*(?:first|até|ate|up to|primeiros?|over|above|acima|0\s*' + SEP + r')\s*([\d][\d,.  ]*\d|\d)\s*$', re.I)
PCT = re.compile(r'(\d{1,3}(?:[.,]\d+)?)\s*%')
NUMC = re.compile(r'(\d[\d,.  ]*\d|\d)')
DEDHDR = re.compile(r'subtract|parcela a abater|deductible amount|deduction|abater|abzug', re.I)
RATEHDR = re.compile(r'rate|taxa|tasa|aliquota|alíquota', re.I)

def cells(r): return [c.strip() for c in r.strip().strip('|').split('|')]

def num(s):
    t = s.replace(' ', ' ').strip()
    if re.fullmatch(r'\d{1,3}(?:[. ]\d{3})+,\d+', t): return float(t.replace('.','').replace(' ','').replace(',','.'))
    if re.fullmatch(r'\d{1,3}(?:[. ]\d{3})+', t):     return float(t.replace('.','').replace(' ',''))
    if re.fullmatch(r'\d+,\d{1,2}', t):               return float(t.replace(',','.'))
    return float(t.replace(',','').replace(' ',''))

checked = bad = 0
for root in sys.argv[1:] or ['skills']:
    for p in sorted(glob.glob(os.path.join(root,'**','*.md'), recursive=True)):
        lines = open(p, encoding='utf-8', errors='replace').read().split('\n')
        i = 0
        while i < len(lines):
            if not lines[i].strip().startswith('|'): i += 1; continue
            j = i
            while j < len(lines) and lines[j].strip().startswith('|'): j += 1
            block, i = lines[i:j], j
            if len(block) < 5: continue
            hdr = cells(block[0])
            ded_c = next((k for k,h in enumerate(hdr) if k and DEDHDR.search(h)), None)
            rate_c = next((k for k,h in enumerate(hdr) if k and k != ded_c and RATEHDR.search(h)), None)
            if ded_c is None or rate_c is None: continue
            rows = []
            for r in block[2:]:
                c = cells(r)
                if len(c) <= max(ded_c, rate_c): continue
                col0 = re.sub(r'\*+','',c[0]).strip()
                m = RANGE.match(col0); f = FIRST.match(col0)
                if m: lo, hi = num(m.group(1)), num(m.group(2))
                elif f: lo, hi = 0.0, num(f.group(1))
                else: continue
                mp = PCT.findall(c[rate_c])
                if not mp: continue
                rt = float(mp[0].replace(',','.'))/100
                mn = NUMC.search(c[ded_c].replace('*',''))
                if not mn: continue
                try: dd = num(mn.group(1))
                except Exception: continue
                rows.append((lo, hi, rt, dd, r.strip()))
            if len(rows) < 3: continue
            checked += 1
            for a, b in zip(rows, rows[1:]):
                B = a[1]                     # boundary = previous band's top
                exp = a[3] + (b[2] - a[2]) * B
                if abs(exp - b[3]) > max(1.0, abs(exp)*0.005):
                    print('%s\n    under: %s' % (p, ' | '.join(hdr)[:100]))
                    print('    %s\n    %s' % (a[4][:92], b[4][:92]))
                    print('    -> continuity at %s needs deduction %s, table says %s'
                          % (format(B, ',g'), format(exp, ',.2f'), format(b[3], ',.2f')))
                    bad += 1
print('quick-formula tables checked: %d ; broken boundaries: %d' % (checked, bad))
