"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

x = int(input())

factors = []
for i in range(1, x):
    if x % i == 0:
        factors.append(i)

print(*factors, sep="\n")
