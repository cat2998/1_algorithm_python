a = int(input())
b = int(input())

n1 = b%10
n2 = (b%100) // 10
n3 = (b // 100)

ans = 0
for i in [n1, n2, n3]:
    print(a*i)
    ans += a*i

print(a*b)