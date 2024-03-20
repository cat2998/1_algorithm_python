import sys


def input():
    return sys.stdin.readline()

# def hei(a):
#     return -len(a)*h+sum(a)


# n, m = list(map(int, input().split()))
# forest = list(map(int, input().split()))
# forest.sort()
# for h in range(forest[n-1]-1, forest[0], -1):
#     for i in range(n):
#         if h < forest[i]:
#             if hei(forest[i:]) == m:
#                 print(h)
#             break
# ----------------
# def forest():
#     n, m = map(int, input().split())
#     trees = list(map(int, input().split()))
#     trees.sort(reverse=True)
#     ans = 0
#     std = trees[0]
#     k = 0  #현재인덱스
#     while k < len(trees) - 1:
#         if ans >= m:
#             print(std)
#             return
    # 맞을떄까지 계속 1씩 낮추는
#         if (trees[k] - trees[k + 1]) * (k + 1) >= m - ans:
#             if (m - ans) % (k + 1) == 0:
#                 std -= (m - ans) // (k + 1)
#             else:
#                 std -= (m - ans) // (k + 1) + 1
#             ans = m
#         else:
#             ans += (trees[k] - trees[k + 1]) * (k + 1)
#             std = trees[k + 1]
#         k += 1

#     if (m - ans) % (k + 1) == 0:
#         std -= (m - ans) // (k + 1)
# #     else:
# #         std -= (m - ans) // (k + 1) + 1

# #     print(std)

# def environmet(arr, height):
#     i = 0
#     while arr[i] < height:
#         i += 1
#     del arr[i:]
#     return arr

# def integrated():
#     summ = 0
#     k = 1
#     for i in range(arr_n[0]-1, 0, -1):
#         summ += k
#         if i in arr_n:
#             k = k+1
#         if summ >= m:
#             break
#     return i
# n, m = map(int, input().split())
# arr_n = list(map(int, input().split()))
# arr_n.sort(reverse=True)

# print(integrated())

# def forest():
#     n, m = map(int, input().split())
#     trees = list(map(int, input().split()))
#     trees.sort(reverse=True)
#     ans = 0
#     std = trees[0]
#     k = 0  # 현재인덱스
#     while k < len(trees) - 1:
#         if ans >= m:
#             print(std)
#             return
#         if (trees[k] - trees[k + 1]) * (k + 1) >= m-ans:
#             if (m-ans) % (k+1) == 0:
#                 std -= (m-ans) // (k+1)
#             else:
#                 std -= (m-ans) // (k+1)+1
#             ans = m
#         else:
#             ans += (trees[k] - trees[k + 1]) * (k + 1)
#             std = trees[k + 1]
#         k += 1

#     if (m - ans) % (k + 1) == 0:
#         std -= (m - ans) // (k + 1)
#     else:
#         std -= (m - ans) // (k + 1) + 1

#     print(std)


# forest()

def cutting_professional(arrr, height):
    a = 0
    for i in range(n):
        if arrr[i] > height:
            a += arrr[i]-height
    return a


def bin_section(forest, obj, lf, rt):
    if lf > rt:
        return rt
    mid = (lf+rt) // 2
    sbj = cutting_professional(forest, mid)
    if sbj == obj:
        return mid
    elif sbj > obj:
        return bin_section(forest, obj, mid+1, rt)
    elif sbj < obj:
        return bin_section(forest, obj, lf, mid-1)


n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
print(bin_section(arr, m, 0, arr[n-1]-1))
