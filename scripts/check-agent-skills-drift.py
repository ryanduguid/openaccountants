#!/usr/bin/env python3
"""Measure how far the hand-maintained agent-skills/ tree has drifted from skills/.

The repo holds three copies of the corpus. packages/ is generated from skills/ by
build-packages.py, so it cannot drift — build and diff. agent-skills/ has no
generator: nothing writes it, only the check scripts read it. It is maintained by
hand, and this reports the consequence.

check-tree-divergence.py compares the two copies label by label and finds the
subset that disagree. That understates the problem, because it can only compare a
label that appears in BOTH copies with a single unambiguous value on each side.
A fact that one copy simply does not contain is invisible to it. This measures
the whole relationship instead.

What it found when written: of 747 agent-skills guides with a same-named
counterpart in skills/, **zero** had an identical body, and the largest were a
sixth the size of their counterpart (za-income-tax: 76,439 characters against
11,529). agent-skills is not a stale mirror of skills/ — it is a separate,
thinner and older corpus standing beside the maintained one.

Individual guides were corrected where the drift made them wrong about the
current year — Canada, Israel, Fiji, the UK, Romania, Ireland, Australia — but
the general case is a maintainer decision, not a value-by-value reconciliation:
either agent-skills is generated from skills/ like packages/ is, or it goes.

Usage: python3 scripts/check-agent-skills-drift.py [--list]
Exit status is always 0: this is a review aid, not a gate.
"""
import glob, io, os, re, signal, sys

# stay quiet when piped into head
try:
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
except (AttributeError, ValueError):
    pass

STRIP_FM = re.compile(r'^---.*?^---', re.S | re.M)


def body(path):
    s = io.open(path, encoding='utf-8', errors='replace').read()
    return re.sub(r'\s+', ' ', STRIP_FM.sub('', s)).strip()


def main():
    show_list = '--list' in sys.argv
    by_name = {}
    for p in glob.glob('skills/**/*.md', recursive=True):
        by_name.setdefault(os.path.basename(p)[:-3], p)

    same, unmatched, rows = 0, [], []
    for d in sorted(glob.glob('agent-skills/*/SKILL.md')):
        slug = d.split(os.sep)[1]
        src = by_name.get(slug)
        if src is None:
            unmatched.append(slug)
            continue
        a, b = body(src), body(d)
        if a == b:
            same += 1
        else:
            rows.append((len(a) - len(b), slug, len(a), len(b)))

    print('agent-skills guides with a skills/ counterpart:  %d' % (same + len(rows)))
    print('  body identical to skills/:                    %d' % same)
    print('  body differs from skills/:                    %d' % len(rows))
    print('agent-skills guides with no counterpart by name: %d' % len(unmatched))
    if not rows:
        return
    thinner = [r for r in rows if r[0] > 0]
    print('\nof the differing guides, %d are SHORTER than their skills/ counterpart' % len(thinner))
    half = [r for r in thinner if r[3] < r[2] / 2]
    print('and %d are less than half its length' % len(half))
    print('\nlargest gaps (characters of body text):')
    for gap, slug, la, lb in sorted(rows, reverse=True)[:20 if not show_list else len(rows)]:
        print('  %-42s skills %7d   agent-skills %7d   gap %7d' % (slug, la, lb, gap))


main()
