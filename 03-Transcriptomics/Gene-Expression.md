# Gene Expression

## Introduction

Gene expression is the process through which information stored in a gene is used to produce a functional product, usually an RNA molecule and, for protein-coding genes, a protein.

In bioinformatics, gene expression is important because the expression level of a gene can change depending on:

- Cell type
- Tissue
- Developmental stage
- Environmental conditions
- Disease state
- Treatment
- Other biological factors

Studying these changes helps researchers understand how biological systems respond to different conditions.

During the internship, gene expression was studied as an important part of transcriptomics, particularly through analysis of publicly available GEO datasets and GEO2R. :contentReference[oaicite:0]{index=0}

## From Gene to Expression

A simplified view of gene expression is:

```text
DNA
 ↓
Transcription
 ↓
RNA
 ↓
Translation
 ↓
Protein

For protein-coding genes, the RNA produced during transcription can serve as the template for protein production.

However, not every RNA molecule is translated into a protein. Many RNA molecules perform regulatory or structural functions.

Therefore, measuring RNA abundance provides useful information about which genes are active and to what extent.

What Does "Gene Expression Level" Mean?

The expression level of a gene represents the amount of its transcript detected in a particular biological sample.

For example:

Gene	Healthy Sample	Disease Sample
Gene A	100	250
Gene B	500	480
Gene C	50	10

In this simplified example:

Gene A has higher expression in the disease sample.
Gene B shows relatively little change.
Gene C has lower expression in the disease sample.

The actual numerical values depend on the experimental technology and preprocessing method.

Gene Expression Is Not Simply "On" or "Off"

Gene expression is often treated as a continuous measurement rather than a simple on/off switch.

A gene can have:

Very low expression
Moderate expression
High expression

The expression level can also change between biological conditions.

For example:

Low expression
      ↓
Moderate expression
      ↓
High expression

This variation is one of the reasons transcriptomic data can contain large amounts of biological information.

Gene Expression Across Conditions

One of the most common applications of gene-expression analysis is comparing two biological conditions.

For example:

Healthy
  ↓
Gene Expression Profile
  ↓
       COMPARISON
  ↓
Disease
  ↓
Gene Expression Profile

The objective is to identify genes that show meaningful differences between the groups.

In the internship, this concept was applied to an asthma-related GEO dataset, where healthy and asthma samples were compared using GEO2R.

Expression Matrix

When many genes are measured across multiple samples, the results can be represented as an expression matrix.

Example:

Gene	Healthy 1	Healthy 2	Healthy 3	Asthma 1	Asthma 2
Gene A	5.1	5.3	5.0	7.8	8.1
Gene B	6.4	6.2	6.5	6.1	6.3
Gene C	3.0	3.2	3.1	5.7	5.5

Here:

Each row represents a gene.
Each column represents a biological sample.
Each value represents an expression measurement.

This type of matrix forms the basis for many transcriptomic analyses.

Biological Replicates

Multiple biological samples are generally required to understand biological variation.

For example:

Healthy Group
 ├── Healthy 1
 ├── Healthy 2
 └── Healthy 3

Asthma Group
 ├── Asthma 1
 ├── Asthma 2
 └── Asthma 3

Comparing groups rather than relying on a single sample helps statistical analysis account for variation between biological samples.

Gene Expression and Disease

Changes in gene expression can provide information about biological processes associated with disease.

A simplified disease-analysis workflow is:

Disease Samples
      ↓
Gene Expression Data
      ↓
Differential Expression
      ↓
Genes of Interest
      ↓
Functional Analysis
      ↓
Pathways and Networks
      ↓
Biological Interpretation

This was an important concept in the internship because the asthma analysis did not stop at identifying genes. The selected genes were subsequently taken forward for functional and network analysis.

Differential Gene Expression

Differential gene expression analysis compares gene-expression measurements between defined groups.

For example:

Healthy Expression
        VS
Disease Expression
        ↓
Statistical Analysis
        ↓
Differentially Expressed Genes

A gene may be described as:

Upregulated
Downregulated
Not significantly changed

These descriptions depend on the direction of the comparison and the statistical criteria used.

Upregulated and Downregulated Genes
Upregulated

A gene is described as upregulated when its expression is higher in the condition being compared against the reference condition.

Reference: 100
Condition: 300

Expression increased
→ Upregulated
Downregulated

A gene is described as downregulated when its expression is lower in the condition being compared against the reference condition.

Reference: 300
Condition: 100

Expression decreased
→ Downregulated

The exact interpretation depends on how the comparison groups were defined.

Fold Change

Fold change is commonly used to describe the magnitude of an expression difference.

For example:

Healthy = 100
Asthma  = 200

Fold Change = 200 / 100
            = 2

This represents a two-fold increase.

For a decrease:

Healthy = 200
Asthma  = 100

Fold Change = 100 / 200
            = 0.5

A fold change of 0.5 represents a two-fold decrease relative to the reference.

Log2 Fold Change

Transcriptomic analysis commonly uses log2 fold change.

log2FC = log2(Fold Change)

Examples:

Fold Change	log2FC	Interpretation
0.25	-2	Decreased
0.5	-1	Decreased
1	0	No fold-change
2	+1	Increased
4	+2	Increased

The sign indicates the direction of change, while the magnitude indicates the size of the change.

P-Value and Adjusted P-Value

Gene-expression experiments can involve thousands of genes.

If each gene is tested individually, many statistical tests are performed. This creates a multiple-testing problem.

Therefore, adjusted p-values are commonly used to reduce the chance of interpreting random findings as significant.

A simplified workflow is:

Gene Expression Data
       ↓
Statistical Testing
       ↓
P-values
       ↓
Multiple-testing Correction
       ↓
Adjusted P-values
       ↓
Gene Filtering

The internship specifically included adjusted p-values and statistical filtering as part of differential gene-expression analysis.

Statistical Significance vs Biological Importance

A statistically significant gene is not automatically biologically important.

For example:

Gene A
Very small expression change
+
Strong statistical significance

and

Gene B
Large expression change
+
Less statistical evidence

can represent different situations.

Therefore, gene-expression results should be interpreted using multiple factors, including:

Effect size
Statistical significance
Biological context
Experimental design
Sample size
Existing biological knowledge

This is particularly important when moving from computational results to biological interpretation.

Heatmaps

A heatmap provides a visual representation of gene-expression patterns across samples.

A simplified representation is:

             Sample 1   Sample 2   Sample 3
Gene A          ██         ███        ████
Gene B          ████       ████       ███
Gene C          █          ██         █
Gene D          ███        █          ██

In an actual heatmap, colors represent relative expression levels.

Heatmaps can help identify:

Similar expression patterns
Differences between groups
Clusters of genes
Similarity between samples
Volcano Plots

A volcano plot is commonly used to visualize differential-expression results.

It combines:

Magnitude of expression change
Statistical significance

A simplified representation is:

              Statistical significance
                       ↑
                       |
         *             |             *
       *               |               *
     *                 |                 *
-----------------------+----------------------→ log2FC
      Downregulated    |     Upregulated

Genes with large absolute log2 fold changes and strong statistical significance may appear farther toward the sides and upper region of the plot.

The exact appearance depends on the dataset and plotting method.

Gene Expression and GEO

The Gene Expression Omnibus (GEO) is a major public repository containing gene-expression and other functional genomics datasets.

Researchers can use publicly available datasets to investigate biological questions without generating an entirely new experimental dataset.

During the internship, GEO was used to access publicly available gene-expression data, and GEO2R was used for comparative analysis.

GEO2R and Gene Expression

GEO2R provides an interface for comparing groups of samples within suitable GEO datasets.

A simplified workflow is:

GEO
 ↓
Select Dataset
 ↓
Identify Sample Groups
 ↓
GEO2R
 ↓
Statistical Comparison
 ↓
Gene Expression Results
 ↓
Differentially Expressed Genes

For the internship case study:

GSE43696
   ↓
GEO
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

The internship documentation identifies GSE43696 as the asthma transcriptomics dataset used in the analysis.

From Genes to Biological Meaning

A list of differentially expressed genes is only the beginning of the analysis.

The next step is to understand what those genes are involved in.

For example:

Differentially Expressed Genes
              ↓
       Gene Ontology
              ↓
       KEGG Pathways
              ↓
       g:Profiler
              ↓
      PPI Network Analysis
              ↓
          Cytoscape
              ↓
      Hub-Gene Analysis

During the internship, Gene Ontology was used to examine biological processes, molecular functions, and cellular components, while KEGG and g:Profiler were used for pathway and enrichment interpretation. STRING and Cytoscape were then used for interaction-network analysis.

Gene Expression Signatures

A group of genes can sometimes show a characteristic expression pattern associated with a biological condition.

Such patterns can be described as gene-expression signatures.

A simplified idea is:

Gene A ↑
Gene B ↑
Gene C ↓
Gene D ↑
Gene E ↓
      ↓
Expression Pattern
      ↓
Biological Signature

During the internship, research-paper discussions related to asthma transcriptomics included topics such as gene-expression signatures, master regulator genes, hub genes, molecular classification, disease-associated pathways, and precision medicine.

Important Factors Affecting Gene Expression Data

Gene-expression measurements can be influenced by both biological and technical factors.

Examples include:

Biological Factors
Tissue type
Cell type
Disease state
Age
Sex
Treatment
Environmental conditions
Biological variation
Technical Factors
Sample preparation
RNA quality
Experimental platform
Batch effects
Measurement technology
Data preprocessing

Therefore, transcriptomic analysis requires careful interpretation rather than simply selecting genes with large numerical differences.

Gene Expression Analysis in the Internship

Gene expression formed one of the central components of the internship.

The documented training included:

Transcriptomics
RNA sequencing
Microarray technology
Gene-expression datasets
Disease vs healthy comparisons
Differential gene expression
Log2 fold change
Adjusted p-values
Statistical filtering
Interpretation of gene-expression results

The practical asthma case study used GSE43696 and GEO2R to compare healthy and asthma samples, followed by differential-expression analysis and statistical filtering.

Common Terms
Term	Meaning
Gene expression	Production or abundance of a gene's RNA product
Transcript	RNA molecule produced from a gene
Expression level	Measured abundance of a transcript
Expression matrix	Table containing expression measurements across genes and samples
Upregulated	Higher expression relative to the reference condition
Downregulated	Lower expression relative to the reference condition
Fold change	Ratio describing the change between conditions
log2FC	Log2-transformed fold change
P-value	Statistical measure used to assess evidence against a null hypothesis
Adjusted p-value	P-value corrected for multiple testing
DEG	Differentially expressed gene
GEO	Gene Expression Omnibus
GEO2R	Tool/interface for comparative analysis of GEO expression datasets
Heatmap	Visualization of expression patterns
Volcano plot	Visualization combining expression change and statistical significance
Key Takeaways
Gene expression describes how information from genes is represented through their RNA products and, for protein-coding genes, proteins.
Expression levels can vary between tissues, individuals, conditions, and disease states.
An expression matrix organizes measurements from many genes across multiple samples.
Differential gene-expression analysis compares expression between defined biological groups.
Fold change and log2FC describe the magnitude and direction of expression changes.
Adjusted p-values are important when many genes are tested simultaneously.
Heatmaps help visualize expression patterns across genes and samples.
Volcano plots combine information about expression change and statistical significance.
GEO provides publicly available gene-expression datasets.
GEO2R can be used to compare sample groups in suitable GEO datasets.
In the internship's asthma case study, GSE43696 was analyzed using GEO2R to compare healthy and asthma samples.
Differentially expressed genes can be taken forward into GO, KEGG, g:Profiler, STRING, Cytoscape, and hub-gene analysis.
Computational gene-expression results need biological interpretation and should not be treated as conclusions solely because a software tool reports them as significant.
Summary

Gene-expression analysis provides a way to investigate how biological conditions are associated with changes in transcript abundance. By comparing expression profiles between groups, researchers can identify genes of interest and investigate their biological roles.

The internship connected these concepts to a practical asthma transcriptomics workflow. A GEO dataset, GSE43696, was explored using GEO2R, healthy and asthma samples were compared, and genes were selected through differential-expression and statistical filtering. These genes were subsequently used for functional and network-based analysis.

This demonstrated an important principle of bioinformatics: gene-expression analysis is not just about finding differentially expressed genes; the larger goal is to understand what those changes may mean biologically.
