# Cytoscape

## Introduction

Cytoscape is an open-source platform used to visualize and analyse biological networks.

In bioinformatics, biological information can often be represented as a network containing nodes and connections. For example, in a protein-protein interaction (PPI) network:

```text
Node → Protein
Edge → Protein association

Cytoscape makes these networks easier to visualize, organize and analyse.

During the internship, Cytoscape was introduced as part of the network-analysis workflow following functional enrichment and STRING-based protein interaction analysis.

What is Cytoscape?

Cytoscape is a software platform designed for:

Network visualization
Network analysis
Biological network interpretation
Identifying important network features
Combining network information with biological data

Although Cytoscape is widely used in biological research, it is not limited to biology. It can also be used for general network analysis.

What is a Biological Network?

A biological network represents relationships between biological entities.

Examples include:

Protein-protein interaction networks
Gene regulatory networks
Metabolic networks
Signaling networks
Gene-gene association networks

A simple network can be represented as:

       B
      / \
     /   \
    A-----C
     \
      \
       D

Here:

A, B, C, D → Nodes

Lines → Edges
Cytoscape in PPI Analysis

One of the important applications of Cytoscape in the internship workflow was analysing protein-protein interaction networks.

The general workflow is:

Differentially Expressed Genes
            ↓
Functional Analysis
            ↓
Selected Genes
            ↓
STRING
            ↓
PPI Network
            ↓
Cytoscape
            ↓
Network Visualization
            ↓
Network Analysis
            ↓
Hub-Gene Identification

STRING and Cytoscape were included in the internship's downstream network-analysis component.

Nodes and Edges

Understanding nodes and edges is essential for working with Cytoscape.

Nodes

A node represents an entity.

In a PPI network:

Node = Protein

In other biological networks, a node could represent:

Gene
Protein
Metabolite
Compound
Disease
Biological process
Edges

An edge represents a relationship between two nodes.

For example:

Protein A ───── Protein B

The line represents an association between Protein A and Protein B.

Creating a Network

A network can be created by importing interaction data or by obtaining a network from an external resource such as STRING.

A simplified process is:

Interaction Data
      ↓
Import into Cytoscape
      ↓
Network Created
      ↓
Apply Layout
      ↓
Visualize
      ↓
Analyse

The resulting network can then be modified and analysed according to the research question.

Network Visualization

Large biological networks can initially look complicated.

For example:

A ─ B ─ C
│ ╲ │ ╱
D ─ E ─ F
    │
    G

Cytoscape provides different network layouts that help arrange nodes and edges in a more understandable way.

The purpose of a layout is mainly to improve visualization.

The physical position of a node on the screen should not automatically be interpreted as biological importance.

Network Layouts

Cytoscape supports different ways of arranging networks.

Common approaches include:

Force-directed layouts
Circular layouts
Grid layouts
Hierarchical layouts

A force-directed layout generally attempts to position connected nodes in a visually meaningful arrangement.

A circular layout places nodes around a circle.

A hierarchical layout can be useful when the network has a directional or hierarchical structure.

The appropriate layout depends on the type of network and how it needs to be presented.

Node Attributes

Cytoscape allows additional information to be associated with nodes.

For example:

Gene       log2FC       Adjusted P-value
----------------------------------------
Gene A      2.4             0.001
Gene B     -1.8             0.012
Gene C      3.1             0.004

This information can then be used to change the visual representation of the network.

For example:

Node size   → Degree
Node label  → Gene name
Node shape  → Category

The exact visual mapping should be clearly documented when preparing figures.

Edge Attributes

Edges can also contain information.

For example:

Protein A ─ Protein B

The edge may have an associated confidence or evidence value.

This can be used to distinguish stronger and weaker associations when appropriate.

Network Degree

One basic network property is degree.

Degree represents the number of edges connected to a node.

For example:

       B
       |
C ──── A ──── D
       |
       E

Protein A has:

Degree = 4

because it has four connections.

Degree can be useful for identifying highly connected nodes.

Hub Nodes

A node with a relatively large number of connections can be described as a hub in the analysed network.

For example:

       B
       |
C ─── HUB ─── D
       |
       E

Hub identification can be performed using network properties such as degree.

However:

High degree
      ≠
Proven disease causation

A hub is a network-level observation and should be interpreted together with biological and experimental evidence.

Centrality Measures

Cytoscape-based network analysis can involve different centrality measures.

Degree Centrality

Measures the number of direct connections.

Degree = Number of connected edges
Betweenness Centrality

Measures how frequently a node occurs on shortest paths between other nodes.

It can identify nodes that occupy connecting positions within a network.

Closeness Centrality

Measures how close a node is to other nodes in terms of network distance.

These measures describe network structure and should not automatically be treated as measures of biological importance.

Cytoscape and Hub-Gene Analysis

A simplified hub-gene workflow is:

PPI Network
     ↓
Network Analysis
     ↓
Calculate Centrality Measures
     ↓
Identify Highly Connected Nodes
     ↓
Candidate Hub Genes
     ↓
Biological Interpretation

The internship included hub-gene analysis as part of the broader research workflow.

Cytoscape in the Asthma Case Study

The internship included an asthma transcriptomics case study using GSE43696.

The overall workflow included:

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
GO / KEGG / g:Profiler
   ↓
STRING
   ↓
Cytoscape
   ↓
Hub-Gene Analysis

The internship report describes STRING and Cytoscape as part of the functional and network-analysis stage following differential gene-expression analysis.

Combining Expression Data with a Network

One useful feature of network visualization is that biological measurements can be associated with network nodes.

For example:

Gene A → log2FC = +2.5
Gene B → log2FC = -1.7
Gene C → log2FC = +3.0

This allows a PPI network to be viewed together with differential-expression information.

Conceptually:

        PPI Network
             +
    Gene Expression Data
             ↓
    Integrated Network View

This can make it easier to examine whether highly connected proteins also show interesting expression patterns.

From Functional Analysis to Cytoscape

Cytoscape is most useful when considered as part of a larger analysis rather than as an isolated tool.

The workflow covered during the internship can be summarized as:

Gene Expression Data
        ↓
Differential Expression
        ↓
Selected Genes
        ↓
Functional Enrichment
        ↓
GO / KEGG / g:Profiler
        ↓
Protein Associations
        ↓
STRING
        ↓
Network Visualization
        ↓
Cytoscape
        ↓
Hub / Network Analysis

This represents the progression from gene-level information to functional and network-level interpretation.

Why Network Visualization Helps

A gene list is essentially a collection of names:

Gene A
Gene B
Gene C
Gene D
Gene E

A network shows relationships:

Gene A ─ Gene B
   │       │
   │       │
Gene C ─ Gene D

This can reveal patterns that are difficult to notice from a simple table.

For example:

Highly connected regions
Isolated nodes
Clusters
Candidate hubs
Relationships between different functional groups
Network Clusters

A biological network may contain groups of closely connected nodes.

A simplified example:

A ─ B ─ C       X ─ Y
│ ╲ │ ╱         │ ╱
D ─ E           Z

The first group and second group may represent different network regions.

Such clusters can sometimes correspond to:

Protein complexes
Functional modules
Biological pathways
Related cellular processes

However, the biological meaning of a cluster must be investigated rather than assumed solely from its network structure.

Important Interpretation Principle

Network analysis generates hypotheses and patterns.

For example:

Highly connected protein
        ↓
Candidate hub
        ↓
Literature + functional evidence
        ↓
Further investigation

It should not be interpreted as:

Highly connected protein
        ↓
Confirmed disease-causing protein

Additional evidence is required to establish biological mechanisms.

Common Mistakes
Mistake 1: Confusing visualization with analysis

A visually central node is not necessarily mathematically or biologically important.

Mistake 2: Assuming every edge represents direct binding

PPI resources can contain functional associations supported by different evidence types.

Mistake 3: Ignoring the input dataset

The network depends on which genes or proteins were selected.

Mistake 4: Overinterpreting hub genes

Hub status describes network connectivity and does not establish causation.

Mistake 5: Creating unreadable figures

Large networks can become difficult to interpret if too many nodes and labels are displayed simultaneously.

Good Practices for Network Figures

When preparing a Cytoscape figure:

Use meaningful node labels
Keep the network readable
Explain what nodes represent
Explain what edges represent
State the source of interaction data
Document filtering criteria
Explain any colour, size or shape mappings
Avoid unnecessary visual complexity
Include an informative figure caption

For scientific reporting, the figure should be understandable without requiring the reader to guess what each visual element means.

Limitations

Cytoscape itself is primarily a visualization and network-analysis platform. The biological reliability of a network depends heavily on the data used to construct it.

Important limitations include:

Network quality depends on input data
Interaction databases may contain predicted associations
Some proteins have more annotation than others
Network structure can change with filtering criteria
Different network-analysis methods can produce different candidate hubs
Network centrality does not establish causality

Therefore, Cytoscape results should be interpreted alongside the original experimental and biological evidence.

What I Learned

The main concept I learned from Cytoscape was how biological interaction data can be converted into a visual and analyzable network.

The progression was:

Differentially Expressed Genes
            ↓
Functional Analysis
            ↓
Protein Interaction Data
            ↓
STRING
            ↓
Cytoscape
            ↓
Network Visualization
            ↓
Hub / Centrality Analysis

This helped me understand how bioinformatics analysis can move from a simple gene list towards a network-level representation of biological relationships.

Quick Revision
Cytoscape
↓
Platform for network visualization and analysis

Network:
Node → Entity
Edge → Relationship

In PPI analysis:
Node → Protein
Edge → Protein association

Uses:
- Network visualization
- Network analysis
- Centrality analysis
- Hub identification
- Integration of biological data

Important terms:
Degree
Betweenness
Closeness
Hub
Cluster

Workflow:
DEGs
 ↓
GO / KEGG / g:Profiler
 ↓
STRING
 ↓
Cytoscape
 ↓
Network Analysis
 ↓
Hub Genes
Conclusion

Cytoscape provides a practical way to visualize and analyse complex biological networks. In the internship workflow, it was used after functional enrichment and STRING-based protein interaction analysis to examine relationships between selected proteins and support downstream network and hub-gene analysis.

The key idea is:

A gene list tells us which genes are present.

Functional enrichment tells us what biological functions
are represented.

PPI analysis tells us how associated proteins are connected.

Cytoscape helps us see and analyse those connections
as a network.
