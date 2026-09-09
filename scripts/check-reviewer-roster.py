#!/usr/bin/env python3
"""Roster files checked against the attribution actually recorded in the guides.

PARTNERS.md and llms.txt both publish, per accountant, a count of the guides
they reviewed. That count is derivable from frontmatter, so the roster can be
checked against the corpus rather than trusted. llms.txt matters most: it is
the file AI agents are pointed at, so a wrong figure there is a claim about a
named professional's sign-off that agents will repeat.

What it found:

  wrong counts     Werner Britz was published as 5 guides against 7 in the
                   corpus, and Mehran Habib as 9 against 13. Both roster files
                   carried the same stale figures.

  split names      Three reviewers were recorded under two spellings each, so
                   any join on the name undercounted them: "Christopher Aryee"
                   (9) beside "Christopher Aryee, CPA" (4) — PARTNERS.md
                   published 4, a third of his real 13. Also Gvantsa Amiridze
                   (5 + 3) and MUHAMMAD HANIS MAT HUSSIN (7 + 1). All are now
                   normalised to the `Name, Credential` form the frontmatter
                   spec requires.

  a disclosed      agent-skills/us-qbi-deduction named a reviewer in its body
  name that        whom skills/ records as "a licensed accountant (name
  should not be    withheld at their request)". The same review, the same
                   guide, two trees, and only one of them honoured the
                   request. The agent-skills copy now matches skills/.

One row is expected to disagree and is documented in PARTNERS.md rather than
reported as an error: that reviewer's 14 guides are attributed anonymously at
his own request, so the frontmatter cannot corroborate the name. The roster
entry stands on his public profile link. Do not "fix" the frontmatter to name
him, and do not delete the row for failing this check.

Usage: python3 scripts/check-reviewer-roster.py
Exit status is always 0: this is a review aid, not a gate.
"""
import collections, io, json, re, signal, sys, unicodedata

try:
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
except (AttributeError, ValueError):
    pass

# documented exception: attributed anonymously at the reviewer's request
ANONYMOUS = {'amir pelinkovic'}


def tokens(name):
    s = unicodedata.normalize('NFKD', name).encode('ascii', 'ignore').decode().lower()
    return set(re.sub(r'[^a-z ]', ' ', s).split())


def corpus_counts():
    data = json.load(open('index.json'))
    counts = collections.Counter()
    for guide in data['guides']:
        for key in ('reviewed_by', 'verified_by'):
            value = guide.get(key)
            if value and isinstance(value, str) and value.strip().lower() not in ('pending', 'none'):
                counts[value.strip()] += 1
    return counts


def best_match(name, counts):
    want, best, score = tokens(name), None, 0
    for candidate in counts:
        overlap = len(want & tokens(candidate))
        if overlap > score:
            best, score = candidate, overlap
    return (counts[best] if score else 0), score


def main():
    counts = corpus_counts()
    problems = 0

    # split spellings undercount everyone who joins on the name
    groups = collections.defaultdict(list)
    for name, n in counts.items():
        stripped = re.sub(r'\b(cpa|ca|acca|crc/sp|cta|cfa|mba|llb|fcca)\b', ' ',
                          unicodedata.normalize('NFKD', name).encode('ascii', 'ignore').decode().lower())
        groups[' '.join(sorted(w for w in re.sub(r'[^a-z ]', ' ', stripped).split() if len(w) > 1))].append((name, n))
    for _, variants in sorted(groups.items()):
        if len(variants) > 1:
            print('reviewer recorded under more than one spelling (total %d): %s'
                  % (sum(n for _, n in variants), ' | '.join('%s (%d)' % v for v in variants)))
            problems += 1

    rows = re.compile(r'\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]*?)\s*\|\s*(\d+)\s*\|')
    for line in io.open('PARTNERS.md', encoding='utf-8'):
        m = rows.match(line)
        if not m:
            continue
        name, claimed = m.group(2), int(m.group(4))
        if name.strip().lower() in ANONYMOUS:
            continue
        got, score = best_match(name, counts)
        if not score or got != claimed:
            print('PARTNERS.md: %s published as %d guides, corpus has %d' % (name, claimed, got))
            problems += 1

    llms = re.compile(r'-\s*\*\*(.+?)\s*\((.+?)\):\*\*\s*(.+?),\s*(\d+) skills')
    for line in io.open('llms.txt', encoding='utf-8'):
        m = llms.search(line)
        if not m:
            continue
        name, claimed = m.group(3).strip(), int(m.group(4))
        if any(a in name.lower() for a in ANONYMOUS):
            continue
        got, score = best_match(name, counts)
        if not score or got != claimed:
            print('llms.txt: %s published as %d skills, corpus has %d' % (name, claimed, got))
            problems += 1

    print('roster rows disagreeing with the corpus:', problems)


main()
