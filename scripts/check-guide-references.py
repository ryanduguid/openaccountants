"""Find inline `guide-slug` references that point at a guide which does not exist.

`validate-guides.py` checks the `depends_on` frontmatter. It does not look at
the far more numerous references written in prose — "see `us-federal-payroll`",
"load `ny-estimated-tax-it-2105`", execution sequences that name a series of
guides to run in order. An agent following one of those finds nothing, and a
human wastes the time it takes to search.

This found 47 distinct dangling references across 88 uses. Most were naming
drift rather than missing content: the guide existed under a different slug
(`us-federal-payroll` for `us-form-941-940-payroll`, `nl-btw-return` for
`nl-vat-return`, `us-federal-ny-return-assembly` for `us-ny-return-assembly`).
Those were repaired. The rest name guides this repository does not contain and
are now marked as such in place, so the pointer still tells a reader what they
need while making clear it is not here.

Do not resolve these by string distance. A fuzzy matcher offered
`senegal-payroll` for `us-federal-payroll` and `ne-income-tax` for
`france-income-tax`; every repair in this branch was made by looking up what
actually exists.

Known false positive: a backticked token can be a workflow *slot* name rather
than a guide — `state-payroll` in co-payroll.md is one.

Usage: python3 scripts/check-guide-references.py
"""
import os, re, collections

TAXISH = re.compile(r'(tax|vat|payroll|income|corporate|return|formation|crypto|invoice|'
                    r'social|assembly|intake|base|matrix|credit|estimated|gst|nexus)')
REF = re.compile(r'`([a-z][a-z0-9]*(?:-[a-z0-9]+){1,6})`')

names = set()
for dp, _, fns in os.walk('skills'):
    for fn in fns:
        if fn.endswith('.md'):
            names.add(fn[:-3])
if os.path.isdir('agent-skills'):
    names |= {d for d in os.listdir('agent-skills') if os.path.isdir(os.path.join('agent-skills', d))}

bad, loc = collections.Counter(), {}
for dp, _, fns in os.walk('skills'):
    for fn in fns:
        if not fn.endswith('.md'):
            continue
        p = os.path.join(dp, fn)
        for i, line in enumerate(open(p, encoding='utf-8', errors='replace'), 1):
            for m in REF.finditer(line):
                r = m.group(1)
                if not TAXISH.search(r) or r in names:
                    continue
                bad[r] += 1
                loc.setdefault(r, (p, i))

for r, c in bad.most_common():
    p, i = loc[r]
    print('%-40s %3dx  first: %s:%d' % (r, c, p, i))
print('distinct dangling references: %d   total uses: %d' % (len(bad), sum(bad.values())))
