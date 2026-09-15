# 03 — Transcriptomics

## Introduction

Transcriptomics is the study of the complete set of RNA transcripts produced by cells or tissues under a particular biological condition.

It provides information about **gene expression** and helps researchers understand which genes are active, how strongly they are expressed, and how their expression changes between different conditions.

During the internship, transcriptomics was studied as an important application of bioinformatics, with particular emphasis on gene expression analysis, microarray data, RNA-seq concepts, GEO datasets, GEO2R, and differential gene expression.

---

## Topics Covered

This section covers:

- Transcriptomics fundamentals
- Gene expression
- RNA-seq
- Microarray technology
- Gene expression datasets
- GEO and public transcriptomic data
- GEO2R
- Differential gene expression
- Statistical filtering
- Biological interpretation of gene expression results

---

## What is Transcriptomics?

The **transcriptome** is the complete collection of RNA molecules produced by a cell, tissue, or organism under specific conditions.

The transcriptome can change depending on factors such as:

- Cell type
- Developmental stage
- Disease condition
- Environmental conditions
- Drug treatment
- Cellular state

Studying these changes allows researchers to investigate how gene activity changes under different biological conditions.

---

## Gene Expression

Gene expression refers to the process through which information encoded in genes is used to produce functional RNA or proteins.

A simplified representation is:

```text
DNA
 ↓
RNA
 ↓
Protein

Transcriptomics mainly focuses on the RNA level and therefore provides information about gene activity.

Why Study Gene Expression?

Comparing gene expression between two conditions can help identify genes whose expression changes.

For example:

Healthy Condition
       ↓
Gene Expression Profile
       ↓
       VS
       ↓
Disease Condition
       ↓
Gene Expression Profile

The differences between the two profiles can reveal genes that may be associated with the biological condition being studied.

Applications include:

Disease research
Biomarker discovery
Understanding disease mechanisms
Drug-response studies
Molecular classification
Precision medicine
Functional genomics
Major Transcriptomic Technologies

Two important technologies discussed during the internship were:

Microarray

Microarray technology measures the expression levels of many genes simultaneously using probes designed to detect specific sequences.

A simplified workflow is:

RNA
 ↓
Sample Preparation
 ↓
Hybridization to Probes
 ↓
Signal Detection
 ↓
Gene Expression Data

Microarrays were historically widely used for large-scale gene expression profiling.

RNA Sequencing

RNA sequencing (RNA-seq) uses sequencing technologies to study RNA molecules.

A simplified conceptual workflow is:

RNA
 ↓
RNA Preparation
 ↓
Library Preparation
 ↓
Sequencing
 ↓
Sequence Reads
 ↓
Read Processing
 ↓
Gene / Transcript Quantification
 ↓
Differential Expression

RNA-seq can provide information about expressed transcripts and their abundance.

During the internship, RNA-seq was studied at the conceptual level alongside microarray-based transcriptomics.

Microarray vs RNA-seq
Feature	Microarray	RNA-seq
Basic principle	Probe-based detection	Sequencing-based detection
Main output	Expression measurements	Sequence reads and expression information
Requires predefined probes	Yes	No in the same way
Transcript discovery	More limited	Can identify previously unannotated transcripts
Data analysis	Probe/intensity based	Read/alignment/count based

Both technologies are useful for studying gene expression, although their experimental designs and computational workflows differ.

Public Transcriptomic Data

Large amounts of transcriptomic data are publicly available through biological databases.

One important resource explored during the internship was the NCBI Gene Expression Omnibus (GEO).

GEO contains publicly available gene expression datasets that can be used for computational research and learning.

A typical workflow is:

Public Dataset
      ↓
Dataset Exploration
      ↓
Sample Information
      ↓
Gene Expression Data
      ↓
Statistical Analysis
      ↓
Biological Interpretation
GEO2R

GEO2R is a web-based tool associated with GEO that can be used to compare gene expression between groups of samples.

For example:

Group 1 → Healthy
Group 2 → Disease

GEO2R can then be used to identify genes whose expression differs between the selected groups.

The resulting information can be used for downstream differential gene expression analysis.

Differential Gene Expression

Differential gene expression analysis identifies genes whose expression differs between biological conditions.

For example:

Healthy Samples
       ↓
Gene Expression
       ↓
       VS
       ↓
Asthma Samples
       ↓
Gene Expression
       ↓
Differential Analysis
       ↓
Differentially Expressed Genes

Genes can show increased or decreased expression between the groups.

Upregulated and Downregulated Genes
Upregulated

A gene is considered upregulated when its expression is higher in one condition compared with the reference condition.

Condition A → Lower expression
Condition B → Higher expression

Result → Upregulated in Condition B
Downregulated

A gene is considered downregulated when its expression is lower in one condition compared with the reference condition.

Condition A → Higher expression
Condition B → Lower expression

Result → Downregulated in Condition B

The direction of change depends on which group is used as the reference.

Log2 Fold Change

Fold change describes how much gene expression changes between two conditions.

A common transformation used in gene expression analysis is log2 fold change (log2FC).

Conceptually:

log2FC > 0
→ Higher expression in the comparison group

log2FC < 0
→ Lower expression in the comparison group

log2FC ≈ 0
→ Little or no expression difference

Using a logarithmic scale makes increases and decreases easier to compare.

Statistical Significance

A difference in gene expression does not automatically mean that the difference is statistically meaningful.

Statistical analysis is used to determine whether an observed difference is likely to represent a real biological difference rather than random variation.

Important measures can include:

P-value
Adjusted p-value
Log2 fold change

Because many genes are tested simultaneously, multiple-testing correction is important.

Statistical Filtering

After differential expression analysis, genes can be filtered using statistical and biological criteria.

A simplified approach is:

All Analysed Genes
       ↓
Statistical Testing
       ↓
Adjusted p-value Filtering
       ↓
Fold-change Filtering
       ↓
Significant Genes

The exact thresholds depend on the study design and research question.

Transcriptomics Workflow Used in the Internship

A major practical component of the internship involved publicly available asthma transcriptomic data.

The workflow was:

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

The selected genes were subsequently taken forward for functional and network analysis using resources such as Gene Ontology, KEGG, g:Profiler, STRING and Cytoscape.

From Transcriptomics to Biological Interpretation

Transcriptomic analysis is not limited to producing a list of genes.

The identified genes can be connected to downstream analyses:

Differentially Expressed Genes
             ↓
      Functional Enrichment
             ↓
      GO + KEGG + g:Profiler
             ↓
        Pathway Analysis
             ↓
         STRING PPI
             ↓
         Cytoscape
             ↓
      Network Interpretation

This allows gene-level changes to be interpreted in a broader biological context.

Importance in Disease Research

Transcriptomics can help researchers investigate molecular changes associated with diseases.

For example, comparing healthy and disease samples can help identify:

Disease-associated genes
Altered biological processes
Relevant pathways
Potential biomarkers
Candidate molecular targets
Gene expression signatures

However, computational associations require further biological interpretation and, where appropriate, experimental validation.

Key Takeaways
Transcriptomics studies the RNA transcriptome.
It is widely used to investigate gene expression.
Gene expression can vary between tissues, conditions and disease states.
Microarrays and RNA-seq are important transcriptomic technologies.
GEO provides access to publicly available gene expression datasets.
GEO2R can be used to compare expression between selected sample groups.
Differential expression analysis identifies genes with changed expression.
Log2 fold change describes the direction and magnitude of expression changes.
Adjusted p-values help account for multiple statistical tests.
Differentially expressed genes can be taken forward for functional, pathway and network analysis.
During the internship, transcriptomic concepts were applied to an asthma dataset, GSE43696.
Summary

Transcriptomics provides a way to study biological systems at the level of gene expression.

The internship demonstrated how publicly available transcriptomic data can be transformed into biologically meaningful information:

Public Transcriptomic Dataset
            ↓
       GEO / GEO2R
            ↓
Differential Gene Expression
            ↓
   Significant Gene List
            ↓
 Functional & Pathway Analysis
            ↓
 Biological Interpretation
