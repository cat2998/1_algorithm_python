n, m = tuple(map(int, input().split()))

def gcp(x, y):
    if x % y != 0:
        return gcp(y, x%y)
    else:
        return y
    
print(gcp(n, m))
