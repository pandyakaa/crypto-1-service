'''
Decrypter

1. Standard vigenere cipher
2. Full vigenere cipher
3. Auto-key vigenere cipher
4. Extended vigenere cipher 
5. Playfair cipher
6. Super encrypt = standard vigenere + transpose cipher
7. Affine cipher
8. Hill cipher
9. Enigma cipher
'''

from .helper.vigenere_helper import *


def standard_vigenere_decrypter(ciphertext, key):
    plaintext = []
    key = generate_vigenere_standard_key(ciphertext, key)
    for i in range(len(ciphertext)):
        decrypted_char = (ord(ciphertext[i]) - ord(key[i]) + 26) % 26
        decrypted_char += ord('A')
        plaintext.append(chr(decrypted_char))

    return "".join(plaintext)


def full_vigenere_decrypter(ciphertext, key):
    return None


def auto_key_vigenere_decrypter(ciphertext, key):
    plaintext = []
    for i in range(len(ciphertext)):
        decrypted_char = (ord(ciphertext[i]) - ord(key[i]) + 26) % 26
        decrypted_char += ord('A')
        plaintext.append(chr(decrypted_char))

    return "".join(plaintext)


def extended_vigenere_decrypter(plaintext, key):
    return None


def playfair_decrypter(ciphertext, key):
    return None


def super_decrypter(ciphertext, key):
    return None


def affine_decrypter(ciphertext, key):
    return None


def hill_decrypter(ciphertext, key):
    return None


def enigma_decrypter(ciphertext, key):
    return None
