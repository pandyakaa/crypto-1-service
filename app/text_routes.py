from app import app
from flask import request


@app.route('/')
def index():
    return "Hello, text!"


''' Text encryption '''


@app.route('/encrypt/text/vigenere', methods=['GET'])
def encrypt_text_vigenere():
    query = request.args.get('query')
    return query


@app.route('/encrypt/text/vigenere/full', methods=['GET'])
def encrypt_full_text_vigenere():
    query = request.args.get('query')
    return query


@app.route('/encrypt/text/vigenere/auto', methods=['GET'])
def encrypt_auto_text_vigenere():
    query = request.args.get('query')
    return query


@app.route('/encrypt/text/vigenere/extended', methods=['GET'])
def encrypt_extended_text_vigenere():
    query = request.args.get('query')
    return query


@app.route('/encrypt/text/playfair', methods=['GET'])
def encrypt_text_playfair():
    query = request.args.get('query')
    return query


@app.route('/encrypt/text/super', methods=['GET'])
def encrypt_text_super():
    query = request.args.get('query')
    return query


@app.route('/encrypt/text/affine', methods=['GET'])
def encrypt_text_affine():
    query = request.args.get('query')
    return query


@app.route('/encrypt/text/hill', methods=['GET'])
def encrypt_text_hill():
    query = request.args.get('query')
    return query


@app.route('/encrypt/text/enigma', methods=['GET'])
def encrypt_text_enigma():
    query = request.args.get('query')
    return query


''' Text decryption '''


@app.route('/decrypt/text/vigenere', methods=['GET'])
def decrypt_text_vigenere():
    query = request.args.get('query')
    return query


@app.route('/decrypt/text/vigenere/full', methods=['GET'])
def decrypt_full_text_vigenere():
    query = request.args.get('query')
    return query


@app.route('/decrypt/text/vigenere/auto', methods=['GET'])
def decrypt_auto_text_vigenere():
    query = request.args.get('query')
    return query


@app.route('/decrypt/text/vigenere/extended', methods=['GET'])
def decrypt_extended_text_vigenere():
    query = request.args.get('query')
    return query


@app.route('/decrypt/text/playfair', methods=['GET'])
def decrypt_text_playfair():
    query = request.args.get('query')
    return query


@app.route('/decrypt/text/super', methods=['GET'])
def decrypt_text_super():
    query = request.args.get('query')
    return query


@app.route('/decrypt/text/affine', methods=['GET'])
def decrypt_text_affine():
    query = request.args.get('query')
    return query


@app.route('/decrypt/text/hill', methods=['GET'])
def decrypt_text_hill():
    query = request.args.get('query')
    return query


@app.route('/decrypt/text/enigma', methods=['GET'])
def decrypt_text_enigma():
    query = request.args.get('query')
    return query
