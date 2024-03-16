n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))


def bubble_sort():
    for i in range(n-1):
        #교환 횟수 0 초기화
        exchng = 0
        for j in range(n-1, i, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                # 교환 횟수 증가
                exchng += 1
        # 교환한 적 없으면 정렬 끝
        if exchng == 0:
            return

# 마지막 교환을 기준으로 버블 정렬
def bubble_sort2():
    k = 0
    while k < n-1:
        last = n-1
        for i in range(n-1):
            for j in range(n-1, i, -1):
                if arr[j] < arr[j-1]:
                    arr[j-1], arr[j] = arr[j], arr[j-1]
                    last = j
        k = last

# 셰이커 정렬
def bubble_sort3():
    left = 0
    right = n-1
    last = right
    while left < right:
        for i in range(right, left, -1):
            if arr[i] < arr[i-1]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                last = i

        left = last

        for i in range(left, right):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                last = i

        right = last
            
bubble_sort3()

for i in arr:
    print(i)