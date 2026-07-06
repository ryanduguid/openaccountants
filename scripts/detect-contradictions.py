#!/usr/bin/env python3
"""
Detect cross-guide contradictions — places where two Guides state DIFFERENT
values for the SAME tax concept in the SAME jurisdiction and tax year.

v1 scope: US (skills/federal + packages/us-federal), UK (skills/international/uk),
DE (skills/international/germany). Where the same basename exists in both
skills/ and packages/, the skills/ copy is canonical and the packages/ copy is
only compared against it for "copy drift" (packages/us-federal is hand-authored
and always scanned directly).

How it works:
  1. A hand-curated concept dictionary per jurisdiction maps concept_id →
     surface terms (regexes), an optional require/exclude context regex, and
     the value kind (money / percent / any).
  2. Every guide body line (frontmatter, fenced code, headings, and changelog
     sections stripped) that mentions a concept term yields a claim: the
     normalized value(s), the tax year it binds to (year in the sentence, else
     a single year in the nearest heading, else the file's frontmatter
     tax_year), and qualifier tags (single/married/employee/monthly/...).
  3. Claims are bucketed by (concept, kind, year, qualifiers). A bucket with
     2+ distinct values (beyond a 0.5% rounding tolerance) is a candidate
     contradiction: HIGH when every conflicting value is backed by an
     explicitly year-bound claim, MEDIUM otherwise.

Precision over recall: lines carrying several distinct values for one concept
(three-year comparison tables, "was X, now Y" changelog prose) are treated as
comparison prose and never used as claim sources.

Dependency-free (stdlib only). Frontmatter parsing is reused from
scripts/build-index.py via importlib.

Usage:
    python3 scripts/detect-contradictions.py --all
    python3 scripts/detect-contradictions.py --jurisdiction DE
    python3 scripts/detect-contradictions.py --all --out /path/to/report.md
"""

import argparse
import importlib.util
import os
import re
import sys
from datetime import datetime, timezone

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Reuse the tolerant frontmatter parser from build-index.py.
_spec = importlib.util.spec_from_file_location(
    "build_index", os.path.join(os.path.dirname(os.path.abspath(__file__)), "build-index.py")
)
_build_index = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_build_index)
extract_frontmatter = _build_index.extract_frontmatter
parse_known_keys = _build_index.parse_known_keys

# ---------------------------------------------------------------------------
# Scope
# ---------------------------------------------------------------------------

# jurisdiction → (canonical tree, generated-copy tree or None)
# The generated-copy tree is deduped by basename against the canonical tree and
# used only for the copy-drift check. packages/us-federal is hand-authored, so
# for US both trees are scanned directly (no basenames overlap there anyway).
JURISDICTION_TREES = {
    "US": {"scan": ["skills/federal", "packages/us-federal"], "shadow": None},
    "UK": {"scan": ["skills/international/uk"], "shadow": "packages/uk"},
    "DE": {"scan": ["skills/international/germany"], "shadow": "packages/germany"},
}

DEFAULT_TAX_YEAR = 2025  # repo's current default year (all rates.*.json are 2025)
BINDING_YEARS = range(2023, 2028)

# A file only contributes claims when its frontmatter jurisdiction matches the
# scan (keeps e.g. packages/germany/eu-vat-directive.md — other member states'
# VAT rates — out of the DE pool).
JURISDICTION_CODES = {"US": {"US"}, "UK": {"GB", "UK"}, "DE": {"DE"}}

# Values are only read within this many characters of a concept-term match, so
# an unrelated number elsewhere on a long line can't attach to the concept.
TERM_WINDOW = 80

# ---------------------------------------------------------------------------
# Concept dictionaries (hand-curated; seeded from packages/*/rates.2025.json)
# ---------------------------------------------------------------------------
# concept: {"terms": [regex,...] (ANY must match the line),
#           "require": regex that ALSO must match (optional),
#           "exclude": regex that must NOT match (optional),
#           "kind": "money" | "percent" | "any"}

CONCEPTS = {
    "DE": {
        "grundfreibetrag": {"terms": [r"Grundfreibetrag", r"basic allowance"], "kind": "money",
                            "min": 10000, "max": 15000},
        "solz_rate": {"terms": [r"Solidarit(?:ä|ae?)tszuschlag", r"\bSolZ\b"], "kind": "percent",
                      "exclude": r"Milderungszone|Gleitzone|phase-?in|marginal|Kirchensteuer",
                      "min": 4, "max": 7},
        "solz_freigrenze": {"terms": [r"Freigrenze", r"SOLZFREI", r"[Ee]xemption threshold"],
                            "require": r"SolZ|SOLZ|Solidarit", "kind": "money",
                            "min": 1000, "max": 50000},
        "kirchensteuer_rate": {"terms": [r"Kirchensteuer", r"church tax"], "kind": "percent",
                               "exclude": r"Bayern|Baden|Bavaria|Württemberg", "min": 7, "max": 10},
        "vat_standard_rate": {"terms": [r"Umsatzsteuer", r"Mehrwertsteuer", r"\bUSt\b", r"\bVAT\b"],
                              "kind": "percent",
                              "exclude": r"reduced|ermäßigt|zero|photovolta|Kleinunternehmer",
                              "min": 16, "max": 25},
        "vat_reduced_rate": {"terms": [r"Umsatzsteuer", r"Mehrwertsteuer", r"\bUSt\b", r"\bVAT\b"],
                             "require": r"reduced|ermäßigt", "kind": "percent", "min": 5, "max": 10},
        "kleinunternehmer_threshold": {"terms": [r"Kleinunternehmer", r"small.business regime", r"§ ?19 UStG"],
                                       "kind": "money", "min": 15000, "max": 120000,
                                       "exclude": r"EU-wide|cross-border"},
        "gwg_limit": {"terms": [r"\bGWG\b", r"geringwertige"], "kind": "money",
                      "exclude": r"Sammelposten|pool", "min": 250, "max": 1500},
        "sammelposten_limit": {"terms": [r"Sammelposten"], "kind": "money", "min": 250, "max": 6000},
        "trade_tax_freibetrag": {"terms": [r"Freibetrag"], "require": r"Gewerbe", "kind": "money",
                                 "min": 10000, "max": 50000},
        "steuermesszahl": {"terms": [r"Steuermesszahl", r"trade tax base rate"], "kind": "percent",
                           "min": 3, "max": 4},
        "minijob_ceiling": {"terms": [r"Minijob", r"geringfügig"], "kind": "money",
                            "exclude": r"Pauschal|flat", "min": 400, "max": 8500},
        "bbg_rv": {"terms": [r"Beitragsbemessungsgrenze", r"\bBBG\b", r"contribution ceiling"],
                   "require": r"Renten|\bRV\b|pension", "kind": "money", "min": 3000, "max": 130000},
        "bbg_kv": {"terms": [r"Beitragsbemessungsgrenze", r"\bBBG\b", r"contribution ceiling"],
                   "require": r"Kranken|\bKV\b|health", "kind": "money", "min": 3000, "max": 130000},
        "rv_rate": {"terms": [r"Rentenversicherung", r"pension insurance"], "kind": "percent",
                    "min": 8, "max": 20},
        "kv_rate": {"terms": [r"Krankenversicherung", r"health insurance"], "kind": "percent",
                    "exclude": r"Zusatzbeitrag|additional contribution|ermäßigt", "min": 6, "max": 18},
        "pv_rate": {"terms": [r"Pflegeversicherung", r"care insurance"], "kind": "percent",
                    "exclude": r"kinderlos|childless|Zuschlag|Abschlag|Sachsen|Saxony|child|KSK|Künstler",
                    "min": 1, "max": 5},
        "av_rate": {"terms": [r"Arbeitslosenversicherung", r"unemployment insurance"], "kind": "percent",
                    "min": 1, "max": 4},
        "arbeitnehmer_pauschbetrag": {"terms": [r"Arbeitnehmer-?Pauschbetrag", r"Werbungskostenpauschale",
                                                r"employee lump.?sum"], "kind": "money",
                                      "min": 1000, "max": 1500},
        "sparer_pauschbetrag": {"terms": [r"Sparer-?Pauschbetrag", r"saver'?s allowance"], "kind": "money",
                                "min": 700, "max": 1300},
        "kindergeld_monthly": {"terms": [r"Kindergeld"], "kind": "money", "min": 150, "max": 350},
        "home_office_pauschale": {"terms": [r"Tagespauschale", r"Homeoffice-?Pauschale", r"home office"],
                                  "kind": "money", "min": 4, "max": 1500},
        "abgeltungsteuer_rate": {"terms": [r"Abgeltung(?:s)?steuer", r"Kapitalertrags?steuer"], "kind": "percent",
                                 "exclude": r"effective|einschl|including|26\.375", "min": 20, "max": 30},
        "geschenke_limit": {"terms": [r"Geschenke", r"business gifts?"], "kind": "money",
                            "min": 20, "max": 100},
        "crypto_freigrenze": {"terms": [r"Spekulation", r"private Ver(?:ä|ae)u(?:ß|ss)erung",
                                        r"§ ?23 EStG", r"private sales?"], "kind": "money",
                              "exclude": r"holding|Haltefrist", "min": 400, "max": 1500},
        "saeumniszuschlag": {"terms": [r"S(?:ä|ae)umniszuschlag", r"late.payment (?:surcharge|penalty)"],
                             "kind": "percent", "min": 0.5, "max": 2},
        "verspaetungszuschlag_min": {"terms": [r"Versp(?:ä|ae)tungszuschlag", r"late.filing surcharge"],
                                     "kind": "money", "min": 10, "max": 100},
    },
    "UK": {
        "personal_allowance": {"terms": [r"[Pp]ersonal [Aa]llowance"], "kind": "money",
                               "exclude": r"taper|withdraw|reduce|abate|blind"},
        "basic_rate": {"terms": [r"basic rate"], "kind": "percent",
                       "exclude": r"dividend|savings|CGT|capital gains|Scot|residential|starter"},
        "higher_rate": {"terms": [r"higher rate"], "kind": "percent",
                        "exclude": r"dividend|savings|CGT|capital gains|Scot|residential"},
        "additional_rate": {"terms": [r"additional rate"], "kind": "percent",
                            "exclude": r"dividend|savings|CGT|capital gains|Scot"},
        "higher_rate_threshold": {"terms": [r"higher.rate threshold"], "kind": "money", "exclude": r"Scot"},
        "vat_standard_rate": {"terms": [r"\bVAT\b", r"value added tax"], "kind": "percent",
                              "exclude": r"reduced|zero|flat.rate|exempt|fuel"},
        "vat_registration_threshold": {"terms": [r"registration threshold", r"VAT registration",
                                                 r"must register for VAT"], "kind": "money",
                                       "exclude": r"deregist"},
        "vat_deregistration_threshold": {"terms": [r"deregistration"], "kind": "money"},
        "cgt_aea": {"terms": [r"annual exempt amount", r"\bAEA\b"], "kind": "money", "exclude": r"trust"},
        "cgt_rates": {"terms": [r"capital gains", r"\bCGT\b"], "kind": "percent",
                      "exclude": r"BADR|Business Asset|carried|Investors|Scot"},
        "badr_rate": {"terms": [r"BADR", r"Business Asset Disposal"], "kind": "percent"},
        "badr_lifetime_limit": {"terms": [r"BADR", r"Business Asset Disposal"], "require": r"lifetime",
                                "kind": "money"},
        "dividend_allowance": {"terms": [r"dividend allowance"], "kind": "money"},
        "dividend_rates": {"terms": [r"dividend"], "kind": "percent", "exclude": r"allowance|corporation"},
        "personal_savings_allowance": {"terms": [r"personal savings allowance", r"\bPSA\b"], "kind": "money"},
        "nic_class2_weekly": {"terms": [r"Class 2"], "kind": "money"},
        "class4_lower_profits_limit": {"terms": [r"lower profits limit", r"\bLPL\b"], "kind": "money"},
        "class1_primary_threshold": {"terms": [r"primary threshold"], "kind": "money"},
        "class1_secondary_threshold": {"terms": [r"secondary threshold"], "kind": "money"},
        "employer_nic_rate": {"terms": [r"employer(?:'s)? (?:NIC|National Insurance)", r"secondary Class 1"],
                              "kind": "percent"},
        "employment_allowance": {"terms": [r"Employment Allowance"], "kind": "money"},
        "upper_earnings_limit": {"terms": [r"upper earnings limit", r"\bUEL\b"], "kind": "money"},
        "lower_earnings_limit": {"terms": [r"lower earnings limit", r"\bLEL\b"], "kind": "money"},
        "trading_allowance": {"terms": [r"trading allowance"], "kind": "money"},
        "property_allowance": {"terms": [r"property allowance"], "kind": "money"},
        "annual_investment_allowance": {"terms": [r"annual investment allowance", r"\bAIA\b"], "kind": "money"},
        "mileage_rate_car": {"terms": [r"mileage"], "kind": "money",
                             "exclude": r"over 10,000|above 10,000|motorc|bicycle|passenger"},
        "marriage_allowance": {"terms": [r"marriage allowance"], "kind": "money",
                               "exclude": r"reducer|worth|saving"},
        "pension_annual_allowance": {"terms": [r"annual allowance"], "require": r"pension", "kind": "money",
                                     "exclude": r"taper|MPAA|money purchase|lifetime"},
        "hicbc_threshold": {"terms": [r"HICBC", r"High Income Child Benefit"], "kind": "money",
                            "exclude": r"full|entire|complete"},
        "student_loan_plan1": {"terms": [r"Plan 1\b"], "kind": "money"},
        "student_loan_plan2": {"terms": [r"Plan 2\b"], "kind": "money"},
        "student_loan_plan4": {"terms": [r"Plan 4\b"], "kind": "money"},
        "student_loan_plan5": {"terms": [r"Plan 5\b"], "kind": "money"},
        "postgraduate_loan_threshold": {"terms": [r"[Pp]ostgraduate [Ll]oan"], "kind": "money"},
        "student_loan_rate": {"terms": [r"student loan"], "kind": "percent", "exclude": r"[Pp]ostgraduate"},
        "corporation_tax_rate": {"terms": [r"[Cc]orporation [Tt]ax"], "kind": "percent",
                                 "exclude": r"small profits|marginal"},
        "payments_on_account_threshold": {"terms": [r"payments on account", r"\bPOA\b"], "kind": "money",
                                          "exclude": r"80%|at source"},
        "sa_late_filing_penalty": {"terms": [r"late filing penalty"], "kind": "money",
                                   "exclude": r"daily|3 months|6 months|12 months|tax.geared"},
    },
    "US": {
        "standard_deduction": {"terms": [r"standard deduction"], "kind": "money",
                               "exclude": r"senior|bonus|age 65|additional|blind"},
        "qbi_rate": {"terms": [r"199A", r"\bQBI\b", r"qualified business income"], "kind": "percent"},
        "qbi_threshold": {"terms": [r"199A", r"\bQBI\b", r"qualified business income"], "kind": "money",
                          "exclude": r"phase-?in|phase-?out|range|W-2 wages|UBIA"},
        "salt_cap": {"terms": [r"\bSALT\b", r"state and local tax"], "kind": "money",
                     "exclude": r"phase|MAGI|income (?:above|over)|reverts|2030"},
        "section_179_limit": {"terms": [r"[Ss]ection 179", r"§ ?179"], "kind": "money",
                              "exclude": r"phase.?out|phase.?down|SUV|vehicle"},
        "bonus_depreciation_rate": {"terms": [r"bonus depreciation", r"168\(k\)"], "kind": "percent"},
        "ss_wage_base": {"terms": [r"wage base"], "require": r"[Ss]ocial [Ss]ecurity|OASDI|SSA|12\.4",
                         "kind": "money"},
        "se_tax_rate": {"terms": [r"self.?employment tax", r"\bSE tax\b"], "kind": "percent",
                        "exclude": r"92\.35"},
        "medicare_rate": {"terms": [r"Medicare"], "kind": "percent", "exclude": r"[Aa]dditional"},
        "additional_medicare": {"terms": [r"[Aa]dditional Medicare"], "kind": "any"},
        "futa": {"terms": [r"FUTA"], "kind": "any", "exclude": r"credit|net|reduction"},
        "limit_401k_deferral": {"terms": [r"401\(k\)", r"401k"], "kind": "money",
                                "exclude": r"catch.?up|super|415|compensation|top.heavy|HCE"},
        "ira_contribution_limit": {"terms": [r"\bIRA\b"], "kind": "money",
                                   "exclude": r"catch|SEP|SIMPLE|phase|rollover"},
        "hsa_limit": {"terms": [r"\bHSA\b"], "kind": "money",
                      "exclude": r"catch|HDHP|out-of-pocket|deductible"},
        "feie_cap": {"terms": [r"FEIE", r"foreign earned income exclusion", r"§ ?911", r"[Ss]ection 911"],
                     "kind": "money", "exclude": r"housing"},
        "gift_annual_exclusion": {"terms": [r"annual (?:gift )?exclusion", r"gift tax exclusion"],
                                  "require": r"gift", "kind": "money", "exclude": r"spouse|non.?citizen"},
        "estate_exclusion": {"terms": [r"basic exclusion", r"estate tax exemption", r"lifetime exemption"],
                             "kind": "money"},
        "form_1099k_threshold": {"terms": [r"1099-K"], "kind": "money", "exclude": r"transactions"},
        "form_1099nec_threshold": {"terms": [r"1099-NEC"], "kind": "money"},
        "fbar_threshold": {"terms": [r"FBAR"], "kind": "money", "exclude": r"penalt"},
        "ctc_per_child": {"terms": [r"child tax credit", r"\bCTC\b"], "kind": "money",
                          "exclude": r"phase|refundable|other dependent"},
        "aotc_max": {"terms": [r"AOTC", r"American Opportunity"], "kind": "money",
                     "exclude": r"phase|refundable"},
        "niit": {"terms": [r"NIIT", r"net investment income tax"], "kind": "any"},
        "c_corp_rate": {"terms": [r"corporate (?:income )?tax rate", r"corporate rate", r"C.corp(?:oration)? rate"],
                        "kind": "percent", "exclude": r"CAMT|minimum|BEAT|state|accumulated|holding"},
        "estimated_safe_harbor": {"terms": [r"safe harbor"], "require": r"estimated|prior.year|preceding year",
                                  "kind": "percent", "exclude": r"150,000|150k"},
        "kiddie_tax_threshold": {"terms": [r"kiddie tax"], "kind": "money"},
        "amt_exemption": {"terms": [r"AMT exemption"], "kind": "money",
                          "exclude": r"phase|trust|estate"},
        "qsbs_exclusion_cap": {"terms": [r"QSBS", r"§ ?1202", r"[Ss]ection 1202"], "kind": "money",
                               "exclude": r"gross assets"},
        "penalty_6698": {"terms": [r"6698"], "kind": "money"},
        "mileage_business": {"terms": [r"mileage"], "kind": "money",
                             "exclude": r"medical|moving|charit"},
        "social_security_rate": {"terms": [r"[Ss]ocial [Ss]ecurity", r"OASDI"], "kind": "percent",
                                 "exclude": r"Medicare|combined|15\.3"},
    },
}

# ---------------------------------------------------------------------------
# Extraction machinery
# ---------------------------------------------------------------------------

CURRENCY_NUM_RE = re.compile(
    r"(?:EUR|GBP|USD|€|£|\$)\s?(\d{1,3}(?:[.,]\d{3})+(?:[.,]\d{1,2})?|\d+(?:[.,]\d{1,2})?)"
)
BARE_NUM_RE = re.compile(
    r"\b\d{1,3}(?:,\d{3})+(?:\.\d{1,2})?\b|\b\d{1,3}(?:\.\d{3})+(?:,\d{1,2})?\b"
)
PENCE_RE = re.compile(r"\b(\d{1,3}(?:\.\d{1,2})?)p\b")
CENTS_RE = re.compile(r"\b(\d{1,3}(?:\.\d{1,2})?) cents?\b")
PERCENT_RE = re.compile(r"(\d{1,3}(?:[.,]\d{1,3})?)\s?%")
MILLION_RE = re.compile(r"^\s?(?:million|m\b|mio)", re.IGNORECASE)

# 2023-2027, tolerating "2025-26" / "2025/26" tax-year labels (start year binds).
YEAR_RE = re.compile(r"\b(20[12]\d)(?:[-/](?:\d{2}|20\d{2}))?\b")

HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s")
# Worked-example / test-vector prose: numbers there are scenario arithmetic,
# not normative claims.
EXAMPLE_LINE_RE = re.compile(
    r"^[>\s*-]*(?:\*\*)?(?:Input|Output|Expected|Computation|Result|Scenario|Example \d|Step \d|Test \d)\b",
    re.IGNORECASE,
)
CHANGELOG_HEADING_RE = re.compile(r"changelog|version history|revision history|what changed", re.IGNORECASE)
HISTORICAL_RE = re.compile(
    r"previously|formerly|superseded|no longer|repealed|pre-OBBBA|before 6 April|until 5 April|old (?:value|threshold|limit)",
    re.IGNORECASE,
)

# NOTE: "annual" and "standard" are deliberately NOT tags — they are the
# unmarked default, and tagging them would split buckets that should compare
# (e.g. "Jahreslohnsteuer up to EUR 19,950" vs "ESt up to EUR 18,130").
QUALIFIER_PATTERNS = {
    "single": r"\bsingle\b|Grundtarif|Grundtabelle|self.?only|Stkl\.? ?I\b(?! ?I)|Steuerklasse I\b(?! ?I)",
    "married": r"\bmarried\b|\bMFJ\b|\bjointly?\b|Splitting|zusammen|\bfamily\b|Stkl\.? ?III\b|Steuerklasse III\b",
    "mfs": r"\bMFS\b|married filing separately",
    "hoh": r"\bHoH\b|head of household",
    "employee": r"\bemployee\b|Arbeitnehmer",
    "employer": r"\bemployer\b|Arbeitgeber",
    "monthly": r"\bmonthly\b|per month|a month|/month|monatlich|pro Monat|je Monat",
    "weekly": r"\bweekly\b|per week|a week|/week|wöchentlich",
    "daily": r"\bdaily\b|per day|a day|/day|pro Tag|Tagespauschale",
    "reduced": r"\breduced\b|ermäßigt",
    "basic": r"\bbasic.rate\b",
    "higher": r"\bhigher.rate\b",
    "additional": r"\badditional.rate\b",
    "prior_year": r"previous[- ](?:calendar |tax )?year|prior[- ]year|preceding[- ]year|Vorjahr",
    "current_year": r"current[- ](?:calendar |tax )?year|laufend",
}
QUALIFIERS = {tag: re.compile(pat, re.IGNORECASE if tag not in ("mfs",) else 0)
              for tag, pat in QUALIFIER_PATTERNS.items()}


def compile_concepts():
    compiled = {}
    for jur, concepts in CONCEPTS.items():
        compiled[jur] = {}
        for cid, spec in concepts.items():
            compiled[jur][cid] = {
                "terms": [re.compile(t) for t in spec["terms"]],
                "require": re.compile(spec["require"]) if spec.get("require") else None,
                "exclude": re.compile(spec["exclude"]) if spec.get("exclude") else None,
                "kind": spec["kind"],
                "min": spec.get("min", 0.0),
                "max": spec.get("max", float("inf")),
            }
    return compiled


def parse_amount(raw):
    """Normalize '12,096', '12.096' (German), '3.5', '3,5', '1,250,000' → float."""
    s = raw
    if "," in s and "." in s:
        if s.rfind(",") > s.rfind("."):  # German decimal comma: 1.234,56
            s = s.replace(".", "").replace(",", ".")
        else:  # English: 1,234.56
            s = s.replace(",", "")
    elif "," in s:
        parts = s.split(",")
        if all(len(p) == 3 for p in parts[1:]):
            s = s.replace(",", "")  # thousands
        else:
            s = s.replace(",", ".")  # German decimal comma
    elif "." in s:
        head, _, tail = s.rpartition(".")
        if head and len(tail) == 3:
            s = s.replace(".", "")  # German thousands: 12.096
    try:
        return float(s)
    except ValueError:
        return None


def extract_percent_values(line):
    values, spans = [], []
    for m in PERCENT_RE.finditer(line):
        v = parse_amount(m.group(1))
        if v is not None and 0 <= v <= 200:
            values.append(v)
            spans.append(m.span())
    return values, spans


def extract_money_values(line, percent_spans):
    def overlaps(span):
        return any(not (span[1] <= s or span[0] >= e) for s, e in percent_spans)

    values = []
    seen_spans = []
    for m in CURRENCY_NUM_RE.finditer(line):
        if overlaps(m.span()):
            continue
        v = parse_amount(m.group(1))
        if v is None:
            continue
        if MILLION_RE.match(line[m.end():m.end() + 9]):
            v *= 1_000_000
        values.append(v)
        seen_spans.append(m.span())
    for m in BARE_NUM_RE.finditer(line):
        span = m.span()
        if overlaps(span):
            continue
        if any(not (span[1] <= s or span[0] >= e) for s, e in seen_spans):
            continue
        v = parse_amount(m.group(0))
        if v is None:
            continue
        if MILLION_RE.match(line[m.end():m.end() + 9]):
            v *= 1_000_000
        values.append(v)
    for m in PENCE_RE.finditer(line):
        values.append(round(parse_amount(m.group(1)) / 100, 4))
    for m in CENTS_RE.finditer(line):
        values.append(round(parse_amount(m.group(1)) / 100, 4))
    return values


def sentence_years(line):
    """Distinct 4-digit binding years mentioned (start year of 2025-26 labels)."""
    years = set()
    for m in YEAR_RE.finditer(line):
        y = int(m.group(1))
        if y in BINDING_YEARS:
            years.add(y)
    return years


def qualifiers_for(line):
    return frozenset(tag for tag, rx in QUALIFIERS.items() if rx.search(line))


def close_enough(a, b):
    """True when two values differ only by a bracket-boundary off-by-one
    (12,570 vs 12,571) or sub-0.05% rounding. Deliberately tight: 12,084 vs
    12,096 (0.1% apart) is a REAL contradiction and must stay distinct."""
    if a == b:
        return True
    if abs(a - b) <= 1.0:
        return True
    denom = max(abs(a), abs(b))
    return denom > 0 and abs(a - b) / denom < 0.0005


def cluster_values(values):
    """Merge values within rounding tolerance; return sorted representatives."""
    reps = []
    for v in sorted(values):
        if not reps or not close_enough(reps[-1], v):
            reps.append(v)
    return reps


def strip_frontmatter_body(text):
    block = extract_frontmatter(text)
    if block is None:
        return None, None
    # Body starts after the closing --- of the frontmatter.
    end = re.search(r"^(---|\.\.\.)\s*$", text[text.find("\n") + 1:], re.MULTILINE)
    body_start = text.find("\n") + 1 + end.end()
    offset = text[:body_start].count("\n")
    return block, (text[body_start:], offset)


def extract_claims(rel_path, text, jurisdiction, compiled, stats):
    """Yield claim dicts from one guide file."""
    block, body_info = strip_frontmatter_body(text)
    if body_info is None:
        return []
    fields = parse_known_keys(block)
    if (fields.get("category") or "").strip().lower() == "foundation":
        return []
    # Only files declaring the scanned jurisdiction contribute claims (skips
    # shared workflow bases, runbooks, and the EU-wide VAT directive guide).
    file_jur = (fields.get("jurisdiction") or "").strip().upper()
    if file_jur not in JURISDICTION_CODES[jurisdiction]:
        return []
    fm_year = None
    if fields.get("tax_year"):
        m = re.match(r"(\d{4})", str(fields["tax_year"]))
        if m:
            fm_year = int(m.group(1))
    fm_year = fm_year or DEFAULT_TAX_YEAR

    body, line_offset = body_info
    claims = []
    in_fence = False
    heading_year = None
    in_changelog = False
    concepts = compiled[jurisdiction]

    for i, line in enumerate(body.splitlines()):
        lineno = line_offset + i + 1
        stripped = line.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if HEADING_RE.match(line):
            in_changelog = bool(CHANGELOG_HEADING_RE.search(line))
            hy = sentence_years(line)
            heading_year = next(iter(hy)) if len(hy) == 1 else None
            continue  # headings are context, never claim sources
        if in_changelog or not stripped:
            continue
        if EXAMPLE_LINE_RE.match(stripped):
            continue

        for cid, spec in concepts.items():
            if not any(rx.search(line) for rx in spec["terms"]):
                continue
            if spec["require"] and not spec["require"].search(line):
                continue
            if spec["exclude"] and spec["exclude"].search(line):
                continue

            pct_values, pct_spans = extract_percent_values(line)
            kinds = []
            if spec["kind"] in ("money", "any"):
                kinds.append(("money", extract_money_values(line, pct_spans)))
            if spec["kind"] in ("percent", "any"):
                kinds.append(("percent", pct_values))

            years = sentence_years(line)
            for kind, values in kinds:
                # 0 is never a normative value for these concepts — it's
                # always example output ("SolZ = 0%"). Plausibility bounds
                # (generous, per concept) drop scenario arithmetic that
                # happens to share a line with the term.
                vmin = spec.get("min", 0.0)
                vmax = spec.get("max", float("inf"))
                reps = cluster_values([v for v in values
                                       if v is not None and v > 0 and vmin <= v <= vmax])
                if not reps:
                    continue
                if len(reps) > 1:
                    # Comparison prose / multi-year table row / "was X now Y":
                    # ambiguous, never a claim source (precision over recall).
                    stats["multivalue_lines_skipped"] += 1
                    continue
                value = reps[0]
                if len(years) == 1:
                    year, explicit = next(iter(years)), True
                elif len(years) > 1:
                    if fm_year in years:
                        year, explicit = fm_year, True
                    else:
                        stats["ambiguous_year_dropped"] += 1
                        continue
                elif heading_year is not None:
                    year, explicit = heading_year, True
                else:
                    year, explicit = fm_year, False
                if not explicit and HISTORICAL_RE.search(line):
                    stats["historical_dropped"] += 1
                    continue
                claims.append({
                    "jurisdiction": jurisdiction,
                    "concept": cid,
                    "kind": kind,
                    "value": value,
                    "year": year,
                    "year_explicit": explicit,
                    "qualifiers": qualifiers_for(line),
                    "path": rel_path,
                    "line": lineno,
                    "sentence": stripped[:200],
                })
    stats["claims"] += len(claims)
    return claims


# ---------------------------------------------------------------------------
# Comparison
# ---------------------------------------------------------------------------

def bucket_claims(claims):
    buckets = {}
    for c in claims:
        key = (c["concept"], c["kind"], c["year"], c["qualifiers"])
        buckets.setdefault(key, []).append(c)
    return buckets


def find_candidates(buckets, stats):
    """Return list of (key, clusters) where clusters maps rep value → claims."""
    candidates = []
    for key, claims in sorted(buckets.items(), key=lambda kv: (kv[0][0], kv[0][1], kv[0][2])):
        reps = cluster_values([c["value"] for c in claims])
        if len(reps) < 2:
            continue
        stats["candidates_before_filters"] += 1
        clusters = {}
        for c in claims:
            rep = next(r for r in reps if close_enough(r, c["value"]))
            clusters.setdefault(rep, []).append(c)
        # Rounding merge may leave a "cluster" whose members all came from one
        # value; require every cluster to keep at least one claim.
        if len(clusters) < 2:
            continue
        candidates.append((key, clusters))
        stats["candidates_after_filters"] += 1
    return candidates


def rank_candidate(clusters):
    """HIGH when every conflicting value has an explicitly year-bound claim."""
    if all(any(c["year_explicit"] for c in cs) for cs in clusters.values()):
        return "HIGH"
    return "MEDIUM"


# ---------------------------------------------------------------------------
# File discovery + copy drift
# ---------------------------------------------------------------------------

def md_files(tree):
    base = os.path.join(REPO_ROOT, tree)
    if not os.path.isdir(base):
        return []
    out = []
    for name in sorted(os.listdir(base)):
        if name.endswith(".md") and not name.lower().startswith("readme"):
            out.append(os.path.join(tree, name).replace(os.sep, "/"))
    return out


def read(rel_path):
    with open(os.path.join(REPO_ROOT, rel_path), encoding="utf-8", errors="replace") as fh:
        return fh.read()


def scan_jurisdiction(jurisdiction, compiled):
    trees = JURISDICTION_TREES[jurisdiction]
    stats = {
        "files_scanned": 0, "claims": 0, "multivalue_lines_skipped": 0,
        "ambiguous_year_dropped": 0, "historical_dropped": 0,
        "buckets": 0, "candidates_before_filters": 0, "candidates_after_filters": 0,
    }
    claims = []
    scanned_basenames = set()
    for tree in trees["scan"]:
        for rel in md_files(tree):
            file_claims = extract_claims(rel, read(rel), jurisdiction, compiled, stats)
            if file_claims is not None:
                stats["files_scanned"] += 1
                claims.extend(file_claims or [])
                scanned_basenames.add(os.path.basename(rel))

    # Copy drift: shadow (generated packages/) copy vs the canonical skills/ copy.
    drift = []
    if trees["shadow"]:
        for rel in md_files(trees["shadow"]):
            base = os.path.basename(rel)
            canonical = None
            for tree in trees["scan"]:
                cand = f"{tree}/{base}"
                if os.path.exists(os.path.join(REPO_ROOT, cand)):
                    canonical = cand
                    break
            if canonical is None:
                # Package-only file: scan it directly (nothing to drift against).
                file_claims = extract_claims(rel, read(rel), jurisdiction, compiled, stats)
                if file_claims:
                    stats["files_scanned"] += 1
                    claims.extend(file_claims)
                continue
            shadow_stats = dict.fromkeys(stats, 0)  # throwaway counters
            shadow_claims = extract_claims(rel, read(rel), jurisdiction, compiled, shadow_stats)
            canon_claims = [c for c in claims if c["path"] == canonical]
            drift.extend(compare_copies(canonical, canon_claims, rel, shadow_claims))

    buckets = bucket_claims(claims)
    stats["buckets"] = len(buckets)
    candidates = find_candidates(buckets, stats)
    return claims, candidates, drift, stats


def compare_copies(canon_path, canon_claims, shadow_path, shadow_claims):
    """Same bucket key present in both copies but with different values = drift."""
    def by_key(claims):
        keyed = {}
        for c in claims:
            key = (c["concept"], c["kind"], c["year"], c["qualifiers"])
            keyed.setdefault(key, []).append(c)
        return keyed

    canon, shadow = by_key(canon_claims), by_key(shadow_claims)
    findings = []
    for key in sorted(set(canon) & set(shadow), key=str):
        cv = cluster_values([c["value"] for c in canon[key]])
        sv = cluster_values([c["value"] for c in shadow[key]])
        only_canon = [v for v in cv if not any(close_enough(v, w) for w in sv)]
        only_shadow = [v for v in sv if not any(close_enough(v, w) for w in cv)]
        if only_canon or only_shadow:
            findings.append({
                "key": key, "canon_path": canon_path, "shadow_path": shadow_path,
                "canon_values": cv, "shadow_values": sv,
                "canon_claims": canon[key], "shadow_claims": shadow[key],
            })
    return findings


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------

def fmt_value(value, kind):
    if kind == "percent":
        return f"{value:g}%"
    if value == int(value):
        return f"{int(value):,}"
    return f"{value:,.4g}"


def fmt_key(key):
    concept, kind, year, quals = key
    q = ", ".join(sorted(quals)) if quals else "none"
    return f"`{concept}` ({kind}, year {year}, qualifiers: {q})"


def render_candidate(lines, key, clusters):
    lines.append(f"### {fmt_key(key)}")
    lines.append("")
    kind = key[1]
    for rep in sorted(clusters):
        claims = clusters[rep]
        lines.append(f"- **{fmt_value(rep, kind)}**")
        seen = set()
        for c in sorted(claims, key=lambda c: (c["path"], c["line"])):
            sig = (c["path"], c["line"])
            if sig in seen:
                continue
            seen.add(sig)
            marker = "" if c["year_explicit"] else " _(year from frontmatter)_"
            lines.append(f"  - `{c['path']}:{c['line']}`{marker}")
            lines.append(f"    > {c['sentence']}")
    lines.append("")


def render_report(results):
    lines = [
        "# Cross-guide contradiction report",
        "",
        f"Generated {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')} by `scripts/detect-contradictions.py` (v1).",
        "",
        "Different values for the same tax concept, jurisdiction, year, and qualifier",
        "set. HIGH = every conflicting value is explicitly year-bound (sentence or",
        "section heading); MEDIUM = at least one side's year comes only from the",
        "file's frontmatter. Precision over recall: multi-value comparison lines are",
        "never used as claim sources.",
        "",
    ]
    for jur, (claims, candidates, drift, stats) in results.items():
        highs = [(k, c) for k, c in candidates if rank_candidate(c) == "HIGH"]
        meds = [(k, c) for k, c in candidates if rank_candidate(c) == "MEDIUM"]
        lines.append(f"## {jur}")
        lines.append("")
        lines.append(f"## {jur} — HIGH confidence ({len(highs)})")
        lines.append("")
        if not highs:
            lines.append("None.")
            lines.append("")
        for key, clusters in highs:
            render_candidate(lines, key, clusters)
        lines.append(f"## {jur} — MEDIUM confidence ({len(meds)})")
        lines.append("")
        if not meds:
            lines.append("None.")
            lines.append("")
        for key, clusters in meds:
            render_candidate(lines, key, clusters)
        lines.append(f"## {jur} — Copy drift (skills/ vs packages/) ({len(drift)})")
        lines.append("")
        if not drift:
            lines.append("None detected on tracked concepts.")
            lines.append("")
        for d in drift:
            lines.append(f"### {fmt_key(d['key'])}")
            kind = d["key"][1]
            cvals = ", ".join(fmt_value(v, kind) for v in d["canon_values"])
            svals = ", ".join(fmt_value(v, kind) for v in d["shadow_values"])
            lines.append(f"- canonical `{d['canon_path']}`: {cvals}")
            lines.append(f"- generated `{d['shadow_path']}`: {svals}")
            for c in d["shadow_claims"][:2]:
                lines.append(f"  - `{d['shadow_path']}:{c['line']}`")
                lines.append(f"    > {c['sentence']}")
            lines.append("")
        lines.append(f"## {jur} — Stats")
        lines.append("")
        for k, v in stats.items():
            lines.append(f"- {k.replace('_', ' ')}: {v}")
        lines.append("")
    return "\n".join(lines) + "\n"


def main(argv=None):
    parser = argparse.ArgumentParser(description="Detect cross-guide value contradictions.")
    parser.add_argument("--jurisdiction", choices=sorted(JURISDICTION_TREES), action="append",
                        help="Jurisdiction to scan (repeatable).")
    parser.add_argument("--all", action="store_true", help="Scan all supported jurisdictions.")
    parser.add_argument("--out", help="Write the markdown report here (default: stdout).")
    args = parser.parse_args(argv)

    if args.all or not args.jurisdiction:
        jurisdictions = sorted(JURISDICTION_TREES)
    else:
        jurisdictions = args.jurisdiction

    compiled = compile_concepts()
    results = {}
    for jur in jurisdictions:
        results[jur] = scan_jurisdiction(jur, compiled)

    report = render_report(results)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(report)
        total_high = total_med = 0
        for jur, (_, candidates, drift, stats) in results.items():
            highs = sum(1 for _, c in candidates if rank_candidate(c) == "HIGH")
            meds = len(candidates) - highs
            total_high += highs
            total_med += meds
            print(f"{jur}: {highs} HIGH, {meds} MEDIUM, {len(drift)} copy-drift "
                  f"({stats['files_scanned']} files, {stats['claims']} claims)")
        print(f"TOTAL: {total_high} HIGH, {total_med} MEDIUM → {args.out}")
    else:
        sys.stdout.write(report)
    return 0


if __name__ == "__main__":
    sys.exit(main())
