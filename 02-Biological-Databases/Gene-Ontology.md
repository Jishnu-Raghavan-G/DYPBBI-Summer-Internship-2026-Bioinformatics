# Gene Ontology (GO)

## Introduction

Gene Ontology (GO) is a standardized system used to describe the functions and biological roles of genes and proteins.

It provides a common vocabulary for describing what a gene or protein does, where it functions, and which biological processes it is involved in.

During the internship, Gene Ontology was explored as an important resource for functional annotation and enrichment analysis of gene lists.

---

## The Three Main GO Categories

Gene Ontology is divided into three major domains:

### 1. Biological Process (BP)

Biological Process describes larger biological activities or processes in which a gene or protein participates.

Examples include:

- Cell cycle
- Immune response
- Signal transduction
- Apoptotic process
- Inflammatory response
- Cell proliferation

A biological process generally involves multiple molecular activities working together to achieve a biological outcome.

---

### 2. Molecular Function (MF)

Molecular Function describes the specific molecular activity performed by a gene product, usually a protein.

Examples include:

- ATP binding
- DNA binding
- Protein kinase activity
- Enzyme activity
- Receptor activity
- Transcription factor activity

Molecular Function focuses on **what the molecule does at the molecular level**.

---

### 3. Cellular Component (CC)

Cellular Component describes where a gene product is located or where it functions within the cell.

Examples include:

- Nucleus
- Cytoplasm
- Plasma membrane
- Mitochondrion
- Ribosome
- Extracellular region

Cellular Component therefore provides information about the **cellular location associated with a gene or protein**.

---

## Simple Way to Remember GO

The three GO categories can be understood as:

| GO Category | Main Question |
|---|---|
| Biological Process | What biological process is it involved in? |
| Molecular Function | What molecular activity does it perform? |
| Cellular Component | Where does it function? |

For example, a protein could:

- participate in an inflammatory response → Biological Process
- have receptor activity → Molecular Function
- be located at the plasma membrane → Cellular Component

---

## GO Terms

The individual descriptions used by Gene Ontology are called **GO terms**.

Each GO term represents a specific biological concept.

A gene can be associated with multiple GO terms because a single gene or protein may have several functions and participate in different biological processes.

GO terms are organized in a hierarchical structure, where broader concepts can be connected to more specific concepts.

This allows biological functions to be described at different levels of detail.

---

## GO Annotation

GO annotation is the process of associating genes or proteins with relevant GO terms.

For example:

```text
Gene / Protein
      ↓
Functional information
      ↓
GO annotation
      ↓
Biological Process
Molecular Function
Cellular Component

GO annotations help researchers interpret the biological meaning of genes identified from experimental or computational studies.

Functional Enrichment Analysis

One of the important applications of Gene Ontology is functional enrichment analysis.

After differential gene expression analysis, researchers may obtain a list of genes that show significant changes between two biological conditions.

Instead of studying every gene individually, the gene list can be analyzed to determine whether particular biological functions are represented more frequently than expected.

The general workflow is:

Biological Dataset
       ↓
Differential Gene Expression
       ↓
Significant Gene List
       ↓
Gene Ontology Analysis
       ↓
Enriched GO Terms
       ↓
Biological Interpretation

Enrichment analysis can identify categories related to:

Biological processes
Molecular functions
Cellular components
Background Gene Set

Functional enrichment analysis requires an appropriate reference or background gene set.

The background represents the genes that could reasonably have been selected in the analysis.

Comparing the selected genes against this background helps determine whether a GO category occurs more often than would be expected by chance.

Therefore, enrichment results depend not only on the selected genes but also on the background used for comparison.

GO Analysis in the Asthma Transcriptomics Study

During the internship, Gene Ontology was used as part of the functional analysis following differential gene expression analysis of the asthma dataset.

The overall workflow was:

GEO Dataset
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
GO Functional Analysis
     ↓
Biological Interpretation

The selected genes were analyzed to investigate their associated:

Biological Processes
Molecular Functions
Cellular Components

This helped move the analysis from a list of statistically significant genes toward a biological interpretation of what those genes may be involved in.

The asthma dataset used in the case study was GSE43696, which was explored through GEO and analyzed using GEO2R.

GO Enrichment vs GO Annotation

These two concepts are related but not identical.

GO Annotation

Answers:

What functions are already associated with this gene?

GO Enrichment

Answers:

Which functions or GO categories are represented more strongly in my selected gene list than expected?

Therefore:

GO Annotation → Information about individual genes

GO Enrichment → Biological patterns within a group of genes
Interpreting GO Results

A GO enrichment result may contain information such as:

GO term
GO category
Number of associated genes
Statistical significance
Adjusted p-value
Gene ratio or enrichment-related measures

A significant GO term does not automatically mean that the biological process causes the disease.

It indicates that the selected genes are statistically associated with that functional category and that the category may be biologically relevant for further investigation.

Importance of Statistical Significance

Large gene lists can produce many GO terms.

Because multiple categories may be tested simultaneously, statistical correction is important when interpreting enrichment results.

Adjusted p-values can help identify GO terms that remain statistically significant after accounting for multiple testing.

Therefore, GO results should be interpreted using both:

Statistical significance
Biological relevance
Redundant GO Terms

GO enrichment results can sometimes contain several related or overlapping terms.

For example, multiple GO terms may describe closely related aspects of the same biological process.

Therefore, enrichment results should not simply be interpreted as a list of completely independent findings.

Related GO terms can sometimes be grouped into broader biological themes.

Relationship with Other Bioinformatics Resources

Gene Ontology is one part of a larger functional and network analysis workflow.

In the internship, the functional analysis workflow connected several resources:

Differentially Expressed Genes
          ↓
     Gene Ontology
          ↓
     KEGG Pathways
          ↓
      g:Profiler
          ↓
      STRING PPI
          ↓
      Cytoscape
          ↓
 Biological Interpretation

GO focuses mainly on functional categories, while KEGG provides pathway-level information, g:Profiler provides enrichment-based analysis, and STRING focuses on protein–protein interactions.

Practical Importance

Gene Ontology is useful because it helps researchers convert a long list of genes into understandable biological information.

It can help with:

Functional annotation
Interpretation of differentially expressed genes
Functional enrichment
Disease research
Biomarker studies
Understanding biological mechanisms
Identifying common biological themes within gene sets
Key Takeaways
Gene Ontology provides a standardized vocabulary for describing gene and protein functions.
GO has three major domains:
Biological Process
Molecular Function
Cellular Component
GO terms describe specific biological concepts.
GO annotation associates genes or proteins with functional terms.
GO enrichment identifies functional categories that are overrepresented in a selected gene list.
An appropriate background gene set is important for enrichment analysis.
Adjusted p-values are important when interpreting multiple enrichment results.
GO was used in the internship to interpret significant genes obtained from the asthma transcriptomics workflow.
GO results should be interpreted together with other biological evidence rather than treated as proof of a disease mechanism.
Workflow Summary
Gene Expression Dataset
          ↓
Differential Gene Expression
          ↓
Significant Gene List
          ↓
Gene Ontology
          ↓
┌─────────────────────────┐
│ Biological Process      │
│ Molecular Function      │
│ Cellular Component      │
└─────────────────────────┘
          ↓
Functional Enrichment
          ↓
Biological Interpretation
