import re

# Indexes for inner lists in the periodic table
NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1
ATOMIC_NUMBER_INDEX = 2

def make_periodic_table():
    periodic_table_dict = {
        # symbol: [name, atomic_mass, atomic_number]
        "H": ["Hydrogen", 1.008, 1],
        "He": ["Helium", 4.002602, 2],
        "Li": ["Lithium", 6.94, 3],
        "Be": ["Beryllium", 9.0122, 4],
        "B": ["Boron", 10.81, 5],
        "C": ["Carbon", 12.011, 6],
        "N": ["Nitrogen", 14.007, 7],
        "O": ["Oxygen", 15.999, 8],
        "F": ["Fluorine", 18.998, 9],
        "Ne": ["Neon", 20.1797, 10],
        "Na": ["Sodium", 22.98976928, 11],
        "Mg": ["Magnesium", 24.305, 12],
        "Al": ["Aluminum", 26.9815386, 13],
        "Si": ["Silicon", 28.085, 14],
        "P": ["Phosphorus", 30.974, 15],
        "S": ["Sulfur", 32.06, 16],
        "Cl": ["Chlorine", 35.45, 17],
        "Ar": ["Argon", 39.948, 18],
        "K": ["Potassium", 39.0983, 19],
        "Ca": ["Calcium", 40.078, 20],
        # Add more elements as needed
    }
    return periodic_table_dict

def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    """Compute and return the total molar mass of all the elements in symbol_quantity_list."""
    total_molar_mass = 0
    for symbol, quantity in symbol_quantity_list:
        atomic_mass = periodic_table_dict[symbol][ATOMIC_MASS_INDEX]
        total_molar_mass += atomic_mass * quantity
    return total_molar_mass

def sum_protons(symbol_quantity_list, periodic_table_dict):
    """Compute and return the total number of protons in all elements listed in symbol_quantity_list."""
    total_protons = 0
    for symbol, quantity in symbol_quantity_list:
        atomic_number = periodic_table_dict[symbol][ATOMIC_NUMBER_INDEX]
        total_protons += atomic_number * quantity
    return total_protons

def get_formula_name(formula, known_molecules_dict):
    """Try to find the formula in known_molecules_dict. If found, return the name; otherwise, return 'unknown compound'."""
    # Normalize formula by fixing common typos (like "H20" -> "H2O")
    formula = formula.replace("0", "O")  # A simple normalization for common typos
    return known_molecules_dict.get(formula, "unknown compound")

def parse_formula(formula, periodic_table_dict):
    """
    Parse a chemical formula and return a list of tuples (symbol, quantity).
    Example: 'H2O' -> [('H', 2), ('O', 1)]
    """
    # Regex pattern to match element symbols and optional quantity
    pattern = r'([A-Z][a-z]?[a-z]?)(\d*)'
    
    # Find all matches in the formula
    matches = re.findall(pattern, formula)
    
    symbol_quantity_list = []
    
    # Iterate through the matches and process them
    for symbol, quantity in matches:
        if symbol in periodic_table_dict:
            quantity = int(quantity) if quantity else 1  # Default to 1 if no quantity is specified
            symbol_quantity_list.append((symbol, quantity))
        else:
            print(f"Warning: Symbol '{symbol}' not found in the periodic table.")
    
    return symbol_quantity_list

def main():
    # Known chemical formulas and their names
    known_molecules_dict = {
        "H2O": "water",
        "CO2": "carbon dioxide",
        "O2": "oxygen",
        "C6H12O6": "glucose",
        "C2H5OH": "ethanol",
        "C13H16N2O2": "melatonin",
        # Add more known molecules as needed
    }

    # Get a chemical formula for a molecule from the user
    formula = input("Enter a chemical formula: ")

    # Get the mass of a chemical sample in grams from the user
    mass = float(input("Enter the mass of the sample in grams: "))

    # Create the periodic table as a dictionary
    periodic_table = make_periodic_table()

    # Convert the formula into a symbol_quantity_list
    symbol_quantity_list = parse_formula(formula, periodic_table)

    # Compute the molar mass
    molar_mass = compute_molar_mass(symbol_quantity_list, periodic_table)

    # Compute the number of moles in the sample
    number_of_moles = mass / molar_mass

    # Get the name of the formula
    compound_name = get_formula_name(formula, known_molecules_dict)

    # Compute the total number of protons
    total_protons = sum_protons(symbol_quantity_list, periodic_table)

    # Display the results
    print(f"Molar mass of {formula}: {molar_mass:.2f} g/mol")
    print(f"Number of moles: {number_of_moles:.2f}")
    print(f"Compound name: {compound_name}")
    print(f"Total number of protons: {total_protons}")

# Protect the call to main
if __name__ == "__main__":
    main()
