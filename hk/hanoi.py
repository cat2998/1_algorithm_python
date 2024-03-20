
#no:원반 개수, x: 시작 기둥, y: 목표 기둥
def hanoi(no, x, y):
    if no > 1:
        hanoi(no-1, x, 6-x-y)

    print(f"원반{no}을 기둥{y}로 옮깁니다.")

    if no > 1:
        hanoi(no-1, 6-x-y, y)

hanoi(3, 1, 3)