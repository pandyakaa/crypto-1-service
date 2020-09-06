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

import numpy as np
from .helper.vigenere_helper import *
from .helper.util import *


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


def extended_vigenere_decrypter(ciphertext, key):
    plaintext = []
    key = generate_vigenere_standard_key(ciphertext, key)
    for i in range(len(ciphertext)):
        decrypted_char = (ord(ciphertext[i]) - ord(key[i]) + 256) % 256
        plaintext.append(chr(decrypted_char))

    return "".join(plaintext)


def playfair_decrypter(ciphertext, key):
    return None


def super_decrypter(ciphertext, key):
    return None


def affine_decrypter(ciphertext, key):
    return None


def hill_decrypter(ciphertext, key):
    res = ""
    ciphertext = ciphertext.replace(" ", "")
    rem = len(ciphertext) % 3
    ciphertext += 'x' * (3-rem)
    key = np.array([[17, 17, 5], [21, 18, 21], [2, 2, 19]])
    key_inversed = np.linalg.inv(key)
    for i in range(0, len(ciphertext) - 3, 3):
        current_string = np.array([getOrder(ciphertext[i]), getOrder(ciphertext[i+1]), getOrder(ciphertext[i+2])])
        dot_result = np.dot(key_inversed, current_string)
        current_result = np.mod(dot_result, 26)
        res += getChar(current_result[0]) + getChar(current_result[1]) + getChar(current_result[2])
    return res


def enigma_decrypter(ciphertext, key):
    return None
