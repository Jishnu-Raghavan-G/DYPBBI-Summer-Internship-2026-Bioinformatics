# Functional and Network Analysis Code

## Overview

This folder contains Python scripts created as reusable examples for processing data generated during functional and network-level bioinformatics analysis.

The scripts are designed to connect the output of differential-expression analysis with downstream analysis such as:

- Gene Ontology (GO)
- KEGG pathway analysis
- g:Profiler
- STRING PPI analysis
- Cytoscape
- Hub-gene analysis

The internship included these functional and network-analysis concepts as part of the downstream analysis workflow. :contentReference[oaicite:0]{index=0}

---

## Files

### `Gene-List-Preparation.py`

Prepares a clean gene list from differential-expression results.

The script demonstrates:

- Loading DEG results
- Removing missing values
- Removing duplicate genes
- Applying adjusted p-value filtering
- Applying log2FC filtering
- Separating upregulated and downregulated genes
- Exporting gene lists

Basic workflow:

```text
DEG Results
    ↓
Clean Data
    ↓
Statistical Filtering
    ↓
Selected Genes
    ↓
Gene List
Enrichment-Data-Processing.py

Processes functional-enrichment results.

The script demonstrates:

Loading enrichment results
Cleaning missing values
Converting statistical columns
Filtering by adjusted p-value
Sorting enriched terms
Creating summary tables
Exporting processed results

Basic workflow:

GO / KEGG / g:Profiler
          ↓
   Enrichment Results
          ↓
      Data Cleaning
          ↓
   Significance Filtering
          ↓
    Processed Results
Network-Data-Processing.py

Processes protein-protein interaction data.

The script demonstrates:

Loading interaction data
Removing missing values
Removing self-interactions
Removing duplicate interactions
Applying an example confidence threshold
Calculating protein degree
Identifying candidate highly connected proteins
Exporting network tables

Basic workflow:

STRING Interaction Data
          ↓
     Data Cleaning
          ↓
   Confidence Filtering
          ↓
      PPI Network
          ↓
    Degree Analysis
          ↓
 Candidate Hub Proteins
How These Scripts Connect

The three scripts can be viewed as a simplified computational workflow:

                    Differential
                  Expression Results
                         │
                         ↓
                Gene-List-Preparation.py
                         │
                         ↓
                    Gene List
                    /        \
                   /          \
                  ↓            ↓
        GO / KEGG /        STRING PPI
        g:Profiler             │
             ↓                  ↓
   Enrichment Results    Network Data
             ↓                  ↓
 Enrichment-Data-       Network-Data-
 Processing.py          Processing.py
             │                  │
             ↓                  ↓
   Functional Results     Network Results
                                │
                                ↓
                         Hub-Gene Analysis

This represents the general progression from differentially expressed genes to functional and network-level interpretation.

Important Note About the Internship Analysis

These scripts are included as reusable learning and portfolio examples.

They should not be interpreted as claiming that every step was performed using these exact Python scripts during the internship.

The documented practical workflow used GEO/GEO2R for the GSE43696 transcriptomics analysis, followed by differential-expression interpretation and downstream functional and network analysis.

The internship methodology included lectures, practical demonstrations, computational exercises, research assignments and scientific discussions.

Requirements

The scripts use Python and primarily rely on:

Python 3
pandas

Install pandas using:

pip install pandas
Example Directory
05-Functional-and-Network-Analysis/
│
├── README.md
├── Gene-Ontology.md
├── KEGG-Pathway-Analysis.md
├── gProfiler.md
├── STRING-PPI.md
├── Cytoscape.md
├── Hub-Gene-Analysis.md
│
└── Code/
    ├── Gene-List-Preparation.py
    ├── Enrichment-Data-Processing.py
    ├── Network-Data-Processing.py
    └── README.md
Scientific Interpretation

The code should be treated as a supporting component of the analysis rather than a replacement for biological interpretation.

A typical analysis progresses through several levels:

Gene
 ↓
Differential Expression
 ↓
Functional Annotation
 ↓
Pathway Analysis
 ↓
Protein Interaction
 ↓
Network Analysis
 ↓
Candidate Hub Genes
 ↓
Biological Interpretation

Each stage provides a different type of information.

Key Learning

The main computational lesson from this section was that bioinformatics analysis often involves moving data between different levels of biological interpretation.

A list of genes can become:

Gene List
   ↓
Functional Terms
   ↓
Pathways
   ↓
Protein Interactions
   ↓
Network
   ↓
Candidate Hub Genes

This helped me understand how transcriptomic results can be connected to functional and network-level biological interpretation.

Reproducibility

For a reproducible analysis, the following should be documented:

Input dataset
Gene identifiers
Organism
Filtering criteria
Adjusted p-value threshold
log2FC threshold
Background gene set
Enrichment database/tool
STRING interaction settings
Network confidence threshold
Hub-identification method
Software versions
Date of analysis

Keeping these details makes it easier for another researcher to understand and reproduce the analysis.

Final Takeaway

The purpose of these scripts is not simply to automate calculations.

They demonstrate how computational processing can support the biological workflow:

Data
 ↓
Cleaning
 ↓
Filtering
 ↓
Analysis
 ↓
Visualization
 ↓
Interpretation

The final biological conclusions should always be based on the complete experimental context rather than on a single computational output.
