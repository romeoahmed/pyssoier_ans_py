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
@File    :   1048.py
@Time    :   2023/08/16 15:27:37
@Author  :   romeoahmed 
@Version :   1.0
@Desc    :   None
"""

num = input()
num_new = ""

for i in range(len(num) - 1, -1, -1):
    num_new += num[i]

num_new = int(num_new)
print(num_new)
