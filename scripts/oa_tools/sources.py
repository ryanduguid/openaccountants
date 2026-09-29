"""Where a citation points: tax authority, recognised publisher, or neither.

One place for the classification three review aids and one gate share.
``classify(host)`` answers ``'authority'`` for a government domain or one of
the listed non-government authorities (revenue services, statutory funds,
official gazettes and legislation services on bare national domains),
``'secondary'`` for everything else, and ``None`` for the corpus's own
boilerplate links. ``PUBLISHER`` recognises the tax publishers a reader can see
are commentary (and Cornell's LII, which republishes the US Code section
itself). ``cited_hosts(text)`` lists the hostnames a guide cites, skipping URL
templates and anything that is not a hostname, the way
``check-cited-hosts.py`` learned to.

The allowlist below is the corpus's institutional memory: every entry was
added because a real authority was being scored as secondary, and every
removal because a name that looked official was not. Keep the comments with
the entries; they are the evidence. ``list-source-mix.py --unclassified``
proposes candidates and ``--load-bearing`` shows which entries a
jurisdiction's whole score rests on.

Used by ``list-source-mix.py``, ``list-statute-links.py``,
``list-single-source-blocks.py``, ``check-cited-hosts.py`` and the gate
``check-sourcing-floor.py``.
"""

import re

# Stop at whitespace and at the delimiters markdown wraps links in. The
# trailing-punctuation strip below handles "see https://x.gov/y." sentences.
URL = re.compile(r'https?://([^\s/?#\)\]>"\'`,]+)')

# A URL with a placeholder is a template, not an address.
PLACEHOLDER = re.compile(r'[{}<>$]|%[sd]|\.\.\.|XX+|YYYY|\bUF\b')

# The extractor above is deliberately loose, so everything it produces is
# validated against what a hostname can actually be. This is not belt and
# braces -- it is load-bearing, and the first version without it had a 59%
# false-positive rate on its strongest grade:
#
#   * `**https://www.sarsefiling.co.za**` yielded `www.sarsefiling.co.za**`,
#     so the checker reported a host that is demonstrably live as dead.
#   * China's guides write `（https://etax.chinatax.gov.cn）完成提交。...`,
#     and the full-width close paren is not in the stop set, so a whole
#     sentence of Chinese came through as a "hostname".
#
# A hostname in a URL is ASCII: letters, digits, hyphens, dots. An
# internationalised name would already be punycode. Anything else is the
# extractor's fault, not the corpus's, and must never reach the report.
HOSTNAME = re.compile(
    r'^[a-z0-9](?:[a-z0-9-]*[a-z0-9])?'
    r'(?:\.[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)+$')

# Government domains across the naming conventions this corpus actually cites:
# irs.gov, gov.uk, gouv.fr, gob.mx, govt.nz, gc.ca, admin.ch, gv.at, europa.eu,
# the go.<cc> form used across east Africa and Japan, and Canada's provincial
# gov.<province>.ca. The government label must sit where the registry puts it:
# as the top-level domain (.gov) or directly under a country code (gov.uk,
# gob.mx) or under a Canadian province; a label elsewhere in the name
# (irs.gov.example.com, gov.uk.example.com) is whatever registered the domain
# after it, and until 2026-09-29 the pattern matched it anywhere.
GOV = re.compile(
    r'(?:^|\.)gov$'
    r'|(?:^|\.)(?:gov|gouv|gob|govt|gub|gv|go|government|etat|public)\.[a-z]{2}$'
    r'|(?:^|\.)gov\.(?:wales|scot)$'
    r'|(?:^|\.)(?:gc\.ca|admin\.ch|europa\.eu)$'
    r'|(?:^|\.)(?:gov|gouv)\.(?:ab|bc|mb|nb|nl|ns|nt|nu|on|pe|qc|sk|yk)\.ca$', re.I)

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
    'cnss.dj',            # Caisse Nationale de Securite Sociale de Djibouti:
                          # the statutory fund that collects the contributions
                          # the payroll guide cites it for (12 citations, scored
                          # secondary until the sourcing-floor pass of 2026-09-29)
    'narodne-novine.nn.hr',    # Narodne novine, the Official Gazette of the
                          # Republic of Croatia, publisher of the enacted text
                          # (20 citations, likewise)
    # German federal bodies on .de (the sourcing-floor pass of 2026-09-29,
    # German tranche; each page was read for the figures it is cited for)
    'gesetze-im-internet.de',  # Bundesministerium der Justiz: the consolidated
                          # federal statutes (EStG, UStG, AO, GewStG, KStG, SGB)
    'bundesfinanzministerium.de',  # Federal Ministry of Finance (AfA tables,
                          # BMF letters, the Lohnsteuer PAP)
    'bmas.de',            # Federal Ministry of Labour and Social Affairs: the
                          # annual Sozialversicherungs-Rechengroessen
    'bundesgesundheitsministerium.de',  # Federal Ministry of Health: GKV
                          # rates and the average Zusatzbeitrag
    'deutsche-rentenversicherung.de',   # the statutory pension insurer:
                          # contribution rates and ceilings
    'bund.de',            # the federal government domain (xrechnung.bund.de
                          # carries the e-invoicing standard)
    # Japan (the same pass, Japanese tranche)
    'kyoukaikenpo.or.jp', # Japan Health Insurance Association, the statutory
                          # insurer that sets the prefectural health and
                          # nursing-care rates
    'lg.jp',              # every Japanese local government (the Tokyo tax
                          # bureau at tax.metro.tokyo.lg.jp); the .go.jp
                          # national bodies match the government rule
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

# Not sources at all: the CTA block every published guide ends with, and links
# to this repository. Counting them would swamp the measurement -- they are
# roughly 7,500 of the corpus's 16,000 URLs.
BOILERPLATE = ('openaccountants.com', 'calendly.com', 'github.com')

# Destinations a reader can recognise for what they are. Two kinds, and the
# distinction is worth keeping in mind even though both are spared:
#
#   commentary  PwC, KPMG, Chambers, Lexology. You land on tax analysis, and
#               you can see that is what it is.
#   primary text  law.cornell.edu. Cornell's LII is a Cornell Law School
#               programme, not the official publisher -- the US Code is
#               published by the OLRC -- so it is a republisher, in the same
#               position as ZambiaLII. But it republishes the SECTION, not a
#               summary of it: `[§1202](law.cornell.edu/uscode/text/26/1202)`
#               lands the reader on 26 U.S.C. §1202 itself. That is a citation
#               doing its job, and flagging it would be the false positive.
PUBLISHER = re.compile(r'pwc|kpmg|deloitte|ey\.com|bakermckenzie|chambers|'
                       r'grantthornton|pkf|bdo|crowe|mazars|lexology|ibfd|'
                       r'orbitax|taxsummaries|practiceguides|legal500|'
                       r'bloombergtax|law\.cornell\.edu', re.I)


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

# Republishers of the primary text itself, on a domain that is not the state's.
# A link to 26 U.S.C. § 1202 on Cornell's LII lands the reader on the section,
# not on a summary of it, so for the sourcing floor it counts as a statute link
# even though ``classify`` scores the host as secondary (Cornell is not the
# official publisher; the OLRC is).
STATUTE_REPUBLISHERS = frozenset(('law.cornell.edu',))


def publisher(host):
    """Whether a host is a recognised tax publisher (commentary a reader can see)."""
    return bool(PUBLISHER.search(host))


def statute_link(host):
    """Whether a citation to this host reaches an authority or the primary text."""
    if classify(host) == 'authority':
        return True
    d = host.lower()
    if d.startswith('www.'):
        d = d[4:]
    return any(d == s or d.endswith('.' + s) for s in STATUTE_REPUBLISHERS)


def cited_hosts(text):
    """The hostnames a guide cites, as ``check-cited-hosts.py`` extracts them.

    A URL carrying a placeholder is a template and is skipped, and anything the
    loose extractor produces that is not a hostname is dropped rather than
    salvaged.
    """
    out = set()
    for match in URL.finditer(text):
        tail = text[match.start():match.start() + 200].split()[0]
        if PLACEHOLDER.search(tail):
            continue
        host = match.group(1).strip('.,;:*_').lower()
        if HOSTNAME.match(host):
            out.add(host)
    return out
