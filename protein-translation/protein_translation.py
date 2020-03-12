def proteins(strand):
    dic = {"AUG": "Methionine", "UUU": "Phenylalanine", "UUC": "Phenylalanine",
           "UUA": "Leucine", "UUG": "Leucine", "UCU": "Serine",
           "UCC": "Serine", "UCA": "Serine", "UCG": "Serine",
           "UAU": "Tyrosine", "UAC": "Tyrosine", "UGU": "Cysteine",
           "UGC": "Cysteine", "UGG": "Tryptophan", "UAA": "STOP",
           "UAG": "STOP", "UGA": "STOP"}
    lista = []
    for i in range(0, len(strand), 3):
        trans = strand[i:i+3]
        if dic[trans] == "STOP":
            break
        else:
            lista.append(dic[trans])
    return lista
