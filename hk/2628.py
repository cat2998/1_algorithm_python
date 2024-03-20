n, m = tuple(map(int, input().split()))

x = [0]*n
y = [0]*m

t = int(input())

for _ in range(t):
    p, q = tuple(map(int, input().split()))
    if p == 0:
        y[q-1] = 1
    else:
        x[q-1] = 1

xlist = []
cnt = 0
for i in range(len(x)):
    if x[i] == 1:
        cnt += 1
        xlist.append(cnt)
        cnt = 0
    elif i == len(x)-1:
        cnt += 1
        xlist.append(cnt)
    else:
        cnt += 1

ylist = []
cnt = 0
for i in range(len(y)):
    if y[i] == 1:
        cnt += 1
        ylist.append(cnt)
        cnt = 0
    elif i == len(y)-1:
        cnt += 1
        ylist.append(cnt)
    else:
        cnt += 1

print(max(xlist)*max(ylist))