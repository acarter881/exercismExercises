def collatz(n):
    if n % 2 == 0:
        return n // 2
    return 3 * n + 1

def steps(number):
    if number < 1:
        raise ValueError('Can\'t use a number less than 1')
    
    iter = 0
    
    while number != 1:
        iter += 1
        if collatz(number) == 1:
            break
        number = collatz(number)

    return iter