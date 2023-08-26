"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def getFactors(n):
    factors = [1]
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            factors.append(i)
            factors.append(int(n / i))
    return factors

def getAmiableNums():
    for i in range(2, 300):
        for j in range(2, 300):
            if sum(getFactors(i)) == j and sum(getFactors(j)) == i and i != j:
                return [i, j]

nums = getAmiableNums()
print(*nums)
