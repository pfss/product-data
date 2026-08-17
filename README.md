# Content Format Investment Framework

A database-backed, interactive capital allocation model — built as a work sample for a Product Finance & Strategy role. Compares Games, Live, and Podcasts as content-format investments using unit economics built from scratch (no established benchmark), with a live scenario engine and six quarters of trend data.

**[Live demo →](https://product-data-repo.vercel.app)**

## Other work samples in this repo

- **[`pricing-strategy-manager/`](pricing-strategy-manager/)** ([live demo](https://pricing-strategy-manager.vercel.app)) — a price-elasticity, willingness-to-pay, and competitive pricing model built for the *Pricing Strategy Manager* role. Same self-contained SQL.js-backed dashboard pattern as this one, applied to plan-tier pricing instead of content-format investment.

## What's in here

- `index.html` — the full dashboard. Single self-contained file: loads an embedded SQLite database via [sql.js](https://github.com/sql-js/sql.js) (SQLite compiled to WebAssembly) and runs real SQL queries client-side to power the trend chart and scenario model. No server, no build step.
- `data/content_format_data.sqlite` — the underlying database (5 tables: `formats`, `quarters`, `quarterly_metrics`, `allocation_defaults`, `model_constants`). Also embedded (base64) directly inside `index.html` so the dashboard works standalone.
- `MEMO.md` — a one-page decision memo written in the style of the target company's internal memo culture, summarizing the model's recommendation.

## Running it locally

No build step — just open `index.html` in a browser, or serve it:

```bash
python3 -m http.server 8000
# then visit http://localhost:8000
```

## Deploying

This is a static site — any static host works:

```bash
npm i -g vercel
vercel deploy
```

Or drag-and-drop `index.html` (with the `data/` folder alongside it, though the DB is also embedded so this isn't strictly required) into Vercel/Netlify's dashboard.

## Data note

All figures in the database are illustrative assumptions built to demonstrate the modeling approach — not real financial data from any company. See the in-app disclaimer and `MEMO.md` for details.
