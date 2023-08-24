"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

num = int(input())

reversedNum = 0
while num != 0:
    reversedNum *= 10
    reversedNum += num % 10
    num //= 10

print(reversedNum)
