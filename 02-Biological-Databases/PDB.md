# PDB — Protein Data Bank

The Protein Data Bank (PDB) is a major resource for studying the three-dimensional structures of biological macromolecules. During the internship, it was introduced as an important database for structural bioinformatics and for understanding the three-dimensional organisation of proteins.

## What is PDB?

PDB stands for **Protein Data Bank**.

It provides access to experimentally determined three-dimensional structures of biological macromolecules.

These structures can help researchers understand:

- Protein architecture
- Three-dimensional organisation
- Secondary-structure elements
- Domains
- Binding regions
- Molecular interactions
- Protein–ligand complexes

## Why PDB Is Important

Protein sequence tells us the order of amino acids, but a protein's biological behaviour is also strongly related to its three-dimensional structure.

A simplified relationship is:

```text
Protein Sequence
       ↓
Protein Folding
       ↓
3D Structure
       ↓
Structural Features
       ↓
Possible Biological Function

Therefore, structural information can provide an additional level of understanding beyond protein sequence and annotation.

Experimentally Determined Structures

The structures available through PDB are obtained experimentally using structural biology techniques.

The important point is that a PDB structure represents an experimentally determined structural model rather than simply a computational prediction.

Different experimental techniques can be used to determine macromolecular structures, depending on the biological system and experimental conditions.

PDB Structure Records

Each structure deposited in PDB is associated with a unique identifier known as a PDB ID.

A PDB ID is generally a four-character identifier.

For example:

PDB ID: 1Y2A

The PDB ID can be used to locate a particular structure and access its associated information.

What Information Can Be Found in a PDB Entry?

A PDB entry can contain information about:

Structure identification
Macromolecule name
Experimental method
Protein chains
Ligands or other molecules
Resolution where applicable
Structural coordinates
Biological assemblies
Related references

The exact information available depends on the particular structure.

Protein Chains

A protein structure may contain one or more chains.

For example:

Protein Structure
      ↓
 ┌────┴────┐
Chain A   Chain B

Different chains may represent separate protein molecules, subunits or components of a molecular complex.

Understanding chains is important when selecting the appropriate protein component for structural analysis.

Protein Structure and Secondary Structure

A protein's three-dimensional structure contains different structural elements.

Common secondary-structure elements include:

Alpha helices
Beta sheets
Loops or turns

These elements combine to form the overall three-dimensional architecture of the protein.

Structural visualisation tools can make these features easier to understand.

Protein–Ligand Structures

Some PDB structures contain a protein together with a bound ligand or another interacting molecule.

A simplified representation is:

Protein
   +
Ligand
   ↓
Protein–Ligand Complex
   ↓
3D Structure

Such structures can be particularly useful for understanding molecular interactions and identifying regions involved in ligand binding.

They can also provide structural information relevant to molecular docking studies.

PDB and UniProt

PDB and UniProt provide complementary information.

UniProt
   ↓
Protein Sequence & Annotation
   ↓
PDB
   ↓
Experimental 3D Structure

UniProt can help identify and understand a protein, while PDB can provide an experimentally determined structure when one is available.

Connecting information across these resources is an important part of structural bioinformatics.

PDB and PDBsum

PDBsum provides additional structural summaries associated with PDB structures.

A simplified workflow is:

PDB
 ↓
PDB Structure
 ↓
PDBsum
 ↓
Structural Summary
 ↓
Structural Interpretation

PDBsum can therefore be used alongside the original PDB entry when studying structural features and molecular interactions.

PDB and PyMOL

PDB structures can also be visualised using molecular visualisation software such as PyMOL.

PDB
 ↓
Structure File
 ↓
PyMOL
 ↓
3D Visualisation
 ↓
Structural Inspection

During the internship, PyMOL was used to visualise and inspect three-dimensional protein structures.

This helped in understanding how proteins are organised spatially rather than only as linear sequences.

PDB and Molecular Docking

PDB structures can also serve as starting structures for molecular docking.

A simplified workflow is:

PDB
 ↓
Select Protein Structure
 ↓
Inspect Structure
 ↓
Protein Preparation
 ↓
Ligand Preparation
 ↓
Molecular Docking

However, a PDB structure should not automatically be used for docking without checking whether it is suitable for the intended analysis.

Structural quality, chains, bound molecules and other properties should be considered before preparation.

Choosing a Suitable PDB Structure

When several structures are available for the same protein, the choice should be based on the purpose of the analysis.

Useful factors to consider include:

Protein identity
Organism
Experimental method
Structural quality
Resolution where applicable
Completeness of the structure
Presence of relevant ligands
Relevant protein chains
Biological context

The structure with the most suitable biological and structural characteristics should be selected rather than simply choosing the first search result.

Structural Coordinates

A PDB structure contains atomic coordinate information.

These coordinates describe the positions of atoms in three-dimensional space.

Conceptually:

Atom
 ↓
X, Y, Z Coordinates
 ↓
3D Molecular Arrangement
 ↓
Protein Structure

Visualisation software can use these coordinates to display the molecule in three dimensions.

PDB File Formats

Structural information can be provided in structure-file formats that contain information about atoms, residues, chains and coordinates.

A structure file can then be opened in compatible molecular visualisation or analysis software.

During the internship, PDB structures were explored as the basis for three-dimensional structural analysis.

Practical Learning

Through working with PDB, I developed familiarity with:

Searching for protein structures
Understanding PDB IDs
Exploring structure records
Identifying protein chains
Examining structural information
Understanding experimentally determined structures
Connecting PDB with UniProt
Using PDBsum for structural information
Using PDB structures for visualisation
Understanding the role of structures in molecular docking
Example Structural Workflow

A simplified workflow from the internship was:

Protein of Interest
       ↓
UniProt
       ↓
Identify Relevant Protein
       ↓
Search PDB
       ↓
Select Suitable Structure
       ↓
Inspect Structure
       ↓
PDBsum
       ↓
PyMOL
       ↓
Structural Interpretation

This workflow shows how protein annotation and structural information can be combined.

Important Considerations

A PDB structure should always be interpreted in its experimental and biological context.

Before using a structure, it is useful to check:

What protein does the structure represent?
Which organism is it from?
What experimental method was used?
Which chains are present?
Are ligands or other molecules present?
Is the structure complete?
Is the structure appropriate for the intended analysis?

These checks are particularly important when a structure will later be used for molecular docking.

Key Takeaways
PDB stands for Protein Data Bank.
PDB provides experimentally determined three-dimensional structures of biological macromolecules.
Every PDB structure has a unique PDB ID.
PDB entries contain structural and experimental information.
Protein structures can contain multiple chains and interacting molecules.
Structural information helps understand protein architecture and molecular interactions.
PDB can be connected with UniProt for protein-level information.
PDBsum provides additional structural summaries.
PDB structures can be visualised using tools such as PyMOL.
Suitable PDB structures can also be used as starting points for molecular docking.
Structure selection should consider biological context and structural quality.
Summary

Learning about PDB introduced me to the structural level of bioinformatics. It helped me understand how experimentally determined three-dimensional protein structures can be retrieved, examined and visualised, and how structural information can later be connected with molecular docking and other computational analyses.
