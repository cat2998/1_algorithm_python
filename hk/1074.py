N, r, c = tuple(map(int, input().split()))

cnt = ans = 0

# def partition(n, x, y):
#     global cnt, ans
#     if ans != 0:
#         return
#     dxs, dys = [0, 0, 1, 1], [0, 1, 0, 1]
#     if n > 1:
#         for dx, dy in zip(dxs, dys):
#             nx, ny = x+dx*(2**(n-1)), y+dy*(2**(n-1))
#             partition(n-1, nx, ny)

#     else:
#         for dx, dy in zip(dxs, dys):
#             nx, ny = x + dx, y + dy
#             cnt += 1
#             if nx == r and ny == c:
#                 ans = cnt
#                 return
#partition(N, 0, 0)

def partition(n, x, y):
    global cnt
    if n == 2:
        dxs, dys = [0, 0, 1, 1], [0, 1, 0, 1]
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if nx == r and ny == c:
                print(cnt)
                return
            cnt += 1
        return
        
    if not ((x <= r and x + n >= r) and (y <= c and y+n >= c)):
        cnt += int(n*n)
        return
    partition(n/2, x, y)
    partition(n/2, x, y + n/2)
    partition(n/2, x + n/2, y)
    partition(n/2, x + n/2, y + n/2)

partition(2**N, 0, 0)


# n, r, c = map(int, input().split())
# a, p = 0, 1
# for i in range(n):
#     a += p * (2 * (r % 2) + (c % 2))
#     p *= 4
#     r //= 2
#     c //= 2
# print(a)