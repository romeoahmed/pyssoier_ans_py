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
@File    :   1093.py
@Time    :   2023/08/16 18:07:18
@Author  :   romeoahmed 
@Version :   1.0
@Desc    :   None
"""

def isPrimeNum(n):
    if (n == 2) or (n == 3):
        return True
    elif (n % 6 != 1) and (n % 6 != 5):
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if (n % i == 0) or (n % (i + 2) == 0):
            return False
    return True

for n in range(6, 101, 2):
    for i in range(2, n // 2 + 1):
        if isPrimeNum(i) and isPrimeNum(n - i):
            print(n, "=", i, "+", n - i, sep="")
            break