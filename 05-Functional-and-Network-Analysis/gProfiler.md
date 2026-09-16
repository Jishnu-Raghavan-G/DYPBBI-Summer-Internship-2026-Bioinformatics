# g:Profiler

## Introduction

g:Profiler is a web-based bioinformatics tool used for functional enrichment analysis of a list of genes.

After differential gene-expression analysis, we may have a list of genes that show significant differences between two biological conditions. Looking at these genes individually does not always tell us what biological functions are represented in the dataset.

g:Profiler helps interpret such gene lists by identifying enriched biological functions, pathways, and other functional annotations.

During the internship, g:Profiler was introduced as part of the downstream analysis of differentially expressed genes, along with Gene Ontology (GO), KEGG, STRING, and Cytoscape. :contentReference[oaicite:0]{index=0}

---

## Why Use g:Profiler?

Suppose differential expression analysis gives us:

```text
Gene A
Gene B
Gene C
Gene D
Gene E
Gene F
...

Instead of analysing every gene separately, we can submit the gene list to g:Profiler and ask:

What biological functions or pathways are overrepresented in this gene list?

This provides a higher-level interpretation of the results.

What Can g:Profiler Analyse?

g:Profiler provides several types of functional analysis, including:

Gene Ontology enrichment
Pathway enrichment
Gene-to-gene mappings
Functional annotations
Identifier conversion
Related biological information

The exact results depend on the organism, identifiers, database annotations, and input gene list.

Basic Workflow

A simplified workflow is:

Differential Expression Analysis
            ↓
Identify Significant Genes
            ↓
Prepare Gene List
            ↓
Select Organism
            ↓
Submit Genes to g:Profiler
            ↓
Functional Enrichment Analysis
            ↓
GO / Pathway Results
            ↓
Statistical Filtering
            ↓
Biological Interpretation
Preparing the Gene List

Before using g:Profiler, the gene list should be cleaned and checked.

For example:

Gene1
Gene2
Gene3
Gene4
Gene5

Depending on the dataset and analysis, identifiers may be:

Gene symbols
Ensembl gene IDs
Other supported identifiers

The identifiers should correspond to the correct organism.

For example:

Organism → Homo sapiens

For a human transcriptomics study, selecting the correct organism is important because gene annotations are organism-specific.

Input Gene List

A gene list may come from differential expression analysis.

For example:

Condition A vs Condition B

↓
Differential expression

↓
Adjusted p-value filtering

↓
log2FC filtering

↓
Selected genes

↓
g:Profiler

The selected genes can then be analysed for enriched biological functions and pathways.

Gene Ontology Enrichment

One major use of g:Profiler is Gene Ontology enrichment.

GO has three major categories:

Gene Ontology
│
├── Biological Process
├── Molecular Function
└── Cellular Component
Biological Process

Describes biological processes in which genes are involved.

Examples include:

Immune response
Cell cycle
Signal transduction
Inflammatory processes
Molecular Function

Describes molecular activities performed by gene products.

Examples include:

DNA binding
ATP binding
Enzyme activity
Receptor activity
Cellular Component

Describes where a gene product is located.

Examples include:

Nucleus
Cytoplasm
Plasma membrane
Mitochondrion
Pathway Enrichment

g:Profiler can also help identify biological pathways associated with a gene list.

A simplified interpretation is:

Gene List
   ↓
Pathway Mapping
   ↓
Enrichment Analysis
   ↓
Significant Pathways

This complements Gene Ontology analysis because pathways provide a different way of understanding relationships between genes.

Statistical Analysis

Enrichment analysis involves statistical testing because many possible biological terms and pathways can be examined.

The results may contain measures such as:

P-value
Adjusted significance
Number of genes
Enrichment information

Multiple-testing correction is important because testing a large number of terms increases the possibility of obtaining apparently significant results by chance.

Therefore, interpretation should generally focus on appropriately corrected statistical results rather than raw p-values alone.

Multiple Testing

Consider a simple example.

If:

1000 biological terms

are tested, some terms may appear significant simply because a large number of statistical tests were performed.

To reduce this problem, enrichment tools use multiple-testing correction methods.

A commonly used concept is:

False Discovery Rate (FDR)

The adjusted significance values should therefore be considered when selecting enriched terms.

Interpreting the Results

An enrichment result should not be interpreted as proof that a particular biological process causes the observed condition.

Instead, it indicates that the submitted gene list contains more genes associated with that function or pathway than expected under the statistical model used.

For example:

Input genes
     ↓
Many genes associated with
inflammatory response
     ↓
Inflammatory response becomes
significantly enriched

This provides a biological hypothesis that can be investigated further.

g:Profiler in the Asthma Case Study

The internship included a transcriptomics case study using GSE43696, where gene-expression data were examined using GEO/GEO2R, followed by differential expression analysis and statistical filtering. Selected genes were then taken into downstream functional analyses.

g:Profiler was included as one of the downstream resources alongside GO and KEGG for functional interpretation of the selected gene set.

The overall concept was:

GSE43696
   ↓
GEO2R
   ↓
Healthy vs Asthma
   ↓
Differentially Expressed Genes
   ↓
Statistical Filtering
   ↓
Selected Gene List
   ↓
g:Profiler
   ↓
GO / Pathway Enrichment
   ↓
Biological Interpretation
g:Profiler and KEGG

g:Profiler and KEGG should not be considered competing tools.

They can be used together.

g:Profiler
    ↓
Functional enrichment
    ↓
GO + pathway-related information

KEGG
    ↓
Pathway database
    ↓
Detailed pathway interpretation

g:Profiler provides a convenient enrichment-analysis interface, while KEGG provides pathway information that can be used to understand molecular relationships within pathways.

g:Profiler and STRING

These tools answer different questions.

g:Profiler

Main question:

What functions or pathways are enriched in my gene list?

STRING

Main question:

How are the proteins encoded by these genes functionally connected?

Therefore:

Gene List
   │
   ├──→ g:Profiler
   │       ↓
   │   Functions / Pathways
   │
   └──→ STRING
           ↓
       Protein Interactions

During the internship, functional enrichment was followed by protein-protein interaction and network analysis using STRING and Cytoscape.

From Enrichment to Network Analysis

Functional enrichment and network analysis can be connected into a larger workflow:

Differentially Expressed Genes
             ↓
       Functional Analysis
             ↓
      GO / KEGG / g:Profiler
             ↓
      Biological Functions
             ↓
         STRING PPI
             ↓
        Cytoscape Network
             ↓
       Hub-Gene Analysis

This provides several levels of interpretation:

Gene
 ↓
Function
 ↓
Pathway
 ↓
Interaction
 ↓
Network

The internship workflow incorporated these stages as part of the broader transcriptomics and network-analysis component.

Important Things to Check

Before interpreting a g:Profiler result, check:

1. Organism

Make sure the correct organism has been selected.

2. Gene identifiers

Check whether the submitted identifiers are valid and correctly mapped.

3. Number of input genes

Very small gene lists may produce unstable or limited enrichment results.

4. Statistical significance

Look at corrected significance values rather than relying only on raw p-values.

5. Biological relevance

A statistically enriched term should still make biological sense in the context of the experiment.

6. Background

The reference/background gene set can affect enrichment results.

Common Mistakes
Mistake 1: Using the wrong organism

Human genes should not be analysed using an unrelated organism's annotations.

Mistake 2: Submitting unfiltered data without understanding the input

The meaning of the enrichment depends strongly on how the gene list was generated.

Mistake 3: Looking only at p-values

Multiple-testing correction should be considered.

Mistake 4: Treating enrichment as proof

Enrichment indicates statistical association, not experimental causation.

Mistake 5: Ignoring gene direction

If the analysis contains both upregulated and downregulated genes, combining them into one list can sometimes hide important differences.

Separate analyses may be useful when scientifically appropriate.

Example Interpretation

Suppose a filtered gene list contains 50 genes.

g:Profiler reports:

Biological Process:
Inflammatory response

Number of genes:
12

Adjusted significance:
Significant

A reasonable interpretation would be:

The analysed gene list is enriched for genes annotated to inflammatory-response-related biological processes.

It would not be appropriate to conclude from enrichment alone that inflammation is definitively causing the observed disease phenotype.

Further evidence from expression patterns, literature, experiments, and network/pathway analysis would be required.

Advantages

g:Profiler is useful because it:

Accepts gene lists for functional interpretation
Provides enrichment analysis
Supports Gene Ontology analysis
Provides pathway-related information
Helps connect genes with biological functions
Reduces the need to inspect every gene individually
Can support downstream biological interpretation
Limitations

Like other enrichment tools, g:Profiler depends on the quality and completeness of biological annotations.

Important limitations include:

Not every gene is equally well annotated
Results depend on the input gene list
Results depend on organism selection
Multiple-testing correction is necessary
Enrichment does not establish causality
Different databases can produce different results
Biological interpretation still requires domain knowledge
What I Learned

Through this part of the internship, I learned how a list of genes obtained from differential expression analysis can be converted into a more meaningful biological interpretation.

The main idea was:

Differentially Expressed Genes
            ↓
       Gene List
            ↓
       g:Profiler
            ↓
 Functional Enrichment
            ↓
 GO / Pathway Information
            ↓
 Biological Interpretation

This was particularly useful in understanding how transcriptomics can move beyond simply identifying differentially expressed genes and towards understanding the biological processes and pathways represented by those genes.

Quick Revision
g:Profiler
↓
Functional enrichment tool

Input:
Gene list

Main uses:
- GO enrichment
- Pathway-related analysis
- Functional interpretation
- Gene identifier-related analysis

Important:
- Select correct organism
- Check gene identifiers
- Consider adjusted p-values
- Consider background genes
- Interpret results biologically

Basic question:
"What functions and pathways are enriched in my gene list?"

Workflow:
DEGs
 ↓
Filtering
 ↓
Gene List
 ↓
g:Profiler
 ↓
Enrichment
 ↓
GO / Pathways
 ↓
Interpretation
Conclusion

g:Profiler provides a practical way to interpret gene lists obtained from transcriptomic and other genomic analyses. Instead of examining genes independently, it helps identify groups of genes associated with common biological functions and pathways.

In the internship workflow, g:Profiler formed part of the functional-analysis stage following differential gene-expression analysis of the asthma-related GSE43696 dataset. Its results could then be considered together with GO, KEGG, STRING, Cytoscape, and hub-gene analysis to build a broader biological interpretation.
