"""The one counting rule for accountant review, and the roster derived from it.

Four files used to say who had reviewed what, and each counted differently:
PARTNERS.md counted a reviewer's name on any tier, llms.txt copied figures by
hand, README.md counted ``tier: 1`` plus a name, and the index builder had its
own copy of that last rule. The counts drifted apart the moment the corpus
moved. This module is the single definition. ``build-index.py`` counts
``accountant_reviewed`` with it, ``check-coverage-claims.py`` checks the
headline figures in README.md, llms.txt and docs/QUALITY-TIERS.md with it, and
``build-partners.py`` writes PARTNERS.md from it.

The rule: a guide is accountant-reviewed when its frontmatter carries an
explicit ``tier: 1`` and a reviewer's name in ``reviewed_by`` (or the legacy
``verified_by``) that is not a placeholder. A name on a ``tier: 2`` guide counts
for nothing, because the field has also been used for plain attribution; the
MCP server applies the same test in ``_quality_tier``. One reviewer asked not
to be named, so their guides carry "A licensed accountant (name withheld at
their request)": a reviewer for the guide count, not a person for the named
count.
"""

import collections
import json
import os

from .paths import REPO_ROOT

#: Values of ``reviewed_by`` / ``verified_by`` that mean "nobody".
UNREVIEWED_MARKERS = frozenset({"pending", "pending_review", "none", "no", "false", "-", "n/a", "tbd"})
#: The reviewer string of the one reviewer who asked not to be named.
WITHHELD_MARKER = "name withheld"

INDEX_PATH = os.path.join(REPO_ROOT, "index.json")
PROFILES_PATH = os.path.join(REPO_ROOT, "docs", "partners.json")
PARTNERS_PATH = os.path.join(REPO_ROOT, "PARTNERS.md")

#: The labels the headline files state, in the order the headline writes them.
HEADLINE_LABELS = ("Guides", "jurisdictions", "accountant-reviewed", "named accountants")


def reviewer_value(value):
    """A stripped reviewer string, or None for blanks, markers and other types."""
    if isinstance(value, str):
        value = value.strip()
        if value and value.lower() not in UNREVIEWED_MARKERS:
            return value
    return None


def reviewer_name(guide):
    """The reviewer name a guide carries, whatever its tier, or None."""
    for key in ("reviewed_by", "verified_by"):
        value = reviewer_value(guide.get(key))
        if value is not None:
            return value
    return None


def reviewer_of(guide):
    """The reviewer a guide is accountant-reviewed by, or None.

    Only an explicit ``tier: 1`` plus a named reviewer counts. A reviewer name
    alone never implies sign-off, or the inventory would report guides as
    accountant-reviewed that the MCP server serves as research-verified.
    """
    if str(guide.get("tier") or "").strip() != "1":
        return None
    return reviewer_name(guide)


def is_named(reviewer):
    """Whether a reviewer string names a person (the withheld one does not)."""
    return WITHHELD_MARKER not in reviewer.lower()


def headline(guides):
    """The four figures every headline states, keyed by :data:`HEADLINE_LABELS`."""
    reviewers = {reviewer_of(guide) for guide in guides}
    reviewers.discard(None)
    return {
        "Guides": len(guides),
        "jurisdictions": len({g.get("jurisdiction") for g in guides if g.get("jurisdiction")}),
        "accountant-reviewed": sum(1 for g in guides if reviewer_of(g)),
        "named accountants": sum(1 for r in reviewers if is_named(r)),
    }


def headline_line(figures):
    """The headline as README.md, llms.txt and docs/QUALITY-TIERS.md write it.

    Each figure is bolded together with its label, which is what the coverage
    gate reads: ``**1,867 Guides** across **243 jurisdictions** · **164
    accountant-reviewed** · **22 named accountants**``.
    """
    bold = {label: "**{:,} {}**".format(figures[label], label) for label in HEADLINE_LABELS}
    return "{} across {} · {} · {}".format(
        bold["Guides"], bold["jurisdictions"], bold["accountant-reviewed"], bold["named accountants"])


def edited_since_review(guide):
    """Whether a reviewed guide was substantively edited after its sign-off.

    ``review_status: pending_review`` on a tier-1 guide is that flag: the
    sync contract set a guide back to pending when an edit superseded the
    reviewed text, and the September 2026 corrections kept the convention.
    The guide stays accountant-reviewed (the sign-off happened) and the
    roster shows the count so the flag is not lost in the headline.
    """
    return str(guide.get("review_status") or "").strip().lower() == "pending_review"


def roster(guides):
    """One row per reviewer of an accountant-reviewed guide, most guides first.

    A row carries the reviewer string as the guides record it, whether it
    names a person, the guide count, how many of those guides were edited
    since the review, a Counter of jurisdiction codes, the newest
    ``last_updated`` among those guides (which dates the content, not the
    review) and the slugs.
    """
    rows = {}
    for guide in guides:
        reviewer = reviewer_of(guide)
        if reviewer is None:
            continue
        row = rows.setdefault(reviewer, {
            "reviewer": reviewer,
            "named": is_named(reviewer),
            "guides": 0,
            "edited_since_review": 0,
            "jurisdictions": collections.Counter(),
            "latest": None,
            "slugs": [],
        })
        row["guides"] += 1
        if edited_since_review(guide):
            row["edited_since_review"] += 1
        row["jurisdictions"][guide.get("jurisdiction") or "-"] += 1
        updated = str(guide.get("last_updated") or "")
        if updated and (row["latest"] is None or updated > row["latest"]):
            row["latest"] = updated
        row["slugs"].append(guide.get("slug"))
    for row in rows.values():
        row["slugs"].sort(key=str)
    return sorted(rows.values(), key=lambda r: (-r["guides"], r["reviewer"].lower()))


def by_jurisdiction(guides):
    """Accountant-reviewed guides per jurisdiction code: ``{code: Counter(reviewer)}``."""
    table = collections.defaultdict(collections.Counter)
    for guide in guides:
        reviewer = reviewer_of(guide)
        if reviewer is not None:
            table[guide.get("jurisdiction") or "-"][reviewer] += 1
    return dict(table)


def load_index(path=INDEX_PATH):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def load_profiles(path=PROFILES_PATH):
    """The hand-maintained public-record links, keyed by the exact reviewer string."""
    if not os.path.isfile(path):
        return {}
    with open(path, encoding="utf-8") as fh:
        return json.load(fh).get("reviewers", {})


GENERATED_MARKER = "<!-- Generated by scripts/build-partners.py"


def render_partners(index, profiles):
    """PARTNERS.md as a string, from the index and the profile links.

    Returns ``(text, unused_profiles)``: a profile keyed by a name that no
    accountant-reviewed guide carries is a ghost the roster would otherwise
    hide, so the caller reports it.
    """
    guides = index["guides"]
    figures = headline(guides)
    rows = roster(guides)
    jurisdictions = by_jurisdiction(guides)
    total_jurisdictions = index.get("counts", {}).get("jurisdictions", figures["jurisdictions"])
    unused = sorted(name for name in profiles if name not in {row["reviewer"] for row in rows})

    def table_name(name):
        return (name.replace("\\", "\\\\").replace("|", "\\|")
                .replace("\r\n", "\n").replace("\r", "\n").replace("\n", "<br>"))

    def record(row):
        profile = profiles.get(row["reviewer"]) or {}
        url = profile.get("public_record")
        if not url:
            return "—"
        return "[{}]({})".format(profile.get("label") or "profile", url)

    edited = sum(row["edited_since_review"] for row in rows)
    edited_note = ""
    if edited == 1:
        edited_note = " · 1 reviewed guide edited since its review"
    elif edited:
        edited_note = " · {} reviewed guides edited since their review".format(edited)
    out = [
        "# Partners: the accountants on record",
        "",
        "{} from `index.json` and `docs/partners.json`; do not edit by hand. Regenerate "
        "with `python3 scripts/build-partners.py` (`make build` runs it); "
        "`scripts/check-coverage-claims.py` fails CI while this file is stale. -->".format(GENERATED_MARKER),
        "",
        "Every row is derived from the guides' frontmatter with one rule: a guide is "
        "accountant-reviewed when it carries `tier: 1` and a reviewer's name in "
        "`reviewed_by` (or the legacy `verified_by`), and a reviewer is on this roster "
        "when at least one guide names them that way. A name on a `tier: 2` guide is "
        "attribution, not review, and does not count. The rule is `reviewer_of` in "
        "`scripts/oa_tools/roster.py`; `index.json`, the README headline and the "
        "coverage gate use the same one, so these figures agree with them by "
        "construction.",
        "",
        "**{:,} accountant-reviewed guides · {} reviewers ({} named) · {} of {} jurisdictions"
        "{}.**".format(
            figures["accountant-reviewed"], len(rows), figures["named accountants"],
            len(jurisdictions), total_jurisdictions, edited_note,
        ),
        "",
        "## Reviewers",
        "",
        "| Reviewer (as recorded in the guides) | Jurisdictions | Guides | Edited since review | Latest guide update | Public record |",
        "|---|---|---|---|---|---|",
    ]
    for row in rows:
        codes = ", ".join(
            "{} ({})".format(code, n) if len(row["jurisdictions"]) > 1 else code
            for code, n in sorted(row["jurisdictions"].items(), key=lambda kv: (-kv[1], kv[0]))
        )
        out.append("| {} | {} | {} | {} | {} | {} |".format(
            table_name(row["reviewer"]), codes, row["guides"], row["edited_since_review"] or "—",
            row["latest"] or "—", record(row)))
    out += [
        "",
        "Jurisdiction codes are the guides' `jurisdiction` values: ISO 3166 country codes, "
        "`US-XX` for a US state, `CA-XX` for a Canadian province or territory, `US` and `CA` "
        "for the federal guides. \"Edited since review\" counts the reviewer's guides whose "
        "frontmatter carries `review_status: pending_review`: a substantive edit after the "
        "sign-off sets that flag, so the reviewed text and the current text differ until the "
        "guide is reviewed again. \"Latest guide update\" is the newest `last_updated` among the "
        "reviewer's accountant-reviewed guides: it dates the content, not the review. A public "
        "record is a profile or a review diff recorded in `docs/partners.json`, which is "
        "hand-maintained; a reviewer without one is on record in the guides alone. Licence "
        "numbers are not published here: they are held by whoever verified the credential and "
        "appear only where the practitioner opts in.",
        "",
        "## Jurisdictions with an accountant-reviewed guide",
        "",
        "| Jurisdiction | Reviewed guides | Reviewers |",
        "|---|---|---|",
    ]
    for code, reviewers in sorted(jurisdictions.items(), key=lambda kv: (-sum(kv[1].values()), kv[0])):
        names = "; ".join(
            "{} ({})".format(table_name(name), n) for name, n in sorted(reviewers.items(), key=lambda kv: (-kv[1], kv[0]))
        )
        out.append("| {} | {} | {} |".format(code, sum(reviewers.values()), names))
    out += [
        "",
        "The other {} jurisdictions in `index.json` hold source-cited drafts only "
        "(`tier: 2`), whatever names their frontmatter carries.".format(
            total_jurisdictions - len(jurisdictions)),
        "",
        "## How a name gets here",
        "",
        "A guide becomes accountant-reviewed in this fork only when a named, licensed "
        "accountant reviews the complete guide and signs it off in a pull request that sets "
        "`tier: 1` and puts their name and credential in `reviewed_by` "
        "([CONTRIBUTING.md → Review](CONTRIBUTING.md#review)). Regenerate this file in the "
        "same change, and add a profile or proof link for the reviewer to `docs/partners.json` "
        "if there is one. Maintainers do not set `tier: 1` on anyone's behalf, and editing "
        "this file by hand changes nothing: the next build rewrites it from the frontmatter.",
    ]
    notes = [(row["reviewer"], (profiles.get(row["reviewer"]) or {}).get("note")) for row in rows]
    notes = [(name, note) for name, note in notes if note]
    if notes:
        out += ["", "## Notes recorded in docs/partners.json", ""]
        out += ["- **{}:** {}".format(name, note) for name, note in notes]
    return "\n".join(out) + "\n", unused
