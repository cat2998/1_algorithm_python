import sys

n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))

def is_check(x):
    pl = 0
    pr = n - 1
    while True:
        pc = (pl + pr) // 2
        if n_list[pc] == x:
            return 1
        if n_list[pc] < x:
            pl = pc + 1
        elif x < n_list[pc]:
            pr = pc - 1
        if pl > pr:
            break
    return 0

n_list.sort()
for i in range(m):
    if is_check(m_list[i]):
        print(1)
    else:
        print(0)