import sys

n = int(sys.stdin. readline())
l = set(sys.stdin.readline().strip() for i in range(n))

l = sorted(l, key=lambda x : (len(x), x))

for i in l:
    print(i)