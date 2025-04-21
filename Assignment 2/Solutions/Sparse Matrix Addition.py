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

def add_matrix(a, b, row):

    matrix_c = []
    for i in range(row):
        row_a = a[i] 
        row_b = b[i] 
        row_c = {}
        cols = sorted(set(row_a.keys()).union(row_b.keys()))
        for j in cols:
            if (j in row_a) and (j in row_b):
                total = row_a[j] + row_b[j]
                if total != 0:
                    row_c[j] = total
            elif (j in row_a):
                row_c[j] = row_a[j]
            elif (j in row_b):
                row_c[j] = row_b[j]
        matrix_c.append(row_c)
    return matrix_c

def print_matrix(matrix, row, col):

    print(row, col)
    for r in matrix:
        if not r:
            print(0)
        else:
            output = [str(len(r))]
            for loc, value in r.items():
                output.extend([str(loc), str(value)])
            print(" ".join(output))

row_a, col_a = map(int, input().split())
matrix_a = read_matrix(row_a)

blank = input()

redundant = input()
matrix_b = read_matrix(row_a)

matrix_c = add_matrix(matrix_a, matrix_b, row_a)
print_matrix(matrix_c, row_a, col_a)