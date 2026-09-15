# Bioinformatics Workflow

A bioinformatics workflow is a systematic sequence of steps used to convert a biological question or raw biological data into meaningful biological information.

During the internship, I learned that bioinformatics is not simply about using individual software or databases. The important part is understanding how different resources can be connected to answer a biological question.

## 1. Starting With a Biological Question

Every analysis should begin with a clearly defined biological question.

Examples include:

- Which genes are associated with a disease?
- Which genes show different expression between two conditions?
- What biological pathways are affected?
- How do proteins interact with each other?
- What does the three-dimensional structure of a protein look like?
- How might a ligand interact with a target protein?

The biological question determines the type of data, database and analysis method required.

## 2. Finding Relevant Biological Data

Once the question is defined, the next step is to identify suitable biological data.

Depending on the problem, this may include:

- Genomic data
- Gene expression data
- Protein sequences
- Protein structures
- Gene or protein lists
- Protein–protein interaction data

Public biological databases can be used to locate relevant information.

## 3. Selecting an Appropriate Database

Different biological databases provide different types of information.

For example:

- NCBI → General biological and sequence resources
- GEO → Gene expression datasets
- UniProt → Protein annotation and functional information
- PDB → Experimentally determined structures
- AlphaFold → Predicted protein structures
- STRING → Protein–protein interactions
- GO → Functional annotation
- KEGG → Biological pathways
- g:Profiler → Functional enrichment
- SWISS-MODEL → Homology modelling

Therefore, database selection should be based on the biological question.

## 4. Dataset Exploration and Preparation

After obtaining a dataset, it needs to be understood before analysis.

Important information includes:

- Dataset identification
- Sample information
- Experimental conditions
- Disease and healthy groups
- Available measurements
- Gene or protein identifiers
- Relevant metadata

Understanding the experimental design is important because computational results depend on how the original biological data were generated.

## 5. Data Analysis

The analysis depends on the type of biological data.

For gene expression studies, an example workflow is:

```text
Gene Expression Dataset
        ↓
Sample Grouping
        ↓
Comparison
        ↓
Differential Gene Expression
        ↓
Statistical Filtering
        ↓
Significant Genes

During the internship, this workflow was applied to an asthma transcriptomics study using the GEO dataset GSE43696 and GEO2R.

The detailed asthma analysis is documented separately in the asthma transcriptomics section.

6. Functional Interpretation

A list of genes is usually only the starting point for biological interpretation.

The selected genes can be analysed to understand their possible biological roles.

Significant Genes
        ↓
Functional Annotation
        ↓
Biological Processes
        ↓
Molecular Functions
        ↓
Cellular Components

Gene Ontology can be used to investigate:

Biological Process
Molecular Function
Cellular Component
7. Pathway Analysis

Genes rarely act independently. They are often involved in biological pathways and signalling systems.

Pathway analysis helps connect individual genes to larger biological processes.

A simplified workflow is:

Gene List
    ↓
Pathway Analysis
    ↓
Relevant Biological Pathways
    ↓
Biological Interpretation

KEGG was explored during the internship for pathway analysis.

g:Profiler was also used as a functional enrichment resource for interpreting gene lists.

8. Protein–Protein Interaction Analysis

After identifying genes or proteins of interest, their relationships can be explored through protein–protein interaction networks.

Genes / Proteins
       ↓
STRING
       ↓
Interaction Network
       ↓
Cytoscape
       ↓
Network Visualisation
       ↓
Hub / Important Nodes

STRING was used to explore protein–protein interactions, while Cytoscape was used for network visualisation and analysis.

This helped demonstrate that biological functions are often carried out through interacting groups of proteins rather than isolated proteins.

9. Structural Analysis

Once important proteins are identified, their structures can be investigated.

A simplified structural workflow is:

Protein
   ↓
UniProt
   ↓
PDB / AlphaFold / SWISS-MODEL
   ↓
Structural Information
   ↓
PDBsum
   ↓
3D Visualisation
   ↓
Structural Interpretation

Different resources provide different types of structural information.

UniProt → Protein annotation
PDB → Experimental structures
AlphaFold → Predicted structures
SWISS-MODEL → Homology modelling
PDBsum → Structural summaries
PyMOL → Three-dimensional visualisation
10. Protein–Ligand Analysis

Structural information can also be used as a starting point for molecular docking studies.

The general workflow is:

Target Protein
      ↓
Protein Preparation
      ↓
Ligand Preparation
      ↓
Docking
      ↓
Docking Poses
      ↓
Binding Interactions
      ↓
Result Interpretation

During the internship, I was introduced to protein and ligand preparation, ChimeraX, AutoDock Tools and AutoDock Vina.

Virtual screening extends this concept by evaluating multiple compounds computationally and prioritising potentially interesting candidates for further investigation.

11. Statistical Interpretation

Bioinformatics results should not be interpreted only by looking at lists, graphs or software outputs.

Statistical concepts are important when analysing biological data.

Examples include:

Statistical significance
P-values
Adjusted p-values
Log₂ fold change
Confidence intervals
Correlation
Data distribution

The appropriate statistical criteria depend on the type of analysis and experimental design.

12. Biological Interpretation

The final objective of a bioinformatics workflow is not simply to generate computational results.

The results need to be interpreted in a biological context.

For example:

Data
 ↓
Genes
 ↓
Functions
 ↓
Pathways
 ↓
Protein Interactions
 ↓
Network Biology
 ↓
Protein Structures
 ↓
Protein–Ligand Interactions
 ↓
Biological Interpretation

This was one of the important concepts I learned during the internship: a list of genes by itself does not provide the complete biological picture.

13. Validation and Critical Thinking

Computational results should always be interpreted carefully.

Factors that can affect interpretation include:

Quality of the original dataset
Sample selection
Statistical thresholds
Gene annotation
Database evidence
Interaction confidence
Structural quality
Docking assumptions
Biological context

Software output should therefore be treated as evidence that needs interpretation rather than as an unquestionable conclusion.

14. Documentation and Reproducibility

A good bioinformatics workflow should be properly documented.

Important information to record includes:

Dataset accession number
Database used
Software or online tool used
Parameters and thresholds
Input data
Output files
Important observations
Figures and screenshots
References

Proper documentation makes it easier to understand, reproduce and communicate an analysis.

Overall Internship Workflow

The different concepts learned during the internship can be connected into one broader workflow:

Biological Question
        ↓
Data / Dataset Identification
        ↓
Database Exploration
        ↓
Data Analysis
        ↓
Differential / Statistical Analysis
        ↓
Significant Genes
        ↓
Functional Enrichment
        ↓
Pathway Analysis
        ↓
Protein–Protein Interaction Analysis
        ↓
Network Analysis
        ↓
Protein Annotation
        ↓
Structural Analysis
        ↓
Protein–Ligand Analysis
        ↓
Biological Interpretation

Not every bioinformatics project follows this exact sequence. The workflow changes depending on the biological question and the type of data available.

Example From the Internship

One of the clearest examples of this approach was the asthma transcriptomics case study:

NCBI GEO
   ↓
GSE43696
   ↓
GEO2R
   ↓
Healthy vs Asthma
   ↓
Differential Gene Expression
   ↓
Statistical Filtering
   ↓
Significant Genes
   ↓
GO / KEGG / g:Profiler
   ↓
STRING
   ↓
Cytoscape
   ↓
Network Interpretation

This practical example helped connect the individual databases and analytical concepts learned throughout the internship.

Key Takeaways
A bioinformatics workflow begins with a biological question.
The biological question determines the required data and tools.
Biological databases provide different types of complementary information.
Data analysis is followed by biological interpretation.
Gene lists can be studied through functional enrichment and pathway analysis.
Protein interactions can be explored using network-based approaches.
Important proteins can be investigated at the structural level.
Molecular docking can be used to study possible protein–ligand interactions.
Statistical and biological context are essential for interpreting computational results.
Proper documentation improves reproducibility.
Bioinformatics is most useful when different computational resources are connected to answer a biological question.

The main lesson from this workflow was that bioinformatics is a connected process rather than a collection of unrelated tools.
