import sys

f = [0] * 10001
n = int(sys.stdin.readline())

for i in range(n):
    f[int(sys.stdin.readline())] += 1

for i in range(len(f)):
    if f[i] != 0:
        for j in range(f[i]):
            print(i)

# l = [None] * 10000000
# print(sys.getsizeof(l))