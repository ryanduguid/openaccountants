#!/usr/bin/env python3
"""The documents' coverage claims checked against the tree they describe.

docs/COVERAGE.md declares itself the canonical record of the repository's
coverage numbers and carries a table "derived from index.json". A derived
table is only worth having if something re-derives it, and nothing did, so it
drifted the moment the corpus changed: 1,954 guide files after one duplicate
was removed, "32 distinct reviewed_by values" after three were normalised.
Both were correct when written and wrong by the time they were read, which
is the whole argument for checking them rather than maintaining them by hand.

The same drift reached the page a reader sees first. README.md's opening line
read "1,798 Guides across 232 jurisdictions - 191 accountant-reviewed - 36
named accountants" against a tree holding 1,953, 244, 171 and 23: the guide
and jurisdiction counts understated the corpus, which costs nothing, and the
other two overstated how much of it a practitioner had signed, by 20 guides
and 13 people. docs/ACCURACY-METHODOLOGY.md exists to say that the one claim
this project must not inflate is how much review has happened.

What is checked, all against index.json and the tree:

  docs/COVERAGE.md       every row of the derived table, the distinct-people
                         figure the reviewer row narrates, and the "N of the N
                         jurisdiction codes" holding accountant-reviewed guides;
  README.md, llms.txt,   the headline line, "**N Guides** across **N
  docs/QUALITY-TIERS.md  jurisdictions** · **N accountant-reviewed** · **N
                         named accountants**", figure by figure;
  PARTNERS.md            that it equals a fresh render from index.json and
                         docs/partners.json (scripts/build-partners.py), and
                         that every profile in docs/partners.json belongs to a
                         reviewer on the roster.

The four review figures come from one rule, scripts/oa_tools/roster.py: a
guide is accountant-reviewed when it carries tier 1 and a reviewer's name,
and a named accountant is such a reviewer who did not ask to be anonymous.

Usage: python3 scripts/check-coverage-claims.py
       python3 scripts/check-coverage-claims.py --write

Gate: exits 1 on any claim that disagrees with the tree (and on a missing
document or derived section). It has no standing queue, so it carries no
baseline file; --json, --baseline PATH, --no-baseline and --update-baseline
are described in scripts/oa_tools/findings.py. When a change to skills/
moves the counts, run `make build`.

--write sets every figure above except PARTNERS.md (build-partners.py writes
that) to the tree's value and exits 0. `make build` runs it after
build-index.py, so the figures are derived output like the index, and
scripts/merge-main.py masks them when it merges a branch.
"""
import glob, io, os, re, signal, sys, unicodedata

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from oa_tools import findings, roster  # noqa: E402

try:
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
except (AttributeError, ValueError):
    pass

# Every path is relative to the working directory, as CI runs the checker
# from the repository root and the tests run it from a throwaway corpus.
DOC = os.path.join('docs', 'COVERAGE.md')
HEADLINE_FILES = ('README.md', 'llms.txt', os.path.join('docs', 'QUALITY-TIERS.md'))
PARTNERS = 'PARTNERS.md'
PROFILES = os.path.join('docs', 'partners.json')

# What the gate reads and --write rewrites. The section runs to the next heading.
SECTION = re.compile(r'##\s*This repository \(derived from `index\.json`\)(.*?)(?=\n##)', re.S)
ROW = re.compile(r'^(\|\s*(.+?)\s*\|\s*\*\*)([\d,]+)(\*\*.*?\|\s*)$', re.M)
PEOPLE = re.compile(r'(Distinct `reviewed_by` values \|\s*\*\*[\d,]+\*\*\s*\()(\d+)( people)')
REVIEWED_IN = re.compile(r'(Accountant-reviewed guides exist in )([\d,]+)( of the )([\d,]+)( jurisdiction codes)')
HEADLINE = re.compile(r'\*\*[\d,]+\s+Guides\*\*')


def normalise(name):
    s = unicodedata.normalize('NFKD', name).encode('ascii', 'ignore').decode().lower()
    s = re.sub(r'\b(cpa|ca|acca|crc/sp|cta|cfa|mba|llb|fcca|warrant|malta)\b', ' ', s)
    return ' '.join(sorted(w for w in re.sub(r'[^a-z0-9 ]', ' ', s).split() if len(w) > 1))


def actual(index):
    guides = index['guides']
    reviewers = {roster.reviewer_value(g.get('reviewed_by')) for g in guides}
    reviewers.discard(None)
    return {
        'Guide files indexed': len(guides),
        'Distinct `jurisdiction` codes': len({g['jurisdiction'] for g in guides if g.get('jurisdiction')}),
        '`tier: 1` (accountant-reviewed)': sum(1 for g in guides if g.get('tier') == 1),
        '`tier: 2` (source-cited draft)': sum(1 for g in guides if g.get('tier') == 2),
        'Distinct `reviewed_by` values': len(reviewers),
        'Country directories under `skills/international/`':
            len([p for p in glob.glob(os.path.join('skills', 'international', '*')) if os.path.isdir(p)]),
        'US jurisdiction codes (`US` + 50 states + DC)':
            len({g['jurisdiction'] for g in guides if (g.get('jurisdiction') or '').startswith('US')}),
        # packages/_shared/ holds the files the bundles share; it is not a bundle.
        'Generated bundles under `packages/`':
            len([p for p in glob.glob(os.path.join('packages', '*'))
                 if os.path.isdir(p) and os.path.basename(p) != '_shared']),
    }, {normalise(r) for r in reviewers}


def figures(index):
    """Every figure the documents state, as the tree has it."""
    table, people = actual(index)
    guides = index['guides']
    return {
        'table': table,
        'people': len(people),
        'reviewed in': len({g['jurisdiction'] for g in guides if g.get('jurisdiction') and roster.reviewer_of(g)}),
        'headline': roster.headline(guides),
    }


def rewrite(path, text, want):
    """``text``, the content of ``path``, with every figure the gate reads set
    to ``want`` (from figures()). All other text is left as it is."""
    path = path.replace(os.sep, '/')
    if path == DOC.replace(os.sep, '/'):
        block = SECTION.search(text)
        if not block:
            return text
        table = want['table']
        body = ROW.sub(lambda m: m.group(1) + format(table[m.group(2).strip()], ',') + m.group(4)
                       if m.group(2).strip() in table else m.group(0), block.group(1))
        body = PEOPLE.sub(lambda m: m.group(1) + str(want['people']) + m.group(3), body)
        body = REVIEWED_IN.sub(lambda m: m.group(1) + format(want['reviewed in'], ',') + m.group(3)
                               + format(table['Distinct `jurisdiction` codes'], ',') + m.group(5), body)
        return text[:block.start(1)] + body + text[block.end(1):]
    if path in {name.replace(os.sep, '/') for name in HEADLINE_FILES}:
        lines = text.splitlines(True)
        for i, line in enumerate(lines):
            if HEADLINE.search(line):
                for label in roster.HEADLINE_LABELS:
                    line = re.sub(r'\*\*[\d,]+(\s+' + re.escape(label) + r'\*\*)',
                                  lambda m: '**' + format(want['headline'][label], ',') + m.group(1), line)
                lines[i] = line
                break
        return ''.join(lines)
    return text


def write_figures(index):
    """--write: set the figures in each document to ``index``'s values."""
    want = figures(index)
    for path in (DOC,) + HEADLINE_FILES:
        if not os.path.isfile(path):
            continue  # the gate reports a missing document
        with io.open(path, encoding='utf-8', newline='') as fh:
            text = fh.read()
        new = rewrite(path, text, want)
        if new != text:
            with io.open(path, 'w', encoding='utf-8', newline='') as fh:
                fh.write(new)
            print('figures updated: %s' % path.replace(os.sep, '/'))
    return 0


def main(argv=None):
    parser = findings.argument_parser('coverage-claims', __doc__.split('\n\n')[0], roots=False)
    parser.add_argument('--write', action='store_true',
                        help="set the documents' figures to the tree's values and exit 0 (make build runs it)")
    args = parser.parse_args(argv)
    if args.write:
        if not os.path.isfile('index.json'):
            sys.exit('index.json not found; run python3 scripts/build-index.py')
        return write_figures(roster.load_index('index.json'))
    report = findings.Report('coverage-claims', args)

    def problem(path, key, message, **detail):
        report.add(findings.Finding(path.replace(os.sep, '/'), key, message, detail=detail, text=message))

    if not os.path.isfile('index.json'):
        problem('index.json', 'missing', 'index.json not found; run python3 scripts/build-index.py')
        return report.finish()
    index = roster.load_index('index.json')

    index_integrity(problem, index)
    derived_table(problem, index)
    headline_claims(problem, index)
    partners_fresh(problem, index)
    report.note('claims disagreeing with the tree: %d' % len(report.findings))
    return report.finish()


def index_integrity(problem, index):
    """Raw tier counts must not describe rows without a reviewer as reviewed."""
    for guide in index['guides']:
        if guide.get('tier') == 1 and roster.reviewer_of(guide) is None:
            path = guide.get('path') or guide.get('slug') or '<unknown guide>'
            problem('index.json', 'tier 1 without reviewer: ' + path,
                    f'index.json: {path}: tier 1 requires a real reviewer', guide=path)


def derived_table(problem, index):
    doc = DOC.replace(os.sep, '/')
    if not os.path.exists(DOC):
        problem(doc, 'missing', '%s not found' % DOC)
        return
    text = io.open(DOC, encoding='utf-8').read()
    block = SECTION.search(text)
    if not block:
        problem(doc, 'derived section', '%s: the derived section is missing' % DOC)
        return

    expected, people = actual(index)
    seen = set()
    for row in ROW.finditer(block.group(1)):
        label, claimed = row.group(2).strip(), int(row.group(3).replace(',', ''))
        if label not in expected:
            continue
        seen.add(label)
        if claimed != expected[label]:
            problem(doc, label, '%s: "%s" says %s, the tree has %s'
                    % (DOC, label, format(claimed, ','), format(expected[label], ',')),
                    claimed=claimed, actual=expected[label])

    for label in expected:
        if label not in seen:
            problem(doc, label, '%s: the derived table has no row for "%s" (tree value %s)'
                    % (DOC, label, format(expected[label], ',')), actual=expected[label])

    # the reviewer-count row also narrates how many distinct people that is
    m = PEOPLE.search(block.group(1))
    if m and int(m.group(2)) != len(people):
        problem(doc, 'distinct people', '%s: the reviewer row says %s distinct people, the tree has %d'
                % (DOC, m.group(2), len(people)), claimed=int(m.group(2)), actual=len(people))

    # the sentence under the table says how many codes hold accountant-reviewed guides
    m = REVIEWED_IN.search(block.group(1))
    if not m:
        problem(doc, 'reviewed jurisdictions', '%s: the derived section has no "Accountant-reviewed guides exist in '
                'N of the N jurisdiction codes" sentence' % DOC)
    else:
        claimed = [int(m.group(2).replace(',', '')), int(m.group(4).replace(',', ''))]
        tree = [figures(index)['reviewed in'], expected['Distinct `jurisdiction` codes']]
        if claimed != tree:
            problem(doc, 'reviewed jurisdictions', '%s: says accountant-reviewed guides exist in %s of the %s '
                    'jurisdiction codes, the tree has %s of %s' % (DOC, claimed[0], claimed[1], tree[0], tree[1]),
                    claimed=claimed, actual=tree)


def headline_claims(problem, index):
    """The four repo-derived numbers in the headline line of each headline file.

    README.md opens with it; llms.txt states it for agents; QUALITY-TIERS.md's
    inventory repeats it. All three bold the number and its label together
    (**1,953 Guides**), so one regex reads all three, and one rule
    (scripts/oa_tools/roster.py) supplies the values. The trailing "questions
    answered" figure upstream publishes is a website metric that cannot be
    derived from this checkout, so it is left alone.
    """
    want = roster.headline(index['guides'])
    for path in HEADLINE_FILES:
        doc = path.replace(os.sep, '/')
        if not os.path.exists(path):
            problem(doc, 'missing', '%s not found' % doc)
            continue
        # the first line that bolds a guide count with its label is the headline
        line = None
        for candidate in io.open(path, encoding='utf-8'):
            if HEADLINE.search(candidate):
                line = candidate
                break
        if line is None:
            problem(doc, 'headline', '%s: the headline claim line is missing' % doc)
            continue
        for label in roster.HEADLINE_LABELS:
            n = want[label]
            m = re.search(r'\*\*([\d,]+)\s+' + re.escape(label) + r'\*\*', line)
            if not m:
                problem(doc, label, '%s: no figure found for "%s"' % (doc, label), actual=n)
                continue
            claimed = int(m.group(1).replace(',', ''))
            if claimed != n:
                problem(doc, label, '%s: headline says %s %s, the tree has %s'
                        % (doc, format(claimed, ','), label, format(n, ',')), claimed=claimed, actual=n)


def partners_fresh(problem, index):
    """PARTNERS.md is generated; a hand edit or a stale copy is a finding."""
    profiles = roster.load_profiles(PROFILES)
    fresh, unused = roster.render_partners(index, profiles)
    for name in unused:
        problem(PROFILES, name, '%s: %r is on no accountant-reviewed guide; remove the profile or fix the guide'
                % (PROFILES.replace(os.sep, '/'), name))
    if not os.path.isfile(PARTNERS):
        problem(PARTNERS, 'missing', '%s not found; run python3 scripts/build-partners.py' % PARTNERS)
        return
    committed = io.open(PARTNERS, encoding='utf-8').read()
    if committed != fresh:
        problem(PARTNERS, 'stale', '%s differs from a fresh render of index.json and %s; '
                'regenerate: python3 scripts/build-partners.py' % (PARTNERS, PROFILES.replace(os.sep, '/')))


if __name__ == '__main__':
    sys.exit(main())
