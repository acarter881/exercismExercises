def classify(number):
    if number <= 0:
        raise ValueError('Please input a number greater than zero.')

    numList = []
    
    for num in range(1, number):
        if number % num == 0:
            numList.append(num)

    total = sum(numList)

    if total == number:
        return 'perfect'
    elif total > number:
        return 'abundant'
    else:
        return 'deficient'
  

print(classify(-1))