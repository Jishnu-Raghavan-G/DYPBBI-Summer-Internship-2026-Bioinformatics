"""
Expression Matrix Analysis
---------------------------

Purpose:
    Basic exploration of a gene-expression matrix.

This script demonstrates simple operations that are commonly
performed before downstream transcriptomic analysis.

Input:
    A CSV file containing genes in rows and samples in columns.

Example structure:

Gene,Healthy_1,Healthy_2,Asthma_1,Asthma_2
GeneA,5.1,5.3,7.8,8.0
GeneB,6.2,6.4,6.1,6.3
GeneC,3.0,3.2,5.6,5.8

The script:
    1. Loads the expression matrix
    2. Examines its dimensions
    3. Checks for missing values
    4. Calculates basic statistics
    5. Separates sample groups
    6. Calculates group-wise mean expression
"""

import pandas as pd


# ---------------------------------------------------------
# 1. Load the expression matrix
# ---------------------------------------------------------

file_path = "expression_matrix.csv"

data = pd.read_csv(file_path)

print("Expression Matrix:")
print(data.head())


# ---------------------------------------------------------
# 2. Inspect the dataset
# ---------------------------------------------------------

print("\nDataset shape:")
print(data.shape)

print("\nColumn names:")
print(data.columns.tolist())

print("\nData types:")
print(data.dtypes)


# ---------------------------------------------------------
# 3. Check for missing values
# ---------------------------------------------------------

print("\nMissing values:")
print(data.isnull().sum())


# ---------------------------------------------------------
# 4. Basic statistics
# ---------------------------------------------------------

# Select only numerical expression columns.
expression_data = data.select_dtypes(include="number")

print("\nBasic statistics:")
print(expression_data.describe())


# ---------------------------------------------------------
# 5. Calculate mean expression for each gene
# ---------------------------------------------------------

data["Mean_Expression"] = expression_data.mean(axis=1)

print("\nMean expression:")
print(data[["Gene", "Mean_Expression"]].head())


# ---------------------------------------------------------
# 6. Separate sample groups
# ---------------------------------------------------------

healthy_columns = [
    "Healthy_1",
    "Healthy_2"
]

asthma_columns = [
    "Asthma_1",
    "Asthma_2"
]


# ---------------------------------------------------------
# 7. Calculate average expression for each group
# ---------------------------------------------------------

data["Healthy_Mean"] = data[healthy_columns].mean(axis=1)

data["Asthma_Mean"] = data[asthma_columns].mean(axis=1)


# ---------------------------------------------------------
# 8. Calculate fold change
# ---------------------------------------------------------

# A small value is added to avoid division by zero.

epsilon = 1e-9

data["Fold_Change"] = (
    (data["Asthma_Mean"] + epsilon)
    / (data["Healthy_Mean"] + epsilon)
)


# ---------------------------------------------------------
# 9. Display the results
# ---------------------------------------------------------

results = data[
    [
        "Gene",
        "Healthy_Mean",
        "Asthma_Mean",
        "Fold_Change"
    ]
]

print("\nGroup comparison:")
print(results.head())


# ---------------------------------------------------------
# 10. Save the processed results
# ---------------------------------------------------------

results.to_csv(
    "expression_matrix_summary.csv",
    index=False
)

print("\nAnalysis completed.")
print("Results saved as expression_matrix_summary.csv")
What This Code Demonstrates

This is a basic educational expression-matrix script, not a replacement for a complete differential-expression pipeline.

It demonstrates how Python can be used to:

Expression Matrix
       ↓
Load Data
       ↓
Inspect Data
       ↓
Check Missing Values
       ↓
Calculate Mean Expression
       ↓
Compare Groups
       ↓
Calculate Fold Change
       ↓
Save Results

The internship involved gene-expression analysis, differential gene expression, log2 fold change, adjusted p-values, and statistical filtering.

For the actual GSE43696 case study, GEO2R was used for the differential-expression analysis rather than claiming that this simple Python script reproduced the GEO2R statistical pipeline.
