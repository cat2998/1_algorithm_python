a, b = map(str, input().split())
a_str = ""
for c in reversed(a):
    a_str += c
b_str = ""
for c in reversed(b):
    b_str += c
print(max(int(a_str), int(b_str)))