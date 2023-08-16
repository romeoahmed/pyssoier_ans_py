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

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1045.py
@Time    :   2023/08/16 15:20:43
@Author  :   romeoahmed 
@Version :   1.0
@Desc    :   None
"""

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

print("%d %d %.3f" % (min, max, mean))
