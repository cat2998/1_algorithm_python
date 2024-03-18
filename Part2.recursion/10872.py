def fact(n):
    # n이 1보다 작아질떄까지 = n=0이될떄까지 n-1을 돌리다가 return n?
    # 한번 fact1까지갔다가 다시 올라옴

    if n > 1:
        return n * fact(n - 1)

    else:
        return n


n = int(input())
if n != 0:
    print(fact(n))
else:
    print(1)
