T = int(input())

for _ in range(T):
    sheet = list(input())
    score, grade = 0, 0
    for q in sheet:
        if q == "O":
            score += 1
            grade += score
        else:
            score = 0
    print(grade)