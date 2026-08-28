import sys
from importlib.metadata import version, PackageNotFoundError
from typing import Any, Tuple


def check_dependencies() -> bool:
    """Check if required dependencies are installed."""
    check = True

    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    try:
        ver = version("pandas")
        print(f"[OK] pandas ({ver}) - Data manipulation ready")
    except PackageNotFoundError:
        print("[KO] pandas - Data manipulation not ready")
        check = False

    try:
        ver = version("numpy")
        print(f"[OK] numpy ({ver}) - Numerical computation ready")
    except PackageNotFoundError:
        print("[KO] numpy - Numerical computation not ready")
        check = False

    try:
        ver = version("matplotlib")
        print(f"[OK] matplotlib ({ver}) - Visualization ready")
    except PackageNotFoundError:
        print("[KO] matplotlib - Visualization not ready")
        check = False

    if not check:
        sys.stderr.write("\nMissing dependencies detected!\n")
        sys.stderr.write("Please install required packages using pip or Poetry:\n")
        sys.stderr.write("  pip:    pip install -r requirements.txt\n")
        sys.stderr.write("  poetry: poetry install\n")
        sys.exit(1)

    return check


def data_generation() -> Tuple[Any, Any]:
    """Synthetic data generation."""
    import numpy as np
    import pandas as pd

    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")

    rng = np.random.default_rng(42)
    data = rng.normal(loc=0.0, scale=1.0, size=1000)

    df = pd.DataFrame({
        "timestamp": range(1000),
        "signal_strength": data,
        "anomaly_score": np.abs(data)
    })

    return df, data


def image_generation(data: Any) -> None:
    """Histogram generation and export."""
    import matplotlib.pyplot as plt

    print("\nGenerating visualization...")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(data, bins=50, color="green", alpha=0.7, edgecolor="black")
    ax.set_title("Matrix Data Distribution")
    ax.set_xlabel("Signal Value")
    ax.set_ylabel("Frequency")
    ax.grid(axis="y", linestyle="--", alpha=0.5)

    fig.savefig("matrix_analysis.png", dpi=150, bbox_inches="tight")
    plt.close(fig)
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    if not check_dependencies():
        sys.exit(1)

    df, data = data_generation()
    image_generation(data)

