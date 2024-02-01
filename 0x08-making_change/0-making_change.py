#!/usr/bin/python3
"""0-making_change Module"""


def makeChange(coins, total):
    """Returns the minimum number of
    coins needed to get the total,"""
    if total <= 0:
        return 0
    rem = total
    coins_count = 0
    coins_idx = 0
    sorted_conins = sorted(coins, reverse=True)
    n = len(coins)
    while rem > 0:
        if coins_idx >= n:
            return -1
        if rem - sorted_conins[coins_idx] >= 0:
            rem -= sorted_conins[coins_idx]
            coins_count += 1
        else:
            coins_idx += 1
    return coins_count
