def cardselec(col):
    if col == k:
        # 이거 왜 ' '하면안되고 '' ㅏㅎ면되지??okok 
        sols.add(''.join(list(map(str, temp))))
        return
    for i in range(n):
        if chk[i] == 1:
            continue
        chk[i] = 1
        temp.append(cards[i])
        cardselec(col+1)
        temp.pop()
        chk[i] = 0


n = int(input())
k = int(input())
cards = []
temp = []
chk = [-1]*n
sols = set()
for i in range(n):
    cards.append(int(input()))
cardselec(0)
print(len(sols))

# 이게 틀임
# def cardselec(col)
#     if k = len of temp
#         sols.add(temp)
#     for i in range(n)
#         if ckh[i]==1:
#             continue
#         chk[i]==1
#         temp.append(cards[i])
#         cardselec(col+1)
#         temp.pop()
#         chk[i]==0
        

# n=int(input())
# k=int(n)
# cards
# sols
# temp
# chk
