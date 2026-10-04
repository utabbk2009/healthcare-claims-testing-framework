import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from generate_data import build_claims
from load_db import load, DB
from rules import RULES


def test_generator_creates_unique_clean_source_claims():
    rows = build_claims(50)
    assert len(rows) == 50
    assert len({r["claim_id"] for r in rows}) == 50
    assert all(r["member_id"] for r in rows)
    assert all(r["paid_amount"] >= 0 for r in rows)


def test_all_rule_queries_execute():
    if not DB.exists():
        from generate_data import write_csv, inject_quality_issues
        source = build_claims(20)
        (ROOT / "data").mkdir(exist_ok=True)
        write_csv(ROOT / "data/source_claims.csv", source)
        write_csv(ROOT / "data/warehouse_claims.csv", inject_quality_issues([dict(r) for r in build_claims(50)]))
        load()
    with sqlite3.connect(DB) as conn:
        for rule_id, name, sql, expected in RULES:
            value = conn.execute(sql).fetchone()[0]
            assert isinstance(value, (int, float)), f"{rule_id} did not return a number"
