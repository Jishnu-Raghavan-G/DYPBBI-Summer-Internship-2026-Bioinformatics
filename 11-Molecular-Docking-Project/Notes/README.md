# Molecular Docking Notes

This folder contains my detailed notes from the molecular docking and computer-aided drug discovery component of the DYPBBI Summer Internship 2026.

The notes are organised to follow the learning sequence from the underlying chemical concepts and molecular interactions to protein and ligand preparation, docking software, docking analysis, and virtual screening.

---

## Purpose

The purpose of these notes is to document the concepts I learned and the workflow I was introduced to during the molecular docking training.

The section focuses on understanding the reasoning behind each stage rather than treating docking software as a black-box process.

---

## Topics Covered

The molecular docking notes cover:

1. Molecular docking concepts
2. Medicinal chemistry and ligands
3. Stereochemistry and isomerism
4. Conformational analysis
5. Protein preparation
6. Ligand preparation
7. ChimeraX
8. AutoDock Tools
9. AutoDock Vina
10. Docking procedure
11. Docking analysis
12. Virtual screening

---

## Learning Sequence

The overall progression of the notes is:

```text
Medicinal Chemistry
        ↓
Molecular Interactions
        ↓
Stereochemistry & Isomerism
        ↓
Conformational Analysis
        ↓
Protein Structure
        ↓
Protein Preparation
        ↓
Ligand Preparation
        ↓
Structure Inspection
        ↓
Docking Setup
        ↓
Molecular Docking
        ↓
Docking Poses & Scores
        ↓
Protein–Ligand Interaction Analysis
        ↓
Virtual Screening
Notes Directory
Molecular Docking Concepts

Molecular-Docking-Concepts.md

Introduces the basic idea of molecular docking, its purpose, the protein–ligand system, docking poses, binding sites, scoring, and the general computational workflow.

Medicinal Chemistry and Ligands

Medicinal-Chemistry-and-Ligands.md

Covers the basic medicinal-chemistry concepts required to understand small-molecule ligands and their interactions with biological targets.

Stereochemistry and Isomerism

Stereochemistry-and-Isomerism.md

Explains molecular stereochemistry and different forms of isomerism relevant to ligand structure and molecular recognition.

Conformational Analysis

Conformational-Analysis.md

Covers molecular conformation, flexibility, and the importance of molecular geometry when considering ligand–protein interactions.

Protein Preparation

Protein-Preparation.md

Documents the concepts involved in preparing a protein structure before molecular docking.

Ligand Preparation

Ligand-Preparation.md

Documents the preparation and inspection of ligand structures before docking.

ChimeraX

ChimeraX.md

Contains notes on using ChimeraX for molecular structure visualisation, inspection, and preparation.

AutoDock Tools

AutoDock-Tools.md

Documents the role of AutoDock Tools in preparing molecular structures for docking.

AutoDock Vina

AutoDock-Vina.md

Introduces AutoDock Vina and its role in molecular docking and prediction of possible protein–ligand binding modes.

Docking Procedure

Docking-Procedure.md

Describes the overall sequence followed during a molecular docking workflow, from prepared structures to docking output.

Docking Analysis

Docking-Analysis.md

Covers the interpretation of docking poses, predicted binding affinity, binding sites, interacting residues, and protein–ligand interactions.

Virtual Screening

Virtual-Screening.md

Introduces virtual screening and explains how docking can be extended to evaluate multiple compounds computationally.

Important Concepts

A major part of the molecular docking training was understanding that a docking result should not be interpreted only through a numerical score.

The analysis should consider:

Docking pose
Binding-site location
Protein–ligand interactions
Interacting residues
Molecular geometry
Stereochemistry
Predicted binding affinity
Structural plausibility
Overall biological context

Computational predictions provide useful information for prioritisation and hypothesis generation, but they require appropriate interpretation and, where necessary, experimental validation.

Software Covered

The main molecular-structure and docking tools documented in this section are:

ChimeraX
AutoDock Tools
AutoDock Vina

These tools were introduced as part of the computational workflow for molecular structure preparation, docking, visualisation, and interpretation.

Relationship with Section 07

Section 07 contains the broader learning material on:

Molecular Docking and Virtual Screening

This section, Section 11, is different.

Section 07 focuses on the general subject and foundational concepts.

Section 11 focuses specifically on the molecular docking component of my internship and organises the detailed notes and project-related material associated with it.

Practical Project Structure

The parent directory also contains separate locations for project material:

11-Molecular-Docking-Project/
│
├── Notes/
├── Protein/
├── Ligands/
├── Docking/
├── Results/
├── Code/
└── Figures/

The Notes/ folder is intended for conceptual documentation, while the other folders are reserved for actual project files and supporting material where applicable.

Learning Outcome

The molecular docking training helped connect concepts from:

Chemistry
   +
Structural Biology
   +
Protein–Ligand Interactions
   +
Computational Methods
        ↓
Molecular Docking
        ↓
Docking Analysis
        ↓
Early-Stage Drug Discovery

The notes in this folder provide a structured record of that learning progression.
