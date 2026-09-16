"""
Protein Sequence Analysis
-------------------------
Basic computational analysis of a protein sequence.

This script demonstrates simple operations commonly used in
structural bioinformatics:

1. Cleaning a protein sequence
2. Calculating sequence length
3. Calculating amino-acid composition
4. Calculating molecular weight
5. Calculating approximate hydrophobic residue percentage

The script uses only Python's standard library.
"""


# Standard amino-acid molecular weights in Daltons (Da)
AMINO_ACID_WEIGHTS = {
    "A": 89.09,
    "R": 174.20,
    "N": 132.12,
    "D": 133.10,
    "C": 121.15,
    "E": 147.13,
    "Q": 146.15,
    "G": 75.07,
    "H": 155.16,
    "I": 131.17,
    "L": 131.17,
    "K": 146.19,
    "M": 149.21,
    "F": 165.19,
    "P": 115.13,
    "S": 105.09,
    "T": 119.12,
    "W": 204.23,
    "Y": 181.19,
    "V": 117.15,
}


# Amino acids generally considered hydrophobic
HYDROPHOBIC_RESIDUES = set("AILMFWVY")


def clean_sequence(sequence):
    """
    Remove spaces, line breaks and convert the sequence to uppercase.
    """
    sequence = sequence.replace(" ", "")
    sequence = sequence.replace("\n", "")
    sequence = sequence.upper()

    return sequence


def validate_sequence(sequence):
    """
    Check whether the sequence contains only standard amino acids.
    """
    invalid_residues = [
        residue
        for residue in sequence
        if residue not in AMINO_ACID_WEIGHTS
    ]

    return invalid_residues


def calculate_length(sequence):
    """
    Calculate the number of amino acids.
    """
    return len(sequence)


def amino_acid_composition(sequence):
    """
    Count the occurrence of each amino acid.
    """
    composition = {}

    for amino_acid in AMINO_ACID_WEIGHTS:
        composition[amino_acid] = sequence.count(amino_acid)

    return composition


def calculate_molecular_weight(sequence):
    """
    Estimate the molecular weight of the protein sequence.

    The calculation sums the average residue molecular weights.
    """
    molecular_weight = 0

    for amino_acid in sequence:
        molecular_weight += AMINO_ACID_WEIGHTS[amino_acid]

    return molecular_weight


def calculate_hydrophobic_percentage(sequence):
    """
    Calculate the percentage of hydrophobic amino acids.
    """
    if len(sequence) == 0:
        return 0

    hydrophobic_count = sum(
        1 for amino_acid in sequence
        if amino_acid in HYDROPHOBIC_RESIDUES
    )

    percentage = (hydrophobic_count / len(sequence)) * 100

    return percentage


def display_composition(composition, sequence_length):
    """
    Display amino-acid composition and percentage.
    """
    print("\nAmino-Acid Composition")
    print("-" * 35)

    for amino_acid, count in composition.items():

        if count > 0:
            percentage = (count / sequence_length) * 100

            print(
                f"{amino_acid}: "
                f"{count} residues "
                f"({percentage:.2f}%)"
            )


def main():

    # Example protein sequence.
    # Replace this with the sequence being analysed.
    protein_sequence = """
    MKTIIALSYIFCLVFADYKDDDDK
    """

    # Clean sequence
    sequence = clean_sequence(protein_sequence)

    print("=" * 50)
    print("PROTEIN SEQUENCE ANALYSIS")
    print("=" * 50)

    # Validate sequence
    invalid_residues = validate_sequence(sequence)

    if invalid_residues:

        print("\nInvalid residues detected:")
        print(set(invalid_residues))

        print("\nPlease provide a valid protein sequence.")
        return

    # Sequence length
    length = calculate_length(sequence)

    print("\nProtein Sequence:")
    print(sequence)

    print(f"\nSequence Length: {length} amino acids")

    # Amino-acid composition
    composition = amino_acid_composition(sequence)

    display_composition(composition, length)

    # Molecular weight
    molecular_weight = calculate_molecular_weight(sequence)

    print(
        f"\nApproximate Molecular Weight: "
        f"{molecular_weight:.2f} Da"
    )

    # Hydrophobic percentage
    hydrophobic_percentage = calculate_hydrophobic_percentage(sequence)

    print(
        f"Hydrophobic Residues: "
        f"{hydrophobic_percentage:.2f}%"
    )

    print("\nAnalysis completed.")


if __name__ == "__main__":
    main()
What this script demonstrates
Protein Sequence
       ↓
Sequence Cleaning
       ↓
Sequence Validation
       ↓
Sequence Length
       ↓
Amino-Acid Composition
       ↓
Molecular Weight
       ↓
Hydrophobic Residue Percentage

This is a basic educational sequence-analysis script, intended to demonstrate how Python can be used to process protein sequences before moving toward more advanced structural-bioinformatics analysis.
