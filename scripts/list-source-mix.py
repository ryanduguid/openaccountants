"""Report which jurisdictions rest entirely on secondary sources.

One publisher carries roughly a third of this corpus's external citations. That
is fine until the summary and the authority differ, and on this branch they have
differed in two distinct ways: a summary that omits a whole head of charge, and
a summary whose prose does not match the schedule the collection agent actually
deducts under. Neither is visible by checking a figure against the source the
guide cites.

So this counts, per jurisdiction, how many citations point at a tax authority
and how many at a secondary source, and lists the jurisdictions with no
authority citation at all. Those carry the most inherited risk.

It ranks, it does not accuse: a secondary source is often right, and an
authority citation does not prove the figures came from it. Always exits 0.

Usage: python3 scripts/list-source-mix.py [--selftest] [--jurisdiction NAME]
"""
import os, re, sys, collections

DOMAIN = re.compile(r'https?://([^/\s\)\]>"]+)')

# Government domains across the naming conventions this corpus actually cites:
# irs.gov, gov.uk, gouv.fr, gob.mx, govt.nz, gc.ca, admin.ch, gv.at, europa.eu,
# and the go.<cc> form used across east Africa and Japan.
GOV = re.compile(
    r'(?:^|\.)(?:gov|gouv|gob|govt|gub|gv)(?:\.|$)'
    r'|(?:^|\.)(?:gc\.ca|admin\.ch|europa\.eu|gouv\.qc\.ca)$'
    r'|(?:^|\.)go\.[a-z]{2}$', re.I)

# Authorities that do not sit on a government domain. Kept short and specific:
# each was added because a real authority publication was being counted as
# secondary. NCCPL is the case that prompted the list -- it is the entity that
# computes and deducts Pakistan's securities CGT, and its notification is more
# authoritative for that tax than any summary of it, but it is a .com.
NON_GOV_AUTHORITY = (
    'nccpl.com.pk',       # Pakistan securities CGT: computes and collects it
    'mufap.com.pk',       # Pakistan mutual funds association, publishes the schedule
    'psx.com.pk',
    'zimra.co.zw',        # Zimbabwe Revenue Authority
    'bnr.rw', 'bnb.bg', 'bnro.ro', 'bportugal.pt',   # central banks
    'ecb.europa.eu', 'nssi.bg', 'nra.bg',
    'skatturinn.is',      # Iceland Revenue and Customs
    'nssi.bg',
    'parliament.gov.pg',
    'nass.gov.ng',
)

# Not sources at all: the CTA block every published guide ends with, and links
# to this repository. Counting them would swamp the measurement -- they are
# roughly 7,500 of the corpus's 16,000 URLs.
BOILERPLATE = ('openaccountants.com', 'calendly.com', 'github.com')

SKIP_TREES = ('us-states', 'foundation', 'templates', 'patterns', 'orchestrator',
              'cross-border', 'verticals', 'integrations')


def classify(domain):
    """'authority', 'secondary', or None for boilerplate."""
    d = domain.lower()
    if d.startswith('www.'):
        d = d[4:]
    if any(b in d for b in BOILERPLATE):
        return None
    if d in NON_GOV_AUTHORITY or GOV.search(d):
        return 'authority'
    return 'secondary'


def scan(root='skills'):
    """Return {jurisdiction: Counter({'authority': n, 'secondary': n})}."""
    out = collections.defaultdict(collections.Counter)
    domains = collections.defaultdict(collections.Counter)
    for dp, _, fns in os.walk(root):
        parts = dp.split(os.sep)
        if len(parts) < 3 or parts[1] in SKIP_TREES:
            continue
        jur = parts[2]
        for fn in sorted(fns):
            if not fn.endswith('.md'):
                continue
            with open(os.path.join(dp, fn), encoding='utf-8', errors='replace') as fh:
                for m in DOMAIN.finditer(fh.read()):
                    kind = classify(m.group(1))
                    if kind:
                        out[jur][kind] += 1
                        domains[jur][m.group(1).lower()] += 1
    return out, domains


def selftest():
    assert classify('irs.gov') == 'authority'
    assert classify('www.gov.uk') == 'authority'
    assert classify('impots.gouv.fr') == 'authority'
    assert classify('sat.gob.mx') == 'authority'
    assert classify('ird.govt.nz') == 'authority'
    assert classify('canada.gc.ca') == 'authority'
    assert classify('estv.admin.ch') == 'authority'
    assert classify('kra.go.ke') == 'authority'
    assert classify('taxsummaries.pwc.com') == 'secondary'
    assert classify('ey.com') == 'secondary'
    assert classify('rivermate.com') == 'secondary'
    # the case the allowlist exists for: a real collection agent on a .com
    assert classify('www.nccpl.com.pk') == 'authority'
    assert classify('skatturinn.is') == 'authority'
    # boilerplate is not a source
    assert classify('www.openaccountants.com') is None
    assert classify('calendly.com') is None

    # KNOWN LIMIT, and the reason this ranks rather than accuses: a domain test
    # says where a link points, not where a figure came from. A guide can cite
    # an authority's home page beside a rate it took from a summary, and score
    # as well as one that read the authority's rate table. The count is a
    # measure of exposure, not of diligence.
    assert classify('ato.gov.au') == 'authority'
    print('selftest: domain classification passes (1 documented limit)')


def main(only=None):
    counts, domains = scan()
    if only:
        c = counts.get(only)
        if not c:
            print('no external citations recorded for %r' % only)
            return 0
        print('%s: %d authority, %d secondary' %
              (only, c['authority'], c['secondary']))
        for d, n in domains[only].most_common():
            print('  %4d  %-40s %s' % (n, d, classify(d) or 'boilerplate'))
        return 0

    zero = sorted(((c['secondary'], j) for j, c in counts.items()
                   if c['authority'] == 0 and c['secondary']), reverse=True)
    for n, j in zero:
        print('  %4d secondary, 0 authority   %s' % (n, j))
    total_a = sum(c['authority'] for c in counts.values())
    total_s = sum(c['secondary'] for c in counts.values())
    print()
    print('jurisdictions with any external citation:', len(counts))
    print('citing no authority domain at all:', len(zero))
    print('citations: %d authority, %d secondary (%.0f%% secondary)'
          % (total_a, total_s, 100.0 * total_s / max(1, total_a + total_s)))
    print('A secondary source is often right, and an authority link does not '
          'prove the figures came from it. This ranks exposure, not diligence.')
    return 0  # never gates CI: citing a summary is not a defect


if __name__ == '__main__':
    if '--selftest' in sys.argv:
        selftest()
    else:
        j = None
        if '--jurisdiction' in sys.argv:
            j = sys.argv[sys.argv.index('--jurisdiction') + 1]
        sys.exit(main(j))
