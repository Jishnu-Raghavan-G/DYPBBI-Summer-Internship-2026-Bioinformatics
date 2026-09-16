# PyMOL

## Introduction

PyMOL is a molecular visualization and analysis software used to view and examine three-dimensional structures of biological macromolecules, especially proteins.

It is useful for understanding protein architecture, secondary structures, domains, ligands, binding regions and interactions in a three-dimensional environment.

During the internship, PyMOL was introduced as part of the structural-bioinformatics component, alongside protein annotation, structure analysis, homology modelling and structure prediction. :contentReference[oaicite:0]{index=0}

## What is PyMOL?

PyMOL is a molecular graphics program that allows researchers to:

- Visualize protein structures
- Examine molecular geometry
- Highlight specific residues
- Display secondary structures
- Visualize ligands
- Inspect protein–ligand interactions
- Change molecular representations
- Prepare structural figures

A typical workflow is:

```text
Protein Structure
       ↓
Obtain Structure
       ↓
Load into PyMOL
       ↓
Choose Representation
       ↓
Select Important Regions
       ↓
Analyze / Visualize
       ↓
Generate Structural Figures
Protein Structure Visualization

Protein structures are three-dimensional objects, so visualization is an important part of structural bioinformatics.

PyMOL can display a protein using different representations.

Common representations include:

Cartoon
   ↓
Shows secondary structure

Surface
   ↓
Shows molecular surface

Sticks
   ↓
Shows bonds and atoms

Spheres
   ↓
Shows atoms / molecular volume
Cartoon Representation

The cartoon representation is commonly used for proteins because it makes secondary structural elements easy to recognize.

Typical elements include:

Alpha helices
Beta sheets
Loops and turns

Conceptually:

Protein
  │
  ├── α-Helices
  ├── β-Sheets
  └── Loops

This representation allows the overall fold of a protein to be understood without displaying every individual atom.

Surface Representation

Surface representation displays the outer molecular surface of a protein.

It can help visualize:

Protein shape
Cavities
Pockets
Exposed regions
Possible ligand-binding regions

A simplified concept is:

Protein Atoms
     ↓
Molecular Surface
     ↓
Surface / Pocket Visualization
Stick Representation

The stick representation displays bonds between atoms.

It is particularly useful when examining:

Ligands
Active-site residues
Amino-acid side chains
Protein–ligand interactions

For example:

Protein
   ↓
Select Active-Site Residues
   ↓
Display as Sticks
   ↓
Inspect Local Environment
Selecting Residues

Specific residues can be selected in PyMOL for closer examination.

Selection can be based on:

Residue number
Residue name
Chain
Ligand
Structural region

A conceptual example is:

Entire Protein
      ↓
Select Residues of Interest
      ↓
Change Representation
      ↓
Inspect Selected Region

This is useful when a particular active site, binding region or mutation needs to be examined.

Chains

Many protein structures contain more than one polypeptide chain.

For example:

Protein Structure
│
├── Chain A
├── Chain B
└── Chain C

PyMOL allows individual chains to be selected and displayed separately.

This can help when studying:

Multimeric proteins
Protein–protein interactions
Different subunits
Chain-specific regions
Ligand Visualization

Protein structures may contain small molecules such as:

Substrates
Inhibitors
Cofactors
Metal ions
Drug-like molecules

PyMOL can display these molecules together with the protein.

A simplified workflow is:

Protein Structure
      +
Ligand
      ↓
Load into PyMOL
      ↓
Display Protein
      ↓
Display Ligand
      ↓
Inspect Binding Region
Protein–Ligand Interaction

PyMOL can be used to visually inspect the environment surrounding a ligand.

For example:

Protein
   ↓
Binding Pocket
   ↓
Ligand
   ↓
Nearby Residues

Potential interactions that may be examined include:

Hydrogen-bonding relationships
Electrostatic interactions
Hydrophobic contacts
Spatial proximity

Visual inspection is useful for understanding the structural context of docking results.

PyMOL in Molecular Docking

PyMOL can be used after molecular docking to visualize docking poses.

A simplified workflow is:

Protein
   ↓
Protein Preparation
   ↓
Docking
   ↓
Docked Complex
   ↓
PyMOL
   ↓
Visualize Binding Pose

The docking score alone does not show how a ligand is positioned inside the binding site. Visualization provides structural context.

Viewing Docking Poses

When a docked ligand is loaded into PyMOL, the ligand can be displayed together with the protein.

A useful representation is:

Protein → Cartoon / Surface
Ligand  → Sticks
Binding residues → Sticks

This makes the binding region easier to inspect.

Structural Comparison

PyMOL can also be useful for comparing protein structures.

For example:

Structure A
     +
Structure B
     ↓
Structural Comparison
     ↓
Identify Similar / Different Regions

Structural comparison can help examine similarities in overall fold or differences in particular regions.

Working with Homology Models

A structure generated through homology modelling can also be visualized in PyMOL.

The workflow is:

Target Sequence
      ↓
SWISS-MODEL
      ↓
Homology Model
      ↓
PyMOL
      ↓
3D Visualization

This allows the predicted structure to be inspected visually after model generation.

Working with AlphaFold Structures

Predicted structures obtained from AlphaFold can similarly be visualized using molecular visualization software.

Protein Sequence
      ↓
AlphaFold Prediction
      ↓
Predicted Structure
      ↓
PyMOL
      ↓
Structural Inspection

The internship included AlphaFold and PyMOL within the structural-bioinformatics workflow.

Basic PyMOL Commands

PyMOL provides commands that can be used to control molecular visualization.

Load a Structure
load protein.pdb

This loads a PDB structure into PyMOL.

Show Cartoon
show cartoon

Displays the protein using cartoon representation.

Show Sticks
show sticks

Displays selected molecular components as sticks.

Show Surface
show surface

Displays the molecular surface.

Hide Representation
hide everything

Hides the currently displayed representations.

Select a Residue

For example:

select residue_100, resi 100

This creates a selection containing residue 100.

Show Selected Residue as Sticks
show sticks, residue_100

This displays the selected residue using sticks.

Example Visualization Workflow
1. Obtain PDB structure
        ↓
2. Open PyMOL
        ↓
3. Load structure
        ↓
4. Display protein as cartoon
        ↓
5. Identify region of interest
        ↓
6. Select important residues
        ↓
7. Display residues as sticks
        ↓
8. Display ligand if present
        ↓
9. Inspect structural relationships
        ↓
10. Prepare figure
PyMOL in the Internship Workflow

The structural-bioinformatics section followed a broader workflow:

Protein Annotation
       ↓
Protein Sequence
       ↓
Protein Structure
       ↓
PDB / AlphaFold / SWISS-MODEL
       ↓
Structure Visualization
       ↓
PyMOL
       ↓
Molecular Docking

The internship report specifically describes protein annotation, protein-structure visualization, homology modelling and structure prediction using resources including UniProt, PDB, AlphaFold and SWISS-MODEL, followed by practical exposure to molecular docking.

Importance of Visualization

Visualization is important because structural information is easier to interpret when viewed in three dimensions.

For example, a sequence may indicate that particular residues are present, but a three-dimensional structure can help determine whether those residues are:

Close to one another
Located in the same structural region
Near a ligand
Exposed on the surface
Located inside a potential binding pocket

Thus:

Sequence Information
        +
Structural Information
        ↓
3D Visualization
        ↓
Better Structural Interpretation
Limitations

PyMOL is primarily a visualization and molecular-analysis environment. Visual inspection alone does not establish that an interaction is biologically or experimentally confirmed.

For computational structures:

Predicted Structure
      ↓
Visualization
      ↓
Structural Interpretation

should not be confused with:

Experimental Validation

Computational observations should therefore be interpreted within the limitations of the underlying structural data.

What I Learned

PyMOL helped me understand how three-dimensional protein structures can be examined visually after obtaining structures from databases or computational prediction tools.

The main concepts included:

Protein structure visualization
Cartoon representation
Surface representation
Stick representation
Chain and residue selection
Ligand visualization
Binding-site inspection
Visualization of predicted structures
Visualization of docking complexes

The software connected the structural concepts learned through PDB, AlphaFold and SWISS-MODEL with practical three-dimensional molecular visualization.

Quick Revision
PyMOL
→ Molecular visualization and analysis software

Main uses:
→ Protein visualization
→ Structure inspection
→ Residue selection
→ Ligand visualization
→ Binding-site inspection
→ Docking-pose visualization
→ Structural figures

Common representations:
→ Cartoon
→ Surface
→ Sticks
→ Spheres

Important workflow:
Protein Structure
      ↓
Load into PyMOL
      ↓
Choose Representation
      ↓
Select Region
      ↓
Visualize / Analyze
Conclusion

PyMOL provides an effective way to convert structural data into an interpretable three-dimensional representation.

Within the internship, it served as the visualization component connecting protein structures and computational models with downstream structural analysis and molecular docking.
