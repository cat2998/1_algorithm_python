t = int(input())
for i in range(t):
    score = input()
    o_num = 0
    result = 0
    for s in score:
        if (s == 'O'):
            o_num += 1
            result += o_num
        else:
            o_num = 0
    print(result)