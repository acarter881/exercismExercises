def convert(number):
    finalRes = ''
    if number % 3 == 0:
        finalRes += 'Pling'
    if number % 5 == 0:
        finalRes += 'Plang'
    if number % 7 == 0:
        finalRes += 'Plong'
    if finalRes == '':
        return str(number)
    else:
        return finalRes

