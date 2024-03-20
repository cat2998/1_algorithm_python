import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

buff = [None]*n
def merge_sort(left, right):

    if left < right:
        center = (left+right)//2

        merge_sort(left, center)
        merge_sort(center+1, right)

        p = k = 0
        i = j = left    
        while i <= center:
            buff[p] = arr[i]
            p += 1
            i += 1

        while i <= right and k < p:
            if arr[i] < buff[k]:
                arr[j] = arr[i]
                i += 1
            else:
                arr[j] = buff[k]
                k += 1
            j += 1

        while k < p:
            arr[j] = buff[k]
            j += 1
            k += 1

merge_sort(0, n-1)

for i in arr:
    print(i)

    
