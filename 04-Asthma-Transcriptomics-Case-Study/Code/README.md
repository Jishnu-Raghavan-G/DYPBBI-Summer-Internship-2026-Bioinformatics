Overview

This folder contains the supporting Python scripts used to organize and process results from the GSE43696 asthma transcriptomics case study.

The scripts are designed to support the workflow after obtaining results from GEO2R. They focus on data organization and filtering rather than replacing the statistical analysis performed by GEO2R.

Files
GEO2R-Results-Processing.py

This script processes an exported GEO2R results table.

It demonstrates how to:

Load GEO2R results using Pandas
Inspect the dataset
Check column names
Identify missing values
Remove completely empty rows
Remove duplicate rows
Convert statistical columns into numerical format
Sort the results
Save a cleaned results table

The output is:

GEO2R_results_cleaned.csv

The script is intended to make the exported results easier to work with before DEG filtering.

DEG-Filtering.py

This script takes the processed GEO2R results and applies differential-expression filtering.

The demonstrated workflow is:

GEO2R Results
      ↓
Adjusted p-value filtering
      ↓
log2FC filtering
      ↓
Selected DEGs
      ↓
 ┌────┴─────┐
 ↓          ↓
Upregulated  Downregulated

The script produces:

selected_DEGs.csv
upregulated_DEGs.csv
downregulated_DEGs.csv

The filtering thresholds in the script are examples. For the final GSE43696 case study, the actual criteria used during the internship should be documented and applied.

Overall Coding Workflow
GSE43696
   ↓
GEO2R
   ↓
Export Results
   ↓
GEO2R-Results-Processing.py
   ↓
Clean Results
   ↓
DEG-Filtering.py
   ↓
Selected DEG List
   ↓
Functional Enrichment
   ↓
PPI Network Analysis
   ↓
Hub-Gene Analysis

This follows the documented internship workflow in which the GSE43696 healthy-versus-asthma comparison was followed by differential-expression analysis, statistical filtering and downstream functional/network analysis.

Relationship With Other Repository Sections

The case-study code should be understood alongside the conceptual material in:

03-Transcriptomics/

and the downstream analyses in:

05-Functional-and-Network-Analysis/

The separation is intentional:

03-Transcriptomics
      ↓
General concepts + learning code

04-Asthma-Transcriptomics-Case-Study
      ↓
Disease-specific application

05-Functional-and-Network-Analysis
      ↓
General enrichment + network methods
Scientific Reproducibility

The scripts should be used with actual exported GSE43696 results when reproducing the case study.

In particular, the repository should preserve:

The GEO accession
Sample-group definitions
GEO2R output
Filtering criteria
Selected DEG list
Downstream analysis outputs

The internship documentation describes the use of GSE43696, GEO2R, differential-expression analysis and statistical filtering as part of the practical asthma transcriptomics component.

Important Limitation

These scripts are supporting data-processing scripts.

They do not independently reproduce the complete statistical methodology of GEO2R.

They also should not be used to create or fabricate missing biological results.

For example:

Actual GEO2R p-values
        ✓

Actual adjusted p-values
        ✓

Actual log2FC values
        ✓

Invented statistical values
        ✗
Learning Outcome

These scripts helped me understand how computational processing fits around a transcriptomics analysis:

Raw/Exported Results
        ↓
Data Inspection
        ↓
Data Cleaning
        ↓
Statistical Filtering
        ↓
DEG Selection
        ↓
Biological Analysis

This completed the coding component of the GSE43696 asthma transcriptomics case study.
