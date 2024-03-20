import sys

n = int(sys.stdin.readline())
w = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

check_n = [0] * n
load = [None] * (n + 1)

result = 100000001

def pick(cnt, cost):
    global result
    if cnt == n:
        if w[load[cnt - 1]][load[0]] == 0:
            return
        else:
            load[cnt] = load[0]
            cost += w[load[cnt - 1]][load[cnt]]
            result = min(result, cost)
    else:
        for i in range(n):
            tmp = cost
            if check_n[i] == 0:
                load[cnt] = i
                if cnt != 0:
                    if w[load[cnt - 1]][load[cnt]] == 0:
                        continue
                    tmp += w[load[cnt - 1]][load[cnt]]
                    if result < tmp:
                        continue
                check_n[i] = 1
                pick(cnt + 1, tmp)
                check_n[i] = 0

pick(0, 0)
print(result)