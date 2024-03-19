import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))

l.sort()

pl = 0
pr = n - 1
answer = abs(l[pl] + l[pr])
answer_pl = l[pl]
answer_pr = l[pr]

while True:
    if pl >= pr:
        break
    if answer > abs(l[pl] + l[pr]):
        answer = abs(l[pl] + l[pr])
        answer_pl = l[pl]
        answer_pr = l[pr]
    if l[pl] + l[pr] <= 0:
        pl += 1
    elif l[pl] + l[pr] > 0:
        pr -= 1

print(answer_pl, answer_pr)