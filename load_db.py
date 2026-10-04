from pathlib import Path
import sqlite3
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "claims.db"

def load():
    conn = sqlite3.connect(DB)
    pd.read_csv(ROOT / "data/source_claims.csv").to_sql("source_claims", conn, if_exists="replace", index=False)
    pd.read_csv(ROOT / "data/warehouse_claims.csv").to_sql("warehouse_claims", conn, if_exists="replace", index=False)
    conn.close()
    return DB

if __name__ == "__main__":
    print(f"Loaded database: {load()}")
