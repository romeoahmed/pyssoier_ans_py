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
@File    :   1060.py
@Time    :   2023/08/16 15:56:17
@Author  :   romeoahmed 
@Version :   1.0
@Desc    :   None
"""

from math import sqrt, floor

def isPerfectSquare(x):
    y = floor(sqrt(x))
    return x == y ** 2

for a in range(1, 10):
    for b in range(1, 10):
        num = 1000 * a + 100 * a + 10 * b + b
        if isPerfectSquare(num):
            print(num)
