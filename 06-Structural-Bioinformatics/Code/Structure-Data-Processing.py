"""
Structure Data Processing
-------------------------
Basic processing of protein structure data from a PDB file.

This script demonstrates how Python can be used to extract
simple structural information from a PDB-format file:

1. Read ATOM records
2. Count atoms
3. Identify chains
4. Count residues
5. Calculate approximate coordinate ranges
6. Display basic structural statistics

No external packages are required.
"""


def read_pdb_file(filename):
    """
    Read ATOM and HETATM records from a PDB file.
    """
    atoms = []

    with open(filename, "r") as file:

        for line in file:

            if line.startswith(("ATOM", "HETATM")):
                atoms.append(line.rstrip())

    return atoms


def extract_atom_information(atom_lines):
    """
    Extract basic information from PDB atom records.
    """

    atom_data = []

    for line in atom_lines:

        atom_name = line[12:16].strip()
        residue_name = line[17:20].strip()
        chain = line[21].strip()
        residue_number = line[22:26].strip()

        try:
            x = float(line[30:38])
            y = float(line[38:46])
            z = float(line[46:54])

        except ValueError:
            continue

        atom_data.append({
            "atom": atom_name,
            "residue": residue_name,
            "chain": chain,
            "residue_number": residue_number,
            "x": x,
            "y": y,
            "z": z
        })

    return atom_data


def count_chains(atom_data):
    """
    Identify the number of unique chains.
    """

    chains = set()

    for atom in atom_data:

        if atom["chain"]:
            chains.add(atom["chain"])

    return chains


def count_residues(atom_data):
    """
    Count unique residues.

    A residue is identified using its chain and residue number.
    """

    residues = set()

    for atom in atom_data:

        residue_id = (
            atom["chain"],
            atom["residue_number"]
        )

        residues.add(residue_id)

    return residues


def coordinate_range(atom_data):
    """
    Calculate minimum and maximum coordinates
    along the X, Y and Z axes.
    """

    if not atom_data:
        return None

    x_coordinates = [atom["x"] for atom in atom_data]
    y_coordinates = [atom["y"] for atom in atom_data]
    z_coordinates = [atom["z"] for atom in atom_data]

    return {
        "x_min": min(x_coordinates),
        "x_max": max(x_coordinates),
        "y_min": min(y_coordinates),
        "y_max": max(y_coordinates),
        "z_min": min(z_coordinates),
        "z_max": max(z_coordinates)
    }


def residue_composition(atom_data):
    """
    Count how many unique residues of each residue type
    are present in the structure.
    """

    residue_types = {}

    unique_residues = set()

    for atom in atom_data:

        residue_id = (
            atom["chain"],
            atom["residue_number"]
        )

        if residue_id not in unique_residues:

            unique_residues.add(residue_id)

            residue_name = atom["residue"]

            if residue_name not in residue_types:
                residue_types[residue_name] = 0

            residue_types[residue_name] += 1

    return residue_types


def display_results(atom_data):

    print("=" * 50)
    print("PROTEIN STRUCTURE DATA ANALYSIS")
    print("=" * 50)

    # Number of atoms
    print(f"\nTotal atoms: {len(atom_data)}")

    # Chains
    chains = count_chains(atom_data)

    print(f"Number of chains: {len(chains)}")

    if chains:
        print("Chains:", ", ".join(sorted(chains)))

    # Residues
    residues = count_residues(atom_data)

    print(f"Number of residues: {len(residues)}")

    # Coordinate ranges
    coordinates = coordinate_range(atom_data)

    if coordinates:

        print("\nCoordinate Range")
        print("-" * 30)

        print(
            f"X: {coordinates['x_min']:.2f} "
            f"to {coordinates['x_max']:.2f}"
        )

        print(
            f"Y: {coordinates['y_min']:.2f} "
            f"to {coordinates['y_max']:.2f}"
        )

        print(
            f"Z: {coordinates['z_min']:.2f} "
            f"to {coordinates['z_max']:.2f}"
        )

    # Residue composition
    composition = residue_composition(atom_data)

    print("\nResidue Composition")
    print("-" * 30)

    for residue, count in sorted(composition.items()):

        print(f"{residue}: {count}")


def main():

    # Replace this with the name of your PDB file.
    pdb_file = "protein.pdb"

    try:

        atom_lines = read_pdb_file(pdb_file)

        if not atom_lines:

            print("No ATOM or HETATM records were found.")

            return

        atom_data = extract_atom_information(atom_lines)

        if not atom_data:

            print("Unable to extract structural coordinates.")

            return

        display_results(atom_data)

    except FileNotFoundError:

        print(f"File not found: {pdb_file}")
        print("Place the PDB file in the same directory as this script.")


if __name__ == "__main__":
    main()
What this script demonstrates
PDB File
   ↓
Read ATOM / HETATM Records
   ↓
Extract Structural Information
   ↓
├── Atom Count
├── Chain Identification
├── Residue Count
├── Residue Composition
└── Coordinate Range

This provides a simple computational foundation for processing structural data before visualization in PyMOL or further structural analysis.
