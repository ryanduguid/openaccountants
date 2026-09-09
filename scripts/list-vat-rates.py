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

Second pass, against the PwC Worldwide Tax Summaries VAT rate chart, which covers
about 150 territories in one page and is far cheaper than one lookup per country.
All of these matched the corpus:

  Peru 18, Ecuador 15, Bolivia 13, Dominican Republic 18, Costa Rica 13,
  Guatemala 12, Honduras 15, El Salvador 13, Nicaragua 15, Mexico 16, Chile 19,
  Argentina 21, Colombia 19, Barbados 17.5, Jamaica 15, Trinidad and Tobago 12.5,
  Bahamas 10, Iceland 24, Albania 20, Serbia 20, Moldova 20, Ukraine 20,
  North Macedonia 18, Bosnia 17, Kosovo 18, Montenegro 21, Georgia 18,
  Armenia 20, Azerbaijan 18, Bangladesh 15, Cambodia 10, Laos 10, Mongolia 10,
  Myanmar 5 (commercial tax, not VAT), Saudi Arabia 15, UAE 5, Bahrain 10,
  Oman 5, Jordan 16, Lebanon 11, Morocco 20, Angola 14, Cameroon 19.25,
  Senegal 18, Ivory Coast 18, Mozambique 16, Namibia 15, Mauritius 15,
  Madagascar 20, Kenya 16, Egypt 14, Nigeria 7.5, Tunisia 19, Uruguay 22,
  Venezuela 16, Israel 18, Greece 24, Pakistan 18 federal goods (15 provincial
  services -- two different taxes), Ghana 15 headline / 20 effective.

Wrong, and fixed:

  * Fiji       12.5% from 1 Aug 2025. fj-income-tax said "15% (from 1 Aug 2024)",
               wrong on rate and date, two changes stale.
  * India      the 12% and 28% GST slabs were abolished 22 Sep 2025. india-gst
               listed them as current in its rate table while its own body
               recorded the abolition.
  * Kazakhstan 16% from 1 Jan 2026. kazakhstan-vat said 12% in twenty places and
               dated its worked examples April 2026.
  * Zimbabwe   15.5% from 1 Jan 2026. zimbabwe-vat said 15% in twelve places
               while zw-tax-overview knew about the rise.

Third pass, PwC chart again plus a global rates page for what it omits. These
matched: Austria 20, Belgium 21, Bulgaria 20, Cabo Verde 15, Chad 18, China 13
(9 and 6 for other categories), Croatia 25, Cyprus 19, Denmark 25, France 20,
Gabon 18, Germany 19, Guyana 14, Hungary 27, Ireland 23, Italy 22, Japan 10,
Latvia 21, Lithuania 21, Luxembourg 17, Malta 18, Mauritania 16, Netherlands 21,
New Zealand 15, Papua New Guinea 10, Philippines 12, Poland 23, Portugal 23,
Rwanda 18, Singapore 9, Slovenia 22, South Africa 15, Spain 21, Sweden 25,
Switzerland 8.1, Taiwan 5, Tanzania 18, Thailand 7, Turkey 20, Uganda 18,
UK 20, Uzbekistan 12, Algeria 19, Ethiopia 15, Nepal 13, South Korea 10,
Bhutan 5 (new GST from 1 Jan 2026).

  * Malawi   17.5% from the start of 2026, raised from 16.5% by the Value Added
             Tax (Amendment) Act 2025 and listed in the MRA's own New Tax
             Measures notice for the Mid-Year Budget Review. Both guides knew
             about the rise but led with "Standard VAT rate (2025) -- 16.5
             percent", so the headline figure was the superseded one. Fixed to
             lead with 17.5%.

Three of the remaining "guides disagree" flags are artefacts worth not chasing
again: Iran is 9% VAT plus 1% municipal tax, and the guides correctly give 9%
as the VAT rate and 10% as the combined rate; Taiwan's 15% is the proposed
global-minimum-tax rate for MNE groups, not VAT (VAT is 5%); Bhutan's 30% is the
corporate rate beside its new 5% GST.

Open: Botswana. A rise to 14% -> 15% was proposed for 1 April 2025 and cannot be
confirmed as enacted; PwC's 2026 chart still shows 14% and BURS serves a bot
check instead of its rate page. The guides state 14% and say so.

Note the shape of the four errors: every one is a jurisdiction where the overview
guide had the right rate and the dedicated VAT guide -- the one an agent loads to
do the work -- did not. That axis is what scripts/check-superseded-rates.py exists
to sweep.

Six of the nine in the first pass were already right, which is the point of
writing the check down:
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
