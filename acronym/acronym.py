import re

acroRegEx = re.compile("([A-Za-z])[A-Za-z']*")

def abbreviate(words):
    return ''.join(re.findall(acroRegEx, words)).upper()

print(abbreviate('Complementary metal-oxide semiconductor'))