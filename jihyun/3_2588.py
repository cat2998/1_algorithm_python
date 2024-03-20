a = int(input())
b = str(input())
i = 0
result = 0
for x in reversed(b):
    c = a * int(x)
    result = result + (c * (10 ** i))
    i += 1
    print(c)
print(result)