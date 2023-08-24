"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

x = int(input())
k = x // 4
y = x % 4

if y == 0:
    m = n = 0
elif y == 1:
    m = 0
    n = 1
    k -= 1
elif y == 2:
    m = 1
    n = 0
    k -= 1
else:
    m = n = 1
    k -= 2

print(m, "\n", n, "\n", k, sep="")
