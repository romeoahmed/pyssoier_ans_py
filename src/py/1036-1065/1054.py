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
@File    :   1054.py
@Time    :   2023/08/16 15:34:35
@Author  :   romeoahmed 
@Version :   1.0
@Desc    :   None
"""

m, n = map(int, input().split())
facts_m = []
facts_n = []

for i in range(1, m + 1):
    if m % i == 0:
        facts_m.append(i)
for i in range(1, n + 1):
    if n % i == 0:
        facts_n.append(i)

result = 1
for i in facts_m:
    if i > result and i in facts_n:
        result = i

print(result)
