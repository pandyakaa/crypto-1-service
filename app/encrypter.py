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
from .helper.handle_character import letter_base_number, standardize_key, get_char, get_order
from .helper.transposition_helper import create_encrypt_matrix


def standard_vigenere_encrypter(plaintext, key):
    ciphertext = []
    key = generate_vigenere_standard_key(plaintext, key)
    plaintext = plaintext.replace(" ", "").strip()
    for i in range(len(plaintext)):
        key_letter = standardize_key(plaintext[i], key[i])
        base_number = letter_base_number(plaintext[i])
        encrypted_char = (ord(plaintext[i]) +
                          ord(key_letter) - 2 * base_number) % 26
        encrypted_char = get_char(encrypted_char, base_number)
        ciphertext.append(encrypted_char)

    return "".join(ciphertext)


def full_vigenere_encrypter(plaintext, key):
    return None


def auto_key_vigenere_encrypter(plaintext, key):
    ciphertext = []
    key = generate_vigenere_full_key(plaintext, key)
    for i in range(len(plaintext)):
        key_letter = standardize_key(plaintext[i], key[i])
        base_number = letter_base_number(plaintext[i])
        encrypted_char = (ord(plaintext[i]) +
                          ord(key_letter) - 2 * base_number) % 26
        encrypted_char = get_char(encrypted_char, base_number)
        ciphertext.append(encrypted_char)

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


def transposition_encrypter(plaintext, key):
    ciphertext = []
    if (len(plaintext) % key) != 0:
        plaintext += 'x' * (key - (len(plaintext) % key))
    encryption_matrix = create_encrypt_matrix(plaintext, key)

    for j in range(len(encryption_matrix[0])):
        for i in encryption_matrix:
            ciphertext.append(i[j])

    return "".join(ciphertext)


def super_encrypter(plaintext, vigenere_key, transpose_key):
    vigenere_encrypted_text = standard_vigenere_encrypter(
        plaintext, vigenere_key)
    transposition_encrypted_text = transposition_encrypter(
        vigenere_encrypted_text, transpose_key)

    return transposition_encrypted_text


def affine_encrypter(plaintext, m, b):
    ciphertext = []
    plaintext = plaintext.replace(" ", "").strip()
    for i in range(len(plaintext)):
        base_number = letter_base_number(plaintext[i])
        encrypted_char = (m * (ord(plaintext[i])-base_number) + b) % 26
        encrypted_char = get_char(encrypted_char, base_number)
        ciphertext.append(encrypted_char)

    return "".join(ciphertext)


def hill_encrypter(plaintext, key):
    ciphertext = ""
    plaintext = plaintext.replace(" ", "")
    rem = len(plaintext) % 3
    if (rem != 0):
        plaintext += 'x' * (3-rem)
    key = np.array([[17, 17, 5], [21, 18, 21], [2, 2, 19]])
    for i in range(0, len(plaintext), 3):
        base_number = [letter_base_number(plaintext[i]), letter_base_number(
            plaintext[i+1]), letter_base_number(plaintext[i+2])]
        current_string = np.array([get_order(plaintext[i], base_number[0]), get_order(
            plaintext[i+1], base_number[1]), get_order(plaintext[i+2], base_number[2])])
        dot_result = np.dot(key, current_string)
        current_result = np.mod(dot_result, 26)
        ciphertext += get_char(current_result[0], base_number[0]) + \
            get_char(current_result[1], base_number[1]) + \
            get_char(current_result[2], base_number[2])
    return ciphertext


def enigma_encrypter(plaintext, key):
    return None
