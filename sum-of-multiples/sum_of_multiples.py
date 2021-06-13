def sum_of_multiples(limit, multiples):
    total = []
    for num in multiples:
        for i in range(limit):
            res = num * i
            if res < limit and res not in total:
                total.append(res)
    return sum(total)

print(sum_of_multiples(15, [4, 6]))