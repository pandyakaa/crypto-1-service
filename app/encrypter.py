'''
Encrypter

1. Standard vigenere cipher
2. Full vigenere cipher
3. Auto-key vigenere cipher
4. Playfair cipher
5. Super encrypt = standard vigenere + transpose cipher
5. Affine cipher
6. Hill cipher
7. Enigma cipher
'''


from .helper.vigenere_helper import *


def standard_vigenere_encrypter(plaintext, key):
    ciphertext = []
    key = generate_vigenere_standard_key(plaintext, key)
    plaintext = plaintext.replace(" ", "").strip()
    for i in range(len(plaintext)):
        encrypted_char = (ord(plaintext[i]) + ord(key[i])) % 26
        encrypted_char += ord('A')
        ciphertext.append(chr(encrypted_char))

    return "".join(ciphertext)


def full_vigenere_encrypter(plaintext, key):
    return None


def auto_key_vigenere_encrypter(plaintext, key):
    ciphertext = []
    key = generate_vigenere_full_key(plaintext, key)
    for i in range(len(plaintext)):
        encrypted_char = (ord(plaintext[i]) + ord(key[i])) % 26
        encrypted_char += ord('A')
        ciphertext.append(chr(encrypted_char))

    return "".join(ciphertext)


def playfair_encrypter(plaintext, key):
    return None


def super_encrypter(plaintext, key):
    return None


def affine_encrypter(plaintext, key):
    return None


def hill_encrypter(plaintext, key):
    return None


def enigma_encrypter(plaintext, key):
    return None
