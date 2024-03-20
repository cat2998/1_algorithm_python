import sys

n = int(sys.stdin.readline())

map = [0] * n
flag_a = [0] * n
flag_b = [0] * (n * 2 - 1)
flag_c = [0] * (n * 2 - 1)

result = 0

def queen(i):
    global result
    if i == n:
        result += 1
    else:
        for j in range(n):
            if flag_a[j] == 0 and flag_b[i + j] == 0 and flag_c[i - j + (n - 1)] == 0:
                map[i] = j
                flag_a[j] = flag_b[i + j] = flag_c[i - j + (n - 1)] = 1
                queen(i + 1)
                flag_a[j] = flag_b[i + j] = flag_c[i - j + (n - 1)] = 0

queen(0)
print(result)