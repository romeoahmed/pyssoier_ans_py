"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n = int(input())
nums = input().split()

nums_new = []
for i in range(1, n):
    nums_new.append(nums[i])
nums_new.append(nums[0])

print(*nums_new, sep=" ")
