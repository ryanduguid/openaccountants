"""Compare money and percentage facts between skills/federal and packages/us-federal.

The two trees hold the same 28 guides. `packages/us-federal/` is hand-authored
and never regenerated, so the copies drift independently, and where a labelled
fact carries different figures in the two of them one is wrong. Every
divergence found so far has resolved in favour of the packages copy, which is
the one carrying accountant sign-off — but check, do not assume, and never
bulk-sync one tree onto the other.

Only currency amounts and percentages are compared. Comparing bare integers
drowns the output in statutory section numbers echoed in citation footers.
A label whose figures in one tree are a superset of the other's is ignored as
citation noise; only genuine disagreement in both directions is reported.

Usage: python3 scripts/check-federal-tree-drift.py
"""
import os, re, collections

LABEL = re.compile(r'\*\*([^*]{4,60})\*\*\s*[—:-]\s*([^\n]{0,300})')
NUM   = re.compile(r'(?<![\w.])(?:\$[\d,]+(?:\.\d+)?|\d+(?:\.\d+)?%)')

def facts(path):
    out = collections.defaultdict(set)
    for line in open(path, encoding='utf-8'):
        for m in LABEL.finditer(line):
            lab = re.sub(r'\s+', ' ', m.group(1)).strip().lower()
            v = frozenset(NUM.findall(m.group(2)))
            if v:
                out[lab].add(v)
    return out

rows = []
for fn in sorted(set(os.listdir('skills/federal')) & set(os.listdir('packages/us-federal'))):
    if not fn.endswith('.md'): continue
    a, b = facts('skills/federal/' + fn), facts('packages/us-federal/' + fn)
    for lab in sorted(set(a) & set(b)):
        ua, ub = set().union(*a[lab]), set().union(*b[lab])
        if (ua - ub) and (ub - ua):
            rows.append((fn, lab, sorted(ua), sorted(ub)))
for fn, lab, x, y in rows:
    print('%s :: %s' % (fn, lab))
    print('   skills/  ', x)
    print('   packages/', y)
print('divergent money/percent facts:', len(rows))
