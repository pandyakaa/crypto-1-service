''' Playfair cipher helper '''

import numpy as np

def create_playfair_key(text) :
    alphabet = 'abcdefghiklmnopqrstuvwxyz'
    a = text.replace('j', '')
    a = a.replace(' ', '')
    key = ''.join(sorted(set(a), key=a.index))
    alphabet = [i for i in alphabet if i not in key]
    key += ''.join(alphabet)
    key_matrix = []
    for i in range(5):
        key_matrix.append([])
        for j in range(5):
            key_matrix[i].append(key[i*5+j])
    return np.array(key_matrix)

def process_plain_input(text):
    a = text.replace('j', 'i')
    a = a.replace(' ', '')
    i = 0
    while(i<len(a)-1):
        if(a[i]==a[i+1]):
            a = a[:i+1] + 'x' + a[i+1:]
        i+=1
    return a+'x' if len(a)%2==1 else a

def encrypt_bigram(bigram, key_matrix):
    first = np.where(key_matrix==bigram[0])
    second = np.where(key_matrix==bigram[1])
    a, b = first[0][0], first[1][0]
    c, d = second[0][0], second[1][0]
    if (a==c):
        y1, y2 = (b+1)%5, (d+1)%5
        return key_matrix[a][y1] + key_matrix[c][y2]
    if (b==d):
        x1, x2 = (a+1)%5, (c+1)%5
        return key_matrix[x1][b] + key_matrix[x2][d]
    return key_matrix[a][d] + key_matrix[c][b]

def decrypt_bigram(bigram, key_matrix):
    first = np.where(key_matrix==bigram[0])
    second = np.where(key_matrix==bigram[1])
    a, b = first[0][0], first[1][0]
    c, d = second[0][0], second[1][0]
    if (a==c):
        y1, y2 = (b-1)%5, (d-1)%5
        return key_matrix[a][y1] + key_matrix[c][y2]
    if (b==d):
        x1, x2 = (a-1)%5, (c-1)%5
        return key_matrix[x1][b] + key_matrix[x2][d]
    return key_matrix[a][d] + key_matrix[c][b]

# if __name__ == "__main__":
#     key_matrix = create_playfair_key('jalan ganesha sepuluh')
#     print(key_matrix)
#     processed_input = process_plain_input('temui ibu nanti malam')