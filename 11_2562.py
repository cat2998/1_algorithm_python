index = 0
result = 0
for i in range(9):
    a = int(input())
    if (a > result):
        result = a
        index = i + 1
print(result)
print(index)