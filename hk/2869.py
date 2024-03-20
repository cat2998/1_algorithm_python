import math

A, B, V = tuple(map(int, input().split()))

day = A - B
days = math.ceil((V-A)/day) + 1
print(days)
