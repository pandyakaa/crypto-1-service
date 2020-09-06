from app import app
from flask import request, jsonify
from .helper.handle_file import handle_file, handle_ascii_file
from .encrypter import *


@app.route('/file')
def index_file():
    return "Hello, file!"


''' File encryption '''


@app.route('/encrypt/file/vigenere', methods=['GET', 'POST'])
def encrypt_file_vigenere():
    file = request.files['file']
    key = request.args.get('key')
    filename, file_context = handle_file(file)
    encrypted_context = standard_vigenere_encrypter(file_context, key)
    return jsonify({'ciphertext': encrypted_context})


@app.route('/encrypt/file/vigenere/full', methods=['GET', 'POST'])
def encrypt_full_file_vigenere():
    query = request.args.get('plaintext')
    return query


@app.route('/encrypt/file/vigenere/auto', methods=['GET', 'POST'])
def encrypt_auto_file_vigenere():
    query = request.args.get('plaintext')
    return query


@app.route('/encrypt/file/vigenere/extended', methods=['GET', 'POST'])
def encrypt_extended_file_vigenere():
    query = request.args.get('plaintext')
    return query


@app.route('/encrypt/file/playfair', methods=['GET', 'POST'])
def encrypt_file_playfair():
    query = request.args.get('plaintext')
    return query


@app.route('/encrypt/file/super', methods=['GET', 'POST'])
def encrypt_file_super():
    query = request.args.get('plaintext')
    return query


@app.route('/encrypt/file/affine', methods=['GET', 'POST'])
def encrypt_file_affine():
    query = request.args.get('plaintext')
    return query


@app.route('/encrypt/file/hill', methods=['GET', 'POST'])
def encrypt_file_hill():
    query = request.args.get('plaintext')
    return query


@app.route('/encrypt/file/enigma', methods=['GET', 'POST'])
def encrypt_file_enigma():
    query = request.args.get('plaintext')
    return query


''' File decryption '''


@app.route('/decrypt/file/vigenere', methods=['GET', 'POST'])
def decrypt_file_vigenere():
    query = request.args.get('ciphertext')
    return query


@app.route('/decrypt/file/vigenere/full', methods=['GET', 'POST'])
def decrypt_full_file_vigenere():
    query = request.args.get('ciphertext')
    return query


@app.route('/decrypt/file/vigenere/auto', methods=['GET', 'POST'])
def decrypt_auto_file_vigenere():
    query = request.args.get('ciphertext')
    return query


@app.route('/decrypt/file/vigenere/extended', methods=['GET', 'POST'])
def decrypt_extended_file_vigenere():
    query = request.args.get('ciphertext')
    return query


@app.route('/decrypt/file/playfair', methods=['GET', 'POST'])
def decrypt_file_playfair():
    query = request.args.get('ciphertext')
    return query


@app.route('/decrypt/file/super', methods=['GET', 'POST'])
def decrypt_file_super():
    query = request.args.get('ciphertext')
    return query


@app.route('/decrypt/file/affine', methods=['GET', 'POST'])
def decrypt_file_affine():
    query = request.args.get('ciphertext')
    return query


@app.route('/decrypt/file/hill', methods=['GET', 'POST'])
def decrypt_file_hill():
    query = request.args.get('ciphertext')
    return query


@app.route('/decrypt/file/enigma', methods=['GET', 'POST'])
def decrypt_file_enigma():
    query = request.args.get('ciphertext')
    return query
