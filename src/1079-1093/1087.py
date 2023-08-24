"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def bubbleSort(arr, length):
    for i in range(1, length):
        for j in range(length - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

length = int(input())
nums = list(map(int, input().split()))
sorted_nums = bubbleSort(nums, length)
print(*sorted_nums, sep=" ")
