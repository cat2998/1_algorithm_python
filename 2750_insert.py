import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

def insert_sort():
    
    for i in range(1, n):
        j = i
        tmp = arr[i]
        while j > 0 and arr[j-1] > tmp:
            arr[j] = arr[j-1]
            j -= 1             

        arr[j] = tmp 

insert_sort()

for i in arr:
    print(i)