def to_rna(dna_strand):
    return ''.join([{'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}[letter] for letter in dna_strand])

print(to_rna('GTTTTTTTTATATCGTGCCTAACG'))