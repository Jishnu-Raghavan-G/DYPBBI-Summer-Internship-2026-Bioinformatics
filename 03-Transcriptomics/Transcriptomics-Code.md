# Transcriptomics — Practical Code

This file contains beginner-friendly Python practicals related to transcriptomics and gene-expression analysis.

The aim is to understand how an expression matrix can be loaded, inspected, compared between two biological conditions, and visualized.

> **Important:** The numerical dataset created in this file is a simulated teaching dataset. It is not the actual GSE43696 dataset. The same workflow can be adapted to a real GEO/GEO2R expression table after downloading and formatting the data.

## 1. Tools Used

The practicals use:

- Python
- Pandas — data handling
- NumPy — numerical calculations
- Matplotlib — plotting
- Seaborn — statistical visualization
- SciPy — statistical tests
- Statsmodels — multiple-testing correction

Install the required packages if they are not already available:

```bash
pip install pandas numpy matplotlib seaborn scipy statsmodels
2. Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from scipy.stats import ttest_ind
from statsmodels.stats.multitest import multipletests

These libraries provide the basic tools required for expression-data analysis.

3. Create a Small Expression Dataset

For learning purposes, we will create a small simulated gene-expression dataset.

There are two groups:

Healthy
Asthma

Each group contains six samples.

# Make the random values reproducible
np.random.seed(42)

genes = [
    "IL6",
    "IL8",
    "CXCL10",
    "MMP9",
    "STAT1",
    "GAPDH",
    "ACTB",
    "TP53",
    "EGFR",
    "VEGFA"
]

healthy_samples = [
    "Healthy_1",
    "Healthy_2",
    "Healthy_3",
    "Healthy_4",
    "Healthy_5",
    "Healthy_6"
]

asthma_samples = [
    "Asthma_1",
    "Asthma_2",
    "Asthma_3",
    "Asthma_4",
    "Asthma_5",
    "Asthma_6"
]

# Generate simulated expression values
healthy_data = np.random.normal(
    loc=10,
    scale=1.0,
    size=(len(genes), len(healthy_samples))
)

asthma_data = np.random.normal(
    loc=10,
    scale=1.0,
    size=(len(genes), len(asthma_samples))
)

# Add higher expression to selected genes in the simulated asthma group
asthma_data[0] += 3.0   # IL6
asthma_data[1] += 2.5   # IL8
asthma_data[2] += 2.0   # CXCL10
asthma_data[3] += 1.8   # MMP9
asthma_data[4] += 1.5   # STAT1

# Combine the data
expression_matrix = pd.DataFrame(
    np.column_stack([healthy_data, asthma_data]),
    index=genes,
    columns=healthy_samples + asthma_samples
)

print(expression_matrix)

The resulting table has genes as rows and biological samples as columns.

4. Save the Expression Matrix

The expression matrix can be saved as a CSV file.

expression_matrix.to_csv("simulated_gene_expression.csv")

print("Expression matrix saved successfully.")

This creates:

simulated_gene_expression.csv
5. Load the Expression Matrix

The same file can be loaded again using Pandas.

expression_matrix = pd.read_csv(
    "simulated_gene_expression.csv",
    index_col=0
)

print(expression_matrix.head())

The index_col=0 argument tells Pandas that the first column contains gene names.

6. Inspect the Dataset

Before performing any analysis, it is useful to inspect the dataset.

print("Number of genes:", expression_matrix.shape[0])
print("Number of samples:", expression_matrix.shape[1])

print("\nSample names:")
print(expression_matrix.columns.tolist())

print("\nGene names:")
print(expression_matrix.index.tolist())

We can also check whether missing values are present.

print("\nMissing values:")
print(expression_matrix.isnull().sum().sum())

A result of 0 means that the simulated dataset contains no missing values.

7. Separate the Biological Groups

The samples are divided into Healthy and Asthma groups.

healthy = expression_matrix[healthy_samples]
asthma = expression_matrix[asthma_samples]

print("Healthy samples:")
print(healthy.columns.tolist())

print("\nAsthma samples:")
print(asthma.columns.tolist())

This separation is important because differential-expression analysis compares expression between biological conditions.

8. Calculate Mean Expression

The average expression of every gene can be calculated for both groups.

mean_healthy = healthy.mean(axis=1)
mean_asthma = asthma.mean(axis=1)

mean_expression = pd.DataFrame({
    "Healthy_Mean": mean_healthy,
    "Asthma_Mean": mean_asthma
})

print(mean_expression)

The resulting table makes it easier to see which genes have higher or lower average expression between the two groups.

9. Calculate Fold Change

Fold change compares the average expression between two conditions.

For this example:

Fold Change = Asthma mean / Healthy mean
fold_change = mean_asthma / mean_healthy

mean_expression["Fold_Change"] = fold_change

print(mean_expression)

A fold change greater than 1 indicates higher expression in the asthma group.

A fold change less than 1 indicates lower expression in the asthma group.

10. Calculate log2 Fold Change

Log2 fold change is commonly used because it makes increases and decreases easier to compare.

mean_expression["log2_FC"] = np.log2(
    mean_expression["Fold_Change"]
)

print(mean_expression)

Interpretation:

log2FC = 0       → no change
log2FC > 0      → higher expression in asthma
log2FC < 0      → lower expression in asthma

For example:

log2FC = +1  → approximately 2 times higher
log2FC = -1  → approximately 2 times lower
log2FC = +2  → approximately 4 times higher
log2FC = -2  → approximately 4 times lower
11. Perform a Statistical Test

A two-sample t-test can be used as a simple introduction to testing whether expression differs between two groups.

p_values = []

for gene in expression_matrix.index:

    healthy_values = healthy.loc[gene]
    asthma_values = asthma.loc[gene]

    statistic, p_value = ttest_ind(
        healthy_values,
        asthma_values,
        equal_var=False
    )

    p_values.append(p_value)

mean_expression["p_value"] = p_values

print(mean_expression)

The p-value indicates how compatible the observed difference is with the null hypothesis of no difference between the groups.

12. Correct for Multiple Testing

When many genes are tested simultaneously, using raw p-values alone can produce false-positive results.

The Benjamini-Hochberg method can be used to control the false discovery rate.

adjusted_results = multipletests(
    mean_expression["p_value"],
    method="fdr_bh"
)

mean_expression["adjusted_p_value"] = adjusted_results[1]

print(mean_expression)

The adjusted p-value is often called:

FDR
Adjusted p-value
q-value

depending on the analysis software and reporting convention.

13. Sort Genes by Significance

The results can be sorted according to adjusted p-value.

results = mean_expression.sort_values(
    by="adjusted_p_value"
)

print(results)

Genes appearing near the top have stronger statistical evidence for differential expression in this example.

14. Apply Differential-Expression Filters

A simple filtering strategy can be used:

|log2FC| >= 1
adjusted p-value < 0.05

This means:

at least a two-fold change in either direction
statistically significant after multiple-testing correction
significant_genes = results[
    (results["adjusted_p_value"] < 0.05) &
    (results["log2_FC"].abs() >= 1)
]

print(significant_genes)

The thresholds used in a real study should be selected according to the experimental design and analysis method rather than chosen automatically.

15. Identify Upregulated Genes

Genes satisfying the positive log2FC threshold can be classified as upregulated.

upregulated = significant_genes[
    significant_genes["log2_FC"] >= 1
]

print("Upregulated genes:")
print(upregulated)
16. Identify Downregulated Genes

Similarly, genes with sufficiently negative log2FC can be classified as downregulated.

downregulated = significant_genes[
    significant_genes["log2_FC"] <= -1
]

print("Downregulated genes:")
print(downregulated)
17. Create a Heatmap

A heatmap provides a visual representation of expression values across samples.

plt.figure(figsize=(12, 7))

sns.heatmap(
    expression_matrix,
    cmap="viridis",
    annot=True,
    fmt=".1f"
)

plt.title("Simulated Gene Expression Heatmap")
plt.xlabel("Samples")
plt.ylabel("Genes")

plt.tight_layout()
plt.show()

The heatmap makes differences in expression patterns across samples easier to observe.

18. Standardize Expression for Heatmap Visualization

Genes can have different expression ranges. Standardization can help compare relative patterns.

standardized = expression_matrix.copy()

standardized = standardized.apply(
    lambda row: (row - row.mean()) / row.std(),
    axis=1
)

print(standardized.head())

Now the standardized values can be plotted.

plt.figure(figsize=(12, 7))

sns.heatmap(
    standardized,
    cmap="coolwarm",
    center=0
)

plt.title("Standardized Gene Expression")
plt.xlabel("Samples")
plt.ylabel("Genes")

plt.tight_layout()
plt.show()

The values represent how far each sample is from the average expression of that particular gene.

19. Create a Volcano Plot

A volcano plot combines two important features:

magnitude of expression change
statistical significance

We first calculate the negative log10 of the adjusted p-value.

results["minus_log10_FDR"] = -np.log10(
    results["adjusted_p_value"]
)

print(results.head())

Now create the plot.

plt.figure(figsize=(10, 7))

plt.scatter(
    results["log2_FC"],
    results["minus_log10_FDR"]
)

plt.axvline(
    x=1,
    linestyle="--"
)

plt.axvline(
    x=-1,
    linestyle="--"
)

plt.axhline(
    y=-np.log10(0.05),
    linestyle="--"
)

plt.xlabel("log2 Fold Change")
plt.ylabel("-log10 Adjusted p-value")
plt.title("Differential Gene Expression Volcano Plot")

plt.tight_layout()
plt.show()

The horizontal and vertical lines represent the example filtering thresholds.

20. Label Significant Genes

Important genes can be labelled on the volcano plot.

plt.figure(figsize=(10, 7))

plt.scatter(
    results["log2_FC"],
    results["minus_log10_FDR"]
)

for gene in significant_genes.index:

    x = results.loc[gene, "log2_FC"]
    y = results.loc[gene, "minus_log10_FDR"]

    plt.text(
        x,
        y,
        gene,
        fontsize=9
    )

plt.axvline(
    x=1,
    linestyle="--"
)

plt.axvline(
    x=-1,
    linestyle="--"
)

plt.axhline(
    y=-np.log10(0.05),
    linestyle="--"
)

plt.xlabel("log2 Fold Change")
plt.ylabel("-log10 Adjusted p-value")
plt.title("Differentially Expressed Genes")

plt.tight_layout()
plt.show()
21. Export Differential-Expression Results

The complete analysis table can be saved for further analysis.

results.to_csv(
    "differential_expression_results.csv"
)

print("Differential-expression results saved.")

The significant genes can also be exported separately.

significant_genes.to_csv(
    "significant_genes.csv"
)

print("Significant genes saved.")

These files can later be used for downstream analyses such as:

Gene Ontology analysis
KEGG pathway analysis
g:Profiler analysis
STRING protein-protein interaction analysis
Cytoscape network visualization
22. Working With a Real Expression CSV

The same workflow can be applied to a real expression matrix downloaded from a public database.

A simple expected structure is:

Gene,Healthy_1,Healthy_2,Healthy_3,Asthma_1,Asthma_2,Asthma_3
IL6,8.2,8.5,8.1,12.3,11.8,12.6
IL8,7.4,7.7,7.5,10.2,10.5,10.1
...

The first column contains gene identifiers.

The remaining columns contain expression values for individual samples.

Load the file:

real_data = pd.read_csv(
    "your_expression_data.csv"
)

print(real_data.head())

Set the gene column as the index:

real_data = real_data.set_index("Gene")

print(real_data.head())

Define the sample groups:

healthy_samples = [
    "Healthy_1",
    "Healthy_2",
    "Healthy_3"
]

asthma_samples = [
    "Asthma_1",
    "Asthma_2",
    "Asthma_3"
]

Then separate the groups:

healthy = real_data[healthy_samples]
asthma = real_data[asthma_samples]

The downstream calculations can then follow the same workflow used above.

23. Important Point About GEO2R

GEO2R is primarily a web-based analysis interface provided through the GEO resource.

Therefore, Python is not required to perform the GEO2R analysis itself.

A practical workflow can be:

GEO dataset
     ↓
GEO2R
     ↓
Differential-expression results
     ↓
Download results
     ↓
Python / Pandas
     ↓
Filtering and visualization
     ↓
GO / KEGG / g:Profiler
     ↓
STRING / Cytoscape

For the asthma case study, the relevant GEO dataset was GSE43696, which was used to study gene-expression differences between healthy and asthma-related samples. The internship workflow involved GEO2R-based differential expression followed by filtering and downstream functional/network analysis.

24. Example: Reading a GEO2R Result Table

If a GEO2R result has already been downloaded as a CSV file, it can be loaded with:

geo_results = pd.read_csv(
    "GEO2R_results.csv"
)

print(geo_results.head())
print(geo_results.columns)

Because GEO exports can contain different column names depending on the analysis and download format, always inspect the columns before writing filtering code.

print(
    geo_results.columns.tolist()
)

For example, if the table contains:

Gene
log2FC
P.Value
adj.P.Val

the significant genes could be extracted using:

significant_geo_genes = geo_results[
    (geo_results["adj.P.Val"] < 0.05) &
    (geo_results["log2FC"].abs() >= 1)
]

print(significant_geo_genes)
25. Select Gene Names for Downstream Analysis

After differential-expression filtering, the gene identifiers can be extracted.

gene_list = significant_geo_genes["Gene"].dropna().tolist()

print("Number of selected genes:", len(gene_list))

print("\nFirst genes:")
print(gene_list[:20])

This gene list can then be used as input for downstream functional-analysis resources.

For example:

Differentially expressed genes
            ↓
       Gene list
            ↓
     ┌──────┼──────┐
     ↓      ↓      ↓
     GO    KEGG  g:Profiler
     ↓      ↓      ↓
 Functional interpretation
26. Basic Gene-Expression Bar Plot

A simple bar plot can be used to compare the average expression of selected genes.

selected_genes = ["IL6", "IL8", "CXCL10", "MMP9"]

plot_data = mean_expression.loc[
    selected_genes,
    ["Healthy_Mean", "Asthma_Mean"]
]

plot_data.plot(
    kind="bar",
    figsize=(10, 6)
)

plt.xlabel("Genes")
plt.ylabel("Mean Expression")
plt.title("Mean Gene Expression: Healthy vs Asthma")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
27. Basic Correlation Between Genes

Correlation can be used to investigate whether two genes show similar expression patterns across samples.

correlation = expression_matrix.T.corr()

print(correlation)

The transpose is used because correlation between genes requires genes to be treated as variables and samples as observations.

A heatmap can visualize the correlation matrix:

plt.figure(figsize=(9, 7))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    center=0
)

plt.title("Gene Expression Correlation")

plt.tight_layout()
plt.show()
28. Complete Beginner Workflow

The practical transcriptomics workflow implemented in this file can be summarized as:

1. Obtain expression data
          ↓
2. Load data with Pandas
          ↓
3. Inspect genes and samples
          ↓
4. Separate biological groups
          ↓
5. Calculate mean expression
          ↓
6. Calculate fold change
          ↓
7. Calculate log2 fold change
          ↓
8. Perform statistical testing
          ↓
9. Correct for multiple testing
          ↓
10. Filter significant genes
          ↓
11. Visualize expression patterns
          ↓
12. Export results
          ↓
13. Perform functional and network analysis
29. Important Practical Notes

The code in this file is intended to teach the computational logic behind transcriptomics analysis.

The simulated dataset is useful for understanding:

expression matrices
biological groups
fold change
log2 fold change
p-values
adjusted p-values
differential-expression filtering
heatmaps
volcano plots
correlation analysis
exporting results

For a real transcriptomics study, additional considerations are required, including:

experimental design
biological replicates
normalization
batch effects
appropriate statistical models
correct annotation of genes
multiple-testing correction
biological interpretation

A simple t-test is useful for learning the concept, but it should not automatically be treated as the preferred analysis method for every real transcriptomics experiment.

30. Learning Outcome

After completing these practicals, a beginner should be able to:

understand the structure of a gene-expression matrix
load expression data using Pandas
separate samples into biological groups
calculate mean expression
calculate fold change
calculate log2 fold change
perform a basic statistical comparison
apply false-discovery-rate correction
identify candidate differentially expressed genes
generate heatmaps
generate volcano plots
export analysis results
understand how GEO/GEO2R results can enter a Python-based downstream workflow
prepare a gene list for functional and network analysis

This practical workflow provides the computational foundation for the transcriptomics case study and downstream analyses performed during the bioinformatics training.
