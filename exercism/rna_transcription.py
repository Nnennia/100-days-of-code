x = str.maketrans("GCTA", "CGAU")


def to_rna(dna_strand):
    if not dna_strand or any(y not in "GCTA" for y in dna_strand):
        return ""
    return dna_strand.translate(x)
