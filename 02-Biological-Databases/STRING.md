# STRING — Protein–Protein Interaction Database

STRING is a biological resource used to explore known and predicted protein–protein associations. During the internship, I was introduced to STRING as part of functional and network analysis, particularly for understanding how proteins interact with one another and how these interactions can be represented as a network.

## What is STRING?

STRING is a database and web resource for studying **protein–protein interactions (PPIs)**.

Instead of looking at proteins individually, STRING allows a group of proteins to be studied together as an interaction network.

A simplified representation is:

```text
Protein A ───── Protein B
    │              │
    │              │
Protein C ───── Protein D

Each protein can act as a node, while an association between proteins can be represented as an edge.

Why Protein–Protein Interactions Matter

Proteins rarely function completely independently.

Many biological processes depend on interactions between multiple proteins.

For example:

Protein A
    ↓
Interacts with
    ↓
Protein B
    ↓
Participates in
    ↓
Biological Process

Studying these relationships can therefore provide more information than studying individual proteins separately.

During the internship, this helped me understand the concept of network biology.

STRING Network

A STRING network represents relationships between proteins.

A simplified network can be visualised as:

          Protein B
         /         \
        /           \
Protein A ─────── Protein C
        \           /
         \         /
          Protein D

In this representation:

Nodes represent proteins.
Edges represent protein associations.

The resulting network can then be examined to identify important proteins and patterns of interaction.

From Gene List to STRING

STRING can be used after obtaining a list of genes or proteins of interest.

A simplified workflow is:

Gene / Protein List
        ↓
STRING
        ↓
Protein Identification
        ↓
Interaction Network
        ↓
Network Analysis
        ↓
Biological Interpretation

In a transcriptomics workflow, genes identified through differential expression can therefore become the starting point for protein-interaction analysis.

STRING in the Asthma Analysis

During the internship, the asthma transcriptomics analysis generated a list of genes of interest.

The broader workflow was:

GEO
 ↓
GSE43696
 ↓
GEO2R
 ↓
Differential Gene Expression
 ↓
Statistical Filtering
 ↓
Significant Genes
 ↓
Functional Analysis
 ↓
STRING
 ↓
PPI Network

The STRING network provided a way to examine relationships among proteins corresponding to genes of interest.

The detailed asthma analysis is documented separately in:

04-Asthma-Transcriptomics/

Interaction Confidence

Not every protein association has the same level of evidence.

STRING provides information about the confidence associated with interactions.

This is important because a network should not automatically be interpreted as proof that every connected pair of proteins physically interacts.

The evidence supporting an association should be considered when interpreting the network.

Different Sources of Evidence

Protein associations can be supported by different types of evidence.

Depending on the network and database information, evidence can come from sources such as:

Experimental evidence
Curated biological knowledge
Computational prediction
Co-expression
Other biological associations

Therefore, it is important to understand what an edge represents before drawing biological conclusions from it.

Network Nodes and Edges

Two basic concepts are important when working with interaction networks.

Node

A node represents an entity in the network.

In a STRING protein network:

Node = Protein
Edge

An edge represents an association between two nodes.

Protein A ───── Protein B
       Edge

Together, nodes and edges form the interaction network.

Network Topology

Once a network has been constructed, its overall structure can be examined.

Network topology refers to the arrangement and connectivity of nodes and edges.

Some proteins may have many connections, while others may have only a few.

       B
       |
A ─────C───── D
       |
       E

Here, protein C has more connections than proteins A, B, D and E.

Highly connected nodes can become candidates for further investigation, although connectivity alone does not establish biological importance.

Hub Proteins

A highly connected node in a biological network is often referred to as a hub.

A simplified example is:

        Protein B
             |
Protein A ─ Protein C ─ Protein D
             |
        Protein E

Protein C has several connections and could therefore be considered a highly connected node in this simplified network.

During the internship, hub-gene analysis was explored as part of network interpretation.

It is important to distinguish a computationally identified hub from a proven biological master regulator. Network centrality provides a clue for further investigation, not definitive proof of biological control.

STRING and Cytoscape

STRING can be used to construct and explore protein interaction networks, while Cytoscape provides additional network visualisation and analysis capabilities.

A simplified workflow is:

Gene / Protein List
        ↓
STRING
        ↓
PPI Network
        ↓
Cytoscape
        ↓
Network Visualisation
        ↓
Topology / Important Nodes
        ↓
Biological Interpretation

During the internship, Cytoscape was used for network visualisation and analysis.

Areas explored included:

Network visualisation
Network topology
Important nodes
Network clusters
Hub genes
Biological interpretation
Network Clusters

A network may contain groups of proteins that are more closely connected to each other.

These groups can form clusters or modules.

Conceptually:

Cluster 1                 Cluster 2

A ─ B                     F ─ G
│ ╲ │                     │ ╲ │
C ─ D                     H ─ I

Such groups can sometimes represent proteins involved in related biological processes, although their biological meaning requires further investigation.

Functional Interpretation of Networks

A PPI network becomes more useful when it is connected back to biological function.

For example:

Protein Network
      ↓
Important Nodes
      ↓
Functional Annotation
      ↓
Biological Processes
      ↓
Pathways
      ↓
Biological Interpretation

This connects network biology with resources such as Gene Ontology and KEGG.

STRING in the Overall Workflow

STRING fits into the larger bioinformatics workflow learned during the internship:

Biological Question
        ↓
Gene Expression Data
        ↓
Differentially Expressed Genes
        ↓
Functional Enrichment
        ↓
Pathway Analysis
        ↓
STRING
        ↓
PPI Network
        ↓
Cytoscape
        ↓
Network Interpretation

This demonstrates how gene-level results can be connected to protein-level interaction networks.

Practical Learning

During the internship, I developed familiarity with:

Understanding protein–protein interaction networks
Using STRING to explore protein associations
Creating interaction networks from proteins of interest
Understanding nodes and edges
Examining interaction confidence
Understanding basic network topology
Identifying highly connected nodes
Understanding hub-gene analysis
Connecting STRING with Cytoscape
Interpreting biological networks in context
Important Considerations

A STRING network should not be treated as direct experimental proof of every protein interaction.

When interpreting a network, it is important to consider:

Type of evidence
Interaction confidence
Biological context
Organism
Protein identity
Network size
Selection of input proteins
Purpose of the analysis

Similarly, a highly connected protein should not automatically be labelled as a disease-causing gene or master regulator.

Network analysis is better viewed as a method for identifying interesting relationships and candidates for further investigation.

Example Workflow

A complete simplified example is:

Differentially Expressed Genes
            ↓
Select Genes of Interest
            ↓
Protein Mapping
            ↓
STRING
            ↓
PPI Network
            ↓
Interaction Confidence
            ↓
Network Analysis
            ↓
Hub / Important Nodes
            ↓
Cytoscape
            ↓
Visualisation
            ↓
Biological Interpretation
Key Takeaways
STRING is used to study protein–protein associations.
Proteins can be represented as nodes in an interaction network.
Associations between proteins are represented as edges.
Different interactions can have different levels and types of supporting evidence.
STRING can be used to explore networks from a selected list of proteins.
Network topology can help identify highly connected nodes.
Highly connected nodes can be investigated as potential hub proteins.
STRING can be combined with Cytoscape for network visualisation and analysis.
PPI networks can be connected with functional enrichment and pathway analysis.
Computational network results require biological interpretation and should not automatically be treated as experimental proof.
Summary

Learning STRING introduced me to network-based analysis in bioinformatics. It helped me move from studying individual genes and proteins towards understanding how groups of proteins can be connected through interaction networks. Combined with functional analysis and Cytoscape visualisation, STRING provided a useful framework for exploring the biological relationships within a selected set of proteins.
