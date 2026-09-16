"""
Heatmap-and-Volcano-Plot.py

Purpose:
    Create simple visualizations for gene-expression results.

    1. Heatmap
       Shows expression patterns across samples.

    2. Volcano plot
       Shows the relationship between fold change
       and statistical significance.

Note:
    This is an educational visualization script.
    The actual statistical results from GEO2R/GSE43696
    should be used when available.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ---------------------------------------------------------
# 1. Load expression data
# ---------------------------------------------------------

expression_file = "expression_matrix.csv"

expression_data = pd.read_csv(expression_file)

print("Expression data loaded.")
print(expression_data.head())


# ---------------------------------------------------------
# 2. Select sample columns
# ---------------------------------------------------------

sample_columns = [
    "Healthy_1",
    "Healthy_2",
    "Asthma_1",
    "Asthma_2"
]

# Check that the required columns exist

missing_columns = [
    column
    for column in sample_columns
    if column not in expression_data.columns
]

if missing_columns:
    print("\nMissing columns:")
    print(missing_columns)

    print(
        "\nPlease change sample_columns so that they "
        "match your expression matrix."
    )

    raise SystemExit


# ---------------------------------------------------------
# 3. Prepare data for visualization
# ---------------------------------------------------------

# Use the gene column as the index.

expression_matrix = expression_data.set_index("Gene")

expression_matrix = expression_matrix[sample_columns]


# ---------------------------------------------------------
# 4. Select the most variable genes
# ---------------------------------------------------------

# Calculating variance helps identify genes whose
# expression changes more strongly across samples.

gene_variance = expression_matrix.var(axis=1)

top_genes = gene_variance.sort_values(
    ascending=False
).head(30).index

heatmap_data = expression_matrix.loc[top_genes]


# ---------------------------------------------------------
# 5. Standardize each gene
# ---------------------------------------------------------

# Z-score normalization:
#
# z = (value - mean) / standard deviation
#
# This makes expression patterns easier to compare.

heatmap_zscore = heatmap_data.sub(
    heatmap_data.mean(axis=1),
    axis=0
)

heatmap_zscore = heatmap_zscore.div(
    heatmap_data.std(axis=1),
    axis=0
)


# ---------------------------------------------------------
# 6. Create heatmap
# ---------------------------------------------------------

plt.figure(figsize=(10, 8))

plt.imshow(
    heatmap_zscore,
    aspect="auto",
    interpolation="nearest"
)

plt.colorbar(label="Z-score")

plt.xticks(
    range(len(sample_columns)),
    sample_columns,
    rotation=45
)

plt.yticks(
    range(len(heatmap_zscore.index)),
    heatmap_zscore.index
)

plt.xlabel("Samples")
plt.ylabel("Genes")

plt.title("Gene Expression Heatmap")

plt.tight_layout()

plt.savefig(
    "gene_expression_heatmap.png",
    dpi=300
)

plt.show()


# ---------------------------------------------------------
# 7. Load differential-expression results
# ---------------------------------------------------------

deg_file = "differential_expression_results.csv"

deg_data = pd.read_csv(deg_file)

print("\nDifferential-expression results:")
print(deg_data.head())


# ---------------------------------------------------------
# 8. Check required columns
# ---------------------------------------------------------

required_deg_columns = [
    "Gene",
    "log2FC",
    "p_value"
]

missing_deg_columns = [
    column
    for column in required_deg_columns
    if column not in deg_data.columns
]

if missing_deg_columns:
    print("\nThe following columns are missing:")
    print(missing_deg_columns)

    print(
        "\nThe volcano plot requires log2FC and "
        "p_value columns."
    )

    raise SystemExit


# ---------------------------------------------------------
# 9. Prepare data for volcano plot
# ---------------------------------------------------------

# Remove rows with missing values.

volcano_data = deg_data.dropna(
    subset=["log2FC", "p_value"]
).copy()


# Avoid log10(0)

volcano_data["p_value"] = volcano_data["p_value"].clip(
    lower=1e-300
)


# Calculate -log10(p-value)

volcano_data["minus_log10_p"] = -np.log10(
    volcano_data["p_value"]
)


# ---------------------------------------------------------
# 10. Define example thresholds
# ---------------------------------------------------------

log2fc_threshold = 1

p_value_threshold = 0.05


# Identify significant genes

significant_genes = volcano_data[
    (
        volcano_data["p_value"]
        < p_value_threshold
    )
    &
    (
        abs(volcano_data["log2FC"])
        >= log2fc_threshold
    )
]


print("\nNumber of genes passing the example thresholds:")

print(len(significant_genes))


# ---------------------------------------------------------
# 11. Create volcano plot
# ---------------------------------------------------------

plt.figure(figsize=(10, 7))

plt.scatter(
    volcano_data["log2FC"],
    volcano_data["minus_log10_p"],
    alpha=0.6,
    s=20
)


# Draw threshold lines

plt.axvline(
    x=log2fc_threshold,
    linestyle="--"
)

plt.axvline(
    x=-log2fc_threshold,
    linestyle="--"
)

plt.axhline(
    y=-np.log10(p_value_threshold),
    linestyle="--"
)


plt.xlabel("log2 Fold Change")

plt.ylabel("-log10(p-value)")

plt.title("Volcano Plot")

plt.tight_layout()


plt.savefig(
    "volcano_plot.png",
    dpi=300
)

plt.show()


# ---------------------------------------------------------
# 12. Save significant genes
# ---------------------------------------------------------

significant_genes.to_csv(
    "significant_genes.csv",
    index=False
)


print("\nVisualization completed.")

print("Files generated:")
print("- gene_expression_heatmap.png")
print("- volcano_plot.png")
print("- significant_genes.csv")
What the visualizations show
Heatmap

A heatmap is used to visually compare gene-expression patterns across samples.

Genes
  ↓
Expression values
  ↓
Standardization
  ↓
Heatmap
  ↓
Identify expression patterns

Genes with similar expression patterns across samples can appear together, helping reveal patterns associated with different biological conditions.

Volcano plot

A volcano plot combines two important aspects of differential expression:

X-axis: log2FC
Y-axis: -log10(p-value)

So genes farther to the left or right have larger expression differences, while genes higher on the plot have smaller p-values.

The script uses example thresholds:

|log2FC| ≥ 1
p-value < 0.05

These are illustrative thresholds, not a claim about the exact thresholds used in your GSE43696 GEO2R analysis. Your internship workflow specifically involved differential-expression analysis followed by statistical filtering and downstream functional/network analysis.

One important correction for the final repository

The previous Differential-Expression-Analysis.py script calculated log2FC but did not generate a p_value column. Therefore, this visualization script assumes a differential-expression results file containing statistical results from an appropriate analysis.
