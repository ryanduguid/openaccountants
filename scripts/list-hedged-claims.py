"""List the figures the corpus flags as unverified, so they can be worked in order.

The highest-yield lead this branch found. Ten withholding rates were checked
against outside sources and four were wrong; every one of the four sat on a line
where the guide had already written "approx -- confirm" or "sources vary". A
guide that doubts itself is a better lead than two guides that disagree, because
someone has already done the work of noticing, and nothing in `scripts/` acts on
it.

`check-research-gap-conflicts.py` covers the subset where a sibling guide states
the same figure plainly. This covers the rest, which is most of it: a hedge with
no sibling to contradict it is invisible to every other check here.

Scope. The corpus carries about 3,500 self-hedged lines. Most are prose, and a
hedge on prose is a maintainer's note rather than a figure a reader will act on.
This keeps the ones that carry a number AND sit on a labelled fact, a bullet or
a table row, which is where this corpus states things an agent will use. That is
roughly 900 lines across 180 jurisdictions.

Reading the output. Volume is not severity. Central African Republic tops the
list because its pack was drafted from thin sources and says so on nearly every
line, which is the guide behaving correctly. A single hedge on a headline rate
in a well-covered jurisdiction is worth more than twenty in a pack that hedges
everything. Sort by what a reader would act on, not by count.

What settling one looks like, from the four that were wrong:

  * Belize gave 15% for dividends, interest and royalties and hedged two with
    "sources vary 15%/25%". They vary because interest and royalties are 25%.
  * Trinidad and Tobago hedged interest with "approx -- confirm" and had the
    dividend rates transposed onto it; interest is 15%, not 8%.
  * Iceland led with 12% while its own hedge said "PwC cites 13%". It is 13%.
  * Ethiopia hedged the royalty split as resident against non-resident. The
    split is by kind of royalty: 5% art and culture, 10% otherwise.

And what an honest unresolved one looks like, since some will not settle: Fiji's
dividend rate is 0% under a 2017 exemption and 15% under the Income Tax Act,
with neither source retracting the other. The guide now names both, dates both,
and says which way to err.

Usage: python3 scripts/list-hedged-claims.py [jurisdiction] [--selftest]
"""
import os, re, sys, collections, signal

# This is meant to be piped into head or grep, and a broken pipe is the reader
# leaving early rather than an error.
try:
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
except (AttributeError, ValueError):
    pass

HEDGE = re.compile(r'\(\(?\s*approx[^)]*\)|verify current value|confirm current|'
                   r'position uncertain|not verified against a primary source|'
                   r'sources conflict|sources vary|--\s*confirm|— confirm', re.I)
# A figure a reader would act on: a rate, or an amount with thousands separators.
FIGURE = re.compile(r'\d{1,3}(?:\.\d+)?\s?%|\b\d{1,3}(?:[,\.]\d{3})+\b')
# Where this corpus states facts, as opposed to explaining them.
LABELLED = re.compile(r'^\s*-\s+\*\*([^*]{4,90})\*\*|^\s*\|\s*([^|]{4,90}?)\s*\|')

SKIP = ('orchestrator', 'cross-border', 'verticals', 'integrations')


def hedged_in(line):
    """Return the label of a hedged, labelled figure on this line, else None."""
    m = LABELLED.match(line)
    if not m:
        return None
    if not HEDGE.search(line) or not FIGURE.search(line):
        return None
    return (m.group(1) or m.group(2) or '').strip()


def selftest():
    """Four real lines that were wrong, and three that must not be listed."""
    hits = [
        ('- **Withholding tax — interest to non-residents** — 15% percent ((approx — sources '
         'vary 15%/25%, confirm))', 'Withholding tax — interest to non-residents'),
        ('- **Withholding tax on interest to non-residents** — 10% to non-resident individuals; '
         '8% to non-resident companies (non-treaty) percent ((approx — confirm))',
         'Withholding tax on interest to non-residents'),
        ('| VAT registration threshold | Historically **EGP 500,000** turnover; lowered to '
         'EGP 250,000 — verify current value |', 'VAT registration threshold'),
        ('- **Withholding tax on royalties** — 5% to 10% depending on residency/context % '
         '((approx — confirm split between resident/non-resident))',
         'Withholding tax on royalties'),
    ]
    for line, label in hits:
        assert hedged_in(line) == label, 'read %r from: %s' % (hedged_in(line), line[:60])
    # a hedge with no figure is a maintainer's note, not a claim to verify
    assert hedged_in('- **Filing portal** — Use the online service (approx — confirm the URL)') is None
    # a figure with no hedge is not this list's business
    assert hedged_in('- **WHT on dividends (resident)** — 15% percent') is None
    # prose is not a labelled fact, however hedged
    assert hedged_in('The rate is commonly cited at 20% but sources vary and this is '
                     'approx — confirm before use.') is None
    print('selftest: %d listed, 3 correctly ignored' % len(hits))


def main(only=None):
    per_jur = collections.defaultdict(list)
    for dp, _, fns in os.walk('skills'):
        parts = dp.split(os.sep)
        jur = parts[2] if len(parts) >= 3 else parts[-1]
        if jur in SKIP:
            continue
        for fn in sorted(fns):
            if not fn.endswith('.md'):
                continue
            for i, line in enumerate(open(os.path.join(dp, fn), encoding='utf-8',
                                          errors='replace'), 1):
                label = hedged_in(line)
                if label is not None:
                    per_jur[jur].append((fn, i, label, line.strip()))

    if only:
        for fn, i, label, line in per_jur.get(only, []):
            print('%s:%d\n    %s\n' % (fn, i, line[:300]))
        print('%s: %d hedged figures' % (only, len(per_jur.get(only, []))))
        return

    for jur, rows in sorted(per_jur.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        print('%-28s %3d  %s' % (jur, len(rows),
                                 ', '.join(sorted({r[2][:28] for r in rows})[:3])))
    print('\nhedged figures on labelled facts:', sum(len(v) for v in per_jur.values()))
    print('jurisdictions carrying at least one:', len(per_jur))
    print('\nRun with a jurisdiction name to see its lines.')


if __name__ == '__main__':
    if '--selftest' in sys.argv:
        selftest()
    else:
        main(sys.argv[1] if len(sys.argv) > 1 else None)
