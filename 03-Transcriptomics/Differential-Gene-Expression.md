# Differential Gene Expression

## Introduction

Differential Gene Expression (DGE) analysis is used to identify genes whose expression levels differ between two or more biological conditions.

For example, researchers may compare:

- Healthy vs disease
- Treated vs untreated
- Control vs experimental
- Different tissue types
- Different developmental stages

The basic idea is:

```text
Condition A
    ↓
Gene Expression Profile
    ↓
        COMPARISON
    ↓
Condition B
    ↓
Gene Expression Profile
    ↓
Statistical Analysis
    ↓
Differentially Expressed Genes

During the internship, differential gene expression was an important part of the transcriptomics workflow. The asthma case study used GEO2R to compare healthy and asthma samples from the GEO dataset GSE43696, followed by statistical filtering of the resulting genes.

What is a Differentially Expressed Gene?

A differentially expressed gene (DEG) is a gene whose measured expression differs between the biological groups being compared according to the statistical and effect-size criteria used in the analysis.

For example:

Gene	Healthy	Disease	Observation
Gene A	100	300	Increased
Gene B	500	480	Small change
Gene C	400	100	Decreased

The numerical difference alone is not sufficient to classify a gene as a meaningful DEG. Statistical evidence and appropriate filtering criteria also need to be considered.

Upregulated and Downregulated Genes

DEGs are commonly divided according to the direction of expression change.

Upregulated Genes

A gene is described as upregulated when its expression is higher in the condition of interest compared with the reference condition.

Reference condition = 100
Disease condition    = 300

Expression increased
        ↓
Upregulated
Downregulated Genes

A gene is described as downregulated when its expression is lower in the condition of interest.

Reference condition = 300
Disease condition    = 100

Expression decreased
        ↓
Downregulated

The interpretation depends on how the comparison was defined.

Expression Matrix

DGE analysis generally begins with expression measurements across multiple samples.

Example:

Gene	Healthy 1	Healthy 2	Asthma 1	Asthma 2
Gene A	5.1	5.3	7.8	8.0
Gene B	6.2	6.4	6.1	6.3
Gene C	3.0	3.2	5.6	5.8

The rows represent genes and the columns represent samples.

The statistical analysis uses the expression measurements from the groups to determine which genes show evidence of differential expression.

Biological Replicates

Biological variation is an important part of gene-expression analysis.

For example:

Healthy
 ├── Sample 1
 ├── Sample 2
 └── Sample 3

Asthma
 ├── Sample 1
 ├── Sample 2
 └── Sample 3

Multiple biological samples allow the analysis to estimate variation within each group.

This is important because a difference observed in only one sample may not represent a consistent biological pattern.

Fold Change

Fold change describes the relative difference in expression between two conditions.

For example:

Healthy = 100
Asthma  = 200

Fold Change = 200 / 100
            = 2

This represents a two-fold increase.

For a decrease:

Healthy = 200
Asthma  = 100

Fold Change = 100 / 200
            = 0.5

This represents a decrease relative to the reference.

Log2 Fold Change

Gene-expression analyses frequently use log2 fold change (log2FC).

log2FC = log2(Fold Change)

Examples:

Fold Change	log2FC	Direction
0.25	-2	Decreased
0.5	-1	Decreased
1	0	No change
2	+1	Increased
4	+2	Increased

The positive or negative sign indicates the direction of the change.

The magnitude indicates how large the change is.

P-Value

A p-value is a statistical measure used to evaluate the evidence for a difference between groups under a specified statistical model.

In DGE analysis, a statistical test is performed for each gene.

A simplified workflow is:

Gene Expression
      ↓
Statistical Test
      ↓
P-value
      ↓
Interpretation

However, thousands of genes may be tested simultaneously.

This creates an important multiple-testing problem.

Multiple Testing

Suppose an analysis examines 10,000 genes.

If each gene is tested separately, 10,000 statistical tests are performed.

Even when there are no real biological differences, some genes may appear statistically significant simply by chance.

Therefore:

Thousands of Genes
       ↓
Thousands of Statistical Tests
       ↓
Multiple-Testing Problem
       ↓
Correction
       ↓
Adjusted P-values

This is why adjusted p-values are commonly considered when selecting DEGs.

Adjusted P-Value

An adjusted p-value accounts for the fact that many statistical tests are being performed simultaneously.

The internship specifically included adjusted p-values as part of transcriptomic analysis and statistical filtering.

A simplified interpretation is:

Raw P-values
     ↓
Multiple-testing correction
     ↓
Adjusted P-values

The exact correction method depends on the statistical workflow.

Statistical Significance

A gene may be considered statistically significant when its statistical result meets the predefined significance criterion.

However, the criterion should be selected before interpreting the final results whenever possible.

For example:

Adjusted p-value
       ↓
Compare with selected threshold
       ↓
Significant / Not significant

The internship case study used adjusted p-values together with log2 fold-change information for statistical filtering.

Effect Size and Statistical Significance

Two different questions should be separated:

Question 1

How large is the expression change?

This can be examined using fold change or log2FC.

Question 2

How strong is the statistical evidence for the observed difference?

This can be examined using p-values and adjusted p-values.

Therefore:

Effect Size
     +
Statistical Evidence
     ↓
More informative DEG interpretation

A statistically significant result does not automatically mean that the biological effect is large.

Similarly, a large apparent expression difference may not have strong statistical support.

DEG Filtering

After obtaining differential-expression results, researchers commonly apply filtering criteria.

A general workflow is:

All Genes
   ↓
Differential Expression Analysis
   ↓
log2FC + Adjusted P-value
   ↓
Apply Selected Thresholds
   ↓
Filtered DEG List

For example, a researcher may require both:

Sufficient expression change
        AND
Sufficient statistical evidence

The exact thresholds should be reported with the analysis.

Example of DEG Filtering

Consider the following simplified results:

Gene	log2FC	Adjusted p-value
Gene A	+2.4	0.001
Gene B	+0.3	0.400
Gene C	-1.9	0.003
Gene D	+1.2	0.200
Gene E	-2.5	0.010

If predefined thresholds are applied, only genes satisfying those thresholds would be retained.

For example, the filtering logic could conceptually be:

IF
   |log2FC| meets required cutoff
AND
   adjusted p-value meets required cutoff

THEN
   retain gene

This is a conceptual example. The actual threshold should come from the specific analysis rather than being assumed.

Volcano Plot

A volcano plot is commonly used to visualize differential-expression results.

It combines information about:

log2 fold change
Statistical significance

A simplified representation:

                    Significance
                         ↑
                         |
              *          |          *
            *            |            *
          *              |              *
        *                |                *
-------------------------+------------------------→ log2FC
     Downregulated       |       Upregulated

Genes with larger expression changes and stronger statistical evidence tend to appear farther from the center and higher on the plot.

Heatmap

A heatmap can be used to visualize expression patterns across samples.

Example:

              Healthy 1  Healthy 2  Asthma 1  Asthma 2

Gene A           ░          ░          █         █
Gene B           █          █          ▓         ▓
Gene C           ░          ░          █         █
Gene D           ▓          ▓          ░         ░

Actual heatmaps normally use a color scale rather than symbols.

Heatmaps can help reveal:

Groups of similarly expressed genes
Similar samples
Differences between conditions
Expression patterns
DGE in the Asthma Case Study

Differential gene expression was a major component of the internship's asthma transcriptomics analysis.

The documented workflow was:

GSE43696
   ↓
GEO
   ↓
GEO2R
   ↓
Healthy vs Asthma
   ↓
Differential Gene Expression
   ↓
Statistical Filtering
   ↓
Selected Genes

The selected genes were subsequently used for functional and network analysis.

From DEGs to Functional Analysis

Identifying DEGs is not the final stage.

The next step is to determine whether the genes are associated with particular biological functions or pathways.

Differentially Expressed Genes
            ↓
      Gene Ontology
            ↓
      KEGG Pathways
            ↓
       g:Profiler
            ↓
    Biological Interpretation

The internship used GO, KEGG, and g:Profiler for this type of downstream interpretation.

From DEGs to PPI Networks

Genes can also be examined through their corresponding proteins and known or predicted interactions.

DEG List
   ↓
STRING
   ↓
Protein-Protein Interaction Network
   ↓
Cytoscape
   ↓
Network Visualization
   ↓
Hub-Gene Analysis

STRING was used to explore protein-protein interactions, and Cytoscape was used for network visualization and analysis during the internship.

Biological Interpretation

A DEG list should not be interpreted in isolation.

A stronger interpretation considers:

The direction of expression change
Magnitude of change
Statistical evidence
Biological function
Pathway involvement
Protein interactions
Existing research literature
Experimental context

This is why the internship progressed from gene-expression analysis toward functional enrichment and network analysis rather than stopping at a list of statistically filtered genes.

Common Mistakes in DGE Analysis
Looking Only at Fold Change

A large fold change does not by itself establish statistical significance.

Looking Only at P-values

A statistically significant result may correspond to a very small biological effect.

Ignoring Multiple Testing

Testing thousands of genes requires appropriate correction.

Ignoring Sample Information

Incorrect group assignment can lead to a comparison that does not represent the intended biological question.

Treating DEGs as Biological Proof

A computationally identified DEG is a result requiring interpretation and, where appropriate, further validation.

DGE Workflow

A generalized workflow can be summarized as:

Expression Dataset
       ↓
Sample Quality / Metadata Review
       ↓
Define Comparison Groups
       ↓
Preprocessing / Normalization
       ↓
Statistical Analysis
       ↓
P-values
       ↓
Multiple-testing Correction
       ↓
Adjusted P-values
       ↓
Effect Size / log2FC
       ↓
DEG Filtering
       ↓
Heatmap / Volcano Plot
       ↓
GO / KEGG / Enrichment
       ↓
PPI / Network Analysis
       ↓
Biological Interpretation

The exact upstream processing differs between technologies such as microarray and RNA-Seq.

Practical Learning During the Internship

The internship provided exposure to:

Gene-expression analysis
RNA sequencing concepts
Microarray technology
GEO datasets
GEO2R
Differential gene expression
Log2 fold change
Adjusted p-values
Statistical filtering
Functional interpretation

The asthma case study provided a practical context for understanding how differential-expression results can be connected to functional and network-level analysis.

Common Terms
Term	Meaning
DGE	Differential Gene Expression
DEG	Differentially Expressed Gene
Upregulated	Increased expression relative to the reference group
Downregulated	Decreased expression relative to the reference group
Fold change	Relative expression difference between groups
log2FC	Log2-transformed fold change
P-value	Statistical measure from a hypothesis test
Adjusted p-value	P-value corrected for multiple testing
Multiple testing	Performing many statistical tests simultaneously
Expression matrix	Gene-by-sample table of expression measurements
Volcano plot	Plot showing expression change and statistical significance
Heatmap	Visualization of expression patterns
Reference group	Group against which another group is compared
Key Takeaways
Differential gene expression identifies genes whose expression differs between biological conditions.
DEGs are commonly classified as upregulated or downregulated according to the direction of change.
Fold change and log2FC describe expression differences.
P-values provide statistical evidence for observed differences.
Adjusted p-values are important because transcriptomic studies test many genes simultaneously.
DEG filtering should use predefined and clearly reported criteria.
Heatmaps and volcano plots help visualize differential-expression results.
A DEG list is a starting point for biological interpretation.
GO, KEGG, g:Profiler, STRING, and Cytoscape can be used for downstream analysis.
Correct sample grouping and careful interpretation are essential.
Statistical significance and biological importance are related but different concepts.
Summary

Differential Gene Expression analysis provides a computational method for identifying genes whose expression differs between biological conditions. The analysis combines measurements of expression change with statistical evidence to produce a list of genes for further investigation.

In the internship's asthma case study, GEO2R was used to compare healthy and asthma samples from GSE43696. The resulting differential-expression results were filtered using log2 fold-change and adjusted p-value information, after which selected genes were taken forward for functional and network analysis.

The broader workflow demonstrated that differential-expression analysis is one stage of a larger bioinformatics process:

Expression Data
      ↓
Differential Expression
      ↓
DEG List
      ↓
Functional Analysis
      ↓
Network Analysis
      ↓
Biological Interpretation
