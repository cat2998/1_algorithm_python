import sys

N, m = tuple(map(int, input().split()))

card = list(map(int, input().split()))


ans = []

res = sys.maxsize
def blackjack(n):
    global res
    if len(ans) == 3:
        if sum(ans) <= m:
            res = min(res, m - sum(ans))
        return
    
    if n >= N:
        return
    
    ans.append(card[n])
    blackjack(n+1)  
    ans.pop()

    blackjack(n+1)

blackjack(0)

print(m-res)