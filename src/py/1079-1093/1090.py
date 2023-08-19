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
@File    :   1090.py
@Time    :   2023/08/16 18:00:32
@Author  :   romeoahmed 
@Version :   1.0
@Desc    :   None
"""

a, b, c = map(float, input().split())

max = lambda a, b, c: (a if a > c else c) if a > b else (b if b > c else c)
m = max(a, b, c) / (max(a + b, b, c) * max(a, b, b + c))

print("%.3f" % m)
