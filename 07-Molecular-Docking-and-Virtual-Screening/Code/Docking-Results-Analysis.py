"""
Docking Results Analysis

This script demonstrates a simple way to read and analyze
molecular docking results stored in a CSV file.

Expected CSV columns:
    Ligand, Pose, Affinity

Example:
    Ligand,Pose,Affinity
    Ligand_A,1,-8.4
    Ligand_A,2,-7.9
    Ligand_B,1,-7.8
    Ligand_B,2,-7.2

The script:
    1. Loads docking results
    2. Displays the results
    3. Sorts poses by docking affinity
    4. Identifies the best-scoring pose for each ligand
    5. Prints the overall best-scoring result

Note:
Docking scores are computational predictions and should not
be interpreted as experimental binding affinities.
"""

import csv


def load_docking_results(filename):
    """Load docking results from a CSV file."""

    results = []

    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            results.append({
                "Ligand": row["Ligand"],
                "Pose": int(row["Pose"]),
                "Affinity": float(row["Affinity"])
            })

    return results


def sort_by_affinity(results):
    """
    Sort docking results from most negative to least negative
    predicted affinity score.
    """

    return sorted(results, key=lambda x: x["Affinity"])


def best_pose_for_each_ligand(results):
    """Find the best-scoring pose for every ligand."""

    best_poses = {}

    for result in results:

        ligand = result["Ligand"]

        if ligand not in best_poses:
            best_poses[ligand] = result

        elif result["Affinity"] < best_poses[ligand]["Affinity"]:
            best_poses[ligand] = result

    return best_poses


def display_results(results):
    """Display docking results in a readable format."""

    print("\nDocking Results")
    print("-" * 45)

    for result in results:
        print(
            f"Ligand: {result['Ligand']:<15}"
            f"Pose: {result['Pose']:<5}"
            f"Affinity: {result['Affinity']:.2f} kcal/mol"
        )


def main():

    # Change this to the name of your docking-results file.
    filename = "docking_results.csv"

    try:
        results = load_docking_results(filename)

    except FileNotFoundError:
        print(f"Error: Could not find '{filename}'.")
        print("Make sure the CSV file is in the same folder as this script.")
        return

    if not results:
        print("No docking results were found.")
        return

    # Display original results.
    display_results(results)

    # Sort all poses by predicted affinity.
    sorted_results = sort_by_affinity(results)

    print("\nResults Ranked by Predicted Affinity")
    print("-" * 45)

    for rank, result in enumerate(sorted_results, start=1):
        print(
            f"{rank}. "
            f"{result['Ligand']} | "
            f"Pose {result['Pose']} | "
            f"{result['Affinity']:.2f} kcal/mol"
        )

    # Find the best pose for every ligand.
    best_poses = best_pose_for_each_ligand(results)

    print("\nBest Pose for Each Ligand")
    print("-" * 45)

    for ligand, result in best_poses.items():
        print(
            f"{ligand}: "
            f"Pose {result['Pose']} | "
            f"{result['Affinity']:.2f} kcal/mol"
        )

    # Identify the overall best-scoring result.
    best_result = sorted_results[0]

    print("\nBest-Scoring Result")
    print("-" * 45)

    print(f"Ligand: {best_result['Ligand']}")
    print(f"Pose: {best_result['Pose']}")
    print(f"Predicted affinity: {best_result['Affinity']:.2f} kcal/mol")

    print("\nImportant:")
    print(
        "Docking scores are computational predictions. "
        "A favorable score alone does not establish experimental "
        "binding or biological activity."
    )


if __name__ == "__main__":
    main()
Example Input File

Create a file named:

docking_results.csv

Ligand,Pose,Affinity
Ligand_A,1,-8.4
Ligand_A,2,-7.9
Ligand_A,3,-7.5
Ligand_B,1,-8.1
Ligand_B,2,-7.6
Ligand_C,1,-7.3
Ligand_C,2,-7.0
What This Script Does
CSV Docking Results
        ↓
Read Ligand / Pose / Affinity
        ↓
Sort by Affinity
        ↓
Find Best Pose
        ↓
Compare Ligands
        ↓
Display Results
Key Python Concepts Used
csv.DictReader() → reads CSV data
float() → converts docking scores to numbers
int() → converts pose numbers to integers
sorted() → ranks docking results
lambda → specifies the sorting criterion
Dictionary → stores the best pose for each ligand
Functions → keeps the program organized
Important Interpretation

If the output contains:

Ligand_A → -8.4 kcal/mol
Ligand_B → -8.1 kcal/mol
Ligand_C → -7.3 kcal/mol

the script is only telling us that Ligand A has the most negative predicted score in this particular dataset. It does not prove that Ligand A has the strongest experimental binding or biological activity.

This keeps the code aligned with the docking-analysis principles covered in the repository.
