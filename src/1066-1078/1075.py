"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n = int(input())
nums = tuple(map(int, input().split()))

max_num_index = 0
for index, value in enumerate(nums):
    if nums[max_num_index] < value:
        max_num_index = index

print(max_num_index + 1)
