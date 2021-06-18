from string import ascii_lowercase

letters = ascii_lowercase # abcdefghijklmnopqrstuvwxyz

def is_pangram(sentence):
    if ''.join(sorted(set([letter for letter in sentence.lower() if letter in ascii_lowercase]))) == letters: return True
    return False