"""
Ligand Data Processing

This script demonstrates basic processing of ligand information
stored in a CSV file.

Expected CSV columns:
    Ligand, Molecular_Weight, LogP, HBD, HBA

Example:
    Ligand,Molecular_Weight,LogP,HBD,HBA
    Ligand_A,320.5,2.4,2,5
    Ligand_B,410.2,3.1,1,6
    Ligand_C,285.7,1.8,3,4

The script:
    1. Loads ligand data
    2. Displays the compounds
    3. Calculates simple summary statistics
    4. Filters compounds using user-defined criteria
    5. Saves the filtered compounds to a new CSV file

Note:
The filters used here are examples for learning purposes.
They should not be treated as universal drug-design rules.
"""

import csv


def load_ligand_data(filename):
    """Load ligand information from a CSV file."""

    ligands = []

    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            ligands.append({
                "Ligand": row["Ligand"],
                "Molecular_Weight": float(row["Molecular_Weight"]),
                "LogP": float(row["LogP"]),
                "HBD": int(row["HBD"]),
                "HBA": int(row["HBA"])
            })

    return ligands


def display_ligands(ligands):
    """Display ligand information."""

    print("\nLigand Data")
    print("-" * 65)

    for ligand in ligands:
        print(
            f"{ligand['Ligand']:<15}"
            f"MW: {ligand['Molecular_Weight']:<8.2f}"
            f"LogP: {ligand['LogP']:<6.2f}"
            f"HBD: {ligand['HBD']:<4}"
            f"HBA: {ligand['HBA']}"
        )


def calculate_averages(ligands):
    """Calculate average molecular properties."""

    if not ligands:
        return

    average_mw = sum(
        ligand["Molecular_Weight"] for ligand in ligands
    ) / len(ligands)

    average_logp = sum(
        ligand["LogP"] for ligand in ligands
    ) / len(ligands)

    average_hbd = sum(
        ligand["HBD"] for ligand in ligands
    ) / len(ligands)

    average_hba = sum(
        ligand["HBA"] for ligand in ligands
    ) / len(ligands)

    print("\nAverage Properties")
    print("-" * 40)
    print(f"Average molecular weight: {average_mw:.2f}")
    print(f"Average LogP: {average_logp:.2f}")
    print(f"Average H-bond donors: {average_hbd:.2f}")
    print(f"Average H-bond acceptors: {average_hba:.2f}")


def filter_ligands(
    ligands,
    max_molecular_weight=500,
    max_logp=5,
    max_hbd=5,
    max_hba=10
):
    """
    Filter ligands using simple molecular-property limits.

    These thresholds are examples for computational filtering.
    """

    filtered = []

    for ligand in ligands:

        if ligand["Molecular_Weight"] > max_molecular_weight:
            continue

        if ligand["LogP"] > max_logp:
            continue

        if ligand["HBD"] > max_hbd:
            continue

        if ligand["HBA"] > max_hba:
            continue

        filtered.append(ligand)

    return filtered


def save_ligands(ligands, filename):
    """Save processed ligand data to a CSV file."""

    fieldnames = [
        "Ligand",
        "Molecular_Weight",
        "LogP",
        "HBD",
        "HBA"
    ]

    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        for ligand in ligands:
            writer.writerow(ligand)


def main():

    input_file = "ligands.csv"
    output_file = "filtered_ligands.csv"

    try:
        ligands = load_ligand_data(input_file)

    except FileNotFoundError:
        print(f"Error: Could not find '{input_file}'.")
        print("Make sure the CSV file is in the same folder.")
        return

    if not ligands:
        print("No ligand data found.")
        return

    # Display original dataset.
    display_ligands(ligands)

    # Calculate basic statistics.
    calculate_averages(ligands)

    # Apply simple property filters.
    filtered_ligands = filter_ligands(ligands)

    print("\nFiltered Ligands")
    print("-" * 40)

    for ligand in filtered_ligands:
        print(
            f"{ligand['Ligand']} | "
            f"MW = {ligand['Molecular_Weight']:.2f} | "
            f"LogP = {ligand['LogP']:.2f}"
        )

    # Save the filtered dataset.
    save_ligands(filtered_ligands, output_file)

    print(f"\nFiltered data saved to: {output_file}")
    print(
        f"Original compounds: {len(ligands)}"
    )
    print(
        f"Compounds after filtering: {len(filtered_ligands)}"
    )


if __name__ == "__main__":
    main()
Example Input

Create:

ligands.csv

Ligand,Molecular_Weight,LogP,HBD,HBA
Ligand_A,320.5,2.4,2,5
Ligand_B,410.2,3.1,1,6
Ligand_C,285.7,1.8,3,4
Ligand_D,620.4,4.2,2,8
Ligand_E,350.8,6.2,1,5

The script will process the molecular-property information and remove compounds that exceed the example filtering limits.

Workflow
Ligand CSV
    ↓
Read Molecular Properties
    ↓
Calculate Summary Statistics
    ↓
Apply Filters
    ↓
Generate Reduced Ligand Set
    ↓
Save Filtered CSV
    ↓
Potential Downstream Docking
Key Concepts
Property	Meaning
Molecular weight	Mass of the molecule
LogP	Measure related to lipophilicity
HBD	Hydrogen-bond donors
HBA	Hydrogen-bond acceptors
Filtering	Removing compounds outside selected criteria
Ligand library	Collection of compounds for analysis
Important Note

The filtering thresholds in this educational script are example computational criteria. Real compound selection depends on the research objective and may involve substantially more properties, including solubility, permeability, ionization, chemical stability, toxicity, and experimentally determined activity.

This script is therefore intended to demonstrate basic ligand-data handling and preprocessing before computational analysis, rather than provide a complete drug-screening pipeline.
