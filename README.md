# DYPBBI Summer Internship 2026 — Bioinformatics

### Learning Portfolio & Research Documentation

> My notes, practical work, analyses, research paper reviews, and learning from the Bioinformatics Summer Internship at Dr. D. Y. Patil Biotechnology & Bioinformatics Institute, Pune.

---

## About

This repository documents the work I completed during my **one-month Summer Internship in Bioinformatics** at **Dr. D. Y. Patil Biotechnology & Bioinformatics Institute (DYPBBI), Pune**.

The repository brings together the concepts I learned, biological databases and software I explored, practical analyses, research paper reviews, workshops, project work, and final internship documentation.

The internship covered a progression from **bioinformatics fundamentals and biological databases** to **transcriptomics, functional enrichment, network biology, structural bioinformatics, molecular docking, virtual screening, statistics, and scientific research and writing**.

Rather than keeping everything only in the final internship report, I have organised the learning and practical work here so that it can be referred to and built upon in future projects.

---

## Internship Details

| | |
|---|---|
| **Programme** | Summer Internship in Bioinformatics |
| **Institute** | Dr. D. Y. Patil Biotechnology & Bioinformatics Institute |
| **University** | Dr. D. Y. Patil Vidyapeeth |
| **Location** | Pune, Maharashtra |
| **Duration** | 1 July 2026 – 31 July 2026 |
| **Student** | Jishnu Raghavan G |
| **Home Institute** | Motilal Nehru National Institute of Technology Allahabad |
| **Programme** | B.Tech Biotechnology |
| **Status** | Completed |

---

# What I Learned

The internship provided exposure to the following areas:

### Bioinformatics & Biological Data
- Introduction to Bioinformatics
- Computational Biology
- Biological Data
- Genomic and Transcriptomic Data
- Bioinformatics Workflows
- Applications of Bioinformatics in Biomedical Research

### Biological Databases
- NCBI
- GEO
- UniProt
- PDB
- PDBsum
- STRING
- Gene Ontology
- KEGG
- g:Profiler
- AlphaFold
- SWISS-MODEL

### Transcriptomics
- Transcriptomics
- Gene Expression
- RNA Sequencing
- Microarray Technology
- GEO Datasets
- GEO2R
- Differential Gene Expression
- Log₂ Fold Change
- Adjusted p-values
- Statistical Filtering

### Functional & Network Analysis
- Gene Ontology Analysis
- KEGG Pathway Analysis
- Functional Enrichment
- Protein–Protein Interaction Analysis
- STRING
- Cytoscape
- Network Analysis
- Hub Gene Identification

### Structural Bioinformatics
- Protein Annotation
- Protein Sequences
- Protein Structures
- PDB Analysis
- PDBsum
- AlphaFold
- Homology Modelling
- SWISS-MODEL
- PyMOL
- ChimeraX

### Molecular Docking & Virtual Screening
- Medicinal Chemistry Basics
- Molecular Interactions
- Stereochemistry
- Isomerism
- Conformational Analysis
- Protein Preparation
- Ligand Preparation
- AutoDock Tools
- AutoDock Vina
- Molecular Docking
- Docking Analysis
- Virtual Screening

### Statistics & Biostatistics
- Descriptive Statistics
- Data Distribution
- Probability
- Hypothesis Testing
- p-values
- Confidence Intervals
- Correlation
- Statistical Significance
- Biological Data Analysis

### Scientific Research & Communication
- Research Methodology
- Literature Review
- Scientific Writing
- Scientific Ethics
- Plagiarism and Originality
- Referencing and Citations
- Mind Mapping
- Portfolio Management

---

# Overall Bioinformatics Workflow

One of the main things I understood during the internship was how different bioinformatics resources can be connected to investigate a biological question.

```text
Biological Question
        ↓
Database Exploration
        ↓
Dataset Selection
        ↓
Gene Expression Data
        ↓
Differential Gene Expression
        ↓
Functional Enrichment
        ↓
Pathway Analysis
        ↓
Protein–Protein Interaction
        ↓
Network Analysis
        ↓
Hub Gene Identification
        ↓
Protein Annotation
        ↓
Protein Structure Analysis
        ↓
Structure Prediction / Homology Modelling
        ↓
Protein Visualization
        ↓
Protein & Ligand Preparation
        ↓
Molecular Docking
        ↓
Virtual Screening
        ↓
Statistical & Biological Interpretation

A major takeaway was that the output of one stage can become the input for the next. A list of genes can therefore be explored through their functions, pathways, interactions, protein structures, and potential protein–ligand interactions.

01 — Bioinformatics Fundamentals

This section contains the fundamental concepts used throughout the internship.

Topics
Introduction to Bioinformatics
Computational Biology
Biological Data
Genomic Data
Transcriptomic Data
Role of Biological Databases
Applications of Bioinformatics
Bioinformatics in Biomedical Research
Bioinformatics in Drug Discovery
Bioinformatics Workflow
02 — Biological Databases

This section documents the major databases and resources explored during the internship.

Resource	Main Use
NCBI	Biological literature, sequences, datasets and other resources
GEO	Public gene expression datasets
UniProt	Protein annotation and functional information
PDB	Experimentally determined 3D structures
PDBsum	Structural summaries and interaction information
STRING	Protein–protein interaction networks
Gene Ontology	Functional annotation
KEGG	Biological and signalling pathways
g:Profiler	Functional enrichment analysis
AlphaFold	Predicted protein structures
SWISS-MODEL	Homology modelling
03 — Transcriptomics

This section covers the concepts used to study gene expression data.

Topics
Transcriptomics
Gene Expression
RNA Sequencing
Microarrays
Gene Expression Datasets
Disease vs Healthy Comparisons
GEO2R
Differential Gene Expression
Log₂ Fold Change
Adjusted p-values
Statistical Filtering
Interpretation of Gene Expression Results
04 — Asthma Transcriptomics Case Study

One of the major practical components of the internship was the analysis and interpretation of gene expression data related to asthma.

Dataset

GEO Accession: GSE43696

The dataset was explored through the NCBI Gene Expression Omnibus (GEO) and analysed using GEO2R.

Analysis Workflow
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
Functional Enrichment
     ↓
Pathway Analysis
     ↓
PPI Network
     ↓
Hub Gene Analysis

The selected genes were taken forward for functional and network-level interpretation.

Research Paper Study

Research papers related to asthma transcriptomics were also studied and discussed, with focus on:

Gene expression signatures
Master regulator genes
Hub genes
Molecular classification
Disease-associated pathways
Transcriptomic analysis
Precision medicine
05 — Functional & Network Analysis

After obtaining genes of interest, the next step was to understand their biological functions and relationships.

Gene Ontology

Analysis of:

Biological Process
Molecular Function
Cellular Component
KEGG

Used to investigate biological and signalling pathways associated with selected genes.

g:Profiler

Used for functional enrichment and interpretation of gene lists.

STRING

Used to explore protein–protein interactions and construct interaction networks.

Cytoscape

Used for:

Network visualisation
Network topology
Important nodes
Network clusters
Hub gene analysis
Biological interpretation
06 — Structural Bioinformatics

The internship then moved from gene-level analysis towards proteins and their three-dimensional structures.

Topics
Protein Annotation
Protein Sequences
Protein Structures
Experimental Structures
Predicted Structures
Protein Domains
Secondary Structures
Ligand-Binding Regions
Homology Modelling
Three-Dimensional Molecular Organisation
Resources & Software

UniProt
Protein annotation and functional information.

PDB
Retrieval and exploration of experimentally determined structures.

PDBsum
Structural summaries and protein–ligand or protein–protein interaction information.

AlphaFold
Exploration of predicted protein structures.

SWISS-MODEL
Introduction to homology modelling and structure prediction.

PyMOL
Three-dimensional protein structure visualisation and structural inspection.

07 — Molecular Docking & Virtual Screening

This section documents the computational concepts involved in early-stage drug discovery.

Supporting Concepts
Medicinal Chemistry Basics
Molecular Interactions
Stereochemistry
Isomerism
Conformational Analysis
Molecular Geometry
Protein Preparation

The preparation workflow included understanding:

Structure inspection
Removal of unwanted molecules
Handling structural issues
Preparation of proteins for docking
Ligand Preparation

Ligands were prepared for computational docking and interaction analysis.

Software
UCSF ChimeraX
AutoDock Tools
AutoDock Vina
PyMOL
Molecular Docking

The docking workflow was used to understand possible interactions between a target protein and ligand.

Topics
Docking Poses
Binding Affinity
Binding Sites
Protein–Ligand Interactions
Docking Result Interpretation
Virtual Screening

Virtual screening introduced the concept of computationally evaluating multiple compounds and prioritising potentially promising candidates for further investigation.

An important takeaway was that docking scores and computational predictions are not experimental proof and require biological interpretation and experimental validation.

08 — Statistics & Biostatistics

Statistical understanding is important when working with biological datasets.

Topics

Descriptive Statistics

Mean
Median
Mode
Range
Variance
Standard Deviation
Quartiles
Interquartile Range

Data Analysis

Data Distribution
Frequency Analysis
Graphical Representation
Outlier Identification

Probability & Statistics

Normal Distribution
Probability Concepts
Hypothesis Testing
p-values
Confidence Intervals
Correlation
Statistical Significance

The sessions helped me understand how statistical methods can support conclusions drawn from biological and experimental data.

09 — Scientific Research & Writing

The internship also covered the research and communication skills required alongside technical analysis.

Research Methodology
Research Planning
Experimental Design
Scientific Thinking
Documentation
Literature Review
Finding Relevant Papers
Reading Research Papers
Understanding Research Methodology
Comparing Scientific Findings
Presenting Research Papers
Scientific Writing
Research Paper Structure
Report Writing
Introduction
Methodology
Results
Discussion
Conclusion
Scientific Presentation
Scientific Ethics
Plagiarism Awareness
Original Writing
Citation Practices
Referencing
Publication Standards
Ethical Scientific Communication
Additional Skills
Mind Mapping
Portfolio Management
Scientific Documentation
10 — Workshops & Additional Learning

Alongside the core bioinformatics modules, several additional sessions and activities were conducted.

Scientific Writing Workshop

Covered scientific writing, research papers, review articles, internship reports, citations, references, clarity, and originality.

Biostatistics Workshop

Focused on statistical concepts and their application to biological data analysis.

Bioreactor Workshop

Introduced basic principles of bioreactors and upstream bioprocessing, including:

Bioreactor Components
Impellers and Agitators
Spargers
Baffles
Temperature Control
pH Control
Dissolved Oxygen
Aeration
Foam Control
Batch Fermentation
Fed-Batch Fermentation
Continuous Fermentation
Scale-Up
Laboratory Safety

Introduction to safety practices in academic and research environments.

Fire Safety & Emergency Drill

Covered:

Fire Prevention
Emergency Response
Fire Extinguisher Use
Emergency Exits
Evacuation Procedures
Laboratory Safety Protocols
Mind Mapping Session

Focused on organising scientific concepts and improving research planning.

Laboratory Visit

Provided exposure to the research environment, laboratory facilities, equipment, and working practices at the institute.

11 — Projects & Practical Work

This section contains the practical work completed during the internship.

Asthma Transcriptomics
GEO
 ↓
GSE43696
 ↓
GEO2R
 ↓
Differential Gene Expression
 ↓
Functional Enrichment
 ↓
Pathway Analysis
 ↓
PPI Network
 ↓
Hub Gene Analysis
Functional Enrichment
Gene Ontology
KEGG
g:Profiler
PPI Network Analysis
STRING
Cytoscape
Network Analysis
Hub Gene Identification
Protein Structure Analysis
UniProt
PDB
PDBsum
AlphaFold
SWISS-MODEL
PyMOL
Molecular Docking
Protein Preparation
Ligand Preparation
ChimeraX
AutoDock Tools
AutoDock Vina
Docking Analysis
Virtual Screening
12 — Research Paper Reviews

Research papers studied during the internship are documented separately.

The primary focus was on asthma and transcriptomic research, including:

Gene Expression Signatures
Master Regulator Genes
Molecular Classification
Hub Genes
Transcriptomic Datasets
Disease Mechanisms
Precision Medicine

The purpose of this section is to document what was understood from the papers and how the findings relate to the learning and analysis performed during the internship.

13 — Internship Documentation

The final internship deliverables are maintained here.

Final Internship Report
Final Presentation
Internship Documentation

The report consolidates the methodology, analysis and interpretation, future prospects, summary, references, and additional learning activities from the internship.

14 — Figures & Screenshots

Supporting figures and screenshots from the internship are organised separately for easy reference.

14-Figures-and-Screenshots/
│
├── Workflow/
├── NCBI/
├── GEO/
├── GEO2R/
├── STRING/
├── Cytoscape/
├── GO-KEGG/
├── Protein-Structures/
├── PyMOL/
├── Docking/
└── Workshops/

This keeps the main documentation readable while preserving the visual evidence from the practical sessions.

Tools & Technologies
Databases & Resources
NCBI
GEO
UniProt
PDB
PDBsum
STRING
Gene Ontology
KEGG
g:Profiler
AlphaFold
SWISS-MODEL
Software & Platforms
GEO2R
Cytoscape
PyMOL
UCSF ChimeraX
AutoDock Tools
AutoDock Vina
Google Colab
Jupyter Notebook
Programming
Python
Repository Structure
DYPBBI-Summer-Internship-2026-Bioinformatics/
DYPBBI-Summer-Internship-2026-Bioinformatics/
│
├── README.md
│
├── 01-Bioinformatics-Fundamentals/
│   ├── README.md
│   ├── Introduction-to-Bioinformatics.md
│   ├── Biological-Data.md
│   └── Bioinformatics-Workflow.md
│
├── 02-Biological-Databases/
│   ├── README.md
│   ├── NCBI.md
│   ├── GEO.md
│   ├── UniProt.md
│   ├── PDB.md
│   ├── PDBsum.md
│   ├── STRING.md
│   ├── Gene-Ontology.md
│   ├── KEGG.md
│   ├── gProfiler.md
│   ├── AlphaFold.md
│   └── SWISS-MODEL.md
│
├── 03-Transcriptomics/
│   ├── README.md
│   ├── Transcriptomics-Basics.md
│   ├── RNA-Seq-and-Microarray.md
│   ├── Gene-Expression.md
│   ├── GEO2R.md
│   ├── Differential-Gene-Expression.md
│   └── Code/
│       ├── Expression-Matrix-Analysis.py
│       ├── Differential-Expression-Analysis.py
│       ├── Heatmap-and-Volcano-Plot.py
│       └── README.md
│
├── 04-Asthma-Transcriptomics-Case-Study/
│   ├── README.md
│   ├── GSE43696.md
│   ├── GEO2R-Analysis.md
│   ├── Differentially-Expressed-Genes.md
│   ├── Functional-Enrichment.md
│   ├── PPI-Network-Analysis.md
│   ├── Hub-Gene-Analysis.md
│   ├── Research-Paper-Review.md
│   └── Code/
│       ├── GEO2R-Results-Processing.py
│       ├── DEG-Filtering.py
│       └── README.md
│
├── 05-Functional-and-Network-Analysis/
│   ├── README.md
│   ├── Gene-Ontology.md
│   ├── KEGG-Pathway-Analysis.md
│   ├── gProfiler.md
│   ├── STRING-PPI.md
│   ├── Cytoscape.md
│   ├── Hub-Gene-Analysis.md
│   └── Code/
│       ├── Gene-List-Preparation.py
│       ├── Enrichment-Data-Processing.py
│       ├── Network-Data-Processing.py
│       └── README.md
│
├── 06-Structural-Bioinformatics/
│   ├── README.md
│   ├── Protein-Annotation.md
│   ├── Protein-Structure.md
│   ├── PDB-Analysis.md
│   ├── PDBsum.md
│   ├── AlphaFold.md
│   ├── Homology-Modelling.md
│   ├── SWISS-MODEL.md
│   ├── PyMOL.md
│   └── Code/
│       ├── Protein-Sequence-Analysis.py
│       ├── Structure-Data-Processing.py
│       └── README.md
│
├── 07-Molecular-Docking-and-Virtual-Screening/
│   ├── README.md
│   ├── Medicinal-Chemistry.md
│   ├── Stereochemistry-and-Isomerism.md
│   ├── Conformational-Analysis.md
│   ├── Protein-Preparation.md
│   ├── Ligand-Preparation.md
│   ├── ChimeraX.md
│   ├── AutoDock-Tools.md
│   ├── AutoDock-Vina.md
│   ├── Molecular-Docking.md
│   ├── Docking-Analysis.md
│   ├── Virtual-Screening.md
│   └── Code/
│       ├── Docking-Results-Analysis.py
│       ├── Ligand-Data-Processing.py
│       └── README.md
│
├── 08-Statistics-and-Biostatistics/
│   ├── README.md
│   ├── Descriptive-Statistics.md
│   ├── Data-Distribution.md
│   ├── Probability.md
│   ├── Hypothesis-Testing.md
│   ├── P-Values.md
│   ├── Confidence-Intervals.md
│   ├── Correlation.md
│   ├── Biological-Data-Analysis.md
│   └── Code/
│       ├── Descriptive-Statistics.py
│       ├── Probability-and-Distributions.py
│       ├── Hypothesis-Testing.py
│       ├── Correlation-Analysis.py
│       └── README.md
│
├── 09-Scientific-Research-and-Writing/
│   ├── README.md
│   ├── Research-Methodology.md
│   ├── Literature-Review.md
│   ├── Scientific-Writing.md
│   ├── Scientific-Ethics.md
│   ├── Plagiarism-and-Originality.md
│   ├── Referencing-and-Citations.md
│   ├── Mind-Mapping.md
│   └── Portfolio-Management.md
│
├── 10-Workshops-and-Additional-Learning/
│   ├── README.md
│   ├── Scientific-Writing-Workshop.md
│   ├── Biostatistics-Workshop.md
│   ├── Bioreactor-Workshop.md
│   ├── Laboratory-Safety.md
│   ├── Fire-Safety-and-Emergency-Drill.md
│   ├── Mind-Mapping-Session.md
│   └── Laboratory-Visit.md
│
├── 11-Molecular-Docking-Project/
│   ├── README.md
│   │
│   ├── Notes/
│   │   ├── README.md
│   │   ├── Molecular-Docking-Concepts.md
│   │   ├── Medicinal-Chemistry-and-Ligands.md
│   │   ├── Stereochemistry-and-Isomerism.md
│   │   ├── Conformational-Analysis.md
│   │   ├── Protein-Preparation.md
│   │   ├── Ligand-Preparation.md
│   │   ├── ChimeraX.md
│   │   ├── AutoDock-Tools.md
│   │   ├── AutoDock-Vina.md
│   │   ├── Docking-Procedure.md
│   │   ├── Docking-Analysis.md
│   │   └── Virtual-Screening.md
│   
│   
│   
│   
│   
│   
│   
│
├── 12-Research-Paper-Reviews/
│   ├── README.md
│   ├── Asthma-Transcriptomics-Paper-1.md
│   ├── Asthma-Transcriptomics-Paper-2.md
│   └── Asthma-Transcriptomics-Paper-3.md
│
├── 13-Internship-Documentation/
│   └── Final-Internship-Report.pdf
│
└── 14-References/
    ├── Databases.md
    ├── Software.md
    ├── Books.md
    └── Research-Papers.md
Key Takeaways

The biggest thing I took away from the internship was understanding how computational tools can be connected to a biological problem.

A list of genes by itself does not tell the complete story.

Genes
  ↓
Functions
  ↓
Pathways
  ↓
Protein Interactions
  ↓
Network Biology
  ↓
Protein Structures
  ↓
Protein–Ligand Interactions
  ↓
Potential Therapeutic Targets

I also learned that computational results need to be interpreted carefully. Statistical thresholds, database evidence, network confidence, structural quality, and docking predictions can all influence the final interpretation.

The software output is therefore only one part of the process. Understanding the biology behind the result is equally important.

Skills Developed

By the end of the internship, I had gained practical exposure to:

Working with biological datasets
Navigating biological databases
Transcriptomic data analysis
Differential gene expression
Functional enrichment
Pathway analysis
Protein–protein interaction networks
Biological network visualisation
Protein annotation
Protein structure analysis
Structure prediction
Homology modelling
Molecular visualisation
Protein and ligand preparation
Molecular docking
Docking result interpretation
Virtual screening
Basic statistical analysis
Scientific literature review
Scientific writing
Research documentation
Future Learning

This internship provided a foundation for exploring more advanced areas of computational biology.

Areas I would like to explore further include:

Advanced Transcriptomics
RNA-seq Analysis
Cancer Genomics
Multi-omics
Systems Biology
Structural Bioinformatics
Molecular Dynamics
Protein Engineering
Computational Drug Discovery
Pharmacogenomics
Precision Medicine
Machine Learning in Bioinformatics
AI-assisted Drug Discovery
References

Detailed references used during the internship are maintained in the References/ directory.

These include:

Biological Databases
Software and Computational Tools
Books and Textbooks
Research Papers
Other Learning Resources
Acknowledgement

I am grateful to Dr. D. Y. Patil Biotechnology & Bioinformatics Institute, Pune, and the faculty and mentors involved in the internship for providing me with the opportunity to learn and work across different areas of bioinformatics.

I am also thankful to Motilal Nehru National Institute of Technology Allahabad for supporting this learning experience.

Final Note

This repository is primarily a record of my learning and practical work during the internship.

Some sections contain concepts and notes, while others contain practical analyses, figures, screenshots, research paper reviews, and internship documentation. I have organised them so that I can return to these topics later and continue building on them through future projects and research.

Internship completed — learning continues.


