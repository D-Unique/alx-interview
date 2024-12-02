#!/usr/bin/python3
"""Making Change."""
"""Athor: Unigwe Emmanuel"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values,determine
    the fewest number of coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0

    coins = sorted(coins, reverse=True)
    num_coins = 0
    remaining_total = total

    for coin in coins:
        if remaining_total <= 0:
            break
        # Use as many of the current coin as possible
        count = remaining_total // coin
        num_coins += count
        remaining_total -= coin * count

    # Check if the total was met
    if remaining_total == 0:
        return num_coins
    return -1
