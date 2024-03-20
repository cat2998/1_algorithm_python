T = int(input())

for _ in range(T):
    n, word = tuple(input().split())

    P = ''
    for w in list(word):
        for _ in range(int(n)):
            P += w

    print(P)
