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
@File    :   1033.py
@Time    :   2023/08/16 14:01:50
@Author  :   romeoahmed 
@Version :   1.0
@Desc    :   None
"""

height = float(input())
weight = float(input())
bmi = weight / (height ** 2)

if bmi < 18.5:
    situation = "偏瘦"
elif 18.5 <= bmi < 25:
    situation = "正常"
elif 25 <= bmi < 30:
    situation = "偏胖"
elif 30 <= bmi < 35:
    situation = "肥胖"
elif 35 <= bmi < 40:
    situation = "重度肥胖"
else:
    situation = "极度肥胖"

print("%.1f" % bmi)
print(situation)
