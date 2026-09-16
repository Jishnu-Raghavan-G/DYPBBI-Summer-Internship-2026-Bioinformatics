Overview

GEO2R was used as the main analysis interface for the GSE43696 asthma transcriptomics case study.

The objective was to compare gene-expression profiles between the relevant healthy and asthma groups and identify genes showing differences in expression. The internship workflow then used the resulting genes for statistical filtering and downstream functional and network analysis.

Dataset Selection

The analysis started with the GEO accession:

GSE43696

The dataset was accessed through the NCBI Gene Expression Omnibus (GEO) database.

The general workflow was:

NCBI GEO
   ↓
GSE43696
   ↓
GEO2R
   ↓
Define sample groups
   ↓
Compare gene expression
Group Comparison

The case study focused on a comparison between:

Healthy samples
        vs
Asthma samples

This comparison was used to investigate genes whose expression differed between the two conditions.

GEO2R Workflow

The practical workflow can be summarized as follows:

1. Open the Dataset

The GSE43696 accession was located in GEO.

The dataset page provides information about the experiment, samples and available expression data.

2. Launch GEO2R

GEO2R was used to perform a statistical comparison of the selected sample groups.

3. Assign Sample Groups

Samples were categorized according to the biological conditions being compared.

Group 1 → Healthy
Group 2 → Asthma

Correct group assignment is important because the statistical comparison depends on how the samples are classified.

4. Run the Comparison

After defining the groups, GEO2R was used to generate the differential-expression results.

The output provides statistical information that can be used to investigate differences in gene expression.

5. Examine the Results

The resulting table was examined using measures such as:

Gene identifiers
Expression-related statistics
Fold change
log2 fold change
p-values
Adjusted p-values

These measures helped determine which genes showed notable differences between the groups.

The internship methodology specifically included differential gene expression, log2FC, adjusted p-values and statistical filtering.

Differential-Expression Filtering

The GEO2R output was not treated as the final biological conclusion.

Instead, genes were filtered using statistical criteria to obtain a relevant set of differentially expressed genes.

Conceptually:

GEO2R Results
      ↓
Statistical filtering
      ↓
Differentially expressed genes
      ↓
Biological interpretation

The exact filtering criteria should be recorded from the actual analysis output used during the internship rather than introducing arbitrary values into the repository.

Log2 Fold Change

One important measure used during the analysis was log2 fold change (log2FC).

It describes the direction and magnitude of expression change between groups.

log2FC > 0
    ↓
Higher expression in the comparison group

log2FC < 0
    ↓
Lower expression in the comparison group

log2FC ≈ 0
    ↓
Little difference in expression

For example:

log2FC = +1  → approximately 2-fold increase

log2FC = -1  → approximately 2-fold decrease

The sign and magnitude therefore provide useful information about expression differences.

Adjusted P-Values

When thousands of genes are tested simultaneously, multiple statistical tests are performed.

Therefore, simply considering raw p-values can result in an increased number of apparently significant results occurring by chance.

Adjusted p-values help account for this multiple-testing problem.

The internship workflow specifically included adjusted p-values as part of differential-expression filtering.

Selection of Genes

After statistical filtering, selected genes were taken forward for downstream analysis.

The workflow was:

GEO2R
  ↓
Differential-expression results
  ↓
Statistical filtering
  ↓
Selected gene list
  ↓
GO / KEGG / g:Profiler
  ↓
STRING / Cytoscape
  ↓
Hub-gene analysis

This progression is documented in the internship material as the main asthma transcriptomics workflow.

Downstream Analysis

The filtered gene list was subsequently used for several types of analysis.

Functional Enrichment

The genes were investigated using:

Gene Ontology
KEGG
g:Profiler

These analyses helped examine biological functions and pathways associated with the selected genes.

PPI Network Analysis

STRING was used to investigate protein-protein interactions associated with the selected genes.

Network Visualization

Cytoscape was used to visualize and explore the interaction network.

Hub-Gene Analysis

The network was further examined to identify highly connected nodes for hub-gene analysis.

What I Learned

The GEO2R exercise helped me understand how a publicly available gene-expression dataset can be converted into a biologically interpretable analysis.

The major learning points were:

How GEO datasets are organized
How a GEO accession is used to identify a study
How sample groups are defined
How gene-expression differences are statistically examined
The meaning of log2FC
The importance of adjusted p-values
How differential-expression results are filtered
How a gene list becomes the input for functional and network analysis
Important Note

GEO2R provides statistical results, but statistical significance does not automatically establish biological importance.

The selected genes therefore need to be interpreted using additional biological evidence, such as functional enrichment, pathway analysis and interaction networks. This was an important part of the internship workflow, where differential-expression results were followed by GO, KEGG, g:Profiler, STRING and Cytoscape analyses.

Reproducibility

For a complete repository, the following should be preserved where available:

Dataset accession
Sample-group definitions
GEO2R output
Filtering criteria
Selected gene list
Statistical results
Figures/screenshots
Downstream analysis outputs

This makes the case study easier to understand and reproduce without confusing the original analysis with simplified educational Python exercises.
