import sys


def input():
    return sys.stdin.readline()


def sqsum(x, y, n):
    sqsumm = 0
    for i in range(x, x+n):
        for j in range(y, y+n):
            sqsumm += arr[i][j]
    return sqsumm


def quad(x, y, n):
    sq = sqsum(x, y, n)

    if sq == n**2:
        res.append(1)
        return
    elif sq == 0:
        res.append(0)
        return
    else:
        res.append('(')
        quad(x, y, n//2)
        quad(x, y+n//2, n//2)
        quad(x+n//2, y, n//2)
        quad(x+n//2, y+n//2, n//2)
        res.append(')')


n = int(input())
res = []
arr = [[int(char) for char in input().strip()] for _ in range(n)]
quad(0, 0, n)
print(*res, sep="")
