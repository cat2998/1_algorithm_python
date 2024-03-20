# dx dy 찾아보기 [0 0 1 1] [0 1 0 1]
# dxdy 용법 dfs 핦 대

    # x랑 y에 sqn 더하면 밖으로나감 ..
def z_find(x, y, sqn):
    global cnt
    if not (x <= r < x+sqn and y <= c < y+sqn):
        cnt += sqn**2
        return
    if sqn > 2:
        sqn //= 2
        z_find(x, y, sqn)
        z_find(x, y+sqn, sqn)
        z_find(x+sqn, y, sqn)
        z_find(x+sqn, y+sqn, sqn)
    else:
        if x == r and y == c:
            print(cnt)
        elif x == r and y+1 == c:
            print(cnt+1)
        elif x+1 == r and y == c:
            print(cnt+2)
        else:
            print(cnt+3)
        return


n, r, c = map(int, input().split())
cnt = 0
z_find(0, 0, 2**n)
