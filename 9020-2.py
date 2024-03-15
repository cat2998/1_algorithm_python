####### 에라토스테네스의 체 ########

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
