import sys


def input():
    return sys.stdin.readline()


def sqsum(x, y, n):
    sqsum = 0
    for i in range(x, x+n):
        for j in range(y, y+n):
            sqsum += arr[i][j]
    return sqsum


def divide(x, y, n):
    global bidx, widx
    if sqsum(x, y, n) == n**2:
        bidx += 1
        return
    elif sqsum(x, y, n) == 0:
        widx += 1
        return
    else:
        divide(x, y, n//2)
        divide(x, y+n//2, n//2)
        divide(x+n//2, y, n//2)
        divide(x+n//2, y+n//2, n//2)


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

widx, bidx = 0, 0

divide(0, 0, n)

print(widx, bidx, sep="\n")
