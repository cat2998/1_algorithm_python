import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))

check_l = [0] * n
pick = [None] * n
result = 0

def result_sum():
    sum = 0
    for i in range(2, n + 1):
        sum += abs(pick[i-2] - pick[i-1])
    return sum

def shuffle(cnt):
    global result
    if cnt == n:
        sum = result_sum()
        result = max(result, sum)
    else:
        for i in range(n):
            if check_l[i] == 0:
                check_l[i] = 1
                pick[cnt] = l[i]
                shuffle(cnt + 1)
                check_l[i] = 0

shuffle(0)
print(result)