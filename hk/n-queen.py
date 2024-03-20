n = int(input())

arr = [0]*n

flag_a = [False]*n
flag_b = [False]*(2*n+1)
flag_c = [False]*(2*n+1)

cnt = 0
def set(j):
    global cnt

    for i in range(n):
        if not flag_a[i] and not flag_b[i+j] and not flag_c[j-i+n-1]:
            arr[j] = i
            if j == n-1:
                cnt += 1
            else:
                flag_a[i] = flag_b[i+j] = flag_c[j-i+n-1] = True
                set(j+1)
                flag_a[i] = flag_b[i+j] = flag_c[j-i+n-1] = False

set(0)
print(cnt)
