import sys

n, c = map(int, sys.stdin.readline().split())
l = list(int(sys.stdin.readline()) for i in range(n))

l.sort()

if c == 2:
    print(l[n - 1] - l[0])
else:
    length = l[n - 1] - l[0]
    left = 1
    right = length

    while True:
        cnt = 1
        center = (left + right) // 2
        start = l[0]
        for i in range(1, n):
            if start + center <= l[i]:
                cnt += 1
                start = l[i]
        if cnt < c:
            right = center - 1
        if cnt >= c:
            left = center + 1
        if left > right:
            print(right)
            break