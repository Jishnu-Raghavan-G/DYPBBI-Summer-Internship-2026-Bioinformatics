# Structural Bioinformatics Code

## Introduction

This directory contains Python scripts for basic computational processing related to structural bioinformatics.

The scripts are intended to demonstrate how programming can support protein sequence and structure analysis.

## Files

### Protein-Sequence-Analysis.py

This script performs basic analysis of a protein sequence.

It includes:

- Sequence cleaning
- Sequence validation
- Protein sequence length
- Amino-acid composition
- Approximate molecular weight
- Hydrophobic residue percentage

Workflow:

```text
Protein Sequence
       ↓
Clean Sequence
       ↓
Validate Sequence
       ↓
Calculate Length
       ↓
Amino-Acid Composition
       ↓
Molecular Weight
       ↓
Hydrophobicity
Structure-Data-Processing.py

This script processes basic information from a PDB-format structure file.

It extracts:

Atom information
Chain identifiers
Residue information
Atom count
Residue count
Residue composition
X, Y and Z coordinate ranges

Workflow:

PDB File
   ↓
Read ATOM / HETATM Records
   ↓
Extract Coordinates
   ↓
Identify Chains
   ↓
Identify Residues
   ↓
Calculate Structural Statistics
Requirements

The scripts are designed to use Python's standard library and therefore do not require external Python packages.

Recommended:

Python 3.x
Running the Scripts
Protein sequence analysis
python Protein-Sequence-Analysis.py

The protein sequence can be modified directly inside the script.

Structure data processing

Place the required PDB file in the same directory as the script and update:

pdb_file = "protein.pdb"

Then run:

python Structure-Data-Processing.py
Relation to Structural Bioinformatics

The scripts provide a programming-based introduction to two important stages of structural analysis:

Protein Sequence
       ↓
Sequence Analysis
       ↓
Protein Structure
       ↓
Structure Data Processing
       ↓
3D Visualization
       ↓
Structural Interpretation

This complements the structural-bioinformatics concepts covered during the internship, including protein annotation, protein structures, homology modelling, structure prediction and visualization using resources such as UniProt, PDB, AlphaFold, SWISS-MODEL and PyMOL.

Scope

These scripts are educational examples rather than complete structural-bioinformatics pipelines.

More advanced analyses can involve specialized tools and databases for:

Sequence alignment
Structure comparison
Structural modelling
Molecular visualization
Protein–ligand analysis
Molecular docking
