"""
Letter                           Value
A, E, I, O, U, L, N, R, S, T       1
D, G                               2
B, C, M, P                         3
F, H, V, W, Y                      4
K                                  5
J, X                               8
Q, Z                               10
"""

def score(word):
    totalValue = 0
    
    for letter in word.upper():
        if letter in ('A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'):
            totalValue += 1
        elif letter in ('D', 'G'):
            totalValue += 2
        elif letter in ('B', 'C', 'M', 'P'):
            totalValue += 3
        elif letter in ('F', 'H', 'V', 'W', 'Y'):
            totalValue += 4
        elif letter == 'K':
            totalValue += 5
        elif letter in ('J', 'X'):
            totalValue += 8
        elif letter in ('Q', 'Z'):
            totalValue += 10
    return totalValue