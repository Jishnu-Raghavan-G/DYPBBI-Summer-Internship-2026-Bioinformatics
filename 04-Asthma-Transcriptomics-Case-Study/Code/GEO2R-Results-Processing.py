"""
GEO2R-Results-Processing.py

Purpose:
    Basic processing and inspection of GEO2R results.

    This script is designed to help organize a GEO2R
    result table before downstream DEG filtering.

Note:
    GEO2R performs the statistical analysis. This script
    only helps inspect, clean and organize the exported
    results.
"""

import pandas as pd


# ---------------------------------------------------------
# 1. Load GEO2R results
# ---------------------------------------------------------

input_file = "GEO2R_results.csv"

data = pd.read_csv(input_file)

print("GEO2R results loaded successfully.")

print("\nFirst five rows:")
print(data.head())


# ---------------------------------------------------------
# 2. Inspect the dataset
# ---------------------------------------------------------

print("\nDataset shape:")
print(data.shape)

print("\nColumn names:")
print(data.columns.tolist())

print("\nMissing values:")
print(data.isnull().sum())


# ---------------------------------------------------------
# 3. Display basic information
# ---------------------------------------------------------

print("\nData types:")
print(data.dtypes)


# ---------------------------------------------------------
# 4. Remove completely empty rows
# ---------------------------------------------------------

data = data.dropna(
    how="all"
)

print("\nShape after removing empty rows:")
print(data.shape)


# ---------------------------------------------------------
# 5. Remove duplicate rows
# ---------------------------------------------------------

data = data.drop_duplicates()

print("\nShape after removing duplicate rows:")
print(data.shape)


# ---------------------------------------------------------
# 6. Convert numerical columns
# ---------------------------------------------------------

# Change these names if the exported GEO2R file
# uses different column names.

numeric_columns = [
    "log2FC",
    "p_value",
    "adjusted_p_value"
]

for column in numeric_columns:

    if column in data.columns:

        data[column] = pd.to_numeric(
            data[column],
            errors="coerce"
        )


# ---------------------------------------------------------
# 7. Check numerical information
# ---------------------------------------------------------

print("\nNumerical summary:")

print(
    data[
        [
            column
            for column in numeric_columns
            if column in data.columns
        ]
    ].describe()
)


# ---------------------------------------------------------
# 8. Sort results
# ---------------------------------------------------------

if "adjusted_p_value" in data.columns:

    data = data.sort_values(
        by="adjusted_p_value",
        ascending=True
    )

elif "p_value" in data.columns:

    data = data.sort_values(
        by="p_value",
        ascending=True
    )


# ---------------------------------------------------------
# 9. Display top results
# ---------------------------------------------------------

print("\nTop results:")

print(
    data.head(20)
)


# ---------------------------------------------------------
# 10. Save cleaned results
# ---------------------------------------------------------

output_file = "GEO2R_results_cleaned.csv"

data.to_csv(
    output_file,
    index=False
)

print(
    f"\nCleaned results saved as: {output_file}"
)


# ---------------------------------------------------------
# 11. Basic summary
# ---------------------------------------------------------

print("\nProcessing completed.")

print(
    "The cleaned GEO2R results can now be used "
    "for further DEG filtering."
)
What This Script Does

The script is intentionally simple. It does not perform the GEO2R statistical analysis itself.

Instead, the workflow is:

GEO2R
  ↓
Export results
  ↓
Load CSV
  ↓
Inspect data
  ↓
Check missing values
  ↓
Remove empty/duplicate rows
  ↓
Convert numerical columns
  ↓
Sort results
  ↓
Save cleaned table
  ↓
DEG filtering
Why Process GEO2R Results?

GEO2R can produce a large results table. Before selecting genes for downstream analysis, it is useful to inspect the exported data and make sure that:

The expected columns are present
Numerical values are actually stored as numbers
Empty rows are removed
Duplicate entries are identified
Results can be sorted according to statistical measures

The internship workflow involved obtaining differential-expression results from the asthma dataset and then applying statistical filtering before downstream functional and network analysis.

Important Column Names

The script assumes columns such as:

log2FC
p_value
adjusted_p_value

However, exported GEO2R files may use different names or formats.

Therefore, the column names should be changed to match the actual exported GSE43696 results.

Do not create artificial p-values or adjusted p-values just to make the script run.

Connection to the Case Study

This script sits between the GEO2R analysis and DEG filtering:

GSE43696
   ↓
GEO2R
   ↓
Exported Results
   ↓
GEO2R-Results-Processing.py
   ↓
DEG-Filtering.py
   ↓
Selected DEGs
   ↓
Functional + Network Analysis

This follows the internship's documented workflow of using GSE43696 for the healthy-versus-asthma comparison, followed by differential-expression analysis, statistical filtering and downstream analysis.
