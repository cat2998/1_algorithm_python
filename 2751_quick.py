import sys

# 최악의 경우 정렬된 배열에서 피봇이 양 끝이면 퀵 정렬은 O(N^2)이 걸린다.
# N이 최대 1,000,000이므로 nlogn일 경우 약 2천만이다.
# 이 문제는 2초가 주어졌으므로 약 2억개의 연산 수행이 제한이다.

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))


def sort_center(first, second, third):
    if arr[first] > arr[second]: arr[first], arr[second] = arr[second], arr[first]
    if arr[second] > arr[third]: arr[third], arr[second] = arr[second], arr[third]
    if arr[first] > arr[second]: arr[first], arr[second] = arr[second], arr[first]
    return second
    

def qsort(left, right):
    pl = left
    pr = right
    m = sort_center(left, (left+right)//2, right)
    x = arr[m]

    while pl <= pr:
        while arr[pl] < x: pl += 1
        while arr[pr] > x: pr -= 1

        if pl <= pr:
            arr[pl], arr[pr] = arr[pr], arr[pl]
            pl += 1
            pr -= 1
    
    if left < pr:
        qsort(left, pr)
    if right > pl:
        qsort(pl, right)
            

if arr[0] > arr[1]:
    for i in range(1, n):
        if arr[i] > arr[i-1]:
            break

else:
    for i in range(1, n):
        if arr[i] < arr[i-1]:
            break

# if i != n-1:
#     arr.sort()
#     for i in arr:
#         print(i)
# else:
#     if arr[0] > arr[1]:
#         for i in range(n-1, -1, -1):
#             print(arr[i])
#     else:
#         for i in arr:
#             print(i)


arr.sort()
for i in arr:
    print(i)