#!/usr/bin/env python3
"""Report labelled percentage facts that disagree between guides in one pack.

scripts/detect-contradictions.py knows four jurisdictions (AU, DE, UK, US) and
a hand-curated concept list. This is the jurisdiction-agnostic complement: it
learns the labels from the corpus itself, so it covers all 244 jurisdictions
without anyone maintaining a concept list.

For every guide it extracts `- **Label** - value` bullets and `| Label | value |`
table rows whose value holds exactly one percentage, normalises the label, and
groups by (pack, label). A group whose files disagree is reported.

Every conflict is worth a look because at most one value can be right for a
given fact — but a conflict is not proof of an error. Generic labels ("reduced",
"higher", "standard", "minimum tax") collide across genuinely different taxes,
which is the dominant false positive. Read both sides before editing.

Values carrying a year, a range, or a list are skipped, since those are usually
deliberate multi-year tables rather than competing claims.

Usage:
    python3 scripts/check-fact-conflicts.py

Exit status is always 0: this is a review aid, not a gate.
"""
import os,re,sys,collections
LABELLED=[
 re.compile(r'^\s*[-*]\s+\*\*(?P<lab>[^*]{4,70}?)\*\*\s*[—–-]+\s*(?P<val>[^_\n]{1,60})'),
 re.compile(r'^\s*\|\s*(?P<lab>[^|]{4,70}?)\s*\|\s*(?P<val>[^|]{1,60}?)\s*\|'),
]
PCT=re.compile(r'(\d{1,3}(?:[\.,]\d{1,3})?)\s?%')
STOP=re.compile(r'(?:19|20)\d\d')
def norm_label(s):
    s=s.lower()
    s=re.sub(r'\(.*?\)','',s)
    s=re.sub(r'[^a-z ]',' ',s)
    s=re.sub(r'\b(the|a|an|for|of|in|on|at|to|and|or|is|rate|rates)\b',' ',s)
    return ' '.join(s.split())
def pack_of(path):
    p=path.split('/')
    if p[0]=='skills' and p[1]=='international': return 'int:'+p[2]
    if p[0]=='skills' and p[1]=='us-states': return 'us:'+p[2]
    if p[0]=='skills': return 'skills:'+p[1]
    return None
facts=collections.defaultdict(list)
for dp,dn,fn in os.walk('skills'):
    for f in sorted(fn):
        if not f.endswith('.md'): continue
        path=os.path.join(dp,f); pack=pack_of(path)
        if not pack: continue
        for i,line in enumerate(open(path,encoding='utf-8',errors='replace'),1):
            if '%' not in line: continue
            for rx in LABELLED:
                m=rx.match(line)
                if not m: break
                lab=norm_label(m.group('lab')); val=m.group('val')
                if len(lab)<6: break
                pcts=PCT.findall(val)
                # single unambiguous percentage only; skip ranges/lists/year-tagged
                if len(pcts)!=1 or STOP.search(val): break
                v=pcts[0].replace(',','.')
                facts[(pack,lab)].append((float(v), path, i, line.strip()[:120]))
                break
conflicts=[]
for k,v in facts.items():
    vals={x[0] for x in v}
    files={x[1] for x in v}
    if len(vals)>1 and len(files)>1: conflicts.append((k,v,vals))
print(f'labelled percentage facts extracted: {sum(len(v) for v in facts.values())}')
print(f'distinct (pack,label) keys: {len(facts)}')
print(f'keys where files disagree: {len(conflicts)}\n')
for (pack,lab),v,vals in sorted(conflicts, key=lambda c:-len({x[1] for x in c[1]}))[:40]:
    print(f'### {pack} :: "{lab}"  -> {sorted(vals)}')
    seen=set()
    for val,path,i,txt in v:
        if (val,path) in seen: continue
        seen.add((val,path))
        print(f'      {val:>7}%  {path}:{i}')
