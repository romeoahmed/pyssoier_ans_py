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
@File    :   1058.py
@Time    :   2023/08/16 15:42:28
@Author  :   romeoahmed 
@Version :   1.0
@Desc    :   None
"""

def fact(x, a = 1):
    if x == 0:
        return 1
    elif x == 1:
        return a
    else:
        return fact(x - 1, a * x)

n = int(input())
s = 0
for i in range(1, n + 1):
    s += fact(i)

print(s)
