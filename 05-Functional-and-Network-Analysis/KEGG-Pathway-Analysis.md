# KEGG Pathway Analysis

## Introduction

KEGG (Kyoto Encyclopedia of Genes and Genomes) is a biological database used to understand how genes and their products are connected to cellular pathways and biological functions.

While Gene Ontology (GO) mainly describes what genes do in terms of biological processes, molecular functions, and cellular components, KEGG helps place genes into **specific biological pathways**.

During the internship, KEGG pathway analysis was introduced as one of the downstream steps after identifying differentially expressed genes. It helped connect a list of genes with biological pathways that may be relevant to a disease or biological condition.

---

## What is a Pathway?

A biological pathway is a series of connected molecular events that work together to perform a particular biological function.

For example, a pathway may involve:

- A receptor receiving a signal
- Activation of intracellular proteins
- Activation of transcription factors
- Changes in gene expression
- Production of a cellular response

Genes usually do not work independently. They participate in networks and pathways where the activity of one component can affect others.

Therefore, after obtaining a list of differentially expressed genes, pathway analysis can provide additional biological context.

---

## What is KEGG?

KEGG stands for **Kyoto Encyclopedia of Genes and Genomes**.

It is a resource that connects molecular information with higher-level biological functions.

KEGG contains information related to:

- Metabolic pathways
- Signaling pathways
- Cellular processes
- Genetic information processing
- Environmental information processing
- Organismal systems
- Human diseases
- Drug-related information

For bioinformatics analysis, KEGG is commonly used to determine whether a group of genes is associated with particular biological pathways.

---

## KEGG Pathway Maps

KEGG represents pathways using pathway maps.

These maps show relationships between biological molecules such as:

- Genes
- Proteins
- Enzymes
- Metabolites
- Receptors
- Signaling molecules

A pathway map can therefore provide a visual representation of how different molecular components interact.

---

## Why Perform KEGG Pathway Analysis?

A differential expression analysis may produce a large list of genes.

For example:

```text
Gene A
Gene B
Gene C
Gene D
Gene E
...
Gene N

Looking at each gene individually can make biological interpretation difficult.

KEGG pathway analysis helps answer a broader question:

Are these genes collectively associated with particular biological pathways?

This makes it easier to move from individual genes to biological mechanisms.

Basic Workflow

A simplified KEGG analysis workflow is:

Differential Expression Analysis
            ↓
Identify Differentially Expressed Genes
            ↓
Prepare Gene List
            ↓
Map Genes to KEGG
            ↓
Perform Pathway Enrichment
            ↓
Identify Significant Pathways
            ↓
Interpret Biological Relevance
Input for KEGG Analysis

The input is generally a list of genes obtained from a previous analysis.

For example:

Gene1
Gene2
Gene3
Gene4
Gene5

Depending on the tool being used, gene identifiers may need to be converted into an appropriate format.

Common identifiers include:

Gene symbols
Entrez Gene IDs
Ensembl IDs

The organism must also be selected correctly.

For example:

Organism: Homo sapiens

Using the wrong organism or incorrect gene identifiers can produce misleading or incomplete results.

Pathway Enrichment

Pathway enrichment asks whether the input gene list contains more genes belonging to a particular pathway than would be expected by chance.

For example, suppose a list of differentially expressed genes contains many genes associated with an inflammatory signaling pathway.

If this enrichment is statistically significant, the pathway may become a useful biological candidate for further investigation.

The important point is that enrichment does not automatically prove that the pathway is responsible for the disease.

It indicates that the genes in the input list are statistically associated with that pathway.

Statistical Significance

KEGG enrichment results commonly contain statistical measures such as:

P-value
Adjusted p-value
Gene ratio
Number of genes
Enrichment-related statistics
P-value

The p-value provides a measure of how unlikely the observed enrichment would be under the null hypothesis.

A smaller p-value generally indicates stronger statistical evidence for enrichment.

However, when many pathways are tested simultaneously, multiple-testing correction becomes important.

Adjusted P-value

When hundreds of pathways are tested, some may appear significant purely by chance.

Therefore, enrichment analyses commonly apply multiple-testing correction.

An adjusted p-value helps control this problem.

A commonly used approach is the False Discovery Rate (FDR).

For example:

Adjusted p-value < 0.05

may be used as a filtering threshold, depending on the analysis design.

The threshold should always be reported clearly rather than treating 0.05 as a universal rule.

Gene Ratio

Gene ratio describes the proportion of genes in the input list that are associated with a particular pathway.

A simplified representation is:

Gene Ratio =
Number of input genes associated with pathway
----------------------------------------------
Total number of input genes

For example, if:

10 genes

from a list of:

100 genes

are associated with a pathway:

Gene Ratio = 10 / 100 = 0.10
Background Gene Set

The background or reference gene set is also important in enrichment analysis.

The analysis should compare the input gene list against an appropriate background population.

For example:

Background:
All genes that could have been detected in the experiment

Input:
Differentially expressed genes

The choice of background can affect enrichment results, so it should be selected carefully.

KEGG in the Asthma Transcriptomics Case Study

In the internship case study, transcriptomic analysis was performed using the GEO dataset GSE43696.

The workflow involved comparing healthy and asthma-related samples, identifying differentially expressed genes, and then carrying selected genes into downstream functional analyses. KEGG was included along with GO and g:Profiler to investigate the biological significance of the selected genes.

The general workflow can be represented as:

GSE43696
   ↓
GEO2R
   ↓
Healthy vs Asthma Comparison
   ↓
Differentially Expressed Genes
   ↓
Statistical Filtering
   ↓
Selected Gene List
   ↓
KEGG Pathway Analysis
   ↓
Biological Interpretation

This helped connect the differential gene-expression results with pathways potentially relevant to the biological condition being investigated.

KEGG vs Gene Ontology

GO and KEGG are complementary rather than interchangeable.

Feature	Gene Ontology	KEGG
Main purpose	Describe gene functions	Represent biological pathways
Main categories	BP, MF, CC	Pathways and molecular systems
Focus	Functional description	Relationships between biological components
Typical output	Enriched GO terms	Enriched pathways
Example interpretation	Genes involved in immune response	Genes associated with a particular signaling pathway

A useful way to remember the difference is:

GO → What are these genes doing?

KEGG → Which biological pathways are these genes involved in?
KEGG and g:Profiler

KEGG can be accessed through different bioinformatics resources and enrichment tools.

During the internship, g:Profiler was introduced as a resource for functional enrichment analysis, including GO and pathway-related interpretation.

A simplified workflow is:

Gene List
   ↓
g:Profiler
   ↓
Functional Enrichment
   ↓
GO Terms + Pathway Information
   ↓
Statistical Filtering
   ↓
Biological Interpretation

This provides a convenient way to examine the functional and pathway-level meaning of a gene list.

Interpreting KEGG Results

A KEGG result should not be interpreted only by looking at the smallest p-value.

Important factors include:

Number of genes contributing to the pathway
Adjusted p-value
Gene ratio
Biological relevance
Direction of gene expression
Background gene set
Experimental design
Whether the pathway is supported by other analyses

For example, if a pathway is significantly enriched, the next question should be:

Which genes from my dataset are responsible for this enrichment?

This connects pathway-level analysis back to individual genes.

Visualizing Pathway Results

Pathway enrichment results are often presented using plots such as:

Bar plots
Dot plots
Enrichment plots
Pathway maps

A typical enrichment plot may contain:

Y-axis → Pathway names

X-axis → Gene ratio / enrichment measure

Additional visual properties may represent:

Statistical significance
Number of genes
Enrichment strength

Visualisation makes it easier to compare multiple pathways.

Limitations

KEGG pathway enrichment has several limitations.

1. Pathway databases are not complete

Not every biological mechanism is represented equally.

2. Gene annotation affects the result

Poorly annotated genes may not be mapped to pathways.

3. Statistical significance is not biological proof

An enriched pathway does not prove that the pathway causes the observed phenotype.

4. Background selection matters

An inappropriate background gene set can influence the enrichment result.

5. Pathways can overlap

The same gene may occur in multiple pathways, making different enriched pathways biologically related.

6. Interpretation requires context

A statistically significant pathway should be interpreted alongside the original experiment, gene-expression patterns, literature, and other analyses.

Connection with Network Analysis

KEGG pathway analysis and protein-protein interaction analysis provide different levels of biological interpretation.

A simplified downstream workflow is:

Differentially Expressed Genes
          ↓
     ┌────┴────┐
     ↓         ↓
   KEGG       STRING
     ↓         ↓
 Pathways      PPI Network
     ↓         ↓
     └────┬────┘
          ↓
 Biological Interpretation

In the internship workflow, functional enrichment using GO, KEGG and g:Profiler was followed by interaction/network analysis using STRING and Cytoscape.

This allowed the analysis to move from:

Genes
  ↓
Functions
  ↓
Pathways
  ↓
Protein interactions
  ↓
Network-level interpretation
Key Learning

The main concept I learned from KEGG pathway analysis was that a list of differentially expressed genes can be interpreted at a higher biological level.

Instead of studying genes individually, pathway analysis helps identify groups of genes participating in related biological processes and molecular pathways.

For the asthma transcriptomics case study, KEGG formed part of the downstream functional analysis after differential gene-expression analysis of GSE43696.

Quick Revision
KEGG
↓
Kyoto Encyclopedia of Genes and Genomes

Purpose:
Understand biological pathways and molecular relationships.

Input:
Gene list

Main analysis:
Pathway enrichment

Important measures:
- P-value
- Adjusted p-value
- Gene ratio
- Gene count

Basic question:
Which pathways are associated with my genes?

GO:
"What are these genes doing?"

KEGG:
"Which pathways are these genes involved in?"

Case Study:
GSE43696
↓
GEO2R
↓
DEGs
↓
Filtering
↓
KEGG / GO / g:Profiler
↓
STRING / Cytoscape
Conclusion

KEGG pathway analysis provides a pathway-level view of gene-expression results. It is particularly useful after differential expression analysis because it helps convert a long list of genes into interpretable biological pathways.

In combination with GO, g:Profiler, STRING and Cytoscape, KEGG contributes to a broader functional and network-level interpretation of transcriptomic datasets.
