# STRING Protein-Protein Interaction (PPI) Analysis

## Introduction

Proteins rarely work completely independently inside a cell. Many biological functions depend on interactions between proteins.

Protein-protein interaction (PPI) analysis is used to study these relationships and to represent them as a network.

During the internship, STRING was introduced as a resource for analysing protein interactions after functional enrichment of selected genes. STRING was used together with GO, KEGG, g:Profiler and Cytoscape as part of the downstream functional and network-analysis workflow. :contentReference[oaicite:0]{index=0}

---

## What is STRING?

STRING is a database and web resource for studying **protein-protein associations**.

STRING stands for:

**Search Tool for the Retrieval of Interacting Genes/Proteins**

It provides information about relationships between proteins based on different types of evidence.

The important idea is that a STRING network does not necessarily mean that every connected pair of proteins has been experimentally shown to physically bind each other.

The relationships can represent different forms of functional association.

---

## What is a Protein-Protein Interaction?

A protein-protein interaction occurs when two proteins are associated with each other in a biological system.

These interactions can be involved in:

- Signal transduction
- Metabolic processes
- Gene regulation
- Immune responses
- Cellular communication
- Protein complexes
- Disease-related mechanisms

A simplified example is:

```text
Protein A
    ↓
Protein B
    ↓
Protein C

These proteins may participate in a common biological function or pathway.

What is a PPI Network?

A PPI network represents proteins and their relationships as a graph.

In a simple network:

       Protein B
       /       \
      /         \
Protein A ----- Protein C
      \
       \
      Protein D
Nodes

Each node represents a protein.

Edges

Each edge represents an association between two proteins.

Therefore:

Node → Protein

Edge → Protein association
Why Perform PPI Analysis?

Differential expression analysis identifies genes whose expression differs between conditions.

Functional enrichment helps determine which biological functions or pathways are represented.

PPI analysis adds another level of interpretation by asking:

How are the proteins encoded by these genes functionally connected?

This can help identify:

Highly connected proteins
Protein clusters
Functional modules
Relationships between candidate genes
Possible key components of a biological network
From Genes to Proteins

Transcriptomics generally produces information about gene expression.

For example:

Gene A
Gene B
Gene C
Gene D

For PPI analysis, these genes can be mapped to their corresponding proteins:

Gene A → Protein A
Gene B → Protein B
Gene C → Protein C
Gene D → Protein D

The protein relationships can then be represented as a network.

Basic STRING Workflow

A simplified workflow is:

Differentially Expressed Genes
            ↓
Select Relevant Genes
            ↓
Map Genes to Proteins
            ↓
Submit to STRING
            ↓
Generate PPI Network
            ↓
Examine Interactions
            ↓
Export Network
            ↓
Cytoscape
            ↓
Network Analysis

This follows the broader internship workflow in which differential expression and functional analysis were followed by STRING and Cytoscape-based network analysis.

Types of Evidence in STRING

STRING combines different types of evidence when determining protein associations.

These may include:

Experimental evidence
Database evidence
Co-expression
Gene neighbourhood
Gene fusion
Gene co-occurrence
Text mining
Other computational evidence

Because different evidence sources can contribute to an association, the network should be interpreted according to the evidence supporting each connection.

Experimental Evidence

Experimental evidence comes from experimentally observed biological relationships.

This type of evidence can provide direct support for an interaction or association.

However, the strength and nature of the experimental evidence should still be checked rather than assuming that every STRING edge represents a direct physical interaction.

Database Evidence

Previously established information from biological databases can contribute to STRING associations.

This allows known biological relationships to be incorporated into the network.

Co-expression

Genes or proteins that show similar expression patterns across datasets may be functionally related.

For example:

Condition 1 → Gene A ↑
Condition 2 → Gene A ↓

Condition 1 → Gene B ↑
Condition 2 → Gene B ↓

Similar expression patterns can provide evidence of functional association.

However, co-expression alone does not prove a physical interaction.

Text Mining

STRING can also use information extracted from scientific literature.

If two proteins are frequently discussed together in biological literature, this information may contribute to their predicted functional association.

Therefore, text-mining evidence should be interpreted as literature-based evidence rather than direct experimental proof.

Interaction Confidence

STRING provides confidence information for associations.

A higher confidence value indicates stronger combined evidence according to STRING's scoring system.

It is important to understand that:

High confidence
≠
Guaranteed physical binding

The score represents confidence in the association based on the evidence available to STRING.

Network Density

A network can contain many or few connections.

A highly connected network may indicate that many proteins in the input set have known or predicted functional relationships.

A sparse network may indicate fewer known associations among the selected proteins.

Network structure can therefore provide additional information beyond simply listing genes.

Hub Proteins

A hub protein is a protein with a relatively large number of connections in a network.

For example:

       Protein B
           |
           |
Protein C—Protein A—Protein D
           |
           |
       Protein E

Here, Protein A has several connections and can be considered a highly connected node.

Hub analysis can help identify proteins that occupy central positions in the analysed network.

However, high connectivity does not automatically mean that a protein is biologically responsible for a disease.

It is a network property that requires further biological validation.

PPI Analysis in the Asthma Case Study

The internship included an asthma transcriptomics case study based on GSE43696.

The analysis involved:

GSE43696
   ↓
GEO2R
   ↓
Healthy vs Asthma
   ↓
Differential Expression
   ↓
Statistical Filtering
   ↓
Selected Genes
   ↓
Functional Analysis
   ↓
STRING PPI Analysis
   ↓
Cytoscape
   ↓
Hub-Gene Analysis

STRING and Cytoscape were specifically included in the downstream network-analysis component of the internship.

The broader research component also focused on concepts such as hub genes, master regulators, disease pathways and molecular classification.

STRING and Functional Enrichment

STRING and enrichment tools answer different questions.

Functional enrichment

Examples:

GO
KEGG
g:Profiler

Main question:

What biological functions and pathways are represented by these genes?

STRING

Main question:

How are the proteins associated with these genes connected?

Therefore:

Gene List
   │
   ├──→ GO / KEGG / g:Profiler
   │       ↓
   │   Functions & Pathways
   │
   └──→ STRING
           ↓
       PPI Network

Using both approaches provides complementary information.

STRING and Cytoscape

STRING can be used to obtain interaction-network information, while Cytoscape is a platform for visualizing and analysing networks.

A simplified workflow is:

Gene / Protein List
       ↓
     STRING
       ↓
Interaction Network
       ↓
    Cytoscape
       ↓
Network Visualization
       ↓
Centrality / Hub Analysis

During the internship, STRING and Cytoscape were part of the network-analysis workflow following functional enrichment.

Why Use Cytoscape After STRING?

A STRING network can become difficult to interpret when many proteins are involved.

Cytoscape can make the network easier to:

Visualize
Organize
Filter
Analyse
Identify highly connected nodes
Present graphically

For example:

STRING
  ↓
Interaction data
  ↓
Cytoscape
  ↓
Network visualization
  ↓
Hub-gene analysis
Network Centrality

Network analysis can use different measures of centrality.

Degree Centrality

Degree is the number of connections associated with a node.

Degree =
Number of edges connected to a node

A protein with many connections has a high degree.

Betweenness Centrality

Betweenness measures how often a node lies along shortest paths between other nodes.

A protein with high betweenness may occupy an important connecting position within the network.

Closeness Centrality

Closeness describes how close a node is to other nodes in terms of network distance.

These measures can help describe network structure, but they should not automatically be interpreted as biological importance.

PPI Network Interpretation

Suppose a network contains:

Protein A → 2 connections
Protein B → 3 connections
Protein C → 15 connections
Protein D → 4 connections

Protein C has the highest degree in this example.

It may therefore be selected as a candidate hub based on degree centrality.

A proper interpretation would be:

Protein C is highly connected within the analysed network.

A stronger biological claim would require additional evidence.

Common Mistakes
Mistake 1: Treating every edge as direct physical binding

STRING represents functional associations and integrates multiple evidence types.

Mistake 2: Assuming a hub gene causes the disease

High network connectivity does not establish causation.

Mistake 3: Ignoring evidence sources

Different interactions may be supported by different types of evidence.

Mistake 4: Ignoring the input gene-selection method

The network depends on which genes were included.

Mistake 5: Overinterpreting network centrality

A central node is mathematically central in the analysed network, but this does not automatically establish biological importance.

Limitations

PPI analysis has several limitations:

Not all protein interactions are known
Database coverage varies between proteins and organisms
Computational predictions may contribute to associations
Different evidence sources have different strengths
Network structure depends on the selected input genes
Hub status does not establish causality
Experimental validation may be required
Relationship with Differential Expression

PPI analysis should generally be interpreted together with the original expression results.

For example:

Gene A
│
├── Expression change
├── Functional annotation
├── Pathway association
└── PPI relationships

A gene can therefore be examined from multiple perspectives.

The combined workflow is more informative than relying on one analysis alone.

Relationship with Hub-Gene Analysis

Hub-gene analysis is a downstream step of network analysis.

The basic idea is:

PPI Network
     ↓
Calculate network properties
     ↓
Identify highly connected nodes
     ↓
Candidate hub genes
     ↓
Biological interpretation

Hub genes may then be investigated using:

Literature
Expression patterns
Functional enrichment
Pathway analysis
Experimental studies

This provides a more complete interpretation of their potential relevance.

What I Learned

The main concept I learned from STRING PPI analysis was how individual genes can be connected through their corresponding proteins to form a biological interaction network.

The analysis helped me understand the transition from:

Differentially Expressed Genes
          ↓
Functional Enrichment
          ↓
Protein Associations
          ↓
PPI Network
          ↓
Network Analysis
          ↓
Hub Genes

This formed an important part of the broader transcriptomics-to-network-analysis workflow covered during the internship.

Quick Revision
STRING
↓
Search Tool for the Retrieval of Interacting Genes/Proteins

Purpose:
Study protein-protein associations.

Input:
Gene / protein list

Output:
PPI network

Network:
Node → Protein
Edge → Association

Evidence may include:
- Experiments
- Databases
- Co-expression
- Text mining
- Computational evidence

Important concept:
STRING association ≠ automatically direct physical interaction

Hub:
Highly connected node

Cytoscape:
Used for network visualization and analysis

Workflow:
DEGs
 ↓
Functional Analysis
 ↓
STRING
 ↓
PPI Network
 ↓
Cytoscape
 ↓
Hub-Gene Analysis
Conclusion

STRING PPI analysis adds a network-level perspective to transcriptomic analysis. Instead of considering differentially expressed genes as isolated entities, it allows their corresponding proteins to be examined in the context of functional associations.

In the internship workflow, STRING was used as part of the downstream analysis following differential expression and functional enrichment, with Cytoscape used for network visualization and further analysis.

The important takeaway is:

Genes → Functions → Pathways → Protein Associations → Networks

This progression helps build a broader biological interpretation of transcriptomic data.
