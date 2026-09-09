#!/usr/bin/env python3
"""Guides filed under the wrong jurisdiction.

Two-letter codes collide. MA is Morocco and Massachusetts, ID is Indonesia and
Idaho, IN is India and Indiana. When a guide is placed by its slug prefix rather
than by what it actually covers, it lands in another country's pack and every
consumer downstream inherits the mistake -- the package bundle, index.json,
llms-full.txt and any agent that loads by jurisdiction.

Nothing else in the repo catches this. The content is internally consistent, the
arithmetic is sound, the rates are right for the jurisdiction the body describes.
Only the label is wrong, and a rate check cannot see a label.

Two independent tests, because each is blind where the other sees:

  consensus   A guide whose frontmatter `jurisdiction` disagrees with the modal
              jurisdiction of its own directory. Self-calibrating: it needs no
              country-name-to-ISO-code table, because each directory votes on
              what it is. Blind when the frontmatter and the directory are wrong
              together.

  filename    A guide named for a US state that sits in a different state's
              directory. This is what catches the "wrong together" case, and it
              found the systematic bug: four sales-tax guides had been filed by
              the FIRST TWO LETTERS OF THE FILENAME rather than the state code,
              so arizona-* went to ar/ (Arkansas), connecticut-* to co/
              (Colorado), and maine-* and maryland-* both to ma/ (Massachusetts).
              Where the first two letters happen to match -- arkansas/ar,
              colorado/co, massachusetts/ma -- placement was correct by accident.

What it found, all now moved:

  * us-states/id/id-income-tax.md was the **Indonesian** PPh Orang Pribadi
    guide -- tier 1, accountant-reviewed by a named reviewer -- carrying an
    Idaho description. It was Indonesia's ONLY personal income tax guide, and it
    was being served as Idaho's. Moved to international/indonesia/.
  * us-states/in/in-income-tax.md was a second copy of the **India** income tax
    guide with an Indiana description. Removed: international/india/ already
    covers India, and better.
  * international/morocco/ma-payroll.md was **Massachusetts** payroll --
    DFML, EMAC, Form M-941, MA PIT -- with jurisdiction US-MA, sitting in
    Morocco's pack. Zero Morocco references in 97 Massachusetts ones. Moved to
    us-states/ma/, which had no payroll guide at all.
  * the four misfiled sales-tax guides above, moved with their jurisdictions
    corrected from US-AR/US-CO/US-MA to US-AZ/US-CT/US-ME/US-MD.

Idaho and Indiana are left with no individual income tax guide. That is an
honest coverage gap, recorded in their READMEs, and better than a guide whose
description says Idaho and whose body is denominated in rupiah.

Usage: python3 scripts/check-jurisdiction-placement.py
Exit status is always 0: this is a review aid, not a gate.
"""
import collections, glob, os, signal, sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
from frontmatter_yaml import load_frontmatter  # noqa: E402

try:
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
except (AttributeError, ValueError):
    pass

STATES = {
    'alabama': 'al', 'alaska': 'ak', 'arizona': 'az', 'arkansas': 'ar', 'california': 'ca',
    'colorado': 'co', 'connecticut': 'ct', 'delaware': 'de', 'florida': 'fl', 'georgia': 'ga',
    'hawaii': 'hi', 'idaho': 'id', 'illinois': 'il', 'indiana': 'in', 'iowa': 'ia',
    'kansas': 'ks', 'kentucky': 'ky', 'louisiana': 'la', 'maine': 'me', 'maryland': 'md',
    'massachusetts': 'ma', 'michigan': 'mi', 'minnesota': 'mn', 'mississippi': 'ms',
    'missouri': 'mo', 'montana': 'mt', 'nebraska': 'ne', 'nevada': 'nv', 'ohio': 'oh',
    'oklahoma': 'ok', 'oregon': 'or', 'pennsylvania': 'pa', 'tennessee': 'tn', 'texas': 'tx',
    'utah': 'ut', 'vermont': 'vt', 'virginia': 'va', 'washington': 'wa', 'wisconsin': 'wi',
    'wyoming': 'wy',
}


def frontmatter(path):
    text = open(path, encoding='utf-8', errors='replace').read()
    if not text.startswith('---'):
        return None
    end = text.find('\n---', 3)
    if end < 0:
        return None
    try:
        data = load_frontmatter(text[3:end])
    except Exception:
        return None
    return data if isinstance(data, dict) else None


def main():
    problems = 0

    by_dir = collections.defaultdict(list)
    for path in sorted(glob.glob('skills/**/*.md', recursive=True)):
        parts = path.split(os.sep)
        if len(parts) < 4 or parts[1] not in ('international', 'us-states'):
            continue
        if os.path.basename(path) in ('README.md', 'references.md'):
            continue
        data = frontmatter(path)
        if not data:
            continue
        code = data.get('jurisdiction')
        if isinstance(code, str) and code.strip():
            by_dir[os.sep.join(parts[:3])].append((path, code.strip().upper()))

    for dirname in sorted(by_dir):
        counts = collections.Counter(code for _, code in by_dir[dirname])
        if len(counts) == 1:
            continue
        mode, n = counts.most_common(1)[0]
        for path, code in by_dir[dirname]:
            if code != mode:
                print('%s\n    jurisdiction %s, but its directory is %d x %s' % (path, code, n, mode))
                problems += 1

    for path in sorted(glob.glob(os.path.join('skills', 'us-states', '*', '*.md'))):
        here = path.split(os.sep)[2]
        base = os.path.basename(path)[:-3]
        for name, code in STATES.items():
            if base.startswith(name + '-') and code != here:
                print('%s\n    named for %s (%s) but sits under us-states/%s'
                      % (path, name.title(), code.upper(), here))
                problems += 1

    print('directories scanned: %d ; misplaced guides: %d' % (len(by_dir), problems))


main()
