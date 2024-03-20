import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

def select_sort():
    min = 0
    k = 0
    while k < n-1:
        min = k
        for i in range(k+1, n):
            if arr[i] < arr[min]:
                min = i

        arr[k], arr[min] = arr[min], arr[k]
        k += 1

select_sort()
for i in arr:
    print(i)