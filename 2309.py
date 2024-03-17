import sys

arr = []
for _ in range(9):
    arr.append(int(sys.stdin.readline()))


ans = []
cnt = 0
def search(n):
    global cnt
    if cnt >= 1:
        return

    if len(ans) == 7:
        if sum(ans) == 100:
            ans.sort()
            for i in ans:
                print(i)
            cnt += 1
            return
    if n >= 9 or len(ans)>7:
        return
    
    ans.append(arr[n])
    search(n+1)
    ans.pop()

    search(n+1)

search(0)
