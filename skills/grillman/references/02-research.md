# 02 Research (only what the brief leaves uncertain)

## When
Models, datasets, libraries, versions, licences, APIs, benchmarks, prior art. Not for things you already know and can verify by running code.

## How
1. Search for current information (versions and repos change). Prefer official docs, papers, model cards, repo READMEs.
2. Open the actual page, do not trust a snippet. Inspect real samples of any dataset (look at 20 items) before trusting its labels.
3. Check licence and terms for every model, dataset and library you will ship or depend on. Flag copyleft (AGPL/GPL) and "research only" licences in the README.
4. Time-box: stop when a decision is clear. Do not collect links for decoration.

## Record (max 5 lines per decision, in CONTEXT.md)
`Choice | Why (tied to an E-id) | Rejected alternative + reason | Risk | Licence`

## Rules
- Never cite a source you did not open. Never invent a URL, metric or benchmark number.
- Prefer a strong baseline you can reproduce over a fancy method you cannot verify.
- If two approaches are close, run a quick spike on real data and let the numbers decide.
