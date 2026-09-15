# Biological Databases

Biological databases are the backbone of bioinformatics. They provide organized and searchable collections of biological information such as DNA sequences, genes, proteins, structures, expression data, pathways, and protein-protein interactions.

During my internship, I explored several major databases and learned how they fit into different stages of a bioinformatics workflow.

---

## Databases Covered

| Database / Resource | Main Use |
|---|---|
| **NCBI** | Nucleotide, gene, literature and biological data |
| **GEO** | Gene expression datasets |
| **UniProt** | Protein sequence and functional annotation |
| **PDB** | Experimentally determined 3D protein structures |
| **PDBsum** | Structural and interaction summaries |
| **STRING** | Protein-protein interaction networks |
| **Gene Ontology (GO)** | Functional annotation of genes/proteins |
| **KEGG** | Biological pathways and molecular processes |
| **g:Profiler** | Functional enrichment and gene-set analysis |
| **AlphaFold DB** | Predicted protein structures |
| **SWISS-MODEL** | Homology-based protein structure modelling |

---

## 1. NCBI

**National Center for Biotechnology Information (NCBI)** provides access to a large collection of biological databases and research resources.

I explored NCBI for:

- Gene information
- DNA and nucleotide sequences
- Protein information
- Scientific literature
- GEO datasets
- Biological annotations

**Official resource:**  
https://www.ncbi.nlm.nih.gov/

---

## 2. GEO

**Gene Expression Omnibus (GEO)** is a public repository for functional genomics and gene expression data.

During the internship, GEO was particularly important for the **asthma transcriptomics case study**.

I learned how to:

- Search for gene expression datasets
- Understand GEO accession numbers
- Examine study descriptions
- Identify samples and experimental groups
- Download or analyse expression data

The main dataset used in the case study was:

**GSE43696**

**Official resource:**  
https://www.ncbi.nlm.nih.gov/geo/

---

## 3. UniProt

**UniProt** provides detailed information about proteins.

It can be used to study:

- Protein sequences
- Protein function
- Domains
- Subcellular location
- Functional annotations
- Protein names and identifiers

UniProt was also useful before moving toward **protein structure analysis and molecular docking**.

**Official resource:**  
https://www.uniprot.org/

---

## 4. PDB

The **Protein Data Bank (PDB)** contains experimentally determined three-dimensional structures of biological macromolecules.

I used PDB concepts to understand:

- Protein structures
- Structural coordinates
- Protein-ligand complexes
- Secondary and tertiary structure
- Structural information required for docking

**Official resource:**  
https://www.rcsb.org/

---

## 5. PDBsum

**PDBsum** provides a visual and summarized interpretation of structures available in the PDB.

It can help examine:

- Protein structure
- Ligand interactions
- Protein-protein interactions
- Secondary structure
- Structural diagrams

**Official resource:**  
https://www.ebi.ac.uk/thornton-srv/databases/pdbsum/

---

## 6. STRING

**STRING** is used to investigate known and predicted **protein-protein interactions (PPI)**.

During the internship, I learned how STRING can be used to:

- Build interaction networks
- Examine relationships between proteins
- Identify highly connected proteins
- Explore functional associations
- Support network-based biological interpretation

STRING was later connected with **Cytoscape** for network visualization and analysis.

**Official resource:**  
https://string-db.org/

---

## 7. Gene Ontology (GO)

**Gene Ontology (GO)** provides a structured way to describe gene and protein functions.

The three major GO categories are:

- **Biological Process (BP)**
- **Molecular Function (MF)**
- **Cellular Component (CC)**

GO analysis helped connect lists of genes with their possible biological roles.

**Official resource:**  
https://geneontology.org/

---

## 8. KEGG

**KEGG (Kyoto Encyclopedia of Genes and Genomes)** is used to study biological pathways and molecular processes.

I explored KEGG for:

- Metabolic pathways
- Signalling pathways
- Gene-pathway relationships
- Functional interpretation of gene sets

**Official resource:**  
https://www.genome.jp/kegg/

---

## 9. g:Profiler

**g:Profiler** is a web-based tool for functional enrichment analysis.

It can be used to investigate:

- GO terms
- Pathways
- Functional categories
- Enrichment of biological processes

It was useful for interpreting lists of genes obtained from transcriptomic analysis.

**Official resource:**  
https://biit.cs.ut.ee/gprofiler/

---

## 10. AlphaFold Database

The **AlphaFold Protein Structure Database** provides predicted protein structures generated using AlphaFold.

I learned how predicted structures can be useful when an experimentally determined structure is unavailable.

The workflow can be thought of as:

**Protein sequence → predicted structure → structural analysis**

**Official resource:**  
https://alphafold.ebi.ac.uk/

---

## 11. SWISS-MODEL

**SWISS-MODEL** is a platform for **homology-based protein structure modelling**.

The basic idea is to use a known related protein structure as a template to construct a model for a target protein.

General workflow:

```text
Target protein sequence
        ↓
Template identification
        ↓
Sequence–template alignment
        ↓
Model construction
        ↓
Model quality assessment

Official resource:
https://swissmodel.expasy.org/

How These Databases Fit Together

The databases are not isolated resources. They can be connected into a single workflow.

NCBI / GEO
     ↓
Gene Expression Data
     ↓
Differentially Expressed Genes
     ↓
GO / KEGG / g:Profiler
     ↓
Functional Interpretation
     ↓
STRING
     ↓
Protein-Protein Interaction Network
     ↓
Cytoscape
     ↓
Network Visualization / Hub Analysis
     ↓
UniProt
     ↓
Protein Information
     ↓
PDB / AlphaFold / SWISS-MODEL
     ↓
Protein Structure
     ↓
Molecular Docking

This helped me understand how bioinformatics moves from raw biological data to biological interpretation and structural analysis.

Key Takeaways
Different databases answer different biological questions.
Database identifiers are important for connecting information across resources.
GEO is useful for studying gene expression datasets.
UniProt connects protein sequences with functional information.
PDB and AlphaFold provide structural information.
STRING and Cytoscape help study biological interaction networks.
GO, KEGG and g:Profiler help interpret gene lists biologically.
Combining multiple databases gives a more complete picture than using a single resource.
Resources
NCBI — https://www.ncbi.nlm.nih.gov/
GEO — https://www.ncbi.nlm.nih.gov/geo/
UniProt — https://www.uniprot.org/
RCSB PDB — https://www.rcsb.org/
PDBsum — https://www.ebi.ac.uk/thornton-srv/databases/pdbsum/
STRING — https://string-db.org/
Gene Ontology — https://geneontology.org/
KEGG — https://www.genome.jp/kegg/
g:Profiler — https://biit.cs.ut.ee/gprofiler/
AlphaFold DB — https://alphafold.ebi.ac.uk/
SWISS-MODEL — https://swissmodel.expasy.org/
