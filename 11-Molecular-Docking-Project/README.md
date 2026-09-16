# Molecular Docking Project

This section documents my learning and practical exposure to molecular docking and computer-aided drug discovery during the DYPBBI Summer Internship 2026.

The molecular docking component connected concepts from medicinal chemistry and structural bioinformatics with computational methods used to study protein–ligand interactions.

---

## Overview

Molecular docking is a computational approach used to investigate how a small molecule ligand may interact with a target protein.

During the internship, I was introduced to the workflow involved in preparing molecular structures, performing docking, examining docking poses, and interpreting predicted protein–ligand interactions.

The training also introduced virtual screening as an extension of docking in which multiple compounds can be computationally evaluated and prioritised for further investigation.

---

## Topics Covered

The molecular docking training covered the following areas:

- Medicinal chemistry fundamentals
- Molecular interactions
- Stereochemistry
- Isomerism
- Conformational analysis
- Molecular geometry
- Protein structure preparation
- Ligand preparation
- Molecular structure inspection
- Protein–ligand docking
- Docking poses
- Binding affinity
- Binding sites
- Protein–ligand interactions
- Docking result interpretation
- Virtual screening

---

## Software and Tools

The following tools were introduced and used during the molecular docking training:

### ChimeraX

ChimeraX was used for molecular structure inspection and preparation.

It helped in understanding and working with three-dimensional molecular structures before docking.

### AutoDock Tools

AutoDock Tools was introduced for preparing protein and ligand structures for docking.

The preparation stage is important because the quality and suitability of the input structures affect downstream docking calculations.

### AutoDock Vina

AutoDock Vina was used to understand the molecular docking process and the prediction of possible protein–ligand binding modes.

The resulting docking poses and predicted binding affinities were examined as part of the analysis.

---

## General Docking Workflow

The workflow learned during the internship can be represented as:

```text
Target Protein
      ↓
Protein Structure Inspection
      ↓
Protein Preparation
      ↓
Ligand Selection
      ↓
Ligand Preparation
      ↓
Define Binding Site / Search Space
      ↓
Molecular Docking
      ↓
Generation of Docking Poses
      ↓
Binding Affinity Evaluation
      ↓
Protein–Ligand Interaction Analysis
      ↓
Interpretation of Results
Protein Preparation

Before docking, the target protein needs to be prepared appropriately.

The training covered concepts related to:

Inspecting the protein structure
Removing unwanted molecules where appropriate
Identifying structural issues
Preparing the protein for docking
Understanding the importance of a suitable input structure
Inspecting the prepared structure using molecular visualisation tools

Detailed notes are provided in:

Notes/Protein-Preparation.md

Ligand Preparation

Ligands also need to be prepared before they can be used for docking.

The training introduced concepts related to:

Ligand structure
Molecular geometry
Stereochemistry
Isomerism
Conformation
Preparation of ligand structures for computational analysis

Detailed notes are provided in:

Notes/Ligand-Preparation.md

Molecular Interactions

Understanding molecular interactions is important for interpreting docking results.

The training introduced interactions that can contribute to protein–ligand binding, including:

Hydrogen bonding
Hydrophobic interactions
Electrostatic interactions
Other non-covalent interactions

These interactions help explain why a ligand may adopt a particular orientation within a binding site.

Docking Poses

A docking program can generate different possible orientations or conformations of a ligand within the target binding site.

These possible arrangements are referred to as docking poses.

The poses can be examined to understand:

Ligand orientation
Binding-site occupancy
Interacting residues
Possible hydrogen bonds
Other protein–ligand interactions
Predicted binding affinity
Binding Affinity

Docking programs such as AutoDock Vina provide predicted binding-affinity scores for generated poses.

These scores can be used as one component of docking-result interpretation.

However, docking scores are computational predictions and should not by themselves be treated as experimental evidence of binding or biological activity.

Docking Analysis

After docking, the predicted complexes can be inspected to understand how the ligand interacts with the target protein.

The analysis can involve:

Comparing docking poses
Examining interacting residues
Inspecting the binding site
Identifying possible hydrogen bonds
Examining other molecular interactions
Comparing predicted binding affinities
Visualising the protein–ligand complex

The detailed learning notes are available in:

Notes/Docking-Analysis.md

Virtual Screening

Virtual screening was introduced as a computational approach for evaluating multiple compounds against a target.

A general virtual-screening workflow can be represented as:

Compound Library
      ↓
Ligand Preparation
      ↓
Target Protein Preparation
      ↓
Docking
      ↓
Scoring
      ↓
Ranking of Compounds
      ↓
Selection of Candidates
      ↓
Further Investigation

The purpose is to computationally prioritise compounds that may be worth further investigation.

Virtual screening was covered primarily as a concept within the internship training.

Project Organisation

The section is organised into two main components:

Notes

The Notes/ directory contains detailed Markdown notes covering the concepts and tools learned during the molecular docking component.

Notes/
├── README.md
├── Molecular-Docking-Concepts.md
├── Medicinal-Chemistry-and-Ligands.md
├── Stereochemistry-and-Isomerism.md
├── Conformational-Analysis.md
├── Protein-Preparation.md
├── Ligand-Preparation.md
├── ChimeraX.md
├── AutoDock-Tools.md
├── AutoDock-Vina.md
├── Docking-Procedure.md
├── Docking-Analysis.md
└── Virtual-Screening.md
Project Files

The remaining directories are reserved for project-related material:

Protein/
Ligands/
Docking/
Results/
Code/
Figures/

These directories can contain molecular structures, docking inputs and outputs, result files, scripts, and project figures where applicable.

Learning Outcome

The molecular docking component helped me understand how structural bioinformatics can be extended towards computational drug discovery.

The training connected:

Protein Structure
      ↓
Ligand Structure
      ↓
Molecular Interactions
      ↓
Protein Preparation
      ↓
Ligand Preparation
      ↓
Molecular Docking
      ↓
Docking Pose Analysis
      ↓
Virtual Screening

This provided an introduction to the computational workflow used to study potential protein–ligand interactions and to support early-stage drug-discovery research.

Important Note

The material in this section documents the concepts, software, workflows, and practical exposure gained during the internship.

Docking scores and computational predictions should be interpreted carefully and do not independently establish experimental binding, efficacy, or therapeutic potential.
