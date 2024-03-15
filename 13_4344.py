import sys
c = int(input())
for i in range(c):
    l = list(map(int, sys.stdin.readline().split()))
    sum = 0
    for j in l:
        sum += j
    avg = int((sum - l[0]) / (len(l) - 1))
    print("avg")
    student = 0
    for j in l:
        if (avg < j and j != l[0]):
            student += 1
    