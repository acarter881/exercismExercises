def triplets_with_sum(number):
    tripList = []

    for i in range(1, int(number / 2)):
        for j in range(i + 1, int(number / 2)):
            for k in range(j + 1, int(number / 2)):
                if (i ** 2 + j ** 2) == (k ** 2) and i + j + k == number:
                    tripList.extend([[i,j,k]])
    
    return tripList