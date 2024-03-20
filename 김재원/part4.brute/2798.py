from itertools import combinations
import sys


def input():
    return sys.stdin.readline()


# N, M = map(int, input().split())
# cards = list(map(int, input().split()))
# closest_sum = 0

# for i in range(N):
#     for j in range(i + 1, N):
#         for k in range(j + 1, N):
#             current_sum = cards[i] + cards[j] + cards[k]

#             if current_sum <= M and current_sum > closest_sum:
#                 closest_sum = current_sum

# print(closest_sum)


# N, M = map(int, input().split())
# nums = list(map(int, input().split()))
# closest_sum = 0

# for cards in combinations(nums, 3):
#     sum_num = sum(cards)
#     if sum_num <= M and closest_sum < sum_num:
#         closest_sum = sum_num
# print(closest_sum)
# 다 ans[]에 넣고 max(ans) but smaller than 'm'하면 되지않을까??


def blackjack(cards, m, index=0, current_sum=0, count=0):
    if count == 3 or index >= len(cards):
        return current_sum if count == 3 and current_sum <= m else 0

    # 현재 카드를 선택하는 경우
    with_card = blackjack(cards, m, index + 1,
                          current_sum + cards[index], count + 1)

    # 현재 카드를 선택하지 않는 경우
    without_card = blackjack(cards, m, index + 1, current_sum, count)

    return max(with_card, without_card)


n, m = map(int, input().split())
cards = list(map(int, input().split()))

print(blackjack(cards, m))
