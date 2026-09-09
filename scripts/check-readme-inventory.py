#!/usr/bin/env python3
"""Folder READMEs checked against the folders they describe.

Each guide folder carries a README with a "Files in this folder" table and,
in the US-state packs, a "What's NOT covered" list. Both are claims about the
directory, so both can be checked against it. Nothing else does: the guides
themselves are correct, the validator passes, the index is fresh — the README
is simply describing a folder that has moved on without it.

Three kinds of defect, all found and fixed on this branch:

  phantom      A README advertising a file that does not exist. Four state
               packs listed `<state>-sales-tax-legacy.md` — Florida, Illinois,
               Texas and Washington. Those files have never existed in the
               repository's history.

  omitted      A guide present in the folder but absent from its README. There
               were 97, across 39 of the 55 folders with a README. Michigan's
               listed two of its nine guides; Georgia's listed none of eight.
               A reader consulting the README to see what a pack covers was
               being told a fraction of it.

  false "not   Worse than an omission, because it is an affirmative claim.
  covered"     28 bullets named a topic as out of scope while a guide for it
               sat in the same folder — North Dakota's README said payroll and
               corporate income tax were not covered, with `nd-payroll.md` and
               `nd-corporate-tax.md` beside it; Virginia said the same of
               Form 500 and Form VA-5. An agent reading the README to decide
               whether to load a guide would decline to load one that exists.

A listed slug that resolves to a real file elsewhere in the repository is a
cross-reference, not a phantom, and is not reported — `skills/foundation`
legitimately points at `docs/skill-template.md`.

Usage: python3 scripts/check-readme-inventory.py
Exit status is always 0: this is a review aid, not a gate.
"""
import glob, os, re, signal, sys

try:
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
except (AttributeError, ValueError):
    pass

SLUG = re.compile(r'`([a-z0-9][a-z0-9-]{2,})(?:\.md)?`|\b([a-z0-9][a-z0-9-]{2,})\.md\b')
TOPICS = [
    (re.compile(r'payroll|withholding', re.I), re.compile(r'payroll|withholding')),
    (re.compile(r'corporate income tax|\bCIT\b|corporate tax', re.I), re.compile(r'corporate|excise|franchise')),
    (re.compile(r'estimated tax', re.I), re.compile(r'estimated')),
    (re.compile(r'city income tax|local income tax|Detroit|Grand Rapids', re.I), re.compile(r'detroit|grand-rapids')),
    (re.compile(r'pass-?through|PTE\b|PTET', re.I), re.compile(r'pte|pass-through|ptet')),
    (re.compile(r'formation|incorporat', re.I), re.compile(r'formation')),
    (re.compile(r'return assembly', re.I), re.compile(r'return-assembly')),
]

# every guide slug in the repo, so a cross-reference is not mistaken for a phantom
ALL = {os.path.basename(p)[:-3]
       for p in glob.glob('skills/**/*.md', recursive=True) + glob.glob('docs/**/*.md', recursive=True)}


def main():
    phantom = omitted = false_claims = folders = 0
    for readme in sorted(glob.glob('skills/**/README.md', recursive=True)):
        folder = os.path.dirname(readme)
        if folder in ('skills', os.path.join('skills', 'us-states')):
            continue                      # top-level indexes span subdirectories
        on_disk = [os.path.basename(p)[:-3] for p in sorted(glob.glob(os.path.join(folder, '*.md')))
                   if os.path.basename(p) != 'README.md']
        if not on_disk:
            continue
        folders += 1
        text = open(readme, encoding='utf-8', errors='replace').read()
        listed = {(m.group(1) or m.group(2)) for m in SLUG.finditer(text)} - {'README'}

        ghosts = sorted(s for s in listed - set(on_disk) if s not in ALL)
        gaps = sorted(set(on_disk) - listed)
        if ghosts:
            print('%s\n    lists files that do not exist: %s' % (readme, ', '.join(ghosts)))
            phantom += len(ghosts)
        if gaps:
            print('%s\n    omits guides that are in the folder: %s' % (readme, ', '.join(gaps)))
            omitted += len(gaps)

        block = re.search(r"##\s*What'?s NOT covered(.*?)(?=\n##|\Z)", text, re.S | re.I)
        if block:
            for line in block.group(1).split('\n'):
                bullet = line.strip()
                if not bullet.startswith('-'):
                    continue
                for bullet_re, file_re in TOPICS:
                    if bullet_re.search(bullet):
                        have = [f for f in on_disk if file_re.search(f)]
                        if have:
                            print('%s\n    claims NOT covered: %s\n    but the folder has: %s'
                                  % (readme, bullet[:96], ', '.join(have)))
                            false_claims += 1
                        break

    print('folders checked: %d ; phantom entries: %d ; omitted guides: %d ; false "not covered" claims: %d'
          % (folders, phantom, omitted, false_claims))


main()
