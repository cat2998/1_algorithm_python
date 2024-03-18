import sys

l = list(int(sys.stdin.readline()) for i in range(9))
check_l = [0] * 9

result = []
flag = 1

def pick(cnt, start):
    global flag
    if flag:
        if cnt == 0:
            if sum(result) == 100:
                flag = 0
                result.sort()
                for i in result:
                    print(i)
        else:
            for i in range(start, 9):
                if check_l[i] == 0:
                    check_l[i] = 1
                    result.append(l[i])
                    pick(cnt - 1, i)
                    check_l[i] = 0
                    result.pop()

pick(7, 0)