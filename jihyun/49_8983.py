import sys

m, n, l = map(int, sys.stdin.readline().split())
m_list = list(map(int, sys.stdin.readline().split()))
n_list = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

m_list.sort()

result = 0

for i in range(n):
    x, y = n_list[i][0], n_list[i][1]
    left = 0
    right = m - 1
    while True:
        if left > right:
            break
        center = (left + right) // 2
        mx = m_list[center]
        if abs(mx - x) + y <= l:
            result += 1
            break
        elif abs(mx - x) + y > l:
            if mx > x:
                right = center - 1
            else:
                left = center + 1

print(result)