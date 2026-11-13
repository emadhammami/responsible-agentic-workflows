from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter, FuncFormatter
from matplotlib.lines import Line2D

BASE = Path(
    "/home/emadh/primary-benchmark-results/PRIMARY-BENCHMARK-V1"
)

INPUT = BASE / "execution_figures_v1/data/task_condition_means.csv"
OUT = BASE / "execution_figures_v2"

# ============================================================
# 1. LOAD + STRICT DATA GUARDS
# ============================================================

df = pd.read_csv(INPUT)

required = {
    "task_id",
    "UC",
    "condition",
    "n_repetitions",
    "total_tokens",
    "llm_calls",
    "retrieval_calls",
    "end_to_end_ms",
}

missing = required - set(df.columns)
assert not missing, f"Missing columns: {sorted(missing)}"

assert len(df) == 90, len(df)
assert df["task_id"].nunique() == 30
assert set(df["condition"]) == {"B0", "B1", "G1"}
assert (df.groupby("condition").size() == 30).all()
assert (df["n_repetitions"] == 3).all()

check_cols = [
    "total_tokens",
    "llm_calls",
    "retrieval_calls",
    "end_to_end_ms",
]

assert not df[check_cols].isna().any().any()
assert (df[check_cols] >= 0).all().all()

# One row = one task-condition, aggregated across three repetitions.
plot_df = df[
    [
        "task_id",
        "UC",
        "condition",
        "n_repetitions",
        "total_tokens",
        "end_to_end_ms",
        "llm_calls",
        "retrieval_calls",
    ]
].copy()

plot_df["latency_s"] = plot_df["end_to_end_ms"] / 1000.0

plot_df.to_csv(
    OUT / "data/figure01_source_data.csv",
    index=False,
)

# ============================================================
# 2. IEEE-ORIENTED TYPOGRAPHY
# ============================================================

font_candidates = [
    "Times New Roman",
    "Times",
    "Nimbus Roman",
    "Liberation Serif",
    "DejaVu Serif",
]

available = {
    f.name
    for f in plt.matplotlib.font_manager.fontManager.ttflist
}

font = next(
    (f for f in font_candidates if f in available),
    "DejaVu Serif",
)

plt.rcParams.update(
    {
        "font.family": "serif",
        "font.serif": [font],
        "font.size": 8.0,
        "axes.labelsize": 8.2,
        "xtick.labelsize": 7.6,
        "ytick.labelsize": 7.6,
        "legend.fontsize": 7.4,
        "axes.linewidth": 0.75,
        "lines.linewidth": 1.7,
        "lines.solid_capstyle": "round",
        "lines.solid_joinstyle": "round",
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
        "svg.fonttype": "none",
        "savefig.dpi": 600,
    }
)

# ============================================================
# 3. COLOR SYSTEM
# ============================================================

# B0 = supporting conventional RAG reference
# B1/G1 = primary matched agentic comparison
#
# Blue + vermillion are based on a colorblind-friendly palette.

CONDITION_COLORS = {
    "B0": "#929292",
    "B1": "#0072B2",
    "G1": "#D55E00",
}

CONDITION_WIDTHS = {
    "B0": 1.65,
    "B1": 2.05,
    "G1": 2.05,
}

# Discrete operational-count palette.
# Neutral blue-gray/teal sequence for discrete call counts.
# Deliberately distinct from the B1 blue and G1 orange condition encoding.
CALL_COLORS = {
    1: "#E8ECEC",
    2: "#C5D6D6",
    3: "#91AFAF",
    4: "#628787",
    5: "#365F5F",
}

conditions = ["B0", "B1", "G1"]

# ============================================================
# 4. HELPERS
# ============================================================

def ecdf(values):
    values = np.asarray(values, dtype=float)
    x = np.sort(values)
    y = np.arange(1, len(x) + 1) / len(x)
    return x, y


def clean_axis(ax):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    ax.spines["left"].set_linewidth(0.75)
    ax.spines["bottom"].set_linewidth(0.75)

    ax.tick_params(
        axis="both",
        direction="out",
        length=3.2,
        width=0.7,
        pad=3,
    )

    ax.grid(False)


def add_condition_legend(ax):
    handles = [
        Line2D(
            [0],
            [0],
            color=CONDITION_COLORS["B0"],
            lw=CONDITION_WIDTHS["B0"],
            linestyle="-",
            label="B0",
        ),
        Line2D(
            [0],
            [0],
            color=CONDITION_COLORS["B1"],
            lw=CONDITION_WIDTHS["B1"],
            linestyle="-",
            label="B1",
        ),
        Line2D(
            [0],
            [0],
            color=CONDITION_COLORS["G1"],
            lw=CONDITION_WIDTHS["G1"],
            linestyle="-",
            label="G1",
        ),
    ]

    ax.legend(
        handles=handles,
        frameon=False,
        ncol=3,
        loc="lower right",
        columnspacing=1.2,
        handlelength=2.4,
        handletextpad=0.5,
    )


def stacked_discrete(ax, column, xlabel):
    categories = sorted(
        int(x)
        for x in plot_df[column].unique()
    )

    y_positions = np.arange(len(conditions))
    left = np.zeros(len(conditions))

    for value in categories:

        counts = []
        proportions = []

        for condition in conditions:
            values = plot_df.loc[
                plot_df["condition"] == condition,
                column,
            ]

            count = int((values == value).sum())

            counts.append(count)
            proportions.append(count / 30.0)

        proportions = np.asarray(proportions)

        color = CALL_COLORS.get(
            value,
            "#4D4D4D",
        )

        bars = ax.barh(
            y_positions,
            proportions,
            left=left,
            height=0.56,
            color=color,
            edgecolor="#333333",
            linewidth=0.65,
            label=f"{value} call" + ("" if value == 1 else "s"),
        )

        for j, (bar, proportion, count) in enumerate(
            zip(bars, proportions, counts)
        ):
            if proportion >= 0.10:
                ax.text(
                    left[j] + proportion / 2,
                    bar.get_y() + bar.get_height() / 2,
                    f"{count}/30",
                    ha="center",
                    va="center",
                    fontsize=7.2,
                    color="#111111",
                )

        left += proportions

    ax.set_yticks(
        y_positions,
        conditions,
    )

    ax.invert_yaxis()

    ax.set_xlim(0, 1)

    ax.xaxis.set_major_formatter(
        PercentFormatter(1.0)
    )

    ax.set_xlabel(xlabel)

    clean_axis(ax)

    ax.legend(
        frameon=False,
        ncol=min(len(categories), 3),
        loc="upper center",
        bbox_to_anchor=(0.5, -0.16),
        columnspacing=0.9,
        handlelength=1.7,
        handletextpad=0.40,
    )


# ============================================================
# 5. FIGURE — IEEE FULL TWO-COLUMN WIDTH
# ============================================================

fig, axs = plt.subplots(
    2,
    2,
    figsize=(7.16, 4.55),
)

fig.subplots_adjust(
    left=0.09,
    right=0.985,
    top=0.97,
    bottom=0.115,
    wspace=0.28,
    hspace=0.37,
)

# ============================================================
# (a) TOTAL TOKENS
# ============================================================

ax = axs[0, 0]

for condition in conditions:

    values = plot_df.loc[
        plot_df["condition"] == condition,
        "total_tokens",
    ]

    x, y = ecdf(values)

    ax.step(
        x,
        y,
        where="post",
        color=CONDITION_COLORS[condition],
        linewidth=CONDITION_WIDTHS[condition],
        linestyle="-",
        zorder=2 if condition == "B0" else 3,
    )

ax.set_xlabel("Total tokens per task")
ax.set_ylabel("Cumulative proportion")

ax.set_ylim(0, 1.02)

ax.yaxis.set_major_formatter(
    PercentFormatter(1.0)
)

ax.xaxis.set_major_formatter(
    FuncFormatter(
        lambda x, _:
        f"{x / 1000:.0f}k"
        if abs(x) >= 1000
        else f"{x:.0f}"
    )
)

add_condition_legend(ax)
clean_axis(ax)

# ============================================================
# (b) END-TO-END LATENCY
# ============================================================

ax = axs[0, 1]

for condition in conditions:

    values = plot_df.loc[
        plot_df["condition"] == condition,
        "latency_s",
    ]

    x, y = ecdf(values)

    ax.step(
        x,
        y,
        where="post",
        color=CONDITION_COLORS[condition],
        linewidth=CONDITION_WIDTHS[condition],
        linestyle="-",
        zorder=2 if condition == "B0" else 3,
    )

ax.set_xlabel(
    "Mean end-to-end latency per task (s)"
)

ax.set_ylabel(
    "Cumulative proportion"
)

ax.set_ylim(0, 1.02)

ax.yaxis.set_major_formatter(
    PercentFormatter(1.0)
)

clean_axis(ax)

# No repeated legend in panel b.
# Panel a already defines condition colors.

# ============================================================
# (c) MODEL CALLS
# ============================================================

stacked_discrete(
    axs[1, 0],
    "llm_calls",
    "Share of tasks",
)

# ============================================================
# (d) RETRIEVAL CALLS
# ============================================================

stacked_discrete(
    axs[1, 1],
    "retrieval_calls",
    "Share of tasks",
)

# ============================================================
# 6. PANEL LABELS
# ============================================================

for label, ax in zip(
    ["(a)", "(b)", "(c)", "(d)"],
    axs.flat,
):
    ax.text(
        -0.13,
        1.04,
        label,
        transform=ax.transAxes,
        fontsize=9.0,
        fontweight="bold",
        ha="left",
        va="bottom",
    )

# ============================================================
# 7. SAVE PUBLICATION ARTIFACTS
# ============================================================

pdf = (
    OUT
    / "figures"
    / "figure01_execution_resource_profile_ieee.pdf"
)

svg = (
    OUT
    / "figures"
    / "figure01_execution_resource_profile_ieee.svg"
)

png = (
    OUT
    / "figures"
    / "figure01_execution_resource_profile_ieee.png"
)

fig.savefig(
    pdf,
    format="pdf",
    bbox_inches="tight",
)

fig.savefig(
    svg,
    format="svg",
    bbox_inches="tight",
)

fig.savefig(
    png,
    format="png",
    dpi=600,
    bbox_inches="tight",
)

plt.close(fig)

# ============================================================
# 8. NUMERIC COMPANION SUMMARY
# ============================================================

summary = (
    plot_df
    .groupby("condition")
    .agg(
        n_tasks=("task_id", "count"),
        mean_tokens=("total_tokens", "mean"),
        median_tokens=("total_tokens", "median"),
        mean_latency_s=("latency_s", "mean"),
        median_latency_s=("latency_s", "median"),
        mean_llm_calls=("llm_calls", "mean"),
        mean_retrieval_calls=("retrieval_calls", "mean"),
    )
)

summary.to_csv(
    OUT / "data/figure01_summary.csv"
)

print("FIGURE01_SOURCE_ROWS=" + str(len(plot_df)))
print(
    "TASKS_PER_CONDITION="
    + str(
        plot_df
        .groupby("condition")
        .size()
        .to_dict()
    )
)

print("FONT=" + font)
print("LINES_ALL_SOLID=YES")
print("B0_COLOR=" + CONDITION_COLORS["B0"])
print("B1_COLOR=" + CONDITION_COLORS["B1"])
print("G1_COLOR=" + CONDITION_COLORS["G1"])

print("PDF=" + str(pdf))
print("SVG=" + str(svg))
print("PNG=" + str(png))

print(
    "SOURCE_DATA="
    + str(
        OUT
        / "data/figure01_source_data.csv"
    )
)

print(
    "SOURCE_SCRIPT="
    + str(Path(__file__).resolve())
)

print("FIGURE01_IEEE_V3=PASS")
