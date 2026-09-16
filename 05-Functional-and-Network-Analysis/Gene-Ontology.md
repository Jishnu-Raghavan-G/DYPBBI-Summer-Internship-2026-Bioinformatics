Overview

Gene Ontology (GO) is a standardized framework used to describe the functions and locations of genes and their associated proteins.

In the internship, Gene Ontology was introduced as part of the functional-analysis stage. After obtaining a selected set of genes from transcriptomics analysis, GO analysis was used to investigate their biological meaning.

Why Gene Ontology Is Useful

A differential-expression analysis may produce a list containing many genes.

For example:

Gene A
Gene B
Gene C
Gene D
Gene E
...

Looking at the genes individually does not always reveal the larger biological pattern.

GO analysis helps organize these genes into functional categories:

Gene List
    ↓
Gene Ontology
    ↓
Biological Functions
    ↓
Biological Interpretation
Three Main GO Categories

Gene Ontology is divided into three major aspects.

Biological Process

Biological Process (BP) describes larger biological processes in which a gene or gene product participates.

Examples include:

Cell signaling
Cell division
Immune response
Metabolic processes
Cellular responses to stimuli

A biological process generally involves multiple molecular activities working together.

Molecular Function

Molecular Function (MF) describes the specific molecular activity performed by a gene product.

Examples include:

DNA binding
Protein binding
Enzyme activity
Receptor activity
Transporter activity

It focuses on what a molecule does at the molecular level.

Cellular Component

Cellular Component (CC) describes the cellular location or structure associated with a gene product.

Examples include:

Nucleus
Cytoplasm
Cell membrane
Mitochondria
Extracellular region

It therefore provides information about where the gene product is associated within the cell.

Simple Comparison
GO Category	Main Question
Biological Process	What biological process is it involved in?
Molecular Function	What molecular activity does it perform?
Cellular Component	Where is it located or associated?

A single gene can have annotations in all three categories.

GO Terms

GO uses standardized terms to describe biological concepts.

For example:

Gene
 ↓
GO annotations
 ↓
Biological Process
Molecular Function
Cellular Component

This standardized terminology makes it easier to compare functional information across different studies and organisms.

GO Enrichment Analysis

GO enrichment analysis asks whether particular GO terms are represented more frequently in a selected gene list than would be expected based on an appropriate background.

The basic workflow is:

Selected Gene List
       ↓
GO Database
       ↓
Compare annotations
       ↓
Enrichment analysis
       ↓
Enriched GO terms
       ↓
Biological interpretation

In the asthma transcriptomics case study, selected genes from the GSE43696 analysis were taken forward for functional analysis including GO.

Example Concept

Imagine a selected gene list contains many genes associated with an immune-related biological process.

The enrichment analysis can ask:

Are immune-related GO terms
represented more frequently
in this gene list than expected?

If the statistical analysis supports enrichment, that GO term can become part of the biological interpretation.

Background Gene Set

The choice of background is important in enrichment analysis.

The selected genes should generally be compared against an appropriate reference/background set rather than assuming that every gene in the genome was equally available for selection.

Conceptually:

Background population
        ↓
Expected representation
        ↓
Compare with
        ↓
Selected genes
        ↓
Observed representation

The resulting enrichment therefore depends partly on the background used.

Statistical Significance

GO enrichment produces statistical measures indicating how strongly the observed enrichment is supported.

Because many GO terms may be tested simultaneously, multiple-testing correction is important.

A result should therefore not be interpreted simply because one raw p-value is small.

Important information can include:

GO term
Number of associated genes
p-value
Adjusted p-value
Enrichment-related statistic
Genes contributing to the term
GO in the Asthma Case Study

The functional-analysis stage of the internship connected the DEG list to biological functions and pathways.

The overall progression was:

GSE43696
   ↓
GEO2R
   ↓
Differentially Expressed Genes
   ↓
Gene Ontology
   ↓
Biological Processes
Molecular Functions
Cellular Components

GO analysis was then considered alongside KEGG and g:Profiler results to provide additional functional context.

GO and KEGG Are Different

Although both can be used for biological interpretation, they provide different perspectives.

Gene Ontology
      ↓
Functional annotations
      ↓
"What biological functions are represented?"

Whereas:

KEGG
      ↓
Pathways
      ↓
"Which biological pathways are represented?"

Using both can provide complementary information.

GO and Network Analysis

GO analysis can also be combined with PPI-network analysis.

DEGs
 ↓
GO Enrichment
 ↓
Functional context

DEGs
 ↓
STRING
 ↓
PPI Network
 ↓
Network context

The internship workflow combined functional enrichment with STRING and Cytoscape-based network analysis.

Important Interpretation

An enriched GO term does not automatically establish that the biological process causes the disease being studied.

It indicates that the submitted gene set has a statistically notable representation of genes associated with that ontology term under the analysis conditions.

Therefore, interpretation should consider:

Statistical significance
Multiple-testing correction
Background gene set
Number of genes contributing to the term
Biological context
Existing research literature
What I Learned

Through Gene Ontology analysis, I learned how a list of genes can be converted into standardized biological descriptions.

The main concepts were:

Gene Ontology
Biological Process
Molecular Function
Cellular Component
GO terms
Functional enrichment
Background gene sets
Statistical significance
Multiple-testing correction
Biological interpretation

GO therefore provides an important bridge between differential gene-expression results and biological meaning, which was an important part of the functional-analysis workflow during the internship.
