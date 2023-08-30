"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

nums = tuple(map(int, input().split()))

count = nums_sum = 0
max = min = nums[0]
for i in nums:
    count += 1
    nums_sum += i
    if i > max:
        max = i
    elif i < min:
        min = i
mean = nums_sum / count

print(f"{min} {max} {mean:.3f}")
