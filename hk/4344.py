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
