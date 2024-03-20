# 팩토리얼
# 10! = 10 * 9! = 10 * 9 * 8!
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# 유클리드 호제법 (최대공약수 찾기)
def gcd(x, y):
    if (y == 0):
        return x
    return gcd(y, x % y)

# 하노이의 탑
# no : 옯겨야할 원반의 개수, x : 시작 기둥의 번호, y : 목표 기둥의 번호
def move(no, x, y):
    if (no == 1):
        print("원반 {0}를 {1}에서 {2}로 옮김".format(no, x, y))
    else:
        move(no - 1, x, 6-x-y)
        print("원반 {0}를 {1}에서 {2}로 옮김".format(no, x, y))
        move(no - 1, 6-x-y, y)

# 8퀸
pos = [False] * 8
flag_a = [False] * 8
flag_b = [False] * 15
flag_c = [False] * 15

def printQueen():
    for i in range(8):
        print(pos[i], end=" ")
    print()

def queen(i):
    cnt = 0
    for j in range(8):
        if  flag_a[j] == False and flag_b[i + j] == False and flag_c[i - j + 7] == False:
            pos[i] = j
            if i == 7:
                printQueen()
                cnt += 1
            flag_a[j] = flag_b[i + j] = flag_c[i - j + 7] = True
            cnt += queen(i + 1)
            flag_a[j] = flag_b[i + j] = flag_c[i - j + 7] = False
    return cnt

def is_check(i, j):
    flag = 1
    for k in range(i):
        if pos[k] == j or abs(pos[k] - j) == abs(k - i):
            flag = 0
    return flag

def queen2(i):
    cnt = 0
    for j in range(8):
        if is_check(i, j):
            pos[i] = j
            if i == 7:
                printQueen()
                cnt += 1
            else:
                cnt += queen2(i + 1)
    return cnt

# print(queen(0))
print(queen2(0))
print(factorial(10))
print(gcd(8, 22))
move(3, 1, 3)