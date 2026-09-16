"""
Network Data Processing

Purpose:
    Process protein-protein interaction (PPI) network data
    obtained from a resource such as STRING.

The script demonstrates how to:

    1. Load PPI data
    2. Clean the interaction table
    3. Remove duplicate interactions
    4. Apply an interaction-confidence threshold
    5. Calculate node degree
    6. Identify highly connected candidate hub nodes
    7. Export processed network data

This is a reusable example for learning and portfolio use.
The exact columns may need to be changed depending on the
format of the downloaded STRING/network file.
"""

import pandas as pd


# ---------------------------------------------------------
# 1. Load network data
# ---------------------------------------------------------

input_file = "string_interactions.csv"

network = pd.read_csv(input_file)

print("Network data loaded successfully.")
print(f"Number of interaction rows: {len(network)}")


# ---------------------------------------------------------
# 2. Inspect available columns
# ---------------------------------------------------------

print("\nAvailable columns:")
print(network.columns.tolist())


# ---------------------------------------------------------
# 3. Define column names
# ---------------------------------------------------------
# Change these names if your network file uses different
# column names.

protein_a = "protein_a"
protein_b = "protein_b"
confidence_column = "combined_score"


# ---------------------------------------------------------
# 4. Remove rows with missing protein information
# ---------------------------------------------------------

network = network.dropna(
    subset=[protein_a, protein_b]
)

print(
    "\nRows after removing missing proteins:",
    len(network)
)


# ---------------------------------------------------------
# 5. Convert confidence score to numeric
# ---------------------------------------------------------

if confidence_column in network.columns:

    network[confidence_column] = pd.to_numeric(
        network[confidence_column],
        errors="coerce"
    )

    network = network.dropna(
        subset=[confidence_column]
    )


# ---------------------------------------------------------
# 6. Remove self-interactions
# ---------------------------------------------------------
# A self-interaction occurs when both columns contain the
# same protein.

network = network[
    network[protein_a] != network[protein_b]
].copy()


# ---------------------------------------------------------
# 7. Remove duplicate interactions
# ---------------------------------------------------------
# A-B and B-A represent the same undirected interaction
# in a simple PPI network.

network["protein_1"] = network[
    [protein_a, protein_b]
].min(axis=1)

network["protein_2"] = network[
    [protein_a, protein_b]
].max(axis=1)

network = network.drop_duplicates(
    subset=["protein_1", "protein_2"]
)


# ---------------------------------------------------------
# 8. Apply confidence threshold
# ---------------------------------------------------------

confidence_cutoff = 0.70

if confidence_column in network.columns:

    # STRING scores may be represented on different scales.
    # This example assumes the score has already been
    # converted to a 0–1 scale.

    network = network[
        network[confidence_column]
        >= confidence_cutoff
    ].copy()


# ---------------------------------------------------------
# 9. Create a clean interaction table
# ---------------------------------------------------------

clean_network = network[
    ["protein_1", "protein_2"]
].copy()


if confidence_column in network.columns:

    clean_network[confidence_column] = network[
        confidence_column
    ].values


# ---------------------------------------------------------
# 10. Calculate degree of each protein
# ---------------------------------------------------------

protein_a_counts = clean_network[
    "protein_1"
].value_counts()

protein_b_counts = clean_network[
    "protein_2"
].value_counts()


degree = protein_a_counts.add(
    protein_b_counts,
    fill_value=0
)


degree = degree.astype(int)

degree_table = (
    degree
    .reset_index()
)

degree_table.columns = [
    "Protein",
    "Degree"
]


# ---------------------------------------------------------
# 11. Sort proteins by degree
# ---------------------------------------------------------

degree_table = degree_table.sort_values(
    by="Degree",
    ascending=False
)


# ---------------------------------------------------------
# 12. Display top connected proteins
# ---------------------------------------------------------

print("\nTop connected proteins:")

print(
    degree_table
    .head(10)
    .to_string(index=False)
)


# ---------------------------------------------------------
# 13. Define a hub threshold
# ---------------------------------------------------------
# This is an example threshold. In a real analysis, the
# threshold should be chosen according to the network size
# and analysis method.

hub_degree_cutoff = 10


hub_candidates = degree_table[
    degree_table["Degree"]
    >= hub_degree_cutoff
].copy()


# ---------------------------------------------------------
# 14. Display candidate hubs
# ---------------------------------------------------------

print(
    f"\nCandidate hubs "
    f"(degree >= {hub_degree_cutoff}):"
)

print(
    hub_candidates.to_string(index=False)
)


# ---------------------------------------------------------
# 15. Save the cleaned network
# ---------------------------------------------------------

clean_network.to_csv(
    "processed_PPI_network.csv",
    index=False
)


# ---------------------------------------------------------
# 16. Save degree information
# ---------------------------------------------------------

degree_table.to_csv(
    "protein_degree_table.csv",
    index=False
)


# ---------------------------------------------------------
# 17. Save candidate hub proteins
# ---------------------------------------------------------

hub_candidates.to_csv(
    "candidate_hub_proteins.csv",
    index=False
)


# ---------------------------------------------------------
# 18. Network summary
# ---------------------------------------------------------

number_of_edges = len(clean_network)

number_of_nodes = len(
    set(clean_network["protein_1"])
    |
    set(clean_network["protein_2"])
)


print("\nNetwork summary:")
print(f"Number of nodes: {number_of_nodes}")
print(f"Number of edges: {number_of_edges}")
print(
    f"Number of candidate hubs: "
    f"{len(hub_candidates)}"
)


# ---------------------------------------------------------
# 19. Final output
# ---------------------------------------------------------

print("\nProcessing completed.")

print(
    """
Generated files:

1. processed_PPI_network.csv
2. protein_degree_table.csv
3. candidate_hub_proteins.csv
"""
)
What this code demonstrates

This script takes a basic PPI interaction table and processes it into a form that can be used for network analysis:

STRING Interaction Data
        ↓
Clean Interaction Table
        ↓
Remove Duplicates
        ↓
Confidence Filtering
        ↓
PPI Network
        ↓
Calculate Degree
        ↓
Highly Connected Proteins
        ↓
Candidate Hub Proteins

The central network concept is:

Node → Protein

Edge → Protein association

Degree → Number of connections

This fits directly with the internship workflow in which selected genes from the transcriptomic analysis were taken into STRING and Cytoscape for protein-interaction and network analysis.

Important technical note

The confidence_cutoff = 0.70 in this example is only a configurable example. It should not be presented in your repository as the actual cutoff you used during the internship unless your internship records specifically document that value.

Likewise, hub_degree_cutoff = 10 is an illustrative threshold, not an internship result.

The actual scientific workflow should document the real interaction threshold, network size, and hub-selection method if those values were used in your analysis.
