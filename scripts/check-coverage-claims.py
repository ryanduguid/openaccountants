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
Exit status is always 0: this is a review aid, not a gate.
"""
import glob, io, json, os, re, signal, sys, unicodedata

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
        'US jurisdiction codes (`US` + 50 states + DC + `US-NY-NYC`)':
            len({g['jurisdiction'] for g in guides if (g.get('jurisdiction') or '').startswith('US')}),
        'Generated bundles under `packages/`':
            len([p for p in glob.glob(os.path.join('packages', '*')) if os.path.isdir(p)]),
    }, {normalise(r) for r in reviewers}


def main():
    if not os.path.exists(DOC):
        print('%s not found' % DOC)
        return
    text = io.open(DOC, encoding='utf-8').read()
    block = re.search(r'##\s*This repository \(derived from `index\.json`\)(.*?)(?=\n##)', text, re.S)
    if not block:
        print('%s: the derived section is missing' % DOC)
        return

    expected, people = actual()
    problems = 0
    seen = set()
    for row in re.finditer(r'^\|\s*(.+?)\s*\|\s*\*\*([\d,]+)\*\*(.*?)\|\s*$', block.group(1), re.M):
        label, claimed = row.group(1).strip(), int(row.group(2).replace(',', ''))
        if label not in expected:
            continue
        seen.add(label)
        if claimed != expected[label]:
            print('%s: "%s" says %s, the tree has %s'
                  % (DOC, label, format(claimed, ','), format(expected[label], ',')))
            problems += 1

    for label in expected:
        if label not in seen:
            print('%s: the derived table has no row for "%s" (tree value %s)'
                  % (DOC, label, format(expected[label], ',')))
            problems += 1

    # the reviewer-count row also narrates how many distinct people that is
    m = re.search(r'Distinct `reviewed_by` values \|\s*\*\*\d+\*\*\s*\((\d+) people', block.group(1))
    if m and int(m.group(1)) != len(people):
        print('%s: the reviewer row says %s distinct people, the tree has %d'
              % (DOC, m.group(1), len(people)))
        problems += 1

    print('derived coverage rows disagreeing with the tree:', problems)


main()
