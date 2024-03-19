"""
SECRET SANTA

Given a list of players, pair up players so that:

1. Each player gives a gift once
2. Each player receives a gift once
3. No player gives a gift to themselves
4. Selection is random

Input: ['Valentina', 'Jorge', 'Luis', 'Miguel', 'Sofia']
Output: [['Valentina', 'Jorge'], ['Jorge', 'Luis'], ['Luis', 'Miguel'], ['Miguel', 'Sofia'], ['Sofia', 'Valentina'
"""

import random


def secret_santa(players):
    pairs = []

    gives = players.copy()
    recives = players.copy()

    while gives:
        giver = random.choice(gives)
        reciver = random.choice(recives)

        if giver != reciver:
            pairs.append([giver, reciver])
            gives.remove(giver)
            recives.remove(reciver)

    return pairs


if __name__ == "__main__":
    players = ["Valentina", "Jorge", "Luis", "Miguel", "Sofia"]

    pairs = secret_santa(players)
    print(pairs)
