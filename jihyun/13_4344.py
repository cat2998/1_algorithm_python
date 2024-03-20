import sys
c = int(input())
for i in range(c):
    l = list(map(int, sys.stdin.readline().split()))
    avg = sum(l[1:]) / l[0]
    count = 0
    for z in l[1:]:
        if z > avg:
            count += 1
    print("{0:.3f}%".format((count / l[0]) * 100))