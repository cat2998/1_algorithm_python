import sys

n, r, c = map(int, sys.stdin.readline().split())
num = 0

# n: 한변의 길이
def visit(n, x, y):
    global num
    if not(x <= r <= x + n and y <= c <= y + n):
        num += n * n
        return

    if n == 2:
        dxs, dxy = [0, 0, 1, 1], [0, 1, 0, 1]
        for dx, dy in zip(dxs, dxy):
            if r == x + dx and c == y + dy:
                print(int(num))
                exit(0)
            num += 1
        return

    visit(n/2, x, y)
    visit(n/2, x, y + n/2)
    visit(n/2, x + n/2, y)
    visit(n/2, x + n/2, y + n/2)

visit(2 ** n, 0, 0)