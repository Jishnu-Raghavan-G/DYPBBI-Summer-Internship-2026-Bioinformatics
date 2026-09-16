# RNA-Seq and Microarray

## Introduction

Transcriptomic studies are used to understand which genes are being expressed in a biological sample and how their expression changes between different conditions.

Two important technologies used for transcriptomic analysis are:

- RNA sequencing (RNA-Seq)
- Microarray

Both methods can be used to study gene expression, but they generate data in different ways.

During the internship, RNA-Seq and microarray-based transcriptomics were introduced as part of the study of gene-expression analysis. The asthma case study was based on a publicly available microarray dataset from GEO, which was analyzed using GEO2R.

## What is RNA-Seq?

RNA sequencing, commonly called RNA-Seq, is a sequencing-based method used to study RNA molecules present in a sample.

Instead of measuring only a predefined set of genes, RNA-Seq generates sequence reads from RNA molecules. These reads can then be processed computationally to determine which transcripts are present and how abundant they are.

A simplified workflow is:

```text
Biological Sample
       ↓
RNA Extraction
       ↓
mRNA / RNA Preparation
       ↓
Library Preparation
       ↓
Sequencing
       ↓
Sequence Reads
       ↓
Quality Control
       ↓
Alignment / Quantification
       ↓
Expression Matrix
       ↓
Differential Expression Analysis
       ↓
Biological Interpretation

The exact workflow can vary depending on the experimental design and analysis method.

Basic Principle of RNA-Seq

The basic idea is to convert RNA molecules into a form that can be sequenced and then use computational analysis to determine their abundance.

A simplified process is:

RNA molecules
      ↓
RNA preparation
      ↓
cDNA/library generation
      ↓
Sequencing
      ↓
Short sequence reads
      ↓
Computational analysis
      ↓
Gene/transcript expression

The resulting sequencing reads contain information about the RNA molecules present in the sample.

Reads

A sequencing instrument does not normally provide a complete RNA molecule as one long sequence.

Instead, sequencing produces many shorter sequences called reads.

For example:

RNA molecule
────────────────────────────────────────

Sequencing reads

Read 1 → ACGTACGT...
Read 2 → TGCAACGA...
Read 3 → CGTATGCA...
Read 4 → ATGCCGTA...

The reads are computationally processed to determine their relationship to genes or transcripts.

Expression Quantification

After processing the sequencing reads, the number of reads associated with particular genes or transcripts can be used to estimate their expression.

A simplified example:

Gene	Sample 1	Sample 2
Gene A	120	450
Gene B	800	760
Gene C	50	300

Gene A and Gene C show higher expression in Sample 2 in this simplified example.

However, raw read counts cannot always be compared directly without considering sequencing depth and other technical factors. Therefore, normalization and appropriate statistical methods are important.

RNA-Seq Data

RNA-Seq analysis can produce an expression matrix similar to other transcriptomic experiments.

             Sample 1   Sample 2   Sample 3
Gene A          120        450        390
Gene B          800        760        820
Gene C           50        300        280
Gene D          210        190        205

Here:

Rows represent genes or transcripts.
Columns represent biological samples.
Values represent an expression measurement.

This matrix can subsequently be used for downstream analyses such as differential expression and visualization.

Advantages of RNA-Seq

Some important advantages of RNA-Seq are:

It is sequencing-based.
It can provide information about transcripts across the transcriptome.
It can detect transcripts that were not specifically included on a predefined array.
It can provide information at transcript-level depending on the analysis.
It can be used for many different types of RNA analysis.
Limitations of RNA-Seq

RNA-Seq also has practical and computational challenges:

Sequencing experiments can generate very large datasets.
Data processing requires computational resources.
Quality control is important.
Read alignment or quantification requires appropriate reference information or methods.
Statistical analysis requires careful experimental design.
Technical variation can affect results.

Therefore, obtaining sequencing data is only the beginning. Proper computational processing is required before biological conclusions can be made.

What is a Microarray?

A microarray is a technology used to measure the expression of many genes simultaneously using probes attached to a solid surface.

The probes are designed to correspond to particular genes or transcript sequences.

A simplified representation is:

RNA from sample
      ↓
Labelled target molecules
      ↓
Hybridization with probes
      ↓
Microarray
      ↓
Signal measurement
      ↓
Expression values

The measured signal is used as an indication of the expression level of the corresponding genes.

Basic Principle of Microarrays

Microarray analysis is based mainly on nucleic-acid hybridization.

A probe on the array is designed to recognize a complementary sequence.

Probe:      A T G C C A
            | | | | | |
Target:     T A C G G T

When the target sequence binds to its corresponding probe, the resulting signal can be measured.

Thousands of probes can be present on a single array, allowing expression of many genes to be studied simultaneously.

Microarray Expression Matrix

The output of a microarray experiment can also be represented as an expression matrix.

For example:

Gene	Healthy 1	Healthy 2	Asthma 1	Asthma 2
Gene A	5.2	5.0	8.1	7.8
Gene B	7.1	7.3	6.9	7.0
Gene C	3.2	3.4	6.2	6.0

This type of matrix can be used to identify genes whose expression differs between biological conditions.

Microarray Probes

One important feature of microarrays is the use of predefined probes.

This means that the genes or sequences that can be measured depend on the design of the array.

Therefore, microarrays are generally more dependent on the probe set and platform used in the experiment.

Microarray Data in GEO

Public repositories such as the Gene Expression Omnibus (GEO) contain many microarray datasets.

During the internship, publicly available asthma-related microarray data were obtained from GEO and explored using GEO2R.

The case study used the dataset:

GSE43696

The analysis involved comparing healthy and asthma-related samples and examining differences in gene expression.

RNA-Seq vs Microarray
Feature	RNA-Seq	Microarray
Main principle	Sequencing	Probe hybridization
Output	Sequencing reads → expression measurements	Probe signal → expression measurements
Data size	Usually large	Generally smaller
Dependence on predefined probes	Lower	Higher
Computational requirements	Usually higher	Usually lower
Transcript discovery	Can provide broader transcript information	Limited to probes represented on the array
Common downstream analysis	Differential expression, transcript analysis	Differential expression
Public datasets	Available in repositories such as GEO	Widely available in GEO

The comparison above is a conceptual overview. Actual performance depends on the experimental platform, study design, sequencing depth, sample quality, and analysis method.

Normalization

Expression measurements can be affected by technical factors.

For example, two samples may have different overall signal or sequencing depth even when their biological expression patterns are similar.

Normalization methods are therefore used to make samples more comparable.

A simplified idea is:

Raw measurements
       ↓
Normalization
       ↓
Comparable expression values
       ↓
Statistical analysis

Normalization is an important part of transcriptomic data analysis because downstream statistical comparisons depend on the quality and comparability of the input data.

Differential Gene Expression

One major application of both RNA-Seq and microarray data is differential gene expression (DGE) analysis.

The goal is to identify genes whose expression differs between two or more biological conditions.

For example:

Healthy samples
       ↓
Gene-expression measurements
       ↓
        VS
       ↓
Asthma samples
       ↓
Gene-expression measurements
       ↓
Statistical comparison
       ↓
Differentially expressed genes

Common quantities considered include:

Fold change
Log2 fold change
p-value
Adjusted p-value
Fold Change

Fold change describes how much the expression level changes between two conditions.

For example:

Condition A = 100
Condition B = 200

Fold change = 200 / 100 = 2

This represents a two-fold increase.

Log2 Fold Change

Gene-expression studies frequently use log2-transformed fold change.

The relationship is:

log2FC = log2(Fold Change)

Examples:

Fold Change	log2FC
0.25	-2
0.5	-1
1	0
2	1
4	2

Therefore:

Positive log2FC → higher expression in the selected comparison group.
Negative log2FC → lower expression in the selected comparison group.
log2FC = 0 → no fold-change difference.

The interpretation also depends on which group was defined as the reference.

Statistical Significance

A gene may show a large expression difference, but statistical testing is needed to determine whether the observed difference is supported by the data.

A p-value is commonly used in hypothesis testing.

However, transcriptomic experiments can involve thousands of genes. Testing thousands of hypotheses creates a multiple-testing problem.

Therefore, adjusted p-values are commonly used.

Adjusted P-Value

An adjusted p-value accounts for multiple statistical comparisons.

In transcriptomic analysis, adjusted p-values are often used when filtering significant genes.

A simplified workflow is:

Expression data
      ↓
Statistical testing
      ↓
P-values
      ↓
Multiple-testing correction
      ↓
Adjusted p-values
      ↓
Significant gene selection

In the asthma case study, adjusted p-values and log2 fold-change values were considered when identifying differentially expressed genes.

Microarray Analysis Using GEO2R

GEO2R is a web-based analysis interface associated with GEO that can be used to compare gene-expression data between groups in suitable GEO datasets.

A simplified workflow is:

GEO dataset
    ↓
Select samples/groups
    ↓
GEO2R analysis
    ↓
Statistical comparison
    ↓
Gene-expression results
    ↓
Adjusted p-value + log2FC
    ↓
Filter significant genes
    ↓
Functional analysis

For the internship case study, GEO2R was used with the asthma-related dataset GSE43696.

The resulting gene list was subsequently used for downstream functional and network analyses.

From Expression Data to Biological Interpretation

Transcriptomic analysis does not end after obtaining a list of differentially expressed genes.

The next question is:

What do these genes actually mean biologically?

A typical analysis can therefore proceed as:

Expression Dataset
       ↓
Differential Expression
       ↓
Differentially Expressed Genes
       ↓
Gene Ontology
       ↓
KEGG / Pathway Analysis
       ↓
Protein-Protein Interaction Analysis
       ↓
Network Visualization
       ↓
Hub-Gene Analysis
       ↓
Biological Interpretation

This was an important part of the internship because the analysis connected computational results with biological interpretation.

RNA-Seq and Microarray in Research

Both technologies have contributed significantly to gene-expression research.

A researcher may select one approach depending on factors such as:

Research question
Available samples
Experimental design
Existing datasets
Required resolution
Available computational resources
Cost
Compatibility with previous studies

There is therefore no single workflow that applies to every transcriptomic experiment.

Important Differences in Data Analysis

Although RNA-Seq and microarray experiments both produce gene-expression information, their upstream data-processing steps differ.

A simplified comparison is:

RNA-Seq

RNA
 ↓
Library preparation
 ↓
Sequencing
 ↓
Reads
 ↓
Quality control
 ↓
Alignment / quantification
 ↓
Expression matrix
 ↓
Differential expression
Microarray

RNA
 ↓
Target preparation
 ↓
Hybridization
 ↓
Microarray scanning
 ↓
Probe signals
 ↓
Expression matrix
 ↓
Differential expression

After the expression matrix has been obtained, many downstream concepts are shared.

For example:

Expression Matrix
       ↓
Normalization / preprocessing
       ↓
Differential Expression
       ↓
Gene List
       ↓
GO / KEGG
       ↓
PPI / Network Analysis
Practical Learning During the Internship

During the internship, transcriptomics was studied as a major component of bioinformatics analysis.

The training included concepts related to:

Transcriptomics
RNA sequencing
Microarray analysis
Gene-expression analysis
GEO datasets
GEO2R
Differential gene expression
Adjusted p-values
Log2 fold change
Functional enrichment
Network-based interpretation

The practical asthma case study focused on a publicly available microarray dataset from GEO. GEO2R was used to compare the selected sample groups, followed by filtering of differentially expressed genes and downstream functional and network analysis.

RNA-Seq was studied as part of the transcriptomics concepts and workflow; the internship work should not be interpreted as a full raw RNA-Seq pipeline unless explicitly documented elsewhere in this repository.

Common Terms
Term	Meaning
Transcriptome	Complete set of RNA transcripts in a biological system under a particular condition
RNA-Seq	Sequencing-based method for studying RNA/transcript expression
Read	A sequence generated by a sequencing instrument
Microarray	Probe-based technology for measuring expression of many genes
Probe	Sequence designed to detect a complementary target
Expression matrix	Table containing expression measurements for genes across samples
Normalization	Processing used to make measurements more comparable
Fold change	Ratio describing expression difference between conditions
log2FC	Log2-transformed fold change
p-value	Measure used in statistical hypothesis testing
Adjusted p-value	P-value corrected for multiple testing
DEG	Differentially expressed gene
GEO	Gene Expression Omnibus
GEO2R	GEO-based interface for comparing gene-expression groups
Key Takeaways
RNA-Seq is a sequencing-based approach for studying RNA and gene expression.
Microarrays measure gene expression using predefined probes.
Both approaches can produce expression matrices for downstream analysis.
Normalization is important for making samples comparable.
Differential expression analysis identifies genes whose expression differs between conditions.
Log2 fold change describes the direction and magnitude of expression change.
Adjusted p-values help account for multiple statistical tests.
GEO provides access to many publicly available transcriptomic datasets.
GEO2R can be used to compare groups within suitable GEO datasets.
The asthma case study used the GEO dataset GSE43696 and microarray-based gene-expression data.
Transcriptomic analysis can be extended from differentially expressed genes to functional enrichment, pathways, PPI networks, and hub-gene analysis.
RNA-Seq and microarray have different experimental principles and upstream processing steps, even though several downstream analytical concepts are shared.
Summary

RNA-Seq and microarray are two major approaches for studying gene expression. RNA-Seq generates sequencing reads that are computationally processed to obtain transcript or gene-expression measurements, while microarrays use predefined probes to measure expression through hybridization-based signals.

Understanding the difference between these technologies is important when working with public transcriptomic datasets. In the internship, these concepts formed the foundation for the later asthma transcriptomics case study, where a GEO microarray dataset was analyzed using GEO2R and the resulting differentially expressed genes were taken forward for functional and network-based interpretation.
