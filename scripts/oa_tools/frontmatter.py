"""The one frontmatter reader: tolerant and strict behind a single API.

A guide opens with a ``---`` line at byte 0 and its frontmatter runs to the
next line that is ``---`` or ``...``. Two readers share that rule:

- The **tolerant** reader (:func:`parse_known_keys`, :func:`read_frontmatter`
  with ``strict=False``) supplies the index's discovery fields. It
  regex-extracts the known keys line by line, so a guide with a malformed
  block still lands in the inventory with whatever keys it does carry. It
  needs nothing outside the standard library.
- The **strict** reader (:func:`load_frontmatter`, ``strict=True``) is what
  validation gates on. PyYAML's safe loader, duplicate keys rejected, and the
  string-typed fields checked so a YAML 1.1 coercion such as
  ``jurisdiction: NO`` (boolean ``False``) fails closed instead of silently
  changing meaning downstream. PyYAML is imported on first use, so the tolerant
  path stays dependency-free.

Both readers see exactly the same block: :func:`extract_frontmatter` is the
only function that decides where a block starts and ends, and every script
goes through it.
"""

import re

#: Frontmatter keys the tolerant reader lifts (the index columns, in order).
KNOWN_KEYS = [
    "name",
    "jurisdiction",
    "category",
    "tier",
    "verified_by",
    "reviewed_by",
    "review_status",
    "tax_year",
    "last_updated",
]

#: Fields that ``docs/skill-template.md`` types as strings. PyYAML follows YAML
#: 1.1 scalar rules, so an unquoted ISO code such as ``NO`` becomes boolean
#: False; the strict reader rejects that rather than routing Norway to nowhere.
STRING_FIELDS = frozenset({
    "name",
    "description",
    "jurisdiction",
    "category",
    "tax_year_notes",
    "verified_by",
    "reviewed_by",
    "review_status",
    "license",
})

#: The block's closing line. ``\s*$`` rather than ``[ \t]*$`` so a closer
#: carrying a stray ``\r`` still closes the block; the match START is what
#: matters, and the callers below never rely on where it ends.
FRONTMATTER_END_RE = re.compile(r"^(---|\.\.\.)\s*$", re.MULTILINE)

#: ``key: value`` at column 0. Tolerates malformed YAML elsewhere in the block.
KEY_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*):[ \t]*(.*)$")


class FrontmatterError(ValueError):
    """Raised by the strict reader when a block is not safe, unambiguous metadata."""


class _StrictMetadata(dict):
    """Parsed fields with the actual root tier's source spelling kept separately."""


# --- Locating the block -----------------------------------------------------


def _closer(text):
    """The match for the closing line, or None. ``text`` must open with ``---``."""
    first_nl = text.find("\n")
    if first_nl == -1 or text[:first_nl].strip() != "---":
        return None, first_nl
    return FRONTMATTER_END_RE.search(text, first_nl + 1), first_nl


def extract_frontmatter(text):
    """The raw frontmatter block (the lines between the delimiters, without
    them), or None when the file has none: no ``---`` at byte 0, anything else
    on that first line, or no closing line."""
    if not text.startswith("---"):
        return None
    close, first_nl = _closer(text)
    if close is None:
        return None
    return text[first_nl + 1:close.start()]


def split_frontmatter(text):
    """``(frontmatter, body)``: the frontmatter with both delimiter lines and
    the newline after the closing one, and everything after it. ``(None, text)``
    when the file has no frontmatter. The editing scripts use this to rewrite
    a body without touching the metadata, or the reverse."""
    if not text.startswith("---"):
        return None, text
    close, _ = _closer(text)
    if close is None:
        return None, text
    line_end = text.find("\n", close.start())
    end = len(text) if line_end == -1 else line_end + 1
    return text[:end], text[end:]


# --- Tolerant reader ----------------------------------------------------------


def clean_value(raw):
    """Normalize a scalar frontmatter value; None for empty and block scalars."""
    value = raw.strip()
    if value in ("", ">", "|", ">-", "|-", ">+", "|+"):
        return None
    # Strip a trailing YAML comment only when the value is unquoted.
    if value[0] in "\"'":
        quote = value[0]
        if len(value) >= 2 and value.rstrip().endswith(quote):
            value = value.strip()[1:-1].strip()
    else:
        value = re.sub(r"\s+#.*$", "", value).strip()
    if value == "" or value.lower() in ("null", "~"):
        return None
    return value


def parse_known_keys(block, keys=KNOWN_KEYS):
    """Regex-extract ``keys`` from a frontmatter block, malformed or not.

    Every key is present in the result, None when absent or empty. The first
    occurrence of a key wins, which is the strict reader's duplicate-key error
    seen from the other side: the tolerant reader never guesses.
    """
    fields = {key: None for key in keys}
    seen = set()
    for line in block.splitlines():
        match = KEY_RE.match(line)
        if not match:
            continue
        key = match.group(1)
        if key not in fields or key in seen:
            continue
        seen.add(key)
        fields[key] = clean_value(match.group(2))
    return fields


# --- Strict reader ------------------------------------------------------------

_LOADER = None


def _unique_key_loader():
    """The SafeLoader subclass that rejects duplicate mapping keys, built once.

    A last-key-wins parse hides which value the author meant. PyYAML is
    imported here, on first use, so importing this module needs nothing
    outside the standard library.
    """
    global _LOADER
    if _LOADER is not None:
        return _LOADER

    import yaml

    class UniqueKeyLoader(yaml.SafeLoader):
        def flatten_mapping(self, node):
            # Freeze direct projection provenance, including its absence.
            if node not in self._scalar_projections:
                projection = None
                for key, value in node.value:
                    if key.tag == "tag:yaml.org,2002:value":
                        self._projection_keys.add(key)
                    if projection is None and key in self._projection_keys:
                        projection = value
                self._scalar_projections[node] = projection
            # Merge operands are flattened recursively before construction.
            merge_seen = False
            for key_node, _ in node.value:
                if key_node.tag == "tag:yaml.org,2002:merge":
                    if merge_seen:
                        raise yaml.constructor.ConstructorError(
                            "while constructing a mapping", node.start_mark,
                            "found duplicate merge key", key_node.start_mark,
                        )
                    merge_seen = True
            return super().flatten_mapping(node)

        def construct_mapping(self, node, deep=False):
            if not isinstance(node, yaml.MappingNode):
                raise yaml.constructor.ConstructorError(
                    "while constructing a mapping", node.start_mark,
                    f"expected a mapping, but found {node.id}", node.start_mark,
                )
            self.flatten_mapping(node)
            mapping = {}
            for key_node, value_node in node.value:
                key = self.construct_object(key_node, deep=deep)
                try:
                    hash(key)
                except TypeError as exc:
                    raise yaml.constructor.ConstructorError(
                        "while constructing a mapping",
                        node.start_mark,
                        "found an unhashable mapping key",
                        key_node.start_mark,
                    ) from exc
                if key in mapping:
                    raise yaml.constructor.ConstructorError(
                        "while constructing a mapping",
                        node.start_mark,
                        f"found duplicate key {key!r}",
                        key_node.start_mark,
                    )
                mapping[key] = self.construct_object(value_node, deep=deep)
            return mapping

        def construct_scalar(self, node):
            if isinstance(node, yaml.MappingNode):
                # Deferred children finish before the document is accepted.
                self.construct_mapping(node)
                projection = self._scalar_projections[node]
                if projection is not None:
                    return self.construct_scalar(projection)
            return super().construct_scalar(node)

        def construct_document(self, node):
            self._document_root = node
            self._ordered_maps = []
            self._scalar_projections = {}
            self._projection_keys = set()
            try:
                data = super().construct_document(node)
                # Deferred aliases must finish before their keys are compared.
                for omap_node, ordered in self._ordered_maps:
                    keys = []
                    for index, (key, _) in enumerate(ordered):
                        mark = omap_node.value[index].value[0][0].start_mark
                        try:
                            duplicate = key in keys
                        except RecursionError as exc:
                            raise yaml.constructor.ConstructorError(
                                "while constructing an ordered map", omap_node.start_mark,
                                "ordered-map keys cannot be compared", mark,
                            ) from exc
                        if duplicate:
                            raise yaml.constructor.ConstructorError(
                                "while constructing an ordered map", omap_node.start_mark,
                                f"found duplicate key {key!r}", mark,
                            )
                        keys.append(key)
                return data
            finally:
                self._document_root = None
                self._ordered_maps.clear()
                self._scalar_projections.clear()
                self._projection_keys.clear()

        def construct_yaml_map(self, node):
            if node is self._document_root:
                data = _StrictMetadata()
                yield data
                data.update(self.construct_mapping(node))
            else:
                yield from super().construct_yaml_map(node)

        def construct_yaml_omap(self, node):
            constructor = super().construct_yaml_omap(node)
            ordered = next(constructor)
            yield ordered
            yield from constructor
            self._ordered_maps.append((node, ordered))

    UniqueKeyLoader.add_constructor("tag:yaml.org,2002:map", UniqueKeyLoader.construct_yaml_map)
    UniqueKeyLoader.add_constructor("tag:yaml.org,2002:omap", UniqueKeyLoader.construct_yaml_omap)

    _LOADER = UniqueKeyLoader
    return _LOADER


def _problem_text(exc):
    problem = getattr(exc, "problem", None) or exc.__class__.__name__
    mark = getattr(exc, "problem_mark", None)
    if mark is None:
        return str(problem)
    return f"line {mark.line + 1}, column {mark.column + 1}: {problem}"


def load_frontmatter(block):
    """Parse one frontmatter block strictly, or raise :class:`FrontmatterError`.

    The result is a mapping with string keys. The fields in
    :data:`STRING_FIELDS` must be strings and ``depends_on`` must be a list of
    non-empty strings, so valid-but-misinterpreted YAML fails closed too.
    """
    import yaml

    loader_class = _unique_key_loader()
    loader = None
    try:
        loader = loader_class(block)
        node = loader.get_single_node()
        tier_source = None
        if isinstance(node, yaml.MappingNode):
            # Capture direct root entries before construction flattens merges.
            for key, value in node.value:
                if key.tag == "tag:yaml.org,2002:str" and key.value == "tier" and key.start_mark.column == 0:
                    match = KEY_RE.match(block.splitlines()[key.start_mark.line])
                    if match and match.group(1) == "tier":
                        tier_source = clean_value(match.group(2))
                        if tier_source in ("1", "2") and not (
                                isinstance(value, yaml.ScalarNode) and
                                value.start_mark.line == value.end_mark.line == key.start_mark.line):
                            tier_source = None
        try:
            metadata = loader.construct_document(node) if node is not None else None
        except (ValueError, TypeError, KeyError, IndexError, AttributeError, RecursionError) as exc:
            # PyYAML's safe scalar constructors use these for invalid input.
            raise FrontmatterError(str(exc) or "invalid YAML scalar") from exc
    except (yaml.YAMLError, RecursionError) as exc:
        raise FrontmatterError(_problem_text(exc)) from exc
    finally:
        if loader is not None:
            loader.dispose()

    if not isinstance(metadata, dict):
        actual = "null" if metadata is None else type(metadata).__name__
        raise FrontmatterError(f"frontmatter root must be a mapping, got {actual}")

    non_string_keys = [key for key in metadata if not isinstance(key, str)]
    if non_string_keys:
        raise FrontmatterError(
            f"frontmatter keys must be strings, got {non_string_keys[0]!r}"
        )

    for key in sorted(STRING_FIELDS & metadata.keys()):
        value = metadata[key]
        if not isinstance(value, str):
            raise FrontmatterError(
                f"`{key}` must be a string, got {type(value).__name__}"
            )

    if "depends_on" in metadata:
        dependencies = metadata["depends_on"]
        if not isinstance(dependencies, list):
            raise FrontmatterError(
                f"`depends_on` must be a YAML list, got {type(dependencies).__name__}"
            )
        if any(not isinstance(item, str) or not item.strip() for item in dependencies):
            raise FrontmatterError("`depends_on` entries must be non-empty strings")

    metadata.tier_source = tier_source
    return metadata


def review_fields(metadata):
    """Tier source spelling and review strings, without changing the strict mapping.

    Keep typed dates and other fields out of the index's lexical columns and
    the validator's format checks. Reviewer markers remain strings; deciding
    whether they identify a reviewer belongs to ``oa_tools.roster``.
    """
    fields = {"tier": metadata.tier_source}
    fields.update({
        key: (metadata[key].strip() or None) if key in metadata else None
        for key in ("reviewed_by", "verified_by")
    })
    # A supplied blank status must reach the validator as invalid, not absent.
    fields["review_status"] = metadata["review_status"].strip() if "review_status" in metadata else None
    return fields


# --- The one entry point -------------------------------------------------------


def read_frontmatter(text, *, strict=False):
    """The metadata of a whole file's text, or None when it has no frontmatter.

    ``strict=False`` returns the tolerant reader's dict of :data:`KNOWN_KEYS`
    (missing ones None). ``strict=True`` returns the full mapping from the
    strict reader and raises :class:`FrontmatterError` on anything it rejects.
    """
    block = extract_frontmatter(text)
    if block is None:
        return None
    if strict:
        return load_frontmatter(block)
    return parse_known_keys(block)
