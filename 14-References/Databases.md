# Databases

This file lists the major biological databases and online resources referred to during the Bioinformatics Summer Internship 2026.

## NCBI

**National Center for Biotechnology Information (NCBI)**

NCBI provides access to a wide range of biological databases and computational resources.

Used for:
- Nucleotide and protein sequence information
- Gene and genome information
- Literature and biomedical resources
- Biological data retrieval

---

## GEO

**Gene Expression Omnibus (GEO)**

GEO is a public repository for functional genomics data, including gene-expression datasets.

Used during the internship for:
- Gene-expression data exploration
- Microarray and transcriptomics datasets
- GEO2R-based differential expression analysis

Important dataset used:

- **GSE43696** — asthma-related gene-expression dataset

---

## UniProt

**Universal Protein Resource (UniProt)**

UniProt provides detailed information about proteins and their biological functions.

Used for:
- Protein identification
- Protein function
- Protein sequences
- Functional annotation

---

## Protein Data Bank

**Protein Data Bank (PDB)**

PDB provides experimentally determined three-dimensional structures of biological macromolecules.

Used for:
- Protein structure retrieval
- Structural bioinformatics
- Molecular visualization
- Molecular docking preparation

---

## PDBsum

PDBsum provides graphical and summarized information about protein structures deposited in the PDB.

Used for:
- Structural interpretation
- Protein-ligand interactions
- Structural diagrams
- Analysis of molecular interactions

---

## STRING

**STRING — Search Tool for the Retrieval of Interacting Genes/Proteins**

STRING is a database and platform for exploring known and predicted protein-protein interactions.

Used for:
- PPI network analysis
- Protein interaction exploration
- Functional association analysis

---

## Gene Ontology

**Gene Ontology (GO)**

Gene Ontology provides standardized descriptions of gene and protein functions.

The main GO categories are:

- Biological Process (BP)
- Molecular Function (MF)
- Cellular Component (CC)

Used for functional enrichment analysis of differentially expressed genes.

---

## KEGG

**Kyoto Encyclopedia of Genes and Genomes (KEGG)**

KEGG provides information about biological pathways, molecular functions, diseases, and cellular processes.

Used for:
- Pathway analysis
- Functional interpretation
- Biological pathway mapping

---

## g:Profiler

**g:Profiler**

g:Profiler is a functional profiling platform used to investigate biological functions and pathways associated with a list of genes.

Used for:
- Gene enrichment analysis
- GO analysis
- Pathway enrichment
- Functional interpretation of gene lists

---

## AlphaFold

**AlphaFold Protein Structure Database**

AlphaFold provides predicted three-dimensional protein structures generated using deep-learning-based structure prediction.

Used for:
- Exploring predicted protein structures
- Structural bioinformatics
- Understanding protein structure when experimental structures may not be available

---

## SWISS-MODEL

**SWISS-MODEL**

SWISS-MODEL is an automated homology-modelling platform for predicting protein three-dimensional structures from amino-acid sequences.

Used for:
- Homology modelling
- Comparative structural analysis
- Protein structure prediction

---

## Reference Workflow

The databases were used at different stages of the bioinformatics workflow:

```text
Biological Question
        ↓
Data Retrieval
        ↓
NCBI / GEO
        ↓
Gene Expression Analysis
        ↓
Functional Annotation
        ↓
GO / KEGG / g:Profiler
        ↓
Protein and Network Analysis
        ↓
UniProt / STRING
        ↓
Structural Analysis
        ↓
PDB / PDBsum / AlphaFold / SWISS-MODEL
Note

These resources were used for learning, data exploration, analysis, interpretation, and understanding of different bioinformatics workflows during the internship.


---

## `14-References/Software.md`

```markdown
# Software

This file lists the major software tools and computational platforms referred to or used during the Bioinformatics Summer Internship 2026.

## GEO2R

**GEO2R — GEO2R Analysis Tool**

GEO2R is a web-based analysis tool provided through GEO for comparing gene-expression profiles between selected groups of samples.

Used for:
- Dataset exploration
- Group comparison
- Differential gene-expression analysis
- Identification of significant genes

---

## Cytoscape

**Cytoscape**

Cytoscape is an open-source platform for visualizing and analysing molecular interaction networks.

Used for:
- PPI network visualization
- Network exploration
- Hub-gene analysis
- Interpretation of interaction networks

---

## PyMOL

**PyMOL**

PyMOL is a molecular visualization system used for viewing and analysing three-dimensional biological structures.

Used for:
- Protein structure visualization
- Molecular structure inspection
- Structural analysis

---

## ChimeraX

**UCSF ChimeraX**

ChimeraX is a molecular visualization and analysis program designed for working with molecular structures and related biological data.

Used during the molecular docking training for:
- Protein structure visualization
- Structure inspection
- Protein preparation
- Molecular interaction analysis

---

## AutoDock Tools

**AutoDock Tools (ADT)**

AutoDock Tools provides tools for preparing molecular structures and setting up molecular docking calculations.

Used during docking training for:
- Protein preparation
- Ligand preparation
- Docking setup
- Preparation of structures for AutoDock-based workflows

---

## AutoDock Vina

**AutoDock Vina**

AutoDock Vina is a molecular docking program used to predict possible binding modes between a protein and a ligand.

Used for learning:
- Molecular docking
- Docking poses
- Binding-affinity scoring
- Protein-ligand interaction analysis

---

## Python

Python was used as a programming language for learning and demonstrating computational analysis of biological data.

Relevant applications include:
- Data processing
- Tabular-data analysis
- Statistical analysis
- Visualization
- Gene-expression data processing

Common libraries relevant to the repository include:

- NumPy
- Pandas
- Matplotlib
- Seaborn

---

## Overall Software Workflow

```text
Biological Data
      ↓
Python / Data Processing
      ↓
GEO2R
      ↓
Differential Expression
      ↓
g:Profiler / GO / KEGG
      ↓
STRING
      ↓
Cytoscape
      ↓
PDB / AlphaFold / SWISS-MODEL
      ↓
PyMOL / ChimeraX
      ↓
AutoDock Tools
      ↓
AutoDock Vina
Note

The software listed here represents tools introduced, explored, or used as part of the internship learning workflow. Their inclusion does not imply that every tool was used for an independent research project.


---

## `14-References/Books.md`

```markdown
# Books

This file lists books and learning resources relevant to the concepts covered during the Bioinformatics Summer Internship 2026.

## Bioinformatics

### Bioinformatics Algorithms

Reference material covering computational approaches to biological data, sequence analysis, algorithms, and biological problem solving.

Useful for:
- Understanding computational biology
- Sequence analysis
- Algorithmic thinking
- Biological data analysis

---

## Molecular Biology

### Molecular Biology of the Cell

A foundational reference for understanding molecular and cellular biology.

Useful for:
- Gene expression
- DNA and RNA biology
- Protein synthesis
- Cellular processes
- Molecular mechanisms

---

## Biostatistics

### Biostatistics: A Foundation for Analysis in the Health Sciences

A reference for statistical concepts relevant to biological and medical data.

Useful for:
- Descriptive statistics
- Probability
- Hypothesis testing
- Statistical interpretation
- Biological data analysis

---

## Structural Bioinformatics

### Structural Bioinformatics

Reference material for understanding protein structures, molecular interactions, structure analysis, and computational structural biology.

Useful for:
- Protein structure
- Molecular interactions
- Structural analysis
- Computational modelling

---

## Medicinal Chemistry

### An Introduction to Medicinal Chemistry

Reference material for understanding the relationship between chemical structure and biological activity.

Useful for:
- Ligands
- Functional groups
- Stereochemistry
- Isomerism
- Molecular interactions
- Drug-design concepts

---

## Purpose of the References

These resources provide background knowledge supporting the concepts covered in:

- Bioinformatics fundamentals
- Biological databases
- Transcriptomics
- Functional enrichment
- Network analysis
- Structural bioinformatics
- Molecular docking
- Virtual screening
- Statistics and biostatistics
- Scientific research and writing
14-References/Research-Papers.md
# Research Papers

This file lists the major research papers and scientific literature reviewed or referenced during the Bioinformatics Summer Internship 2026.

## Asthma Transcriptomics

The internship included a research-paper review component focused on the evolution of gene-expression research in asthma.

The reviewed literature covered topics including:

- Asthma-associated gene-expression signatures
- Differential gene expression
- Disease-associated pathways
- Molecular classification
- Hub genes and regulatory mechanisms
- Transcriptomic analysis
- Precision medicine
- Multicohort analysis

---

## Selected Papers

### 1. Moffatt et al. — 2007

**Moffatt MF et al.**

*Genetic variants regulating ORMDL3 expression contribute to the risk of childhood asthma.*

**Journal:** Nature  
**Year:** 2007  
**GEO Dataset:** GSE8052

This work is part of the early genomic and gene-expression research that helped establish molecular associations with asthma.

---

### 2. Woodruff et al. — 2009

**Woodruff PG et al.**

Research examining gene-expression patterns associated with asthma in airway epithelial cells.

**Journal:** American Journal of Respiratory and Critical Care Medicine  
**Year:** 2009  
**GEO Dataset:** GSE4302

This work contributed to the understanding of airway epithelial gene-expression patterns in asthma.

---

### 3. Peters et al. — 2014

**Peters MC et al.**

Research investigating molecular and transcriptomic characteristics associated with asthma and airway inflammation.

**Journal:** Journal of Allergy and Clinical Immunology  
**Year:** 2014

The study represents the increasing use of molecular profiling to understand asthma heterogeneity.

---

### 4. Nicodemus-Johnson et al. — 2016

**Nicodemus-Johnson J et al.**

Research examining molecular features and gene-expression patterns associated with asthma.

**Journal:** JCI Insight  
**Year:** 2016  
**GEO Dataset:** GSE85568

This work contributed to the development of molecular approaches for studying asthma heterogeneity.

---

### 5. Alladina et al. — 2023

**Alladina J et al.**

Research using transcriptomic approaches to investigate molecular features of asthma.

**Journal:** Science Immunology  
**Year:** 2023  
**GEO Dataset:** GSE193816

The study represents the increasing application of high-throughput transcriptomic approaches to asthma research.

---

### 6. Do et al. — 2021

**Do AN et al.**

Research examining molecular characteristics of asthma using transcriptomic and related computational approaches.

**Journal:** Journal of Allergy and Clinical Immunology  
**Year:** 2021

**Data resource:** Synapse syn20687810

---

### 7. Szczesny et al. — 2024

**CAAPA Consortium / Szczesny et al.**

Research examining genetic, transcriptomic, and epigenetic features relevant to asthma.

**Journal:** Nature Communications  
**Year:** 2024  
**GEO Dataset:** GSE240567  
**Companion methylation dataset:** GSE250513

The work represents the integration of transcriptomic and epigenetic information in asthma research.

---

### 8. Lee et al. — 2025

**Lee I, Ganesan A, Kalesinskas L et al.**

*Multicohort Analysis of Bronchial Epithelial Cell Expression in Healthy Subjects and Patients with Asthma Reveals Four Clinically Distinct Clusters.*

**Journal:** American Journal of Respiratory Cell and Molecular Biology  
**Year:** 2025  
**Volume:** 73  
**Pages:** 73–87  
**GEO Dataset:** GSE115824

The study used multicohort transcriptomic analysis to identify clinically distinct molecular clusters in asthma and included an independent pediatric nasal-lavage validation cohort.

---

## Dataset Used for Practical Analysis

### GSE43696

The internship included practical exploration of the asthma-related GEO dataset **GSE43696**.

The workflow involved:

```text
GSE43696
   ↓
GEO2R
   ↓
Healthy vs Asthma Comparison
   ↓
Differential Gene Expression
   ↓
Significant Gene Selection
   ↓
GO / KEGG / g:Profiler
   ↓
STRING
   ↓
Cytoscape
   ↓
Hub-Gene Analysis
Research Timeline

The reviewed literature broadly represented the development of asthma molecular research from:

Early Gene-Expression Studies
          ↓
Microarray-Based Research
          ↓
Advanced Transcriptomics
          ↓
Multicohort Analysis
          ↓
Molecular Classification
          ↓
Clinical Translation
          ↓
Precision-Medicine Approaches
Note

The papers listed here were used as scientific reading and reference material during the internship. They should be consulted in their original publications for complete methodology, datasets, statistical methods, results, and conclusions.
