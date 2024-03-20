T = int(input())

cnt = 0
NUMBER_LIST = [True]*(10001)
NUMBER_LIST[0] = NUMBER_LIST[1] = False

prime = [False, False] + [True] * 10000
for i in range(2, int(10001 ** 0.5) + 1):
    if prime[i]:
        for j in range(i * i, 10001, i):
            prime[j] = False
prime_numbers = [i for i in range(10001) if prime[i]]

for _ in range(T):
    num = int(input())

    for i in range(num//2, 0, -1):

        if i in prime_numbers:
            if num - i in prime_numbers:
                print(i, num-i)
                break