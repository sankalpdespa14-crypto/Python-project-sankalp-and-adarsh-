# DNA to Protein Translator (Clean + Slightly Advanced)

# mRNA codon table
CODON_TABLE = {
    "AUG": "M",  # Start codon
    "UUU": "F", "UUC": "F",
    "UUA": "L", "UUG": "L",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
    "UAU": "Y", "UAC": "Y",
    "UGU": "C", "UGC": "C",
    "UGG": "W",
    "UAA": "*", "UAG": "*", "UGA": "*"
}

VALID_BASES = {"A", "T", "G", "C"}


def validate_dna(dna):
    """Check if DNA contains only valid bases"""
    dna = dna.upper()
    for base in dna:
        if base not in VALID_BASES:
            return False
    return True


def transcribe_dna(dna):
    """Convert DNA to mRNA"""
    return dna.upper().replace("T", "U")


def reverse_complement(dna):
    """Get reverse complement of DNA"""
    complement = {"A": "T", "T": "A", "G": "C", "C": "G"}
    reversed_seq = dna[::-1]
    new_seq = ""

    for base in reversed_seq:
        new_seq += complement[base]

    return new_seq


def translate_from_position(mrna, start_index):
    """Translate protein starting from a given index"""
    protein = ""

    for i in range(start_index, len(mrna), 3):
        codon = mrna[i:i+3]

        if len(codon) < 3:
            break

        amino = CODON_TABLE.get(codon, "")

        if amino == "*":  # stop codon
            return protein

        if amino:
            protein += amino

    return ""


def find_proteins(mrna):
    """Find all proteins in one mRNA sequence"""
    proteins = []

    for i in range(len(mrna) - 2):
        codon = mrna[i:i+3]

        if codon == "AUG":  # start codon
            protein = translate_from_position(mrna, i)
            if protein:
                proteins.append(protein)

    return proteins


def analyze_dna(dna):
    """Main analysis function"""
    dna = dna.upper()

    if not validate_dna(dna):
        return "Invalid DNA sequence"

    # Forward strand
    mrna = transcribe_dna(dna)
    proteins_forward = find_proteins(mrna)

    # Reverse strand
    rev_dna = reverse_complement(dna)
    rev_mrna = transcribe_dna(rev_dna)
    proteins_reverse = find_proteins(rev_mrna)

    return {
        "DNA": dna,
        "mRNA": mrna,
        "Reverse DNA": rev_dna,
        "Proteins (forward)": proteins_forward,
        "Proteins (reverse)": proteins_reverse
    }


def display_results(results):
    """Print results neatly"""
    if isinstance(results, str):
        print(results)
        return

    print("\n--- Analysis ---")
    print("DNA:", results["DNA"])
    print("mRNA:", results["mRNA"])
    print("Reverse DNA:", results["Reverse DNA"])

    print("\nProteins from forward strand:")
    if results["Proteins (forward)"]:
        for p in results["Proteins (forward)"]:
            print("-", p)
    else:
        print("None found")

    print("\nProteins from reverse strand:")
    if results["Proteins (reverse)"]:
        for p in results["Proteins (reverse)"]:
            print("-", p)
    else:
        print("None found")


def main():
    print("🧬 DNA to Protein Translator\n")

    dna_input = input("Enter DNA sequence: ")
    results = analyze_dna(dna_input)
    display_results(results)


if __name__ == "__main__":
    main()
