# Homology Modelling

## Introduction

Homology modelling is a computational approach used to construct a three-dimensional model of a target protein using the experimentally determined structure of a related protein as a template.

The basic idea is that proteins with sufficiently similar sequences can often have related structural arrangements.

During the internship, homology modelling was introduced as part of structural bioinformatics along with protein annotation, PDB analysis, AlphaFold, SWISS-MODEL and protein structure visualization. :contentReference[oaicite:0]{index=0}

The basic concept is:

```text
Target Protein Sequence
        ↓
Find Related Protein
        ↓
Select Structural Template
        ↓
Sequence Alignment
        ↓
Build Model
        ↓
Evaluate Model
        ↓
Predicted 3D Structure
What is Homology Modelling?

Homology modelling, also called comparative modelling, predicts the structure of a target protein based on a structurally characterized related protein.

The protein whose structure is being predicted is called the target.

The known structure used as a reference is called the template.

Target
→ Protein whose structure we want to model

Template
→ Related protein with a known structure
Why is Homology Modelling Useful?

Experimental structures are not available for every protein.

If a target protein has a suitable related protein with a known structure, homology modelling can provide a structural model.

A simplified workflow is:

Target Protein
      ↓
No Suitable Experimental Structure
      ↓
Search for Related Structure
      ↓
Suitable Template?
      ↓
Homology Modelling
      ↓
3D Model

This can provide structural information that may otherwise be unavailable.

Basic Principle

The underlying principle is:

Similar Sequence
      ↓
Related Protein
      ↓
Potentially Related Fold
      ↓
Structural Model

The reliability of the resulting model depends strongly on the relationship between the target and template and on the quality of the modelling process.

Target and Template
Target

The target is the protein for which a structural model is required.

Template

The template is a related protein for which a suitable experimentally determined structure is available.

For example:

Target Sequence
M A G K L V A A ...
        ↓
Search Related Proteins
        ↓
Template Structure
        ↓
Model Target
Template Selection

Choosing a suitable template is one of the important steps in homology modelling.

Useful considerations include:

Sequence similarity
Sequence coverage
Structural information
Biological relevance
Quality of the template structure
Presence of important regions
Completeness of the template

A template should not be selected simply because it has a similar name.

Sequence Alignment

The target sequence and template sequence need to be aligned.

A simplified alignment looks like:

Target:    M A G K L V A A T G
Template:  M A G K L I A A T G
           | | | | | | | | | |

The alignment identifies corresponding positions between the target and template.

A poor alignment can lead to an inaccurate structural model.

General Homology-Modelling Workflow
1. Obtain target sequence
          ↓
2. Search for related proteins
          ↓
3. Identify suitable templates
          ↓
4. Select template
          ↓
5. Align target and template
          ↓
6. Build structural model
          ↓
7. Evaluate model
          ↓
8. Inspect model
Step 1: Obtain the Target Sequence

The target protein sequence is required before modelling.

It can be obtained from a protein database such as UniProt.

Protein Identification
        ↓
UniProt
        ↓
Target Sequence

Protein annotation therefore provides the starting point for structural modelling.

Step 2: Search for a Template

The target sequence is compared with available protein sequences and structures to identify related proteins.

The goal is to find a structurally characterized protein that can act as a useful template.

Target Sequence
       ↓
Similarity Search
       ↓
Candidate Templates
       ↓
Template Selection
Step 3: Select the Template

A suitable template should provide sufficient sequence similarity and structural coverage for the region being modelled.

Important questions include:

How similar are the sequences?
How much of the target is covered?
Is the template structure complete?
Does it contain the relevant domain?
Is the structural information appropriate for the intended analysis?
Step 4: Align the Sequences

The target and template sequences are aligned before the model is constructed.

Target:    A B C D E F G H I
Template:  A B C D - F G H I

The alignment helps determine which residues correspond between the two proteins.

Step 5: Build the Model

The target structure is generated using information from the template structure and the target-template alignment.

Conceptually:

Template Structure
        +
Target-Template Alignment
        ↓
Structural Model

The resulting model represents a predicted three-dimensional structure of the target.

Step 6: Model Evaluation

A generated model should not automatically be considered correct.

It should be evaluated using appropriate structural and model-quality measures.

The evaluation can consider:

Overall structural quality
Geometry
Sequence-template relationship
Model confidence
Problematic regions
Alignment quality
Predicted Model
      ↓
Quality Assessment
      ↓
Identify Potential Problems
      ↓
Interpret Model Carefully
Step 7: Structural Inspection

The model can then be visually inspected.

A simplified workflow is:

Homology Model
      ↓
3D Visualization
      ↓
Inspect
├── Alpha helices
├── Beta sheets
├── Loops
├── Domains
└── Functional regions

PyMOL can be used for three-dimensional protein visualization and structural inspection.

During the internship, PyMOL was used for protein structure visualization.

SWISS-MODEL

SWISS-MODEL is a web-based resource for automated protein structure modelling.

During the internship, SWISS-MODEL was introduced for understanding homology modelling and protein structure prediction.

A simplified workflow is:

Target Sequence
       ↓
SWISS-MODEL
       ↓
Template Identification
       ↓
Model Generation
       ↓
Model Assessment
       ↓
3D Structure
Homology Modelling and PDB

PDB is important because experimentally determined structures can serve as templates for homology modelling.

The relationship can be represented as:

PDB
 ↓
Known Protein Structure
 ↓
Template
 ↓
Homology Modelling
 ↓
Target Protein Model

Therefore, experimental structural databases provide an important foundation for comparative modelling.

Homology Modelling and UniProt

UniProt provides useful information about the target protein, including its sequence and annotation.

The workflow is:

UniProt
 ↓
Target Protein
 ↓
Protein Sequence
 ↓
Template Search
 ↓
Homology Model

This demonstrates how protein annotation and structural modelling are connected.

Homology Modelling vs AlphaFold

Both approaches can produce computational protein structures, but their underlying approaches differ.

Feature	Homology Modelling	AlphaFold
Main principle	Uses a related structural template	Deep-learning-based structure prediction
Key requirement	Suitable template	Protein sequence and related information
Template dependence	Strong	Different from traditional template-based modelling
Output	Predicted structural model	Predicted structural model
Example resource	SWISS-MODEL	AlphaFold

The internship introduced both approaches as part of structural-bioinformatics training.

Homology Modelling and Experimental Structures

It is important to distinguish a model from an experimentally determined structure.

Experimental Structure
        ↓
Measured / determined experimentally

Homology Model
        ↓
Computationally constructed using a template

A homology model should therefore be treated as a prediction.

Importance of Sequence Similarity

The quality of a homology model depends significantly on how well the target is related to the template.

Conceptually:

Higher similarity
      ↓
Better basis for comparative modelling

Lower similarity
      ↓
Greater modelling uncertainty

This is a general principle rather than a guarantee of model quality.

Importance of Sequence Coverage

A template may be similar to the target but cover only part of the target sequence.

For example:

Target:
|---------------------------------------------|

Template:
|-------------------------|

In this case, the template may not provide structural information for the entire target.

Coverage should therefore be considered along with sequence similarity.

Loops and Insertions

Regions that differ between the target and template can be more challenging to model.

For example:

Target:    A B C D E F G H I J K
Template:  A B C D - - G H I J K

The additional or missing residues may require special modelling.

Flexible loops can also be structurally difficult to predict accurately.

Domains and Homology Modelling

A protein may contain several domains.

Sometimes a modelling analysis may focus on a particular domain rather than the complete protein.

Protein
|----------|-------------|-------------|
 Domain A     Domain B       Domain C
                 ↑
          Target region

Domain-level analysis can be useful when the relevant biological function is associated with a particular region.

Homology Modelling for Structural Analysis

Once a model has been generated, it can be used to explore questions about:

Overall protein architecture
Secondary structures
Domains
Potential binding regions
Relative positions of residues
Structural organization

However, conclusions should account for the fact that the structure is modelled rather than experimentally determined.

Homology Modelling and Molecular Docking

A homology model may sometimes serve as a starting structure for downstream computational analysis.

A conceptual workflow is:

Target Protein
      ↓
Sequence
      ↓
Template Search
      ↓
Homology Model
      ↓
Model Evaluation
      ↓
Protein Preparation
      ↓
Ligand Preparation
      ↓
Molecular Docking

The internship progressed from structure prediction and homology modelling towards protein preparation, ligand preparation and molecular docking.

The suitability of a model for docking should be evaluated rather than assumed.

Common Mistakes
Mistake 1: Choosing a template only by name

A similar protein name does not necessarily mean that the proteins are suitable structural relatives.

Mistake 2: Ignoring sequence alignment

A poor alignment can produce an inaccurate model.

Mistake 3: Ignoring coverage

A template that covers only part of the target may not be suitable for modelling the complete protein.

Mistake 4: Treating the model as an experimental structure

A homology model is computationally generated.

Mistake 5: Ignoring model quality

A generated model should be evaluated before being used for further analysis.

Mistake 6: Ignoring biological context

Structural similarity alone does not establish that two proteins perform the same biological function.

Limitations

Homology modelling has several limitations:

It depends on the availability of suitable templates.
Low sequence similarity can increase uncertainty.
Poor alignments can affect model accuracy.
Insertions and deletions can be difficult to model.
Flexible loops can be challenging.
The model may not represent every possible protein conformation.
A computational model does not replace experimental structural evidence.
Example Workflow
Step 1
Identify target protein
        ↓
Step 2
Retrieve target sequence
        ↓
Step 3
Search for related structures
        ↓
Step 4
Compare candidate templates
        ↓
Step 5
Select appropriate template
        ↓
Step 6
Align target and template
        ↓
Step 7
Generate model
        ↓
Step 8
Evaluate model
        ↓
Step 9
Visualize model
        ↓
Step 10
Use cautiously for downstream analysis
What I Learned

Homology modelling helped me understand how a protein structure can be computationally estimated when a related protein with a known structure is available.

The main progression was:

Target Sequence
      ↓
Related Structure
      ↓
Template
      ↓
Sequence Alignment
      ↓
Homology Model
      ↓
Model Evaluation
      ↓
3D Visualization

During the internship, SWISS-MODEL was introduced as a tool for understanding homology modelling and protein structure prediction, while PDB provided the structural context and PyMOL was used for visualization.

Quick Revision
Homology Modelling
→ Template-based protein structure modelling

Target
→ Protein whose structure is being predicted

Template
→ Related protein with a known structure

Main steps:
1. Target sequence
2. Template search
3. Template selection
4. Sequence alignment
5. Model generation
6. Model evaluation
7. Structural inspection

Important resource:
SWISS-MODEL

Related resources:
UniProt
PDB
PyMOL
AlphaFold
Conclusion

Homology modelling provides a way to construct a computational protein structure using the known structure of a related protein.

The process connects protein sequence, structural databases, sequence alignment and three-dimensional modelling:

Sequence
   ↓
Template
   ↓
Alignment
   ↓
Model
   ↓
Evaluation
   ↓
3D Structure

In the internship, homology modelling was introduced alongside PDB, AlphaFold, SWISS-MODEL and PyMOL as part of the broader transition from protein annotation to structural analysis and molecular docking.
