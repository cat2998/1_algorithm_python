n = int(input())

pos = [False] * n
flag_a = [False] * n
flag_b = [False] * (2 * n - 1)
flag_c = [False] * (2 * n - 1)

def printQueen():
    for i in range(8):
        print(pos[i], end=" ")
    print()

def queen(i):
    cnt = 0
    for j in range(n):
        if  flag_a[j] == False and flag_b[i + j] == False and flag_c[i - j + (n - 1)] == False:
            pos[i] = j
            if i == n - 1:
                # printQueen()
                cnt += 1
            flag_a[j] = flag_b[i + j] = flag_c[i - j + (n - 1)] = True
            cnt += queen(i + 1)
            flag_a[j] = flag_b[i + j] = flag_c[i - j + (n - 1)] = False
    return cnt

print(queen(0))

# n = int(input())

# pos = [False] * n

# def is_check(i, j):
#     flag = 1
#     for k in range(i):
#         if pos[k] == j or abs(pos[k] - j) == abs(k - i):
#             flag = 0
#     return flag

# def queen(i):
#     cnt = 0
#     for j in range(n):
#         if is_check(i, j):
#             pos[i] = j
#             if i == (n - 1):
#                 cnt += 1
#             else:
#                 cnt += queen(i + 1)
#     return cnt

# print(queen(0))