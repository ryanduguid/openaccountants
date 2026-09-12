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
# The test for an entry: the domain belongs to the body that MAKES,
# ADMINISTERS or COLLECTS the charge the guide cites it for, or publishes the
# official text of the law. Not "the site is about tax in that country".
#
# The first version of this script had only a handful of entries and
# consequently reported that 76% of citations were secondary and that 41
# jurisdictions cited no authority at all. Both were wrong. Botswana was top of
# that list while citing burs.org.bw, its own revenue service; Estonia's tax
# board (emta.ee) is the corpus's most-cited authority after the IRS and scored
# as secondary. Andorra and Kosovo were still on the list while citing
# impostos.ad and atk-ks.org.
#
# Every correction went the same way -- the corpus cites more authority than the
# checker could see -- until a code review found manao.mg on this list, added
# from its name as a "Madagascar tax portal". Manao sells management software.
# It was Madagascar's ONLY scored authority, so one wrong entry took a
# jurisdiction off the queue this script exists to produce. Three more went the
# same way: startup.sm (San Marino Management Srl), camcom.sm (a mixed
# public-private S.p.A.) and palgakalkulaator.ee, a salary calculator with no
# stated publisher, cited as the source for Estonia's statutory minimum wage.
#
# So the error runs in both directions, and they are not symmetric. A missing
# entry over-reports risk and someone eventually notices; a wrong entry silently
# removes a jurisdiction from the queue, and nothing ever looks at it again.
# Run --load-bearing to see which entries a jurisdiction's whole score rests on:
# check those hardest, because those are the ones a mistake hides. Run
# --unclassified to re-derive candidates when guides are added. This list will
# always be incomplete, which is why the authority count is a floor.
NON_GOV_AUTHORITY = frozenset((
    # Official gazette publishers and legal-information services. State bodies
    # that publish the law itself, on a domain that carries no government
    # suffix — the same blind spot the revenue authorities below sat in.
    'incv.cv',            # Imprensa Nacional de Cabo Verde (Boletim Oficial)
    'overheid.nl',        # The Dutch government's own publishing platform.
                          # wetten.overheid.nl carries the CONSOLIDATED text of
                          # every Dutch act, and zoek.officielebekendmakingen.nl
                          # the Staatsblad. There is no .gov.nl or .go.nl — the
                          # Netherlands publishes its law on a bare .nl, so the
                          # suffix rules below cannot see it.
    'boe.es',             # Boletin Oficial del Estado — Spain's official
                          # gazette and the publisher of its consolidated
                          # legislation. Again a bare national domain: Spain
                          # has no .gob.es requirement for the BOE itself.
    'ohada.org',          # OHADA itself — the Journal Officiel and the digital
                          # library that carries it. Supranational rather than
                          # national, so no country suffix to recognise it by;
                          # its uniform acts ARE the company law of seventeen
                          # member states. Note ohada.com is a different body
                          # (the UNIDA association) and is deliberately absent.
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
    'vinhi.vg',           # BVI National Health Insurance: its own bulletin of
                          # 12 Sep 2024 sets the ceiling the guide cites
                          # (US$102,000 a year, 3.75% + 3.75%).
    'iss.sm',             # San Marino, Istituto per la Sicurezza Sociale: the
                          # body that collects the contributions and publishes
                          # the annual "redditi minimi ed aliquote contributive"
                          # circular. Not to be confused with startup.sm and
                          # camcom.sm, both removed from this list as commercial
                          # or mixed-capital bodies -- a .sm domain is not the
                          # test, being the collector is.
    # Fourth pass, over the destinations the statute-link checker was calling
    # marketing sites. Each of these is the body that computes and collects the
    # charge the guide quotes, publishing its own contribution page.
    'vissb.vg',           # Virgin Islands Social Security Board
    'nibtt.net',          # National Insurance Board of Trinidad and Tobago
    'nib-bahamas.com',    # National Insurance Board of The Bahamas
    'svbcur.org',         # Sociale Verzekeringsbank Curacao (AOV/AWW/BVZ)
    'nationalsif.netlify.app',   # South Sudan National Social Insurance Fund;
                                 # a statutory fund on free hosting is still
                                 # the statutory fund.
    'obr.bi',             # Office Burundais des Recettes
    'llv.li',             # Liechtenstein Landesverwaltung (Steuerverwaltung)
    'prh.fi',             # Finnish Patent and Registration Office, trade register
    'tonga.tradeportal.org',     # hosts the Laws of Tonga: the Consumption Tax
                                 # Act CAP. 26.02 s.5(3)(a) is the 15% the
                                 # guide cites, in full, as a PDF.
    # Armenia. The guides were already citing the revenue committee and the
    # central bank while the jurisdiction sat on the zero-authority list.
    'arlis.am',           # ARLIS, the official legal information system
    'src.am',             # State Revenue Committee
    'e-register.am',      # state business register
    'cba.am',             # Central Bank of Armenia
    # Andorra and Kosovo, both on the zero-authority list while citing their
    # own tax administrations -- found by listing what those jurisdictions
    # actually cite rather than by filtering on domain shape.
    'impostos.ad',        # Andorra, Departament de Tributs i Fronteres
    'e-govern.ad',        # Andorran government portal
    'atk-ks.org',         # Administrata Tatimore e Kosoves (and etax. portal)
    'bqk-kos.org',        # Central Bank of the Republic of Kosovo
    'rks-gov.net',        # Kosovo government, including gzk.rks-gov.net, the
                          # Official Gazette. Hyphenated into rks-gov, so "gov"
                          # is not a label of its own and the GOV pattern -
                          # which matches whole dot-separated labels - misses
                          # the entire national domain.
    'egov.mv',            # Maldives government portal; "egov" is not "gov"
                          # either. Requiring a whole label is still right:
                          # it is what keeps rigobertoparedes.com, a Honduran
                          # law firm, out of the authority count.
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
    'consigliograndeegenerale.sm',  # San Marino's parliament, publishing the
                          # text of the laws it enacts in its own archive
    'bollettinoufficiale.sm',       # San Marino's Official Bulletin
    'lex.uz',             # Uzbekistan, official national legislation database
    'cabinet.salyk.kz',   # Kazakhstan tax portal (salyk = tax)
    'ciregistry.ky',      # Cayman Islands registry
    'rdb.rw', 'org.rdb.rw', 'businessprocedures.rdb.rw',   # Rwanda Development Board
    'en.caisses-sociales.mc',  # Monaco social funds
    'socialsecurity.org.bz', 'pensionfund.sc', 'sozialfonds.li',
    'mirovinsko.hr',
    'pensionikeskus.ee',  # AS Pensionikeskus is a private company, but it is
                          # the statutory registrar of the II pillar and where
                          # the employee's 2/4/6% election is made, so it
                          # administers the charge the guides cite it for.
    # Second pass over --unclassified. Tajikistan reached the zero-authority
    # list while citing andoz.tj, its own tax committee, for the same reason
    # Botswana did.
    'andoz.tj',           # Tajikistan, Tax Committee (andoz = tax)
    'revenue.ie',         # Irish Revenue Commissioners
    'ontario.ca',         # Government of Ontario
    'enpf.co.sz',         # Eswatini National Provident Fund
    'cnps.ci',            # Cote d'Ivoire social security
    'pacra.org.zm',       # Zambia companies registry
    'cipa.co.bw',         # Botswana Companies and IP Authority
    'nrbf.to',            # Tonga National Retirement Benefits Fund
    'boi.org.il',         # Bank of Israel
    'moj.gm',             # Gambia Ministry of Justice
    'lmis.gm',            # Gambia Labour Market Information System, run by the
                          # Ministry of Trade, Industry, Employment and Regional
                          # Integration with GBoS, the NTA and the SSHFC.
    # Fifth pass. These came out of the STATUTE-LINK queue rather than from
    # --unclassified: that checker reports "names a statute, lands somewhere
    # that is not an authority", so reading its destinations is a way of asking
    # this list what it is missing. Each was fetched and read before adding.
    'u.ae',               # "The Official Platform of the UAE Government", run
                          # by UAE mGovernment. Sits directly on the national
                          # TLD with no "gov" label, so GOV cannot see it.
    'nssfug.org',         # Uganda National Social Security Fund: the statutory
                          # fund that collects the contribution, publishing the
                          # NSSF Act Cap 230 and its regulations on its own site.
    # Legal information institutes are NOT a class -- the network is mixed, and
    # the test splits it. These two are run by state bodies:
    'eswatinilii.org',    # "operated by the Judiciary of eSwatini"
    'namiblii.org',       # "a project of the Law Reform and Development
                          # Commission", Namibia's statutory law-reform body.
    'belastingdienst.sr', # "Belasting Dienst - Suriname": the national tax
                          # service, publishing BTW, Loonbelasting and
                          # Inkomstenbelasting guidance, the Wetten and its
                          # Beschikkingen. belastingdienst.nl was already here
                          # for the Netherlands; the Surinamese one sits on a
                          # bare .sr with no "gov" label, and was the only
                          # external citation the whole jurisdiction had.
    # Sixth pass. Found by the SINGLE-SOURCE queue rather than --unclassified:
    # after the Togo guides were rewritten against the statute, that queue
    # reported all five of them as resting on "neither an authority nor a
    # recognised publisher" -- naming the revenue authority itself. A checker
    # that calls the Office Togolais des Recettes a commercial host will do the
    # same to the next jurisdiction whose authority sits on a bare ccTLD.
    'otr.tg',             # Office Togolais des Recettes: Togo's revenue
                          # authority, which assesses and collects the taxes and
                          # publishes the consolidated Code General des Impots
                          # et Livre des Procedures Fiscales. Bare .tg, no "gov"
                          # label, so GOV cannot see it.
    'dgbf.ci',            # Direction generale du Budget et des Finances,
                          # Ministere des Finances et du Budget, Cote d'Ivoire:
                          # publishes the enacted annexe fiscale to each loi de
                          # finances -- the official text of the amending law.
                          # Found the same way otr.tg was, one commit later:
                          # citing it moved Cote d'Ivoire's guides OFF the
                          # single-source queue and the corpus's secondary share
                          # UP. Twice in one session is not a coincidence; a
                          # francophone African ministry on a bare ccTLD is a
                          # shape this pattern cannot see, and the next one will
                          # arrive the same way.
    'mef.gw',             # Ministerio da Economia e Financas, Guinea-Bissau,
                          # and with it dgci.mef.gw (Direccao Geral das
                          # Contribuicoes e Impostos, the tax authority) and
                          # kontaktu.mef.gw (its portal, which serves the
                          # CONSOLIDATED tax codes with superseded wording struck
                          # through and each amending law named in-line). The
                          # prediction written beside dgbf.ci above -- "the next
                          # one will arrive the same way" -- came true on the
                          # next jurisdiction opened, and it was a lusophone
                          # ministry rather than a francophone one, so the shape
                          # is a bare ccTLD, not a language. Subdomains are
                          # matched, so all three count from this one entry.
))

# Removed from the list above after a code review, and kept here so the same
# names are not re-proposed from their shape. Each was scored as an authority
# and is not one; the first two were the only thing keeping their jurisdiction
# off the zero-authority queue.
#
#   manao.mg            Manao sells accounting and payroll software (Madagascar)
#   startup.sm          "(c) San Marino Management Srl", a private company
#   camcom.sm           "societa a capitale misto pubblico-privato" -- an
#                       economic development agency, not the Ufficio Tributario
#   palgakalkulaator.ee a salary calculator naming no publisher, cited as the
#                       source for Estonia's statutory minimum wage
#
# Considered in the fifth pass and NOT added, each for a stated reason, so the
# same names are not proposed again from their shape:
#
#   zambialii.org       The LII network is not homogeneous. EswatiniLII is run
#                       by the Judiciary and NamibLII by a statutory commission,
#                       so both are on the list above; ZambiaLII is "hosted by
#                       the Southern African Institute for Policy and Research
#                       (SAIPAR), an independent, educational and development
#                       oriented research centre" and "collects cases indirectly
#                       from the Zambian judiciary". An excellent republisher,
#                       but not the official publisher of the law.
#   dlb.az              Reads as an Azerbaijani state body; it is "DLB
#                       Consulting", selling corporate services.
#   nasfund.com.pg      A licensed PNG superannuation fund with shareholders and
#                       its own Deed -- one fund among several, not the body
#                       that imposes the charge. Contrast nrbf.to above.
#   onrc.ro,            Romania's trade register and Lithuania's Centre of
#   registrucentras.lt  Registers, both almost certainly authorities -- but one
#                       answers with a WAF rejection and the other with a
#                       Cloudflare challenge, so neither could be read. Left off
#                       deliberately: adding a domain because its name and
#                       reputation fit is exactly how manao.mg got here.

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
    # Suffix, not equality: etax.atk-ks.org is the Kosovo tax administration's
    # own filing portal and info.altinn.no is Norway's reporting portal, and an
    # exact-match test scored both as commercial sites.
    if (GOV.search(d)
            or any(d == a or d.endswith('.' + a) for a in NON_GOV_AUTHORITY)
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
