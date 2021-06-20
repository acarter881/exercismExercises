def decode(string):
    count = 0
    decodedString = ''

    # TODO turn "12WB12W3B24WB" -> "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
    for i in range(len(string)):
        if string[i].isdigit() and string[i+1].isdigit():
            decodedString += int(string[i] + string[i+1]) * string[i+2]
        elif string[i].isdigit() and (string[i+1].isalpha() or string[i+1] == ' ') and not string[i-1].isdigit():
            decodedString += int(string[i]) * string[i+1]
        elif string[i].isalpha() and string[i-1].isalpha():
            decodedString += string[i]
        elif string[i] == ' ' and not string[i-1].isdigit():
            decodedString += string[i]
        elif i != len(string) - 1:
            if string[i].isalpha() and string[i] != string[i+1] and not string[i-1].isdigit():
                decodedString += string[i]
    return decodedString

def encode(string):
    count = 0
    encodedString = ''

    for i in range(len(string)):
        if i == 0: count += 1
        elif i == len(string) - 1:
            if string[i] == string[i-1]:
                encodedString += str(count+1) + string[i]
            elif string[i] != string[i-1] and count > 1:
                encodedString += str(count) + string[i-1] + string[i]
            else:
                encodedString += string[i-1] + string[i]
        elif string[i] == string[i-1]: count += 1
        elif count == 1 and string[i] != string[i-1]:
            encodedString += string[i-1]
            count = 1
        else:
            encodedString += str(count) + string[i-1]
            count = 1
    return encodedString