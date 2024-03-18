import sys
from itertools import permutations

n = int(sys.stdin.readline())
w = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

copy_n = [i for i in range(n)]
check_n = [0] * n
load = [None] * (n + 1)

result = 100000001

def check_cost():
    sum = 0
    for i in range(1, n + 1):
        # if w[load[i - 1]][load[i]] == 0:
        #     return -1
        sum += w[load[i - 1]][load[i]]
    # if w[load[n - 1]][load[0]] == 0:
    #     return -1
    # sum += w[load[n - 1]][load[0]]
    return sum

def pick(cnt, cost):
    global result
    if cnt == n:
        if w[load[cnt - 1]][load[0]] == 0:
            return
        else:
            load[cnt] = load[0]
            c = check_cost()
            print(load)
            print(c)
            result = min(result, c)
    else:
        for i in range(n):
            if check_n[i] == 0:
                load[cnt] = copy_n[i]
                if cnt != 0:
                    if w[load[cnt - 1]][load[cnt]] == 0:
                        # check_n[i] = 0
                        continue
                    cost += w[load[cnt - 1]][load[cnt]]
                    if result < cost:
                        # check_n[i] = 0
                        # cost -= w[load[cnt - 1]][load[cnt]]
                        continue
                check_n[i] = 1
                pick(cnt + 1, cost)
                check_n[i] = 0
                # if cnt != 0:
                #     cost -= w[load[cnt - 1]][load[cnt]]

pick(0, 0)
print(result)