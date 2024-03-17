import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

def shell_sort():
    h = 1
    while h < n//9:
        h = h*3 +1

    while h > 0:

        for i in range(h, n):
            j = i - h
            tmp = arr[i]
            while j >= 0 and arr[j] > tmp:
                arr[j+h] = arr[j]
                j -= h
            arr[j+h] = tmp
        h //= 3

shell_sort()

for i in arr:
    print(i)

