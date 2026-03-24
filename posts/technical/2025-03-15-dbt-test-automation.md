---
title: Building a DBT Test Automation Framework
date: March 15, 2025
excerpt: How I built a framework that reduced downstream data quality issues by 85% — the patterns, the gotchas, and what I'd do differently.
tags: DBT, Snowflake, Python, Data Quality
---

# Building a DBT Test Automation Framework

Data quality issues are expensive. A single bad row in the wrong table can cascade into wrong dashboards, wrong reports, and wrong decisions. I learned this the hard way — which is why I built a test automation framework that reduced downstream issues by **85%**.

Here's how it works, and what I learned.

## The Problem

Our DBT project had grown to 200+ models across 5 domains. We had *some* tests — `unique`, `not_null`, `accepted_values` — but they were scattered, inconsistently applied, and mostly written by hand for the tables someone remembered to test.

The result: silent failures. Data would pass all tests and still be wrong.

## The Approach

Instead of writing tests per-table, I wanted a **metadata-driven** approach:

1. Define test rules in a YAML config file
2. Auto-generate `schema.yml` test blocks from that config
3. Run them as part of the CI/CD pipeline on every merge

```python
# generate_tests.py
import yaml
from pathlib import Path

def generate_dbt_tests(config_path: str, output_path: str):
    with open(config_path) as f:
        config = yaml.safe_load(f)

    models = []
    for table, rules in config["tables"].items():
        columns = []
        for col, tests in rules["columns"].items():
            columns.append({"name": col, "tests": tests})
        models.append({"name": table, "columns": columns})

    schema = {"version": 2, "models": models}
    with open(output_path, "w") as f:
        yaml.dump(schema, f, default_flow_style=False)
```

## Results

After rolling this out across all 5 domains:

- **85% reduction** in downstream data issues reported by stakeholders
- Test coverage went from ~30% of columns to **100%**
- New model onboarding time dropped by **60%** — tests generated automatically

## What I'd Do Differently

Build in **custom severity levels** from day one. Not all test failures are equal — a null in a primary key is a showstopper; a null in an optional enrichment field is a warning. DBT supports `warn` vs `error` severity, but wiring that into the config cleanly took extra iteration.

---

*Questions? Reach out on LinkedIn or open an issue on GitHub.*
