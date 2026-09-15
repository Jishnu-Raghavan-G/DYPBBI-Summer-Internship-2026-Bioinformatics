# Transcriptomics

## Introduction

Transcriptomics is the study of the complete set of RNA transcripts produced by a cell, tissue, or organism under a particular condition.

The collection of RNA molecules present at a particular time is called the **transcriptome**.

While genomics mainly focuses on the DNA sequence, transcriptomics focuses on **gene expression at the RNA level**.

During my Bioinformatics Summer Internship, transcriptomics was an important part of the computational workflow. The practical work included exploration of publicly available gene-expression data, GEO datasets, GEO2R, differential gene expression and downstream functional analysis.

---

## What is the Transcriptome?

The transcriptome represents the RNA molecules produced from the genome under a particular biological condition.

It can include:

- Messenger RNA (mRNA)
- Ribosomal RNA (rRNA)
- Transfer RNA (tRNA)
- MicroRNA (miRNA)
- Long non-coding RNA (lncRNA)
- Other non-coding RNAs

The transcriptome is dynamic.

It can change depending on:

- Cell type
- Tissue type
- Developmental stage
- Disease condition
- Environmental conditions
- Drug treatment
- Cellular state

Therefore, two cells with essentially the same genome can have very different transcriptomes.

---

## Transcriptomics and the Central Dogma

A simplified view of biological information flow is:

```text
DNA
 ↓
RNA
 ↓
Protein
 ↓
Cellular Function

Transcriptomics primarily investigates the RNA stage.

Genome
  ↓
Transcription
  ↓
Transcriptome
  ↓
Translation
  ↓
Proteome

The genome tells us what genetic information is present.

The transcriptome gives information about which genes are being expressed under a particular condition.

Gene Expression

Gene expression refers to the process through which information stored in a gene is used to produce a functional product.

For protein-coding genes:

DNA
 ↓
Transcription
 ↓
RNA
 ↓
Translation
 ↓
Protein

The amount of transcript produced from a gene can be used as an indicator of its expression level.

However, RNA abundance does not always directly correspond to protein abundance because regulation can occur at multiple stages.

Why Study Gene Expression?

Gene expression analysis can help answer questions such as:

Which genes are active?
Which genes are expressed at higher levels?
Which genes are expressed at lower levels?
Which genes change between healthy and diseased conditions?
Which biological processes are affected?
Which pathways may be involved?

For example:

Healthy Samples
      ↓
Gene Expression Profile
      ↓
       VS
      ↓
Disease Samples
      ↓
Gene Expression Profile
      ↓
Identify Expression Changes
Transcriptome is Condition-Dependent

Gene expression is not constant.

The same gene can have different expression levels depending on the biological context.

For example:

Same Gene
   │
   ├── Healthy condition → Low expression
   │
   ├── Disease condition → High expression
   │
   └── Drug-treated condition → Moderate expression

This is one of the reasons transcriptomics is useful in disease research.

Types of RNA
Messenger RNA (mRNA)

mRNA carries genetic information from DNA that can be translated into proteins.

It is one of the major RNA molecules studied in gene-expression analysis.

Ribosomal RNA (rRNA)

rRNA forms an important structural and functional component of ribosomes.

Transfer RNA (tRNA)

tRNA carries amino acids to the ribosome during protein synthesis.

MicroRNA (miRNA)

miRNAs are small non-coding RNAs that can regulate gene expression.

Long Non-Coding RNA (lncRNA)

lncRNAs are relatively long RNA molecules that generally do not code for proteins and can have regulatory functions.

Coding and Non-Coding RNA

RNA molecules can broadly be classified into coding and non-coding RNA.

RNA
│
├── Coding RNA
│      └── mRNA
│
└── Non-Coding RNA
       ├── miRNA
       ├── lncRNA
       ├── rRNA
       └── tRNA

The transcriptome therefore contains much more information than only protein-coding mRNA.

Measuring Gene Expression

Gene expression can be studied using several technologies.

Two major approaches discussed during the internship were:

Microarray

Microarrays use probes to measure the abundance of specific transcripts.

RNA Sequencing

RNA-seq uses sequencing technology to generate reads from RNA-derived molecules and quantify transcript abundance.

Both technologies can generate large-scale gene-expression datasets for computational analysis.

Microarray
Basic Principle

A microarray contains many probes designed to recognize specific nucleic-acid sequences.

A simplified workflow is:

Biological Sample
      ↓
RNA Isolation
      ↓
cDNA Preparation
      ↓
Labeling
      ↓
Hybridization
      ↓
Microarray
      ↓
Signal Detection
      ↓
Expression Data

The resulting signal intensity provides information about the relative abundance of transcripts represented on the array.

Microarray Data

Microarray experiments can produce an expression matrix.

A simplified example:

Gene	Sample 1	Sample 2	Sample 3
Gene A	8.2	8.7	8.4
Gene B	3.1	3.4	3.0
Gene C	6.5	6.1	6.7

Each row represents a gene or probe.

Each column represents a biological sample.

The values represent measured expression levels.

RNA Sequencing
Basic Principle

RNA sequencing, commonly called RNA-seq, uses sequencing technology to study RNA molecules.

A simplified workflow is:

Biological Sample
      ↓
RNA Isolation
      ↓
RNA Processing
      ↓
Library Preparation
      ↓
Sequencing
      ↓
Raw Reads
      ↓
Quality Control
      ↓
Alignment / Quantification
      ↓
Expression Matrix
      ↓
Differential Expression

The exact workflow can vary depending on the experimental design and analysis pipeline.

RNA-seq Reads

Sequencing produces short or long sequence fragments called reads.

These reads contain sequence information derived from RNA molecules.

Computational analysis can then determine which genes or transcripts the reads correspond to and estimate their abundance.

Conceptually:

RNA
 ↓
Sequencing
 ↓
Reads
 ↓
Alignment / Quantification
 ↓
Gene Expression
Microarray vs RNA-seq
Feature	Microarray	RNA-seq
Basic principle	Probe hybridization	Sequencing
Main output	Signal/intensity values	Sequencing reads and counts
Predefined probes	Required	Not required in the same way
Novel transcript detection	Limited	Better potential
Data processing	Probe-based	Read-based
Computational complexity	Generally lower	Generally higher

Neither technology should simply be considered universally "better"; the appropriate method depends on the research question, experimental design, available resources and study requirements.

Public Gene Expression Data

Modern biological research produces very large quantities of gene-expression data.

Instead of generating every dataset from scratch, researchers can use publicly available datasets.

One important resource explored during the internship was the NCBI Gene Expression Omnibus (GEO).

GEO contains publicly available gene-expression datasets from different biological studies.

A researcher can use these datasets to:

Explore gene expression
Reproduce analyses
Compare biological conditions
Generate research hypotheses
Learn computational workflows
GEO and Transcriptomics

A simplified GEO-based workflow is:

Research Question
      ↓
Search GEO
      ↓
Select Dataset
      ↓
Study Sample Information
      ↓
Obtain Expression Data
      ↓
Perform Analysis
      ↓
Interpret Results

Dataset metadata is important because expression values cannot be interpreted correctly without understanding:

Sample groups
Tissue or organism
Experimental conditions
Treatment
Disease status
Technology used
GEO2R

GEO2R is a web-based analysis interface associated with GEO.

It can be used to compare gene-expression profiles between selected groups of samples.

For example:

Group 1
Healthy
   ↓
   VS
   ↓
Group 2
Asthma

GEO2R can then be used to identify genes whose expression differs between the selected groups.

Differential Gene Expression

Differential gene expression analysis identifies genes whose expression differs between biological conditions.

For example:

Healthy
   ↓
Expression Data
   ↓
       Comparison
   ↓
Asthma
   ↓
Expression Data
   ↓
Differentially Expressed Genes

The resulting genes may be:

Upregulated
Downregulated
Not significantly changed
Upregulation

A gene is described as upregulated when its expression is higher in one condition relative to the reference condition.

Example:

Healthy → 5 units
Disease → 20 units

Expression increased
→ Gene is upregulated in Disease

The direction always depends on which group is used as the reference.

Downregulation

A gene is described as downregulated when its expression is lower in one condition relative to the reference condition.

Example:

Healthy → 20 units
Disease → 5 units

Expression decreased
→ Gene is downregulated in Disease
Fold Change

Fold change describes the relative change in expression between two conditions.

For example:

Control = 5
Disease = 20

Fold Change = 20 / 5
            = 4

The gene has approximately four times the expression in the disease group compared with the control group.

Log2 Fold Change

Gene-expression studies commonly use the logarithm base 2 of fold change.

Conceptually:

log2FC = log2(Disease / Control)

Examples:

2-fold increase
→ log2FC = +1

4-fold increase
→ log2FC = +2

2-fold decrease
→ log2FC = -1

4-fold decrease
→ log2FC = -2

Therefore:

Positive log2FC → Higher expression
Negative log2FC → Lower expression
log2FC ≈ 0       → Little expression change
P-Value

A p-value is a statistical measure used to assess how compatible an observed result is with a specified null hypothesis.

In differential expression analysis, p-values help determine whether an observed difference in expression is statistically significant.

However, transcriptomic experiments usually test thousands of genes simultaneously.

This creates a multiple-testing problem.

Adjusted P-Value

When thousands of genes are tested, some genes may appear significant simply by chance.

Therefore, statistical correction is applied.

The resulting value is often called an adjusted p-value.

A common approach is controlling the false discovery rate (FDR).

For transcriptomic analysis:

Thousands of Genes
       ↓
Statistical Testing
       ↓
Multiple Testing Correction
       ↓
Adjusted P-values
       ↓
Significant Genes
Statistical Filtering

Differentially expressed genes can be filtered using statistical and biological criteria.

A simplified workflow is:

All Analysed Genes
       ↓
Differential Expression
       ↓
Adjusted P-value Filter
       ↓
Log2 Fold Change Filter
       ↓
Significant Gene List

The exact thresholds should be chosen according to the study design and research objective.

Biological Replicates

Biological replicates are independent biological samples representing the same experimental condition.

For example:

Healthy
├── Sample 1
├── Sample 2
├── Sample 3
└── Sample 4

Disease
├── Sample 1
├── Sample 2
├── Sample 3
└── Sample 4

Replicates help researchers estimate biological variation and improve the reliability of statistical comparisons.

Normalization

Expression measurements can contain technical differences between samples.

Normalization attempts to reduce unwanted technical variation so that samples can be compared more appropriately.

Conceptually:

Raw Expression Data
        ↓
Normalization
        ↓
More Comparable Samples
        ↓
Downstream Analysis

Normalization methods differ between technologies and analysis pipelines.

Heatmaps

A heatmap is a visual representation of gene-expression values.

A simplified structure is:

             Samples
          S1   S2   S3   S4
Gene A    ██   ██   ░░   ░░
Gene B    ░░   ░░   ██   ██
Gene C    ██   ██   ██   ░░

Heatmaps can help identify patterns of expression across samples.

They are particularly useful for visually examining groups of genes and samples.

Volcano Plots

A volcano plot is commonly used to visualize differential gene expression.

It generally combines:

Fold change
Statistical significance

Conceptually:

             Significant
                genes
                 ↑
                 │  •
                 │ • •
                 │•
─────────────────┼─────────────────→ log2 Fold Change
               • │ •
              •  │
                 ↓

Genes with large expression changes and strong statistical significance tend to appear toward the upper left or upper right regions.

From Differential Expression to Functional Analysis

Identifying significant genes is not the final step.

The next question is:

What do these genes actually do?

This leads to functional enrichment and pathway analysis.

Differentially Expressed Genes
            ↓
       Gene Ontology
            ↓
       KEGG Pathways
            ↓
        g:Profiler
            ↓
     Functional Meaning

The results can then be connected with protein interaction analysis.

Functional Analysis
        ↓
STRING
        ↓
Protein–Protein Interactions
        ↓
Cytoscape
        ↓
Network Analysis
Asthma Transcriptomics Case Study

A major practical component of the internship involved publicly available asthma transcriptomic data.

The GEO accession used was:

GSE43696

The dataset was explored through GEO and analyzed using GEO2R.

The simplified workflow was:

GEO
 ↓
GSE43696
 ↓
GEO2R
 ↓
Healthy vs Asthma Samples
 ↓
Differential Gene Expression
 ↓
Statistical Filtering
 ↓
Significant Genes
 ↓
Functional Analysis

The selected genes were subsequently taken forward for functional and network analysis.

Complete Transcriptomics Workflow

The concepts learned during the internship can be connected into one workflow:

Biological Question
        ↓
Public Gene Expression Dataset
        ↓
GEO
        ↓
Dataset and Sample Exploration
        ↓
GEO2R
        ↓
Differential Gene Expression
        ↓
Statistical Filtering
        ↓
Significant Genes
        ↓
┌───────────┬────────────┬──────────────┐
↓           ↓            ↓
GO         KEGG       g:Profiler
└───────────┴────────────┴──────────────┘
        ↓
Functional Interpretation
        ↓
STRING PPI
        ↓
Cytoscape
        ↓
Network Analysis
        ↓
Biological Interpretation

This demonstrates how transcriptomics can connect gene-expression data with functional and systems-level analysis.

Important Concepts
Concept	Meaning
Transcriptome	Complete set of RNA transcripts under a particular condition
Transcriptomics	Study of the transcriptome
Gene expression	Production of RNA or other functional gene products
Microarray	Probe-based gene-expression technology
RNA-seq	Sequencing-based transcriptomic technology
GEO	Public repository for gene-expression datasets
GEO2R	Interface for comparing selected GEO sample groups
Differential expression	Identification of genes with expression differences
Fold change	Relative change in expression
log2FC	Logarithm base 2 of fold change
P-value	Measure used in statistical hypothesis testing
Adjusted p-value	P-value corrected for multiple testing
Normalization	Processing used to reduce unwanted technical variation
Functional enrichment	Identification of biological categories overrepresented in a gene set
Key Takeaways
Transcriptomics studies RNA expression across biological systems.
The transcriptome is dynamic and changes with biological conditions.
Microarrays and RNA-seq are major transcriptomic technologies.
GEO provides publicly available gene-expression datasets.
GEO2R can be used to compare selected sample groups.
Differential gene expression identifies genes whose expression differs between conditions.
Positive log2FC generally indicates increased expression in the comparison group, while negative log2FC indicates decreased expression.
Multiple-testing correction is important because thousands of genes can be tested simultaneously.
Significant genes can be investigated using GO, KEGG and g:Profiler.
Network analysis can then be performed using resources such as STRING and Cytoscape.
The internship applied this workflow to the asthma transcriptomics dataset GSE43696.
Final Concept

The most important idea from transcriptomics is that the analysis should not stop at:

"This gene changed."

The goal is to move from:

Gene Expression
      ↓
Differentially Expressed Genes
      ↓
Functional Categories
      ↓
Pathways
      ↓
Interaction Networks
      ↓
Biological Meaning

This is what makes transcriptomic analysis useful for understanding complex biological conditions.
