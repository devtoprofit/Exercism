"""Function for determine the RNA complement of a given DNA sequence.
"""

def to_rna(dna_strand: str) -> str:
    """Determine the RNA complement of a given DNA sequence.

    Args:
        dna_strand (str): The DNA sequence.

    Returns:
        str: The RNA complement of a given DNA sequence.
    """

    dna = "GCTA"
    rna = "CGAU"

    translation_table = str.maketrans(dna, rna)
    return dna_strand.translate(translation_table)
