"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

for i in range(1, 10):
    for j in range(10):
        for k in range(10):
            num = 100 * i + 10 * j + k
            if num == i ** 3 + j ** 3 + k ** 3:
                print(num)
