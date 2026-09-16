# Structural Bioinformatics

## Overview

Structural bioinformatics focuses on understanding biological molecules, especially proteins, through their three-dimensional structures.

While sequence-based bioinformatics mainly deals with nucleotide and amino-acid sequences, structural bioinformatics adds another important layer:

```text
Sequence
   ↓
Protein
   ↓
3D Structure
   ↓
Structural Features
   ↓
Biological Function

During the internship, structural bioinformatics was introduced after the transcriptomics, functional-analysis and network-analysis components. The training included protein structures, structural databases, protein analysis, homology modelling and tools used for structural interpretation.

Why Study Protein Structure?

Proteins perform a large number of biological functions.

Their functions depend strongly on their three-dimensional structure.

A protein can be described at different structural levels:

Primary Structure
       ↓
Secondary Structure
       ↓
Tertiary Structure
       ↓
Quaternary Structure

Understanding these levels helps explain how a protein folds and performs its biological function.

Primary Structure

Primary structure refers to the amino-acid sequence of a protein.

For example:

M A G K L V A L ...

The order of amino acids determines the sequence information of the protein.

This sequence can be obtained from resources such as UniProt.

Secondary Structure

Secondary structure describes local structural arrangements within a protein.

The major secondary-structure elements are:

Alpha helices
Beta sheets
Turns and loops

These structures are formed and stabilised mainly through interactions involving the protein backbone.

Tertiary Structure

Tertiary structure refers to the overall three-dimensional arrangement of a single polypeptide chain.

It describes how different secondary-structure elements come together to form the folded protein.

A simplified representation is:

Amino-acid sequence
        ↓
Local secondary structures
        ↓
Overall 3D folding
        ↓
Tertiary structure
Quaternary Structure

Some proteins contain multiple polypeptide chains.

The arrangement and interaction of these chains form the quaternary structure.

For example:

      Subunit A
          \
           \
        Protein Complex
           /
          /
      Subunit B

Not every protein has a quaternary structure.

Structural Databases

Structural bioinformatics depends heavily on biological databases.

Important resources covered in the repository include:

PDB
PDBsum
AlphaFold
SWISS-MODEL
UniProt

These resources provide complementary information.

For example:

UniProt
   ↓
Protein information
   ↓
PDB
   ↓
Experimental structures
   ↓
PDBsum
   ↓
Structural summary

When an experimental structure is unavailable, predicted structures can be considered using resources such as AlphaFold or modelling approaches such as SWISS-MODEL.

Protein Structure Analysis Workflow

A simplified workflow is:

Protein Sequence
       ↓
Protein Identification
       ↓
Sequence / Annotation Analysis
       ↓
Search Structural Databases
       ↓
Obtain Structure
       ↓
Structural Analysis
       ↓
Visualization
       ↓
Further Applications

The final structural information can subsequently be used in applications such as molecular docking.

PDB

The Protein Data Bank (PDB) is an important repository for experimentally determined three-dimensional structures of biological macromolecules.

PDB structures can provide information about:

Protein chains
Atomic coordinates
Ligands
Bound molecules
Structural complexes
Experimental information

A PDB structure can be visualized using molecular-visualization software such as PyMOL or ChimeraX.

PDBsum

PDBsum provides a graphical summary of information associated with structures in the Protein Data Bank.

It can help examine:

Protein structure
Secondary structures
Protein-ligand interactions
Protein-protein interactions
Structural diagrams
Other structural annotations

It is useful when a quick structural overview is needed before detailed visualization.

AlphaFold

AlphaFold is an AI-based approach for predicting protein structures from amino-acid sequences.

Conceptually:

Amino-Acid Sequence
        ↓
Structure Prediction
        ↓
Predicted 3D Structure
        ↓
Structural Analysis

Predicted structures are useful when experimental structures are unavailable.

However, predicted structures should be interpreted according to their confidence and intended application.

Homology Modelling

Homology modelling is a computational approach for predicting the structure of a protein based on the experimentally determined structure of a related protein.

The basic idea is:

Target Protein Sequence
          ↓
Find Related Template
          ↓
Sequence Alignment
          ↓
Build Model
          ↓
Model Evaluation

The quality of a model depends strongly on the quality and similarity of the selected template.

SWISS-MODEL

SWISS-MODEL is a web-based resource for automated protein structure homology modelling.

A simplified workflow is:

Target Sequence
      ↓
Template Identification
      ↓
Sequence Alignment
      ↓
Model Generation
      ↓
Model Assessment

The resulting model can then be inspected using structural-visualization software.

Structural Visualization

A three-dimensional structure is often easier to understand visually than from raw coordinate data.

Molecular-visualization software can display:

Protein backbone
Secondary structures
Amino-acid residues
Ligands
Binding sites
Protein surfaces
Protein-protein interfaces

The repository includes PyMOL as a dedicated structural-visualization topic.

PyMOL

PyMOL is a molecular visualization system commonly used to display and analyse biological structures.

It can be used to:

Open PDB structures
Display proteins in different representations
Highlight residues
Visualize ligands
Examine binding sites
Produce publication-quality molecular figures

A simplified workflow is:

PDB Structure
     ↓
Open in PyMOL
     ↓
Choose Representation
     ↓
Highlight Important Residues
     ↓
Inspect Structure
     ↓
Create Figure
Structural Bioinformatics and Molecular Docking

Structural bioinformatics provides the structural foundation for molecular docking.

Before docking, information about the target protein is required.

A simplified progression is:

Protein Sequence
      ↓
Protein Structure
      ↓
Structure Preparation
      ↓
Binding-Site Analysis
      ↓
Ligand Preparation
      ↓
Molecular Docking

The internship covered structural tools before moving into molecular docking and virtual-screening concepts.

Protein Structure and Function

Protein structure can provide clues about biological function.

For example:

Structure
   ↓
Shape and organization
   ↓
Potential binding regions
   ↓
Molecular interactions
   ↓
Possible biological function

However, structure alone should not be treated as definitive proof of function.

Structural interpretation should be combined with sequence, annotation, experimental and literature evidence.

Protein-Ligand Interactions

Some proteins interact with small molecules called ligands.

A simplified representation is:

Protein
   +
Ligand
   ↓
Protein-Ligand Complex

The structure of the complex can help identify interactions such as:

Hydrogen bonds
Hydrophobic interactions
Electrostatic interactions
Other non-covalent interactions

These interactions are particularly relevant to molecular docking and drug-discovery studies.

Structural Analysis in the Internship

Structural bioinformatics formed part of the later stages of the internship.

The overall training progressed broadly from:

Biological Databases
        ↓
Gene Expression
        ↓
Differential Expression
        ↓
Functional Analysis
        ↓
Network Analysis
        ↓
Protein Structures
        ↓
Structural Analysis
        ↓
Molecular Docking

The internship objectives included understanding protein structures and structural-bioinformatics tools in addition to transcriptomics and functional analysis.

Structural Data vs Sequence Data

Sequence and structure provide different types of information.

Sequence	Structure
Amino-acid order	3D arrangement
Primary information	Spatial information
Useful for sequence comparison	Useful for structural comparison
Can be used for homology searches	Can be used for structural analysis
Provides the molecular sequence	Shows molecular shape and organization

They are complementary.

Sequence
   +
Structure
   ↓
Better understanding of protein
Experimental vs Predicted Structures

Protein structures can come from different sources.

Experimental Structure

Determined using experimental structural-biology methods and deposited in resources such as the PDB.

Predicted Structure

Generated computationally using methods such as AlphaFold.

Modelled Structure

Constructed using approaches such as homology modelling through a suitable template.

A simplified comparison:

Experimental
     ↓
Observed structural data

Predicted
     ↓
Computational prediction

Modelled
     ↓
Structure inferred from a related template

The source of a structure should always be clearly stated.

Structural Quality

Not every structure should be treated as equally reliable.

When analysing a structure, it is important to consider:

Experimental method
Resolution where applicable
Missing residues
Model confidence
Structural coverage
Template quality for homology models
Prediction confidence for computational models

This becomes particularly important when the structure will later be used for molecular docking.

Common Mistakes
Mistake 1: Treating predicted structures as experimental structures

The source and confidence of the structure should be reported.

Mistake 2: Ignoring missing residues

Some experimental structures do not contain the complete protein sequence.

Mistake 3: Assuming structure automatically determines function

Structural evidence needs biological context.

Mistake 4: Using an unsuitable model for docking

Structural quality and completeness matter when preparing a protein for docking.

Mistake 5: Confusing PDB and PDBsum

PDB is the structural repository, while PDBsum provides summaries and graphical structural information.

Limitations

Structural bioinformatics also has limitations:

Experimental structures may not be available for every protein
Structures may contain unresolved regions
Predicted structures have varying confidence
Homology models depend on template quality
Static structures do not fully represent molecular dynamics
Structural similarity does not always imply identical biological function

Therefore, structural analysis should be combined with other biological evidence.

What I Learned

The main concept I learned from structural bioinformatics was how sequence information can be connected to three-dimensional protein structure.

The progression can be summarized as:

Protein Sequence
       ↓
Protein Annotation
       ↓
Structural Database Search
       ↓
Experimental / Predicted Structure
       ↓
Structural Visualization
       ↓
Structural Interpretation
       ↓
Molecular Docking

This provided the foundation for the molecular-docking concepts covered later in the internship.

Quick Revision
Structural Bioinformatics
↓
Study of biological molecules using structural information.

Important concepts:
- Primary structure
- Secondary structure
- Tertiary structure
- Quaternary structure

Important resources:
- PDB
- PDBsum
- AlphaFold
- SWISS-MODEL
- UniProt

Important software:
- PyMOL
- ChimeraX

Homology Modelling:
Target sequence
 ↓
Template
 ↓
Alignment
 ↓
Model

Overall:
Sequence
 ↓
Structure
 ↓
Structural Analysis
 ↓
Docking
Conclusion

Structural bioinformatics adds three-dimensional information to sequence and functional analysis. During the internship, this area connected the earlier bioinformatics workflow with protein-level analysis and molecular docking.

The overall transition was:

Genes
 ↓
Proteins
 ↓
Protein Structures
 ↓
Structural Analysis
 ↓
Protein-Ligand Interactions
 ↓
Molecular Docking

Understanding this connection was an important step in moving from transcriptomic and network-level analysis toward structure-based computational biology.
