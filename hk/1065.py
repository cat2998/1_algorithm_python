n = int(input())

cnt = 0
for i in range(1,n+1):
    if i < 100:
        cnt += 1
    else:
        n1 = i%10
        n3 = i//100
        n2 = i//10 - n3*10
        if n3 - n2 == n2 - n1:
            cnt += 1
print(cnt)
        

