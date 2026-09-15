# SWISS-MODEL

## Introduction

SWISS-MODEL is a web-based platform for **protein structure prediction through homology modelling**.

Homology modelling is a computational approach used to build a three-dimensional model of a protein when the structure of a related protein is already known.

During the internship, SWISS-MODEL was explored as part of structural bioinformatics and protein structure prediction.

---

## What is Homology Modelling?

Homology modelling is based on the principle that proteins with similar amino acid sequences can have similar three-dimensional structures.

If the structure of a related protein is already known, that structure can be used as a **template** to construct a model of the target protein.

The basic idea is:

```text
Target Protein Sequence
          ↓
Find Related Protein
          ↓
Select Structural Template
          ↓
Sequence Alignment
          ↓
Build 3D Model
          ↓
Evaluate Model
Important Terms
Target Protein

The protein whose three-dimensional structure needs to be predicted.

Template

A protein with a known three-dimensional structure that is sufficiently similar to the target protein.

Sequence Alignment

The target and template sequences are aligned to identify corresponding regions.

Homology Model

The predicted three-dimensional structure generated using the template and sequence information.

Basic Workflow

A simplified homology-modelling workflow is:

Protein Sequence
       ↓
Template Search
       ↓
Template Selection
       ↓
Sequence Alignment
       ↓
Model Building
       ↓
Model Quality Assessment
       ↓
3D Structure

The quality of the final model depends strongly on the quality and suitability of the selected template.

Template Selection

Template selection is an important step in homology modelling.

A suitable template should ideally have:

Good sequence similarity with the target
Appropriate structural coverage
Reliable experimental structural information
Relevant biological characteristics

A poor template can lead to an unreliable predicted model.

Therefore, simply finding a template is not enough; its suitability must be evaluated.

Sequence Alignment

The target sequence is aligned with the selected template sequence.

The alignment helps identify which residues in the target correspond to residues in the known structure.

Target:    M K L A A B C D E F G
Template:  M K L A A B - D E F G
                   ↑
              Alignment

Accurate alignment is important because errors in alignment can affect the resulting three-dimensional model.

Model Building

After selecting a suitable template and obtaining the sequence alignment, the structural information from the template is used to construct a model of the target protein.

The resulting model provides a predicted three-dimensional representation of the target protein.

Model Quality Assessment

A predicted model should not automatically be considered correct.

The model needs to be evaluated for structural quality.

Important aspects can include:

Overall model quality
Sequence-template agreement
Structural coverage
Geometry
Unusual structural regions
Quality of individual modelled regions

Quality assessment helps determine whether the model is suitable for further analysis.

SWISS-MODEL and PDB

SWISS-MODEL and the Protein Data Bank (PDB) are closely connected in structural bioinformatics.

PDB contains experimentally determined protein structures that can serve as templates for homology modelling.

A simplified relationship is:

PDB
 ↓
Known Experimental Structure
 ↓
Template
 ↓
SWISS-MODEL
 ↓
Target Protein Model

Therefore, experimentally determined structures in structural databases can support computational prediction of related proteins.

SWISS-MODEL and AlphaFold

Both SWISS-MODEL and AlphaFold can provide predicted protein structures, but they use different approaches.

SWISS-MODEL

Primarily uses homology modelling, where a suitable known structure is used as a template.

AlphaFold

Uses an AI-based protein structure prediction approach to predict protein structures from sequence information.

A simplified comparison is:

Feature	SWISS-MODEL	AlphaFold
Main approach	Homology modelling	AI-based structure prediction
Requires suitable template	Yes, generally	Not in the same template-dependent way
Main input	Protein sequence	Protein sequence
Output	Predicted protein model	Predicted protein structure

Both approaches are useful, but the most appropriate method depends on the protein and the research question.

Structural Bioinformatics Workflow

SWISS-MODEL fits into the broader structural workflow explored during the internship:

Protein Identification
        ↓
UniProt
        ↓
Protein Sequence
        ↓
Check PDB
        ↓
Experimental Structure Available?
        ↓
   ┌────┴────┐
  Yes        No
   ↓          ↓
  PDB    Structure Prediction
              ↓
       AlphaFold / SWISS-MODEL
              ↓
       Structural Analysis
              ↓
            PyMOL

During the internship, UniProt, PDB, PDBsum, AlphaFold, SWISS-MODEL and PyMOL were explored together to understand protein annotation, structure prediction and three-dimensional visualization.

Applications

Homology modelling can be useful for:

Studying protein structure
Understanding protein architecture
Investigating protein function
Comparing related proteins
Studying potential binding regions
Structural visualization
Molecular interaction studies
Supporting computational drug discovery

A predicted model can sometimes provide structural information when an experimental structure is unavailable.

Connection with Molecular Docking

A predicted protein structure may potentially be used in downstream computational studies such as molecular docking.

A simplified workflow is:

Target Protein Sequence
        ↓
SWISS-MODEL
        ↓
Predicted Structure
        ↓
Structure Quality Check
        ↓
Protein Preparation
        ↓
Ligand Preparation
        ↓
Molecular Docking
        ↓
Docking Analysis

However, the quality and suitability of the predicted structure must be evaluated before using it for downstream applications.

Limitations

Homology modelling has several limitations.

Dependence on Template Quality

The quality of the model depends strongly on the selected template.

Sequence Similarity

Low similarity between the target and template can reduce model reliability.

Alignment Errors

Incorrect sequence alignment can produce incorrect structural regions.

Structural Coverage

Some regions of the target may not be adequately represented by the template.

Experimental Validation

A computational model is a prediction and does not automatically represent the experimentally verified structure of the target protein.

Therefore, predicted structures should be interpreted carefully.

Practical Learning During the Internship

The main purpose of exploring SWISS-MODEL was to understand how protein sequences can be converted into predicted three-dimensional structures using homology modelling.

The conceptual workflow learned was:

Protein Sequence
       ↓
Identify Suitable Template
       ↓
Sequence Alignment
       ↓
Homology Modelling
       ↓
Predicted 3D Structure
       ↓
Model Evaluation
       ↓
Structural Visualization

This helped connect protein sequence information with structural bioinformatics and downstream molecular analysis.

Key Takeaways
SWISS-MODEL is a platform for protein structure prediction using homology modelling.
Homology modelling uses a structurally known related protein as a template.
Template selection and sequence alignment are critical steps.
The resulting model should be evaluated before further use.
PDB structures can provide templates for homology modelling.
SWISS-MODEL and AlphaFold use different approaches to protein structure prediction.
Predicted structures can support structural analysis and computational drug-discovery workflows.
Computational models should be interpreted carefully and do not replace experimental validation.
Summary

SWISS-MODEL demonstrates how known protein structures can be used to predict the three-dimensional structure of related proteins.

Within the internship, it formed part of the structural bioinformatics workflow together with UniProt, PDB, PDBsum, AlphaFold and PyMOL.

Protein Sequence
       ↓
Template Identification
       ↓
Sequence Alignment
       ↓
SWISS-MODEL
       ↓
Homology Model
       ↓
Model Evaluation
       ↓
3D Structural Analysis
