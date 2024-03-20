import sys


def input():
    return sys.stdin.readline()


# def richman(arr,  lf, rt):
#     global res
#     for i in range(333333333):
#         mid = (lf+rt)//2
#         if lf > rt:
#             break
#         cnt = 1
#         now = house[0]
#         for j in range(1, n):
#             if abs(-now+house[j]) >= mid:
#                 cnt += 1
#                 now = house[j]
#         if cnt >= m:
#             res = mid
#             return richman(arr, mid+1, rt)

#         if cnt < m:
#             return richman(arr, lf, mid-1)
#     return res


# res = 0

# n, m = map(int, input().split())
# house = [int(input()) for _ in range(n)]
# house.sort()
# print(richman(house, 1, house[-1] - house[0]))


n, m = map(int, input().split())
house = [int(input()) for _ in range(n)]
house.sort()

start, end, res= 0, house[n-1], 0
while start <= end:
    now=house[0]
    mid = (start+end)//2
    cnt = 1
    for i in range(1, n):
        if now+mid <= house[i]:
            now = house[i]
            cnt += 1
    if cnt >= m:
        res = mid
        start = mid+1
    else:
        end = mid-1
print(res)
