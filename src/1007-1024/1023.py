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
@File    :   1023.py
@Time    :   2023/08/16 13:36:33
@Author  :   romeoahmed 
@Version :   1.0
@Desc    :   None
"""

l = list(map(int, input().split()))
for i in range(len(l)):
    if i == 0:
        l[i] //= 3
        l[-1] += l[i]
        l[i+1] += l[i]
    elif i == len(l) - 1:
        l[i] //= 3
        l[0] += l[i]
        l[i-1] += l[i]
    else:
        l[i] //= 3
        l[i+1] += l[i]
        l[i-1] += l[i]

for j in l:
    print("%5d" % j, end="")
