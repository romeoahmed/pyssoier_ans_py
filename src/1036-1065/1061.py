"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

for i in range(101):
    for j in range(101):
        for k in range(101):
            if i + j + k == 100 and 5 * i + 3 * j + k / 3 == 100 and k % 3 == 0:
                print(i, j, k, sep=" ")
