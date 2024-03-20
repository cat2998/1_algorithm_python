
# def fsort(arr, max_arr=-1):
#     if max_arr == -1:
#         max_arr = max(arr)
#     f = [0]*(max_arr+1)
#     brr = [0]*n

#     for i in range(n):
#         f[arr[i]] += 1
#     for i in range(1, max_arr+1):
#         f[i] += f[i-1]
#     # stable하게만들기위해 뒷자리부터, f[arr[i]]때매 역순될수도있음
#     for i in range(n):
#         f[arr[i]] -= 1
#         brr[f[arr[i]]] = arr[i]
#     return brr

# n = int(input())
# arr = [int(input()) for _ in range(n)]
# n = len(arr)
# sorted_arr = fsort(arr)
# [print(i) for i in sorted_arr]


# def sort(arr):
#     for i in range(n):
#         chklst[arr[i]] += 1
#     for i in range(1, 10001):
#         if chklst[i] == 0:
#             print(i)

# n = int(input())
# arr = [int(input()) for _ in range(n)]
# chklst = [-1]*10001
# sorted_arr = sort(arr)


import sys


def input():
    return int(sys.stdin.readline())


def sort():
    chklst = [0]*10001
    n = input()

    for i in range(n):
        num = input()
        chklst[num] += 1

    for i in range(1, 10001):
        if chklst[i] != 0:
            [print(i) for _ in range(chklst[i])]


sort()
