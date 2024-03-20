from itertools import combinations
import sys


def input():
    return sys.stdin.readline()
# itertools 사용함
# from itertools import permutations

# n = int(input())
# a = list(map(int, input().split()))

# max_val = 0
# curr_val = 0
# for perm in permutations(a, n):
#     for i in range(n-1):
#         curr_val += abs(perm[i]-perm[i+1])
#     max_val = max(max_val, curr_val)
#     curr_val=0

# print(max_val)

# perm구현함


def perm(arr, n):
    res = []
    if n == 0:
        return [[]]

    for i in range(len(arr)):
        elem = arr[i]
        for rest in perm(arr[:i]+arr[i+1:], n-1):
            res.append([elem]+rest)
    return res


n = int(input())
a = list(map(int, input().split()))

answer = 0
summ = 0
for per in perm(a, n):
    summ = sum(abs(per[i]-per[i+1]) for i in range(n-1))
    if summ > answer:
        answer = summ
    else:
        summ = 0

print(answer)
