n = int(input())
k = int(input())
l = list(input() for i in range(n))
l_check = list(0 for i in range(n))
pick = []
result = set()

def choice(cnt):
    if cnt == 0:
        st = ""
        for i in pick:
            st += str(i)
        result.add(st)
    else:
        for i in range(n):
            if l_check[i] == 0:
                l_check[i] = 1
                pick.append(l[i])
                choice(cnt - 1)
                l_check[i] = 0
                pick.pop()

choice(k)
print(len(result))