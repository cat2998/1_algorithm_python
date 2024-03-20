m, n = map(int, input().split())
t = int(input())
m_list = [0, m]
n_list = [0, n]
max_m = 0
max_n = 0
for i in range(t):
    a, b = map(int, input().split())
    if a == 0:
        n_list.append(b)
    else:
        m_list.append(b)
m_list.sort()
n_list.sort()
for i in range(len(m_list) - 1):
    max_m = max(max_m, m_list[i + 1] - m_list[i])
for i in range(len(n_list) - 1):
    max_n = max(max_n, n_list[i + 1] - n_list[i])
print(max_m * max_n)