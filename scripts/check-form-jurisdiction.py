"""Flag a form number cited in one jurisdiction that belongs to another.

Written after two of this class turned up by hand: a North Dakota payroll guide
telling the taxpayer to pay estimates on **Form 540-ES**, which is California's,
and a Detroit guide naming a "Form 5125" that does not exist in the city series.
A form number is exactly the kind of detail that reads as authoritative and is
never recomputed by a reader.

The heuristic: learn each form token's home jurisdiction from where it is used
across the corpus, then report a token used once or twice in state A while used
six or more times in state B, where B accounts for at least 75% of all its uses.

**Most output is not an error.** Federal forms legitimately appear in state
guides; state matrices legitimately cite every state's forms; reciprocity
sections legitimately cite a neighbouring state's withholding certificate (a
Maryland payroll guide citing Virginia's VA-4 is correct); and some numbers
genuinely collide — Georgia and Maryland both have a Form 500. Read the cited
line before concluding anything.

Usage: python3 scripts/check-form-jurisdiction.py
"""
import os, re, collections
FORM = re.compile(r'\bForm\s+([A-Z0-9][A-Z0-9\-\./]{1,14}[A-Z0-9])\b')
def juris(p):
    parts = p.split(os.sep)
    if 'us-states' in parts: return 'us-' + parts[parts.index('us-states')+1]
    if 'international' in parts: return parts[parts.index('international')+1]
    if 'federal' in parts: return 'us-federal'
    return parts[1] if len(parts) > 1 else '?'
use = collections.defaultdict(collections.Counter)   # form -> juris -> count
where = collections.defaultdict(list)
for dp,_,fns in os.walk('skills'):
    for fn in fns:
        if not fn.endswith('.md'): continue
        p = os.path.join(dp, fn); j = juris(p)
        for i,line in enumerate(open(p,encoding='utf-8',errors='replace'),1):
            for m in FORM.finditer(line):
                f = m.group(1).rstrip('.')
                use[f][j] += 1
                where[(f,j)].append((p,i))
sus = []
for f, js in use.items():
    if len(js) < 2: continue
    tot = sum(js.values())
    home, hn = js.most_common(1)[0]
    if hn / tot < 0.75: continue                   # no dominant home jurisdiction
    for j, n in js.items():
        if j == home: continue
        if n <= 2 and hn >= 6 and j.startswith('us-') and home.startswith('us-'):
            sus.append((f, j, n, home, hn))
for f, j, n, home, hn in sorted(sus, key=lambda r: -r[4]):
    p,i = where[(f,j)][0]
    print('Form %-10s cited in %-8s (%dx) but is %s\'s form (%dx)  ->  %s:%d' % (f, j, n, home, hn, p, i))
print('candidates:', len(sus))
