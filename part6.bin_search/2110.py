import sys


def input():
    return sys.stdin.readline()


def richman(arr, obj, lf, rt):
    if obj == mid:
        return mid
    mid = (lf+rt)//2
    if obj > mid:
        return richman(arr, obj, mid+1, rt)
    if obj < mid:
        return richman(arr, obj, lf, mid-1)


n, m = map(int, input().split())
house = [int(input()) for _ in range(n)]
richman(house, distance, 0, house[n-1])
