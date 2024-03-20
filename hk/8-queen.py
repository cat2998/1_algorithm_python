pos = [0]*8
flag_a = [False]*8
#flag_b = [False]*15
#flag_c = [False]*15

def put():
    for j in range(8):
        for i in range(8):
            print('⬛️' if pos[i] == j else 'ㅁ', end=" ")
        print()
    print('-------------------------------')
def set(i):
    for j in range(8):
        if (not flag_a[j]):
            pos[i] = j
            flag_a[j] = True
            print(flag_a)
            if i == 7:
                put()
            else:
                set(i+1)
                flag_a[j] = False

set(0)