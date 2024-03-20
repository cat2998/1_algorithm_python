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

t = int(input())
for i in range(t):
    n = int(input())
    a = n // 2
    for x in range(a, 0, -1):
        if is_prime(x) and is_prime(n - x):
            print(min(x, n - x), end=" ")
            print(max(x, n - x))
            break