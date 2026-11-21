"""Shared helpers imported by every notebook (Requirement 4.9).

Anything used in more than one notebook belongs here rather than being
copied between notebooks.
"""

from pathlib import Path
import random

import numpy as np

# --- Paths -----------------------------------------------------------------
# Relative to the repository, never absolute, so the code runs on any machine.
ROOT = Path(__file__).resolve().parent.parent
DATA_RAW = ROOT / "data" / "raw"
DATA_PROCESSED = ROOT / "data" / "processed"
FIGURES = ROOT / "figures"

# --- Data -----------------------------------------------------------------
# Years of the Kaggle dataset hwaitt/horse-racing used in the project.
YEARS = list(range(2010, 2021))  # 2010–2020 inclusive


def load_raw(kind: str, years=None):
    """Load and stack the raw yearly files for `kind` ("horses" or "races").

    Reads data/raw/<kind>_<year>.csv for each year (written by 01_get_data.ipynb)
    and returns one DataFrame with a `file_year` column saying which file each row came from.
    """
    import pandas as pd

    if kind not in ("horses", "races"):
        raise ValueError(f"kind must be 'horses' or 'races', not {kind!r}")
    frames = []
    for year in years or YEARS:
        path = DATA_RAW / f"{kind}_{year}.csv"
        if not path.exists():
            raise FileNotFoundError(f"{path} not found: run code/01_get_data.ipynb first")
        frames.append(pd.read_csv(path, low_memory=False).assign(file_year=year))
    return pd.concat(frames, ignore_index=True)


# --- Reproducibility -------------------------------------------------------
SEED = 42


def set_seed(seed: int = SEED) -> None:
    """Fix the random seeds so every run gives the same numbers."""
    random.seed(seed)
    np.random.seed(seed)


def ensure_dirs() -> None:
    """Create the output folders if they do not exist yet."""
    for d in (DATA_RAW, DATA_PROCESSED, FIGURES):
        d.mkdir(parents=True, exist_ok=True)


def save_figure(fig, name: str) -> Path:
    """Save a matplotlib figure to figures/<name>.pdf and .png for the paper."""
    ensure_dirs()
    pdf_path = FIGURES / f"{name}.pdf"
    fig.savefig(pdf_path, bbox_inches="tight")
    fig.savefig(FIGURES / f"{name}.png", dpi=200, bbox_inches="tight")
    return pdf_path


def save_table(df, name: str) -> Path:
    """Save a pandas DataFrame as a LaTeX table in figures/<name>.tex."""
    ensure_dirs()
    path = FIGURES / f"{name}.tex"
    df.to_latex(path, index=True, float_format="%.3f")
    return path
