import sys

n, m = map(int, sys.stdin.readline().split())
tree_list = list(map(int, sys.stdin.readline().split()))

def slice_tree(center):
    sum = 0
    for t in tree_list:
        if center < t:
            sum += t - center
    if sum >= m:
        return 1
    return 0

tree_list.sort()

flag = 0
min_m = 0
max_m = tree_list[n - 1]
result = 0

while True:
    center = (min_m + max_m) // 2
    if slice_tree(center):
        result = max(result, center)
        min_m = center + 1
    else:
        max_m = center - 1
    if max_m < min_m:
        break

print(result)

# for i in range(max_m, 1, -1):
#     sum = 0
#     for t in tree_list:
#         if i < t:
#             sum += t - i
#     if sum >= m:
#         print(i)
#         break