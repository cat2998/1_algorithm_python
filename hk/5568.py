n = int(input())
k = int(input())

card = []
for i in range(n):
    num = input()

    card.append(num)

ans = []
used = [False]*n
integer = []
def backtrack():
    if len(integer) >= k:
        ans.append(''.join(integer))
        return
    
    for i in range(n):
        if not used[i]:
            integer.append(card[i])
            used[i] = True
            backtrack()
            used[i] = False
            integer.pop()

backtrack()
print(len(set(ans)))

