num = 1

for _ in range(3):
    n = int(input())
    num = num*n

numlist = list(str(num))

for i in range(10):
    print(numlist.count(str(i)))