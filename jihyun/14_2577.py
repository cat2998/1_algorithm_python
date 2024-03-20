a = int(input())
b = int(input())
c = int(input())
mul = str(a * b * c)
l = list(int(0) for i in range(10))
for m in mul:
    l[int(m)] += 1
for i in l:
    print(i)