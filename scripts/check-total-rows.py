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

# ---------------------------------------------------------------------------
# THE SECOND SHAPE: the same assertion made in bullets rather than a table.
#
# Everything above reads markdown tables. The corpus's generated fact blocks are
# bullet lists, and they make exactly the same double assertion:
#
#   - **Total employer social-security contribution** - 27.4% ...
#   - **Employer - pension (first pillar)** - 16.6% ...
#   - **Employer - Fondiss** - 2.0% ...
#
# 27.4% against components summing to 25.5%. Invisible here until now, because
# no pipe character appears anywhere in it. sm-payroll-social states both an
# employer total 1.9 points above its parts and an employee total 0.1 below.
#
# Note the order is reversed from the table convention: the total LEADS its
# components instead of closing them.
#
# Two rules keep the false-positive rate near the table pass's. A component must
# share a topic word with the total -- without that, any later bullet carrying a
# percentage got swept in and 45 of 61 groups "failed", which was the measuring
# instrument failing, not the corpus. And a component naming the opposite side of
# the payroll must not join an employer total; bj-payroll-social otherwise summed
# employer CNSS, employee CNSS and the employer payroll tax into one figure.
#
# The known false-positive mode is the table pass's, unchanged: alternatives that
# look like components. Cyprus lists three reliefs under a combined CAP, and
# Lithuania lists two pension-pillar options a worker chooses between.
BULLET = re.compile(r'^\s*-\s+\*\*(.+?)\*\*\s*[-\u2014\u2013]\s*(.*)$')
ANY_TOTAL = re.compile(r'\b(total|combined|aggregate|overall)\b', re.I)
SIDE = re.compile(r'\bemploy(?:er|ee)\b', re.I)
STOPWORDS = set('total combined aggregate overall the and for rate rates of on to'
                ' contribution contributions social security insurance'.split())


def topic(label):
    return {w for w in re.findall(r'[a-z]+', label.lower())
            if w not in STOPWORDS and len(w) > 2}


def side(label):
    m = SIDE.search(label)
    return m.group(0).lower() if m else None


b_checked = b_bad = 0
for root in sys.argv[1:] or ['skills']:
    for p in sorted(glob.glob(os.path.join(root, '**', '*.md'), recursive=True)):
        rows = []
        for line in open(p, encoding='utf-8', errors='replace'):
            m = BULLET.match(line)
            if not m:
                rows.append(None)
                continue
            found = PCT.findall(m.group(2))
            rows.append((m.group(1), float(found[0].replace(',', '.'))
                         if len(found) == 1 else None))
        for i, r in enumerate(rows):
            if not r or r[1] is None:
                continue
            if not ANY_TOTAL.search(r[0]) or SKIP.search(r[0]):
                continue
            key, who, parts, usable = topic(r[0]), side(r[0]), [], True
            if not key:
                continue
            for j in range(i + 1, len(rows)):
                nxt = rows[j]
                if not nxt:
                    break
                if ANY_TOTAL.search(nxt[0]) or SKIP.search(nxt[0]):
                    break
                if not (topic(nxt[0]) & key):
                    break
                if who and side(nxt[0]) and side(nxt[0]) != who:
                    break
                if nxt[1] is None:
                    # Belongs to the group but its value is not a single
                    # percentage. Abandon the group rather than report the
                    # partial sum: ga-payroll-social writes its CNAMGS branch as
                    # "4.1% total (0.6% + 2% + 1.5%)", and stopping short there
                    # reported 16% against a total of 20.1% that is in fact
                    # exactly right.
                    usable = False
                    break
                parts.append(nxt)
            if not usable or len(parts) < 2:
                continue
            # Components that each restate the total are not a partition of it.
            # bz-payroll-social says "Larger share of the 10% total" and
            # "Smaller share of the 10% total" -- two bullets carrying the
            # total's own figure, summing to double it.
            if all(abs(x[1] - r[1]) < 0.051 for x in parts):
                continue
            b_checked += 1
            s_ = sum(x[1] for x in parts)
            if abs(s_ - r[1]) > 0.051:
                b_bad += 1
                print('%s\n    bullet total: **%s** - %g%%\n'
                      '    -> its %d components sum to %.2f%%'
                      % (p, r[0][:88], r[1], len(parts), s_))

print('total rows checked: %d ; not equal to their components: %d' % (checked, bad))
print('bullet totals checked: %d ; not equal to their components: %d'
      % (b_checked, b_bad))
