import sys

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
            
qsort(0, n-1)

for i in arr:
    print(i)