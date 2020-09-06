'''
Encrypter

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
from .helper.handle_capital import letter_base_number, standardize_key
from .helper.util import *


def standard_vigenere_encrypter(plaintext, key):
    ciphertext = []
    key = generate_vigenere_standard_key(plaintext, key)
    plaintext = plaintext.replace(" ", "").strip()
    for i in range(len(plaintext)):
        key_letter = standardize_key(plaintext[i], key[i])
        base_number = letter_base_number(plaintext[i])
        encrypted_char = (ord(plaintext[i]) + ord(key_letter)) % 26
        encrypted_char += base_number
        ciphertext.append(chr(encrypted_char))

    return "".join(ciphertext)


def full_vigenere_encrypter(plaintext, key):
    return None


def auto_key_vigenere_encrypter(plaintext, key):
    ciphertext = []
    key = generate_vigenere_full_key(plaintext, key)
    for i in range(len(plaintext)):
        key_letter = standardize_key(plaintext[i], key[i])
        base_number = letter_base_number(plaintext[i])
        encrypted_char = (ord(plaintext[i]) + ord(key_letter)) % 26
        encrypted_char += base_number
        ciphertext.append(chr(encrypted_char))

    return "".join(ciphertext)


def extended_vigenere_encrypter(plaintext, key):
    ciphertext = []
    key = generate_vigenere_standard_key(plaintext, key)
    plaintext = plaintext.replace(" ", "").strip()
    for i in range(len(plaintext)):
        encrypted_char = (ord(plaintext[i]) + ord(key[i])) % 256
        ciphertext.append(chr(encrypted_char))

    return "".join(ciphertext)


def playfair_encrypter(plaintext, key):
    return None


def super_encrypter(plaintext, key):
    return None


def affine_encrypter(plaintext, m, b):
    ciphertext = []
    plaintext = plaintext.replace(" ", "").strip()
    for i in range(len(plaintext)):
        base_number = letter_base_number(plaintext[i])
        encrypted_char = (m * (ord(plaintext[i])-base_number) + b) % 26
        encrypted_char += base_number
        ciphertext.append(chr(encrypted_char))

    return "".join(ciphertext)


def hill_encrypter(plaintext, key):
    res = ""
    plaintext = plaintext.replace(" ", "")
    rem = len(plaintext) % 3
    plaintext += 'x' * (3-rem)
    key = np.array([[17, 17, 5], [21, 18, 21], [2, 2, 19]])
    for i in range(0, len(plaintext) - 3, 3):
        current_string = np.array([getOrder(plaintext[i]), getOrder(
            plaintext[i+1]), getOrder(plaintext[i+2])])
        dot_result = np.dot(key, current_string)
        current_result = np.mod(dot_result, 26)
        res += getChar(current_result[0]) + \
            getChar(current_result[1]) + getChar(current_result[2])
    return res


def enigma_encrypter(plaintext, key):
    return None
