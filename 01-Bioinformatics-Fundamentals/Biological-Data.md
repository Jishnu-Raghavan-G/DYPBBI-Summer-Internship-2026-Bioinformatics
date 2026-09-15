# Biological Data

Biological data is the information generated from biological systems and experiments. In bioinformatics, this data is converted into formats that computers can store, process and analyse.

The main challenge is not only the amount of data, but also its complexity. Different experiments produce different types of data, and each type requires suitable methods for analysis.

---

## 1. What is Biological Data?

Biological data can describe many levels of a biological system.

For example:

```text
DNA
 ↓
RNA
 ↓
Protein
 ↓
Cellular Function
 ↓
Biological System

Depending on the experiment, we may study the DNA sequence, RNA expression, protein sequence, protein structure, molecular interactions or other biological properties.

Bioinformatics provides computational methods for working with this information.

2. Major Types of Biological Data
2.1 Genomic Data

Genomic data represents information stored in DNA.

It can include:

DNA sequences
Genes
Genomic regions
Mutations
Single nucleotide variants (SNVs)
Insertions and deletions
Whole-genome sequences

A DNA sequence can be represented as:

ATGCGTACCGATGCTA

The four standard DNA bases are:

A → Adenine
T → Thymine
G → Guanine
C → Cytosine
Example

Suppose two sequences are:

Sequence 1: ATGCGTAC
Sequence 2: ATGAGTAC

The difference at one position represents a sequence variation.

Bioinformatics tools can compare large numbers of sequences and identify such variations automatically.

2.2 Transcriptomic Data

Transcriptomic data describes RNA molecules present in a cell, tissue or biological condition.

It is especially useful for studying gene expression.

For example:

Gene        Healthy     Disease
--------------------------------
Gene A         50          120
Gene B        200           80
Gene C         35           37

Here:

Gene A has higher expression in the disease condition.
Gene B has lower expression in the disease condition.
Gene C shows relatively little change.

Large transcriptomic datasets allow thousands of genes to be compared simultaneously.

During the internship, this type of data was important for the asthma transcriptomics case study using the GEO dataset GSE43696.

3. Gene Expression Data

Gene expression refers to how much a gene is being expressed under a particular condition.

The amount of RNA produced from a gene can be measured using technologies such as:

Microarrays
RNA sequencing (RNA-seq)

The resulting data can be represented numerically.

For example:

             Healthy    Asthma
IL-related      40        110
Gene B          80         30
Gene C          55         57

The important question is not simply whether a gene exists.

The question is:

How does its expression change between different biological conditions?

This leads to differential gene expression analysis, which is covered in the transcriptomics section.

4. Microarray Data

A microarray measures the expression of many genes simultaneously using probes designed to detect specific sequences.

A simplified representation is:

Biological sample
       ↓
RNA extraction
       ↓
Labelled target material
       ↓
Hybridisation to array probes
       ↓
Signal measurement
       ↓
Gene expression values

The final dataset contains expression measurements for many genes across multiple samples.

Microarray datasets are commonly available through public repositories such as NCBI GEO.

5. RNA-Seq Data

RNA sequencing is a sequencing-based approach for studying RNA.

A simplified workflow is:

RNA sample
    ↓
RNA preparation
    ↓
Library preparation
    ↓
Sequencing
    ↓
Raw sequence reads
    ↓
Quality control
    ↓
Alignment / quantification
    ↓
Gene expression data

RNA-seq can provide large amounts of sequence information and is widely used for transcriptomic studies.

During the internship, I learned the concepts behind both RNA-seq and microarray data. The asthma case study used GEO/GEO2R rather than requiring a complete raw RNA-seq pipeline.

6. Proteomic Data

Proteomic data is related to proteins present in a biological system.

It can include:

Protein abundance
Protein sequences
Protein functions
Protein modifications
Protein interactions
Protein structures

Protein information connects gene-level analysis with structural and functional biology.

A simplified relationship is:

Gene
 ↓
RNA
 ↓
Protein
 ↓
Protein Function
 ↓
Cellular Function
7. Protein Sequence Data

Proteins are made from amino acids.

There are 20 commonly occurring standard amino acids used to build proteins.

A protein sequence is represented using one-letter amino-acid codes.

Example:

MKTLLLTLVVVTIVCLDLGY

Sequence information can be used to study:

Similarity between proteins
Conserved regions
Functional domains
Motifs
Possible evolutionary relationships

Protein sequence and annotation information can be retrieved from resources such as UniProt.

8. Protein Structure Data

Protein structure describes the three-dimensional arrangement of atoms in a protein.

Protein structure can provide information about:

Overall shape
Secondary structures
Binding regions
Active sites
Ligand interactions

Structural information may come from:

Experimental structures
Computational predictions
Homology modelling

Resources such as PDB, AlphaFold and SWISS-MODEL are useful for structural studies.

9. Biological Network Data

Biological systems do not work as isolated components.

Genes and proteins can interact with one another.

These relationships can be represented as networks.

For example:

        Protein A
        /       \
       /         \
Protein B ------ Protein C
                  |
                  |
              Protein D

In a network:

Nodes represent biological entities such as proteins or genes.
Edges represent relationships or interactions.

During the internship, I used this concept while learning STRING and Cytoscape for protein–protein interaction and network analysis.

10. Biological Data and Databases

Because biological datasets can be very large, databases are essential for storing and retrieving them.

Different databases focus on different types of information.

Examples:

Data type	Example resource
Nucleotide / genomic information	NCBI
Gene expression	GEO
Protein annotation	UniProt
Protein structures	PDB
Structural summaries	PDBsum
Protein interactions	STRING
Functional classification	Gene Ontology
Pathways	KEGG

The important idea is that a researcher usually does not use one database for everything.

Different resources can be combined to answer a biological question.

11. From Raw Data to Biological Meaning

Raw biological data by itself may not provide a clear conclusion.

A typical analysis can look like:

Raw Biological Data
        ↓
Quality / Data Checking
        ↓
Data Processing
        ↓
Statistical Analysis
        ↓
Significant Results
        ↓
Functional Interpretation
        ↓
Biological Conclusion

For example, in transcriptomics:

Gene Expression Dataset
        ↓
Compare Conditions
        ↓
Differential Gene Expression
        ↓
Significant Genes
        ↓
GO / KEGG / Enrichment
        ↓
Biological Interpretation

This is the basic idea behind the asthma transcriptomics work carried out later in the internship.

12. Biological Data Formats

Bioinformatics data is stored in different file formats depending on the type of information.

Some commonly encountered formats are:

FASTA

Used for nucleotide or protein sequences.

Example:

>Example_Protein
MKTLLLTLVVVTIVCLDLGY

The first line beginning with > is the sequence identifier, followed by the sequence.

FASTQ

Commonly used for raw sequencing reads.

Unlike FASTA, FASTQ also stores a quality score for each base.

A simplified FASTQ record contains:

@Read1
ATGCGTAC
+
IIIIIIII
CSV / TSV

Used for tabular biological data.

Example:

Gene,Sample1,Sample2,Sample3
GeneA,120,135,110
GeneB,50,45,60

CSV means Comma-Separated Values, while TSV means Tab-Separated Values.

PDB

PDB-format files contain information about three-dimensional molecular structures.

They can include atomic coordinates and other structural information.

These files can be opened and analysed using molecular visualisation software such as PyMOL and ChimeraX.

13. Biological Data Requires Context

A numerical value does not automatically have biological meaning.

For example:

Gene A = 250

This number alone tells us very little.

We need to know:

What organism?
Which tissue?
Which experiment?
Which condition?
Which technology?
Which samples?
What does the value represent?
How was the data processed?

Therefore, metadata is extremely important.

14. Metadata

Metadata is information that describes the biological dataset itself.

It can include:

Organism
Tissue or cell type
Disease status
Sample information
Experimental conditions
Technology used
Treatment
Control group
Patient or sample characteristics

For example:

Sample 01
Organism: Homo sapiens
Tissue: Nasal epithelial cells
Condition: Asthma
Platform: Microarray

Without proper metadata, it can be difficult to correctly interpret a dataset.

This became particularly important when working with public gene-expression datasets in GEO.

15. Biological Data Analysis Needs Multiple Levels

One useful way to think about biological data is to move from one level to another:

Sequence
   ↓
Gene
   ↓
Expression
   ↓
Protein
   ↓
Function
   ↓
Pathway
   ↓
Interaction
   ↓
Network
   ↓
Biological Process

For example, finding a gene that is significantly changed is only the beginning.

The next questions could be:

What does the gene do?
Which protein does it encode?
Which pathway is it involved in?
Which proteins interact with it?
Is it part of an important network?
Could it be biologically relevant to the disease?

This is why different bioinformatics resources are used together.

16. Biological Data in Disease Research

Bioinformatics is particularly useful when comparing biological data from different conditions.

A common design is:

Healthy
   vs
Disease

The analysis may identify:

Disease-associated genes
        ↓
Functional categories
        ↓
Biological pathways
        ↓
Protein interactions
        ↓
Important network nodes

Such analyses can help generate hypotheses about disease mechanisms and potential biomarkers or therapeutic targets.

However, computational findings usually require further biological validation before being treated as confirmed mechanisms.

17. Data Interpretation

One of the important lessons from the internship was that software output is not the final answer.

Results have to be interpreted using:

Statistical significance
Biological relevance
Experimental context
Database evidence
Quality of the dataset
Confidence of predicted interactions
Structural information

For example, a statistically significant gene is not automatically a disease-causing gene.

Similarly, a strong docking score does not by itself prove that a drug will work experimentally.

The computational result is a starting point for biological interpretation and further investigation.

18. Simple Example of Biological Data Analysis

Consider a small gene-expression dataset:

Gene    Healthy    Disease
---------------------------
A          20         80
B         100         40
C          50         52

A first observation would be:

Gene A → increased in disease
Gene B → decreased in disease
Gene C → little change

A proper analysis would then consider statistical testing across biological replicates rather than relying only on these raw values.

The genes showing statistically supported changes could then be investigated using functional and pathway analysis.

19. What I Learned

From this part of the internship, I understood that biological data is not limited to DNA sequences.

It can represent different levels of biology:

Genomic
   ↓
Transcriptomic
   ↓
Proteomic
   ↓
Structural
   ↓
Interaction / Network

Each type of data answers different questions, but they can also be connected.

The main lesson for me was:

The value of biological data comes from turning raw measurements into biologically meaningful information.

This requires the right dataset, proper metadata, suitable computational methods and careful biological interpretation.

Key Points
Biological data can represent DNA, RNA, proteins, structures and biological interactions.
Genomic data describes DNA and genetic variation.
Transcriptomic data is used to study RNA and gene expression.
Microarrays and RNA-seq are important transcriptomic technologies.
Proteomic data focuses on proteins and their properties.
Protein structures provide three-dimensional information about molecules.
Biological networks represent relationships between genes or proteins.
Databases make large biological datasets accessible and reusable.
Metadata is essential for understanding what a dataset actually represents.
Raw data must be processed and interpreted before biological conclusions can be made.
Different types of biological data can be connected to build a more complete understanding of a biological problem.
