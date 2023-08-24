"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fact(x, a = 1):
    if x == 0:
        return 1
    elif x == 1:
        return a
    else:
        return fact(x - 1, a * x)

n = int(input())
s = 0
for i in range(1, n + 1):
    s += fact(i)

print(s)
