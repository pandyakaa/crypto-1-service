import os
import time

save_path = os.getcwd() + '/app/file_resources/'


def create_plain_text_response(plaintext):
    return ({'plaintext': plaintext})


def create_cipher_text_response(cipher_text):
    n = 5
    splitted_ciphertext = [cipher_text[i:i+n]
                           for i in range(0, len(cipher_text), n)]
    return ({'ciphertext': cipher_text, 'splitted_ciphertext': splitted_ciphertext})


def create_file_response(filename, cipher_text):
    filename = str(int(time.time())) + '.encrypted.' + filename
    complete_filename = os.path.join(save_path, filename)
    with open(complete_filename, 'wb+') as f:
        f.write(cipher_text)

    return complete_filename
