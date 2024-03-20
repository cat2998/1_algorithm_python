n = int(input())
result = []

def move(no, x, y):
    if no == 1:
        if n <= 20:
            result.extend([x, y])
    else:
        move(no - 1, x, 6-x-y)
        if n <= 20:
            result.extend([x, y])
        move(no - 1, 6-x-y, y)

move(n, 1, 3)
print(len(result) // 2)
if n <= 20:
    for i in range(0, len(result) - 1, 2):
        print("{0} {1}".format(result[i], result[i + 1]))