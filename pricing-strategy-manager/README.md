# Plan Pricing & Elasticity Model

A database-backed, interactive price-elasticity model — built as a work sample for the *Pricing Strategy Manager* role (Commerce Product Org). Models Netflix's three plan tiers (Standard with Ads, Standard, Premium) on willingness-to-pay, price elasticity, and projected revenue impact, with a live price-change scenario engine and six quarters of subscriber-mix trend data.

**[Live demo →](#)** *(add your deployed URL here once live)*

## What's in here

- `index.html` — the full dashboard. Single self-contained file: loads an embedded SQLite database via [sql.js](https://github.com/sql-js/sql.js) (SQLite compiled to WebAssembly) and runs real SQL queries client-side to power the trend chart, WTP cards, and scenario engine. No server, no build step.
- `data/netflix_pricing_data.sqlite` — the underlying database (5 tables: `plans`, `quarters`, `plan_metrics`, `elasticity_assumptions`, `model_constants`). Also embedded (base64) directly inside `index.html` so the dashboard works standalone.
- `data/build_db.py` — the script that generates the SQLite database from scratch, for reproducibility.
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

All figures in the database are illustrative assumptions built to demonstrate the modeling approach — not real financial data from any company. Price elasticity coefficients and willingness-to-pay ranges are informed estimates, not measured conjoint data. See the in-app disclaimer and `MEMO.md` for details.
