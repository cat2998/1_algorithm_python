
import sys


def input():
    return sys.stdin.readline()


a, b, c = map(int, input().split())


def power(a, n):
    if n == 1:
        return a % c
    else:
        temp = power(a, n//2)
        if n % 2 == 0:
            return (temp **2) % c
        else:
            return ((temp **2) * a) % c


print(power(a, b))
