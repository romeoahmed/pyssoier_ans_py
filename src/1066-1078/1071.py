"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

matches = (6, 2, 5, 5, 4, 5, 6, 3, 7, 6)
for i in range(112):
    if i < 10:
        if matches[i] == 6:
            print(i)
    elif 10 <= i < 100:
        x = i // 10
        y = i % 10
        if matches[x] + matches[y] == 6:
            print(i)
    else:
        x = i // 100
        y = (i // 10) % 10
        z = i - 100 * x - 10 * y
        if matches[x] + matches[y] + matches[z] == 6:
            print(i)
