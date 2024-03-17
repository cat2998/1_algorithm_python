import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

def binary_insert():
    for i in range(1, n):
        key = arr[i]

        pl = 0
        pr = i - 1

        while True:
            pc = (pl+pr)//2
            if arr[pc] == key:
                break

            elif arr[pc] < key:
                pl = pc + 1

            else:
                pr = pc - 1

            if pl > pr:
                break

        pd = pc + 1 if pl <= pr else pr + 1

        for j in range(i, pd, -1):
            arr[j] = arr[j-1]

        arr[pd] = key
        print(arr)

binary_insert()
