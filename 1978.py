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

T = int(input())

for _ in range(T):
    sheet = list(map(int, input().split()))
    avg = sum(sheet[1:]) / sheet[0]
    people = 0
    for s in sheet[1:]:
        if s > avg:
            people += 1
    result = round(people/sheet[0]*100,3)
    print(f"{result:.{3}f}"+'%')