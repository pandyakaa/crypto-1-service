from itertools import permutations
''' Vigenere cipher helper '''


def generate_vigenere_standard_key(text, key):
    key = list(key)
    if len(key) == len(text):
        return key
    elif len(key) > len(text):
        key = key[:len(text)]
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])

    return "".join(key)


def generate_vigenere_auto_key(text, key):
    key = list(key)
    if len(key) == len(text):
        return key
    elif len(key) > len(text):
        key = key[:len(text)]
    else:
        for i in range(len(text) - len(key)):
            key.append(text[i])

    return "".join(key)


'''
[   [], 
    [], 
    [], 
    [], 
    [], 
    [], 
    [], 
    [], 
    [], 
    [], 
    [], 
    [], 
    [], 
    [], 
    [], 
    [], 
    [], 
    [], 
    [], 
    [], 
    [], 
    [], 
    [], 
    [], 
    [], 
    [] ]
'''


def generate_vigenere_matrix():
    matrix = [['a', 'z', 'b', 'y', 'c', 'x', 'd', 'w', 'e', 'v', 'f', 'u', 'g',
               't', 'h', 's', 'i', 'r', 'j', 'q', 'k', 'p', 'l', 'o', 'm', 'n'],
              ['z', 'b', 'y', 'c', 'x', 'd', 'w', 'e', 'v', 'f', 'u', 'g', 't',
               'h', 's', 'i', 'r', 'j', 'q', 'k', 'p', 'l', 'o', 'm', 'n', 'a'],
              ['b', 'y', 'c', 'x', 'd', 'w', 'e', 'v', 'f', 'u', 'g', 't', 'h',
               's', 'i', 'r', 'j', 'q', 'k', 'p', 'l', 'o', 'm', 'n', 'a', 'z'],
              ['y', 'c', 'x', 'd', 'w', 'e', 'v', 'f', 'u', 'g', 't', 'h', 's',
               'i', 'r', 'j', 'q', 'k', 'p', 'l', 'o', 'm', 'n', 'a', 'z', 'b'],
              ['c', 'x', 'd', 'w', 'e', 'v', 'f', 'u', 'g', 't', 'h', 's', 'i',
               'r', 'j', 'q', 'k', 'p', 'l', 'o', 'm', 'n', 'a', 'z', 'b', 'y'],
              ['x', 'd', 'w', 'e', 'v', 'f', 'u', 'g', 't', 'h', 's', 'i', 'r',
               'j', 'q', 'k', 'p', 'l', 'o', 'm', 'n', 'a', 'z', 'b', 'y', 'c'],
              ['d', 'w', 'e', 'v', 'f', 'u', 'g', 't', 'h', 's', 'i', 'r', 'j',
               'q', 'k', 'p', 'l', 'o', 'm', 'n', 'a', 'z', 'b', 'y', 'c', 'x'],
              ['w', 'e', 'v', 'f', 'u', 'g', 't', 'h', 's', 'i', 'r', 'j', 'q',
               'k', 'p', 'l', 'o', 'm', 'n', 'a', 'z', 'b', 'y', 'c', 'x', 'd'],
              ['e', 'v', 'f', 'u', 'g', 't', 'h', 's', 'i', 'r', 'j', 'q', 'k',
               'p', 'l', 'o', 'm', 'n', 'a', 'z', 'b', 'y', 'c', 'x', 'd', 'w'],
              ['v', 'f', 'u', 'g', 't', 'h', 's', 'i', 'r', 'j', 'q', 'k', 'p',
               'l', 'o', 'm', 'n', 'a', 'z', 'b', 'y', 'c', 'x', 'd', 'w', 'e'],
              ['f', 'u', 'g', 't', 'h', 's', 'i', 'r', 'j', 'q', 'k', 'p', 'l',
               'o', 'm', 'n', 'a', 'z', 'b', 'y', 'c', 'x', 'd', 'w', 'e', 'v'],
              ['u', 'g', 't', 'h', 's', 'i', 'r', 'j', 'q', 'k', 'p', 'l', 'o',
               'm', 'n', 'a', 'z', 'b', 'y', 'c', 'x', 'd', 'w', 'e', 'v', 'f'],
              ['g', 't', 'h', 's', 'i', 'r', 'j', 'q', 'k', 'p', 'l', 'o', 'm',
               'n', 'a', 'z', 'b', 'y', 'c', 'x', 'd', 'w', 'e', 'v', 'f', 'u'],
              ['t', 'h', 's', 'i', 'r', 'j', 'q', 'k', 'p', 'l', 'o', 'm', 'n',
               'a', 'z', 'b', 'y', 'c', 'x', 'd', 'w', 'e', 'v', 'f', 'u', 'g'],
              ['h', 's', 'i', 'r', 'j', 'q', 'k', 'p', 'l', 'o', 'm', 'n', 'a',
               'z', 'b', 'y', 'c', 'x', 'd', 'w', 'e', 'v', 'f', 'u', 'g', 't'],
              ['s', 'i', 'r', 'j', 'q', 'k', 'p', 'l', 'o', 'm', 'n', 'a', 'z',
               'b', 'y', 'c', 'x', 'd', 'w', 'e', 'v', 'f', 'u', 'g', 't', 'h'],
              ['i', 'r', 'j', 'q', 'k', 'p', 'l', 'o', 'm', 'n', 'a', 'z', 'b',
               'y', 'c', 'x', 'd', 'w', 'e', 'v', 'f', 'u', 'g', 't', 'h', 's'],
              ['r', 'j', 'q', 'k', 'p', 'l', 'o', 'm', 'n', 'a', 'z', 'b', 'y',
               'c', 'x', 'd', 'w', 'e', 'v', 'f', 'u', 'g', 't', 'h', 's', 'i'],
              ['j', 'q', 'k', 'p', 'l', 'o', 'm', 'n', 'a', 'z', 'b', 'y', 'c',
               'x', 'd', 'w', 'e', 'v', 'f', 'u', 'g', 't', 'h', 's', 'i', 'r'],
              ['q', 'k', 'p', 'l', 'o', 'm', 'n', 'a', 'z', 'b', 'y', 'c', 'x',
               'd', 'w', 'e', 'v', 'f', 'u', 'g', 't', 'h', 's', 'i', 'r', 'j'],
              ['k', 'p', 'l', 'o', 'm', 'n', 'a', 'z', 'b', 'y', 'c', 'x', 'd',
               'w', 'e', 'v', 'f', 'u', 'g', 't', 'h', 's', 'i', 'r', 'j', 'q'],
              ['p', 'l', 'o', 'm', 'n', 'a', 'z', 'b', 'y', 'c', 'x', 'd', 'w',
               'e', 'v', 'f', 'u', 'g', 't', 'h', 's', 'i', 'r', 'j', 'q', 'k'],
              ['l', 'o', 'm', 'n', 'a', 'z', 'b', 'y', 'c', 'x', 'd', 'w', 'e',
               'v', 'f', 'u', 'g', 't', 'h', 's', 'i', 'r', 'j', 'q', 'k', 'p'],
              ['o', 'm', 'n', 'a', 'z', 'b', 'y', 'c', 'x', 'd', 'w', 'e', 'v',
               'f', 'u', 'g', 't', 'h', 's', 'i', 'r', 'j', 'q', 'k', 'p', 'l'],
              ['m', 'n', 'a', 'z', 'b', 'y', 'c', 'x', 'd', 'w', 'e', 'v', 'f',
               'u', 'g', 't', 'h', 's', 'i', 'r', 'j', 'q', 'k', 'p', 'l', 'o'],
              ['n', 'a', 'z', 'b', 'y', 'c', 'x', 'd', 'w', 'e', 'v', 'f', 'u',
               'g', 't', 'h', 's', 'i', 'r', 'j', 'q', 'k', 'p', 'l', 'o', 'm']
              ]

    return matrix
