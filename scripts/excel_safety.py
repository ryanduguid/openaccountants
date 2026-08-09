"""Small safeguards for exporting externally supplied text to Excel."""

import re

# Excel and compatible spreadsheet applications interpret values beginning with
# these characters as formulas. Prefixing text with an apostrophe preserves the
# value while forcing a text cell.
FORMULA_PREFIXES = ("=", "+", "-", "@", "\t", "\r", "\n")
FILENAME_COMPONENT_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,63}$")


def excel_safe(value):
    """Return *value* safe for assignment to an Excel cell.

    Non-string values retain their native spreadsheet types. Values already
    beginning with an apostrophe are safe and are left unchanged.
    """
    if isinstance(value, str) and value.startswith(FORMULA_PREFIXES):
        return "'" + value
    return value


def safe_filename_component(value):
    """Return a bounded ASCII filename component or reject path syntax.

    Workbook jurisdiction codes become filenames. Treating an imported JSON
    value as a path would otherwise let separators or ``..`` escape the chosen
    output directory.
    """
    if not isinstance(value, str) or not FILENAME_COMPONENT_RE.fullmatch(value):
        raise ValueError(
            "workbook filename component must start with a letter or digit and "
            "contain only letters, digits, dot, underscore, or hyphen"
        )
    return value
