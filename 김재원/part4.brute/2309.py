import sys


def input():
    return int(sys.stdin.readline())


# dwarves = [int(input()) for _ in range(9)]
# total = sum(dwarves)
# diff = total-100

# for i in range(8):
#     temp = dwarves.pop(i)
#     if diff - temp in dwarves:
#         dwarves.remove(diff - temp)
#         break
#     else:
#         dwarves.insert(i,temp)

# [print(dwarf) for dwarf in sorted(dwarves)]


def dotori_sum(idx, ans=[]):
    if idx == len(dwarves):
        if sum(ans) == 100 and len(ans) == 7:
            for dwarf in sorted(ans):
                print(dwarf)
            exit()
        return

    ans.append(dwarves[idx])
    dotori_sum(idx + 1, ans)

    ans.pop()
    dotori_sum(idx + 1, ans)


dwarves = [int(input()) for _ in range(9)]
dotori_sum(0)
