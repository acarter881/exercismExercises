"""
1. The list must be sorted in order for the binary search to work 
2. The lower and upper bounds need to be updated after each iteration
"""

def find(search_list, value):
    search_list = sorted(search_list)

    lower, upper = 0, len(search_list) - 1

    while lower <= upper:
        middle = (lower + upper) // 2

        if search_list[middle] == value:
            return middle
        
        if search_list[middle] < value:
            lower = middle + 1
        elif search_list[middle] > value:
            upper = middle - 1

    if value not in search_list:
        raise ValueError('Not in there, bud.')