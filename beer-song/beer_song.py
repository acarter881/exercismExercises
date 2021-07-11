def recite(start, take=1):
    beerList = []

    bottles = start

    for i in range(take):
        if bottles > 2:
            beerList.append(f'{start-i} bottles of beer on the wall, {start-i} bottles of beer.')
            beerList.append(f'Take one down and pass it around, {start-i-1} bottles of beer on the wall.')
            beerList.append('')
            bottles -= 1
        elif bottles == 2:
            beerList.append(f'{start-i} bottles of beer on the wall, {start-i} bottles of beer.')
            beerList.append(f'Take one down and pass it around, {start-i-1} bottle of beer on the wall.')
            beerList.append('')
            bottles -= 1
        elif bottles == 1:
            beerList.append('1 bottle of beer on the wall, 1 bottle of beer.')
            beerList.append('Take it down and pass it around, no more bottles of beer on the wall.')
            beerList.append('')
            bottles -= 1
        elif bottles == 0:
            beerList.append('No more bottles of beer on the wall, no more bottles of beer.')
            beerList.append('Go to the store and buy some more, 99 bottles of beer on the wall.')
            beerList.append('')
          
    return beerList[:-1]