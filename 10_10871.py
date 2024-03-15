n, x = map(int, input().split())
a = list(int(i) for i in input().split())
for i in a:
    if (i < x):
        print(i, end=" ")