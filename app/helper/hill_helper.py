import numpy as np

def find_adjugate(matrix):
    adj = np.array([[0 for _ in range(3)] for _ in range(3)])
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            comp_i = find_comp(i)
            comp_j = find_comp(j)
            a, b, c, d = matrix[comp_i[0]][comp_j[0]], matrix[comp_i[0]][comp_j[1]], matrix[comp_i[1]][comp_j[0]], matrix[comp_i[1]][comp_j[1]]
            m = -1 if (i+j) in [1, 3] else 1
            adj[i][j] = m * (a*d-b*c)
    return np.transpose(adj)
            
def find_comp(i):
    a = [0,1,2]
    a.remove(i)
    return a 

def fraction_mod(a,b):
    i = 1
    while(True):
        if (i*a) % b == 1:
            return i
        else:
            i+=1

def hill_inverse(matrix):
    det = int(np.linalg.det(matrix) % 26)
    mult = fraction_mod(det, 26)
    adjugate = find_adjugate(matrix)
    adjugate *= mult
    adjugate %= 26
    return adjugate

def create_hill_key(key):
    key_matrix = np.array(list(map(int,key.split())))
    key_matrix = np.reshape(key_matrix, (3,3))
    return key_matrix

# if __name__ == "__main__":
    # test = np.array([[17, 17, 5],[21,18,21],[2,2,19]])
    # key_string = "17 17 5 21 18 21 2 2 19"
    # print(create_hill_key(key_string))
    # print(hill_inverse(test))
    # print(find_adjugate(test))
    
    # print(fraction_mod(23,26))