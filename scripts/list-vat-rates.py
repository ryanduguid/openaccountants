"""List each jurisdiction's stated standard VAT/GST rate, so it can be checked.

The point is what it does *not* do. `check-fact-conflicts.py` finds two guides
that disagree; it cannot find a rate that every guide agrees on and that is
simply wrong, which is the normal case for a country covered by one VAT guide.
This dumps the claim so a human — or a search — can compare it against the
outside world.

Two errors were found this way that no internal check could have caught:
Israel's dedicated VAT guide had 17% (the rate until 31 December 2024) while
two sibling guides had the correct 18%, and Fiji's had 9%, a rate that ended
on 31 July 2023 and has since been replaced twice.

Read the output with care. The regex takes "standard rate" literally, and in
Hong Kong that phrase means the salaries tax standard rate, in Australia it
catches the corporate rate, and a handful of jurisdictions return an artefact
figure. A number here is a claim to verify, not a finding.

Usage: python3 scripts/list-vat-rates.py
"""
import os, re, collections

PAT = re.compile(r'(?:standard(?:\s+VAT|\s+GST)?\s+rate|VAT\s+standard\s+rate|'
                 r'standard\s+rate\s+of\s+(?:VAT|GST))[^.\n|]{0,60}?(\d{1,2}(?:\.\d+)?)\s?%', re.I)

out = collections.defaultdict(collections.Counter)
for dp, _, fns in os.walk(os.path.join('skills', 'international')):
    for fn in fns:
        if not fn.endswith('.md'):
            continue
        p = os.path.join(dp, fn)
        juris = p.split(os.sep)[2]
        for line in open(p, encoding='utf-8', errors='replace'):
            for m in PAT.finditer(line):
                out[juris][m.group(1)] += 1

for juris in sorted(out):
    counts = out[juris]
    flag = '  <-- guides disagree' if len(counts) > 1 else ''
    print('%-24s %s%s' % (juris, ', '.join('%s%% (%d)' % (k, v) for k, v in counts.most_common()), flag))
print('jurisdictions with a stated standard rate:', len(out))
