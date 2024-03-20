import sys

result = sys.maxsize

n = int(sys.stdin.readline())
l = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

l = sorted(l, key = lambda x : l[x])
print(l)

def div(n, left, right):
    if n == 2:
        return (l[left][0] - l[right][0]) ** 2 + (l[left][1] - l[right][1]) **2
    else:
        result_1 = div(n//2, left, right - n//2)
        result_2 = div(n//2, left + n//2, right)
        print(result_1, result_2)
        return min(result_1, result_2)

print(div(n, 0, n - 1))