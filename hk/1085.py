x, y, w, h = tuple(map(int, input().split()))

ans1 = min(w-x,h-y)
ans2 = min(x, y)

print(min(ans1, ans2))