"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n = int(input())
win_combinations = (("Rock", "Scissors"), ("Scissors", "Paper"), ("Paper", "Rock"))
results = []

for i in range(n):
    a, b = input().split()

    if a == b:
        result = "Tie"
    elif (a, b) in win_combinations:
        result = "Player1"
    else:
        result = "Player2"
    results.append(result)

print(*results, sep="\n")
