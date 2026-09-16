

upregulated.to_csv(
    "upregulated_DEGs.csv",
    index=False
)

downregulated.to_csv(
    "downregulated_DEGs.csv",
    index=False
)


# ---------------------------------------------------------
# 13. Print final summary
# ---------------------------------------------------------

print("\nFiltering completed.")

print(
    f"Total selected DEGs: {len(deg_data)}"
)

print(
    f"Upregulated genes: {len(upregulated)}"
)

print(
    f"Downregulated genes: {len(downregulated)}"
)

print("\nFiles generated:")

print("- selected_DEGs.csv")
print("- upregulated_DEGs.csv")
print("- downregulated_DEGs.csv")
What This Script Does

This script takes the cleaned GEO2R results and applies two basic criteria:

GEO2R Results
      ↓
Adjusted p-value filter
      ↓
log2FC filter
      ↓
Selected DEGs
      ↓
 ┌────┴────┐
 ↓         ↓
Upregulated   Downregulated

The internship workflow specifically involved statistical filtering of differential-expression results before taking selected genes into functional and network analysis.

Filtering Logic

The example criteria are:

Adjusted p-value ≤ 0.05
AND
|log2FC| ≥ 1

This means a gene must satisfy both conditions to enter the final DEG list.

For example:

Gene A
log2FC = +1.8
adjusted p-value = 0.02
→ Selected

Gene B
log2FC = +2.1
adjusted p-value = 0.20
→ Not selected

Gene C
log2FC = +0.4
adjusted p-value = 0.001
→ Not selected

The thresholds above are illustrative. The repository should use the actual thresholds from the GSE43696 analysis if you have them documented. The internship material confirms the use of log2FC, adjusted p-values and statistical filtering, but the cited material does not specify the exact numerical cutoff values.

Upregulated vs Downregulated

The script uses the sign of log2FC to separate the genes:

log2FC ≥ +1
      ↓
Upregulated

and

log2FC ≤ -1
      ↓
Downregulated

The direction depends on which group was defined as the reference/comparison group in the original analysis.

Output Files

The script generates three tables:

selected_DEGs.csv

Contains all genes passing the filtering criteria.

upregulated_DEGs.csv

Contains genes meeting the positive log2FC threshold.

downregulated_DEGs.csv

Contains genes meeting the negative log2FC threshold.

These gene lists can then become inputs for the downstream functional and network analyses documented in the case study. The internship workflow proceeded from selected differential-expression results to GO, KEGG, g:Profiler, STRING and Cytoscape analysis.

Important Reproducibility Note

This script does not create statistical results. It only filters results that already came from a differential-expression analysis.

For the final repository:

Actual GSE43696 GEO2R output
          ↓
Actual statistical values
          ↓
Documented filtering criteria
          ↓
Actual DEG list

should be used wherever possible.

That keeps the repository scientifically honest and separates the actual internship analysis from the simplified Python exercises created to demonstrate the concepts
