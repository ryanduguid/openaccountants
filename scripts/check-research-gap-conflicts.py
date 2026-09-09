"""Find a figure one guide calls unknown while a sibling states it as fact.

The corpus carries 1,724 `[RESEARCH GAP -- reviewer to confirm]` markers across
165 guides. They are an honest device, but they are written per-file, and a
country pack is written file by file: nothing stops `x-payroll` from asserting
a number that `x-social-contributions` says cannot be pinned down. An agent
loading both gets told the figure is settled and unsettled at once, and a
practitioner following the cautious guide withholds a treatment the confident
guide applies.

So: within each jurisdiction, collect the distinctive figures that appear
inside a gap-marked sentence, and report those a sibling guide states in a
sentence carrying no marker. This is a reading aid, not a defect list -- a
figure can legitimately be the best available value in one guide and worth
confirming in another. Read the pair before changing anything.

"Distinctive" does real work. Bare years and round numbers recur across
unrelated subjects and drown the signal: including them takes the output from
141 rows to 328, none of the extras meaning anything. So a four-digit number in
1900-2100 is a year, a number that is a leading digit followed by zeros is
round, and neither counts.

What it found, from a row that no longer appears because the conflict behind
it is fixed -- `serbia 10,878,192 -- unknown in serbia-social-contributions,
stated in serbia-income-tax, serbia-payroll`:
the three Serbian guides modelled the annual supplementary tax three different
ways. Two banded it on gross income, one on the base after the non-taxable
amount, and the same taxpayer drew RSD 1,803,398.85 or RSD 1,531,444.05
depending on which guide was loaded. The cautious guide was the correct one.
Inside the same worked example sat `5,439,096 x 10% = 487,450.80` and a
subtraction that went negative and was then used as positive.

Sampling the rest: Mozambique's, Luxembourg's, Slovenia's and Serbia's other
rows are benign -- a real open question sitting near a figure that is not in
doubt. Expect that to be the common case.

Usage: python3 scripts/check-research-gap-conflicts.py [skills]
"""
import os, re, collections, sys

GAP = re.compile(r'\[RESEARCH GAP[^\]]*\]')
NUM = re.compile(r'\b\d{1,3}(?:,\d{3})+(?:\.\d+)?\b|\b\d{4,}(?:\.\d+)?\b|\b\d{1,3}\.\d{1,2}%')

def distinctive(f):
    if f.endswith('%'):
        return True
    d = f.replace(',', '')
    if '.' in d:
        return True
    if len(d) == 4 and 1900 <= int(d) <= 2100:
        return False                                   # a year, not an amount
    return not re.fullmatch(r'[1-9]\d{0,2}0{3,}', d)   # 50,000 / 1,200,000 ...

def main(root):
    gapfigs  = collections.defaultdict(lambda: collections.defaultdict(set))
    factfigs = collections.defaultdict(lambda: collections.defaultdict(set))
    for dp, _, fns in os.walk(root):
        for fn in sorted(fns):
            if not fn.endswith('.md'):
                continue
            p = os.path.join(dp, fn)
            parts = p.split(os.sep)
            if len(parts) < 3:
                continue
            text = open(p, encoding='utf-8', errors='replace').read()
            for s in re.split(r'(?<=[.!?])\s+|\n', text):
                tgt = gapfigs if GAP.search(s) else factfigs
                for f in set(NUM.findall(s)):
                    if distinctive(f):
                        tgt[parts[2]][f].add(p)

    hits = 0
    base = lambda ps: ','.join(sorted(os.path.basename(x) for x in ps))
    for jur in sorted(gapfigs):
        for fig, gfiles in sorted(gapfigs[jur].items()):
            ffiles = factfigs[jur].get(fig, set()) - gfiles
            if ffiles:
                print('%-20s %-13s unknown in %-34s stated in %s'
                      % (jur, fig, base(gfiles), base(ffiles)))
                hits += 1
    print('distinctive figures marked unknown in one guide and stated in a sibling:', hits)
    return hits

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'skills')
