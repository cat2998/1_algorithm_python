N = 9

ans, idx = 0, 0
for i in range(1, N+1):
    n = int(input())
    if ans < n:
        ans = n
        idx = i

print(ans)
print(idx)