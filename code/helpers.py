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
