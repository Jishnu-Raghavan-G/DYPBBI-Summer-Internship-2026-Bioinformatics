"""
Gene List Preparation

Purpose:
    Prepare a clean gene list for downstream functional and
    network analysis.

Typical workflow:
    Differential Expression Results
            ↓
       Filter genes
            ↓
      Clean gene names
            ↓
       Remove duplicates
            ↓
      Save final gene list
            ↓
     GO / KEGG / g:Profiler / STRING

This script is written as a simple example and can be
adapted to the actual format of a differential-expression
results file.
"""

import pandas as pd


# ---------------------------------------------------------
# 1. Load differential-expression results
# ---------------------------------------------------------

input_file = "differential_expression_results.csv"

df = pd.read_csv(input_file)

print("Dataset loaded successfully.")
print(f"Number of rows: {len(df)}")


# ---------------------------------------------------------
# 2. Inspect the available columns
# ---------------------------------------------------------

print("\nAvailable columns:")
print(df.columns.tolist())


# ---------------------------------------------------------
# 3. Define the important columns
# ---------------------------------------------------------
# Change these names if your input file uses different
# column names.

gene_column = "Gene"
log2fc_column = "log2FC"
padj_column = "adjusted_p_value"


# ---------------------------------------------------------
# 4. Remove rows with missing gene information
# ---------------------------------------------------------

df = df.dropna(subset=[gene_column])

print(f"\nRows after removing missing genes: {len(df)}")


# ---------------------------------------------------------
# 5. Remove duplicate genes
# ---------------------------------------------------------
# A gene should normally occur only once in the final
# gene list used for downstream analysis.

df = df.drop_duplicates(subset=[gene_column])


# ---------------------------------------------------------
# 6. Convert numerical columns
# ---------------------------------------------------------

df[log2fc_column] = pd.to_numeric(
    df[log2fc_column],
    errors="coerce"
)

df[padj_column] = pd.to_numeric(
    df[padj_column],
    errors="coerce"
)


# ---------------------------------------------------------
# 7. Remove rows with missing statistical values
# ---------------------------------------------------------

df = df.dropna(
    subset=[log2fc_column, padj_column]
)


# ---------------------------------------------------------
# 8. Define filtering criteria
# ---------------------------------------------------------

adjusted_pvalue_cutoff = 0.05
log2fc_cutoff = 1.0


# ---------------------------------------------------------
# 9. Filter significantly differentially expressed genes
# ---------------------------------------------------------

filtered_df = df[
    (df[padj_column] < adjusted_pvalue_cutoff)
    &
    (df[log2fc_column].abs() >= log2fc_cutoff)
].copy()


# ---------------------------------------------------------
# 10. Sort genes by adjusted p-value
# ---------------------------------------------------------

filtered_df = filtered_df.sort_values(
    by=padj_column
)


# ---------------------------------------------------------
# 11. Extract the final gene list
# ---------------------------------------------------------

gene_list = filtered_df[gene_column].drop_duplicates()


# ---------------------------------------------------------
# 12. Save the complete filtered table
# ---------------------------------------------------------

filtered_df.to_csv(
    "filtered_DEGs.csv",
    index=False
)


# ---------------------------------------------------------
# 13. Save only the gene names
# ---------------------------------------------------------

gene_list.to_csv(
    "gene_list.txt",
    index=False,
    header=False
)


# ---------------------------------------------------------
# 14. Display summary
# ---------------------------------------------------------

print("\nFiltering completed.")

print(
    f"Adjusted p-value cutoff: "
    f"{adjusted_pvalue_cutoff}"
)

print(
    f"Absolute log2FC cutoff: "
    f"{log2fc_cutoff}"
)

print(
    f"Number of selected genes: "
    f"{len(gene_list)}"
)


# ---------------------------------------------------------
# 15. Display the first few genes
# ---------------------------------------------------------

print("\nFirst few genes:")

print(
    gene_list.head(10).to_string(index=False)
)


# ---------------------------------------------------------
# 16. Separate upregulated and downregulated genes
# ---------------------------------------------------------

upregulated = filtered_df[
    filtered_df[log2fc_column] >= log2fc_cutoff
]

downregulated = filtered_df[
    filtered_df[log2fc_column] <= -log2fc_cutoff
]


print(
    f"\nUpregulated genes: "
    f"{len(upregulated)}"
)

print(
    f"Downregulated genes: "
    f"{len(downregulated)}"
)


# ---------------------------------------------------------
# 17. Save separate gene lists
# ---------------------------------------------------------

upregulated[gene_column].drop_duplicates().to_csv(
    "upregulated_genes.txt",
    index=False,
    header=False
)

downregulated[gene_column].drop_duplicates().to_csv(
    "downregulated_genes.txt",
    index=False,
    header=False
)


print("\nFiles generated:")
print("- filtered_DEGs.csv")
print("- gene_list.txt")
print("- upregulated_genes.txt")
print("- downregulated_genes.txt")
What this code does

The script takes a differential-expression results table and prepares a clean gene list for the next stages of analysis:

DEG Results
    ↓
Remove missing values
    ↓
Remove duplicate genes
    ↓
Apply adjusted p-value cutoff
    ↓
Apply log2FC cutoff
    ↓
Final DEG list
    ↓
GO / KEGG / g:Profiler
    ↓
STRING

The filtering step uses adjusted p-value and absolute log2FC, concepts that were part of the transcriptomics workflow in the internship.

One important point for the repository: this is a reusable analysis script, not a claim that this exact Python filtering workflow was used to generate the original GSE43696 results. Your documented practical workflow used GEO2R for the differential-expression stage.
