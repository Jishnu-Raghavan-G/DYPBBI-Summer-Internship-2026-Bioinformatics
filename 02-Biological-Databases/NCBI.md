# NCBI Database

The **National Center for Biotechnology Information (NCBI)** is one of the major resources used in bioinformatics and molecular biology.

NCBI provides access to a wide range of biological databases, sequence information, literature, gene records, protein data and functional annotations.

---

## What is NCBI?

NCBI is a collection of biological databases and computational resources maintained by the **National Library of Medicine (NLM)**.

It provides researchers with access to biological information from different sources in one platform.

For me, NCBI was important because it connected several parts of the internship workflow, especially:

- Gene and protein information
- DNA and nucleotide sequences
- Scientific literature
- Gene expression datasets
- Biological annotations

---

## Important NCBI Resources

Some of the major resources I explored or encountered during the internship were:

| Resource | Purpose |
|---|---|
| **Gene** | Gene-specific information and annotations |
| **Nucleotide** | DNA and RNA sequence records |
| **Protein** | Protein sequence records |
| **PubMed** | Scientific literature |
| **GEO** | Gene expression and functional genomics data |
| **BLAST** | Sequence similarity searching |

---

## 1. NCBI Gene

The **Gene** database provides information associated with individual genes.

A gene record can contain information such as:

- Gene name
- Gene symbol
- Organism
- Gene identifiers
- Genomic location
- Functional information
- Links to related biological resources

This is useful when moving from a gene list obtained from an analysis to more detailed biological information.

---

## 2. Nucleotide Database

The Nucleotide database contains nucleotide sequence records.

These include sequences of:

- DNA
- RNA
- Genomic regions
- Transcripts

Sequence records can be used for downstream analysis such as sequence comparison and identification.

---

## 3. Protein Database

NCBI also provides protein sequence information.

Protein records can be useful for:

- Examining amino acid sequences
- Identifying proteins
- Comparing sequences
- Connecting protein information with other databases

Protein sequence information can later be connected with structural resources such as **PDB, AlphaFold and SWISS-MODEL**.

---

## 4. PubMed

**PubMed** is a major resource for searching scientific literature.

During the internship, literature searching was important for understanding previous research, particularly research related to:

- Asthma
- Gene expression
- Transcriptomics
- Differentially expressed genes
- Molecular mechanisms
- Bioinformatics analysis

A typical literature workflow is:

```text
Research Question
      ↓
Search PubMed
      ↓
Select Relevant Papers
      ↓
Read and Understand Methods
      ↓
Compare Results
      ↓
Extract Useful Information
5. GEO

The Gene Expression Omnibus (GEO) is another important NCBI resource.

GEO contains publicly available functional genomics and gene expression datasets.

During my internship, GEO was used for the asthma transcriptomics case study.

The main dataset explored was:

GSE43696

More detailed GEO and GEO2R analysis is documented separately in the repository.

6. BLAST

BLAST (Basic Local Alignment Search Tool) is used to compare biological sequences against sequence databases.

It can be used to identify sequences with similarity to a query sequence.

Basic concept:

Query Sequence
      ↓
BLAST Search
      ↓
Database Comparison
      ↓
Similar Sequences
      ↓
Alignment & Similarity Results

BLAST is useful for sequence identification and comparison.

NCBI in the Internship Workflow

NCBI can act as an entry point into several stages of a bioinformatics workflow.

NCBI
 │
 ├── Gene
 │     ↓
 │   Gene Information
 │
 ├── Nucleotide
 │     ↓
 │   DNA / RNA Sequences
 │
 ├── Protein
 │     ↓
 │   Protein Sequences
 │
 ├── PubMed
 │     ↓
 │   Research Literature
 │
 └── GEO
       ↓
   Gene Expression Data

This made NCBI particularly useful for connecting sequence data, gene information, expression data and scientific literature.

What I Learned
NCBI is much more than a single database.
Different NCBI resources are designed for different types of biological information.
Gene, nucleotide and protein records provide complementary information.
PubMed is useful for finding and reviewing previous research.
GEO provides access to publicly available gene expression datasets.
BLAST can be used to investigate sequence similarity.
Cross-linking between databases makes it easier to move from one type of biological information to another.
Official Resource

https://www.ncbi.nlm.nih.gov/
