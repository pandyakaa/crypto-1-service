''' Affine cipher helper '''


def find_m_inverse(m):
    found = False
    i = 1
    result = 0
    while not found:
        if (((26 * i + 1) % m) == 0):
            found = True
            result = ((26 * i + 1) / m) % 26
        else:
            i += 1

    result = int(result)
    return result
