#!/usr/bin/env python3
"""Find a heading and an adjacent bold label that name DIFFERENT tax years.

Found by hand in australia-payroll, where an update changed the heading but left
the old label sitting under it:

    ### Resident Individual Tax Rates (2026--27)

    **Resident Individual Tax Rates (2025--26)**

    | Taxable Income (AUD) | Rate | ... |
    | 18,201 -- 45,000 | 15% | ... |

The table beneath is the 2026-27 one. Nothing else in the file is wrong, every
figure in the table is right, and the arithmetic self-verifies -- so no rate
check, bracket check or arithmetic check can see it. The only wrong thing is the
year written above the numbers, and an agent that trusts the bold label reads a
current table as last year's.

This is the noun class again: the defect is in a label, not a value.

Matches a heading (#, ##, ### ...) or bold line naming a year or a year range,
followed within three lines by another heading or bold line naming a DIFFERENT
year, with no intervening prose. Reports the pair for a human to read.

Usage: python3 scripts/check-stale-subheadings.py [path ...]
Exit status is always 0: this is a review aid, not a gate.
"""
import glob, io, os, re, sys

YEARS = re.compile(r'\b(20\d{2})\s*(?:--|—|–|-|/)\s*(\d{2,4})\b|\b(20\d{2})\b')
LABEL = re.compile(r'^\s*(?:#{1,6}\s+(?P<h>.+?)|\*\*(?P<b>[^*]+)\*\*)\s*$')


def years_in(text):
    out = set()
    for m in YEARS.finditer(text):
        if m.group(1):
            a, b = m.group(1), m.group(2)
            b = b if len(b) == 4 else a[:2] + b
            out.add('%s-%s' % (a, b))
        elif m.group(3):
            out.add(m.group(3))
    return out


def norm(s):
    return re.sub(r'[^a-z]+', ' ', s.lower()).strip()


def main():
    roots = [a for a in sys.argv[1:] if not a.startswith('-')] or ['skills', 'packages', 'agent-skills']
    hits = 0
    for root in roots:
        for p in sorted(glob.glob(os.path.join(root, '**', '*.md'), recursive=True)):
            lines = io.open(p, encoding='utf-8', errors='replace').read().split('\n')
            labels = []
            for i, line in enumerate(lines):
                m = LABEL.match(line)
                if not m:
                    continue
                text = m.group('h') or m.group('b')
                labels.append((i, text, years_in(text)))
            for k in range(len(labels) - 1):
                i, t1, y1 = labels[k]
                j, t2, y2 = labels[k + 1]
                if j - i > 3 or not y1 or not y2 or y1 == y2:
                    continue
                # only when the two labels are otherwise the SAME heading
                a, b = norm(re.sub(r'[\d()–—/-]+', '', t1)), norm(re.sub(r'[\d()–—/-]+', '', t2))
                if not a or a != b:
                    continue
                # nothing but blank lines between them
                if any(l.strip() for l in lines[i + 1:j]):
                    continue
                hits += 1
                print('%s:%d' % (p, i + 1))
                print('    %s' % t1.strip())
                print('    %s' % t2.strip())
    print('\nstale duplicated headings: %d' % hits)


main()
