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
"""
import os, re, sys, collections

DOMAIN = re.compile(r'https?://([^/\s\)\]>"]+)')

# Government domains across the naming conventions this corpus actually cites:
# irs.gov, gov.uk, gouv.fr, gob.mx, govt.nz, gc.ca, admin.ch, gv.at, europa.eu,
# and the go.<cc> form used across east Africa and Japan.
GOV = re.compile(
    r'(?:^|\.)(?:gov|gouv|gob|govt|gub|gv|government|etat|public)(?:\.|$)'
    r'|(?:^|\.)(?:gc\.ca|admin\.ch|europa\.eu|gouv\.qc\.ca)$'
    r'|(?:^|\.)go\.[a-z]{2}$', re.I)

# Authorities that do not sit on a government domain. Kept short and specific:
# each was added because a real authority publication was being counted as
# secondary. NCCPL is the case that prompted the list -- it is the entity that
# computes and deducts Pakistan's securities CGT, and its notification is more
# authoritative for that tax than any summary of it, but it is a .com.
# The list below was built by measurement, not by guessing: every entry is a
# domain this corpus actually cites at least three times. The first version of
# this script had only a handful and consequently reported that 76% of citations
# were secondary and that 41 jurisdictions cited no authority at all. Both were
# wrong. Botswana was top of that list while citing burs.org.bw, its own revenue
# service; Estonia's tax board (emta.ee) is the corpus's most-cited authority
# after the IRS and scored as secondary. Run --unclassified to re-derive
# candidates when guides are added; this list will always be incomplete, which
# is a reason to read it as a floor on authority citations, never a ceiling.
NON_GOV_AUTHORITY = frozenset((
    # Revenue and tax administrations
    'emta.ee',            # Estonian Tax and Customs Board
    'frcs.org.fj',        # Fiji Revenue and Customs Service
    'rsl.org.ls',         # Revenue Services Lesotho
    'gra.gm',             # Gambia Revenue Authority
    'mra.mu',             # Mauritius Revenue Authority
    'mra.mw',             # Malawi Revenue Authority
    'dgi.bf',             # Burkina Faso, Direction Generale des Impots
    'impots.cm',          # Cameroon, Direction Generale des Impots
    'sii.cl',             # Chile, Servicio de Impuestos Internos
    'zimra.co.zw',        # Zimbabwe Revenue Authority
    'ers.org.sz',         # Eswatini Revenue Service
    'namra.org.na',       # Namibia Revenue Agency
    'zra.org.zm',         # Zambia Revenue Authority
    'burs.org.bw',        # Botswana Unified Revenue Service
    'vero.fi',            # Finnish Tax Administration
    'skat.dk',            # Danish tax administration
    'skatturinn.is',      # Iceland Revenue and Customs
    'aade.gr',            # Greek Independent Authority for Public Revenue
    'anaf.ro',            # Romanian National Agency for Fiscal Administration
    'vmi.lt',             # Lithuanian State Tax Inspectorate
    'rs.ge',              # Georgia Revenue Service
    'ros.ie',             # Irish Revenue Online Service
    'altinn.no',          # Norwegian government reporting portal
    'canada.ca',          # Government of Canada
    'eesti.ee', 'gub.uy', 'impo.com.uy',   # state portals and official gazette
    # Collection agents: not the tax authority, but the body that computes and
    # deducts the tax, whose notification outranks any summary of it.
    'nccpl.com.pk', 'mufap.com.pk', 'psx.com.pk',
    # Statutory social-security and pension bodies. The corpus cites these for
    # contribution rates, which they set and publish.
    'sodra.lt', 'nssi.bg', 'nra.bg', 'cnps.cm', 'nssa.org.zw',
    'myfnpf.com.fj', 'nis.org.gy', 'epf.lk', 'etfb.lk', 'vnpf.com.vu',
    'nppf.org.bt', 'sshfc.gm', 'nassit.org.sl', 'ssnit.org.gh', 'npf.ws',
    'bipa.na', 'cleiss.fr',
    # Central banks, cited for official conversion rates
    'ecb.europa.eu', 'bnr.rw', 'bnb.bg', 'bnro.ro', 'bportugal.pt',
    # Legislatures, cited for the statute itself
    'parliament.gov.pg', 'nass.gov.ng',
    # Third pass, after widening the candidate finder to any country-code TLD
    # rather than short labels only.
    'financnasprava.sk',  # Financial Administration of the Slovak Republic
    'slovensko.sk',       # Slovak government portal
    'legislation.mt',     # Malta, official legislation
    'irishstatutebook.ie',
    'ministere-finances.dj',   # Djibouti Ministry of Finance
    'skatteverket.se',    # Swedish Tax Agency
    'skatteetaten.no',    # Norwegian Tax Administration
    'belastingdienst.nl', # Netherlands Tax Administration
    'finances.belgium.be',
    'bmf-steuerrechner.de',    # German Federal Ministry of Finance calculator
    'riksdagen.se', 'parliament.lk',
    'cabinet.salyk.kz',   # Kazakhstan tax portal (salyk = tax)
    'ciregistry.ky',      # Cayman Islands registry
    'rdb.rw', 'org.rdb.rw', 'businessprocedures.rdb.rw',   # Rwanda Development Board
    'en.caisses-sociales.mc',  # Monaco social funds
    'socialsecurity.org.bz', 'pensionfund.sc', 'sozialfonds.li',
    'mirovinsko.hr', 'pensionikeskus.ee', 'palgakalkulaator.ee',
    # Second pass over --unclassified. Tajikistan reached the zero-authority
    # list while citing andoz.tj, its own tax committee, for the same reason
    # Botswana did.
    'andoz.tj',           # Tajikistan, Tax Committee (andoz = tax)
    'manao.mg',           # Madagascar tax portal
    'revenue.ie',         # Irish Revenue Commissioners
    'ontario.ca',         # Government of Ontario
    'enpf.co.sz',         # Eswatini National Provident Fund
    'cnps.ci',            # Cote d'Ivoire social security
    'pacra.org.zm',       # Zambia companies registry
    'cipa.co.bw',         # Botswana Companies and IP Authority
    'camcom.sm',          # San Marino chamber of commerce (business registry)
    'nrbf.to',            # Tonga National Retirement Benefits Fund
    'boi.org.il',         # Bank of Israel
    'moj.gm',             # Gambia Ministry of Justice
    'startup.sm',         # San Marino government startup portal
    'lmis.gm',            # Gambia labour market information (government)
))

# Whole domains where every subdomain is the same authority. chinhphu.vn is the
# Government of Vietnam's portal and its subdomains carry the gazette
# (congbao), the consolidated legislation (vanban) and the policy explainers
# (xaydungchinhsach) -- listing them one by one would go stale on the next
# guide that cites a fourth.
AUTHORITY_SUFFIX = ('chinhphu.vn', 'quochoi.vn')

# Domains that look like an authority by shape but are not: professional firms,
# and bodies that regulate something other than what the guide cites them for.
NOT_AUTHORITY = frozenset((
    # Professional firms and commercial publishers whose domain shape looks
    # like an authority's. pwc.co.za and pwc.com.cy are the same publisher as
    # taxsummaries.pwc.com wearing a country-code TLD.
    'pwc.co.za', 'pwc.com.cy', 'kstlaw.gr', 'hlb.al', 'misha.pe', 'qhrm.io',
    'nexus.ua',
    'nevo.co.il',         # commercial Israeli legal database
    'andina.pe',          # state news agency: reports law, does not make it
    'vfsc.vu',            # financial services regulator, not the tax authority
    'lndc.org.ls', 'msm.org.ls', 'koda.ee',
    # Consultancies and law firms on country-code TLDs
    'taxatlas.io', 'commenda.io', 'quaderno.io', 'bridgewest.eu', 'eurofast.eu',
    'goldblum.ch', 'zmayetlaw.co.ls', 'saotomeexpert.pt', '1office.co',
    'toccacelibronzetti.sm', 'aplusconsulting.com.kh', 'atlasconsulting.gr',
    'saaccounting.me', 'caspianlegalcenter.az', 'en.legal-force.uz',
    'tax-legal.uz', 'accounting.az', 'businessnorway.uk', 'impuestos.com.bo',
    # News organisations and community wikis: they report law, they do not make
    # it, and a paraphrase in a newspaper is a secondary source however official
    # the outlet.
    'thebhutanese.bt', 'elheraldo.hn', 'dailypost.vu', 'news.err.ee',
    'cubadebate.cu', 'kolzchut.org.il',
    'grantthornton.lv', 'grantthornton.com.cw', 'pkf.trunco.com.np',
))

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
    if d in NOT_AUTHORITY:
        return 'secondary'
    if (d in NON_GOV_AUTHORITY or GOV.search(d)
            or any(d == a or d.endswith('.' + a) for a in AUTHORITY_SUFFIX)):
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


def unclassified(minimum=3):
    """Propose allowlist candidates: authority-shaped domains scored secondary.

    The allowlist can only ever be as complete as the last time someone ran
    this. Printing the candidates makes it maintainable from evidence instead
    of from memory, and makes the omission visible rather than silent.
    """
    _, domains = scan()
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
    else:
        j = None
        if '--jurisdiction' in sys.argv:
            j = sys.argv[sys.argv.index('--jurisdiction') + 1]
        sys.exit(main(j))
