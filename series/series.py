# Number of groups = len of series - length + 1 (i.e., '49142' has a len of 5; with a length of 3, we'll be expecting 5 - 3 + 1 = 3 groups)

def slices(series, length):
    if series == '' or length <= 0 or length > len(series): raise ValueError('That ain\'t right!')
    return [series[i:i+length] for i in range(len(series)-length+1)]