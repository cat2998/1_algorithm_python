import sys


def input():
    return sys.stdin.readline().strip()


ln = int(input())
dict = {}
for i in range(ln):
    n = input()
    dict[n] = len(n)

sorted_words = sorted(dict.items(), key=lambda x: (x[1], x[0]))
for word in sorted_words:
    print(word[0])
