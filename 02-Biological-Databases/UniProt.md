# UniProt

UniProt is an important biological resource used for obtaining information about proteins. It provides protein sequence information along with functional and annotation-related details.

During the internship, UniProt was introduced as part of the transition from gene-level analysis towards protein-level and structural bioinformatics.

## What is UniProt?

UniProt stands for **Universal Protein Resource**.

It is a major protein database that provides information about proteins from many different organisms.

A UniProt entry can connect a protein with information such as:

- Protein name
- Gene name
- Organism
- Protein sequence
- Functional annotation
- Protein length
- Related identifiers
- Structural information
- Links to other biological databases

This makes UniProt useful as a starting point for studying a protein before moving into structural or molecular analysis.

## Why UniProt Is Important

Genes ultimately produce functional products such as proteins, and proteins perform many of the functions required for cellular processes.

Therefore, after identifying a gene of interest, it can be useful to investigate its corresponding protein.

A simplified relationship is:

```text
Gene
  ↓
Protein
  ↓
Protein Sequence
  ↓
Protein Function
  ↓
Protein Structure
  ↓
Structural / Molecular Analysis

UniProt helps provide the protein-level information required for this type of workflow.

Protein Sequence

One of the important pieces of information available through UniProt is the protein's amino acid sequence.

A protein sequence represents the order of amino acids that make up a protein.

For example:

M A G K L V A L ...

The sequence can be used as a starting point for several types of computational analysis.

Protein sequences are also useful when searching for related proteins or studying structural relationships.

Protein Annotation

Protein annotation involves associating biological information with a protein sequence.

Annotations can provide information about:

Protein function
Biological role
Cellular location
Domains
Important regions
Related genes
Sequence features

Annotation helps transform a protein sequence into biologically meaningful information.

Gene–Protein Relationship

A gene and its protein product are related, but they are not the same biological entity.

A simplified view is:

DNA
 ↓
Gene
 ↓
mRNA
 ↓
Protein

UniProt mainly focuses on the protein level, while other resources may provide more detailed information about genes, nucleotide sequences or gene expression.

Connecting these different levels is an important part of bioinformatics.

UniProt and Other Databases

UniProt can be connected with other biological databases.

For example:

Gene / Gene Expression Data
          ↓
       Protein
          ↓
       UniProt
          ↓
 Protein Annotation
          ↓
 PDB / AlphaFold / SWISS-MODEL
          ↓
 Protein Structure

This allows information from different databases to be combined during a biological investigation.

UniProt and Structural Bioinformatics

During the structural bioinformatics part of the internship, UniProt was useful for understanding protein information before exploring protein structures.

A typical workflow can be represented as:

Protein of Interest
       ↓
UniProt
       ↓
Protein Information
       ↓
Search for Structure
       ↓
PDB / AlphaFold / SWISS-MODEL
       ↓
3D Structural Analysis

The available structural resource depends on whether an experimentally determined or predicted structure is available.

Protein Identifiers

Protein databases use identifiers to distinguish individual protein records.

When working with a protein, it is important to keep track of the correct identifier rather than relying only on a general protein name.

Identifiers can help connect the same protein across different resources.

For example:

UniProt
   ↓
Protein Identifier
   ↓
Related Database Records
   ↓
PDB / Other Resources

This is particularly useful when moving between databases.

Protein Function

Protein function describes what a protein does or contributes to biologically.

A protein may be involved in:

Enzymatic reactions
Signalling
Transport
Regulation
Structural processes
Cellular metabolism
Other biological processes

Functional annotation provides context for understanding why a particular protein may be biologically important.

Protein Sequence and Structure

Protein sequence and protein structure are closely related concepts.

Amino Acid Sequence
        ↓
Protein Folding
        ↓
Three-Dimensional Structure
        ↓
Molecular Function

However, sequence alone does not provide the complete structural picture.

This is why structural resources such as PDB, AlphaFold and SWISS-MODEL become useful when studying protein structure.

From UniProt to PDB

If a protein of interest has an experimentally determined structure, the corresponding structure can be investigated using the Protein Data Bank (PDB).

A simplified workflow is:

UniProt
   ↓
Identify Protein
   ↓
Find Related Structure
   ↓
PDB
   ↓
PDB Structure
   ↓
PDBsum / PyMOL

The structure can then be inspected to understand its three-dimensional organisation.

From UniProt to AlphaFold

When an experimentally determined structure is unavailable or when predicted structural information is useful, AlphaFold can be explored.

UniProt
   ↓
Protein
   ↓
AlphaFold
   ↓
Predicted Structure
   ↓
Structural Inspection

Predicted structures should still be interpreted carefully and considered in the context of their confidence and biological purpose.

Practical Learning

During the internship, I developed familiarity with:

Searching for proteins
Understanding protein annotations
Exploring protein sequences
Understanding gene–protein relationships
Connecting protein information with other databases
Using protein information as a starting point for structural analysis
Understanding the role of UniProt in a broader bioinformatics workflow
Example Workflow

A complete simplified example is:

Biological Question
        ↓
Identify Gene
        ↓
Identify Protein
        ↓
UniProt
        ↓
Protein Annotation
        ↓
PDB / AlphaFold / SWISS-MODEL
        ↓
Protein Structure
        ↓
PDBsum / PyMOL
        ↓
Structural Interpretation

This demonstrates how protein annotation can form the bridge between gene-level information and structural bioinformatics.

Important Considerations

While using UniProt, it is important to make sure that the correct protein and organism are being studied.

Before using a protein record, useful information to verify includes:

Protein name
Gene name
Organism
Protein sequence
Protein identifier
Available annotations
Links to related resources

A similar protein name does not necessarily mean that two records represent the same protein.

Key Takeaways
UniProt is an important resource for protein information.
It provides protein sequences and functional annotations.
Protein identifiers help connect records across different databases.
UniProt can be used as a starting point for structural bioinformatics.
Protein information can be connected with PDB, AlphaFold and SWISS-MODEL.
Protein sequence and protein structure represent different levels of biological information.
Correct identification of the protein and organism is important for reliable analysis.
UniProt helped bridge the transition from gene-level information to protein-level analysis during the internship.
Summary

Learning about UniProt helped me understand how protein sequence and functional information can be organised and connected with other biological resources. It provided an important foundation for the structural bioinformatics topics covered later in the internship, including PDB, PDBsum, AlphaFold, SWISS-MODEL and PyMOL.
