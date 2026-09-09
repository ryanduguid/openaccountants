#!/usr/bin/env python3
"""Compare labelled numeric facts between copies of the same guide in different trees.

Internal checks cannot catch a guide that is self-consistent and simply wrong.
Comparing two copies of the same guide can: where `skills/`, `agent-skills/` and
the hand-authored `packages/us-federal/` all carry a version of one guide, any
figure that differs means at most one side is right.

This is how the Belgian self-employed brackets were caught. Both trees said
"2025" and each was internally consistent, so nothing local flagged them; only
the cross-tree comparison showed 73,447.52/108,238.40 against
73,947.40/109,152.35.

Reading the output — two cautions learned the hard way:

  * A row is compared as its WHOLE numeric vector, because tables in the two
    trees often have different columns. `| Seattle | 3.60% | 10.10% |` carries a
    local rate and a combined rate; comparing only its first cell against a
    one-column table elsewhere compares a local rate to a combined rate and
    "finds" a divergence that is not one. When one side's vector is a superset,
    it is usually an extra column, not a wrong figure.
  * A difference is a lead, not a verdict. Decide which side is right from a
    primary source; do NOT bulk-sync one tree onto the other. Several apparent
    divergences are the two trees covering different tax years.

Bare integers are skipped (they are mostly statute, form and year references,
and comparing them just surfaces citation-formatting noise), as are labels that
look like citations.

Usage:
    python3 scripts/check-tree-divergence.py

Exit status is always 0: this is a review aid, not a gate.
"""
import os,re,sys,collections
LAB=[re.compile(r'^\s*[-*]\s+\*\*(?P<lab>[^*]{4,80}?)\*\*\s*[—–-]+\s*(?P<val>.{1,120})'),
     # capture EVERY remaining cell, not just the first: a row like
     # `| Seattle | 3.60% | 10.10% |` has a local rate AND a combined rate, and
     # comparing only the first cell against a one-column table elsewhere
     # silently compares different quantities.
     re.compile(r'^\s*\|\s*(?P<lab>[^|]{4,80}?)\s*\|(?P<val>.*)$')]
# Only rates and money amounts. Bare integers are usually statute/form/year
# references, and comparing those just surfaces citation-formatting differences.
NUM=re.compile(r'\d+(?:[\.,]\d+)?\s?%|\d{1,3}(?:,\d{3})+(?:\.\d+)?|\d+\.\d{2}\b')
CITE=re.compile(r'\b(irc|reg|regs|notice|pub|publication|t d|rev proc|rev rul|section|form|schedule|instructions|circular|usc|cfr|act|law|code)\b')
YEAR=re.compile(r'^(19|20)\d\d$')
def norm_label(s):
    s=re.sub(r'\*\*|`','',s.lower()); s=re.sub(r'\(.*?\)','',s)
    s=re.sub(r'[^a-z0-9 ]',' ',s)
    return ' '.join(w for w in s.split() if w not in
        {'the','a','an','for','of','in','on','at','to','and','or','is','be'})
def facts(path):
    out=collections.defaultdict(set)
    try: lines=open(path,encoding='utf-8',errors='replace').read().splitlines()
    except OSError: return out
    for line in lines:
        for rx in LAB:
            m=rx.match(line)
            if not m: continue
            lab=norm_label(m.group('lab'))
            if len(lab)<6 or CITE.search(lab): break
            vals=frozenset(x.strip().replace(' ','') for x in NUM.findall(m.group('val'))
                           if not YEAR.match(x.strip().replace(' ','').replace(',','')))
            if vals: out[lab].add(vals)
            break
    return out

pairs=[]
# skills/** <-> agent-skills/<name>/SKILL.md
for dp,dn,fn in os.walk('skills'):
    for f in fn:
        if not f.endswith('.md'): continue
        a=os.path.join(dp,f); b=f'agent-skills/{f[:-3]}/SKILL.md'
        if os.path.exists(b): pairs.append((a,b))
# skills/federal/** <-> packages/us-federal/**
for f in sorted(os.listdir('skills/federal')):
    if f.endswith('.md') and os.path.exists(f'packages/us-federal/{f}'):
        pairs.append((f'skills/federal/{f}', f'packages/us-federal/{f}'))

print(f'guide pairs compared: {len(pairs)}')
div=[]
for a,b in pairs:
    fa,fb=facts(a),facts(b)
    for lab in set(fa)&set(fb):
        va,vb=fa[lab],fb[lab]
        if va!=vb:
            # only flag when each side has a single unambiguous value set
            if len(va)==1 and len(vb)==1:
                sa,sb=next(iter(va)),next(iter(vb))
                if sa and sb and sa!=sb:
                    div.append((a,b,lab,sorted(sa),sorted(sb)))
print(f'labels whose value differs between the two copies: {len(div)}\n')
by=collections.Counter(a for a,_,_,_,_ in div)
for f,c in by.most_common(30): print(f'  {c:3}  {f}')
print()
for a,b,lab,sa,sb in div:
    print(f'--- {lab}\n    {a}: {sa}\n    {b}: {sb}')
