####### 에라토스테네스의 체: 특정 구간까지 소수가 몇 개인지 찾아낼 때 유용한 알고리즘! ########

n = 100

prime = [True]*101
prime[0] = prime[1] = False
for i in range(2, int(n**0.5), +1):
    if prime[i]:
        for j in range(i*i, n+1, i):
            prime[j] = False

for i in range(2, len(prime)):
    if prime[i]:
        print(i, end=" ")


# 특정 수가 소수인지 아닌지 판별할 때는 일반적인 소수 찾기 방식을 쓰면 된다.