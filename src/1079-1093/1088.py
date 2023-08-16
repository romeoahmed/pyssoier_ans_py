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
@File    :   1088.py
@Time    :   2023/08/16 17:55:00
@Author  :   romeoahmed 
@Version :   1.0
@Desc    :   None
"""

def getPerfectNum(n):
    perfect_nums = []
    for i in range(2, n + 1):
        total = 0
        for j in range(1, i):
            if i % j == 0:
                total += j
        if total == i:
            perfect_nums.append(i)
    return perfect_nums

n = int(input())
for i in getPerfectNum(n):
    print(i)
