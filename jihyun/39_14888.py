import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
tmp = list(map(int, sys.stdin.readline().split()))

operator = []
operator_check = [0] * (n - 1)
pick_operator = [0] * (n - 1)

max_result = -1000000000
min_result = 1000000000

for i in range(4):
    for j in range(tmp[i]):
        operator.append(i)

def calculator(a, op, b):
    if op == 0:
        return a + b
    if op == 1:
        return a - b
    if op == 2:
        return a * b
    if op == 3:
        if a < 0:
            a *= -1
            return -1 * (a // b)
        return a // b

def pick(cnt):
    global max_result
    global min_result
    if cnt == n - 1:
        # print(pick_operator)
        result = a[0]
        for i in range(n - 1):
            result = calculator(result, pick_operator[i], a[i + 1])
        # print(result)
        max_result = max(max_result, result)
        min_result = min(min_result, result)
    else:
        for i in range(n - 1):
            if operator_check[i] == 0:
                operator_check[i] = 1
                pick_operator[cnt] = operator[i]
                pick(cnt + 1)
                operator_check[i] = 0

pick(0)
print(max_result)
print(min_result)