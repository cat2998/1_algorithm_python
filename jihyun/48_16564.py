import sys

n, k = map(int, sys.stdin.readline().split())
l = [int(sys.stdin.readline()) for i in range(n)]

l.sort()

left = l[0]
right = l[n - 1] + k
while True:
    center = (left + right) // 2
    sum = 0
    for i in l:
        if i < center:
            sum += center - i
    if sum > k:
        right = center -1
    elif sum <= k:
        left = center + 1
    if left > right:
        break
    
print(right)
    