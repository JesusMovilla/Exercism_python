def to_rna(dna_strand):
    changes = {'A': 'U', 'T': 'A', 'C': 'G', 'G': 'C'}
    rna = ''
    for dna in dna_strand:
        rna += changes[dna]
    return rna
