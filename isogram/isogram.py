def is_isogram(string):
    myDict = {}
    for char in string.lower():
        if char not in ('-', ' '):
            try:
                myDict[char] += 1
            except:
                myDict.setdefault(char, 1)
        else:
            pass
    
    for v in myDict.values():
        if v > 1:
            return False
        else:
            pass
    return True   


print(is_isogram('Alphabet'))
