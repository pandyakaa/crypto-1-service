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

from .helper.vigenere_helper import generate_vigenere_standard_key
from .helper.handle_capital import letter_base_number, standardize_key
from .helper.affine_helper import find_m_inverse


def standard_vigenere_decrypter(ciphertext, key):
    plaintext = []
    key = generate_vigenere_standard_key(ciphertext, key)
    for i in range(len(ciphertext)):
        key_letter = standardize_key(ciphertext[i], key[i])
        base_number = letter_base_number(ciphertext[i])
        decrypted_char = (ord(ciphertext[i]) - ord(key_letter) + 26) % 26
        decrypted_char += base_number
        plaintext.append(chr(decrypted_char))

    return "".join(plaintext)


def full_vigenere_decrypter(ciphertext, key):
    return None


def auto_key_vigenere_decrypter(ciphertext, key):
    plaintext = []
    for i in range(len(ciphertext)):
        key_letter = standardize_key(ciphertext[i], key[i])
        base_number = letter_base_number(ciphertext[i])
        decrypted_char = (ord(ciphertext[i]) - ord(key_letter) + 26) % 26
        decrypted_char += base_number
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


def affine_decrypter(ciphertext, m, b):
    plaintext = []
    for i in range(len(ciphertext)):
        inversed_m = find_m_inverse(m)
        base_number = letter_base_number(ciphertext[i])
        decrypted_char = (
            inversed_m * ((ord(ciphertext[i])-base_number) - b)) % 26
        decrypted_char += base_number
        plaintext.append(chr(decrypted_char))

    return "".join(plaintext)


def hill_decrypter(ciphertext, key):
    return None


def enigma_decrypter(ciphertext, key):
    return None
