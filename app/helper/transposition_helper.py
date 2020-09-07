''' Super cipher helper '''


def create_encrypt_matrix(text, width):
    r = 0
    c = 0
    mat = [[]]
    for _, char in enumerate(text):
        mat[r].append(char)
        c += 1
        if c >= width:
            c = 0
            r += 1
            mat.append([])
    
    mat = mat[:-1]

    return mat
