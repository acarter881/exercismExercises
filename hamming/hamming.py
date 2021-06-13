def distance(strand_a, strand_b):
    if len(strand_a) == len(strand_b):
        hammingCount = 0
        for i in range(len(strand_a)):
            if strand_a[i] == strand_b[i]:
                pass
            else:
                hammingCount += 1
        return hammingCount
    else:
        raise ValueError('We can\'t compare DNA strands of different lengths.')


print(distance('GAGCCTACTAACGGGAfffT', 'CATCGTAATGACGGCCT'))
