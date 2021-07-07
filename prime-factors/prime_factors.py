def factors(value):
    myFactors = []

    i = 3

    while value != 1:
        if i > value:
            i = 3
        if value % 2 == 0:
            value = int(value / 2)
            myFactors.append(2)
        elif value % i == 0:
            value = int(value / i)
            myFactors.append(i)
            i += 1
        else:
            i += 1
        
    return sorted(myFactors)