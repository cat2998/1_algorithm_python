T = int(input())

num = list(map(int, input().split()))
cnt = 0
for i in range(T):
    if num[i] == 2:
        cnt += 1
    else:
        for j in range(2, num[i]):
            if num[i] % j == 0:
                break
            if num[i] == j+1:
                cnt += 1
print(cnt)