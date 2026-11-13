"""Numerical agreement and figure functions extracted from the thesis script.

The original agreement() and plot() bodies are unchanged. Original raw-response
reconstruction, expert-cutoff checks and participant-availability assertions are
omitted. This module does not read human evaluation records or validate answer
semantics. The public reconstruction adapter supplies numeric inputs and OUT.
"""
import numpy as np
import matplotlib.pyplot as plt
from generate_benchmark_figures import style

OUT = None


def agreement(matrix):
    n = int(matrix.sum())
    observed = np.trace(matrix)/n
    expected = np.outer(matrix.sum(axis=1), matrix.sum(axis=0))/n
    kappa = (observed - np.trace(expected)/n)/(1 - np.trace(expected)/n)
    weights = (np.arange(3)[:, None]-np.arange(3)[None, :])**2/4
    weighted = 1 - (matrix*weights).sum()/(expected*weights).sum()
    return {"n": n, "exact": int(np.trace(matrix)), "agreement": float(observed), "unweighted_kappa": float(kappa), "quadratic_weighted_kappa": float(weighted)}



def plot(matrix, metrics):
    style()
    fig = plt.figure(figsize=(4.8, 3.65))
    ax = fig.add_axes((.20, .24, .56, .65))
    from matplotlib.colors import LinearSegmentedColormap
    colors = LinearSegmentedColormap.from_list("judge_counts", ["#FAFAFA", "#0072B2"])
    heatmap = ax.imshow(matrix, cmap=colors, vmin=0, vmax=270, interpolation="none")
    color_ax = fig.add_axes((.81, .24, .035, .65))
    colorbar = fig.colorbar(heatmap, cax=color_ax, ticks=[0, 90, 180, 270])
    colorbar.set_label("Paired output count", fontsize=9)
    colorbar.outline.set_linewidth(.5)
    for i in range(3):
        for j in range(3):
            ax.text(j, i, str(matrix[i, j]), ha="center", va="center", color="white" if matrix[i, j] > 135 else "#171717", fontsize=14)
    ax.set(xticks=[0, 1, 2], yticks=[0, 1, 2], xlabel="Gemini J2 correctness score", ylabel="Cohere J1 correctness score")
    ax.set_xticks(np.arange(-.5, 3, 1), minor=True)
    ax.set_yticks(np.arange(-.5, 3, 1), minor=True)
    ax.grid(which="minor", color="white", linewidth=1.1)
    ax.tick_params(which="both", length=0)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.set_title("Provisional inter-judge agreement", fontsize=11, pad=11)
    fig.text(.5, .065, f"Exact agreement: {metrics['exact']}/{metrics['n']} ({100*metrics['agreement']:.1f}%)", ha="center", fontsize=10)
    fig.savefig(OUT / "provisional_judge_correctness_matrix.pdf", metadata={"CreationDate": None, "ModDate": None})
    fig.savefig(OUT / "provisional_judge_correctness_matrix.png", dpi=450)
    plt.close(fig)

