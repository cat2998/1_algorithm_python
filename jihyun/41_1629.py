import sys
sys.setrecursionlimit(10**8)

a, b, c = map(int, sys.stdin.readline().split())

def power(a, b, c):
    if b == 0:
        return 1
    else:
        x = power(a, b//2, c)
        if b % 2 == 0:
            return x * x % c
        else:
            return x * x % c * a % c

print(power(a, b, c))