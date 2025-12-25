from __future__ import annotations

import os
from pathlib import Path

import typer
from dotenv import load_dotenv
from rich import print

app = typer.Typer(add_completion=False, help="Clinical Risk CLI")

def _ensure_dirs() -> None:
    Path("artifacts").mkdir(exist_ok=True)
    Path("data").mkdir(exist_ok=True)

@app.command("doctor")
def doctor():
    """Check environment + folder health."""
    load_dotenv()
    _ensure_dirs()

    print("[bold green]Clinical Risk Project Doctor[/bold green]")
    print("Python:", os.sys.version.split()[0])

    db_uri = os.getenv("MIMIC_DB_URI", "")
    mlflow_uri = os.getenv("MLFLOW_TRACKING_URI", "file:./artifacts/mlflow")
    print("MIMIC_DB_URI set:", bool(db_uri))
    print("MLFLOW_TRACKING_URI:", mlflow_uri)

    import pandas  # noqa: F401
    import sklearn  # noqa: F401
    import mlflow  # noqa: F401

    print("[bold green]Imports OK[/bold green]")

@app.command("version")
def version():
    """Print package version info."""
    print("clinical-risk-mimic v0.1.0")