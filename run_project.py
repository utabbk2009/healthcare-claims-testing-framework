import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def step(script):
    subprocess.run([sys.executable, str(ROOT / "src" / script)], check=True)

if __name__ == "__main__":
    step("generate_data.py")
    step("load_db.py")
    step("run_validations.py")
    print("Next: run 'pytest -v' to test the framework code.")
