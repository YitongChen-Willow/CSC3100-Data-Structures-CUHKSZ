def read_matrix(row):

    matrix = []
    for _ in range(row):
        info = list(map(int, input().split()))
        num = info[0]
        row_cont = {}
        for i in range(num):
            locate = info[1 + 2*i]
            element = info[2 + 2*i]
            row_cont[locate] = element
        matrix.append(row_cont)

    return matrix

def multiply_matrix(a, b, row_a, col_b):

    matrix_c = []
    for i in range(row_a):
        row_c = {}
        for col_a in a[i]:
            for col_b in b[col_a]:
                total = (a[i][col_a])*(b[col_a][col_b])
                row_c[col_b] = row_c.get(col_b, 0) + total
        row_c = {l:v for l,v in row_c.items() if v != 0}
        matrix_c.append(row_c)
    return matrix_c
 
def print_matrix(matrix, row, col):

    print(row, col)
    for r in matrix:
        if not r:
            print(0)
        else:
            output = [str(len(r))]
            for loc, value in sorted(r.items()):
                output.extend([str(loc), str(value)])
            print(" ".join(output))

row_a, col_a = map(int, input().split())
matrix_a = read_matrix(row_a)

blank = input()

row_b, col_b = map(int, input().split())
matrix_b = read_matrix(row_b)

matrix_c = multiply_matrix(matrix_a, matrix_b, row_a, col_b)
print_matrix(matrix_c, row_a, col_b)
