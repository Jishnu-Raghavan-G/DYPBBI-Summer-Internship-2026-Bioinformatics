Overview

After identifying and filtering the differentially expressed genes from the GSE43696 asthma transcriptomics analysis, the next stage was to examine relationships between the proteins associated with those genes.

This was done using protein-protein interaction (PPI) network analysis, with STRING used to investigate protein interactions and Cytoscape used for network visualization and analysis.

What Is a PPI Network?

A protein-protein interaction network represents relationships between proteins.

Instead of studying each gene independently, the genes can be connected through the proteins they encode.

Gene
 ↓
Protein
 ↓
Protein-Protein Interaction
 ↓
Network

A network can therefore provide a broader view of how different molecular components may be connected.

Why Use PPI Analysis?

A DEG list tells us which genes show differences in expression.

However, genes and their protein products generally function as parts of biological systems rather than completely independently.

PPI analysis therefore helps answer questions such as:

Which proteins interact with each other?
Which proteins form connected groups?
Which genes are represented in the interaction network?
Which nodes have many connections?
Are there network-level patterns worth investigating?
Workflow

The PPI analysis followed the broader case-study workflow:

Differentially Expressed Genes
             ↓
       Selected Gene List
             ↓
           STRING
             ↓
 Protein-Protein Interaction Network
             ↓
         Cytoscape
             ↓
   Network Visualization & Analysis
             ↓
       Hub-Gene Analysis

STRING and Cytoscape were specifically included in the internship's downstream functional/network-analysis workflow.

STRING

STRING is a resource used to investigate known and predicted protein-protein associations.

The selected genes from the transcriptomics analysis can be submitted to STRING to obtain an interaction network.

Conceptually:

Gene list
   ↓
STRING
   ↓
Protein identifiers
   ↓
Interaction information
   ↓
PPI network

The resulting network can then be explored for connectivity and relationships among the proteins.

Network Nodes and Edges

A basic network contains two important elements.

Nodes

Nodes represent proteins or other biological entities included in the network.

●   ●   ●   ●
Edges

Edges represent interactions or associations between nodes.

●────●
 \   /
  \ /
   ●

Therefore:

Node = biological entity

Edge = relationship/interaction
Interaction Confidence

Interaction databases can assign confidence information to associations.

A higher-confidence interaction provides stronger support within the database's scoring framework, while lower-confidence interactions should be interpreted more cautiously.

Therefore, network analysis should consider the confidence settings used when generating the network.

Cytoscape

After obtaining the interaction network, Cytoscape was used for network visualization and exploration.

Cytoscape makes it easier to:

Visualize nodes and edges
Rearrange networks
Examine connectivity
Identify highly connected nodes
Apply network layouts
Export network figures

The internship workflow included Cytoscape after STRING for PPI network analysis.

Network Visualization

A simplified PPI network may look conceptually like:

       ●
      / \
     ●───●
    / \   \
   ●   ●───●
        \
         ●

Different network layouts can make different structural features easier to examine.

The final repository can include screenshots or exported network figures under:

04-Asthma-Transcriptomics-Case-Study/Figures/

General Cytoscape screenshots can also be organized under:

14-Figures-and-Screenshots/Cytoscape/
From PPI Network to Hub Genes

One of the main reasons for constructing a PPI network is to investigate highly connected nodes.

The next stage of the case study therefore involved hub-gene analysis.

Conceptually:

PPI Network
     ↓
Examine node connectivity
     ↓
Identify highly connected nodes
     ↓
Hub-gene analysis
     ↓
Further biological interpretation

The internship documentation specifically describes STRING, Cytoscape and hub-gene analysis as components of the downstream network workflow.

Important Interpretation

A PPI network should not be interpreted as proof that every displayed interaction occurs directly inside the biological system being studied.

Interaction databases can contain information from different experimental studies, computational predictions and curated sources.

Therefore, network results should be treated as a way of generating and investigating biological relationships, rather than automatically establishing causation.

Relationship With Functional Enrichment

PPI analysis complements the functional-enrichment stage.

DEGs
 ↓
Functional Enrichment
 ↓
"What functions/pathways are represented?"
 
DEGs
 ↓
PPI Network
 ↓
"How are the associated proteins connected?"

Using both perspectives provides a more complete interpretation of the transcriptomics results.

What I Learned

This part of the internship helped me understand how gene-level transcriptomics results can be converted into a network representation.

The main concepts I learned were:

Protein-protein interactions
STRING
Network nodes and edges
Interaction confidence
Cytoscape
Network visualization
Node connectivity
Hub-gene analysis
Interpretation of biological networks

The PPI analysis therefore extended the GSE43696 analysis from individual differentially expressed genes toward relationships between proteins within a biological network.
