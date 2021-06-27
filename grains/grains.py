def square(number):
    if number < 1 or number > 64: raise ValueError('Please enter a number greater than or equal to 1.')
    return 2 ** (number - 1)

def total():
    return sum((2 ** i for i in range(64)))