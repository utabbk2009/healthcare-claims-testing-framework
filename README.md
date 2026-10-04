# Automated Healthcare Claims Data Testing Framework

A portfolio project that uses **Python, SQL, SQLite, pandas, and pytest** to test healthcare claims data quality and source-to-target integrity. All records are synthetic and contain no protected health information.

## Business problem

Claims teams need reliable data before using it for payment, reporting, analytics, or machine learning. This project generates a clean source dataset, creates a warehouse copy with deliberate defects, runs reusable SQL controls, and exports an audit-friendly test report.

## Tests included

- Missing member and claim identifiers
- Duplicate claim IDs
- Negative paid amounts
- Invalid claim statuses
- Submission dates before service dates
- Paid amounts exceeding charges
- Source-to-target row-count reconciliation
- Automated query execution tests with pytest

## Project structure

```text
src/       data generation, database loading, validation engine
sql/       standalone SQL quality checks
tests/     pytest tests
data/      synthetic source and target claims
reports/   generated validation evidence
```

## Quick start

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python run_project.py
pytest -v
```

Open `reports/validation_results.csv` to see PASS/FAIL evidence. Failures are expected because the target data intentionally contains defects.

## Portfolio talking points

- Translated business rules into executable SQL controls.
- Automated repeatable data-quality testing with Python.
- Reconciled source and warehouse data after an ETL-style load.
- Produced traceable results containing rule IDs, expected values, actual defects, status, and timestamps.
- Designed the framework so additional claims rules can be added in `src/rules.py` without changing the validation engine.

## Suggested resume bullet

Built an automated healthcare claims data-testing framework using Python, SQL, SQLite, pandas, and pytest; validated source-to-target completeness, business-rule accuracy, duplicates, nulls, financial integrity, and date sequencing while producing audit-ready PASS/FAIL reports.

## Safe-use note

The included data is synthetic. Do not place real member, patient, or claim information in a public portfolio repository.
