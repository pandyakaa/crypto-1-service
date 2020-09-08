from app import app
from flask import request, send_file, jsonify
from .encrypter import standard_vigenere_encrypter, auto_key_vigenere_encrypter, extended_vigenere_encrypter, playfair_encrypter, super_encrypter, affine_encrypter, hill_encrypter, full_vigenere_encrypter
from .decrypter import standard_vigenere_decrypter, auto_key_vigenere_decrypter, extended_vigenere_decrypter, playfair_decrypter, super_decrypter, affine_decrypter, hill_decrypter, full_vigenere_decrypter
from .util.create_response import create_file_response
from .util.handle_file import handle_file, handle_ascii_file


@app.route('/file')
def index_file():
    return "Hello, file!"


''' File encryption '''


@app.route('/encrypt/file/vigenere', methods=['GET', 'POST'])
def encrypt_file_vigenere():
    file = request.files['file']
    key = request.form['key']
    filename, file_context = handle_file(file)
    encrypted_context = standard_vigenere_encrypter(file_context, key)

    complete_filename = create_file_response(
        filename, encrypted_context)
    return send_file(complete_filename)


@app.route('/encrypt/file/vigenere/full', methods=['GET', 'POST'])
def encrypt_full_file_vigenere():
    file = request.files['file']
    key = request.form['key']
    filename, file_context = handle_file(file)
    encrypted_context = full_vigenere_encrypter(file_context, key)

    complete_filename = create_file_response(
        filename, encrypted_context)
    return send_file(complete_filename)


@app.route('/encrypt/file/vigenere/auto', methods=['GET', 'POST'])
def encrypt_auto_file_vigenere():
    file = request.files['file']
    key = request.form['key']
    filename, file_context = handle_file(file)
    encrypted_context = auto_key_vigenere_encrypter(file_context, key)

    complete_filename = create_file_response(
        filename, encrypted_context)
    return send_file(complete_filename)


@app.route('/encrypt/file/vigenere/extended', methods=['GET', 'POST'])
def encrypt_extended_file_vigenere():
    file = request.files['file']
    key = request.form['key']
    filename, file_context = handle_ascii_file(file)
    encrypted_context = extended_vigenere_encrypter(file_context, key)

    complete_filename = create_file_response(
        filename, encrypted_context)
    return send_file(complete_filename)


@app.route('/encrypt/file/playfair', methods=['GET', 'POST'])
def encrypt_file_playfair():
    file = request.files['file']
    key = request.form['key']
    filename, file_context = handle_file(file)
    encrypted_context = playfair_encrypter(file_context, key)

    complete_filename = create_file_response(
        filename, encrypted_context)
    return send_file(complete_filename)


@app.route('/encrypt/file/super', methods=['GET', 'POST'])
def encrypt_file_super():
    file = request.files['file']
    key = request.form['key']
    vigenere_key, transpose_key = key.split(',')
    transpose_key = int(transpose_key)
    filename, file_context = handle_file(file)
    encrypted_context = super_encrypter(
        file_context, vigenere_key, transpose_key)

    complete_filename = create_file_response(
        filename, encrypted_context)
    return send_file(complete_filename)


@app.route('/encrypt/file/affine', methods=['GET', 'POST'])
def encrypt_file_affine():
    file = request.files['file']
    key = request.form['key']
    m, b = key.split(',')

    m, b = int(m), int(b)
    filename, file_context = handle_file(file)
    encrypted_context = affine_encrypter(file_context, m, b)

    complete_filename = create_file_response(
        filename, encrypted_context)
    return send_file(complete_filename)


@app.route('/encrypt/file/hill', methods=['GET', 'POST'])
def encrypt_file_hill():
    file = request.files['file']
    key = request.form['key']
    filename, file_context = handle_file(file)
    encrypted_context = hill_encrypter(file_context, key)

    complete_filename = create_file_response(
        filename, encrypted_context)
    return send_file(complete_filename)


@app.route('/encrypt/file/enigma', methods=['GET', 'POST'])
def encrypt_file_enigma():
    query = request.args.get('message')
    return query


''' File decryption '''


@app.route('/decrypt/file/vigenere', methods=['GET', 'POST'])
def decrypt_file_vigenere():
    file = request.files['file']
    key = request.form['key']
    filename, file_context = handle_file(file)
    decrypted_context = standard_vigenere_decrypter(file_context, key)

    complete_filename = create_file_response(
        filename, decrypted_context)
    return send_file(complete_filename)


@app.route('/decrypt/file/vigenere/full', methods=['GET', 'POST'])
def decrypt_full_file_vigenere():
    file = request.files['file']
    key = request.form['key']
    filename, file_context = handle_file(file)
    decrypted_context = full_vigenere_decrypter(file_context, key)

    complete_filename = create_file_response(
        filename, decrypted_context)
    return send_file(complete_filename)


@app.route('/decrypt/file/vigenere/auto', methods=['GET', 'POST'])
def decrypt_auto_file_vigenere():
    file = request.files['file']
    key = request.form['key']
    filename, file_context = handle_file(file)
    decrypted_context = auto_key_vigenere_decrypter(file_context, key)

    complete_filename = create_file_response(
        filename, decrypted_context)
    return send_file(complete_filename)


@app.route('/decrypt/file/vigenere/extended', methods=['GET', 'POST'])
def decrypt_extended_file_vigenere():
    file = request.files['file']
    key = request.form['key']
    filename, file_context = handle_ascii_file(file)
    decrypted_context = extended_vigenere_decrypter(file_context, key)

    complete_filename = create_file_response(
        filename, decrypted_context)
    return send_file(complete_filename)


@app.route('/decrypt/file/playfair', methods=['GET', 'POST'])
def decrypt_file_playfair():
    file = request.files['file']
    key = request.form['key']
    filename, file_context = handle_file(file)
    decrypted_context = playfair_decrypter(file_context, key)
    decrypted_context = decrypted_context.replace('x', '')

    complete_filename = create_file_response(
        filename, decrypted_context)
    return send_file(complete_filename)


@app.route('/decrypt/file/super', methods=['GET', 'POST'])
def decrypt_file_super():
    file = request.files['file']
    key = request.form['key']
    vigenere_key, transpose_key = key.split(',')
    transpose_key = int(transpose_key)
    filename, file_context = handle_file(file)
    decrypted_context = super_decrypter(
        file_context, vigenere_key, transpose_key)

    complete_filename = create_file_response(
        filename, decrypted_context)
    return send_file(complete_filename)


@app.route('/decrypt/file/affine', methods=['GET', 'POST'])
def decrypt_file_affine():
    file = request.files['file']
    key = request.form['key']
    m, b = key.split(',')

    m, b = int(m), int(b)
    filename, file_context = handle_file(file)
    decrypted_context = affine_decrypter(file_context, m, b)

    complete_filename = create_file_response(
        filename, decrypted_context)
    return send_file(complete_filename)


@app.route('/decrypt/file/hill', methods=['GET', 'POST'])
def decrypt_file_hill():
    file = request.files['file']
    key = request.form['key']
    filename, file_context = handle_file(file)
    decrypted_context = hill_decrypter(file_context, key)

    complete_filename = create_file_response(
        filename, decrypted_context)
    return send_file(complete_filename)


@app.route('/decrypt/file/enigma', methods=['GET', 'POST'])
def decrypt_file_enigma():
    query = request.args.get('message')
    return query
