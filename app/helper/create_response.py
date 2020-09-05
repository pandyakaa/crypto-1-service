from flask import jsonify


def create_plaintext_response(plaintext):
    return ({'plaintext': plaintext})


def create_cipher_text_response(cipher_text):
    return ({'ciphertext': cipher_text})


def create_plain_file_response(plaintext):
    # TODO
    return plaintext


def create_cipher_file_response(cipher_text):
    # TODO
    return cipher_text
