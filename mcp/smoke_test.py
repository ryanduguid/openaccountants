#!/usr/bin/env python3
"""
Smoke test for the OpenAccountants MCP server and package structure.

Run from the repo root:

    python mcp/smoke_test.py

If the MCP SDK is installed, tests run through the server functions.
Otherwise, falls back to direct filesystem checks (same assertions).

Exits 0 on success, 1 on failure.
"""

import os
import sys
from pathlib import Path

failures = 0


def check(label: str, condition: bool, detail: str = "") -> None:
    global failures
    status = "PASS" if condition else "FAIL"
    msg = f"  [{status}] {label}"
    if detail and not condition:
        msg += f"  -- {detail}"
    print(msg)
    if not condition:
        failures += 1


# ---------------------------------------------------------------------------
# Try importing the MCP server; fall back to direct filesystem access
# ---------------------------------------------------------------------------

sys.path.insert(0, str(Path(__file__).resolve().parent))

try:
    from openaccountants_mcp.server import (
        PACKAGES_DIR as _pkgdir,
        _safe_resolve,
        list_jurisdictions,
        list_files,
        get_file,
    )
    PACKAGES_DIR = _pkgdir
    USE_MCP = True
except ImportError:
    REPO_ROOT = Path(__file__).resolve().parents[1]
    PACKAGES_DIR = REPO_ROOT / "packages"
    USE_MCP = False

    def _safe_resolve(packages_dir, *segments):
        joined = packages_dir.joinpath(*segments).resolve()
        try:
            joined.relative_to(packages_dir)
        except ValueError:
            raise ValueError(f"Path escapes allowed root: {joined}")
        return joined

    def list_jurisdictions():
        if not PACKAGES_DIR.is_dir():
            return []
        return sorted(
            d.name for d in PACKAGES_DIR.iterdir()
            if d.is_dir() and any(d.glob("*.md"))
        )

    def list_files(jurisdiction):
        jdir = _safe_resolve(PACKAGES_DIR, jurisdiction)
        if not jdir.is_dir():
            raise ValueError(f"Unknown jurisdiction: {jurisdiction}")
        return sorted(
            f.name for f in jdir.iterdir()
            if f.is_file() and f.suffix in {".md", ".json"}
        )

    def get_file(jurisdiction, filename):
        fpath = _safe_resolve(PACKAGES_DIR, jurisdiction, filename)
        if not fpath.is_file():
            raise ValueError(f"File not found: {jurisdiction}/{filename}")
        return fpath.read_text(encoding="utf-8")


mode = "MCP server" if USE_MCP else "filesystem fallback"
print(f"PACKAGES_DIR = {PACKAGES_DIR}")
print(f"Mode: {mode}\n")

# --- path safety ---------------------------------------------------------
print("Path safety:")
for bad in ["../../etc/passwd", "/etc/passwd", "../README.md"]:
    try:
        _safe_resolve(PACKAGES_DIR, bad)
        check(f"reject {bad!r}", False, "did NOT raise")
    except (ValueError, Exception):
        check(f"reject {bad!r}", True)

good = _safe_resolve(PACKAGES_DIR, "malta", "foundation.md")
check("accept malta/foundation.md", PACKAGES_DIR in good.parents or good == PACKAGES_DIR)

# --- list_jurisdictions ---------------------------------------------------
print("\nlist_jurisdictions:")
jurisdictions = list_jurisdictions()
check("returns a list", isinstance(jurisdictions, list))
check("contains 'malta'", "malta" in jurisdictions, f"got {jurisdictions[:5]}...")
check("contains 'uk'", "uk" in jurisdictions)
check("contains 'germany'", "germany" in jurisdictions)
check("contains 'japan'", "japan" in jurisdictions)
check(">150 jurisdictions (intl + US)", len(jurisdictions) > 150, f"got {len(jurisdictions)}")

# US state package discovery
us_states = [j for j in jurisdictions if j.startswith("us-") and j != "us"]
check("US state packages >= 51", len(us_states) >= 51, f"got {len(us_states)}")
check("contains 'us-ca'", "us-ca" in jurisdictions)
check("contains 'us-tx'", "us-tx" in jurisdictions)
check("contains 'us-ny'", "us-ny" in jurisdictions)
check("contains 'us-wa' (no income tax)", "us-wa" in jurisdictions)
check("contains 'us-fl' (no income tax)", "us-fl" in jurisdictions)
check("'us' index exists", "us" in jurisdictions)
check("'_cross-border' exists", "_cross-border" in jurisdictions)

# --- list_files (international) -------------------------------------------
print("\nlist_files('malta'):")
mt_files = list_files("malta")
check("returns a list", isinstance(mt_files, list))
check("contains foundation.md", "foundation.md" in mt_files)
check("contains intake.md", "intake.md" in mt_files)
check("contains malta-vat-return.md", "malta-vat-return.md" in mt_files)
check("contains malta-income-tax.md", "malta-income-tax.md" in mt_files)
check("contains eu-vat-directive.md (EU member)", "eu-vat-directive.md" in mt_files)
check(">=8 files", len(mt_files) >= 8, f"got {len(mt_files)}")

print("\nlist_files('germany'):")
de_files = list_files("germany")
check("contains de-payroll.md (rescued)", "de-payroll.md" in de_files)
check("contains references.md (rescued)", "references.md" in de_files)
check("contains de-income-tax.md", "de-income-tax.md" in de_files)
check("contains eu-vat-directive.md (EU member)", "eu-vat-directive.md" in de_files)

print("\nlist_files('canada'):")
ca_intl_files = list_files("canada")
check("contains bc-individual-return.md (provincial)", "bc-individual-return.md" in ca_intl_files)
check("contains qc-individual-return.md (provincial)", "qc-individual-return.md" in ca_intl_files)
check("contains on-individual-return.md (provincial)", "on-individual-return.md" in ca_intl_files)
check("contains references.md", "references.md" in ca_intl_files)
check(">=14 files (incl. provincial)", len(ca_intl_files) >= 14, f"got {len(ca_intl_files)}")

print("\nlist_files('thailand') (rescued PIT):")
th_files = list_files("thailand")
check("contains thailand-pit.md (rescued)", "thailand-pit.md" in th_files)
check("contains thailand-vat.md", "thailand-vat.md" in th_files)
check("contains references.md", "references.md" in th_files)

print("\nlist_files('_cross-border'):")
xb_files = list_files("_cross-border")
check("contains cross-border-vat-gst.md", "cross-border-vat-gst.md" in xb_files)
check("contains withholding-tax-matrix.md", "withholding-tax-matrix.md" in xb_files)
check("contains eu-reverse-charge.md", "eu-reverse-charge.md" in xb_files)
check(">=9 skills", len([f for f in xb_files if f != "README.md"]) >= 9,
      f"got {len(xb_files) - 1}")

try:
    list_files("../../../etc")
    check("reject traversal jurisdiction", False, "did NOT raise")
except (ValueError, Exception):
    check("reject traversal jurisdiction", True)

# --- list_files (US states) -----------------------------------------------
print("\nlist_files('us-ca'):")
ca_files = list_files("us-ca")
check("returns a list", isinstance(ca_files, list))
check("contains us-tax-workflow-base.md", "us-tax-workflow-base.md" in ca_files)
check("contains ca-income-tax.md", "ca-income-tax.md" in ca_files)
check("contains us-schedule-c-and-se-computation.md", "us-schedule-c-and-se-computation.md" in ca_files)
check("contains us-ca-freelance-intake.md (CA-only)", "us-ca-freelance-intake.md" in ca_files)
check("no unrelated state files in us-ca",
      not any(f.startswith("ny-") or f.startswith("tx-") for f in ca_files),
      f"found cross-state files: {[f for f in ca_files if f.startswith(('ny-','tx-'))]}")

print("\nlist_files('us-tx'):")
tx_files = list_files("us-tx")
check("contains tx-franchise-tax.md", "tx-franchise-tax.md" in tx_files)
check("contains tx-sales-tax.md", "tx-sales-tax.md" in tx_files)
check("no CA files in us-tx",
      not any(f.startswith("ca-") for f in tx_files),
      f"found cross-state: {[f for f in tx_files if f.startswith('ca-')]}")

print("\nlist_files('us-wa') (no income tax):")
wa_files = list_files("us-wa")
check("contains wa-b-and-o-tax.md", "wa-b-and-o-tax.md" in wa_files)
check("contains wa-sales-tax.md", "wa-sales-tax.md" in wa_files)
check("still has federal skills", "us-schedule-c-and-se-computation.md" in wa_files)

# --- get_file -------------------------------------------------------------
print("\nget_file('malta', 'foundation.md'):")
text = get_file("malta", "foundation.md")
check("returns a string", isinstance(text, str))
check("non-empty", len(text) > 100, f"length={len(text)}")

print("\nget_file('germany', 'references.md') (rescued file):")
de_ref = get_file("germany", "references.md")
check("returns a string", isinstance(de_ref, str))
check("non-empty", len(de_ref) > 10, f"length={len(de_ref)}")

try:
    get_file("malta", "../../README.md")
    check("reject traversal filename", False, "did NOT raise")
except (ValueError, Exception):
    check("reject traversal filename", True)

# US state file read
print("\nget_file('us-ca', 'ca-income-tax.md'):")
ca_text = get_file("us-ca", "ca-income-tax.md")
check("returns a string", isinstance(ca_text, str))
check("non-empty", len(ca_text) > 100, f"length={len(ca_text)}")

# Path safety — escape above packages/ root
print("\nPath safety (escape packages root):")
try:
    get_file("us-ca", "../../README.md")
    check("reject escape above packages/", False, "did NOT raise")
except (ValueError, Exception):
    check("reject escape above packages/", True)

# --- summary --------------------------------------------------------------
print()
if failures:
    print(f"FAILED — {failures} check(s) did not pass.")
    sys.exit(1)
else:
    print("ALL CHECKS PASSED.")
    sys.exit(0)
