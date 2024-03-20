def is_han(num):
    num = str(num)
    diff = int(num[0]) - int(num[1])
    for i in range(1, len(num) - 1):
        if diff != int(num[i]) - int(num[i + 1]):
            return 0
    return 1

n = int(input())
count = 0
for num in range(1, n + 1):
    if num < 100:
        count = num
    else:
        count += is_han(num)
print(count)