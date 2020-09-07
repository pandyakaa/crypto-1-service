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
from .helper.vigenere_helper import generate_vigenere_standard_key
from .helper.handle_character import letter_base_number, standardize_key, get_char, get_order
from .helper.affine_helper import find_m_inverse
from .helper.transposition_helper import create_decrypt_matrix


def standard_vigenere_decrypter(ciphertext, key):
    plaintext = []
    key = generate_vigenere_standard_key(ciphertext, key)
    for i in range(len(ciphertext)):
        key_letter = standardize_key(ciphertext[i], key[i])
        base_number = letter_base_number(ciphertext[i])
        decrypted_char = (ord(ciphertext[i]) - ord(key_letter)) % 26
        decrypted_char = get_char(decrypted_char, base_number)
        plaintext.append(decrypted_char)

    return "".join(plaintext)


def full_vigenere_decrypter(ciphertext, key):
    return None


def auto_key_vigenere_decrypter(ciphertext, key):
    plaintext = []
    for i in range(len(ciphertext)):
        key_letter = standardize_key(ciphertext[i], key[i])
        base_number = letter_base_number(ciphertext[i])
        decrypted_char = (ord(ciphertext[i]) - ord(key_letter)) % 26
        decrypted_char = get_char(decrypted_char, base_number)
        plaintext.append(decrypted_char)

    return "".join(plaintext)


def extended_vigenere_decrypter(ciphertext, key):
    plaintext = []
    key = generate_vigenere_standard_key(ciphertext, key)
    for i in range(len(ciphertext)):
        decrypted_char = (ord(ciphertext[i]) - ord(key[i])) % 256
        plaintext.append(chr(decrypted_char))

    return "".join(plaintext)


def playfair_decrypter(ciphertext, key):
    return None


def transposition_decrypter(ciphertext, key):
    plaintext = []
    if (len(ciphertext) % key) != 0:
        ciphertext += 'x' * (key - (len(ciphertext) % key))
    decryption_matrix = create_decrypt_matrix(ciphertext, key)

    for j in range(len(decryption_matrix[0])):
        for i in decryption_matrix:
            plaintext.append(i[j])

    return "".join(plaintext)


def super_decrypter(ciphertext, vigenere_key, transpose_key):
    plaintext = transposition_decrypter(ciphertext, transpose_key)
    plaintext = standard_vigenere_decrypter(plaintext, vigenere_key)

    return plaintext


def affine_decrypter(ciphertext, m, b):
    plaintext = []
    for i in range(len(ciphertext)):
        inversed_m = find_m_inverse(m)
        base_number = letter_base_number(ciphertext[i])
        decrypted_char = (
            inversed_m * ((ord(ciphertext[i])-base_number) - b)) % 26
        decrypted_char = get_char(decrypted_char, base_number)
        plaintext.append(decrypted_char)

    return "".join(plaintext)


def hill_decrypter(ciphertext, key):
    plaintext = ""
    ciphertext = ciphertext.replace(" ", "")
    key = np.array([[17, 17, 5], [21, 18, 21], [2, 2, 19]])
    key_inversed = np.linalg.inv(key)
    for i in range(0, len(ciphertext), 3):
        base_number = [letter_base_number(ciphertext[i]), letter_base_number(
            ciphertext[i+1]), letter_base_number(ciphertext[i+2])]
        current_string = np.array([get_order(ciphertext[i], base_number[0]), get_order(
            ciphertext[i+1], base_number[1]), get_order(ciphertext[i+2], base_number[2])])
        dot_result = np.dot(key_inversed, current_string)
        current_result = np.mod(dot_result, 26)
        plaintext += get_char(current_result[0], base_number[0]) + \
            get_char(current_result[1], base_number[1]) + \
            get_char(current_result[2], base_number[2])
    return plaintext


def enigma_decrypter(ciphertext, key):
    return None
