import sys

n, b = map(int, sys.stdin.readline().split())
matirx = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

def matrix_multi(a, b):
    tmp = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                tmp[i][j] += a[i][k] * b[k][j] % 1000
            tmp[i][j] = tmp[i][j] % 1000
    return tmp


def matrix_power(m, b):
    if b == 1:
        for i in range(n):
            for j in range(n):
                m[i][j] = m[i][j] % 1000
        return m
    else:
        x = matrix_power(m, b//2)
        if b % 2 == 0:
            return matrix_multi(x, x)
        else:
            return matrix_multi(matrix_multi(x, x), m)

m = matrix_power(matirx, b)
for i in range(n):
    for j in range(n):
        print(m[i][j], end=" ")
    print()