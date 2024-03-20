import sys

n, m = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))

pick_card = [None] * 3
result = 0

def pick(depth, start):
    global result
    if depth == 3:
        if sum(pick_card) <= m:
            result = max(result, sum(pick_card))
    else:
        for i in range(start, n):
            pick_card[depth] = l[i]
            pick(depth + 1, i + 1)

pick(0, 0)
print(result)