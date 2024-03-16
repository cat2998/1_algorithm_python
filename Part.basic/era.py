a = list(range(0, 101))
discr = int(len(a)**(1/2))+1

for i in range(2, discr):
    if a[i] != False:
        for j in range(i**2, 101, i):
            a[j] = False

f = [i for i in a if i != False]
f.remove(1)
print(f)
