from flask import jsonify


def create_plain_text_response(plaintext):
    return ({'plaintext': plaintext})


def create_cipher_text_response(cipher_text):
    n = 5
    splitted_ciphertext = [cipher_text[i:i+n]
                           for i in range(0, len(cipher_text), n)]
    return ({'ciphertext': cipher_text, 'splitted_ciphertext': splitted_ciphertext})


def create_plain_file_response(plaintext):
    # TODO
    return plaintext


def create_cipher_file_response(cipher_text):
    # TODO
    return cipher_text
