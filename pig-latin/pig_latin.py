import re

yRegEx1 = re.compile('([bcdfghjklmnpqrstvwxyz]{2,})y')
yRegEx2 = re.compile('([a-z]{1})y')
vowels = ['a', 'e', 'i', 'o', 'u', 'xr', 'yt']


def translate(text):
    s = []
    for word in text.split():
        if word[0] in vowels or word[0:2] in vowels:
            s.append(word + 'ay')
        elif word[1:3] == 'qu':
            s.append(word[3:] + word[:3] + 'ay')
        elif re.match(yRegEx2, word):
            s.append(word[1] + word[0] + 'ay')
        elif re.match(yRegEx1, word):
            s.append(word[len(re.match(yRegEx1, word).group(1)):] + word[:len(re.match(yRegEx1, word).group(1))] + 'ay')
        elif word[0:2] == 'qu':
            s.append(word[2:] + word[0:2] + 'ay')
        else:
            count = 0
            for letter in word:
                if letter not in vowels:
                    count += 1
                else:
                    break 
            s.append(word[count:] + word[:count] + 'ay')
    return ' '.join(s)


print(translate("queen"))
