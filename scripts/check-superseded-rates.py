#!/usr/bin/env python3
"""Find a jurisdiction where one guide records a rate change and a sibling ignores it.

Every rate error found by checking VAT rates against outside sources had the same
shape, and it is not the shape the other checkers look for:

  * Fiji       -- fiji-vat and fj-tax-overview both said 12.5% from 1 Aug 2025.
                  fj-income-tax said "15% (from 1 Aug 2024)", two changes stale.
  * India      -- india-gst's own body said "Former 12% and 28% slabs abolished
                  22 Sep 2025" while its rate table at the top still listed them.
  * Kazakhstan -- kz-tax-overview said "12% in 2025 (rises to 16% from 1 January
                  2026)". kazakhstan-vat said 12% in twenty places, and dated its
                  worked examples April 2026.

In all three the corpus already contained the right answer. It was in the wrong
file, or in the wrong half of the right file, and the copy that a reader would
actually load to do the work was the stale one.

check-tree-divergence.py cannot see this: it compares skills/ against packages/
and agent-skills/, and here all three trees carry the same stale guide. This
compares SIBLINGS INSIDE a jurisdiction instead, which is the axis nothing else
covers.

Method: find sentences that record a rate change -- "rises to 16% from 1 January
2026", "24% (from 1 July 2025; was 22%)", "raised from 17% to 18%", "abolished
22 Sep 2025" -- and take the superseded rate out of them. Then look for a sibling
guide in the same jurisdiction that states that superseded rate as its CURRENT
standard rate. Report the pair.

REGRESSION-TESTED, and it had to be. The first version of this script reported
zero hits across the whole corpus, which looked like good news and was a bug: one
of its patterns captured the new rate but had no group for the old one, so every
match was silently discarded. Run it against the pre-fix content of the three
known cases (git show <commit>:<path> into a scratch tree) and it must report
all three. It does. A checker for a defect class you have already fixed is worth
nothing until you have watched it fail on the unfixed version.

Two false-positive classes are filtered out, both found the same way:

  * Jamaica -- "residential electricity GCT reduced from 15% to 7% (May 2025)"
    does not supersede the 15% standard GCT. A change sentence naming a sector or
    commodity is about a sector rate. Hence SECTOR.
  * Australia -- the 30% company rate got paired with a partnership capital-gains
    note. Both sides must be about the same tax family, and the keyword is often
    only in the filename ("fiji-vat.md"), not the sentence. Hence VATISH over
    line-or-filename.

Corpus result after those filters: one lead, Botswana, where bw-vat-gst and
bw-tax-overview both say 14% and both flag a proposed rise to 15% from 1 April
2025 as unconfirmed. Checked externally and it stays unresolved: secondary
sources split on whether the increase was enacted, and BURS serves a bot check
rather than the rate page. The guides' hedge is the correct treatment and was
left alone -- moving them to 15% on ambiguous evidence would be worse than the
flag they already carry.

A hit is a lead, not a verdict. The legitimate case is a guide deliberately
covering an earlier tax year, so read the frontmatter tax_year before acting, and
check whether the sibling scopes the old rate to a period ("for supplies before
...") rather than asserting it flatly.

Usage: python3 scripts/check-superseded-rates.py [--verbose]
Exit status is always 0: this is a review aid, not a gate.
"""
import glob, io, os, re, sys, collections

# A sentence records a change when it carries change language AND a year from 2023 on.
# Getting old-vs-new right matters more than matching many shapes: an inverted pair
# reports the CURRENT rate as superseded and buries the real hits in noise.
CHANGE_WORD = re.compile(r'\b(rise[sn]?|rises|rising|increase[sd]?|raised|raise|rose|'
                         r'reduce[sd]?|reduction|cut|falls|fell|lowered|abolish(?:ed)?|'
                         r'removed|repealed|replaced|superseded|from)\b', re.I)
YEAR = re.compile(r'\b20(?:2[3-9]|[3-9]\d)\b')
PCT = re.compile(r'(\d{1,2}(?:\.\d+)?)\s?%')
# "<verb> ... to N%" -- N is the NEW rate
TO_NEW = re.compile(r'\b(?:rise[sn]?|rises|increase[sd]?|raised|rose|reduce[sd]?|cut|'
                    r'lowered|falls|fell|changed|moves?|moved)\b[^.\n]{0,40}?\bto\b\s*\**(\d{1,2}(?:\.\d+)?)\s?%', re.I)
# "from X% to Y%" -- X old, Y new
FROM_TO = re.compile(r'\bfrom\b\s*\**(\d{1,2}(?:\.\d+)?)\s?%\s*\**\s*\bto\b\s*\**(\d{1,2}(?:\.\d+)?)\s?%', re.I)
# "was N%" / "previously N%" / "Before that N%" -- N is OLD
WAS_OLD = re.compile(r'\b(?:was|previously|prior(?:ly)?|before that|formerly|had been)\b\s*\**(\d{1,2}(?:\.\d+)?)\s?%', re.I)
# "N% ... abolished/removed/repealed" -- N is OLD, with no replacement named
ABOLISHED = re.compile(r'(\d{1,2}(?:\.\d+)?)\s?%[^.\n]{0,60}?\b(?:abolish(?:ed)?|removed|repealed|scrapped)\b', re.I)


def superseded_in(line):
    """Return {old_rate: new_rate_or_None} recorded by this line."""
    if not (CHANGE_WORD.search(line) and YEAR.search(line)):
        return {}
    out = {}
    m = FROM_TO.search(line)
    if m:
        out[m.group(1)] = m.group(2)
        return out
    m = TO_NEW.search(line)
    new = m.group(1) if m else None
    for w in WAS_OLD.finditer(line):
        out[w.group(1)] = new
    for a in ABOLISHED.finditer(line):
        out.setdefault(a.group(1), new)
    if not out and new:
        # no explicit old rate: take any OTHER percentage in the line as the old one
        others = [x for x in PCT.findall(line) if x != new]
        if len(set(others)) == 1:
            out[others[0]] = new
    return {o: n for o, n in out.items() if o != n}


# a guide asserting a rate as its CURRENT standard rate
CURRENT = re.compile(
    r'(?:\|\s*Standard(?:\s+VAT|\s+GST)?\s+rate\s*\|\s*|'
    r'\*\*Standard(?:\s+VAT|\s+GST)?\s+rate\*\*\s*[\u2014-]\s*|'
    r'\*\*(\d{1,2}(?:\.\d+)?)%\s+rate\*\*\s*[\u2014-]\s*|'
    r'(?:VAT|GST)?\s*standard\s+rate\s+(?:is|of\s+(?:VAT|GST)\s+is)\s+)'
    r'\**(\d{1,2}(?:\.\d+)?)\s?%', re.I)
# A change sentence that names a sector or commodity is about a sector rate, not the
# standard one: Jamaica's "residential electricity GCT reduced from 15% to 7%" does not
# supersede the 15% standard GCT. Australia's company rate got paired with a partnership
# CGT note the same way, so also require the change sentence to be about the same tax
# family as the claim it would supersede.
SECTOR = re.compile(r'\b(electricit|residential|tourism|hotel|accommodation|food|fuel|'
                    r'medicine|medical|pharmac|book|newspaper|transport|agricultur|'
                    r'luxury|sin goods|demerit|capital gain|CGT|partner|payroll|'
                    r'withholding|excise|customs|stamp|property|land)\w*\b', re.I)
VATISH = re.compile(r'\b(VAT|GST|GCT|IVA|NDS|sales tax|value.added)\b', re.I)

SCOPED = re.compile(r'\b(was|before|until|prior|previously|historic|former|abolish|'
                    r'superseded|repealed|removed|no longer|through 3[01]|apply the rate)\b', re.I)


def jurisdiction_of(path):
    parts = path.split(os.sep)
    if len(parts) > 2 and parts[0] == 'skills' and parts[1] == 'international':
        return parts[2]
    if len(parts) > 2 and parts[0] == 'skills' and parts[1] == 'us-states':
        return 'us-' + parts[2]
    return None


def main():
    verbose = '--verbose' in sys.argv
    files = collections.defaultdict(list)
    for p in sorted(glob.glob('skills/**/*.md', recursive=True)):
        j = jurisdiction_of(p)
        if j:
            files[j].append(p)

    hits = 0
    for j in sorted(files):
        superseded = {}          # old rate -> (new rate, file, line, sentence)
        for p in files[j]:
            for n, line in enumerate(io.open(p, encoding='utf-8', errors='replace'), 1):
                if SECTOR.search(line):
                    continue
                for old, new in superseded_in(line).items():
                    superseded.setdefault(old, (new, p, n, line.strip()[:150]))
        if not superseded:
            continue
        for p in files[j]:
            for n, line in enumerate(io.open(p, encoding='utf-8', errors='replace'), 1):
                for m in CURRENT.finditer(line):
                    rate = m.group(1) or m.group(2)
                    if rate not in superseded:
                        continue
                    if SCOPED.search(line):      # the guide scopes it itself
                        continue
                    new, sp, sn, sent = superseded[rate]
                    # both sides must be about the same tax family. The keyword is often
                    # only in the filename ("fiji-vat.md"), not in the line itself, so
                    # take the family from either.
                    def vatish(text, path):
                        return bool(VATISH.search(text) or VATISH.search(os.path.basename(path)))
                    if vatish(line, p) != vatish(sent, sp):
                        continue
                    same = os.path.abspath(sp) == os.path.abspath(p)
                    if same and abs(sn - n) <= 1:
                        continue            # the note sits on the change line itself
                    hits += 1
                    tail = ' -> %s%%' % new if new else ' (abolished)'
                    where = 'THE SAME FILE' if same else 'a sibling'
                    print('%s: states %s%% as current; %s records %s%%%s' % (j, rate, where, rate, tail))
                    print('    stale : %s:%d' % (p, n))
                    print('            %s' % line.strip()[:150])
                    print('    change: %s:%d' % (sp, sn))
                    print('            %s' % sent)
    print('\nsuperseded-rate leads: %d' % hits)


main()
