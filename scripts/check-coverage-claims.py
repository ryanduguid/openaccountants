#!/usr/bin/env python3
"""COVERAGE.md's derived table checked against the tree it claims to describe.

docs/COVERAGE.md declares itself "the canonical record of OpenAccountants
coverage numbers", and carries a section headed "This repository (derived from
index.json)". A derived table is only worth having if something re-derives it,
and nothing did — so it drifted the moment the corpus changed.

It had drifted on this branch, from this branch's own work: 1,954 guide files
after one duplicate was removed, and "32 distinct reviewed_by values (29 people
— three are spelled two ways)" after those three were normalised. Both were
correct when written and wrong by the time they were read, which is the whole
argument for checking them rather than maintaining them by hand.

The frozen upstream tables further down the file are NOT checked. They count
the production database rather than this checkout, they say so, and they are
expected to disagree.

Usage: python3 scripts/check-coverage-claims.py

Gate: exits 1 on any row or headline figure that disagrees with the tree
(and on a missing COVERAGE.md or derived section). It has no standing queue,
so it carries no baseline file; --json, --baseline PATH, --no-baseline and
--update-baseline are described in scripts/oa_tools/findings.py. When a
change to skills/ moves the counts, update the figures it names and run it
again until it passes.
"""
import glob, io, json, os, re, signal, sys, unicodedata

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from oa_tools import findings  # noqa: E402

try:
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
except (AttributeError, ValueError):
    pass

DOC = os.path.join('docs', 'COVERAGE.md')


def normalise(name):
    s = unicodedata.normalize('NFKD', name).encode('ascii', 'ignore').decode().lower()
    s = re.sub(r'\b(cpa|ca|acca|crc/sp|cta|cfa|mba|llb|fcca|warrant|malta)\b', ' ', s)
    return ' '.join(sorted(w for w in re.sub(r'[^a-z0-9 ]', ' ', s).split() if len(w) > 1))


def actual():
    data = json.load(open('index.json'))
    guides = data['guides']
    reviewers = {g['reviewed_by'].strip() for g in guides
                 if g.get('reviewed_by') and str(g['reviewed_by']).strip().lower() not in ('pending', 'none')}
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


def main(argv=None):
    parser = findings.argument_parser('coverage-claims', __doc__.split('\n\n')[0], roots=False)
    args = parser.parse_args(argv)
    report = findings.Report('coverage-claims', args)
    doc = DOC.replace(os.sep, '/')

    def problem(path, key, message, **detail):
        report.add(findings.Finding(path, key, message, detail=detail, text=message))

    if not os.path.exists(DOC):
        problem(doc, 'missing', '%s not found' % DOC)
        return report.finish()
    text = io.open(DOC, encoding='utf-8').read()
    block = re.search(r'##\s*This repository \(derived from `index\.json`\)(.*?)(?=\n##)', text, re.S)
    if not block:
        problem(doc, 'derived section', '%s: the derived section is missing' % DOC)
        return report.finish()

    expected, people = actual()
    seen = set()
    for row in re.finditer(r'^\|\s*(.+?)\s*\|\s*\*\*([\d,]+)\*\*(.*?)\|\s*$', block.group(1), re.M):
        label, claimed = row.group(1).strip(), int(row.group(2).replace(',', ''))
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
    m = re.search(r'Distinct `reviewed_by` values \|\s*\*\*\d+\*\*\s*\((\d+) people', block.group(1))
    if m and int(m.group(1)) != len(people):
        problem(doc, 'distinct people', '%s: the reviewer row says %s distinct people, the tree has %d'
                % (DOC, m.group(1), len(people)), claimed=int(m.group(1)), actual=len(people))

    readme_headline(problem)
    report.note('derived coverage rows disagreeing with the tree: %d' % len(report.findings))
    return report.finish()


def readme_headline(problem):
    """The four repo-derived numbers in README.md's opening line.

    The same drift, on the page a reader reaches first, and worse in direction.
    It read "1,798 Guides across 232 jurisdictions - 191 accountant-reviewed -
    36 named accountants" against a tree holding 1,953, 244, 171 and 23. The
    guide and jurisdiction counts understated the corpus, which costs nothing.
    The other two overstated how much of it a practitioner has signed, by 20
    guides and 13 people, and docs/ACCURACY-METHODOLOGY.md exists to say that
    the one claim this project must not inflate is how much review has happened.

    The trailing "questions answered" figure is a website metric and cannot be
    derived from this checkout, so it is left alone.
    """
    if not os.path.exists('README.md'):
        return
    line = None
    for l in io.open('README.md', encoding='utf-8'):
        if 'accountant-reviewed' in l and 'Guides' in l:
            line = l
            break
    if line is None:
        problem('README.md', 'headline', 'README.md: the headline claim line is missing')
        return

    data = json.load(open('index.json'))
    guides = data['guides']

    # Match build-index.py exactly. Counting only a truthy `reviewed_by` was
    # wrong twice over: it ignored the legacy `verified_by` field, and it
    # accepted sentinels like "pending", so this check could disagree with the
    # accountant_reviewed count in the very file it reads.
    unreviewed = {'pending', 'none', 'no', 'false', '-', 'n/a', 'tbd'}

    def reviewer_of(g):
        if str(g.get('tier') or '').strip() != '1':
            return None
        for key in ('reviewed_by', 'verified_by'):
            v = g.get(key)
            if v and str(v).strip().lower() not in unreviewed:
                return str(v).strip()
        return None

    reviewers = {reviewer_of(g) for g in guides}
    reviewers.discard(None)
    # One reviewer asked not to be named, so they are reviewed but not *named*.
    named = {r for r in reviewers if 'name withheld' not in r.lower()}
    want = [('Guides', len(guides)),
            ('jurisdictions', len({g['jurisdiction'] for g in guides if g.get('jurisdiction')})),
            ('accountant-reviewed', data.get('counts', {}).get(
                'accountant_reviewed', sum(1 for g in guides if reviewer_of(g)))),
            ('named accountants', len(named))]
    for label, n in want:
        # the headline bolds the number and its label together: **1,953 Guides**
        m = re.search(r'\*\*([\d,]+)\s+' + re.escape(label) + r'\*\*', line)
        if not m:
            problem('README.md', label, 'README.md: no figure found for "%s"' % label, actual=n)
            continue
        claimed = int(m.group(1).replace(',', ''))
        if claimed != n:
            problem('README.md', label, 'README.md: headline says %s %s, the tree has %s'
                    % (format(claimed, ','), label, format(n, ',')), claimed=claimed, actual=n)


if __name__ == '__main__':
    sys.exit(main())
