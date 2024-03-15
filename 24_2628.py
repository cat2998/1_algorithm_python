m, n = map(int, input().split())
t = int(input())
m_list = list(True for i in range(m + 1))
n_list = list(True for i in range(n + 1))
for i in range(t):
    a, b = map(int, input().split())
    if a == 0:
        n_list[b] = False
    else:
        m_list[b] = False
max_m = 0
max_n = 0
cnt = 0
for i in range(1, len(m_list)):
    cnt += 1
    if m_list[i] == False or i == len(m_list) - 1:
        max_m = max(max_m, cnt)
        cnt = 0
cnt = 0
for i in range(1, len(n_list)):
    cnt += 1
    if n_list[i] == False or i == len(n_list) - 1:
        max_n = max(max_n, cnt)
        cnt = 0
print(max_m * max_n)