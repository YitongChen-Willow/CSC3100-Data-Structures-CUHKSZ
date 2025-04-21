import math

def read_matrix(row):

    matrix = []
    for _ in range(row):
        info = list(map(int, input().split()))
        num = info[0]
        locate = []
        element = []
        for i in range(num):
            locate.append(info[1 + 2*i])
            element.append(info[2 + 2*i])
        matrix.append((locate, element))

    return matrix

def generate_seed(row):
     
    b = [1.0 / math.sqrt(row)] * row
    return b

def multiply(a, b, row_a):

    _b = [0.0] * row_a
    for i in range(row_a):
        loc_i, val_i = a[i]
        _row_b = 0
        for loc, val in zip(loc_i, val_i):
            _row_b += val * b[loc]
        _b[i] = _row_b
    return _b

row, col = map(int, input().split())
matrix_a = read_matrix(row)

b = generate_seed(row)
max_iterate = 1200
prev_eigen = float('-inf')
epsilon = 1e-4

for _ in range(max_iterate):

    Ab = multiply(matrix_a, b, row)
    current_eigen = sum(b[i] * Ab[i] for i in range(row))

    if abs(current_eigen - prev_eigen) < epsilon:
        break
    prev_eigen = current_eigen

    norm_Ab = math.sqrt(sum(i**2 for i in Ab))
    for i in range(row):
        b[i] = Ab[i] / norm_Ab

result = abs(current_eigen)
print("{0:.4f}".format(result))