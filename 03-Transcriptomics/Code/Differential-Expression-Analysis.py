"""
Differential-Expression-Analysis.py

Purpose:
    Basic educational workflow for comparing gene expression
    between two biological groups.

Example groups:
    Healthy vs Asthma

Note:
    This script demonstrates the logic behind differential
    expression analysis using an expression matrix.

    It is NOT a reproduction of the GEO2R statistical pipeline
    used for GSE43696.
"""

import pandas as pd
import numpy as np


# ---------------------------------------------------------
# 1. Load the expression matrix
# ---------------------------------------------------------

file_name = "expression_matrix.csv"

data = pd.read_csv(file_name)

print("Expression Matrix:")
print(data.head())

print("\nShape of dataset:")
print(data.shape)


# ---------------------------------------------------------
# 2. Identify sample groups
# ---------------------------------------------------------

healthy_samples = [
    "Healthy_1",
    "Healthy_2"
]

asthma_samples = [
    "Asthma_1",
    "Asthma_2"
]


# Check whether all required columns are present

required_columns = healthy_samples + asthma_samples

missing_columns = [
    column for column in required_columns
    if column not in data.columns
]

if missing_columns:
    print("\nMissing sample columns:")
    print(missing_columns)

    print(
        "\nPlease change the sample names in the script "
        "to match your expression matrix."
    )

    raise SystemExit


# ---------------------------------------------------------
# 3. Calculate mean expression for each group
# ---------------------------------------------------------

data["Healthy_Mean"] = data[healthy_samples].mean(axis=1)

data["Asthma_Mean"] = data[asthma_samples].mean(axis=1)


# ---------------------------------------------------------
# 4. Calculate fold change
# ---------------------------------------------------------

# A small value prevents division by zero.

small_value = 1e-9

data["Fold_Change"] = (
    (data["Asthma_Mean"] + small_value)
    /
    (data["Healthy_Mean"] + small_value)
)


# ---------------------------------------------------------
# 5. Calculate log2 fold change
# ---------------------------------------------------------

data["log2FC"] = np.log2(data["Fold_Change"])


# ---------------------------------------------------------
# 6. Identify upregulated and downregulated genes
# ---------------------------------------------------------

# Example threshold:
# log2FC >= 1  → approximately 2-fold higher expression
# log2FC <= -1 → approximately 2-fold lower expression

upregulated = data[data["log2FC"] >= 1]

downregulated = data[data["log2FC"] <= -1]


print("\nNumber of upregulated genes:")
print(len(upregulated))

print("\nNumber of downregulated genes:")
print(len(downregulated))


# ---------------------------------------------------------
# 7. Display selected genes
# ---------------------------------------------------------

print("\nUpregulated genes:")

print(
    upregulated[
        ["Gene", "Healthy_Mean", "Asthma_Mean", "log2FC"]
    ].head(20)
)


print("\nDownregulated genes:")

print(
    downregulated[
        ["Gene", "Healthy_Mean", "Asthma_Mean", "log2FC"]
    ].head(20)
)


# ---------------------------------------------------------
# 8. Sort genes by log2 fold change
# ---------------------------------------------------------

sorted_genes = data.sort_values(
    by="log2FC",
    ascending=False
)


print("\nGenes with highest positive log2FC:")

print(
    sorted_genes[
        ["Gene", "Healthy_Mean", "Asthma_Mean", "log2FC"]
    ].head(10)
)


print("\nGenes with lowest log2FC:")

print(
    sorted_genes[
        ["Gene", "Healthy_Mean", "Asthma_Mean", "log2FC"]
    ].tail(10)
)


# ---------------------------------------------------------
# 9. Save the results
# ---------------------------------------------------------

data.to_csv(
    "differential_expression_results.csv",
    index=False
)

upregulated.to_csv(
    "upregulated_genes.csv",
    index=False
)

downregulated.to_csv(
    "downregulated_genes.csv",
    index=False
)


print("\nAnalysis completed.")

print("Files generated:")
print("- differential_expression_results.csv")
print("- upregulated_genes.csv")
print("- downregulated_genes.csv")
What this code demonstrates

This script follows the basic idea of differential gene-expression analysis:

Expression Matrix
       ↓
Separate samples into groups
       ↓
Calculate group-wise expression
       ↓
Calculate Fold Change
       ↓
Calculate log2 Fold Change
       ↓
Identify potentially upregulated/
downregulated genes
       ↓
Save results
Important concept

For two groups:

Fold Change = Asthma expression / Healthy expression

Then:

log2FC = log2(Fold Change)

So:

log2FC	Interpretation
+1	~2× higher
+2	~4× higher
0	No fold difference
-1	~2× lower
-2	~4× lower
