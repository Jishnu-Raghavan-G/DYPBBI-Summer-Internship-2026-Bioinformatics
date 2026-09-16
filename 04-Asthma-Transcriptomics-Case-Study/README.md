Overview

This folder contains the main transcriptomics case study carried out during the bioinformatics internship.

The case study focuses on asthma-related gene-expression analysis using a publicly available Gene Expression Omnibus (GEO) dataset, GSE43696. The analysis was based on comparing gene-expression patterns between healthy and asthma samples and then using the resulting genes for downstream functional and network analysis.

Case Study Workflow

The overall workflow followed during the case study can be summarized as:

GSE43696
   ↓
GEO Database
   ↓
GEO2R
   ↓
Healthy vs Asthma Comparison
   ↓
Differential Gene Expression
   ↓
Statistical Filtering
   ↓
Selected Differentially Expressed Genes
   ↓
Functional Enrichment
   ↓
PPI Network Analysis
   ↓
Hub-Gene Analysis

This connects the transcriptomics concepts learned during the internship with a disease-focused biological question.

Dataset
GSE43696

GSE43696 is the GEO accession used for the asthma transcriptomics case study.

The dataset was accessed through the NCBI Gene Expression Omnibus (GEO) platform and analyzed using GEO2R.

The main comparison considered:

Healthy samples
        vs
Asthma samples

The purpose was to identify differences in gene-expression patterns associated with the asthma condition.

More details about the dataset and its analysis are documented in:

GSE43696.md
GEO2R-Analysis.md
Differential Gene Expression

Differential gene-expression analysis was used to identify genes whose expression differed between the groups.

Important concepts involved included:

Gene-expression values
Fold change
log2 fold change
p-values
Adjusted p-values
Statistical filtering
Upregulated genes
Downregulated genes

The internship notes specifically included log2FC, adjusted p-values and statistical filtering as part of the transcriptomics workflow.

The resulting genes were then taken forward for biological interpretation.

Functional Analysis

After obtaining the relevant differentially expressed genes, functional analysis was used to investigate their biological significance.

The downstream analysis included:

Gene Ontology (GO)
KEGG pathway analysis
g:Profiler

These approaches help connect a list of genes with biological processes, molecular functions, cellular components and pathways.

The detailed analysis is documented in:

Functional-Enrichment.md
Protein-Protein Interaction Analysis

The selected genes were also examined from a network perspective.

STRING was used for protein-protein interaction analysis, followed by visualization and exploration of the resulting network using Cytoscape.

This allowed the analysis to move from individual genes toward relationships between proteins and genes within a biological network.

Hub-Gene Analysis

Network analysis can identify highly connected nodes within a PPI network.

These highly connected genes or proteins can then be examined as potential hub genes within the analyzed network.

The internship workflow included STRING, Cytoscape and hub-gene analysis as downstream components of the asthma transcriptomics case study.

The detailed discussion is provided in:

Hub-Gene-Analysis.md
Research Paper Review

The case study was complemented by reviewing research papers related to asthma transcriptomics and gene-expression research.

The reviewed topics included:

Gene-expression signatures
Master regulators
Hub genes
Molecular classification
Disease-associated pathways
Precision medicine

These reviews helped connect computational analysis with published biological research.

The individual paper reviews are maintained separately under:

12-Research-Paper-Reviews/
Figures

Important screenshots and visual outputs from the analysis are organized under:

04-Asthma-Transcriptomics-Case-Study/Figures/

These may include:

GEO/GEO2R screenshots
Differential-expression plots
Enrichment results
STRING networks
Cytoscape networks
Hub-gene visualizations

Additional general screenshots are maintained in:

14-Figures-and-Screenshots/
Code

The Code/ directory contains supporting Python scripts for processing and organizing analysis results:

Code/
├── GEO2R-Results-Processing.py
├── DEG-Filtering.py
└── README.md

These scripts are intended to support data handling and reproducibility.

They should not be interpreted as replacing GEO2R or other specialized statistical tools used for the original analysis.

Learning Outcome

This case study helped connect several major areas of bioinformatics into one workflow:

Biological Database
        ↓
Transcriptomics
        ↓
Differential Expression
        ↓
Functional Enrichment
        ↓
Protein Interaction Network
        ↓
Hub-Gene Analysis
        ↓
Biological Interpretation

It provided practical exposure to how publicly available gene-expression data can be investigated computationally and then connected to biological pathways and interaction networks.

Repository Note

The case study is documented separately from the general transcriptomics notes so that the repository distinguishes between:

Concepts learned → 03-Transcriptomics/
Actual asthma case study → 04-Asthma-Transcriptomics-Case-Study/
General functional/network methods → 05-Functional-and-Network-Analysis/
Research-paper reviews → 12-Research-Paper-Reviews/

This separation keeps the repository organized and avoids repeating the same material across multiple files.
