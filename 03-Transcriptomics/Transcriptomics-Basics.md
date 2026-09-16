# Transcriptomics Basics

Transcriptomics is the study of the complete set of RNA molecules produced by a cell, tissue, or organism under a particular condition.

During the internship, I learned transcriptomics as a way of connecting changes in gene expression with biological conditions. The topic became especially useful later when working with public gene-expression data from GEO and comparing healthy and disease samples.

## What Is a Transcriptome?

The **transcriptome** is the collection of RNA transcripts present in a biological sample at a particular time and under particular conditions.

Unlike the genome, which is relatively stable, the transcriptome can change depending on factors such as:

- Cell type
- Developmental stage
- Disease condition
- Environmental conditions
- Treatment
- Cellular state

For this reason, transcriptomic data can provide information about what genes are actively being expressed in a biological system.

## Genome vs Transcriptome

The genome contains the complete genetic information of an organism.

The transcriptome represents the RNA molecules produced from that genetic information.

A simple comparison is:

```text
Genome
  ↓
Genetic information
  ↓
Transcription
  ↓
RNA transcripts
  ↓
Transcriptome

The genome gives the potential genetic information, while the transcriptome provides a snapshot of gene activity under a particular condition.

From DNA to RNA

Gene expression begins when information stored in DNA is transcribed into RNA.

The basic relationship can be represented as:

DNA
 ↓
Transcription
 ↓
RNA
 ↓
Translation
 ↓
Protein

Not every RNA molecule is translated into a protein. Many RNA molecules perform regulatory or structural functions.

Types of RNA

RNA is not a single type of molecule.

Some important types include:

Messenger RNA

mRNA carries information from DNA that can be used for protein synthesis.

It is one of the main RNA molecules considered when studying protein-coding gene expression.

Ribosomal RNA

rRNA forms an important structural and functional component of ribosomes.

Transfer RNA

tRNA helps deliver amino acids during protein synthesis.

Non-Coding RNA

Many RNA molecules do not directly encode proteins.

Examples include:

microRNA (miRNA)
long non-coding RNA (lncRNA)
small nuclear RNA (snRNA)

These molecules can have regulatory and structural roles.

Gene Expression

Gene expression refers to the process through which information from a gene is used to produce a functional product.

For protein-coding genes, this generally involves:

DNA
 ↓
RNA
 ↓
Protein

The amount of RNA produced from a gene can vary between different biological conditions.

For example:

Healthy sample
     ↓
Gene X expression = lower

Disease sample
     ↓
Gene X expression = higher

This difference can become an interesting starting point for further biological investigation.

Why Study Gene Expression?

Gene expression analysis can help researchers investigate questions such as:

Which genes change between healthy and disease conditions?
Which genes respond to a treatment?
Which biological processes are active?
Which pathways may be associated with a condition?
Which genes show similar expression patterns?

However, an expression difference by itself does not establish that a gene causes a disease. It is evidence that can be investigated further.

Transcriptomic Data

Transcriptomic experiments produce numerical data representing RNA abundance or gene-expression measurements.

A simplified expression matrix can look like this:

Gene	Sample 1	Sample 2	Sample 3	Sample 4
Gene A	12.4	13.1	11.8	20.3
Gene B	5.2	5.7	5.4	4.9
Gene C	18.1	17.6	19.0	30.2

The rows represent genes and the columns represent samples.

In a real experiment, the matrix may contain thousands of genes and many samples.

Biological Replicates

Biological replicates are independent biological samples representing the same experimental condition.

For example:

Healthy
 ├── Healthy 1
 ├── Healthy 2
 └── Healthy 3

Disease
 ├── Disease 1
 ├── Disease 2
 └── Disease 3

Replicates are important because biological measurements naturally vary.

Looking at only one sample from each group would make it difficult to distinguish a true biological pattern from random variation.

Microarray

Microarray technology is one approach used to measure the expression of many genes simultaneously.

A microarray contains probes designed to detect specific nucleic-acid sequences.

A simplified workflow is:

RNA from biological samples
          ↓
Sample preparation
          ↓
Hybridisation to array probes
          ↓
Signal detection
          ↓
Expression measurements

The resulting measurements can be used to compare gene expression between groups.

RNA Sequencing

RNA sequencing, commonly called RNA-seq, uses sequencing technology to study RNA molecules.

A simplified workflow is:

RNA
 ↓
Library preparation
 ↓
Sequencing
 ↓
Sequence reads
 ↓
Quality control
 ↓
Alignment / quantification
 ↓
Expression matrix
 ↓
Differential expression

RNA-seq can provide a broad view of the transcriptome and is not limited to the predefined probes used in a traditional microarray.

Microarray vs RNA-seq

Both approaches can be used for transcriptomic studies, but their experimental principles are different.

Feature	Microarray	RNA-seq
Basic principle	Probe-based detection	Sequencing-based measurement
Input	RNA	RNA
Output	Probe-associated expression signals	Sequencing reads and derived expression measurements
Known targets	Generally requires predefined probes	Can detect a wider range of transcripts
Data processing	Array-specific workflow	Sequencing and computational workflow
Typical analysis	Expression comparison	Read processing, quantification, expression comparison

The choice of technology depends on the biological question, experimental design, available resources, and required resolution.

Public Transcriptomic Data

Transcriptomic experiments generate large datasets that can be deposited in public repositories.

One important resource introduced during the internship was the NCBI Gene Expression Omnibus (GEO).

GEO contains publicly available functional genomics data, including gene-expression datasets.

The basic idea is:

Published experiment
       ↓
Public database
       ↓
GEO dataset
       ↓
Download / explore data
       ↓
Computational analysis

This makes publicly available experiments useful for learning, exploratory analysis, and research.

GEO Accession Numbers

GEO datasets are identified using accession numbers.

For example:

GSE43696

was the GEO dataset used in the asthma transcriptomics case study during the internship.

The dataset was explored through GEO and analysed using GEO2R to compare healthy and disease-related samples.

GEO2R

GEO2R is a web-based analysis interface associated with GEO.

It allows users to compare groups of samples within a GEO dataset and examine differences in gene expression.

A simplified workflow is:

GEO dataset
     ↓
Select samples
     ↓
Create comparison groups
     ↓
Run GEO2R
     ↓
Differential-expression results
     ↓
Inspect significant genes

GEO2R became an important part of the transcriptomics case study because it provided a practical introduction to differential gene-expression analysis.

Differential Gene Expression

Differential gene expression refers to identifying genes whose measured expression differs between two or more biological conditions.

For example:

Healthy             Disease

Gene A = 5          Gene A = 5.2
Gene B = 8          Gene B = 18
Gene C = 12         Gene C = 4

Gene B shows an increase in expression.

Gene C shows a decrease.

Gene A shows relatively little change.

The statistical analysis helps determine whether observed differences are supported by the data.

Fold Change

Fold change describes the relative difference in expression between two conditions.

A simplified calculation is:

Fold Change =
Expression in comparison group
--------------------------------
Expression in reference group

For example:

Reference expression = 10
Comparison expression = 20

Fold Change = 20 / 10
            = 2

This represents a two-fold increase.

Log2 Fold Change

Large fold-change values can be easier to interpret after logarithmic transformation.

The commonly used measure is:

log2 Fold Change

Examples:

Fold Change = 2
log2FC = +1

Fold Change = 4
log2FC = +2

Fold Change = 0.5
log2FC = -1

The positive and negative values make increases and decreases easier to compare.

P-Value

A p-value is a statistical quantity used when testing a hypothesis.

In differential-expression analysis, it helps assess the evidence against the null hypothesis that there is no difference between the groups under the statistical model being used.

A small p-value can provide evidence of a difference, but it does not by itself describe the biological importance of that difference.

Adjusted P-Value

Transcriptomic experiments can involve thousands of genes.

If each gene is tested separately, some genes may appear significant simply by chance.

Therefore, multiple-testing correction is important.

The internship analysis used adjusted p-values together with log2 fold change when filtering differential-expression results.

One commonly used approach is controlling the false discovery rate (FDR).

Statistical Significance vs Biological Significance

These two ideas should not be treated as identical.

Statistical significance

Addresses whether the observed result has sufficient statistical evidence under the chosen analysis.

Biological significance

Addresses whether the observed change has meaningful biological implications.

For example, a very small expression change may become statistically significant in a sufficiently large dataset, while a larger change may require more evidence if the data are highly variable.

Therefore, interpretation should consider both statistical evidence and biological context.

Normalization

Expression measurements can be affected by technical differences between samples.

Normalization is used to make measurements more comparable by accounting for systematic technical differences.

The exact normalization procedure depends on the experimental platform and analysis method.

For example:

Raw measurements
       ↓
Quality control
       ↓
Normalization
       ↓
Comparable expression data
       ↓
Statistical analysis

Normalization is an important part of transcriptomic data analysis and should not be skipped when working with raw experimental data.

Heatmaps

A heatmap is a visual representation of numerical values using different levels of visual intensity.

In transcriptomics, heatmaps are commonly used to examine expression patterns across genes and samples.

A simplified structure is:

             Samples
          S1   S2   S3   S4

Gene A    ▓    ▓▓   ▓    ▓▓▓
Gene B    ▓▓▓  ▓▓   ▓▓▓  ▓
Gene C    ▓    ▓    ▓▓   ▓▓▓

Heatmaps can make groups or expression patterns easier to inspect.

Volcano Plots

A volcano plot combines:

magnitude of expression change
statistical significance

A typical plot uses:

X-axis → log2 Fold Change

Y-axis → -log10(p-value or adjusted p-value)

Genes with large expression changes and strong statistical evidence appear farther from the centre and higher on the plot.

Volcano plots are useful for quickly exploring differential-expression results.

From Genes to Biological Meaning

Finding differentially expressed genes is usually not the end of the analysis.

The next question is:

What do these genes mean biologically?

A common progression is:

Differentially Expressed Genes
            ↓
Gene Ontology
            ↓
KEGG Pathways
            ↓
g:Profiler
            ↓
Protein-Protein Interactions
            ↓
STRING
            ↓
Cytoscape
            ↓
Network Interpretation

This progression was part of the broader internship workflow, where selected genes were taken from differential-expression analysis into functional enrichment and PPI/network analysis.

Transcriptomics in Disease Research

Transcriptomic analysis can be used to investigate molecular differences associated with diseases.

In the internship, asthma was used as the main transcriptomics case study.

The general workflow was:

Asthma-related biological question
              ↓
Public GEO dataset
              ↓
GSE43696
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
              ↓
Functional and Network Analysis

This case study is documented separately in:

04-Asthma-Transcriptomics-Case-Study/
What I Took Away From This Topic

The most useful concept for me was understanding that transcriptomics is not simply about producing a list of genes.

The analysis becomes more meaningful when the expression results are connected to biological functions and pathways.

The progression can be viewed as:

Expression Data
      ↓
Differentially Expressed Genes
      ↓
Functions
      ↓
Pathways
      ↓
Protein Interactions
      ↓
Biological Interpretation

This helped me understand how computational analysis can be connected back to an actual biological question.

Summary

Transcriptomics provides a way to study RNA-level changes across biological conditions.

The important concepts covered in this section are:

Transcriptome
Gene expression
RNA types
Microarray
RNA-seq
Expression matrices
Biological replicates
GEO
GEO2R
Differential gene expression
Fold change
log2 fold change
P-values
Adjusted p-values
Multiple testing
Normalization
Heatmaps
Volcano plots
Functional interpretation

These concepts form the foundation for the more practical analysis carried out later in the asthma transcriptomics case study.
