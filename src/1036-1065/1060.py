"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sqrt, floor

def isSquareNum(n):
    root = sqrt(n)
    return root == floor(root)

for a in range(1, 10):
    for b in range(1, 10):
        num = 1000 * a + 100 * a + 10 * b + b
        if isSquareNum(num):
            print(num)
