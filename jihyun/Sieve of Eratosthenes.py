# 1 ~ 100

l = list(int(i) for i in range(0, 101))
l[0] = l[1] = 0
for x in l:
    if x != 0:
        i = 2
        while (x * i <= len(l)):
            l[x * i] = 0
            i += 1

cnt = 0
for x in l:
    if x != 0:
        print(x)
        cnt += 1
print(cnt)