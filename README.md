# India CSR Flows

A single-page snapshot of mandatory CSR spending (Section 135, Companies Act 2013) by 40 Indian companies for FY2024-25, with areas of impact, impact details, FY2025-26 figures where found, and future commitments. Amounts are in ₹ crore.

Snapshot date: 7 October 2026. This is not a live feed.

## What is in it

- `index.html`: the finished page. It is self-contained and can be opened directly or served from GitHub Pages.
- `src/companies.json`: the company dataset. Every field is taken from a published source, and each company lists its links. Missing values are `null` and the page shows them as "Not found in the sources reviewed".
- `src/page.html`: the page template. National, thematic, state and commitment figures are written into its script block with their sources.
- `src/build.py`: rebuilds `index.html` from the two files above.

## Rebuild

```
python3 src/build.py
```

## Method and limits

- The list holds the 40 companies for which a FY25 figure could be verified. It is not a certified national top 40 or top 100.
- The main figure is the FY25 Section 135 spend as reported by PRIME Infobase or the company's annual report. Nine companies carry a "Check basis" tag because their figure is a group, standalone or non-Section 135 number.
- Sector groups and PSU tags are labels added for readability, not categories from any source.
- Some publishers block automated reading, and the MCA portal and Dataful dashboards did not load. Figures from those came from search result excerpts, and the sector table is partial for that reason.
- Totals and shares calculated from published figures are marked "computed" on the page.
