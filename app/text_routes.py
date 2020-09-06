from app import app
from flask import request
from .decrypter import *
from .encrypter import *
from .helper.create_response import create_cipher_text_response, create_plain_text_response


@app.route('/')
def index():
    return "Hello, text!"


''' Text encryption '''


@app.route('/encrypt/text/vigenere', methods=['GET'])
def encrypt_text_vigenere():
    query = request.args.get('plaintext')
    key = request.args.get('key')
    encrypted_text = standard_vigenere_encrypter(query, key)

    response = create_cipher_text_response(encrypted_text)
    return response


@app.route('/encrypt/text/vigenere/full', methods=['GET'])
def encrypt_full_text_vigenere():
    query = request.args.get('plaintext')
    return query


@app.route('/encrypt/text/vigenere/auto', methods=['GET'])
def encrypt_auto_text_vigenere():
    query = request.args.get('plaintext')
    key = request.args.get('key')
    encrypted_text = auto_key_vigenere_encrypter(query, key)

    response = create_cipher_text_response(encrypted_text)
    return response


@app.route('/encrypt/text/vigenere/extended', methods=['GET'])
def encrypt_extended_text_vigenere():
    query = request.args.get('plaintext')
    return query


@app.route('/encrypt/text/playfair', methods=['GET'])
def encrypt_text_playfair():
    query = request.args.get('plaintext')
    return query


@app.route('/encrypt/text/super', methods=['GET'])
def encrypt_text_super():
    query = request.args.get('plaintext')
    return query


@app.route('/encrypt/text/affine', methods=['GET'])
def encrypt_text_affine():
    query = request.args.get('plaintext')
    m = request.args.get('m')
    b = request.args.get('b')

    m, b = int(m), int(b)
    encrypted_text = affine_encrypter(query, m, b)

    response = create_cipher_text_response(encrypted_text)
    return response


@app.route('/encrypt/text/hill', methods=['GET'])
def encrypt_text_hill():
    query = request.args.get('plaintext')
    encrypted_text = hill_encrypter(query,'')
    response = create_cipher_text_response(encrypted_text)
    return response


@app.route('/encrypt/text/enigma', methods=['GET'])
def encrypt_text_enigma():
    query = request.args.get('plaintext')
    return query


''' Text decryption '''


@app.route('/decrypt/text/vigenere', methods=['GET'])
def decrypt_text_vigenere():
    query = request.args.get('ciphertext')
    key = request.args.get('key')
    decrypted_text = standard_vigenere_decrypter(query, key)

    response = create_plain_text_response(decrypted_text)
    return response


@app.route('/decrypt/text/vigenere/full', methods=['GET'])
def decrypt_full_text_vigenere():
    query = request.args.get('ciphertext')
    return query


@app.route('/decrypt/text/vigenere/auto', methods=['GET'])
def decrypt_auto_text_vigenere():
    query = request.args.get('ciphertext')
    key = request.args.get('key')
    decrypted_text = auto_key_vigenere_decrypter(query, key)

    response = create_plain_text_response(decrypted_text)
    return response


@app.route('/decrypt/text/vigenere/extended', methods=['GET'])
def decrypt_extended_text_vigenere():
    query = request.args.get('ciphertext')
    return query


@app.route('/decrypt/text/playfair', methods=['GET'])
def decrypt_text_playfair():
    query = request.args.get('ciphertext')
    return query


@app.route('/decrypt/text/super', methods=['GET'])
def decrypt_text_super():
    query = request.args.get('ciphertext')
    return query


@app.route('/decrypt/text/affine', methods=['GET'])
def decrypt_text_affine():
    query = request.args.get('ciphertext')
    return query


@app.route('/decrypt/text/hill', methods=['GET'])
def decrypt_text_hill():
    query = request.args.get('ciphertext')
    decrypted_text = hill_decrypter(query,'')
    response = create_plain_text_response(decrypted_text)
    return response


@app.route('/decrypt/text/enigma', methods=['GET'])
def decrypt_text_enigma():
    query = request.args.get('ciphertext')
    return query
