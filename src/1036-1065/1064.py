"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n = int(input())
sum = 0
tmp = 1

for i in range(1, n + 1):
    tmp *= i
    tmp %= 1000000

    sum += tmp
    sum %= 1000000

print(sum)
