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

Checked externally so far (do not re-derive these from the corpus):

  * Israel   18%    -- the dedicated VAT guide had 17%, the rate until 31 Dec 2024.
  * Fiji     12.5%  -- from 1 Aug 2025; 15% ran 1 Aug 2023 - 31 Jul 2025, and the
                       9% before that ended 31 Jul 2023. fj-income-tax still said
                       "15% (from 1 Aug 2024)", wrong on the rate AND the date.
  * Russia   22%    -- from 1 Jan 2026, Federal Law No. 425-FZ. CORRECT in the
                       corpus; the 20% hits are its own historical notes.
  * Finland  25.5%  -- from 1 Sep 2024. CORRECT; the 24% hit is a historical note.
  * Slovakia 23%    -- from 1 Jan 2025 (reduced 10% abolished, new 19%). CORRECT.
  * Romania  21%    -- from 1 Aug 2025, reduced rates consolidated to 11%. CORRECT.
  * Vietnam  10%    -- standard, with the 2% cut to 8% extended to 31 Dec 2026 by
                       Resolution 204/2025/QH15 and Decree 174/2025/ND-CP. CORRECT.
  * Estonia  24%    -- permanent from 1 Jul 2025; 22% ran 1 Jan 2024 - 30 Jun 2025.
  * Indonesia       -- 12% nominal from 1 Jan 2025 but PMK 131/2024 sets the base at
                       11/12 for non-luxury supplies, so 11% effective. CORRECT, and
                       stated with that nuance.

Six of the nine were already right, which is the point of writing the check down:
"the corpus disagrees with itself" and "the corpus is wrong" are different
questions, and a rate flagged here is a claim to verify, not a defect found.

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
