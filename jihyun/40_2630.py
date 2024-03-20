import sys

n = int(sys.stdin.readline())
map = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

result_white = 0
result_blue = 0

def is_same_check(n, x, y):
    for i in range(n):
        for j in range(n):
            if map[x][y] != map[x + i][y + j]:
                return 0
    return 1

# n: 한변의 길이
def div(n, x, y):
    global result_blue
    global result_white
    if is_same_check(n, x, y):
        if map[x][y] == 1:
            result_blue += 1
        else:
            result_white += 1
    else:
        div(n//2, x, y)
        div(n//2, x + n//2, y)
        div(n//2, x, y + n//2)
        div(n//2, x + n//2, y + n//2)

div(n, 0, 0)
print(result_white)
print(result_blue)