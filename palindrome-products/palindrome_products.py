def palindromes(min_factor, max_factor):
    return [(x * y, [x, y]) for x in range(min_factor, max_factor+1)\
                  for y in range(min_factor, max_factor+1)\
                  if str(x * y) == str(x * y)[::-1]
           ]

def largest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError('First argument must be <= second.')

    try:
        x, y = max(palindromes(min_factor, max_factor))
        return x, [b for a, b in palindromes(min_factor, max_factor) if a == x]
    except ValueError:
        return None, []

def smallest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError('First argument must be <= second.')
        
    try:
        x, y = min(palindromes(min_factor, max_factor))
        return x, [b for a, b in palindromes(min_factor, max_factor) if a == x]
    except ValueError:
        return None, []