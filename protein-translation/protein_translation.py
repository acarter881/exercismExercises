proteinDict = {'Methionine': 'AUG', 
               'Phenylalanine': ['UUU', 'UUC'], 
               'Leucine': ['UUA', 'UUG'],
               'Serine': ['UCU', 'UCC', 'UCA', 'UCG'],
               'Tyrosine': ['UAU', 'UAC'],
               'Cysteine': ['UGU', 'UGC'],
               'Tryptophan': 'UGG',
               'STOP': ['UAA', 'UAG', 'UGA']
               }

def proteins(strand):
    strand = [strand[i:i+3] for i in range(0, len(strand), 3)]

    proteinList = []

    for codon in strand:
        if codon in proteinDict['STOP']:
            return proteinList
        for key in proteinDict.keys():
            if codon in proteinDict[key]:
                proteinList.append(key)

    return proteinList