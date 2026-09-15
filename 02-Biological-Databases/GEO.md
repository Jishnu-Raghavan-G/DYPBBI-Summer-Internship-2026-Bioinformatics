# GEO — Gene Expression Omnibus

The Gene Expression Omnibus (GEO) is a public repository for gene expression and other functional genomics datasets. It is particularly useful in bioinformatics because researchers can access previously generated biological datasets and use them for computational analysis.

During the internship, GEO became especially important during the asthma transcriptomics case study, where the dataset **GSE43696** was explored and analysed using GEO2R.

## What is GEO?

GEO stands for **Gene Expression Omnibus**.

It is a public repository maintained by NCBI that provides access to gene expression datasets submitted from research studies.

These datasets can contain information generated using technologies such as:

- Microarrays
- High-throughput sequencing
- Other functional genomics approaches

The data can be used to study differences in gene expression between biological conditions.

## Why GEO Is Important

Generating biological datasets experimentally can require significant time, resources and biological samples.

Public repositories such as GEO allow researchers to reuse existing datasets for further analysis.

GEO can therefore be useful for:

- Exploring published gene expression studies
- Comparing biological conditions
- Identifying differentially expressed genes
- Studying disease-associated expression patterns
- Reanalysing publicly available datasets
- Supporting computational research and hypothesis generation

## GEO Dataset Structure

A GEO study contains more than just a table of gene expression values.

Important information may include:

- Study description
- Experimental design
- Biological samples
- Organism
- Experimental conditions
- Sample characteristics
- Platform information
- Gene expression measurements
- Associated publications

This information is important because gene expression values cannot be properly interpreted without understanding how the samples were obtained and compared.

## GEO Accession Numbers

GEO uses accession numbers to identify datasets and other records.

An accession number provides a convenient way to locate a particular study.

During my internship, the main GEO dataset used for the asthma transcriptomics case study was:

**GSE43696**

The accession number was used to locate the dataset and understand the associated experimental information before performing downstream analysis.

## Types of GEO Records

GEO contains different levels of records.

### GEO Series — GSE

A **GSE** record represents a study or series of related samples.

For example:

```text
GSE43696

was the study used in the asthma transcriptomics analysis.

GEO Sample — GSM

A GSM record represents an individual biological sample within a GEO study.

A single GSE study can therefore contain multiple GSM samples.

Simplified relationship:

GSE Study
   ↓
Multiple Samples
   ↓
GSM Records
GEO Platform — GPL

A GPL record represents the platform or technology used to generate the data.

The platform provides information about the experimental technology and associated gene/probe annotations.

Simplified relationship:

GSE
 ↓
GSM Samples
 ↓
GPL Platform

Understanding these different record types helps in navigating GEO correctly.

Exploring a GEO Dataset

Before beginning analysis, a GEO dataset should be examined carefully.

Important questions include:

What biological question was investigated?
Which organism was studied?
What type of samples were used?
How many samples are present?
What are the experimental groups?
Which technology was used?
What does the platform measure?
Is there an associated research publication?

This initial exploration helps determine whether the dataset is suitable for the intended analysis.

Gene Expression Data

Gene expression data describe the activity or abundance of gene transcripts under particular biological conditions.

For a disease study, samples may be divided into groups such as:

Healthy Samples
       vs
Disease Samples

The expression values can then be compared to identify genes whose expression differs between the groups.

GEO2R

GEO2R is an online analysis tool associated with GEO that allows users to compare groups of samples within selected GEO datasets.

A simplified workflow is:

GEO Dataset
     ↓
Select Samples
     ↓
Define Groups
     ↓
GEO2R
     ↓
Statistical Comparison
     ↓
Gene Expression Results

During the internship, GEO2R was used for the analysis of GSE43696.

Asthma Transcriptomics Example

The main practical use of GEO during my internship was the asthma transcriptomics case study.

The overall workflow was:

NCBI
  ↓
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

The resulting genes were then taken forward for functional and network analysis.

The detailed analysis is documented separately in:

04-Asthma-Transcriptomics/

Differential Gene Expression

One of the important applications of GEO datasets is differential gene expression analysis.

The basic idea is to determine whether particular genes show different expression levels between two or more biological conditions.

For example:

Healthy Group
      ↓
Gene Expression
      ↕
Comparison
      ↕
Gene Expression
      ↓
Disease Group

Genes showing meaningful differences can then be selected for further investigation.

Important measures encountered during the internship included:

Log₂ fold change
P-values
Adjusted p-values
Statistical significance

These measures help determine which observed expression differences are worth investigating further.

Log₂ Fold Change

Log₂ fold change describes the relative change in gene expression between two conditions on a logarithmic scale.

A positive value generally indicates higher expression in the selected comparison group, while a negative value indicates lower expression.

For example:

log₂FC > 0  → Higher expression
log₂FC < 0  → Lower expression
log₂FC = 0  → No expression change

The exact interpretation of the direction depends on which group is used as the reference and which group is being compared.

Adjusted P-Values

When thousands of genes are tested simultaneously, many statistical tests are performed.

This increases the possibility of obtaining apparently significant results by chance.

Adjusted p-values help account for multiple testing and provide a more appropriate basis for selecting statistically significant genes.

Therefore, differential expression results should not be interpreted using raw p-values alone.

From GEO to Biological Meaning

GEO provides the data, but the final goal is biological interpretation.

A simplified progression is:

GEO Dataset
      ↓
Expression Data
      ↓
Differentially Expressed Genes
      ↓
Functional Enrichment
      ↓
Pathway Analysis
      ↓
Protein–Protein Interactions
      ↓
Biological Interpretation

This demonstrates how a public dataset can become the starting point for a larger bioinformatics investigation.

Importance of Metadata

Metadata describes the biological and experimental context of the dataset.

Examples include:

Sample type
Disease status
Organism
Experimental condition
Treatment
Tissue or cell type
Technology used

Metadata is essential because the same expression value can have a very different meaning depending on the biological context.

Practical Skills Learned

Through working with GEO, I developed familiarity with:

Navigating the GEO resource
Searching for gene expression datasets
Understanding GEO accession numbers
Examining study and sample information
Understanding experimental groups
Exploring gene expression data
Using GEO2R
Understanding differential expression results
Interpreting log₂ fold change
Understanding adjusted p-values
Selecting genes for downstream analysis
Important Considerations

A GEO dataset should not be selected only because its title appears relevant.

Before analysis, it is important to check:

Experimental design
Sample characteristics
Number of samples
Disease and control groups
Organism
Data platform
Study description
Associated publication
Available metadata

Careful dataset selection is an important part of a reliable bioinformatics workflow.

Key Takeaways
GEO stands for Gene Expression Omnibus.
GEO is a public repository for gene expression and functional genomics datasets.
GEO datasets can be reused for computational analysis.
GSE identifies a GEO Series or study.
GSM identifies an individual sample.
GPL identifies the experimental platform.
Metadata is essential for understanding biological context.
GEO2R can be used to compare groups of samples within GEO studies.
Differential gene expression can identify genes that differ between biological conditions.
Log₂ fold change describes the direction and magnitude of expression change.
Adjusted p-values are important when many genes are tested.
The GEO dataset GSE43696 was used for the asthma transcriptomics case study during the internship.
Summary

Working with GEO introduced me to the practical use of publicly available gene expression data. More importantly, it showed me how a biological dataset can become the starting point for a complete computational analysis, from selecting and understanding samples to identifying significant genes and subsequently investigating their biological functions and interactions.
