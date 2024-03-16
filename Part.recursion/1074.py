# 블럭 옮길때마다 2^(n-1)씩 더해주면됨
# n커질떄마다 2^n씩 행렬간이동함
# 계속 돌다가 cr 만족하면 idx출력
def reached(c, r):
    if init_pos[0] == c and init_pos[1] == r:
        return True
    False


def move_micro(c, r):
    global idx
    for j in range(3):
        init_pos[0] += move_z[j][0]
        init_pos[1] += move_z[j][1]
        idx += 1
        if reached(c, r):
            return idx


def move_macro(n, c, r):
    global division
    for i in range(n-1):
        if n == 0:
            move_micro(c, r)
        else:
            division[n] += 1
            n=int(n/2)
            move_macro(n, c, r)


idx = 0
n, c, r = map(int, (input()).split())
division = [0]*n
init_pos = [0, 0]
move_z = [[1, 0], [-1, 1], [1, 0]]
move_micro(c, r)
print(idx)
