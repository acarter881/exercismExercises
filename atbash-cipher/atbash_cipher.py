plain = 'abcdefghijklmnopqrstuvwxyz0123456789'
cipher = 'zyxwvutsrqponmlkjihgfedcba0123456789'

def encode(plain_text):
    return ' '.join([''.join([dict(zip(plain, cipher))[character] for character in plain_text.lower() if character not in (' ', '.', ',')])[i:i+5] for i in range(0, len(''.join([dict(zip(plain, cipher))[character] for character in plain_text.lower() if character not in (' ', '.', ',')])), 5)])

def decode(ciphered_text):
    return ''.join([dict(zip(cipher, plain))[character] for character in ciphered_text.lower() if character not in (' ', '.', ',')])