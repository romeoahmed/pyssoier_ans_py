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
@File    :   1035.py
@Time    :   2023/08/16 14:03:31
@Author  :   romeoahmed 
@Version :   1.0
@Desc    :   None
"""

x = int(input())
k = x // 4
y = x % 4

if y == 0:
    m = n = 0
elif y == 1:
    m = 0
    n = 1
    k -= 1
elif y == 2:
    m = 1
    n = 0
    k -= 1
else:
    m = n = 1
    k -= 2

print(m, "\n", n, "\n", k, sep="")
