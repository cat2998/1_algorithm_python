n = int(input())

# n: 원판 개수 x: 시작 원판 y: 도착 원판

sequence = []
def hanoi(n, x, y):
    global cnt
    if n > 0:
        hanoi(n-1, x, 6-x-y)

        sequence.append([x, y])
        cnt += 1

        hanoi(n-1, 6-x-y, y)



def hanoi2(n, x, y):
    global cnt
    for _ in range(n):
        cnt *= 2

if n > 20:
    cnt = 1
    hanoi2(n, 1, 3)
    print(cnt-1)
else:
    cnt = 0
    hanoi(n, 1, 3)
    print(cnt)
    for s in sequence:
        A, B = s
        print(A, B)