The National Center for Biotechnology Information (NCBI) is one of the major resources used in bioinformatics for accessing, searching and analysing biological information.

During the internship, I was introduced to NCBI and its different resources, particularly for locating biological information and publicly available datasets.

## What is NCBI?

NCBI is a biological information resource that provides access to a large collection of databases, sequence information, scientific literature and other computational resources.

It acts as an important starting point when searching for biological information related to genes, genomes, proteins, diseases and research studies.

## Why NCBI Is Important in Bioinformatics

Biological research generates large amounts of information that needs to be stored and made accessible to researchers.

NCBI helps researchers:

- Search for biological information
- Retrieve nucleotide and genomic sequences
- Find gene-related information
- Access gene expression datasets
- Explore protein-related resources
- Search scientific literature
- Connect information from different biological resources
- Access publicly available research data

The main advantage is that different types of biological information can be explored through a common resource ecosystem.

## Major Resources Associated With NCBI

NCBI provides access to several important resources.

Some of the resources relevant to my internship were:

### Gene

The NCBI Gene database provides information about genes from different organisms.

A gene record can contain information such as:

- Gene name
- Gene symbol
- Gene identifier
- Organism
- Genomic location
- Related sequences
- Links to additional biological resources

This makes it useful when moving from a gene identifier to additional biological information.

### GEO

The Gene Expression Omnibus (GEO) is an important NCBI resource for functional genomics data.

It contains publicly available gene expression datasets generated using technologies such as microarrays and high-throughput sequencing.

During my internship, GEO was particularly important because I used a GEO dataset for the asthma transcriptomics case study.

### Nucleotide

The Nucleotide database provides access to nucleotide sequences such as DNA and RNA sequences.

Sequences can be searched using identifiers, gene names, organisms or other relevant terms.

### Protein

NCBI also provides access to protein sequence information.

Protein records can be connected with genes, nucleotide sequences and other biological resources.

### PubMed

PubMed is used to search scientific literature, particularly biomedical and life-science research articles.

It is useful during literature reviews because research papers can be searched using:

- Keywords
- Authors
- Topics
- Genes
- Diseases
- Biological processes

## NCBI as a Starting Point

A useful way to think about NCBI is as an entry point into biological information.

For example:

```text
Biological Question
        ↓
NCBI
        ↓
Gene / Sequence / Dataset / Literature
        ↓
Further Analysis
        ↓
Biological Interpretation

The information obtained from NCBI can then be used with other specialised resources.

For example:

NCBI
  ↓
GEO
  ↓
Gene Expression Dataset
  ↓
GEO2R
  ↓
Differential Gene Expression

This type of connection became particularly relevant during the asthma transcriptomics analysis.

Searching Biological Information

When searching NCBI, it is important to use appropriate search terms.

Possible search inputs include:

Gene symbols
Gene names
Protein names
Accession numbers
Organism names
Disease names
Dataset identifiers
Sequence identifiers

Using a specific identifier is generally more reliable than relying only on a broad keyword search.

Accession Numbers and Identifiers

Biological databases use identifiers to uniquely refer to records.

An accession number or database identifier can be used to locate a specific biological record or dataset.

For example, during the internship:

GSE43696

was the GEO accession used for the asthma transcriptomics case study.

Using the accession number makes it easier to locate the exact dataset rather than searching for asthma-related datasets broadly.

NCBI and Data Interpretation

Finding a record is only the first step.

Before using biological information for analysis, it is important to understand:

What the record represents
Which organism it belongs to
What type of experiment produced the data
What the identifier refers to
What information is experimentally supported
How the record is connected to other resources

This prevents incorrect interpretation of biological data.

Example: Asthma Transcriptomics

The role of NCBI can be understood through the asthma transcriptomics case study from the internship.

The workflow began with the NCBI Gene Expression Omnibus:

NCBI
  ↓
GEO
  ↓
GSE43696
  ↓
GEO2R
  ↓
Healthy vs Asthma
  ↓
Differential Gene Expression
  ↓
Significant Genes

The resulting gene list was subsequently used for functional and network analysis.

The complete analysis is documented separately in:

04-Asthma-Transcriptomics/

Connecting NCBI With Other Resources

NCBI does not need to be used independently.

Biological information can be transferred between different resources depending on the analysis.

For example:

NCBI
  ↓
Gene / Dataset
  ↓
UniProt
  ↓
Protein Information
  ↓
PDB / AlphaFold
  ↓
Protein Structure

Similarly:

NCBI / GEO
       ↓
Gene List
       ↓
GO / KEGG / g:Profiler
       ↓
Functional Interpretation
       ↓
STRING
       ↓
Protein Interaction Network

This demonstrates an important principle of bioinformatics: different databases provide complementary information about the same biological system.

Practical Skills Learned

During the internship, I developed familiarity with:

Navigating NCBI
Searching biological records
Understanding database identifiers
Locating GEO datasets
Connecting biological records with other resources
Using accession numbers to identify datasets
Understanding the importance of metadata
Using database information as the starting point for downstream analysis
Important Considerations

While using NCBI or any biological database, it is important to check the context of the information before using it.

Some important questions are:

What exactly does the record represent?
Which organism is being studied?
What type of biological data is available?
What experiment produced the data?
Is the identifier correct?
What additional information is available through linked resources?

Careful database navigation reduces the possibility of selecting the wrong dataset, sequence or biological record.

Key Takeaways
NCBI is a major resource for biological information and bioinformatics research.
It provides access to multiple biological databases and resources.
GEO is an important NCBI resource for gene expression datasets.
Gene and sequence information can be retrieved through NCBI resources.
PubMed is useful for finding scientific literature.
Accession numbers and identifiers help locate specific records.
NCBI can act as the starting point for downstream bioinformatics analysis.
Information from NCBI can be connected with resources such as UniProt, PDB, GEO, GO, KEGG and STRING.
Understanding the biological context of a database record is as important as finding the record itself.
Summary

My introduction to NCBI helped me understand how biological information can be systematically searched and connected across different resources. This became especially useful during the internship because the NCBI ecosystem provided the starting point for accessing the GEO dataset used in the asthma transcriptomics case study.
