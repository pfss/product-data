#!/usr/bin/env python3
"""
Builds netflix_pricing_data.sqlite — illustrative data for the Pricing
Strategy Manager work sample. All figures are constructed assumptions,
not real Netflix data. Run: python3 build_db.py
"""
import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "netflix_pricing_data.sqlite")
if os.path.exists(DB_PATH):
    os.remove(DB_PATH)

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

cur.executescript("""
CREATE TABLE plans (
    plan_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    tier_order INTEGER NOT NULL,
    current_price_usd REAL NOT NULL,
    description TEXT NOT NULL
);

CREATE TABLE quarters (
    quarter_id INTEGER PRIMARY KEY,
    label TEXT NOT NULL,
    sort_order INTEGER NOT NULL
);

CREATE TABLE plan_metrics (
    metric_id INTEGER PRIMARY KEY,
    plan_id INTEGER NOT NULL REFERENCES plans(plan_id),
    quarter_id INTEGER NOT NULL REFERENCES quarters(quarter_id),
    subscribers_m REAL NOT NULL,
    arpu_usd REAL NOT NULL,
    churn_rate_pct REAL NOT NULL
);

CREATE TABLE elasticity_assumptions (
    plan_id INTEGER PRIMARY KEY REFERENCES plans(plan_id),
    price_elasticity REAL NOT NULL,
    wtp_p25_usd REAL NOT NULL,
    wtp_median_usd REAL NOT NULL,
    wtp_p75_usd REAL NOT NULL
);

CREATE TABLE model_constants (
    key TEXT PRIMARY KEY,
    value REAL NOT NULL,
    note TEXT NOT NULL
);
""")

plans = [
    (1, "Standard with Ads", 1, 7.99, "Ad-supported entry tier — highest price sensitivity, growth engine"),
    (2, "Standard", 2, 17.99, "Ad-free mainstream tier — the largest base, most exposed to trade-down risk"),
    (3, "Premium", 3, 24.99, "4K + multi-room tier — lowest price sensitivity, feature-anchored"),
]
cur.executemany("INSERT INTO plans VALUES (?,?,?,?,?)", plans)

quarters = [
    (1, "Q2 25", 1), (2, "Q3 25", 2), (3, "Q4 25", 3),
    (4, "Q1 26", 4), (5, "Q2 26", 5), (6, "Q3 26", 6),
]
cur.executemany("INSERT INTO quarters VALUES (?,?,?)", quarters)

# subscribers_m, arpu_usd, churn_rate_pct per plan per quarter (illustrative trend)
plan_metrics = [
    # Standard with Ads — accelerating growth, improving churn as tier matures
    (1, 1, 40.0, 6.30, 4.8), (1, 2, 46.0, 6.35, 4.7), (1, 3, 55.0, 6.40, 4.6),
    (1, 4, 62.0, 6.45, 4.5), (1, 5, 70.0, 6.50, 4.4), (1, 6, 79.0, 6.55, 4.3),
    # Standard — slow erosion as members trade down to Ads or up to Premium
    (2, 1, 130.0, 15.80, 3.00), (2, 2, 128.0, 15.85, 3.05), (2, 3, 125.0, 15.90, 3.10),
    (2, 4, 121.0, 15.95, 3.15), (2, 5, 117.0, 16.00, 3.20), (2, 6, 112.0, 16.05, 3.25),
    # Premium — steady modest growth, best-in-class retention
    (3, 1, 55.0, 22.10, 1.80), (3, 2, 57.0, 22.20, 1.75), (3, 3, 59.0, 22.30, 1.70),
    (3, 4, 62.0, 22.40, 1.65), (3, 5, 65.0, 22.50, 1.60), (3, 6, 69.0, 22.60, 1.55),
]
cur.executemany(
    "INSERT INTO plan_metrics (plan_id, quarter_id, subscribers_m, arpu_usd, churn_rate_pct) VALUES (?,?,?,?,?)",
    plan_metrics,
)

elasticity = [
    (1, -0.95, 5.00, 7.50, 10.00),
    (2, -0.55, 14.00, 18.50, 23.00),
    (3, -0.30, 21.00, 27.00, 34.00),
]
cur.executemany("INSERT INTO elasticity_assumptions VALUES (?,?,?,?,?)", elasticity)

constants = [
    ("churn_risk_threshold_pct", 8.0, "Projected subscriber decline (%) beyond which a price move is flagged high-risk"),
    ("wtp_value_note", 1.0, "WTP percentiles are illustrative survey-style estimates, not measured conjoint data"),
]
cur.executemany("INSERT INTO model_constants VALUES (?,?,?)", constants)

conn.commit()
conn.close()
print(f"Built {DB_PATH}")
