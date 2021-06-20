from string import ascii_lowercase, ascii_uppercase

LOWERCASE_LETTERS = ascii_lowercase
UPPERCASE_LETTERS = ascii_uppercase

def rotate(text, key):
    rotated_string = ''

    for char in text:
        if char in LOWERCASE_LETTERS:
            rotated_string += LOWERCASE_LETTERS[(LOWERCASE_LETTERS.index(char) + key) % len(LOWERCASE_LETTERS)]
        elif char in UPPERCASE_LETTERS:
            rotated_string += UPPERCASE_LETTERS[(UPPERCASE_LETTERS.index(char) + key) % len(UPPERCASE_LETTERS)]
        else:
            rotated_string += char

    return rotated_string

print(rotate('Gur dhvpx oebja sbk whzcf bire gur ynml qbt.', 13))
