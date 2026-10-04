from pathlib import Path
import csv
import random
from datetime import date, timedelta

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
random.seed(42)

MEMBERS = [f"M{i:04d}" for i in range(1, 51)]
PROVIDERS = [f"P{i:03d}" for i in range(1, 11)]
STATUSES = ["PAID", "DENIED", "PENDING"]

def build_claims(n=200):
    rows = []
    start = date(2026, 1, 1)
    for i in range(1, n + 1):
        service = start + timedelta(days=random.randint(0, 180))
        submitted = service + timedelta(days=random.randint(0, 7))
        charge = round(random.uniform(75, 5000), 2)
        status = random.choice(STATUSES)
        paid = 0.0 if status != "PAID" else round(charge * random.uniform(.45, .95), 2)
        rows.append({
            "claim_id": f"C{i:05d}", "member_id": random.choice(MEMBERS),
            "provider_id": random.choice(PROVIDERS), "service_date": service.isoformat(),
            "submitted_date": submitted.isoformat(), "claim_status": status,
            "charge_amount": charge, "paid_amount": paid,
            "diagnosis_code": f"Z{random.randint(10,99)}.{random.randint(0,9)}"
        })
    return rows

def inject_quality_issues(rows):
    # Synthetic defects deliberately added to demonstrate detection.
    rows[4]["member_id"] = ""
    rows[12]["paid_amount"] = -25.00
    rows[20]["submitted_date"] = "2025-12-01"
    rows[31]["claim_status"] = "UNKNOWN"
    rows.append(dict(rows[40]))
    return rows

def write_csv(path, rows):
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader(); writer.writerows(rows)

if __name__ == "__main__":
    DATA.mkdir(exist_ok=True)
    source = build_claims()
    warehouse = inject_quality_issues([dict(r) for r in source])
    write_csv(DATA / "source_claims.csv", source)
    write_csv(DATA / "warehouse_claims.csv", warehouse)
    print(f"Created {len(source)} source and {len(warehouse)} warehouse rows")
