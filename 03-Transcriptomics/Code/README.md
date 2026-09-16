Overview

This folder contains Python scripts used to understand and process gene-expression data during the transcriptomics section of the bioinformatics internship.

The scripts focus on three basic tasks:

Inspecting an expression matrix
Performing basic differential-expression calculations
Visualizing expression patterns using heatmaps and volcano plots

The internship covered transcriptomics, gene expression, RNA-seq and microarray concepts, differential gene expression, log2 fold change, adjusted p-values, and statistical filtering.

Files
Expression-Matrix-Analysis.py

This script introduces the basic structure of an expression matrix.

It demonstrates how to:

Load expression data using Pandas
Inspect rows and columns
Check data types
Identify missing values
Calculate descriptive statistics
Calculate average expression
Compare average expression between two groups
Calculate a basic fold change

The script is mainly intended for learning how expression data can be handled programmatically.

Differential-Expression-Analysis.py

This script demonstrates the basic mathematical idea behind differential-expression analysis.

It calculates:

Mean expression for each group
Fold change
log2 fold change
Potentially upregulated genes
Potentially downregulated genes

The script uses example thresholds to demonstrate filtering.

A proper differential-expression workflow also considers statistical significance and multiple-testing correction. The internship workflow included statistical filtering before downstream analysis.

Heatmap-and-Volcano-Plot.py

This script demonstrates two commonly used visualizations.

Heatmap

Used to visualize expression patterns across genes and samples.

Volcano plot

Used to visualize the relationship between:

log2 Fold Change
        +
Statistical significance

The script demonstrates how expression patterns and differential-expression results can be converted into visual representations.

Example Workflow
Expression Matrix
       ↓
Expression-Matrix-Analysis.py
       ↓
Inspect and understand the data
       ↓
Differential-Expression-Analysis.py
       ↓
Calculate basic fold changes
       ↓
Heatmap-and-Volcano-Plot.py
       ↓
Visualize expression patterns
Relationship to the Internship

The coding exercises in this folder are intended to reinforce the concepts learned during the internship rather than claim to reproduce every step of the original analysis.

The main practical transcriptomics case study involved GSE43696, where gene-expression data were examined using GEO/GEO2R for a healthy-versus-asthma comparison, followed by differential-expression analysis and downstream functional and network analysis.

Important Note

The Python scripts use simplified example input files and sample names.

They should not be treated as a replacement for the statistical analysis performed by GEO2R or other dedicated differential-expression tools.

For the actual asthma case study, the repository should contain the genuine analysis outputs and documented parameters rather than simulated or invented results.

Requirements

The scripts primarily use:

Python
Pandas
NumPy
Matplotlib

Install the required packages with:

pip install pandas numpy matplotlib
Learning Outcome

Through these scripts, I learned how computational tools can support transcriptomics analysis—from inspecting biological datasets to comparing gene-expression patterns and presenting results visually.

This provided a foundation for the more specific GSE43696 asthma transcriptomics case study in:
04-Asthma-Transcriptomics-Case-Study/
