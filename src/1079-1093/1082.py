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
@File    :   1082.py
@Time    :   2023/08/16 17:26:38
@Author  :   romeoahmed 
@Version :   1.0
@Desc    :   None
"""

from math import sqrt
l1, l2, l3, l4, l5 = map(float, input().split())

p1 = (l1 + l2 + l5) / 2
p2 = (l3 + l4 + l5) / 2
s = sqrt(p1*(p1-l1)*(p1-l2)*(p1-l5)) + sqrt(p2*(p2-l3)*(p2-l4)*(p2-l5))

print("%.2f" % s)
