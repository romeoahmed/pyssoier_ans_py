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
@File    :   1071.py
@Time    :   2023/08/16 16:35:47
@Author  :   romeoahmed 
@Version :   1.0
@Desc    :   None
"""

matches = (6, 2, 5, 5, 4, 5, 6, 3, 7, 6)
for i in range(112):
    if i < 10:
        if matches[i] == 6:
            print(i)
    elif 10 <= i < 100:
        x = i // 10
        y = i % 10
        if matches[x] + matches[y] == 6:
            print(i)
    else:
        x = i // 100
        y = (i // 10) % 10
        z = i - 100 * x - 10 * y
        if matches[x] + matches[y] + matches[z] == 6:
            print(i)
