import sys

n = int(sys.stdin.readline())
arr = [[] for _ in range(52)]
for _ in range(n):
    word = input()
    arr[len(word)].append(word)

def merge_sort(left, right):
    if left < right:
        center = (left+right) // 2

        merge_sort(left, center)
        merge_sort(center+1, right)

        p = k = 0
        i = j = left

        while i <= center:
            buff[p] = arr2[i]
            p += 1
            i += 1

        while k < p and i <= right:
            if buff[k] <= arr2[i]:
                arr2[j] = buff[k]
                k += 1
            else:
                arr2[j] = arr2[i]
                i += 1
            j += 1
        
        while k < p:
            arr2[j] = buff[k]
            j += 1
            k += 1
 
for i in arr:
    if len(i) > 0:
        buff = [None]*(len(i))
        arr2 = ['']*(len(i))
        for j in range(len(i)):
            arr2[j] = i[j]
        arr2 = list(set(arr2))
        merge_sort(0, len(arr2)-1)
        for k in arr2:
            print(k)