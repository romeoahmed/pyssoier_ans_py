"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

odd_sum = even_sum = 0
for i in range(1, int(input()) + 1):
    if i % 2 != 0:
        odd_sum += i
    else:
        even_sum += i

print(even_sum, odd_sum)
