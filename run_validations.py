from pathlib import Path
import csv
import sqlite3
from datetime import datetime, timezone
from rules import RULES
from load_db import DB

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "reports" / "validation_results.csv"

def run(db_path=DB, report_path=REPORT):
    results = []
    with sqlite3.connect(db_path) as conn:
        for rule_id, name, sql, expected in RULES:
            actual = conn.execute(sql).fetchone()[0]
            results.append({
                "run_timestamp_utc": datetime.now(timezone.utc).isoformat(),
                "rule_id": rule_id, "test_name": name,
                "expected_defects": expected, "actual_defects": actual,
                "status": "PASS" if actual == expected else "FAIL"
            })
    report_path.parent.mkdir(exist_ok=True)
    with report_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=results[0].keys())
        writer.writeheader(); writer.writerows(results)
    passed = sum(r["status"] == "PASS" for r in results)
    print(f"Validation complete: {passed}/{len(results)} passed. Report: {report_path}")
    return results

if __name__ == "__main__":
    run()
