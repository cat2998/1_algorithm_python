n, m = tuple(input().split())

p, q = '', ''
for i in range(2,-1,-1):
    p += n[i]
    q += m[i]

print(max(int(p), int(q)))