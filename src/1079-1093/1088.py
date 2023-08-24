"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def getPerfectNum(n):
    perfect_nums = []
    for i in range(2, n + 1):
        total = 0
        for j in range(1, i):
            if i % j == 0:
                total += j
        if total == i:
            perfect_nums.append(i)
    return perfect_nums

n = int(input())
print(*getPerfectNum(n), sep="\n")
