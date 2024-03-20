import sys
# 도수 정렬 시간복잡도 : O(N)
# 메모리 계산은 sys.getsizeof() 10,000,000길이의 리스트는 약 80MB필요
n = int(sys.stdin.readline())
f = [0]*10001
for _ in range(n):
    f[(int(sys.stdin.readline()))] += 1

def counting_sort():
    
    for i in range(10001):
        if f[i] > 0:
            for j in range(f[i]):
                print(i)

    # for i in range(1, 10001):
    #     f[i] += f[i-1]
    # for i in range(n-1, -1, -1):
    #     f[arr[i]] -= 1
    #     b[f[arr[i]]] = arr[i]
        # for i in range(n):
        #     arr[i] = b[i]

counting_sort()
