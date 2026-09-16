# Software

This file lists the major software tools and computational platforms introduced, explored, or used during the Bioinformatics Summer Internship 2026.

## GEO2R

**GEO2R** is a web-based tool associated with the NCBI Gene Expression Omnibus (GEO) for comparing gene-expression profiles between selected groups of samples.

It was used during the asthma transcriptomics workflow for:

- Exploring GEO datasets
- Comparing healthy and asthma samples
- Differential gene-expression analysis
- Identifying genes showing significant expression differences

The practical analysis included the asthma-related dataset **GSE43696**.

---

## Cytoscape

**Cytoscape** is an open-source platform for visualizing and analysing biological networks.

It was introduced for:

- Protein-protein interaction network visualization
- Network exploration
- Identification of highly connected genes or proteins
- Hub-gene analysis
- Interpretation of molecular interaction networks

Cytoscape was used together with STRING-based interaction data in the functional and network-analysis workflow.

---

## PyMOL

**PyMOL** is a molecular visualization tool used for viewing and analysing three-dimensional biological structures.

It was introduced as part of structural bioinformatics learning for:

- Protein structure visualization
- Examination of three-dimensional molecular structures
- Structural interpretation
- Visualization of molecular interactions

---

## ChimeraX

**UCSF ChimeraX** is a molecular visualization and analysis program used to work with biological macromolecular structures.

It was introduced during the molecular docking training for:

- Protein structure visualization
- Structural inspection
- Protein preparation
- Examination of molecular structures
- Understanding protein-ligand interactions

---

## AutoDock Tools

**AutoDock Tools (ADT)** provides tools for preparing molecular structures and setting up AutoDock-based molecular docking workflows.

It was introduced during the docking sessions for:

- Protein preparation
- Ligand preparation
- Docking setup
- Preparing structures for docking calculations

---

## AutoDock Vina

**AutoDock Vina** is a molecular docking software used to investigate possible binding modes between proteins and ligands.

It was introduced for understanding:

- Molecular docking
- Docking poses
- Predicted binding affinity
- Protein-ligand interactions
- Binding-site analysis
- Interpretation of docking results

The docking results were understood as computational predictions rather than experimental confirmation of binding.

---

## Python

**Python** was used as a programming language for computational and biological data analysis.

Applications relevant to the internship and repository include:

- Data processing
- Biological-data handling
- Statistical analysis
- Gene-expression data processing
- Data visualization

### Common Python Libraries

#### NumPy

Used for numerical and array-based operations.

#### Pandas

Used for handling tabular datasets and performing data-processing operations.

#### Matplotlib

Used for creating plots and visualizing analytical results.

#### Seaborn

Used for statistical data visualization and exploratory analysis.

---

## Software by Learning Area

| Learning Area | Software / Platform |
|---|---|
| Transcriptomics | GEO2R |
| Network Analysis | Cytoscape |
| Molecular Visualization | PyMOL |
| Molecular Visualization & Preparation | ChimeraX |
| Docking Preparation | AutoDock Tools |
| Molecular Docking | AutoDock Vina |
| Computational Analysis | Python |
| Numerical Analysis | NumPy |
| Data Processing | Pandas |
| Data Visualization | Matplotlib, Seaborn |

---

## Overall Computational Workflow

The major software tools fit into different stages of the internship workflow:

```text
Biological Dataset
        ↓
GEO / GEO2R
        ↓
Differential Gene Expression
        ↓
GO / KEGG / g:Profiler
        ↓
STRING
        ↓
Cytoscape
        ↓
Protein Structure Resources
        ↓
PyMOL / ChimeraX
        ↓
Protein & Ligand Preparation
        ↓
AutoDock Tools
        ↓
AutoDock Vina
        ↓
Docking Analysis
Important Note

The software listed here represents tools introduced, explored, or used during the internship and in the associated learning workflow.

Their inclusion does not mean that every tool was used for an independent research project. The purpose of this section is to document the computational tools encountered during the internship and their role in the broader bioinformatics workflow.
