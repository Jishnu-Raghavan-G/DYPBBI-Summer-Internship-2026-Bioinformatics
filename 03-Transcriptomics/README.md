# Transcriptomics

This section contains the concepts and practical approaches I learned during my bioinformatics internship for studying gene expression and transcriptomic data.

The main focus was on understanding how expression data can be obtained from public databases, compared between biological conditions, and interpreted to identify genes showing meaningful changes.

## What I Learned

The transcriptomics training covered:

- Basic concepts of transcriptomics
- Gene expression and regulation
- RNA and different RNA types
- Microarray technology
- RNA sequencing concepts
- Public gene-expression datasets
- NCBI Gene Expression Omnibus (GEO)
- GEO2R
- Differential gene expression
- Fold change and log2 fold change
- P-values and adjusted p-values
- Statistical filtering
- Interpretation of differentially expressed genes

The internship specifically included the use of publicly available asthma-related microarray data from GEO and GEO2R for comparing healthy and disease samples. :contentReference[oaicite:0]{index=0}

## Section Structure

```text
03-Transcriptomics/
│
├── README.md
│
├── Transcriptomics-Basics.md
├── RNA-Seq-and-Microarray.md
├── Gene-Expression.md
├── GEO2R.md
├── Differential-Gene-Expression.md
│
└── Code/
    ├── Expression-Matrix-Analysis.py
    ├── Differential-Expression-Analysis.py
    ├── Heatmap-and-Volcano-Plot.py
    └── README.md

The Markdown files contain the concepts and workflow, while the Code/ directory contains Python programs used to understand and practise computational analysis.

General Workflow

The basic transcriptomics workflow I learned can be represented as:

Biological Question
        ↓
Public Gene-Expression Dataset
        ↓
GEO
        ↓
Sample Selection
        ↓
GEO2R / Differential Expression
        ↓
Statistical Filtering
        ↓
Significant Genes
        ↓
Functional Interpretation
        ↓
Network Analysis

This workflow later connected with the asthma transcriptomics case study and the functional/network analysis sections of the repository.

Why Transcriptomics Was Important

One of the useful ideas I took from this part of the internship was that a gene-expression dataset is not just a table of numbers.

The expression differences can be used as a starting point for asking biological questions:

Expression Changes
        ↓
Which genes changed?
        ↓
What do these genes do?
        ↓
Which pathways are involved?
        ↓
Which proteins interact?
        ↓
What biological processes may be affected?

This helped me understand how transcriptomic analysis can connect computational data with biological interpretation.

Connection With the Internship Case Study

The transcriptomics concepts were applied later to an asthma-related case study using GEO dataset GSE43696.

The dataset was explored through GEO and analysed using GEO2R. The resulting genes were then taken forward for functional enrichment and protein–protein interaction analysis.

The detailed case study is maintained separately in:

04-Asthma-Transcriptomics-Case-Study/
Code

The Code/ directory contains beginner-level Python programs for understanding the computational side of transcriptomics.

Expression Matrix Analysis
Code/Expression-Matrix-Analysis.py

Used to understand how gene-expression matrices can be loaded, inspected, cleaned, and explored using Python.

Differential Expression Analysis
Code/Differential-Expression-Analysis.py

Contains a learning implementation of comparing expression between two groups and calculating values such as fold change and statistical significance.

Heatmap and Volcano Plot
Code/Heatmap-and-Volcano-Plot.py

Contains visualization examples for examining gene-expression patterns and differential-expression results.

Important Note About the Code

The Python programs in this section are learning and demonstration workflows.

They should not be interpreted as a replacement for the exact GEO2R analysis performed during the internship. GEO2R was used directly for the public GEO dataset analysis, while Python provides an additional way to understand and process expression data computationally.

For real datasets, experimental design, biological replicates, normalization, statistical methods, multiple-testing correction, and appropriate biological interpretation must all be considered.

Learning Outcome

By completing this section, I developed an understanding of how transcriptomic data moves from a biological question to computational analysis.

The main progression was:

RNA Biology
     ↓
Gene Expression
     ↓
Microarray / RNA-seq
     ↓
Public Expression Data
     ↓
GEO
     ↓
GEO2R
     ↓
Differential Expression
     ↓
Significant Gene List
     ↓
Functional and Network Analysis

This provided the foundation for the asthma transcriptomics case study that follows.
