# KEGG Pathway Database

## Introduction

KEGG (Kyoto Encyclopedia of Genes and Genomes) is a biological database resource used to understand genes and proteins in the context of biological pathways and cellular processes.

Unlike resources that mainly provide information about individual genes or proteins, KEGG helps connect biological molecules to larger systems such as metabolic pathways, signalling pathways, cellular processes and disease-related pathways.

During the internship, KEGG was explored as part of functional and pathway analysis following differential gene expression analysis.

---

## What is a Pathway?

A biological pathway is a series of interconnected molecular events that work together to perform a biological function.

For example:

```text
Signal
  ↓
Receptor
  ↓
Intracellular signalling molecules
  ↓
Transcription factors
  ↓
Gene expression
  ↓
Cellular response

Studying pathways helps researchers understand how multiple genes and proteins work together rather than examining them individually.

What KEGG Provides

KEGG contains information related to several areas of biology, including:

Metabolic pathways
Signalling pathways
Cellular processes
Genetic information processing
Environmental information processing
Human diseases
Drug-related information

The pathway component of KEGG is particularly useful when interpreting gene lists obtained from biological experiments.

KEGG Pathway Analysis

When a list of genes has been obtained from an experiment, those genes can be mapped to KEGG pathways.

The general idea is:

Gene List
    ↓
KEGG Mapping
    ↓
Associated Pathways
    ↓
Pathway Enrichment
    ↓
Biological Interpretation

This helps identify pathways that may be particularly relevant to the biological condition being studied.

KEGG and Differential Gene Expression

Differential gene expression analysis can produce a large list of genes that are significantly upregulated or downregulated.

Looking at individual genes provides useful information, but it may not explain the larger biological picture.

KEGG pathway analysis helps group these genes according to the pathways in which they participate.

For example:

Differentially Expressed Genes
             ↓
       Pathway Mapping
             ↓
      Related KEGG Pathways
             ↓
      Biological Interpretation

This provides a systems-level view of gene expression changes.

KEGG in the Asthma Transcriptomics Case Study

KEGG pathway analysis formed part of the functional analysis performed after identifying significant genes from the asthma transcriptomics dataset.

The case-study workflow was:

GEO Dataset
     ↓
GEO2R
     ↓
Healthy vs Asthma
     ↓
Differential Gene Expression
     ↓
Statistical Filtering
     ↓
Significant Genes
     ↓
GO + KEGG + g:Profiler
     ↓
Functional Interpretation
     ↓
STRING + Cytoscape

The dataset used for the case study was GSE43696. The selected genes from the differential expression analysis were taken forward for functional and network analysis.

KEGG Enrichment

KEGG enrichment analysis asks whether particular pathways contain more genes from the selected gene list than would be expected by chance.

For example:

Selected Gene List
       ↓
 ┌───────────────┐
 │ Gene A        │
 │ Gene B        │
 │ Gene C        │
 │ Gene D        │
 │ Gene E        │
 └───────────────┘
       ↓
KEGG Pathway Mapping
       ↓
Pathway 1 → several genes
Pathway 2 → few genes
Pathway 3 → several genes
       ↓
Enrichment Analysis

Enriched pathways can then be investigated in greater biological detail.

Relationship Between GO and KEGG

Gene Ontology and KEGG provide complementary information.

Gene Ontology

GO helps answer:

What biological functions are associated with these genes?

It describes:

Biological Process
Molecular Function
Cellular Component
KEGG

KEGG helps answer:

Which biological pathways are these genes involved in?

Therefore:

GO
↓
Functional Categories

KEGG
↓
Biological Pathways

Using both resources provides a broader interpretation of a gene list.

Relationship with g:Profiler

g:Profiler can also be used for enrichment analysis of gene lists.

A simplified workflow is:

Significant Genes
       ↓
 ┌─────┼─────────┐
 ↓     ↓         ↓
 GO   KEGG   g:Profiler
 └─────┼─────────┘
       ↓
Functional Interpretation

During the internship, g:Profiler was explored as an additional enrichment resource alongside GO and KEGG.

Pathway Interpretation

A statistically enriched pathway should not automatically be interpreted as proof that the pathway causes a disease or biological condition.

Pathway results need to be considered together with:

Differential expression results
Statistical significance
Gene direction of change
Biological knowledge
Literature evidence
Other computational analyses

This is especially important in disease-related transcriptomic studies.

Advantages of KEGG Analysis

KEGG pathway analysis can help researchers:

Organize genes into biological pathways
Understand relationships between genes
Interpret differential expression results
Identify potentially relevant signalling pathways
Study metabolic processes
Connect molecular changes with disease mechanisms
Generate hypotheses for further research
Limitations and Points to Consider

KEGG analysis is a computational interpretation tool and should not be treated as experimental validation.

Important considerations include:

Pathway annotations may not represent every biological context.
A gene can participate in multiple pathways.
Pathways may overlap with each other.
Statistical significance does not necessarily imply biological importance.
Enrichment results depend on the selected gene list and background set.
Computational findings require further biological investigation and experimental validation.
Practical Workflow

The following workflow summarizes how KEGG fits into the internship's analysis pipeline:

1. Obtain biological dataset
          ↓
2. Perform differential gene expression analysis
          ↓
3. Select significant genes
          ↓
4. Submit / map genes for functional analysis
          ↓
5. Identify KEGG-associated pathways
          ↓
6. Examine enriched pathways
          ↓
7. Compare findings with GO and g:Profiler
          ↓
8. Integrate results with PPI/network analysis
          ↓
9. Interpret biological significance
Key Takeaways
KEGG is a major biological resource for pathway-based analysis.
It connects genes and proteins to biological pathways.
KEGG can be used to interpret lists of differentially expressed genes.
Pathway enrichment helps identify biological pathways represented more strongly in a selected gene set.
GO and KEGG are complementary:
GO focuses on functional categories.
KEGG focuses on biological pathways.
KEGG was part of the functional analysis workflow used for the asthma transcriptomics case study.
Pathway enrichment results should be interpreted together with statistical and biological evidence.
Computational pathway analysis generates useful biological hypotheses but does not replace experimental validation.
Summary

KEGG provides a pathway-level view of biological data. In the internship workflow, it helped bridge the gap between a list of differentially expressed genes and a broader understanding of the biological pathways associated with those genes.

Gene Expression
      ↓
Differentially Expressed Genes
      ↓
KEGG Pathway Analysis
      ↓
Enriched Biological Pathways
      ↓
Systems-Level Interpretation
