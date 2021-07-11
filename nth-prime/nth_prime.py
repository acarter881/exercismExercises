def prime(number):
    if number == 0:
        raise ValueError('There is no zeroth prime.')

    count = 0
    y = 1

    while count < number:
        y += 1

        if isPrime(y):
            count += 1

    return y
        
def isPrime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True