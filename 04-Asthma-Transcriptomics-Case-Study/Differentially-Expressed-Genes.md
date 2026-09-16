Overview

Differentially expressed genes (DEGs) are genes whose expression levels differ between the biological conditions being compared.

In this case study, the comparison was between healthy and asthma samples from the GSE43696 dataset. The differential-expression results obtained through the GEO2R workflow were subsequently filtered to obtain genes suitable for downstream biological analysis.

What Is Differential Gene Expression?

Cells do not express every gene at the same level.

Gene-expression levels can change depending on:

Cell type
Biological condition
Disease state
Environmental factors
Developmental stage
Treatment or stimulation

Therefore, comparing gene-expression profiles between two groups can reveal genes associated with differences between those conditions.

For this case study:

Healthy samples
       ↓
Gene-expression profile
       ↓
          Comparison
       ↑
Asthma samples

The resulting differences were investigated as part of the asthma transcriptomics workflow.

Differential-Expression Results

GEO2R provides statistical results for the comparison between the selected sample groups.

Important quantities considered during the analysis included:

Gene identifier
Expression-related statistics
Fold change
log2 fold change
p-value
Adjusted p-value

The internship material specifically describes differential-expression analysis using log2FC, adjusted p-values and statistical filtering.

Fold Change

Fold change describes how much expression differs between two groups.

Conceptually:

Fold Change =
Expression in comparison group
------------------------------
Expression in reference group

For example:

Fold Change = 2

means that expression is approximately twice as high in the comparison group relative to the reference group.

A value below 1 indicates lower expression relative to the reference.

Log2 Fold Change

Fold change is commonly converted into log2 fold change because it provides a symmetric scale for increases and decreases.

log2FC = log2(Fold Change)

Examples:

Fold Change	log2FC	Interpretation
4	+2	Higher expression
2	+1	Higher expression
1	0	No fold difference
0.5	-1	Lower expression
0.25	-2	Lower expression

Therefore:

Positive log2FC
        ↓
Higher expression in the comparison group

Negative log2FC
        ↓
Lower expression in the comparison group
P-Value

The p-value is used to assess the statistical evidence for an observed difference under the statistical model being used.

A smaller p-value indicates stronger statistical evidence against the null hypothesis.

However, transcriptomics experiments can involve thousands of genes being tested simultaneously.

Therefore, using raw p-values alone can be problematic.

Adjusted P-Value

Because many genes are tested simultaneously, multiple-testing correction is important.

An adjusted p-value accounts for the multiple comparisons performed during the analysis.

The internship workflow specifically included adjusted p-values as part of the statistical filtering process.

Conceptually:

Thousands of genes
        ↓
Thousands of statistical tests
        ↓
Multiple-testing correction
        ↓
Adjusted significance measures
Filtering DEGs

The GEO2R results were examined and filtered to obtain a relevant set of differentially expressed genes.

The general workflow was:

GEO2R results
      ↓
Check statistical measures
      ↓
Apply filtering criteria
      ↓
Select relevant genes
      ↓
Downstream analysis

The exact numerical thresholds used for the final case-study gene list should be taken from the actual analysis output rather than reconstructed or invented.

Upregulated and Downregulated Genes

Differentially expressed genes can broadly be separated according to the direction of expression change.

Upregulated Genes

These show higher expression in the comparison condition relative to the reference condition.

log2FC > 0
Downregulated Genes

These show lower expression in the comparison condition.

log2FC < 0

The direction should always be interpreted according to how the two groups were defined in the analysis.

Why DEGs Are Important

A list of DEGs is useful because it provides a starting point for asking biological questions.

For example:

Which biological processes are represented?
             ↓
Which pathways are involved?
             ↓
Which proteins interact?
             ↓
Which genes are highly connected?

This is why differential-expression analysis was followed by functional enrichment and network analysis in the internship workflow.

From DEGs to Biological Interpretation

The selected genes from the asthma analysis were subsequently used for:

Gene Ontology analysis
KEGG pathway analysis
g:Profiler analysis
STRING protein-protein interaction analysis
Cytoscape network analysis
Hub-gene analysis

Thus, the DEG list was not treated as the final result. It served as an input for understanding the biological context of the observed expression differences.

Important Interpretation

A gene being differentially expressed does not by itself prove that the gene causes asthma or is a therapeutic target.

The analysis identifies statistical differences in gene expression between the studied groups. Biological interpretation requires additional evidence from functional analysis, interaction networks, experimental studies and published research.

This distinction was important in the internship's overall computational workflow, which progressed from transcriptomic data toward functional and network interpretation rather than stopping at the DEG list.

Case Study Connection

The complete progression can therefore be represented as:

GSE43696
   ↓
GEO2R
   ↓
Healthy vs Asthma
   ↓
Differential Expression
   ↓
Statistical Filtering
   ↓
DEG List
   ↓
Functional Enrichment
   ↓
PPI Network
   ↓
Hub-Gene Analysis

This forms the central computational pipeline of the asthma transcriptomics case study.
