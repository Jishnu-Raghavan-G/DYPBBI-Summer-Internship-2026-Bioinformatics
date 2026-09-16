Overview

This section covers the functional and network-based methods used to move from a list of genes toward biological interpretation.

The internship workflow used Gene Ontology (GO), KEGG, g:Profiler, STRING and Cytoscape for functional and network analysis. These methods were also applied as downstream steps after the asthma transcriptomics analysis.

Why Functional and Network Analysis?

Differential-expression analysis gives us genes that differ between biological conditions.

However, a list of genes does not immediately explain:

What biological processes are involved
Which pathways are represented
How the associated proteins interact
Which nodes are highly connected
What biological themes may be present in the dataset

Functional and network analysis provides additional layers of interpretation.

Differentially Expressed Genes
            ↓
    ┌───────┴────────┐
    ↓                ↓
Functional         Network
Analysis           Analysis
    ↓                ↓
GO / KEGG        STRING / Cytoscape
g:Profiler           ↓
    ↓            Hub Analysis
Biological            ↓
Functions          Network
and Pathways      Interpretation
Main Tools Covered
Gene Ontology

GO analysis is used to organize genes according to:

Biological Process
Molecular Function
Cellular Component

This helps describe the biological functions represented by a gene set.

KEGG

KEGG can be used to investigate pathways associated with a set of genes.

It provides a pathway-level perspective instead of examining each gene independently.

g:Profiler

g:Profiler provides tools for functional profiling of gene lists and can be used to investigate enriched biological annotations and pathways.

It was included in the internship's functional-analysis workflow alongside GO and KEGG.

STRING

STRING was used to investigate protein-protein interaction networks.

It provides a way of examining relationships between proteins associated with the genes being studied.

Cytoscape

Cytoscape was used to visualize and explore biological networks.

It allows nodes and their relationships to be represented graphically and supports further network analysis.

Overall Workflow

The general workflow covered in this section is:

Gene List
   ↓
Gene Identifier Preparation
   ↓
┌───────────────┬────────────────┐
↓               ↓
GO / KEGG       STRING
g:Profiler         ↓
↓              PPI Network
Functional          ↓
Enrichment       Cytoscape
                    ↓
                Hub Genes
Connection to the Asthma Case Study

The GSE43696 asthma analysis followed a similar progression:

GSE43696
   ↓
GEO2R
   ↓
Differential Expression
   ↓
Selected Genes
   ↓
GO / KEGG / g:Profiler
   ↓
STRING
   ↓
Cytoscape
   ↓
Hub-Gene Analysis

This workflow is documented in the internship material as the main downstream analysis following the asthma transcriptomics component.

Functional Analysis vs Network Analysis

These approaches answer different questions.

Analysis	Main Question
Gene Ontology	What functions are represented?
KEGG	Which pathways are represented?
g:Profiler	Which functional annotations are enriched?
STRING	How are associated proteins connected?
Cytoscape	How can the network be visualized and explored?
Hub-gene analysis	Which nodes have high connectivity?

They can therefore be used together rather than as interchangeable tools.

Interpretation

A useful way to think about the complete analysis is:

Genes
 ↓
Functions
 ↓
Pathways
 ↓
Protein interactions
 ↓
Network structure
 ↓
Biological interpretation

Each step adds another layer of information.

Importantly, enrichment or network connectivity alone does not establish that a particular gene or pathway causes a disease. The computational findings need to be interpreted alongside experimental evidence and published literature.

Code

The Code/ directory contains supporting Python scripts:

Code/
├── Gene-List-Preparation.py
├── Enrichment-Data-Processing.py
├── Network-Data-Processing.py
└── README.md

These scripts are intended primarily for organizing and processing analysis data.

They do not replace the specialized databases and software used for functional and network analysis.

Repository Organization

The detailed concepts are separated into individual files:

Gene-Ontology.md
KEGG-Pathway-Analysis.md
gProfiler.md
STRING-PPI.md
Cytoscape.md
Hub-Gene-Analysis.md

This keeps each method understandable on its own while allowing them to be connected through the overall workflow.

Learning Outcome

This section helped me understand how bioinformatics can move beyond simply identifying differentially expressed genes.

The main progression was:

Differential Expression
        ↓
Functional Enrichment
        ↓
Pathway Analysis
        ↓
Protein Interaction
        ↓
Network Visualization
        ↓
Hub Analysis
        ↓
Biological Interpretation

This was one of the major computational components of the internship and formed an important bridge between transcriptomics data and biological interpretation.
