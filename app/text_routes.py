from app import app
from flask import request
from .decrypter import hill_decrypter, affine_decrypter, auto_key_vigenere_decrypter, standard_vigenere_decrypter, super_decrypter, extended_vigenere_decrypter, playfair_decrypter
from .encrypter import hill_encrypter, affine_encrypter, auto_key_vigenere_encrypter, standard_vigenere_encrypter, super_encrypter, extended_vigenere_encrypter, playfair_encrypter
from .util.create_response import create_cipher_text_response, create_plain_text_response


@app.route('/')
def index():
    return "Hello, text!"


''' Text encryption '''


@app.route('/encrypt/text/vigenere', methods=['POST'])
def encrypt_text_vigenere():
    json_request = request.get_json()
    query = json_request['message']
    key = json_request['key']
    encrypted_text = standard_vigenere_encrypter(query, key)

    response = create_cipher_text_response(encrypted_text)
    return response


@app.route('/encrypt/text/vigenere/full', methods=['POST'])
def encrypt_full_text_vigenere():
    query = request.args.get('message')
    return query


@app.route('/encrypt/text/vigenere/auto', methods=['POST'])
def encrypt_auto_text_vigenere():
    json_request = request.get_json()
    query = json_request['message']
    key = json_request['key']
    encrypted_text = auto_key_vigenere_encrypter(query, key)

    response = create_cipher_text_response(encrypted_text)
    return response


@app.route('/encrypt/text/vigenere/extended', methods=['POST'])
def encrypt_extended_text_vigenere():
    json_request = request.get_json()
    query = json_request['message']
    key = json_request['key']
    query = query.encode()
    encrypted_text = extended_vigenere_encrypter(query, key)

    response = create_cipher_text_response(encrypted_text)
    return response


@app.route('/encrypt/text/playfair', methods=['POST'])
def encrypt_text_playfair():
    json_request = request.get_json()
    query = json_request['message']
    key = json_request['key']
    encrypted_text = playfair_encrypter(query, key)

    response = create_cipher_text_response(encrypted_text)
    return response


@app.route('/encrypt/text/super', methods=['POST'])
def encrypt_text_super():
    json_request = request.get_json()
    query = json_request['message']
    vigenere_key = json_request['vigenere_key']
    transpose_key = int(json_request['transpose_key'])

    encrypted_text = super_encrypter(query, vigenere_key, transpose_key)

    response = create_cipher_text_response(encrypted_text)
    return response


@app.route('/encrypt/text/affine', methods=['POST'])
def encrypt_text_affine():
    json_request = request.get_json()
    query = json_request['message']
    m = json_request['m']
    b = json_request['b']

    m, b = int(m), int(b)
    encrypted_text = affine_encrypter(query, m, b)

    response = create_cipher_text_response(encrypted_text)
    return response


@app.route('/encrypt/text/hill', methods=['POST'])
def encrypt_text_hill():
    json_request = request.get_json()
    query = json_request['message']
    key = json_request['key']
    response = hill_encrypter(query, key)
    response = create_cipher_text_response(response)
    return response


@app.route('/encrypt/text/enigma', methods=['POST'])
def encrypt_text_enigma():
    query = request.args.get('message')
    return query


''' Text decryption '''


@app.route('/decrypt/text/vigenere', methods=['POST'])
def decrypt_text_vigenere():
    json_request = request.get_json()
    query = json_request['message']
    key = json_request['key']
    decrypted_text = standard_vigenere_decrypter(query, key)

    response = create_plain_text_response(decrypted_text)
    return response


@app.route('/decrypt/text/vigenere/full', methods=['POST'])
def decrypt_full_text_vigenere():
    query = request.args.get('message')
    return query


@app.route('/decrypt/text/vigenere/auto', methods=['POST'])
def decrypt_auto_text_vigenere():
    json_request = request.get_json()
    query = json_request['message']
    key = json_request['key']
    decrypted_text = auto_key_vigenere_decrypter(query, key)

    response = create_plain_text_response(decrypted_text)
    return response


@app.route('/decrypt/text/vigenere/extended', methods=['POST'])
def decrypt_extended_text_vigenere():
    json_request = request.get_json()
    query = json_request['message']
    key = json_request['key']
    decrypted_text = extended_vigenere_decrypter(query, key)

    response = create_plain_text_response(decrypted_text)
    return response


@app.route('/decrypt/text/playfair', methods=['POST'])
def decrypt_text_playfair():
    json_request = request.get_json()
    query = json_request['message']
    key = json_request['key']
    decrypted_text = playfair_decrypter(query, key)
    decrypted_text = decrypted_text.replace('x', '')

    response = create_plain_text_response(decrypted_text)
    return response


@app.route('/decrypt/text/super', methods=['POST'])
def decrypt_text_super():
    json_request = request.get_json()
    query = json_request['message']
    vigenere_key = json_request['vigenere_key']
    transpose_key = json_request['transpose_key']
    decrypted_text = super_decrypter(query, vigenere_key, transpose_key)

    response = create_plain_text_response(decrypted_text)
    return response


@app.route('/decrypt/text/affine', methods=['POST'])
def decrypt_text_affine():
    json_request = request.get_json()
    query = json_request['message']
    m = json_request['m']
    b = json_request['b']

    m, b = int(m), int(b)
    decrypted_text = affine_decrypter(query, m, b)

    response = create_plain_text_response(decrypted_text)
    return response


@app.route('/decrypt/text/hill', methods=['POST'])
def decrypt_text_hill():
    json_request = request.get_json()
    query = json_request['message']
    key = json_request['key']
    response = hill_decrypter(query, key)

    response = create_plain_text_response(response)
    return response


@app.route('/decrypt/text/enigma', methods=['POST'])
def decrypt_text_enigma():
    query = request.args.get('message')
    return query
