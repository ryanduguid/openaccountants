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
       python3 scripts/list-source-mix.py --unclassified   # allowlist candidates
       python3 scripts/list-source-mix.py --load-bearing   # entries to check first
"""
import os, re, sys, collections

DOMAIN = re.compile(r'https?://([^/\s\)\]>"]+)')

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from oa_tools.sources import (  # noqa: E402  (the classification lives there; see its docstring)
    GOV, NON_GOV_AUTHORITY, AUTHORITY_SUFFIX, NOT_AUTHORITY, classify)

# Any domain on a country-code TLD. Used only by --unclassified, to propose
# candidates for the lists above.
#
# The first version of this pattern required a label of at most seven
# characters, on the theory that authorities use acronyms. Plenty do not:
# financnasprava.sk is the Slovak Financial Administration, cited nine times and
# never once proposed, which is why Slovakia stayed on the zero-authority list
# after the review had corrected its minimum tax against that very site. So did
# legislation.mt, belastingdienst.nl, skatteverket.se, skatteetaten.no and
# guichet.public.lu. The tool built to make an omission visible had the same
# shape of omission inside it.
CC_TLD = re.compile(r'\.[a-z]{2}$')

SKIP_TREES = ('us-states', 'foundation', 'templates', 'patterns', 'orchestrator',
              'cross-border', 'verticals', 'integrations')


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
    assert classify('fin.gov.nt.ca') == 'authority'       # Canadian province
    assert classify('www.finances.gouv.qc.ca') == 'authority'
    assert classify('nts.go.kr') == 'authority'
    assert classify('eur-lex.europa.eu') == 'authority'
    assert classify('www.gov.scot') == 'authority'
    # the government label counts only where the registry puts it
    assert classify('irs.gov.example.com') == 'secondary'
    assert classify('gov.uk.example.com') == 'secondary'
    assert classify('www.gov.example.com') == 'secondary'
    assert classify('taxsummaries.pwc.com') == 'secondary'
    assert classify('ey.com') == 'secondary'
    assert classify('rivermate.com') == 'secondary'
    # the cases the allowlist exists for: authorities that are not on a
    # government domain. The first version of this script scored all of these
    # as secondary, which is how Botswana reached the top of the
    # zero-authority list while citing its own revenue service.
    assert classify('www.nccpl.com.pk') == 'authority'   # collection agent
    assert classify('burs.org.bw') == 'authority'        # Botswana revenue
    assert classify('emta.ee') == 'authority'            # Estonian tax board
    assert classify('frcs.org.fj') == 'authority'        # Fiji revenue
    assert classify('sii.cl') == 'authority'             # Chile SII
    assert classify('mra.mu') == 'authority'             # Mauritius revenue
    # long-named authorities the short-label candidate finder never proposed
    assert classify('financnasprava.sk') == 'authority'   # Slovak Financial Admin
    assert classify('belastingdienst.nl') == 'authority'
    assert classify('skatteverket.se') == 'authority'
    assert classify('legislation.mt') == 'authority'
    # a state gazette publisher on a bare national domain
    assert classify('incv.cv') == 'authority'            # Imprensa Nacional CV
    assert classify('boe.incv.cv') == 'authority'        # and its gazette subdomain
    assert classify('biblio.ohada.org') == 'authority'   # OHADA's own library
    assert classify('ohada.com') != 'authority'          # a different body (UNIDA)
    assert classify('digesto.asamblea.gob.ni') == 'authority'  # via the GOB pattern
    assert classify('lex.uz') == 'authority'             # official legislation
    assert classify('guichet.public.lu') == 'authority'   # via the GOV pattern
    assert classify('mi.government.bg') == 'authority'    # via the GOV pattern
    # every subdomain of the Vietnamese government portal, not just the ones
    # that happen to be cited today
    assert classify('chinhphu.vn') == 'authority'
    assert classify('xaydungchinhsach.chinhphu.vn') == 'authority'
    assert classify('congbao.chinhphu.vn') == 'authority'
    assert classify('notchinhphu.vn') == 'secondary'      # suffix, not substring
    # and the shape-alikes that are not authorities
    assert classify('kstlaw.gr') == 'secondary'           # law firm
    assert classify('taxatlas.io') == 'secondary'         # consultancy
    assert classify('thebhutanese.bt') == 'secondary'     # newspaper
    assert classify('news.err.ee') == 'secondary'         # broadcaster
    assert classify('skatturinn.is') == 'authority'
    # revenue authorities on a bare ccTLD, which the GOV pattern cannot see
    assert classify('www.otr.tg') == 'authority'          # Togo, OTR
    assert classify('www.dgbf.ci') == 'authority'         # Cote d'Ivoire, DGBF
    assert classify('mef.gw') == 'authority'              # Guinea-Bissau, MEF
    assert classify('dgci.mef.gw') == 'authority'         # its tax directorate
    assert classify('kontaktu.mef.gw') == 'authority'     # its legislation portal
    # San Marino: three bare .sm ccTLDs with no "gov" label, the same shape that
    # made otr.tg, dgbf.ci and mef.gw read as commercial. gov.sm already passes
    # on the label; these three do not, and all three are cited by sm-payroll-social.
    assert classify('iss.sm') == 'authority'              # collects the contributions
    assert classify('www.iss.sm') == 'authority'          # and with the www. prefix
    assert classify('consigliograndeegenerale.sm') == 'authority'   # enacts the law
    assert classify('bollettinoufficiale.sm') == 'authority'        # publishes it
    assert classify('gov.sm') == 'authority'              # already passed on "gov"
    # but the .sm domains an earlier pass removed must stay out: the test is
    # being the collector or the publisher, not the country-code TLD.
    assert classify('startup.sm') == 'secondary'          # "San Marino Management Srl"
    assert classify('camcom.sm') == 'secondary'           # mixed public-private capital
    assert classify('belastingdienst.sr') == 'authority'  # Suriname
    assert classify('cnss.dj') == 'authority'             # Djibouti, statutory fund
    assert classify('narodne-novine.nn.hr') == 'authority' # Croatia, Official Gazette
    assert classify('gesetze-im-internet.de') == 'authority'  # German statutes
    assert classify('xrechnung.bund.de') == 'authority'       # bund.de suffix
    assert classify('tax.metro.tokyo.lg.jp') == 'authority'   # lg.jp suffix
    assert classify('andoz.tj') == 'authority'            # Tajikistan
    # Western European law publishers on a bare national domain. Both were
    # scoring 'secondary' while serving the consolidated statute itself, which
    # understated authority coverage for every Dutch and Spanish citation.
    assert classify('wetten.overheid.nl') == 'authority'   # consolidated Dutch law
    assert classify('www.boe.es') == 'authority'           # Spain's official gazette
    assert classify('boe.es') == 'authority'
    # and the near-miss that must NOT be swept in with them
    assert classify('overheid.example.nl') == 'secondary'  # not the .nl platform
    # DELIBERATELY ABSENT: zoek.officielebekendmakingen.nl, which carries the
    # Staatsblad and is plainly the same Dutch government platform — its own
    # pages are titled "Overheid.nl > Officiele bekendmakingen". It is a
    # separate registrable domain, so the overheid.nl entry does not reach it,
    # and no document was successfully retrieved from it here: one request
    # 404'd and one returned 500. A domain that has not served a document is
    # not recorded as an authority on the strength of its name.
    assert classify('zoek.officielebekendmakingen.nl') == 'secondary'

    # boilerplate is not a source
    assert classify('www.openaccountants.com') is None
    assert classify('calendly.com') is None

    # KNOWN LIMIT, and the reason this ranks rather than accuses: a domain test
    # says where a link points, not where a figure came from. A guide can cite
    # an authority's home page beside a rate it took from a summary, and score
    # as well as one that read the authority's rate table. The count is a
    # measure of exposure, not of diligence.
    assert classify('ato.gov.au') == 'authority'

    # A site being about tax in a country does not make it that country's
    # authority. Each of these was on the allowlist and was removed; the first
    # two were the only thing keeping their jurisdiction off the queue.
    assert classify('manao.mg') == 'secondary'            # sells software
    assert classify('www.startup.sm') == 'secondary'      # a private Srl
    assert classify('www.camcom.sm') == 'secondary'       # development agency
    assert classify('www.palgakalkulaator.ee') == 'secondary'   # no publisher
    print('selftest: domain classification passes (1 documented limit)')


def unclassified(minimum=3):
    """Propose allowlist candidates: authority-shaped domains scored secondary.

    The allowlist can only ever be as complete as the last time someone ran
    this. Printing the candidates makes it maintainable from evidence instead
    of from memory, and makes the omission visible rather than silent.

    Two filters keep the general list readable -- at least `minimum` citations,
    and a two-letter country TLD -- and both have hidden real authorities.
    Armenia cited src.am and cba.am once each and stayed on the zero-authority
    list; nibtt.net, svbcur.org, nib-bahamas.com and tonga.tradeportal.org were
    all found by reading a different queue, never by this one, because none of
    them ends in a country TLD. So the filters are skipped entirely for any
    jurisdiction the script is claiming cites no authority at all. That is the
    only place where a missed authority changes the answer, it is where the
    claim is strongest, and 20 jurisdictions' worth of domains is a queue
    somebody will actually read.
    """
    counts, domains = scan()
    seen = collections.Counter()
    for per_jur in domains.values():
        seen.update(per_jur)
    rows = []
    for d, n in seen.items():
        bare = d[4:] if d.startswith('www.') else d
        if (n >= minimum and classify(d) == 'secondary'
                and bare not in NOT_AUTHORITY and CC_TLD.search(bare)):
            rows.append((n, bare))
    for n, d in sorted(rows, reverse=True):
        print('  %4d  %s' % (n, d))
    print()
    print('authority-shaped domains currently counted as secondary:', len(rows))
    print('Check each: a revenue authority belongs in NON_GOV_AUTHORITY, a '
          'firm or unrelated regulator in NOT_AUTHORITY.')

    zero = sorted(j for j, c in counts.items()
                  if c['secondary'] and not c['authority'])
    print()
    print('Every domain cited by a jurisdiction this script calls '
          'zero-authority (%d of them). No minimum, no TLD filter: one '
          'recognised domain here moves a jurisdiction off that list.'
          % len(zero))
    for j in zero:
        ds = sorted(((n, d[4:] if d.startswith('www.') else d)
                     for d, n in domains[j].items()
                     if classify(d) == 'secondary'), reverse=True)
        print('  %s' % j)
        print('     ' + ', '.join('%s (%d)' % (d, n) for n, d in ds))
    return 0


def load_bearing():
    """List allowlist entries a jurisdiction's entire authority score rests on.

    manao.mg is why this exists. It was added from its name, it is a software
    vendor, and it was the ONLY domain scoring as an authority for Madagascar --
    so one unchecked entry removed a jurisdiction from the zero-authority queue
    and nothing in the tool could say so. The same was true of startup.sm and
    camcom.sm for San Marino.

    The asymmetry is the point. A missing entry over-reports risk, and the
    jurisdiction stays on a list somebody reads. A wrong entry under-reports it,
    silently, forever. Sorting the allowlist by what it is holding up says where
    a mistake is expensive, so review effort goes there first.
    """
    counts, domains = scan()
    holds = collections.defaultdict(list)
    for jur, per_jur in domains.items():
        auth = [(d, n) for d, n in per_jur.items() if classify(d) == 'authority']
        if len(auth) != 1:
            continue
        d, n = auth[0]
        bare = d[4:] if d.startswith('www.') else d
        if GOV.search(bare):
            continue          # a .gov domain is not an allowlist judgement
        entry = next((a for a in sorted(NON_GOV_AUTHORITY) + list(AUTHORITY_SUFFIX)
                      if bare == a or bare.endswith('.' + a)), bare)
        holds[entry].append((jur, n, len(per_jur)))
    print('Allowlist entries holding a jurisdiction off the zero-authority '
          'queue on their own (%d):' % len(holds))
    print()
    for entry in sorted(holds, key=lambda e: (-len(holds[e]), e)):
        print('  %s' % entry)
        for jur, n, total in sorted(holds[entry]):
            print('      %-28s cited %d time%s; %d domains cited in all'
                  % (jur, n, '' if n == 1 else 's', total))
    print()
    print('Verify each against the test at the top of this file: does the '
          'domain belong to the body that makes, administers or collects the '
          'charge? If not, remove it -- the jurisdiction belongs on the queue.')
    return 0


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
    elif '--unclassified' in sys.argv:
        sys.exit(unclassified())
    elif '--load-bearing' in sys.argv:
        sys.exit(load_bearing())
    else:
        j = None
        if '--jurisdiction' in sys.argv:
            j = sys.argv[sys.argv.index('--jurisdiction') + 1]
        sys.exit(main(j))
