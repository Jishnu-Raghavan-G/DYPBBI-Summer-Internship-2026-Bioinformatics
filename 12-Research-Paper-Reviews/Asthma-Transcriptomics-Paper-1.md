# Asthma Transcriptomics — Paper 1

## Paper Information

**Title:** Network Study of Nasal Transcriptome Profiles Reveals Master Regulator Genes of Asthma

**Authors:** Anh N. Do, Yoojin Chun, Galina Grishina, Alexander Grishin, Angela J. Rogers, Benjamin A. Raby, Scott T. Weiss, Alfin Vicencio, Eric E. Schadt, and Supinda Bunyavanich

**Journal:** Journal of Allergy and Clinical Immunology

**Year:** 2021

**Volume:** 147

**Issue:** 3

**Pages:** 879–893

**DOI:** 10.1016/j.jaci.2020.07.006

**PMID:** 32828590

**PMCID:** PMC7892642

---

## Research Area

This paper focuses on:

- Asthma
- Nasal transcriptomics
- Gene-expression analysis
- Gene co-expression networks
- Probabilistic causal networks
- Master regulator genes
- Ciliary function
- Inflammatory response

The study investigates whether nasal transcriptomic data can be used to move beyond identifying asthma-associated gene signatures and instead identify genes that may regulate groups of downstream genes involved in asthma-related biological processes. :contentReference[oaicite:1]{index=1}

---

## Background

Asthma is a complex respiratory disease involving multiple biological processes.

Gene-expression studies can identify molecular signatures associated with asthma. However, simply identifying genes that are differentially expressed does not necessarily explain how those genes are connected or which genes may have regulatory influence over larger groups of genes.

The authors therefore focused on identifying **master regulator genes** using network-based and probabilistic causal approaches.

The study also explored nasal transcriptomics as an accessible way of investigating asthma-related biology. :contentReference[oaicite:2]{index=2}

---

## Aim of the Study

The main objective was to identify master regulator genes that could regulate genes associated with asthma phenotypes.

The study specifically investigated:

1. Gene-expression signatures associated with severe persistent asthma.
2. Gene-expression signatures associated with mild/moderate persistent asthma.
3. Co-expression modules containing asthma-associated genes.
4. Master regulator genes within these modules.
5. Whether identified regulators were consistent across different asthma severities and age groups.
6. Whether the findings could be reproduced in independent cohorts. :contentReference[oaicite:3]{index=3}

---

## Study Design

The study used several cohorts.

### ARIA-1

The ARIA-1 cohort included children with severe persistent asthma and controls.

A total of **156 children** were recruited, including:

- 34 children with severe persistent asthma
- 122 children without asthma

Nasal transcriptome profiles were analysed to identify genes associated with severe persistent asthma. :contentReference[oaicite:4]{index=4}

### ATOM

An independent cohort of **190 adults** with mild/moderate asthma and controls was analysed using a similar approach.

This allowed the researchers to investigate whether molecular patterns observed in severe childhood asthma were also present in mild/moderate asthma in adults. :contentReference[oaicite:5]{index=5}

### Validation Cohorts

The findings were subsequently examined in independent cohorts, including:

- **ARIA-test:** 21 children with severe asthma
- **ARIA-2:** 154 children with mild/moderate asthma

These additional cohorts were used to test the consistency of the identified master regulators. :contentReference[oaicite:6]{index=6}

---

## Overall Analytical Workflow

The study followed a network-based transcriptomic analysis workflow:

```text
Nasal Samples
      ↓
Transcriptome Profiling
      ↓
Identify Asthma-Associated Genes
      ↓
Gene Co-Expression Analysis
      ↓
Identify Functional Modules
      ↓
Probabilistic Causal Networks
      ↓
Key Driver Analysis
      ↓
Identify Master Regulators
      ↓
Independent Validation

The study therefore moved from gene-expression signatures toward network-level interpretation.

Nasal Transcriptomics

Nasal transcriptomics was used to investigate gene-expression patterns associated with asthma.

The approach is useful because the nasal epithelium provides an accessible tissue for studying airway-related molecular processes.

The study identified gene signatures associated with both severe persistent asthma and mild/moderate persistent asthma.

Gene Co-Expression Network Analysis

The researchers used weighted gene co-expression network analysis (WGCNA) to investigate relationships between genes.

Instead of considering each gene independently, co-expression analysis groups genes according to their expression relationships across samples.

A simplified representation is:

Gene Expression Data
        ↓
Gene-Gene Expression Relationships
        ↓
Co-Expression Network
        ↓
Functional Modules
        ↓
Biological Interpretation

The asthma-associated genes were found to be enriched in modules related to ciliary function and inflammatory response.

Functional Modules

Two major biological themes identified in the study were:

Ciliary Function

Ciliary function is associated with the activity and organisation of cilia in airway epithelial cells.

The study identified a cilium-related co-expression module enriched for asthma-associated genes.

Inflammatory Response

Another major module was associated with inflammatory responses.

These two biological themes were observed across the studied asthma cohorts.

Probabilistic Causal Networks

After identifying co-expression modules, the researchers constructed probabilistic causal networks.

These networks were used to investigate potential regulatory relationships between genes.

The purpose was to move beyond simple correlation and identify candidate genes that may act as important regulators of downstream genes.

The study used probabilistic causal network construction together with key driver analysis to identify master regulators.

Master Regulator

A master regulator in this study refers to a gene identified through network and probabilistic causal analysis as a potential regulator of downstream genes within an asthma-associated functional module.

The term should therefore be understood in the context of the computational analysis used by the authors.

The study did not simply select the most highly expressed genes. Instead, it used network structure and probabilistic causal analysis to identify candidate regulators.

Key Finding: FOXJ1

One of the most important findings was the identification of FOXJ1 as a master regulator associated with the ciliary function module.

FOXJ1 was identified as a common master regulator across asthma severity and age groups examined in the study.

The authors reported FOXJ1 as a master regulator in:

ARIA-1
ATOM
ARIA-2

This consistency supported its relevance across different asthma groups.

FOXJ1 and Ciliary Function

FOXJ1 is associated with regulation of genes involved in ciliary biology.

The paper discusses its role in regulating genes involved in:

Ciliary basal bodies
Dynein motor components
Apical docking
Cilia motility

The authors also connect FOXJ1 dysregulation with abnormalities in ciliary function and mucociliary clearance based on previous research.

Other Master Regulators

The study also identified additional master regulator genes.

Severe Persistent Asthma in Children

The reported master regulators included:

LRRC23
TMEM231
CAPS
PTPRC
FYB
Mild/Moderate Persistent Asthma

The study identified:

C1orf38
FMNL1

The identification of these genes differed according to cohort, asthma severity, and age group.

High Gene Overlap Between Cohorts

The researchers observed substantial overlap between genes belonging to asthma-associated functional modules across cohorts.

For example, the study reported substantial overlap between ARIA-1 and ATOM in:

Cilium assembly
Inflammatory response
Keratinocyte differentiation

This provided evidence that several molecular patterns were shared between different asthma groups.

Validation

An important part of the study was validation using independent cohorts.

The researchers examined whether master regulators identified in the discovery cohorts were also observed in additional datasets.

The repeated identification of FOXJ1 across the ARIA-1, ATOM, and ARIA-2 cohorts supported its consistency as a candidate master regulator associated with asthma.

Main Results

The major results can be summarised as:

Nasal Transcriptome Data
          ↓
Asthma Gene Signatures
          ↓
Co-Expression Modules
          ↓
Ciliary Function + Inflammatory Response
          ↓
Probabilistic Causal Networks
          ↓
Master Regulators
          ↓
FOXJ1 and Other Candidate Regulators
          ↓
Independent Validation

The study therefore progressed from transcriptomic measurements to network-level biological interpretation.

Biological Significance

The findings suggest that asthma-associated gene-expression changes are not isolated events.

Instead, they can form interconnected networks associated with biological processes such as:

Ciliary function
Inflammatory response
Airway epithelial biology

Identifying regulators within these networks provides potential targets for further mechanistic research.

The authors described the identified master regulators as providing a path toward further investigation of asthma mechanisms and potential therapeutic directions.

Relation to Bioinformatics

This paper demonstrates how multiple bioinformatics approaches can be combined:

Transcriptomics
      ↓
Gene-Expression Analysis
      ↓
Network Analysis
      ↓
Functional Modules
      ↓
Probabilistic Causal Analysis
      ↓
Master Regulator Identification
      ↓
Biological Interpretation

This is particularly relevant to the computational analysis workflow studied during the DYPBBI internship.

Relation to the GSE43696 Case Study

The paper was reviewed alongside the asthma transcriptomics case study based on GSE43696.

The two approaches illustrate different levels of transcriptomic analysis.

GSE43696 Analysis

The internship case study focused on:

GEO Dataset
   ↓
GEO2R
   ↓
Differential Gene Expression
   ↓
GO / KEGG / g:Profiler
   ↓
STRING / Cytoscape
   ↓
Network and Hub-Gene Analysis
Paper 1

The published study used:

Nasal Transcriptomes
   ↓
Asthma-Associated Genes
   ↓
WGCNA
   ↓
Functional Modules
   ↓
Probabilistic Causal Networks
   ↓
Key Driver Analysis
   ↓
Master Regulators

Both demonstrate how gene-expression data can be transformed into biologically interpretable results, although the analytical methods and research objectives are different.

Critical Interpretation

One important point from this paper is the distinction between identifying genes associated with a disease and identifying genes that may regulate broader gene networks.

A simple differential-expression analysis can identify genes whose expression differs between groups.

Network-based approaches can additionally investigate:

Gene-gene relationships
Co-expression modules
Functional organisation
Candidate regulatory relationships
Network-level drivers

This provides a broader perspective on transcriptomic data.

Limitations and Interpretation

The master regulator relationships reported by the study are based on statistical and probabilistic network analysis.

Therefore, the identified regulatory relationships should be interpreted as computationally inferred relationships rather than automatically treating every relationship as experimentally established causation.

Independent validation strengthens the findings, but further mechanistic experiments are still relevant for establishing biological causality.

Key Takeaways
The paper investigated asthma using nasal transcriptomic data.
The researchers studied both severe persistent and mild/moderate asthma.
Gene-expression signatures were identified for different asthma groups.
WGCNA was used to identify gene co-expression modules.
Major modules were associated with ciliary function and inflammatory response.
Probabilistic causal networks and key driver analysis were used to identify candidate master regulators.
FOXJ1 was identified as a common master regulator across several cohorts.
Other identified regulators included LRRC23, TMEM231, CAPS, PTPRC, FYB, C1orf38, and FMNL1.
Independent cohorts were used for validation.
The study demonstrates how transcriptomics can be combined with network analysis to investigate disease mechanisms.
The findings provide a network-level perspective that goes beyond simply identifying individual asthma-associated genes.
Personal Learning from the Paper

This paper helped connect several concepts from the bioinformatics internship:

Transcriptomic analysis
Gene-expression signatures
Co-expression networks
Functional modules
Network analysis
Causal inference
Master regulators
Biological interpretation

The major conceptual takeaway was that transcriptomic research can move from a list of genes toward understanding relationships between genes and biological processes.

Reference

Do AN, Chun Y, Grishina G, Grishin A, Rogers AJ, Raby BA, Weiss ST, Vicencio A, Schadt EE, Bunyavanich S. Network study of nasal transcriptome profiles reveals master regulator genes of asthma. Journal of Allergy and Clinical Immunology. 2021;147(3):879–893.

DOI: 10.1016/j.jaci.2020.07.006

PMID: 32828590

PMCID: PMC7892642

Official article: https://pmc.ncbi.nlm.nih.gov/articles/PMC7892642/
