n = int(input())

pos = [0]*n
flag_a = [False]*n
flag_b = [False]*(2*n+1)
flag_c = [False]*(2*n+1)

cnt = 0
def set(i):
    global cnt
    for j in range(n):
        if (not flag_a[j] and not flag_b[i+j] and not flag_c[i-j+n-1]):
            pos[i] = j
            if i == n-1:
                cnt += 1
            else:
                # 격자점을 행을 x좌표로 열을 y좌표로 한 다음 오른쪽대각선은 x+y,
                # 왼쪽 대각선은 y-x인데 -7~7까지의 값이 나오기 때문에 공통의 격자점에서
                # 대각선의 값이 동일한 값이 나오도록 하기 위해서 +7을 해주는 것.
                flag_a[j] = flag_b[i+j] = flag_c[i-j+n-1] = True
                set(i+1)
                flag_a[j] = flag_b[i+j] = flag_c[i-j+n-1] = False


set(0)
print(cnt)