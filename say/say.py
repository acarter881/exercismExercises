by_one = (
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
    'ten',
    'eleven',
    'twelve',
    'thirteen',
    'fourteen',
    'fifteen',
    'sixteen',
    'seventeen',
    'eighteen',
    'nineteen'
)

by_ten = (
    'zero',
    'ten',
    'twenty',
    'thirty',
    'forty',
    'fifty',
    'sixty',
    'seventy',
    'eighty',
    'ninety'    
)

def say(number):
    if number not in range(0, 1000000000000): raise ValueError('This number is not in range.')

    if number < 20:
        return by_one[number]
    elif number < 100:
        ten = int(number / 10)
        remainder = number % 10
        return by_ten[ten] + ('-' + say(remainder) if remainder > 0 else '')
    elif number < 1000:
        hundred = int(number / 100)
        remainder = number % 100
        return by_one[hundred] + ' hundred' + (' ' + say(remainder) if remainder > 0 else '') 
    elif number < 1000000:
        thousand = int(number / 1000)
        remainder = number % 1000
        return say(thousand) + ' thousand' + (' ' + say(remainder) if remainder > 0 else '') 
    elif number < 1000000000:
        million = int(number / 1e6)
        remainder = int(number % 1e6)
        return say(million) + ' million' + (' ' + say(remainder) if remainder > 0 else '')
    else:
        billion = int(number / 1e9)
        remainder = int(number % 1e9)
        return say(billion) + ' billion' + (' ' + say(remainder) if remainder > 0 else '')