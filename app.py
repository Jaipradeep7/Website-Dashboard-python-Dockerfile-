from flask import Flask, render_template, jsonify
import json
from datetime import datetime, timedelta
import random

app = Flask(__name__)

# ── Sample Data ──────────────────────────────────────────────────────────────

CATEGORIES = ["Electronics", "Apparel", "Groceries", "Home & Garden", "Sports", "Beauty"]

def generate_monthly_sales():
    months = []
    base = datetime(2024, 1, 1)
    for i in range(12):
        month = base + timedelta(days=30 * i)
        months.append(month.strftime("%b %Y"))
    return months

def generate_sales_data():
    months = generate_monthly_sales()
    data = {}
    for cat in CATEGORIES:
        base_val = random.randint(50000, 200000)
        trend = random.uniform(0.95, 1.08)
        data[cat] = []
        val = base_val
        for _ in months:
            noise = random.uniform(0.88, 1.15)
            val = int(val * trend * noise)
            data[cat].append(val)
    return {"months": months, "series": data}

def generate_kpi():
    return {
        "total_revenue":   {"value": 4_823_150, "change": 12.4},
        "total_orders":    {"value": 38_274,    "change": 8.1},
        "avg_order_value": {"value": 126,        "change": 3.9},
        "top_category":    {"value": "Electronics", "change": 22.7},
    }

def generate_top_products():
    products = [
        {"name": "iPhone 15 Pro", "category": "Electronics", "sales": 1_240_000, "units": 4_100},
        {"name": "Nike Air Max",   "category": "Apparel",     "sales": 860_000,  "units": 12_300},
        {"name": "Instant Pot",    "category": "Home & Garden","sales": 530_000, "units": 8_900},
        {"name": "Protein Powder", "category": "Sports",       "sales": 410_000, "units": 14_500},
        {"name": "Serum Kit",      "category": "Beauty",       "sales": 380_000, "units": 9_200},
        {"name": "Organic Bundle", "category": "Groceries",    "sales": 295_000, "units": 21_400},
    ]
    return products

def generate_region_data():
    regions = ["North", "South", "East", "West", "Central"]
    return [
        {"region": r, "sales": random.randint(400_000, 1_200_000), "growth": round(random.uniform(-5, 25), 1)}
        for r in regions
    ]

# ── Routes ────────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/sales")
def api_sales():
    return jsonify(generate_sales_data())

@app.route("/api/kpi")
def api_kpi():
    return jsonify(generate_kpi())

@app.route("/api/top-products")
def api_top_products():
    return jsonify(generate_top_products())

@app.route("/api/regions")
def api_regions():
    return jsonify(generate_region_data())

@app.route("/api/category-mix")
def api_category_mix():
    mix = {cat: random.randint(80_000, 600_000) for cat in CATEGORIES}
    return jsonify(mix)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
