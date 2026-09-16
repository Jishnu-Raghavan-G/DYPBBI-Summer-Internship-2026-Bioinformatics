# Hub-Gene Analysis

## Introduction

In a biological network, some nodes have many more connections than others. These highly connected nodes can be identified using network-analysis methods and are commonly referred to as **hub nodes** or **hub genes** when the network represents genes or their corresponding proteins.

Hub-gene analysis was included in the downstream network-analysis component of the internship. The broader research work also covered concepts such as hub genes, master regulators, disease pathways and molecular classification. :contentReference[oaicite:0]{index=0}

The basic idea is:

```text
Gene List
   ↓
PPI Network
   ↓
Network Analysis
   ↓
Identify Highly Connected Nodes
   ↓
Candidate Hub Genes
   ↓
Biological Interpretation
What is a Hub Gene?

A hub gene is a gene whose corresponding protein has a relatively large number of connections within the analysed network.

For example:

        Gene B
          |
          |
Gene C — Gene A — Gene D
          |
          |
        Gene E

Here, Gene A has several connections and may be considered a hub based on its network connectivity.

The important point is that hub status is relative to the network being analysed.

A gene may be highly connected in one network but not in another network constructed using different input data or filtering criteria.

Why Identify Hub Genes?

Differential expression analysis can produce many significant genes.

For example:

Gene A
Gene B
Gene C
Gene D
Gene E
Gene F
...
Gene Z

Network analysis can help identify genes that occupy prominent positions within the interaction network.

Hub-gene analysis can therefore be useful for:

Prioritising candidate genes
Understanding network structure
Identifying highly connected proteins
Exploring functional relationships
Generating hypotheses for further research
Selecting candidates for additional biological investigation

It is a prioritisation approach rather than proof of biological causation.

Hub Genes in the Transcriptomics Workflow

The internship workflow can be represented as:

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
Selected Genes
   ↓
Functional Enrichment
   ↓
GO / KEGG / g:Profiler
   ↓
STRING PPI Network
   ↓
Cytoscape
   ↓
Hub-Gene Analysis

The internship report describes GSE43696, differential expression, functional enrichment and subsequent STRING/Cytoscape network analysis as components of the practical workflow.

From Differentially Expressed Genes to Hub Genes

The process starts with a set of genes obtained from differential expression analysis.

For example:

Differentially Expressed Genes
            ↓
        Gene Filtering
            ↓
        Selected Genes
            ↓
     Protein Interaction
            ↓
        PPI Network
            ↓
     Network Properties
            ↓
      Candidate Hubs

The genes included in the network are important because they determine the network that will be analysed.

Degree Centrality

One of the simplest ways to identify highly connected nodes is degree centrality.

Degree is the number of direct connections a node has.

For example:

          B
          |
          |
C ———— A ———— D
          |
          |
          E

Gene A has four direct connections.

Therefore:

Degree(A) = 4

If Gene B has only one connection:

Degree(B) = 1

Gene A would have a higher degree in this example.

Betweenness Centrality

Another network measure is betweenness centrality.

It describes how frequently a node lies along shortest paths connecting other nodes in a network.

A simplified example:

A —— B —— C

If B connects two otherwise separated parts of the network, B may have relatively high betweenness.

This can identify nodes that occupy connecting positions within a network.

Closeness Centrality

Closeness centrality is based on the distance between a node and other nodes in the network.

A node that can reach other nodes through relatively short paths may have higher closeness.

Conceptually:

Shorter network distances
        ↓
Greater closeness

Like other centrality measures, it describes a mathematical property of the network.

Comparing Centrality Measures

Different centrality measures capture different aspects of network structure.

Measure	Basic idea
Degree	Number of direct connections
Betweenness	Position along shortest paths
Closeness	Distance to other nodes

Therefore, the term "hub" should be interpreted in relation to the method used to identify it.

Hub-Gene Identification

A simplified method is:

PPI Network
     ↓
Calculate Degree
     ↓
Rank Nodes
     ↓
Select Highly Connected Nodes
     ↓
Candidate Hub Genes

For example:

Gene A → Degree 18
Gene B → Degree 12
Gene C → Degree 5
Gene D → Degree 3

Gene A is the most connected node in this small example.

It can therefore be described as a highly connected node in the analysed network.

Hub Genes and Cytoscape

Cytoscape can be used to visualize and analyse interaction networks.

A typical workflow is:

STRING
  ↓
PPI Network
  ↓
Import / Visualize
  ↓
Cytoscape
  ↓
Network Analysis
  ↓
Centrality Measures
  ↓
Candidate Hub Genes

Cytoscape makes it possible to inspect the network structure and associate network properties with individual nodes.

The internship included Cytoscape as part of the network-analysis stage following STRING.

Visualizing Hub Genes

A network can be visually modified to make highly connected nodes easier to identify.

For example:

             B
             |
             |
       C — HUB — D
             |
             |
             E

Node properties can be mapped to visual features.

For example:

Node size → Degree
Node label → Gene name

A larger node can therefore represent a higher degree if that mapping has been explicitly defined.

The figure legend should always explain the mapping.

Hub Genes and Differential Expression

A useful analysis can combine network connectivity with expression changes.

For example:

Gene A
log2FC = +2.4
Degree = 15

Gene B
log2FC = -1.8
Degree = 12

Gene C
log2FC = +0.4
Degree = 20

This provides two different types of information:

Differential expression
        +
Network connectivity

A highly connected gene and a strongly differentially expressed gene are not necessarily the same gene.

This distinction is important when interpreting network results.

Hub Genes and Functional Enrichment

After identifying candidate hubs, they can be examined using functional resources.

For example:

Candidate Hub Genes
        ↓
GO Analysis
        ↓
KEGG Analysis
        ↓
Pathway Interpretation

This can help determine whether candidate hubs are associated with biological functions or pathways relevant to the research question.

The internship workflow combined functional enrichment using GO, KEGG and g:Profiler with subsequent STRING/Cytoscape network analysis.

Hub Genes and Literature

A candidate hub should also be investigated using scientific literature.

A simplified workflow is:

Candidate Hub
      ↓
Functional Annotation
      ↓
Pathway Information
      ↓
Existing Literature
      ↓
Expression Evidence
      ↓
Further Investigation

Literature can help determine whether the candidate has previously been associated with the biological condition or pathway being studied.

However, previous association does not automatically establish a causal role.

Hub Genes in Disease Research

Network-based analysis is commonly used in disease-related bioinformatics research.

The general concept is:

Disease Dataset
      ↓
Differential Expression
      ↓
Candidate Genes
      ↓
PPI Network
      ↓
Network Analysis
      ↓
Candidate Hub Genes
      ↓
Functional Interpretation

In the internship's research component, disease-related transcriptomic analysis included concepts such as hub genes, master regulators, disease pathways and molecular classification.

Asthma Transcriptomics Context

The asthma case study used GSE43696 and compared healthy and asthma-related samples.

After differential expression and statistical filtering, selected genes were used for downstream functional and network analysis.

The network-analysis stage can be represented as:

Selected Genes
      ↓
STRING
      ↓
PPI Network
      ↓
Cytoscape
      ↓
Network Properties
      ↓
Candidate Hub Genes
      ↓
Functional / Biological Interpretation

The purpose is to move from a list of differentially expressed genes toward a network-level view of their relationships.

Hub Gene vs Master Regulator

These terms should not be treated as identical.

Hub Gene

A hub gene is identified based primarily on its position or connectivity within a network.

Network property
      ↓
High connectivity
      ↓
Hub
Master Regulator

A master regulator generally refers to a biological regulator that controls or influences multiple downstream processes, such as transcriptional programs.

Regulatory activity
      ↓
Influence on multiple targets
      ↓
Regulatory role

A highly connected PPI hub is therefore not automatically a master regulator.

Important Interpretation

One of the most important lessons in network analysis is:

High connectivity
        ≠
Biological causation

A hub gene may be:

Important to the analysed network
Well studied
Highly connected
Associated with multiple pathways

But these observations alone do not establish that the gene causes a disease or phenotype.

Additional evidence is required.

Why Hub Results Can Change

Hub-gene results depend on several factors.

Input genes

Changing the gene list changes the network.

Interaction database

Different databases can contain different interactions.

Confidence threshold

Changing the interaction-confidence cutoff can remove or add edges.

Network-analysis method

Different centrality measures can identify different nodes.

Organism and annotation

The available interaction information depends on biological annotation.

Therefore, hub identification is analysis-dependent.

Common Mistakes
Mistake 1: Calling the highest-degree gene "the most important gene"

Degree measures connectivity, not overall biological importance.

Mistake 2: Assuming hub genes cause disease

Network connectivity does not prove causality.

Mistake 3: Ignoring network construction

The network depends on the selected genes, database and filtering criteria.

Mistake 4: Using only one type of evidence

Network results are stronger when considered together with expression, functional and literature evidence.

Mistake 5: Confusing hub genes with master regulators

A network hub and a biological regulator are different concepts.

Limitations

Hub-gene analysis has several limitations:

Results depend on the input gene list
PPI databases are incomplete
Some interactions may be predicted
Highly studied proteins may have more known interactions
Different centrality methods can produce different results
Network connectivity does not establish biological causation
Experimental validation may be necessary
A Better Way to Interpret a Hub

Instead of writing:

Gene X is the most important gene in asthma.

a more scientifically appropriate statement is:

Gene X showed high connectivity within the analysed
PPI network and was therefore identified as a candidate
hub gene for further investigation.

This separates the network observation from the biological interpretation.

What I Learned

The main concept I learned from hub-gene analysis was how network properties can be used to prioritise genes for further investigation.

The workflow can be summarized as:

Differentially Expressed Genes
            ↓
      Functional Analysis
            ↓
        STRING PPI
            ↓
        Cytoscape
            ↓
    Network Properties
            ↓
      Candidate Hubs
            ↓
 Functional + Literature Evidence
            ↓
    Further Investigation

This helped me understand that bioinformatics analysis does not end with identifying differentially expressed genes. Those genes can be examined at functional, pathway and network levels to generate biologically meaningful hypotheses.

Quick Revision
Hub Gene
↓
Gene whose corresponding protein has high connectivity
within the analysed network.

Main measures:
- Degree
- Betweenness
- Closeness

Degree:
Number of direct connections.

Workflow:
DEGs
 ↓
Filtering
 ↓
STRING
 ↓
PPI Network
 ↓
Cytoscape
 ↓
Centrality Analysis
 ↓
Candidate Hub Genes

Important:
Hub ≠ proven causal gene
Hub ≠ automatically master regulator
High connectivity ≠ overall biological importance
Conclusion

Hub-gene analysis provides a way to identify highly connected nodes within a biological interaction network. In the internship workflow, it formed part of the downstream analysis following differential expression, functional enrichment, STRING interaction analysis and Cytoscape network visualization.

The key idea is:

Differential Expression
        ↓
Functional Analysis
        ↓
PPI Network
        ↓
Network Centrality
        ↓
Candidate Hub Genes
        ↓
Biological Investigation

Hub-gene analysis is therefore best understood as a candidate-prioritisation and network-interpretation step, not as proof of a gene's causal role.
