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

t = int(input())
v = (25000 / t) * 3.6

if 100 < v < 120:
    situation = "超过规定时速且不足20%"
elif 120 <= v < 150:
    situation = "超过规定时速20%以上且不足50%"
elif 150 <= v < 170:
    situation = "超过规定时速50%以上且不足70%"
elif v >= 170:
    situation = "超过规定时速70%以上"
else:
    situation = "正常"

print(round(v, 1))
print(situation)
