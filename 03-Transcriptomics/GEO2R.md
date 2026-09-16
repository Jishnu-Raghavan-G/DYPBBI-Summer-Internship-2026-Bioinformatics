# GEO2R

## Introduction

GEO2R is a web-based analysis interface associated with the NCBI Gene Expression Omnibus (GEO). It allows researchers to compare gene-expression profiles between groups of samples within suitable GEO datasets.

It is particularly useful when working with publicly available expression datasets because it provides a relatively accessible way to perform comparative gene-expression analysis without building an entire analysis pipeline from raw experimental data.

During the internship, GEO2R was used for the practical analysis of an asthma-related GEO dataset. The dataset used for the case study was **GSE43696**, and healthy and asthma samples were compared to identify differentially expressed genes. :contentReference[oaicite:0]{index=0}

## GEO and GEO2R

GEO acts as the repository, while GEO2R provides an analysis interface for suitable datasets.

```text
GEO
 │
 │  Public gene-expression datasets
 ↓
Select Dataset
 │
 ↓
GEO2R
 │
 ↓
Define Sample Groups
 │
 ↓
Statistical Comparison
 │
 ↓
Differential Expression Results

The internship specifically included learning to perform gene-expression analysis using GEO datasets and GEO2R for identifying differentially expressed genes associated with human diseases.

GEO Accession Number

Every GEO dataset is associated with an accession number that identifies the dataset.

For the asthma transcriptomics case study:

GEO Accession:
GSE43696

This dataset was explored through GEO and analyzed using GEO2R.

Basic GEO2R Workflow

The overall workflow used during the case study can be represented as:

GEO Dataset
     ↓
Select GSE43696
     ↓
Inspect Samples
     ↓
Define Sample Groups
     ↓
Healthy vs Asthma
     ↓
Run GEO2R
     ↓
Obtain Gene-Expression Results
     ↓
Differential Gene Expression
     ↓
Statistical Filtering
     ↓
Selected Genes

The selected genes were then taken forward for functional and network analysis.

Step 1 — Identify the GEO Dataset

The first step is to identify an appropriate GEO dataset based on the biological question.

For example:

Research Question
      ↓
Find Relevant GEO Dataset
      ↓
Check Dataset Description
      ↓
Check Sample Information
      ↓
Select Dataset

For the internship case study, an asthma-related transcriptomic dataset was selected.

Step 2 — Inspect Sample Information

Before performing a comparison, it is important to understand what the samples represent.

A dataset may contain samples from different:

Biological conditions
Patient groups
Experimental treatments
Controls
Tissues
Cell types

The sample information determines how the groups should be defined for analysis.

Step 3 — Define the Comparison Groups

The biological question needs to be converted into a computational comparison.

For the asthma case study:

Group 1
Healthy Samples

        VS

Group 2
Asthma Samples

This allows the expression profiles of the two groups to be statistically compared.

Step 4 — Run the GEO2R Analysis

After defining the groups, GEO2R performs the comparative analysis and produces gene-level results.

The output can contain information such as:

Gene identifiers
Gene names
Expression-related statistics
Fold-change information
p-values
Adjusted p-values

These results can then be examined to identify genes showing differences between the selected groups.

Step 5 — Differential Gene Expression

The purpose of the comparison is to identify differentially expressed genes.

A simplified representation is:

Healthy Expression
        ↓
        VS
        ↓
Asthma Expression
        ↓
Statistical Analysis
        ↓
Differentially Expressed Genes

The internship documentation describes differential gene-expression analysis using GEO2R as a major component of the transcriptomics work.

Log2 Fold Change

One important measurement used when interpreting differential-expression results is log2 fold change (log2FC).

log2FC = log2(Fold Change)

For example:

Fold Change	log2FC
0.25	-2
0.5	-1
1	0
2	+1
4	+2

The sign indicates the direction of change according to the selected comparison.

Positive log2FC
      ↓
Higher expression in the tested condition

Negative log2FC
      ↓
Lower expression in the tested condition

The interpretation always depends on which group was used as the reference.

P-Value

A p-value is used to assess statistical evidence for a difference between groups.

A small p-value indicates stronger statistical evidence against the null hypothesis under the assumptions of the statistical test.

However, transcriptomic studies commonly involve thousands of genes, so p-values must be interpreted with multiple-testing considerations.

Adjusted P-Value

When thousands of genes are tested simultaneously, simply using the raw p-value can result in many apparently significant findings occurring by chance.

Therefore, adjusted p-values are commonly used.

The internship specifically included adjusted p-values as part of the differential-expression analysis and statistical filtering process.

A simplified workflow is:

Gene-wise Statistical Tests
          ↓
       P-values
          ↓
Multiple-testing Correction
          ↓
Adjusted P-values
          ↓
Gene Filtering
Statistical Filtering

After obtaining the GEO2R results, genes can be filtered using selected statistical and effect-size criteria.

A conceptual filtering workflow is:

GEO2R Results
     ↓
Check log2FC
     ↓
Check adjusted p-value
     ↓
Apply selected thresholds
     ↓
Filtered Gene List

The internship case study used adjusted p-values and log2 fold-change values when filtering the differential-expression results.

The exact threshold should always be documented rather than assumed, because different studies can use different criteria.

Example of Filtering

Consider a simplified result table:

Gene	log2FC	Adjusted p-value
Gene A	2.1	0.001
Gene B	0.2	0.400
Gene C	-1.8	0.004
Gene D	0.7	0.020

If the researcher selects particular cutoffs for both effect size and adjusted p-value, only genes satisfying those criteria would be retained.

The important point is that filtering should be based on predefined criteria rather than selecting genes simply because their names appear interesting.

Upregulated and Downregulated Genes

After filtering, genes can be separated according to the direction of their expression change.

                 Differentially
               Expressed Genes
                     │
          ┌──────────┴──────────┐
          ↓                     ↓
    Upregulated            Downregulated
    Positive log2FC        Negative log2FC

Again, the direction depends on the comparison setup.

Interpreting the GEO2R Results

A GEO2R result should not be treated as a biological conclusion by itself.

The next questions are:

What are these genes?
What biological processes are they involved in?
Which pathways contain them?
Do their proteins interact?
Are particular genes central within an interaction network?
Are the findings consistent with existing literature?

This leads to downstream functional and network analysis.

From GEO2R to Functional Analysis

The internship followed the gene list beyond differential expression.

GSE43696
    ↓
GEO2R
    ↓
Healthy vs Asthma
    ↓
Differentially Expressed Genes
    ↓
Statistical Filtering
    ↓
Selected Gene List
    ↓
GO
    ↓
KEGG
    ↓
g:Profiler
    ↓
STRING
    ↓
Cytoscape
    ↓
Hub-Gene Analysis

The documented internship workflow describes this progression from GEO2R-derived genes to functional enrichment and PPI/network analysis.

Gene Ontology After GEO2R

The selected genes can be submitted for Gene Ontology analysis.

GO provides information in three broad categories:

Biological Process

Describes biological processes in which genes or their products participate.

Molecular Function

Describes molecular activities associated with gene products.

Cellular Component

Describes cellular locations where gene products are found.

The internship used GO analysis to investigate these three aspects of the selected gene list.

KEGG After GEO2R

KEGG pathway analysis can be used to investigate pathways associated with the selected genes.

Selected Genes
      ↓
KEGG
      ↓
Associated Pathways
      ↓
Biological Interpretation

During the internship, KEGG was used to connect selected genes with biological and signalling pathways.

g:Profiler After GEO2R

g:Profiler was explored as another resource for functional enrichment and interpretation of gene lists.

Gene List
   ↓
g:Profiler
   ↓
Enriched Biological Categories
   ↓
Interpretation

The internship documentation identifies g:Profiler as one of the resources used for functional enrichment analysis.

STRING and Cytoscape

The selected genes can also be investigated at the protein-interaction level.

Gene List
   ↓
STRING
   ↓
Protein-Protein Interactions
   ↓
Network
   ↓
Cytoscape
   ↓
Network Visualization
   ↓
Hub-Gene Analysis

STRING was used to explore protein-protein interactions, while Cytoscape was used for network visualization and analysis.

Why Sample Selection Matters

GEO2R analysis depends heavily on correctly defining the sample groups.

For example, if the biological question is:

Healthy vs Disease

the selected samples should represent those conditions appropriately.

Incorrect grouping can produce results that do not answer the intended biological question.

Therefore, before running the analysis, the sample metadata should be carefully examined.

Important Considerations

When interpreting a GEO2R analysis, several points should be considered:

Understand the dataset before analyzing it.
Check the sample descriptions.
Define biologically meaningful comparison groups.
Understand which group is the reference.
Examine both effect size and statistical significance.
Consider multiple testing.
Avoid interpreting individual genes without biological context.
Validate interesting findings using biological knowledge and relevant literature.
Treat computational results as evidence that requires interpretation rather than automatic proof of a biological mechanism.
Practical Learning From the Internship

GEO2R was one of the tools through which the internship connected public biological datasets with downstream bioinformatics analysis.

The documented workflow included:

Public GEO Dataset
       ↓
Sample Comparison
       ↓
Differential Gene Expression
       ↓
Statistical Filtering
       ↓
Functional Enrichment
       ↓
PPI Network Analysis
       ↓
Biological Interpretation

This helped demonstrate how a publicly available gene-expression dataset can be taken from an initial database entry toward a broader biological interpretation.

Common Terms
Term	Meaning
GEO	Gene Expression Omnibus
GEO2R	Interface for comparative analysis of suitable GEO expression datasets
GSE	GEO Series accession identifier
GSE43696	GEO dataset used in the internship asthma case study
Sample group	Set of samples representing a defined biological condition
log2FC	Log2-transformed fold change
P-value	Statistical measure associated with a hypothesis test
Adjusted p-value	P-value corrected for multiple testing
DEG	Differentially expressed gene
GO	Gene Ontology
KEGG	Kyoto Encyclopedia of Genes and Genomes
PPI	Protein-protein interaction
Hub gene	A gene/protein occupying a highly connected or otherwise notable position in a network
Key Takeaways
GEO is a repository of publicly available functional genomics datasets.
GEO2R provides an accessible interface for comparative analysis of suitable GEO datasets.
GSE43696 was used as the asthma transcriptomics dataset in the internship case study.
Healthy and asthma samples were compared using GEO2R.
Differentially expressed genes were obtained from the comparison.
Log2FC describes the direction and magnitude of expression change.
Adjusted p-values help account for multiple statistical testing.
Statistical filtering can be used to obtain a selected gene list.
The selected genes can then be studied using GO, KEGG, g:Profiler, STRING, and Cytoscape.
Correct sample grouping and careful interpretation are essential for meaningful results.
GEO2R is a starting point in the analysis rather than the final biological conclusion.
Summary

GEO2R provides a practical way to perform comparative gene-expression analysis using suitable datasets available through GEO. In the internship, it was used as part of an asthma transcriptomics case study involving GSE43696.

The workflow progressed from dataset and sample selection to healthy-versus-asthma comparison, differential gene-expression analysis, statistical filtering, and downstream functional and network analysis.
