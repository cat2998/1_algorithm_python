n = int(input())

def Factorial(x):
    if x > 1:
        return x * Factorial(x-1)
    else:
        return 1
    
ans = Factorial(n)

print(ans)