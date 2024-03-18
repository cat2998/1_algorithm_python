# 1000으로 나눈 나머지를 구할 때
# 매번 모드 연산 시에 줄어드는 시간 복잡도에 대해 알아보아야 함.

n, b = tuple(map(int, input().split()))

matrix = [
    list(map(int, input().split()))
    for _ in range(n)
]

def calc(m1, m2):
    matrix2 = [
        [0]*n
        for _ in range(n)
    ]
    def calc2(m1, m2, x, y):
        num = 0
        for i in range(n):
            num += m1[x][i]*m2[i][y]
        return num%1000


    for i in range(n):
        for j in range(n):
            matrix2[i][j] = calc2(m1, m2, i, j)
    return matrix2

def divide_conquer(b):

    if b == 0:
        return 1
    
    if b == 1:
        return matrix
    
    m = divide_conquer(b//2)

    if b % 2 == 0:
        return calc(m, m)
    else:
        return calc(calc(m, m), matrix)
    

result = divide_conquer(b)

for i in result:
    for j in i:
        print(j%1000, end=" ")
    print()