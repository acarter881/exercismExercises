from functools import reduce
from operator import mul

def largest_product(series, size):
    if size < 0 or size > len(series): raise ValueError('Please input an integer greater than or equal to 0.')

    if size == 0: return 1

    return max([reduce(mul, list(map(int, list(thing)))) for thing in [series[i:i+size] for i in range(0, len(series)) if len(series[i:i+size]) == size]])