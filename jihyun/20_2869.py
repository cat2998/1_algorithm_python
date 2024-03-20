a, b, v = map(int, input().split())
answer = 0
if a >= v:
    answer = 1
else:
    goal = v - a
    climb = a - b
    if goal <= climb:
        answer = 2
    else:
        if goal % climb == 0:
            answer = goal // climb + 1
        else:
            answer = goal // climb + 2
print(answer)