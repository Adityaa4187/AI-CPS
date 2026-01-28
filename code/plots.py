# plots.py
import os
import numpy as np
import matplotlib.pyplot as plt


def _save_show_close(save_path):
    plt.tight_layout()
    plt.savefig(save_path, dpi=200)
    plt.show()
    plt.close()
    print(f"[SAVED] {save_path}")


# EXISTING PLOTS (KEEP SAME)
def plot_numeric_corr(corr_sorted, out_dir):
    os.makedirs(out_dir, exist_ok=True)

    plt.figure(figsize=(12, 6))
    corr_sorted.plot(kind="bar")
    plt.axhline(0, linewidth=1)
    plt.title("Numeric Feature Correlation vs Attrition")
    plt.ylabel("Pearson Correlation")
    plt.xticks(rotation=75)

    out_path = os.path.join(out_dir, "numeric_corr_bar.png")
    _save_show_close(out_path)


def plot_cramers_v(cramer_series, out_dir):
    os.makedirs(out_dir, exist_ok=True)

    plt.figure(figsize=(12, 6))
    cramer_series.plot(kind="bar")
    plt.title("Categorical Feature Association vs Attrition (Cramér’s V)")
    plt.ylabel("Cramér’s V (0 to 1)")
    plt.xticks(rotation=75)

    out_path = os.path.join(out_dir, "categorical_cramersv_bar.png")
    _save_show_close(out_path)


