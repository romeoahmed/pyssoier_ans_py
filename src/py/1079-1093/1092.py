"""
Copyright 2023 Romeo Ahmed <ahmedorqwn@gmail.com>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@File    :   1092.py
@Time    :   2023/08/16 18:03:54
@Author  :   romeoahmed 
@Version :   1.0
@Desc    :   None
"""

def getFactors(n):
    factors = [1]
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            factors.append(i)
            factors.append(int(n / i))
    factors.sort()
    return factors

def getAmiableNums():
    for i in range(1, 300):
        for j in range(1, 300):
            if sum(getFactors(i)) == j and sum(getFactors(j)) == i and i != j:
                return [i, j]

nums = getAmiableNums()
print(nums[0], nums[1])
