# When every number in a guide comes from one place

> Entry of 2026-09-10 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

Three jurisdictions failed the same way, and it was the same shape each time: an
entire table of rates and thresholds resting on a single non-authority page.

| Jurisdiction | Source carrying the table | What was wrong |
|---|---|---|
| Benin | one HR-platform page | every IRPP band boundary, and band 4's rate |
| Zambia | one page on `zambiaprice.com` | unknowable — the domain now serves gambling SEO |
| Burundi | one HR-platform page | unknowable — `obr.bi` answers with a crash |

Benin is the one that makes the case. Those figures were not hedged and not
marked uncertain. They were simply wrong, and the shared source is the thing a
reader could have noticed *without knowing any Beninese tax law*.

`scripts/list-single-source-blocks.py` measures it: of the bullets in a guide
that state a number **and** carry a citation, what share point at one host.

The split matters more than the count. Concentration on a revenue service is a
guide doing it right. Concentration on PwC is weaker but honest, and is how much
of this corpus is necessarily built — see the section above on authorities that
cannot be read. Reported first is the Benin case, where the one host is neither.

```
other  38 guides    publisher  181    authority  79      (of 515 with 4+ facts)
```

`remotepeople.com` carries four of those 38 outright, `taxatlas.io` three,
`remotesolutionsafrica.com` two. The Benin fix shows up where it should: its two
guides moved out of `other` and into `authority`.

This is not a defect detector and never gates CI. A single-sourced guide is not
a wrong guide; it is one with no internal corroboration, which is a statement
about what a mistake would cost, not evidence that one was made.
