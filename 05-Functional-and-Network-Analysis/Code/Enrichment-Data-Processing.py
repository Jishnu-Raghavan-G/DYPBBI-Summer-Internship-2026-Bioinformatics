"""
Enrichment Data Processing

Purpose:
    Clean and prepare functional-enrichment results for
    downstream analysis and visualization.

Typical workflow:

    Gene List
        ↓
    GO / KEGG / g:Profiler
        ↓
    Enrichment Results
        ↓
    Clean Results
        ↓
    Filter Significant Terms
        ↓
    Sort Results
        ↓
    Export Processed Table

This is a reusable example script. Column names may need
to be changed depending on the enrichment tool and the
format of the downloaded results.
"""

import pandas as pd


# ---------------------------------------------------------
# 1. Load enrichment results
# ---------------------------------------------------------

input_file = "enrichment_results.csv"

df = pd.read_csv(input_file)

print("Enrichment dataset loaded successfully.")
print(f"Number of results: {len(df)}")


# ---------------------------------------------------------
# 2. Inspect available columns
# ---------------------------------------------------------

print("\nAvailable columns:")
print(df.columns.tolist())


# ---------------------------------------------------------
# 3. Define important columns
# ---------------------------------------------------------
# Change these names if your downloaded file uses different
# column names.

term_column = "Term"
pvalue_column = "p_value"
adjusted_pvalue_column = "adjusted_p_value"


# ---------------------------------------------------------
# 4. Remove rows without term names
# ---------------------------------------------------------

df = df.dropna(subset=[term_column])


# ---------------------------------------------------------
# 5. Convert statistical columns to numeric
# ---------------------------------------------------------

df[pvalue_column] = pd.to_numeric(
    df[pvalue_column],
    errors="coerce"
)

df[adjusted_pvalue_column] = pd.to_numeric(
    df[adjusted_pvalue_column],
    errors="coerce"
)


# ---------------------------------------------------------
# 6. Remove rows with missing statistical values
# ---------------------------------------------------------

df = df.dropna(
    subset=[
        pvalue_column,
        adjusted_pvalue_column
    ]
)


# ---------------------------------------------------------
# 7. Define significance threshold
# ---------------------------------------------------------

adjusted_pvalue_cutoff = 0.05


# ---------------------------------------------------------
# 8. Filter significant enrichment results
# ---------------------------------------------------------

significant_results = df[
    df[adjusted_pvalue_column]
    < adjusted_pvalue_cutoff
].copy()


# ---------------------------------------------------------
# 9. Sort by adjusted p-value
# ---------------------------------------------------------

significant_results = significant_results.sort_values(
    by=adjusted_pvalue_column,
    ascending=True
)


# ---------------------------------------------------------
# 10. Remove duplicate terms
# ---------------------------------------------------------

significant_results = (
    significant_results
    .drop_duplicates(subset=[term_column])
)


# ---------------------------------------------------------
# 11. Display summary
# ---------------------------------------------------------

print("\nEnrichment analysis summary:")

print(
    f"Total terms analysed: "
    f"{len(df)}"
)

print(
    f"Significant terms: "
    f"{len(significant_results)}"
)

print(
    f"Adjusted p-value cutoff: "
    f"{adjusted_pvalue_cutoff}"
)


# ---------------------------------------------------------
# 12. Display top results
# ---------------------------------------------------------

print("\nTop enriched terms:")

print(
    significant_results[
        [
            term_column,
            pvalue_column,
            adjusted_pvalue_column
        ]
    ]
    .head(10)
    .to_string(index=False)
)


# ---------------------------------------------------------
# 13. Save all processed results
# ---------------------------------------------------------

significant_results.to_csv(
    "significant_enrichment_results.csv",
    index=False
)


print(
    "\nSaved: "
    "significant_enrichment_results.csv"
)


# ---------------------------------------------------------
# 14. Optional: create a compact results table
# ---------------------------------------------------------

columns_to_keep = [
    term_column,
    pvalue_column,
    adjusted_pvalue_column
]

# Keep only columns that actually exist in the dataset.
available_columns = [
    column
    for column in columns_to_keep
    if column in significant_results.columns
]

compact_results = significant_results[
    available_columns
]


compact_results.to_csv(
    "enrichment_summary.csv",
    index=False
)


print("Saved: enrichment_summary.csv")


# ---------------------------------------------------------
# 15. Optional gene-count processing
# ---------------------------------------------------------
# Some enrichment-result files contain a column describing
# the number of genes associated with each term.

possible_gene_count_columns = [
    "GeneCount",
    "gene_count",
    "Count",
    "count"
]

gene_count_column = None

for column in possible_gene_count_columns:
    if column in significant_results.columns:
        gene_count_column = column
        break


if gene_count_column is not None:

    significant_results[gene_count_column] = pd.to_numeric(
        significant_results[gene_count_column],
        errors="coerce"
    )

    significant_results = significant_results.sort_values(
        by=gene_count_column,
        ascending=False
    )

    significant_results.to_csv(
        "enrichment_by_gene_count.csv",
        index=False
    )

    print(
        "Saved: enrichment_by_gene_count.csv"
    )


# ---------------------------------------------------------
# 16. Final message
# ---------------------------------------------------------

print("\nProcessing completed successfully.")

print(
    """
The processed enrichment table can now be used for:

- Biological interpretation
- GO analysis
- KEGG pathway interpretation
- Result tables
- Enrichment plots
- Downstream reporting
"""
)
What this script is doing

The purpose is to turn a raw enrichment-results table into something easier to interpret:

GO / KEGG / g:Profiler Results
            ↓
       Load Results
            ↓
       Clean Data
            ↓
   Remove Missing Values
            ↓
   Adjusted P-value Filter
            ↓
      Sort Results
            ↓
    Significant Terms
            ↓
     Export CSV Table

The internship specifically covered GO, KEGG and g:Profiler as functional-analysis resources after the differential-expression stage.

Important note for the repository

This code is deliberately written as a general reusable processing script. It should not be presented as though you personally used this exact Python script to generate your internship's g:Profiler/GO/KEGG results. Your documented internship workflow used these resources for downstream interpretation of selected genes from the GSE43696 analysis
