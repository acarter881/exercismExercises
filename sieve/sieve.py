def primes(limit):
    composites = []

    for i in range(2, limit + 1):
        if i not in composites:
            tempList = [i for i in range(i, limit + 1, i) if i not in composites]
            composites.extend(tempList[1:])
    
    return [num for num in range(2, limit + 1) if num not in composites]
