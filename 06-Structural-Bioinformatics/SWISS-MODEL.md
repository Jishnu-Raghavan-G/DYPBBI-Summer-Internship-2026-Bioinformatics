# SWISS-MODEL

## Introduction

SWISS-MODEL is a web-based resource used for automated protein structure modelling, particularly through homology modelling.

Homology modelling uses a related protein with a known structure as a template to construct a three-dimensional model of a target protein.

During the internship, SWISS-MODEL was introduced to understand homology modelling and protein structure prediction as part of the structural-bioinformatics module. :contentReference[oaicite:0]{index=0}

The basic workflow is:

```text
Target Protein Sequence
        ↓
Template Identification
        ↓
Sequence / Structure Comparison
        ↓
Model Generation
        ↓
Model Assessment
        ↓
3D Protein Model
What is SWISS-MODEL?

SWISS-MODEL is an online platform for protein structure modelling.

Its main use in this context is to generate a three-dimensional model of a protein when an appropriate experimentally determined structure of a related protein can be used as a template.

The general principle is:

Known Related Structure
        +
Target Protein Sequence
        ↓
Homology Modelling
        ↓
Target Protein Model
Why Use SWISS-MODEL?

Experimental structures are not available for every protein.

When a suitable experimentally determined structure of a related protein exists, homology modelling can provide a computational model of the target.

This makes structure modelling useful for:

Structural analysis
Protein visualization
Studying protein architecture
Exploring functional regions
Generating models for further computational investigation
Target and Template

Two important terms are:

Target

The target is the protein for which a structure needs to be modelled.

Template

The template is a related protein for which structural information is already available.

Target
→ Unknown / unavailable structure

Template
→ Known experimental structure

The quality of the resulting model depends strongly on the suitability of the selected template.

Basic SWISS-MODEL Workflow
1. Obtain target sequence
        ↓
2. Submit / identify target
        ↓
3. Search for suitable templates
        ↓
4. Examine template information
        ↓
5. Select an appropriate template
        ↓
6. Generate model
        ↓
7. Assess model
        ↓
8. Visualize structure
Target Sequence

The target protein sequence is the starting point.

A sequence may be obtained from a protein database such as UniProt.

Protein
   ↓
UniProt
   ↓
Protein Sequence
   ↓
SWISS-MODEL

Correct sequence selection is important because the resulting model represents the submitted target sequence.

Template Identification

SWISS-MODEL can identify potential structural templates for a target protein.

A template search generally considers the relationship between the target sequence and proteins for which structural information is available.

Conceptually:

Target Sequence
       ↓
Template Search
       ↓
Candidate Structures
       ↓
Template Evaluation
Template Selection

A suitable template should be evaluated rather than selected automatically.

Important considerations include:

Sequence similarity
Sequence coverage
Structural quality
Biological relevance
Presence of the relevant domain
Completeness of the template

For example:

Target:
|--------------------------------------|

Template A:
|--------------------------------------|

Template B:
|----------------------|

A template with greater relevant coverage may provide more structural information for the target, but other factors also need to be considered.

Sequence Alignment

The target and template sequences need to be aligned.

A simplified example is:

Target:    M A G K L V A A T G
Template:  M A G K L I A A T G
           | | | | | | | | | |

The alignment determines which residues are treated as corresponding positions.

An inaccurate alignment can lead to structural errors in the resulting model.

Model Generation

Once a suitable template and alignment are available, a three-dimensional model of the target can be constructed.

The concept is:

Template Structure
        +
Target Sequence
        +
Sequence Alignment
        ↓
Target Protein Model

The resulting model is a computational prediction.

Model Assessment

A generated model should be evaluated before being used for further analysis.

Assessment can involve examining:

Template suitability
Sequence identity
Coverage
Model quality
Structural geometry
Potentially problematic regions

A simple workflow is:

Generated Model
      ↓
Quality Assessment
      ↓
Identify Weak Regions
      ↓
Interpret Carefully
Protein Structure Visualization

After generating a model, its three-dimensional structure can be inspected using molecular visualization software.

During the internship, PyMOL was used for protein structure visualization and structural inspection.

The workflow can therefore be represented as:

SWISS-MODEL
     ↓
Homology Model
     ↓
3D Structure
     ↓
PyMOL
     ↓
Structural Visualization
What Can Be Examined?

A model can be inspected for:

Alpha helices
Beta sheets
Loops
Domains
Overall fold
Structural regions
Possible binding regions

A simplified structure is:

        ______
      /        \
     /  Helix   \
    |            |
    |  β-sheet   |
     \          /
      \________/
SWISS-MODEL and UniProt

UniProt and SWISS-MODEL can be connected in a typical protein-analysis workflow.

UniProt
   ↓
Protein Annotation
   ↓
Target Sequence
   ↓
SWISS-MODEL
   ↓
Homology Model

UniProt provides the biological and sequence context, while SWISS-MODEL can be used for structure modelling.

SWISS-MODEL and PDB

PDB is important because experimentally determined structures can serve as templates for homology modelling.

The relationship is:

PDB
 ↓
Known Experimental Structure
 ↓
Template
 ↓
SWISS-MODEL
 ↓
Target Protein Model

Therefore, structural databases and modelling resources are closely connected.

SWISS-MODEL and AlphaFold

SWISS-MODEL and AlphaFold can both provide predicted protein structures, but their approaches are different.

                Protein Sequence
                       ↓
              ┌────────┴────────┐
              ↓                 ↓
       SWISS-MODEL          AlphaFold
              ↓                 ↓
      Homology Model      Predicted Structure

SWISS-MODEL is strongly associated with template-based homology modelling, whereas AlphaFold uses a deep-learning-based prediction approach.

The internship introduced both approaches within the structural-bioinformatics section.

SWISS-MODEL and PDBsum

PDBsum can be useful for examining structural information associated with PDB structures that may serve as templates.

A simplified workflow is:

PDB
 ↓
Template Structure
 ↓
PDBsum
 ↓
Structural Information
 ↓
SWISS-MODEL
 ↓
Homology Model

This connects experimental structures with computational modelling.

SWISS-MODEL and Molecular Docking

A homology model can potentially be used as a starting point for downstream computational analysis.

The conceptual workflow is:

Protein Sequence
       ↓
SWISS-MODEL
       ↓
Homology Model
       ↓
Model Assessment
       ↓
Protein Preparation
       ↓
Ligand Preparation
       ↓
Molecular Docking

The internship progressed from protein structure prediction and homology modelling into protein preparation, ligand preparation and molecular docking.

However, a model should be evaluated for suitability before being used for docking.

Advantages

SWISS-MODEL-based homology modelling can:

Provide a structural model when a suitable experimental target structure is unavailable
Help visualize protein architecture
Support structural interpretation
Help explore domains and structural regions
Provide a starting point for some computational analyses
Limitations

Homology modelling also has limitations.

Template dependence

A suitable template is important for obtaining a useful model.

Sequence similarity

Lower similarity between target and template can increase uncertainty.

Coverage

A template may not cover the entire target protein.

Alignment errors

Incorrect alignment can produce structural inaccuracies.

Flexible regions

Loops and flexible regions can be difficult to model accurately.

Prediction is not experiment

The generated model is computationally constructed and should not automatically be treated as an experimentally determined structure.

Common Mistakes
Mistake 1: Selecting the first available template

The first template is not necessarily the most appropriate one.

Mistake 2: Ignoring coverage

A template may only represent part of the target.

Mistake 3: Ignoring sequence alignment

The quality of the alignment directly affects the model.

Mistake 4: Treating the model as experimentally verified

A homology model is a prediction.

Mistake 5: Using an unassessed model for docking

Model quality and the region being studied should be considered before downstream analysis.

Example Workflow
Step 1
Identify target protein
        ↓
Step 2
Retrieve target sequence
        ↓
Step 3
Submit / search sequence
        ↓
Step 4
Review available templates
        ↓
Step 5
Compare template suitability
        ↓
Step 6
Select template
        ↓
Step 7
Generate homology model
        ↓
Step 8
Assess model
        ↓
Step 9
Visualize model
        ↓
Step 10
Consider downstream analysis
What I Learned

SWISS-MODEL helped me understand how a protein sequence can be converted into a computational three-dimensional model using information from a related experimentally characterized protein.

The main progression was:

Target Sequence
      ↓
Template Search
      ↓
Template Selection
      ↓
Alignment
      ↓
Model Generation
      ↓
Model Assessment
      ↓
3D Visualization

During the internship, SWISS-MODEL was introduced specifically for understanding homology modelling and protein structure prediction, alongside PDB, AlphaFold and PyMOL.

Quick Revision
SWISS-MODEL
→ Resource for protein structure modelling

Main approach
→ Homology modelling

Target
→ Protein being modelled

Template
→ Related protein with a known structure

Main steps:
1. Target sequence
2. Template search
3. Template selection
4. Sequence alignment
5. Model generation
6. Model assessment
7. Visualization

Related resources:
→ UniProt
→ PDB
→ PDBsum
→ AlphaFold
→ PyMOL
Conclusion

SWISS-MODEL provides a practical way to generate protein structure models through homology modelling.

Its role can be summarized as:

Protein Sequence
       ↓
Find Related Structure
       ↓
Select Template
       ↓
Build Model
       ↓
Assess Model
       ↓
Visualize Structure

Within the internship, SWISS-MODEL formed part of the structural-bioinformatics workflow connecting protein annotation and experimental structures with predicted models and three-dimensional visualization.
