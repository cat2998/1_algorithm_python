import sys

n, m, l = tuple(map(int, sys.stdin.readline().split()))

shooter = list(map(int, sys.stdin.readline().split()))
shooter.sort()
animals = [
    tuple(map(int, sys.stdin.readline().split()))
    for _ in range(m)
]
cnt = 0
for x, y in animals:
    if y > l:
        continue
    distance = l - y
    target = x
    start = 0
    end = n-1

    while start <= end:
        
        mid = (start+end) // 2

        if shooter[mid] - distance <= target <= shooter[mid] + distance:
            cnt += 1
            break
        
        if shooter[mid] < target:
            start = mid + 1
        elif shooter[mid] > target:
            end = mid - 1

print(cnt)        

        