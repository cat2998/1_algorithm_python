import math

def is_prime(num):
    if num == 1:
        return 0
    if num == 2:
        return 1
    for i in range(2, math.ceil(math.sqrt(num)) + 1):
        if num % i == 0:
            return 0
    return 1

n = int(input())
l = list(int(i) for i in input().split())
count = 0
for num in l:
    count += is_prime(num)
print(count)