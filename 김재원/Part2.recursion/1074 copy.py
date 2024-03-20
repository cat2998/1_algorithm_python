def calculate_x_and_y(n):
    if n == 1:
        return 0, 0
    
    # x 계산
    x = (2**(2*n) - 1) % 2
    
    # y 계산
    y = (2**(2*n) - 1) - 2**(2*(n-1)-1)
    
    # 재귀적으로 다음 값을 계산
    x1, y1 = calculate_x_and_y(n - 1)
    
    # 남은 값이 1이 될 때까지 반복
    while y1 != 1:
        # x1과 y1을 다시 계산
        x1, y1 = calculate_x_and_y(n - 1)
    
    return x, y

# 테스트
x, y = calculate_x_and_y(4)
print("x:", x)
print("y:", y)
