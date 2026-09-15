# Introduction to Bioinformatics

Bioinformatics is an interdisciplinary field that combines **biology, computer science, mathematics, statistics, and information technology** to study and interpret biological data.

Modern biological research produces a huge amount of data from techniques such as DNA sequencing, RNA analysis, protein studies and other high-throughput experiments. Bioinformatics provides computational methods to store, organize, analyse and interpret this data.

In simple terms:

> **Bioinformatics uses computation to answer biological questions.**

For example, instead of manually comparing thousands of DNA sequences, a computer can compare them, identify similarities, find mutations and help determine their possible biological significance.

---

## 1. What is Bioinformatics?

Bioinformatics deals with biological information in a computational way.

It involves three basic activities:

### 1. Data Representation

Biological information can be complex, so it is converted into formats that computers can process and researchers can interpret.

Examples:

- DNA sequences represented using nucleotide letters
- Protein sequences represented using amino-acid letters
- Gene expression represented using numerical values
- Biological networks represented as nodes and connections
- Protein structures represented as three-dimensional coordinates

### 2. Data Storage and Retrieval

Biological experiments generate large datasets. These datasets need to be stored in organised databases so that researchers can retrieve and reuse them.

Examples include:

- DNA and RNA sequence databases
- Gene expression databases
- Protein databases
- Protein structure databases
- Scientific literature databases

### 3. Data Analysis

Raw biological data usually does not directly provide an answer.

Computational and statistical methods are used to find patterns and relationships in the data.

Examples:

- Comparing DNA or protein sequences
- Identifying differentially expressed genes
- Finding biological pathways
- Studying protein interactions
- Analysing protein structures
- Predicting molecular interactions

The internship helped me understand that these three parts are closely connected: **biological data has to be represented properly, stored systematically and then analysed to obtain useful biological information.**

---

# 2. Bioinformatics and Computational Biology

The terms **bioinformatics** and **computational biology** are closely related, and they are often used together.

### Bioinformatics

Bioinformatics generally focuses more on:

- Managing biological data
- Developing and using databases
- Developing computational tools
- Processing biological datasets
- Analysing sequences and other biological information

### Computational Biology

Computational biology focuses more on using computational and mathematical approaches to understand biological systems and mechanisms.

Examples include:

- Modelling biological systems
- Studying gene regulatory networks
- Predicting protein structures
- Simulating molecular interactions
- Analysing biological networks
- Building computational models of disease processes

There is considerable overlap between the two fields.

A simple way to remember the difference is:

> **Bioinformatics → managing and analysing biological information**

> **Computational biology → using computation to understand biological systems**

In actual research, both approaches are often used together.

---

# 3. Why Bioinformatics is Important

Biological research has moved from relatively small datasets to extremely large datasets.

For example, sequencing technologies can generate millions or billions of sequence reads. Similarly, transcriptomic experiments can measure the expression of thousands of genes at the same time.

Manually analysing this amount of information is not practical.

Bioinformatics helps researchers:

- Handle large biological datasets
- Find patterns in biological data
- Compare sequences
- Identify important genes
- Study gene expression
- Understand biological pathways
- Analyse protein interactions
- Study protein structures
- Identify potential drug targets
- Support disease research

The important point is that bioinformatics does not replace biological experiments. Instead, it helps researchers make sense of the data produced by those experiments.

---

# 4. Types of Biological Data

During the internship, I came across different types of biological data.

## 4.1 Genomic Data

Genomic data describes the DNA of an organism.

It can include:

- DNA sequences
- Genes
- Genetic variants
- Mutations
- Genomic regions

A DNA sequence is represented using four main nucleotides:

```text
A = Adenine
T = Thymine
G = Guanine
C = Cytosine

Example:

ATGCGTACCGAT

Bioinformatics can be used to compare such sequences, identify variations and study genes or genomic regions.

4.2 Transcriptomic Data

Transcriptomics deals with the collection of RNA molecules, particularly gene expression, in a biological sample.

A transcriptomic experiment can help answer questions such as:

Which genes are active?
Which genes are expressed more strongly?
Which genes are expressed less strongly?
How does gene expression differ between healthy and diseased samples?

For example:

Healthy       → Gene A: 100
Asthma        → Gene A: 250

The difference in expression can indicate that Gene A may be associated with the condition being studied.

During the internship, this concept was later applied to an asthma gene-expression dataset using GEO and GEO2R.

4.3 Proteomic Data

Proteomics deals with proteins present in a biological system.

Protein-related information can include:

Protein sequences
Protein functions
Protein structures
Protein domains
Protein interactions
Protein abundance

This connects bioinformatics with structural biology and molecular docking.

4.4 Structural Data

Structural bioinformatics deals with the three-dimensional structures of biological molecules, especially proteins.

A protein structure can provide information about:

Overall protein shape
Secondary structures
Binding regions
Active sites
Interactions with other molecules

Structures can be obtained experimentally or predicted computationally.

5. The Central Dogma of Molecular Biology

A basic understanding of the Central Dogma is important before studying bioinformatics because many bioinformatics datasets are related to DNA, RNA and proteins.

The simplified flow of genetic information is:

DNA
 ↓
RNA
 ↓
Protein

This represents:

DNA --transcription--> RNA --translation--> Protein
5.1 DNA

DNA is the main hereditary material of cells.

It contains the genetic information required for the growth, development and functioning of an organism.

DNA consists of nucleotides containing four bases:

A — Adenine
T — Thymine
G — Guanine
C — Cytosine

A gene is a region of DNA that contains information needed to produce a functional product, such as a protein or functional RNA.

5.2 Transcription

Transcription is the process in which information from DNA is used to produce RNA.

The enzyme mainly responsible is RNA polymerase.

The basic stages are:

Initiation
    ↓
Elongation
    ↓
Termination
Initiation

RNA polymerase binds to the appropriate region of DNA, including the promoter region.

Elongation

RNA polymerase moves along the DNA template and synthesises an RNA strand.

Termination

When the appropriate termination signal is reached, transcription stops and the RNA molecule is released.

5.3 Types of RNA

Some important types of RNA are:

mRNA — Messenger RNA

Carries genetic information used for protein synthesis.

rRNA — Ribosomal RNA

Forms an important structural and functional component of ribosomes.

tRNA — Transfer RNA

Carries amino acids to the ribosome during protein synthesis.

5.4 Translation

Translation is the process in which the information in mRNA is used to produce a protein.

It occurs at the ribosome.

The basic stages are:

Initiation
    ↓
Elongation
    ↓
Termination

During translation, tRNA molecules bring amino acids according to the codons present in the mRNA.

The amino acids are joined together to form a polypeptide chain, which can fold into a functional protein.

6. Why the Central Dogma Matters in Bioinformatics

The Central Dogma helps connect different types of biological data.

For example:

DNA
 ↓
Gene
 ↓
RNA
 ↓
Gene Expression
 ↓
Protein
 ↓
Protein Function
 ↓
Protein Structure
 ↓
Molecular Interaction

This is one reason bioinformatics is useful across multiple biological fields.

A change in DNA can potentially affect RNA expression or protein function, while changes in gene expression can provide information about disease mechanisms.

This connection becomes particularly important when combining transcriptomics, protein annotation, structural biology and molecular docking.

7. Biological Databases

Biological databases are an important part of bioinformatics.

They provide organised access to biological information collected from experiments, publications and computational studies.

Different databases specialise in different types of information.

Examples explored during the internship include:

Resource	Main use
NCBI	Access to multiple biological resources
GEO	Gene expression datasets
UniProt	Protein sequence and functional information
PDB	Experimentally determined 3D structures
PDBsum	Structural summaries
STRING	Protein–protein interaction information
Gene Ontology	Functional classification
KEGG	Biological and signalling pathways
g:Profiler	Functional enrichment
AlphaFold	Predicted protein structures
SWISS-MODEL	Homology modelling

These resources are covered in greater detail in the later Biological Databases section of this repository.

8. Applications of Bioinformatics

Bioinformatics is used in many areas of modern biology and medicine.

8.1 Genomics

Bioinformatics can be used to:

Analyse DNA sequences
Compare genomes
Identify genetic variants
Study mutations
Annotate genes
8.2 Transcriptomics

Bioinformatics helps analyse gene-expression data to determine how gene activity changes between different conditions.

For example:

Healthy samples
        vs
Disease samples
        ↓
Gene expression comparison
        ↓
Differentially expressed genes

This type of analysis was later used in the internship's asthma transcriptomics case study.

8.3 Biomedical Research

Bioinformatics can help researchers study diseases at the molecular level.

It can be used to:

Identify disease-associated genes
Study molecular pathways
Compare healthy and diseased tissues
Identify potential biomarkers
Study molecular mechanisms of disease
Support precision medicine research

For example, gene-expression data can reveal genes whose activity differs between healthy and diseased samples.

8.4 Drug Discovery

Bioinformatics also plays an important role in computational drug discovery.

A simplified workflow is:

Disease
   ↓
Identify important gene/protein
   ↓
Study protein function
   ↓
Study protein structure
   ↓
Identify binding site
   ↓
Prepare protein and ligand
   ↓
Molecular docking
   ↓
Compare potential compounds

Docking and virtual screening were covered later in the internship.

8.5 Structural Biology

Computational tools can help researchers:

Retrieve protein structures
Predict structures
Compare structures
Visualise proteins
Study binding regions
Investigate protein–ligand interactions

Tools such as PDB, AlphaFold, SWISS-MODEL and PyMOL were introduced during the internship.

8.6 Precision Medicine

Bioinformatics can help connect molecular information with individual disease characteristics.

For example:

Patient data
    ↓
Genomic / transcriptomic information
    ↓
Molecular analysis
    ↓
Disease-associated patterns
    ↓
Potentially more personalised treatment decisions

This is one of the broader applications of bioinformatics in modern biomedical research.

9. A Simple Bioinformatics Workflow

The overall idea I understood during the internship was that bioinformatics is not just about using individual software tools.

Different tools can be connected to answer one biological question.

A simplified workflow is:

Biological Question
        ↓
Find Relevant Data
        ↓
Retrieve Dataset
        ↓
Process / Analyse Data
        ↓
Identify Important Results
        ↓
Functional Interpretation
        ↓
Biological Pathways
        ↓
Protein / Network Analysis
        ↓
Structural Analysis
        ↓
Biological Interpretation

For a gene-expression problem, this could become:

Biological Question
        ↓
GEO Dataset
        ↓
GEO2R
        ↓
Gene Expression Analysis
        ↓
Differentially Expressed Genes
        ↓
Functional Enrichment
        ↓
Pathway Analysis
        ↓
PPI Network
        ↓
Hub Genes

The later sections of this repository cover each of these steps in more detail.

10. Important Terms
Gene

A region of DNA containing information that contributes to a functional biological product.

Genome

The complete genetic material of an organism.

Transcriptome

The collection of RNA transcripts produced in a cell, tissue or biological condition at a particular time.

Proteome

The complete set of proteins produced in a biological system under a particular condition.

Gene Expression

The process by which information from a gene is used to produce a functional product, commonly measured through its RNA transcript.

Dataset

A structured collection of biological measurements or observations used for analysis.

Database

An organised system for storing and retrieving biological information.

Biomarker

A measurable biological feature that can provide information about a biological condition or disease.

Computational Analysis

Using algorithms, statistics and software to extract useful information from biological data.

11. What I Took Away From This Section

The main thing I understood from the fundamentals was that bioinformatics sits at the intersection of biology and computation.

The important part is not simply knowing a particular database or software. The real value comes from understanding:

Biological Question
        ↓
Biological Data
        ↓
Computational Analysis
        ↓
Biological Interpretation

A computer can process a large amount of data very quickly, but the result still has to be interpreted in a biological context.

This became clearer later during the internship when gene-expression results were connected with functional enrichment, pathways, protein interactions, protein structures and molecular docking.

Key Points
Bioinformatics combines biology with computational and statistical methods.
Biological data can include genomic, transcriptomic, proteomic and structural information.
Biological data needs to be represented, stored, retrieved and analysed.
The Central Dogma connects DNA, RNA and proteins.
Databases provide organised access to biological information.
Bioinformatics is widely used in genomics, transcriptomics, biomedical research, structural biology and drug discovery.
Computational results are useful only when they are interpreted in the correct biological context.
