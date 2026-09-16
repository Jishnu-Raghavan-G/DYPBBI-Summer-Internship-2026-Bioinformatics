Overview

After obtaining the selected differentially expressed genes from the GSE43696 asthma transcriptomics analysis, the next step was to understand what those genes might represent biologically.

A gene list by itself does not provide much biological context. Functional enrichment analysis helps determine whether particular biological functions, processes, or pathways are represented more frequently in the selected genes than expected.

The internship workflow used Gene Ontology (GO), KEGG and g:Profiler for this stage of the analysis.

Why Functional Enrichment Was Needed

The differential-expression stage produces a list such as:

Gene 1
Gene 2
Gene 3
Gene 4
Gene 5
...

The next question is:

What biological functions and pathways are associated with these genes?

Functional enrichment helps move from:

Gene-level results
       ↓
Biological meaning
Overall Workflow
Differentially Expressed Genes
             ↓
        Gene List
             ↓
      Functional Analysis
             ↓
      ┌──────┼──────┐
      ↓      ↓      ↓
      GO    KEGG  g:Profiler
      ↓      ↓      ↓
      Biological Functions
             ↓
      Pathway Interpretation

This was followed by protein-protein interaction and network analysis in the broader case-study workflow.

Gene Ontology

Gene Ontology (GO) provides a standardized way of describing gene and protein functions.

The three major GO categories are:

Biological Process

Describes biological processes in which a gene or protein participates.

Examples include processes related to:

Cell signaling
Immune responses
Cell proliferation
Metabolic processes
Molecular Function

Describes the molecular activity performed by a gene product.

Examples include:

Enzyme activity
DNA binding
Receptor activity
Protein binding
Cellular Component

Describes where a gene product is located within a cell.

Examples include:

Nucleus
Cytoplasm
Cell membrane
Extracellular region

The GO analysis therefore provides three complementary perspectives on the genes being studied.

KEGG Pathway Analysis

KEGG can be used to associate genes with biological pathways.

Instead of considering genes individually, pathway analysis allows them to be viewed as components of larger biological systems.

Conceptually:

Gene list
   ↓
Pathway database
   ↓
Associated pathways
   ↓
Biological interpretation

This is particularly useful for disease-related transcriptomics because several differentially expressed genes may participate in the same biological pathway.

g:Profiler

g:Profiler was another resource used during the functional-analysis stage.

It can be used to investigate functional enrichment and related biological annotations from a submitted gene list.

The internship workflow included g:Profiler alongside GO and KEGG analysis.

The general workflow was:

Selected genes
      ↓
Submit gene list
      ↓
Functional enrichment
      ↓
Significant terms/pathways
      ↓
Interpret biological relevance
Enrichment Concept

Suppose a selected DEG list contains many genes associated with the same biological process.

If that process occurs more frequently in the selected list than expected from the background population, it may appear as an enriched term.

Conceptually:

Background genes
       ↓
Expected representation
       ↓
Compare with
       ↓
Selected DEG list
       ↓
Observed representation
       ↓
Enrichment analysis

The statistical significance of an enrichment result must also be considered when interpreting the output.

Interpreting Enrichment Results

An enrichment result may contain information such as:

GO term
Pathway name
Number of associated genes
Statistical significance
Adjusted significance
Enrichment-related measures
Genes contributing to the term

A simplified interpretation could look like:

Selected DEGs
      ↓
Several genes associated
with one biological process
      ↓
Process appears enriched
      ↓
Investigate its relevance
to the disease context
From Enrichment to Biology

The main purpose was not simply to collect a large list of enriched terms.

The results need to be interpreted in the context of the original biological question:

Asthma
  ↓
Gene-expression differences
  ↓
DEGs
  ↓
Enriched biological processes
  ↓
Enriched pathways
  ↓
Possible biological interpretation

This makes functional enrichment a bridge between statistical transcriptomics and biological interpretation.

Relationship With Network Analysis

Functional enrichment was followed by protein-protein interaction analysis as part of the internship workflow.

The overall progression was:

DEGs
 ↓
GO / KEGG / g:Profiler
 ↓
Functional interpretation
 ↓
STRING
 ↓
PPI network
 ↓
Cytoscape
 ↓
Hub-gene analysis

The internship documentation describes GO, KEGG, g:Profiler, STRING and Cytoscape as connected components of the downstream analysis.

Important Interpretation

Functional enrichment does not automatically mean that an enriched pathway causes asthma.

It indicates that the submitted gene set is statistically associated with particular annotations or pathways under the analysis method and background used.

Therefore, interpretation should consider:

Statistical significance
Multiple-testing correction
Background gene set
Number of genes contributing to the result
Biological context
Published literature
What I Learned

Through this part of the case study, I learned how a list of differentially expressed genes can be converted into a more meaningful biological description.

The main concepts were:

Gene Ontology
Biological Process
Molecular Function
Cellular Component
KEGG pathways
g:Profiler
Enrichment analysis
Statistical significance
Biological interpretation

This stage helped connect the gene-level results from GSE43696 with broader biological processes and pathways before moving into PPI and network analysis.
